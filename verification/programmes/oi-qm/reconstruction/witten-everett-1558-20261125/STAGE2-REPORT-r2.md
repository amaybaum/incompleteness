# #1558 Stage 2 — Can OI provide a structural resolution of the quantum measurement problem?

(Revision r2: STAGE2-REPORT.md with review corrections R1–R7 applied; STAGE2-REPORT.md is unchanged.)

## Covering summary

Paper-only, read-only. Built on the accepted Stage 1 report (R2 and R5 in particular). Pin
`e2e2a623265187a28ebec604ab8bcc672742888f`. No premise is proposed or reinterpreted. Posit (iv),
Axiom 1 and the Definition are taken as they stand.

**Organizing frame (owner).** Three levels of explanation, assessed separately:
- **Ontological:** why reality and records are definite.
- **Operational:** why realizable measurements show quantum behaviour (interference,
  incompatibility, entanglement).
- **Statistical:** why outcomes obey the Born rule and quantum state update.

Success at one level does not carry to the others.

**Two questions, evaluated separately.**
- **Resolving the measurement problem:** a definite ontology with definite outcomes that reproduces
  quantum predictions without collapse. This is the Bohmian strategy, which can succeed even if some
  quantum structure stays postulated.
- **Deriving quantum mechanics:** why quantum structure and its probability rules emerge from OI's
  principles.

**Three reconstruction endpoints** (none reached):
- (i) quantum operations added as a premise: a conditional quantum model;
- (ii) quantum operations derived from the substratum: a physical reconstruction of operational
  quantum structure;
- (iii) complex kinematics and probability rules also derived: a stronger foundational
  reconstruction.

**Three tiers of the current position.**
- (1) **Trivial:** a classical stochastic theory needs no collapse. This holds for OI's stated
  observer interface.
- (2) **Established:** definite reversible dynamics is compatible with supplied finite quantum
  statistics. Two constructions with different inputs show this (Section 2.2).
- (3) **Not achieved:** a derivation of genuinely quantum measurement behaviour from OI's principles.

Verified in this report: the principal identified obstruction is (3), not the absence of a theory of
knowing (Sections 4.1–4.2, 5).

**Owner's hypothesis, evaluated rather than assumed.** If all three levels can be established
without a theory of subjective knowing, OI gives a substantive structural resolution of the physical
measurement problem.
- The antecedent is not met today: the operational and statistical levels are not established from
  OI's principles.
- No step identified depends on a theory of knowing.
- Section 5 assesses what each reconstruction endpoint would deliver for each of the two questions.

### Verdicts by level

**Ontological level: definite configurations by premise; records need more.**
- **(a) Definite configuration.** The detector, like every subsystem, always occupies a definite
  configuration. OI's ontology is a set of configurations evolved by a bijection (Definition,
  Main.md:42; determinism A2, Substratum.md:94; single trajectory, Substratum.md:465). This is a
  premise of the same kind as Bohmian positions or 't Hooft's ontological states.
- **(b) Encoding.** That the configuration encodes the outcome needs a record-forming interaction.
- **(c) Accessibility.** That the record stays accessible for later comparison needs record-retaining
  dynamics.
- Only (a) follows from the ontology. For a native apparatus, (b) and (c) are physical-sourcing
  questions that the corpus records as NOT PASSED
  (`repeatable-measurement-feasibility-20261118/DECISION.md`:3).
- Reversibility keeps the information of a record in the global state. It does not keep the record
  at a readable location (Main.md:74).
- **Established compatibility (tier 2).** Every finite stochastic law has a finite reversible
  realization (kernel: `S_imp_D`, within `finite_horizon_equivalence`). Every finite action-labelled
  family, double-slit settings included, has one too (paper proof, Main.md:490, 694).
- The realization is per law and per horizon. No fixed finite realization reproduces even one qubit
  exactly (Main.md:496, 568).
- Registration needs no knower: a detector is a registering locus (Main.md:36).

**Operational level: not derived; obstructed in the stated architecture; conditional beyond it.**
- **Physically sourced observer theory** (`obsTheory = permTheory`). Every available operation
  preserves nonnegative entries, and there are no phases and no dense unitary control (kernel:
  `obsTheory_nonnegBounded`, `frozen_sourcing_verdict`, `nonnegBounded_verdict`), for every
  microscopic rule (`sourcing_rule_independent`).
- **Larger monomial theory** (`substratumClass`, with complex phases as a stated intervention
  principle). It lacks composite unitary control (kernel: `substratumGen_not_control`) and fails
  elementary drivability (kernel: `substratumClass_not_drivesElementary`). Its effects are all
  diagonal, so coherence present in an input never affects an outcome probability (derivation,
  Stage 1 R5; not a kernel theorem).
- In these classes "no collapse is needed" is tier (1).
- Interference from the substratum dynamics is stated open: Main.md:694, Substratum.md:463, and
  [unreviewed draft ledger] row B-P4-MEAS-5.
- **Sufficient conditions (kernel: `substratum_plus_control_qm`).** Exact finite endomorphic
  operational QM, on the system and every positive composite, holds on every nonempty finite carrier
  for any implementation class that:
  - extends the substratum class;
  - is structurally closed (architecture, context stability, label invariance, dagger stability);
  - drives the elementary transitions (`DrivesElementary`: transition flows at every real time for
    every pair, swaps and quarter phases, at every carrier).

  This holds within complex matrix kinematics taken as given, whose derivation is open
  (Main.md:572).
- **Necessary conditions.** A theory with phases or dense unitary control cannot be
  nonnegativity-bounded (`nonnegBounded_verdict`). Executing a layer flow requires a non-monomial
  admissible operator (`exists_nonMonomial_of_layerFlowExecutable`).
- The programme has retired the equivalence endpoint F1 for the stated architecture
  (`verification/programmes/oi-qm/PROGRAMME.md`:40, :521). The active F2 extension is open.

**Statistical level: not derived.**
- The Born form is part of the definition of `Q_fb` (Main.md:18, 564). Its exponent is not selected
  (Main.md:226, 564).
- The corpus record states: "OI has not yet been shown to derive the Born rule or select the
  physical probability measure"
  (`verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md`:5).
- Lüders update is established only as Bayesian conditioning in the diagonal sector (Main.md:664).
- **Conditioning.** The predictive laws are conditional on available information: records, and
  possibly further information (Stage 1 R2). Conditioning is defined mathematically and needs no
  theory of awareness.
- Which information the quantum weights condition on is open. So are the physical motivation of
  posit (iv), the Born exponent and the measure. None of these open items is shown to depend on a
  theory of knowing.

### Verdicts by question

1. **Definite outcomes.**
   - Tier (1) holds: in the stated observer interface no collapse is needed, as in any classical
     stochastic theory.
   - Tier (2) is established: two constructions realize supplied finite quantum statistics with
     definite reversible dynamics.
     - The intervention dilation realizes supplied finite outcome laws, double-slit settings included,
       with no density matrix stored (Main.md:490, 694).
     - The gluing construction realizes supplied quantum instruments and an initial state as one
       adaptive realization to stated accuracy, with the density matrix stored in a hidden register
       (Main.md:574–590).
   - Tier (3) is not achieved: neither construction derives interference from native dynamics, and
     the stated observer interface cannot produce coherence-sensitive statistics.

2. **Measurement rules.**
   - Born rule and basis selection: Born form definitional; exponent and measure open; the
     configuration basis is privileged by premise.
   - State update: conditioning in the diagonal sector; Kraus update only under the completion
     conditions.
   - Repeatability: a native record that stays readable is not sourced (NOT PASSED). Reversibility
     preserves record information globally, not at a location.
   - Observer agreement: a joint law exists for the ordinary Wigner's friend. Agreement on comparing
     records also needs the records to encode the same outcome and stay accessible. Genuinely quantum
     extended protocols are not modelled.
   - Contextuality: inherited only with supplied data; the native fragment is simplex-embeddable
     under named hypotheses (research record).
   - Bell: ceiling of 2 for a screened local completion; the adopted branch needs ontic parameter
     dependence; H-Bell open.

   The exact missing mechanisms are listed in the status table (Section 3.8).

3. **Observation and knowledge.**
   - Definiteness of configurations and the operation classes need no notion of knowing.
   - The stochastic weights depend on conditioning on available information (R2). This is
     dependence on information, not on a theory of knowing.
   - The closed-eyes detector case separates registration (ontological) from learning (conditioning)
     in OI's models. So does a classical theory: the case does not discriminate OI, and it says
     nothing about why the registered statistics are quantum.
   - **Local friendliness (conditional).** IF an OI completion reproduces the local-friendliness-
     violating correlations, satisfies the precise absoluteness condition (including readback
     consistency) and retains no-superdeterminism for that experiment, THEN it must violate the
     theorem's Locality condition. None of the antecedents is established. OI's adopted ontic-
     parameter-dependent Bell branch indicates a direction but does not establish the completion.

4. **Structural resolution.**
   - **Resolving the measurement problem.** Per-experiment compatibility (tier 2) is established.
     A resolution by OI's own physical substratum, with one dynamics reproducing quantum predictions,
     is not established.
     - Under endpoint (i), paired with a definite realization of the added operations, it would be
       a Bohmian-type resolution with postulated quantum structure.
     - Under (ii) or (iii) it would also be a derivation.
   - **Deriving QM.** Not established. Endpoint (ii) requires native sourcing of the coherent
     resource (F2, open). Endpoint (iii) additionally requires deriving the complex kinematics and the
     probability rules (open).

5. **Distinctiveness** (formal architecture and literature checked).
   - Distinctive and negative: a kernel-checked proof that the configuration-level observer theory,
     for every microscopic rule, is nonnegativity-bounded (`sourcing_rule_independent`). This locates
     what an embedded-observer explanation must add.
   - The positive representation equivalence is exact but universal: it includes Markov chains.
   - The definite-ontology account of outcomes is shared with Bohm, 't Hooft and Barandes.
   - OI's Bell placement (measurement independence kept, ontic parameter dependence) differs from
     't Hooft's superdeterminism and resembles Bohmian nonlocality.

### Main uncertainties
- External texts were retrieved at abstract level only (Section 1).
- R5's "effects are diagonal" is a derivation from the definitions, not a kernel theorem.
- Whether an extended architecture sources coherence is open; this report does not prejudge it.
- The exact definitions of Bong et al.'s Locality and Absoluteness of Observed Events are
  [background].

### What is NOT shown
- That OI derives quantum interference, the Born rule, contextuality or Bell violation from its
  substratum.
- That OI's physical substratum, with one fixed dynamics, reproduces quantum measurement statistics.
- That OI resolves or dissolves the measurement problem.
- That any of OI's no-collapse statements carry quantum content beyond the operationally classical
  sector, other than through the two compatibility constructions with supplied data.

***

## 1. Sources and pin

**Corpus.**
- Read from pinned objects only, at `e2e2a623265187a28ebec604ab8bcc672742888f`, the head of `main`.
- No later commit is relied on. Line numbers are at the pin unless stated otherwise.
- Main areas read:
  - `papers/Main.md` (§§1.2, 2.1 C2 definition, 3.1–3.4, 4.1–4.5)
  - `papers/Substratum.md` (§§6.3–6.4)
  - `papers/GR.md` (Appendix A)
  - `book/ch01-observation.md`, `book/ch18-beyond.md`, `book/ch19-open-problems.md`,
    `book/appendix-c-objections.md`
  - `verification/programmes/oi-qm/PROGRAMME.md`
  - `verification/lean-mathlib/OIBridge/FrozenSourcing.lean`, `ImplementationLocality.lean`,
    `OperationalAssembly.lean`, `StructuralClosure.lean`, `SubstratumSource.lean`
  - Under `verification/programmes/oi-qm/reconstruction/`: `measurement-record-formation/`,
    `repeatable-measurement-feasibility-20261118/DECISION.md`, `meas-q-20261120/RESULT.md`,
    `born-sel-b-measure-20261104/QB3-EVIDENCE.md`, `oa-1-20261112/STATUS.md`,
    `oa-2-20261112/STATUS.md`, `drafts/unified-ledger-20261114/LEDGER-r9.md`
  - The accepted Stage 1 report.
- No Lean build or computation was run.

**Classification labels.** The briefed classes are kernel theorem, paper proof, conditional
consequence, missing mechanism and open question. Conclusions that rest only on reading or comparing
texts, or on a definition, are labelled **source reading**. That label carries no proof weight.

**Unreviewed draft ledger.** Rows cited from `drafts/unified-ledger-20261114/LEDGER-r9.md` are marked
[unreviewed draft ledger]. The directory is headed "UNREVIEWED — NOT AUTHORITATIVE", and r9 is
pending review. Those rows are cited only where an authoritative source (a paper line, Lean module or
programme record) states the same thing.

**External sources retrieved (arXiv abstract pages).**

| Source | arXiv ID, version | Used for |
|---|---|---|
| Barandes, "The Stochastic-Quantum Correspondence" | 2302.10778v3 | Deflationary account of interference and collapse; wave function demoted |
| 't Hooft, "The Cellular Automaton Interpretation of QM" | 1405.1548v3 | Claims to eradicate the measurement problem; superdeterminism |
| Spekkens, "In defense of the epistemic view... toy theory" | quant-ph/0401052v2 | Epistemic restriction reproduces interference analogues, not Bell or KS |
| Schmid, Selby, Wolfe, Kunjwal, Spekkens | 1911.10386v2 | Generalized noncontextuality is equivalent to simplex embeddability (finite ontic space) |
| Wetterich, "Quantum mechanics from classical statistics" | 0906.4919v2 | Classical ensemble with probabilistic observables and a purity constraint |
| Fuchs, Mermin, Schack, "An Introduction to QBism..." | 1311.5253v1 | QBist contrast |
| Barandes, Hasan, Kagan, "The CHSH Game, Tsirelson's Bound, and Causal Locality" | 2512.18105v1 | Tsirelson bound from causal locality of indivisible processes |
| Frauchiger, Renner | 1604.07422v2 | Extended Wigner's friend no-go |
| Bong et al., "A strong no-go theorem on the Wigner's friend paradox" | 1907.05607v4 (Nat. Phys. 16, 1199 (2020)) | Assumptions: No-Superdeterminism, Locality, Absoluteness of Observed Events |
| Proietti et al., "Experimental test of local observer-independence" | 1902.05080v2 | Six-photon test; violation of the associated inequality by 5 standard deviations |

**Not retrieved, marked [background] where used:** Bohm 1952; GRW 1986; Everett 1957; Nelson 1966;
Wallstrom; Griffiths and Gell-Mann–Hartle on consistent histories; Gleason 1957; Kochen–Specker; PBR
2012. The full texts of the Frauchiger–Renner and Bong et al. papers were not retrieved, including
the exact definitions of (Q), (C), (S), Locality and Absoluteness of Observed Events.

***

## 2. Question 1: definite outcomes

### 2.1 Where definiteness comes from

- **The Definition** (Main.md:42) makes an observation a triple `(S, phi, V)`. `V` is a proper
  subsystem with finitely many distinguishable states.
- **A2** makes `phi` a bijection (Substratum.md:94).
- **Single trajectory.** "A fixed bijection on a finite set has exactly one trajectory from any
  initial state. There is no point at which the trajectory splits" (Substratum.md:465).
- So at every time V occupies one configuration, an element of a set. It is definite by
  construction. This is claim (a).
- This is a premise of the ontology, as for Bohmian positions or 't Hooft's ontological basis
  [background]. It is not derived from anything weaker.
- **What does not follow from the ontology.**
  - (b) That V's configuration encodes the outcome of an interaction with a system. This needs a
    record-forming coupling.
  - (c) That the encoded outcome stays accessible for later reading or comparison. This needs
    record-retaining dynamics.
- Reversibility preserves the information of a record in the global state, by injectivity. It does
  not preserve the record at a location: a reversible step can move it. The corpus's C2-structural is
  stated as retention of the information carried by a hidden record. It admits a fast bath that
  "routes the record back within the window", and treats "a record that stays put" as one mechanism
  among others (Main.md:74).
- For a native apparatus, (b) and (c) are recorded as NOT PASSED (Section 3.4).
- **Skeptical reading.** "OI explains definite outcomes" can mean only "OI posits a definite ontology
  and shows it is consistent with record statistics". The second half is substantive (2.2); the
  first is stipulation.

### 2.2 What the corpus establishes about definite ontology and record statistics

- **Finite realization.** Every finite stochastic law on a finite alphabet and horizon has a finite
  reversible deterministic realization.
  - Kernel: `S_imp_D`, assembled in `finite_horizon_equivalence`
    (`verification/lean-mathlib/OIBridge/Equivalence.lean:462`).
  - This includes the record statistics of any fixed finite quantum experiment, given its
    probabilities (Main.md:20, 80 item 3).
- **Interventions: the intervention dilation.** Every finite action-labelled family has one
  realization with permutation instruments, one fixed prior and one bijection (paper proof,
  Main.md:490).
  - It reproduces Leggett–Garg violations, such as `K = 3/2`, because the instruments are invasive
    (Main.md:494; exact probe `lg_comb_probes.py`).
  - It covers the double-slit settings: "every such family has a finite reversible realization with
    one fixed prior, in which the substratum occupies a single configuration at every step"
    (Main.md:694).
  - Its input is the supplied finite outcome law. No density matrix is stored.
- **Quantum envelopes: the gluing construction.** For supplied quantum instruments, an initial state
  and a finite horizon, one finite reversible realization reproduces the adaptive envelope to
  accuracy epsilon (paper proof, Main.md:574–590). Its hidden sector stores the branch density
  matrix.
- **Limits.**
  - No fixed finite realization carries the whole instrument algebra (Main.md:496).
  - No horizon-independent intervened representation exists at fixed dimension (Main.md:502).
  - No fixed finite carrier is exactly operationally equivalent to one qubit's full theory
    (Main.md:568). The factorization half is proved there; the unboundedness is imported.
  - The gluing machinery also realizes non-quantum finite families (Main.md:592), so it does not
    single out quantum statistics.

### 2.3 Three tiers: trivial, established compatibility, unachieved derivation

**Tier (1), trivial (established).** In the stated architecture the available operations are
operationally classical. Two theories must be kept apart.
- **The physically sourced observer theory** `obsTheory = permTheory`:
  - `obsTheory_nonnegBounded` and `permTheory_nonnegBounded` (`FrozenSourcing.lean`): every
    available operation preserves nonnegative entries.
  - `frozen_sourcing_verdict` (`FrozenSourcing.lean:318`): no phases, no dense unitary control.
  - `sourcing_rule_independent` (`FrozenSourcing.lean:295`) and `obsTheory_rule_independent`
    (`SubstratumInterfaceAudit.lean:780`): the verdict does not depend on the microscopic rule.
  - `obs_not_layerFlowExecutable` (`ExecSource.lean:129`): no layer flow.
- **The larger monomial theory** generated by `substratumClass` (operators `permMatrix sigma *
  diagonal d` with complex `d`; the phases are a stated intervention principle, Main.md:598):
  - `substratumGen_not_control` (`StructuralClosure.lean:330`): no composite unitary control on
    `Fin 2`.
  - `substratumClass_not_drivesElementary` (`StructuralClosure.lean`, header "THE RESIDUAL").
  - `coherentLiftClass_eq_substratumClass` (`LiftSource.lean:164`): coherent lifts add nothing beyond
    the monomial class.
  - Stage 1 R5 (derivation from the definitions; not a kernel theorem): every Kraus operator is
    monomial, so every effect is diagonal. Coherence present in an input can be moved and rephased
    but never affects an outcome probability.
- In both theories a "measurement" is classical conditioning. Main.md:664 states that the Lüders rule
  "transcribes Bayesian updating ... for the represented diagonal sector".
- That "no collapse is needed" is then a property of every classical stochastic theory. It does not
  address the quantum content of the measurement problem: the coexistence of definite outcomes with
  interference between alternatives.

**Tier (2), compatibility (established).** Definite reversible dynamics can realize supplied finite
quantum statistics without collapse, by two constructions with different inputs (2.2).
- **Dilation.** Input: supplied finite outcome laws, double-slit settings included. Output: a
  definite reversible realization with no stored density matrix (Main.md:490, 694).
- **Gluing.** Input: supplied quantum instruments and initial state. Output: one adaptive realization
  to the stated accuracy, with the density matrix stored in a hidden register (Main.md:574, 590:
  "Quantum mechanics enters as the instrument data and as the state held in the hidden register").
- Both are existence results per finite experiment. Their dynamics and hidden sector depend on the
  supplied data and grow with it (Main.md:496, 584).
- Neither is OI's physical substratum with its selected rule, and neither derives the statistics.

**Tier (3), derivation (not achieved).** This would need coherence-sensitive statistics — a
non-diagonal effect, or a preparation reaching a superposition — generated by admissible observer
operations on the definite substratum.
- **Corpus status.**
  - "a derivation of the two-slit interference pattern from the substratum dynamics is open"
    (Main.md:694; also Substratum.md:463).
  - "*operational* interference and entanglement predictions require in addition the instrument and
    observable structure of the operational bridge, characterized conditionally and with its
    physical sourcing open" (Main.md:666).
  - The programme frontier is F2, the sourcing of a nonclassical resource by an extended architecture
    (`PROGRAMME.md`:40).
  - Native attempts on record report no sourced coherent instrument:
    - F2-1: no admissible map `Theta*`.
    - PC-1: void, 25 candidates screened.
    - MR-1: stage-1 token `GAP`, provisional
      (`reconstruction/measurement-record-formation/README.md`:35; preregistration §2.3).

**Representation route.** `S <=> D <=> Q_fb` gives a unitary Born representation of any visible law,
but it does not supply tier (3).
- The unitary is the permutation `U_phi`, whose entries are 0 or 1 (Main.md:290, 564).
- The initial state is diagonal, and readout is in the fixed basis at every step (Main.md:14).
- The representation is universal, Markov chains included (Main.md:18).
- The padding theorem shows that "represented" is a disqualified ground for any sourcing claim: every
  unitary on every nonempty finite carrier occurs in some representation (`PROGRAMME.md`:216).
- Relating evolutions are not unique (Main.md:656).
- So the existence of a Hilbert-space representation is not superposition derived from definite
  reality.

### 2.4 Classification (Question 1)

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| Every subsystem occupies a definite configuration (claim (a)) | conditional consequence | Main.md:42; Substratum.md:94, 465 | Definition and A2 (premises; A1 open and not adopted, not needed here) |
| Encoding (b) and later accessibility (c) of an outcome follow from the ontology | open question (not a consequence; native apparatus NOT PASSED) | `repeatable-measurement-feasibility-20261118/DECISION.md`:3 | record-forming and retaining dynamics |
| Reversibility preserves record information globally, not at a location | source reading | Main.md:74 (C2-structural; routing example) | bijective realization |
| Every finite stochastic law has a finite reversible realization | kernel theorem | `S_imp_D`, `finite_horizon_equivalence` (Equivalence.lean:462) | finite alphabet and horizon; realization depends on law and horizon |
| Finite action-labelled families (LG-violating and double-slit included) have one permutation-instrument realization without a stored density matrix | paper proof | Main.md:490, 494, 694 | supplied finite outcome laws; per finite menu and horizon |
| Supplied quantum instruments and state have one adaptive reversible realization to accuracy epsilon | paper proof | Main.md:574–590 | supplied data; density matrix stored; exact-arithmetic hypotheses |
| No fixed finite realization is exactly equivalent to a qubit | paper proof (factorization half); imported unboundedness | Main.md:568 | factorization interface |
| The physically sourced observer theory is nonnegativity-bounded (no phases, no dense control), for every rule | kernel theorem | `obsTheory_nonnegBounded`, `frozen_sourcing_verdict`, `nonnegBounded_verdict`, `sourcing_rule_independent`, `obs_not_layerFlowExecutable` | finite carriers; stated architecture |
| The monomial theory lacks composite unitary control and elementary drivability | kernel theorem | `substratumGen_not_control`, `substratumClass_not_drivesElementary`, `coherentLiftClass_eq_substratumClass` | `Fin 2` for control; class level for drivability |
| Every effect in the monomial class is diagonal | paper proof (Stage 1 R5 derivation from the definitions; not a stated kernel theorem) | `InstAvail` (ImplementationLocality.lean:268), `preservesDiag_conj_of_monomial` | finite carriers |
| "No collapse needed" in these classes is tier (1) | paper proof (this report, from the rows above) | Main.md:664 | stated architecture |
| Interference derived from substratum dynamics (tier 3) | open question | Main.md:666, 694; Substratum.md:463; B-P4-MEAS-5 [unreviewed draft ledger] | — |
| Superposition derived from definite reality (the owner's reversal) | missing mechanism | PROGRAMME.md:40 (F2 open); MR-1 `GAP` provisional | a native, non-monomial, admissible coherent operation |

***

## 3. Question 2: quantum measurement rules

### 3.1 Born rule

- **Today.** In `Q_fb` the Born dictionary `p = |U|^2` is part of the definition (Main.md:18, 564).
- On permutation unitaries every exponent `p > 0` gives the same table, so nothing selects 2
  (Main.md:564; exponent "a frontier item", Main.md:226).
- The record `born-sel-b-measure-20261104/QB3-EVIDENCE.md`:5 states that OI "has not yet been shown
  to derive the Born rule or select the physical probability measure".
- In the stated architecture, outcome probabilities are classical marginals of the hidden prior. For
  constructed realizations that prior is selected by posit (iv) (Main.md:736).
- **If reconstruction succeeds (endpoints (i) or (ii)).**
  - Under the five completion conditions, available families are exactly the normalized Kraus
    instruments (kernel: `exactAll_iff_physical_general`, GeneralCarrier.lean:100).
  - Outcome probabilities then have trace form, but only within complex matrix kinematics "taken as
    given", whose derivation "is open" (Main.md:572).
  - Deriving the trace rule is part of endpoint (iii).
  - Gleason-type routes [background] are cited (Main.md, ref. [54]) but are not developed as an OI
    derivation in any passage traced.

### 3.2 Measurement-basis selection

- **Today.** The configuration basis of V is privileged by the ontology. Every available effect is
  diagonal in it (R5). This answers preferred-basis questions only in the tier-(1) sense: no other
  basis is measurable.
- **If reconstruction succeeds.** Which basis is measured would be fixed by which physically
  available coupling precedes readout. That needs native apparatus formation, which is NOT PASSED:
  - `repeatable-measurement-feasibility-20261118/DECISION.md`:3: "Physical measurement sourcing is
    NOT PASSED".
  - `meas-q-20261120/RESULT.md` summary: physical measurement sourcing not passed; A1 open and not
    adopted.
- Decoherence-based basis selection is not derived in any passage traced. Book ch01:292 hedges it as
  depending "on the interaction and preparation".

### 3.3 Effective state update

- **Today.**
  - Lüders update holds as Bayesian conditioning in the diagonal sector (Main.md:664).
  - A passive internal reader's branch is `rho -> P_o rho P_o`, with law `tr(P_o rho P_o)` (kernel:
    `internal_branch_eq_blockPart`, `internal_outcome_law`, InternalObserver.lean:137, 150; matrix
    kinematics).
  - Within `FiniteOperationalTheory`, the ancilla readout is forced to be local Lüders by spectator
    independence (kernel: `readout_is_localLuders`, OperationalAssembly.lean:658). The rule it starts
    from already fixes the action on products (Main.md:572, rule (e)), so the theorem extends a
    premised form.
- **If reconstruction succeeds.** General Kraus update follows within the given kinematics
  (`exactAll_iff_physical_general`). The update "for noncommuting interventions belongs to that
  algebra", and "its extension to arbitrary coherent density matrices belongs to the operational
  bridge" (Main.md:664).

### 3.4 Repeatability

- **Today.**
  - Reading the same configuration twice, with no intervening change, gives the same value. This
    holds by definition and presupposes (b) and (c) of 2.1.
  - Passive reading of a register is a projection and so idempotent (kernel:
    `internal_branch_eq_blockPart`; matrix kinematics).
  - Reversibility preserves a record's information in the global state (Main.md:74, C2-structural).
    It does not guarantee that the record stays at a readable location between readings.
- **Physical apparatus.**
  - The fixed ring design fails a second use: "At the exact ready signature for a common second
    request, the first result cannot be read from the same four coordinates alone"
    (`repeatable-measurement-feasibility-20261118/DECISION.md`:3).
  - On the published rounded rule, finite confined classes are periodic and erase their records
    (MEAS-Q MQ4; unreviewed derivation in that record).
- **If reconstruction succeeds.** Projective repeatability holds within QM. A native record path that
  survives re-arming is still needed for an OI apparatus.

### 3.5 Observer agreement

- **Today.**
  - Wigner's friend: one joint law whose marginals are both observers' laws, unique given `phi`
    (paper proof, Main.md:698–704).
  - Nested trace-outs agree (GR.md:729–751, Theorems A.1–A.4). Corollary A.3, Hamiltonian
    consistency, is conditional on H-BG and the §3.3 hypotheses.
- **What a single configuration does and does not give.**
  - A single underlying configuration fixes a fact of the matter at each time.
  - It does not make compared records agree. Two observers' records agree on comparison only if each
    encodes the same outcome (b) and stays accessible until compared (c).
  - A faulty or overwritten record disagrees with the configuration it was meant to encode.
  - Agreement is therefore not automatic, even in the operationally classical class.
- **Not established.** "It does not by itself resolve the full Frauchiger–Renner protocol"
  (Main.md:704). Protocols needing a superobserver's coherent operation on friend plus system cannot
  be modelled with the available operations (kernel no-go, 2.3). See 4.4.

### 3.6 Contextuality

- **Today.**
  - Kochen–Specker: in the gluing realization, for `d >= 3` with a KS set, "every deterministic
    account reproducing the exact statistics must assign values contextually" (Main.md:580). The
    statistics are supplied data; this is KS applied [background], not a native derivation.
  - Spekkens noncontextuality "is not claimed" (Main.md:580).
  - Under the OA-2 hypotheses ((H1), H-AR, (H3), (H4), (SP), item (xiv)), the native prepare–measure
    fragment of the affine class is simplex-embeddable (OA-2 Theorem E(b), `oa-2-20261112/STATUS.md`:62;
    research record, agent-reviewed, not adopted).
  - By arXiv:1911.10386, simplex embeddability means a generalized-noncontextual model exists, i.e. a
    classical one.
  - The stated architecture's diagonal-effect theory is simplex-embeddable: map each state to its
    diagonal and each effect to its diagonal vector (this report; follows from R5).
  - A designed reversible classical computer shows an exact preparation-contextual gbit at bounded
    horizons (OA-2 N2.3). Bounded-horizon criteria G0, G1 and G3 therefore do not separate classical
    from quantum.
- **If reconstruction succeeds.** KS and generalized contextuality are inherited from exact QM.

### 3.7 Bell correlations

- **Today.**
  - A screened local completion has `|S_CHSH| <= 2` (paper proof with an exhaustive 16-table check,
    Main.md:370–397).
  - Bare OI realizes PR boxes, so Tsirelson is not selected (Main.md:366).
  - Measurement independence "is retained as a posit about the initial condition, not derived"
    (Main.md:410–416).
  - The adopted branch is ontic parameter dependence with operational no-signalling required
    (Main.md:418).
  - The reference nearest-neighbour graph cannot supply that dependence for wings outside the graph
    cone (Main.md:420–424).
  - The measurement-dependence alternative gives the lower bound `I_ont >= 0.0309` bits
    (Main.md:429–433).
  - H-Bell (i)–(iii) is open (Substratum.md:131–133). `verification/programmes/oi-qm/h-bell/` holds
    only a preregistration.
- **If reconstruction succeeds and H-Bell holds.** Quantum CHSH values become reachable with
  operational no-signalling. Tsirelson selection (BELL-QSET) is a further open obligation (A-BELL,
  [unreviewed draft ledger]; consistent with Main.md:366).

### 3.8 Measurement rules status table

| Rule | Status today | If reconstruction succeeds | Missing mechanism or premise (corpus record) |
|---|---|---|---|
| Born rule | Definitional in `Q_fb`; exponent not selected; physical measure posited by (iv); "not yet shown to derive" | Trace-form probabilities for all Kraus instruments, within complex matrix kinematics taken as given (endpoints (i) and (ii)) | Derivation of the kinematics (Main.md:572); exponent and measure selection (`born-sel-b-measure-20261104/QB3-EVIDENCE.md`); both part of endpoint (iii) |
| Basis selection | Configuration basis privileged by premise; only diagonal effects available (tier 1) | Basis set by the available coupling before readout | Native apparatus or record formation: `repeatable-measurement-feasibility-20261118/DECISION.md` (NOT PASSED); `measurement-record-formation/` (`GAP` provisional); `meas-q-20261120/RESULT.md` |
| State update | Bayesian conditioning, diagonal sector (Main.md:664); passive reading `P_o rho P_o` (kernel); local Lüders readout from spectator independence (kernel) | General Kraus update | Sourcing of non-commuting instruments: F2, `PROGRAMME.md`:40; coherent-input update, "operational bridge" (Main.md:664) |
| Repeatability | Definitional for re-reading one configuration; idempotent passive reading (kernel); record information preserved globally, not at a location (Main.md:74) | Projective repeatability within QM | Native record surviving re-arming (`repeatable-measurement-feasibility-20261118/DECISION.md`); MEAS-Q MQ4 record erasure |
| Observer agreement | Joint law for ordinary Wigner's friend (paper); nested trace-out consistency (paper, partly conditional); agreement on comparison needs encoding and accessibility of records, not automatic | Extended-Wigner protocols computable | Record formation and retention (as above); superobserver coherent operations (unsourced); FR and local-friendliness premise analysis (Main.md:704; appendix-c C.3; open) |
| Contextuality | KS contextuality only with supplied data (Main.md:580); native fragment simplex-embeddable under OA-2 hypotheses (research record); classical gbit at bounded horizons | Inherited from QM | A native non-simplex-embeddable fragment (`oa-2-20261112/STATUS.md`; "Open: G3 for admissible non-affine rules") |
| Bell correlations | CHSH <= 2 for screened local completion; PR boxes in bare OI; adopted branch: ontic parameter dependence; H-Bell open | Quantum CHSH with no-signalling, if H-Bell holds | H-Bell (i)–(iii) (Substratum.md:131–133; `h-bell/round-hb-1-obligation-shape/`, preregistration only); Tsirelson selection (Main.md:366) |

### 3.9 Classification (Question 2)

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| Born form part of `Q_fb` | source reading (definitional) | Main.md:18, 288–290, 564 | fixed-basis class |
| Born exponent not selected | paper proof (construction is exponent-blind) | Main.md:564; probe check 6 | — |
| Born rule or physical measure derived | open question | QB3-EVIDENCE.md:5 | — |
| Kraus instruments iff five conditions | kernel theorem | `exactAll_iff_physical_general` (GeneralCarrier.lean:100) | complex matrix kinematics taken as given; finite carrier |
| Exact finite endomorphic and composite QM from an extension of the substratum class | kernel theorem / conditional consequence | `substratum_plus_control_qm` (StructuralClosure.lean:397) | `ExtendsSubstratum`, `StructurallyClosed`, `DrivesElementary` (flows at all real t for all pairs, swaps, quarter phases, every carrier); nonempty finite carrier; given kinematics |
| Necessary: leave the nonnegativity-bounded class; a non-monomial operator for layer flows | kernel theorem | `nonnegBounded_verdict`; `exists_nonMonomial_of_layerFlowExecutable` (ExecSource.lean:52) | finite carriers |
| Diagonal-sector Lüders = conditioning | paper proof | Main.md:664 | diagonal sector |
| Passive reading `P_o rho P_o` | kernel theorem | `internal_branch_eq_blockPart`, `internal_outcome_law` | matrix kinematics |
| Readout is local Lüders | kernel theorem | `readout_is_localLuders` | `FiniteOperationalTheory` rule (e) |
| Native repeatable apparatus | missing mechanism | `repeatable-measurement-feasibility-20261118/DECISION.md`:3 | fixed ring interface |
| Ordinary Wigner's friend joint law | paper proof | Main.md:698–704 | common joint preparation |
| Agreement on comparison automatic | not established (requires (b) and (c)) | 3.5 | — |
| KS contextuality of deterministic reproductions | conditional consequence | Main.md:580; KS [background] | supplied quantum data, `d >= 3` |
| Native fragment simplex-embeddable | conditional consequence (research record) | OA-2 STATUS:62 | (H1), H-AR, (H3), (H4), (SP), (xiv) |
| Stated architecture's prepare–measure theory simplex-embeddable | paper proof (this report; from R5) | R5; arXiv:1911.10386 | finite carriers, monomial class |
| CHSH <= 2 for screened local completion | paper proof | Main.md:370–397 | conditions (i)–(iv) |
| Measurement independence | posit (source reading) | Main.md:410–416 | — |
| Quantum Bell correlations from OI | open question | Main.md:418, 437; Substratum.md:131–133 | H-Bell |

***

## 4. Question 3: observation versus knowledge

### 4.1 Does definiteness require knowing?

- **No, at the level of premises and operation classes.**
- The Definition is third-person (Main.md:42). Its Lean form reads "the visible readout
  distinguishes states" (`OIRealization.lean:289`; Stage 1 §8.2).
- Axiom 1's locus "asserts no I" (Main.md:36). The text states: "the Definition covers every
  registering locus, and for a detector or a horizon that a registering occurs is a physical fact,
  not an indubitable one" (Main.md:36).
- Stage 1 §8.3 found that no theorem depends on first-person registering.
- What stays unargued is the bridge from the indubitable registering to the physical Definition
  (Stage 1 N3). That concerns Axiom 1's warrant, not definiteness of physical configurations.

### 4.2 Do the weights depend on epistemic conditioning, and does that need a theory of knowing?

- **Dependence on available information: yes.** Stage 1 R2 holds: the observer's predictive laws are
  pushforwards of `mu_prep(. | R)` (`pushforward_identity`, HiddenMemory.lean:83). Further
  information K gives `mu_prep(. | R, K)`.
- Posit (iv) selects "the maximal-entropy invariant measure compatible with the observer's records",
  labelled "a standard but substantive epistemic postulate" (Main.md:736).
- **No dependence on a theory of knowing.** Conditioning is mathematically defined without any
  theory of awareness.
  - Example: before a detector registers, `P(0) = P(1) = 1/2`. Conditional on the detector record
    `R = 0`, `P(0 | R = 0) = 1`.
  - This update is conditional probability on an event, whoever or whatever holds the record.
  - "Epistemic" in OI's laws therefore means dependence on available information, not dependence on
    a theory of knowledge.
- **What is open.**
  - Which information the quantum weights condition on: records `R` only, or further information
    `K` such as known invariants or prior information (Stage 1 §5.4.3 item 3).
  - Whether posit (iv)'s measure is physically motivated.
  - These are questions about information and measure. Stage 1 R2 does not establish that solving
    Witten's knowledge problem is needed for the measure or for the Born rule. Both remain
    unresolved for the reasons in Section 3.1.
- In the operationally classical class, the "collapse" when an observer learns is Bayesian
  conditioning. This is not specific to quantum mechanics.

### 4.3 The closed-eyes detector case

Three events: (1) system–detector interaction, (2) the detector registers, (3) the scientist learns.

**(a) Is the detector an observational locus?** Yes.
- "the Definition covers every registering locus, and for a detector or a horizon that a registering
  occurs is a physical fact" (Main.md:36).
- With the detector as V (Main.md:42), the detector always occupies a definite configuration (claim
  (a) of 2.1). Event 2 additionally requires that configuration to encode the outcome (claim (b)).
  Event 3 requires the encoding to stay accessible to a later coupling with the scientist (claim
  (c)).
- Only (a) follows from the ontology. In OI's general constructions, (b) and (c) are built in by the
  realization; for a native apparatus they are NOT PASSED (3.4).
- Main.md:34 adds that "a momentary registering with no persistent record satisfies the first axiom
  and fails C2". Physical registration is admitted even without persistence; a persistent record is
  the further C2 requirement.

**(b) Does the record and feed-forward machinery model event 2 and the variant?**
- `InstAvail` (ImplementationLocality.lean:268) has `readout` (native Lüders readout of a register)
  and `bind` ("sequential composition with outcome-dependent continuation"). Together they are the
  formal form of record-controlled feed-forward.
- The adaptive corollary realizes "the policy-controlled step ... the instrument selected by the
  protocol from the retained record" as one reversible map (Main.md:590).
- In the stated monomial class, `bind` after `readout` gives classical feed-forward on diagonal
  states. The variant (the record controls a further experiment that nobody knows about) is modelled,
  but only at tier (1): any classical stochastic theory models it.
- In a structurally closed extension that drives the elementary transitions, the same constructors
  give quantum feed-forward (`substratum_plus_control_qm`, `exactAll_iff_physical_general`; endpoint
  (i)).
- In the gluing construction, adaptive protocols are realized to accuracy epsilon with supplied data
  (Main.md:576, 590; tier 2).
- Both are conditional on resources not sourced from the substratum.

**(c) Wigner-type agreement and interpretation dependence.**
- In OI's ontology, at event 2 the detector occupies a definite configuration by premise
  (Substratum.md:465, Main.md:704). "An outcome already exists" additionally needs (b).
- In Everett-type readings [background] it is not so, and in QBism [background] it is
  agent-relative.
- The case is therefore interpretation-dependent at the ontological level. Stating it does not favour
  OI over Bohmian mechanics, which also has a definite record at event 2 [background].

**(d) Does the case separate the levels?** Yes.
- Events 1–2 are ontological: a definite configuration by premise, plus record formation. Event 3 is
  conditioning on available information.
- Neither says why the detector's statistics, or a larger observer's statistics on detector plus
  system, are quantum. That is the operational and statistical content, which is not derived
  (Sections 2–3).
- The owner's reading — knowledge does not make the outcome real, the outcome can be acquired because
  it exists, and quantum rules still need derivation — matches OI's premises, provided (b) holds. The
  case confirms the separation; it does not reduce the operational or statistical burden.

### 4.4 Four notions kept separate; Wigner's friend and local friendliness

**Definiteness** (substratum level). A premise, for configurations (2.1(a)). It does not rest on
irreversibility: OI's dynamics is a bijection, so no record is fundamentally irreversible.
- Reversibility preserves a record's information globally, not at a location (Main.md:74).
- A record can be moved by a reversible step or erased locally: confined classes on rule Q erase
  their records (MEAS-Q MQ4).

**Decoherence** (effective-description level). Not derived in any passage traced.
- Main.md:730: on coherent inputs the permutation unitary "carries visible coherence into the hidden
  register". Whether memory is classical "depends on the realization rather than on the visible law".
- So the visible law does not fix coherence properties. Coherent inputs are not available to
  embedded observers in the stated architecture (2.3).

**Irreversibility.** Effective only. The substratum is reversible (A2). A record can be overwritten
locally by later dynamics while the configuration was definite throughout.

**Inter-observer agreement.**
- For the ordinary Wigner's friend, a joint law exists (3.5).
- Agreement of compared records needs encoding and accessibility (3.5). It is not automatic.
- For genuinely quantum extended protocols it is not modelled.

**Can a definite record coexist with a larger observer's interference on detector plus system?**
- Logically yes, in hidden-variable theories. Bohmian mechanics has definite positions while the
  joint wave function interferes [background], at the cost of nonlocality.
- In OI the coexistence cannot be exhibited today. The superobserver's coherent operation on friend
  plus system is not an available operation in the stated architecture (kernel no-go, 2.3).
- In the gluing construction, the friend's visible outcome register is a classical record and the
  coherent state lives in the hidden density register (Main.md:574). Reproducing Wigner's
  interference on "friend plus system" would require modelling the friend's lab inside the supplied
  quantum data. The friend's definite visible record and the quantum system Wigner interferes would
  then be different objects.
- Whether OI can make them the same object, a definite record that is also part of a coherently
  interferable system, is open.

**Extended-Wigner no-go results.**
- Bong et al. (arXiv:1907.05607v4) name three assumptions: No-Superdeterminism, Locality and
  Absoluteness of Observed Events. They show that if quantum evolution is controllable at observer
  scale, at least one fails. Proietti et al. (arXiv:1902.05080v2) report a six-photon violation of an
  associated inequality by 5 standard deviations.
- **Conditional conclusion.** IF an OI completion
  - (1) reproduces the relevant local-friendliness-violating correlations,
  - (2) satisfies the theorem's precise absoluteness condition, including consistency of the friends'
    outcomes with what is later read back, and
  - (3) retains the theorem's no-superdeterminism condition for that extended experiment,

  THEN it must violate the theorem's Locality condition. This is the theorem applied
  (arXiv:1907.05607, abstract; exact definitions [background]).
- **Status of each antecedent in OI.**
  - (1) Not established: superobserver operations are not available (2.3), and F2 is open.
  - (2) Not established. Definite configurations give claim (a) only. Absoluteness of an observed
    event also needs the friend's configuration to encode the outcome (b), and the read-back
    consistency the theorem uses needs (c). "In Wigner's friend, the Friend has a definite outcome"
    (Substratum.md:463) asserts this but does not establish it for an extended protocol in which the
    friend's measurement is reversed.
  - (3) Not established. OI's measurement-independence posit (Main.md:410–416) is stated for the
    Bell setting ensemble. It is not shown to cover the settings of an extended Wigner's-friend
    experiment that includes the superobservers' choices.
- **Direction, not result.** OI's adopted Bell branch, "ontic parameter dependence" with operational
  no-signalling required (Main.md:418), suggests where such a completion would fail Locality. It does
  not establish that the completion exists. Whether its Locality failure is compatible with
  operational no-signalling for the compared records is open; no corpus passage analyses it.
- **Corpus treatment.**
  - A corpus-wide search found local friendliness only in `book/appendix-c-objections.md` (C.3). It
    says "Observer-relative information alone does not establish which local-friendliness premise a
    proposed completion violates" and that this requires "separate checks".
  - Frauchiger–Renner is stated unresolved (Main.md:704; appendix-c C.3).
  - No paper, Lean module or programme record analyses Bong et al. or Proietti et al.
  - OI asserts (S), single outcomes, by premise. Whether (Q) or (C) fails for an OI completion is
    undetermined [background on the definitions].
- **The essential question.** How can observers have different operational descriptions of one
  reality and agree on comparison? OI answers for the ordinary friend (one joint law), provided the
  records form and persist. For extended protocols it cannot answer yet. Under the conditional above,
  the no-go results indicate the answer would involve a Locality violation.

### 4.5 Classification (Question 3)

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| Definiteness of configurations and operation classes need no notion of knowing | source reading (textual and definitional trace) | Main.md:36, 42; OIRealization.lean:289; Stage 1 §8.3 | search scope of Stage 1 |
| Stochastic weights depend on conditioning on available information | kernel theorem (pushforward) plus source reading | `pushforward_identity`; Main.md:58, 736 | Stage 1 R2 |
| Conditioning needs no theory of knowing or awareness | paper proof (elementary; conditional probability on an event) | 4.2 | — |
| Which information the quantum weights condition on; physical motivation of posit (iv) | open question | Main.md:58 vs 60, 736 | posit (iv) not reinterpreted |
| Witten's knowledge problem necessary for the measure or the Born rule | not established (no evidence found) | Stage 1 R2; 3.1 | — |
| Detector is a registering locus | source reading | Main.md:36, 42 | Definition |
| Detector configuration definite (a); encoding (b) and accessibility (c) | (a) conditional consequence; (b), (c) missing mechanism for native apparatus | 2.1; `repeatable-measurement-feasibility-20261118/DECISION.md` | Definition, A2 |
| Feed-forward is modelled (`bind`, `readout`, policy step) | source reading (Lean definitions) plus paper proof (Main.md:590) | ImplementationLocality.lean:268; Main.md:590 | — |
| In the stated class that feed-forward is classical (tier 1) | paper proof (from R5) | R5; `frozen_sourcing_verdict` | monomial class |
| Quantum feed-forward | conditional consequence | `substratum_plus_control_qm`; Main.md:574–590 | `DrivesElementary` extension, or supplied quantum data |
| Closed-eyes case separates the ontological level from the operational and statistical levels, and does not discriminate OI | paper proof (this report) | 4.3 | — |
| Definite record plus superobserver interference exhibited in OI | open question | 2.3 kernel no-go; Main.md:574 | — |
| IF reproduction, full absoluteness and no-superdeterminism THEN Locality fails | conditional consequence (external theorem applied) | arXiv:1907.05607 (abstract) | antecedents (1)–(3), none established; exact definitions [background] |
| OI's measurement-independence posit covers extended-Wigner settings | open question | Main.md:410–416 | — |
| Compatibility of a Locality failure with operational no-signalling | open question | appendix-c C.3; no paper analysis | — |
| FR premise failing for OI | open question | Main.md:704; appendix-c C.3 | — |
| Decoherence derived | missing mechanism | Main.md:730 (realization-dependent); no derivation traced | — |

***

## 5. Question 4: structural resolution

### 5.1 Endpoints and the two questions

Native sourcing of the coherent resource is itself a reconstruction target (F2, `PROGRAMME.md`:40).
Success is not defined here so as to exclude it. Three endpoints are distinguished:

- **(i) Conditional quantum model.** Quantum operations are added as a premise. The Lean form is
  `substratum_plus_control_qm`: an extension of the substratum class that is structurally closed and
  drives the elementary transitions generates exact finite endomorphic and composite QM. This holds
  within complex matrix kinematics taken as given.
- **(ii) Physical reconstruction of operational quantum structure.** The added operations are derived
  from the substratum (F2 sourcing; lift seam `PROGRAMME.md`:474; Arc E `PROGRAMME.md`:489).
- **(iii) Stronger foundational reconstruction.** The complex kinematics and the probability rules are
  also derived (Main.md:572; QB3-EVIDENCE.md:5).

### 5.2 Resolving the measurement problem (definite outcomes while reproducing quantum predictions)

- **Today.** Tiers (1) and (2) are established.
  - Per finite experiment, definite reversible dynamics realizes supplied quantum statistics without
    collapse. The dilation does so from supplied outcome laws; the gluing construction from supplied
    instruments and state, to accuracy epsilon, including incompatible measurements and adaptive
    protocols.
  - These are models built from the statistics, not OI's physical substratum with one fixed dynamics.
  - No fixed finite carrier reproduces a qubit exactly (Main.md:568). One fixed dynamics covering all
    experiments would need an infinite carrier or a limit, which is open.
- **Under endpoint (i).** The Lean theory is a theory of operations on configuration-indexed complex
  matrices. It does not itself give a definite-configuration realization: applied to a diagonal
  state, an admissible non-monomial operator gives a non-diagonal state.
  - Paired with a definite-ontology realization of those operations — available per finite
    experiment through the gluing construction, with the state stored in a hidden register — it would
    support a Bohmian-type resolution: definite outcomes, quantum predictions, and some quantum
    structure postulated.
  - A single realization serving all experiments is not constructed.
- **Under endpoints (ii) and (iii).** The same resolution would follow, with the quantum operations,
  and for (iii) the probability rules, derived rather than postulated.
- **Status.** A resolution by OI's own physical substratum is not established. All three endpoints
  are open.
- **Locality.** By the conditional of 4.4, any endpoint that reproduced extended-Wigner predictions
  with the full absoluteness condition and no-superdeterminism would violate Locality.

### 5.3 Deriving quantum mechanics (why quantum structure and probability rules emerge)

- **Today.** Not achieved (tier 3).
  - The stated observer interface is operationally classical (kernel).
  - The Born form is definitional and the measure posited.
  - The representation equivalence is universal and does not select quantum structure.
- **Endpoint (i)** does not derive quantum structure; it adds it.
- **Endpoint (ii)** would derive the operational quantum structure.
  - Necessary: leave the nonnegativity-bounded class (`nonnegBounded_verdict`), and have a
    non-monomial admissible operator for layer flows
    (`exists_nonMonomial_of_layerFlowExecutable`).
  - Sufficient, with structural closure: the elementary flows, swaps and quarter phases
    (`substratum_plus_control_qm`). Relative to the monomial class, the missing elementary
    ingredient is the flows (`substratumClass_not_drivesElementary`; the class already has swaps and
    phases).
  - Native sourcing is open (`PROGRAMME.md`:40; MR-1 `GAP` provisional).
- **Endpoint (iii)** would also derive the complex kinematics (Main.md:572) and the Born exponent and
  measure (QB3-EVIDENCE.md:5). All are open.

### 5.4 By level

**Ontological level**
- **Established:**
  - definite configurations and no branching, by premise (Definition, A2);
  - compatibility of definite reversible dynamics with supplied finite record statistics (kernel
    `S_imp_D`; paper Main.md:490, 574–590, 694);
  - per-realization nonuniformity (paper Main.md:496, 568).
- **Not a consequence of the ontology:** encoding and accessibility of records. Native apparatus NOT
  PASSED.
- **Conditional on reconstruction:** a definite realization of a fixed physical dynamics reproducing
  quantum predictions (endpoints (i) plus a realization, (ii) or (iii)).
- **Unresolved:** whether the definite ontology is the one nature has (Main.md:732: "what is
  empirically falsifiable is the framework's physical identification of nature"; no memory falsifier
  is established, Main.md:730).

**Operational level**
- **Established:** the physically sourced observer theory and the monomial theory are operationally
  classical (kernel; diagonal effects by derivation). The measurement problem's quantum content does
  not arise there.
- **Conditional (endpoint (i)):** exact finite operational QM under `substratum_plus_control_qm`'s
  hypotheses.
- **Target (endpoint (ii)):** native sourcing of those operations. Open steps: F2 (`PROGRAMME.md`:40,
  Arc D); the physical lift seam to instruments and composites (`PROGRAMME.md`:474); Arc E composites
  and Bell (`PROGRAMME.md`:489).

**Statistical level**
- **Established:** Born form by definition; diagonal-sector conditioning; Lüders readout form within
  `FiniteOperationalTheory` (kernel).
- **Conditional (endpoints (i), (ii)):** trace-form probabilities and Kraus update, within the given
  complex kinematics.
- **Target (endpoint (iii)):** derivation of the kinematics (Main.md:572) and of the Born exponent and
  measure (QB3-EVIDENCE.md:5).
- **Open:** which information the quantum weights condition on (R2). This is a question about
  information and measure, not about a theory of knowing (4.2).

### 5.5 Evaluation of the owner's hypothesis
- The antecedent requires all three levels without a theory of subjective knowing.
- **Knowing.** No step identified at any level depends on a theory of knowing. The obstruction is the
  missing derivation of quantum operational behaviour (5.3), with the open statistical items of 3.1.
- **Today.** Ontological: configurations by premise, records conditional on apparatus formation.
  Operational: not derived. Statistical: definitional only. The antecedent is not met.
- **Endpoint (i)** plus a definite realization would give a Bohmian-type resolution of the
  measurement problem, with postulated quantum structure. It would not give a derivation.
- **Endpoint (ii)** would add a derivation of the operational structure.
- **Endpoint (iii)** would add a derivation of the probability rules.
- The reversal of explanatory direction — superposition from definite reality — corresponds to
  endpoint (ii) or (iii). No corpus result indicates how either is reached. Under endpoint (i) the
  superposition is supplied, not derived.

### 5.6 Classification (Question 4)

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| Ontological level: definite configurations | conditional consequence | Main.md:42; Substratum.md:94, 465 | Definition, A2 |
| Per-experiment compatibility with supplied quantum statistics | kernel theorem plus paper proof | `S_imp_D`; Main.md:490, 574–590, 694 | supplied data; finite experiment; finite accuracy for gluing |
| Operational level not addressed in stated architecture | kernel theorem | `frozen_sourcing_verdict`, `nonnegBounded_verdict`, `substratumGen_not_control`, `substratumClass_not_drivesElementary` | finite carriers |
| Endpoint (i): exact QM from a structurally closed, elementary-driving extension | conditional consequence (kernel) | `substratum_plus_control_qm`, `exactAll_iff_physical_general` | `ExtendsSubstratum`, `StructurallyClosed`, `DrivesElementary`; given kinematics |
| Endpoint (i) gives a definite-configuration realization by itself | not established | 5.2 | — |
| Bohmian-type resolution under endpoint (i) plus a definite realization | conditional consequence | 5.2; Main.md:574–590 | endpoint (i); per-experiment realization with stored state |
| Endpoint (ii): native sourcing of the operations | missing mechanism | PROGRAMME.md:40; MR-1 `GAP` provisional | — |
| Endpoint (iii): kinematics, exponent and measure derived | open question | Main.md:572; QB3-EVIDENCE.md:5 | — |
| Statistical level: Born by definition only | source reading | Main.md:18, 564 | — |
| Principal obstruction is the missing derivation of quantum operational behaviour, not knowing | paper proof (this report, from the rows above and 4.1–4.2) | 4.1, 4.2, 5.3 | search scope of Stage 1 |

***

## 6. Question 5: distinctiveness

Scope: the comparison is restricted to OI's formal architecture as read at the pin and to the
literature in Section 1. External positions not retrieved are [background].

### 6.1 Comparison with other approaches

**Bohmian / pilot-wave** [background].
- Shared: a definite configuration ontology; quantum predictions as statistics; nonlocality (book
  appendix-c:158 says so).
- Bohm derives the full quantum statistics from the guidance equation plus quantum equilibrium. OI
  derives neither.
- OI has two compatibility constructions.
  - The gluing construction stores the quantum state in a hidden register (Main.md:574, 590), a role
    analogous to the pilot wave.
  - The intervention dilation stores no quantum state but takes the outcome laws as supplied input
    (Main.md:490, 694).
- The claim that OI "reproduces Bohmian's ... statistical-predictions content without the pilot
  wave's structural cost" (appendix-c:162) is a candidate finding for separate verification
  (Section 9).

**'t Hooft cellular automaton** (arXiv:1405.1548v3).
- Both posit deterministic discrete dynamics and claim to dispose of collapse.
- The Bell placement differs: 't Hooft argues superdeterminism can be defended. OI keeps measurement
  independence and adopts ontic parameter dependence (Main.md:410–418, 716).
- Whether 't Hooft derives interference natively for generic rules was not checked: only the
  abstract was retrieved [background].

**Barandes stochastic–quantum correspondence** (arXiv:2302.10778v3; 2512.18105v1).
- Barandes demotes the wave function and gives a "deflationary account" of interference and collapse
  over a configuration-space stochastic process.
- OI instantiates his tuple (TI1, `PROGRAMME.md`:308).
- His indivisibility is a class name, not OI's failure predicate (BD3, `PROGRAMME.md`:222).
- His interference term depends on a choice of unitary lift that the visible data do not fix (SA2,
  `PROGRAMME.md`:284).
- An interference round on this route is "not well posed" until a candidate is selected
  (`PROGRAMME.md`:377).
- OI's distinctive addition is a deterministic reversible mechanism that produces the stochastic
  process (`S <=> D`). That is a mechanism for stochasticity, not for interference.
- Barandes–Hasan–Kagan obtain Tsirelson from causal locality of indivisible processes; OI's
  deterministic completion instead caps at 2 under screening (Main.md:397–405).

**Wetterich** (arXiv:0906.4919v2).
- A classical ensemble with probabilistic observables and a "purity constraint" yields density
  matrices, Bell violation and the Born rule per the abstract.
- No derived counterpart of the purity constraint was found in the OI sources read. OI's sourced
  observer theory is nonnegativity-bounded.

**Nelson** [background].
- Continuous stochastic process; Wallstrom's quantization objection.
- OI avoids it by not deriving the Schrödinger equation from a process (Main.md:718), which also
  means OI does not derive the Schrödinger dynamics.

**GRW / objective collapse** (contrast) [background].
- Adds stochastic dynamics to make outcomes definite. OI adds nothing dynamical.
- OI's no-collapse is at tier (1) for its own observer interface and tier (2) for the compatibility
  constructions. A derivation-level no-collapse account (tier 3) is not achieved (Section 2).

**Everett / relative-state** (contrast) [background].
- OI denies branching by premise (Substratum.md:465).
- Everett's branches are coherent components. OI's stated architecture has no coherent components to
  deny.
- "The Everettian measure problem does not arise" (Main.md:694) is accurate within OI's ontology, by
  premise (Stage 1 O12).

**Consistent histories** [background].
- OI's substratum fixes one classical measure on configuration histories, in effect a single fixed
  framework.
- Incompatible frameworks (non-commuting history families) have no counterpart in OI's stated
  architecture.

**QBism** (arXiv:1311.5253v1, contrast).
- QBism is agent-centred, with no ontology beneath. OI shares dependence of the weights on available
  information (R2) but has a definite ontology.
- OI's claim to provide a "structural why" relative to QBism (Main.md:716) is a candidate finding for
  separate verification (Section 9).

**Spekkens toy theory** (quant-ph/0401052v2).
- The closest precedent for "superposition-like behaviour from restricted knowledge of definite
  states". An epistemic restriction reproduces analogues of interference and noncommutativity but not
  Bell violation or KS.
- The toy theory is itself a restricted classical theory. Diagonal effects at OI's observer interface
  therefore do not exclude Spekkens-type analogues in a suitably restricted description. Whether OI's
  stated architecture produces them is not shown either way.
- The corpus itself draws the lesson that "restricted access does not by itself single out quantum
  theory" (appendix-c:214).
- Spekkens' theory is generalized-noncontextual [background], so "interference analogues" are not a
  sufficient test. A derivation-level result must produce a non-simplex-embeddable fragment
  (arXiv:1911.10386).

### 6.2 What is distinctive, within the architecture and literature checked
1. A kernel-checked, rule-independent proof that the configuration-level observer theory is
   nonnegativity-bounded, hence classical (`sourcing_rule_independent`, `frozen_sourcing_verdict`).
   This identifies what an embedded-observer explanation of QM must add. It is a sharp negative
   result, not a resolution.
2. An exact finite equivalence `S <=> D <=> Q_fb` with an internal proof. It is universal, so it does
   not discriminate quantum from classical (Main.md:18).
3. The C4 history-readback characterization of a memory-bearing sector (Main.md:18, 97). Its content
   is classical memory, not coherence.
4. An explicit Bell placement with a quantitative measurement-dependence bound (Main.md:429–433).

Within the literature checked, none of these is a mechanism for producing quantum measurement
behaviour from definite outcomes that the compared approaches lack.

### 6.3 Classification (Question 5)

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| Definite-ontology account of outcomes is shared with Bohm, 't Hooft, Barandes | source reading (comparison) | 6.1; external abstracts; [background] | literature checked |
| Gluing construction stores the quantum state (pilot-wave-like role); dilation does not but takes outcome laws as input | source reading | Main.md:490, 574, 590, 694 | — |
| OI instantiates Barandes' tuple; interference term not fixed by visible data | kernel theorem (TI1) plus audit determination (SA2) | PROGRAMME.md:284, 308 | Source A direct branch |
| Bell placement differs from 't Hooft | source reading | Main.md:410–418, 716; arXiv:1405.1548 (abstract) | — |
| Rule-independent classical ceiling of configuration-level observation | kernel theorem | `sourcing_rule_independent`, `nonnegBounded_verdict` | stated architecture |
| Spekkens-type analogues in OI | open question | 6.1 | — |
| A non-simplex-embeddable native fragment | open question | OA-2 STATUS ("Open: G3 for admissible non-affine rules") | — |

***

## 7. Three-way partition

The partition is given separately for the two questions. Each item carries its support class.

### 7.1 Resolving the measurement problem

**Already established**
- Definite configurations, no branching (conditional consequence: Definition, A2).
- Registration needs no knower (source reading: Main.md:36).
- Per-experiment compatibility of definite reversible dynamics with supplied quantum statistics, by
  dilation and by gluing (kernel `S_imp_D`; paper proofs Main.md:490, 574–590, 694).
- The ordinary Wigner's-friend joint law (paper proof).
- Tier (1): no collapse in the operationally classical observer interface (kernel plus derivation).

**Conditional on reconstruction (open step named)**
- A definite-ontology account in which OI's physical substratum, with one fixed dynamics, reproduces
  quantum measurement statistics.
  - Under endpoint (i), it needs `substratum_plus_control_qm`'s hypotheses plus a definite
    realization of the added operations. Per experiment, that realization is available through the
    gluing construction.
  - Under (ii) or (iii), it needs F2 sourcing (`PROGRAMME.md`:40), the lift seam (`PROGRAMME.md`:474)
    and Arc E (`PROGRAMME.md`:489).
- Native record formation and retention: claims (b) and (c), repeatability, and agreement on
  comparison (`repeatable-measurement-feasibility-20261118/DECISION.md`; MR-1 provisional).
- Quantum Bell correlations with no-signalling (H-Bell (i)–(iii), Substratum.md:131–133).
- Extended-Wigner protocols: IF reproduced with full absoluteness and no-superdeterminism, THEN
  Locality fails (conditional consequence, 4.4).

**Unresolved even then**
- Whether a definite realization can serve all experiments with one fixed dynamics. A fixed finite
  carrier cannot be exact for a qubit (Main.md:568); infinite carriers and limits are open.
- Whether the required Locality failure is compatible with operational no-signalling for compared
  records (no corpus analysis).
- Whether OI's measurement-independence posit covers extended-Wigner settings (open).

### 7.2 Deriving quantum mechanics

**Already established**
- The configuration-level observer theory is nonnegativity-bounded for every rule (kernel). This is a
  negative result locating what must be added.
- The exact but universal representation equivalence (kernel).
- Born form by definition; diagonal-sector Lüders as conditioning; local Lüders readout form within
  `FiniteOperationalTheory` (source reading, paper proof, kernel).

**Conditional on reconstruction (open step named)**
- Endpoint (ii): native sourcing of the elementary flows, or of another non-monomial admissible
  resource, together with structural closure (F2, `PROGRAMME.md`:40).
  - Necessary resources: leave the nonnegativity-bounded class; a non-monomial operator for layer
    flows.
  - Sufficient completion: `substratum_plus_control_qm`.
- KS and generalized contextuality from a native non-simplex-embeddable fragment (OA-2 "Open").
- Endpoint (iii): derivation of the complex kinematics (Main.md:572) and of the Born exponent and
  measure (QB3-EVIDENCE.md:5).

**Unresolved even if endpoint (i) is adopted**
- Derivation of the operational quantum structure (endpoint (ii)).
- Derivation of the kinematics and probability rules (endpoint (iii)).
- Which information the quantum weights condition on, and the physical motivation of posit (iv)
  (R2). This is a question about information and measure, not about a theory of knowing.

***

## 8. Limitations

- External sources were read at abstract level. The exact definitions of the Frauchiger–Renner (Q),
  (C), (S) and of Bong et al.'s Locality and Absoluteness of Observed Events were not retrieved. The
  conditional in 4.4 is stated relative to them.
- Bohm, GRW, Everett, Nelson, consistent histories, Gleason, Kochen–Specker and PBR are
  [background].
- R5's diagonal-effect statement and this report's simplex-embeddability and feed-forward
  observations are derivations from definitions, not kernel theorems. No Lean was built. The Lean
  statements of `substratum_plus_control_qm` and `DrivesElementary` were read in source.
- Research records were read at their stated standing:
  - MEAS-Q, OA-1, OA-2 and QB3 are research records reviewed by agents, not established claims.
  - The unified ledger directory is marked unreviewed. r9 is pending review and r5 is
    owner-accepted. Its rows are cited only alongside authoritative sources.
  - MR-1's `GAP` is provisional.
- No result in this report rests on any of these alone.
- The reconstruction programme is large. Native-sourcing sub-records were sampled, not exhaustively
  read:
  - `native-y-continuation-20261024/`, `univ-2-20261120/`, `physical-source-hypotheses-20261118/`.
  - The status lines read report no sourced coherent instrument.
  - A positive native coherence result in an unread record cannot be excluded. `PROGRAMME.md`:40 and
    the frozen-sourcing kernel results bound what such a result could be for the stated
    architecture.
- Stage 1's search scopes are inherited for the knowing and Axiom 1 findings.

***

## 9. Manuscript inaccuracies found (for the separate correction package; no edit made)

These are candidate findings for separate verification, not accepted consequences of this report.
Each needs its own check before any correction is considered.

1. **papers/Main.md:692** (mirror Main.tex:5189). "Their quantum behavior is a downstream consequence
   of the trace-out." Candidate: stronger than the evidence. The trace-out gives a representation that
   is universal, Markov included (Main.md:18). Operational quantum behaviour requires the unsourced
   operational bridge (Main.md:666, 694). Kernel: `frozen_sourcing_verdict`. Pattern: representation
   promoted to behaviour.

2. **papers/Substratum.md:463** (mirror Substratum.tex near :2651). Two candidate problems:
   - "The wave function ... is a derived object." The representation exists, but it is non-unique
     (Main.md:656; padding theorem, `PROGRAMME.md`:216) and fixed-basis/diagonal only.
   - "Wigner's superposition reflects his epistemic deficit." Epistemic incompleteness gives a
     mixture. A coherent superposition of Friend's states is not derived as a reduced description,
     and the stated interface cannot distinguish the two (R5).

   Candidate: partly right. Related passages:
   - `book/appendix-c-objections.md`:323 ("superpositions are reduced descriptions used by embedded
     observers with incomplete information"; mirror FULL.md:6478, FULL.tex:25426);
   - `book/ch19-open-problems.md`:64 (labelled a proposed interpretation; lower severity).

3. **book/ch01-observation.md:286** (mirror FULL.md:619, FULL.tex:2745). "the modified game whose
   rational odds sheet carries interference terms". Candidate: the terms are P-indivisibility
   discrepancies. On the Barandes route an interference round is "not well posed" until a candidate
   is selected (`PROGRAMME.md`:377), and native interference is open (Main.md:694).
   - Also ch01:292: "so there was never anything to collapse". This holds without qualification only
     in the operationally classical sector.

4. **book/ch18-beyond.md:110** (mirror FULL.md:4841). "Quantum indeterminacy is the cost of partial
   observation, not a feature of reality." Candidate: in the stated architecture partial observation
   yields classical stochasticity (kernel `nonnegBounded_verdict`). Whether it yields quantum
   indeterminacy (contextual, Bell-violating) is open.

5. **book/appendix-c-objections.md:162** (mirror in FULL.md). "The framework reproduces Bohmian's
   deterministic-substratum and statistical-predictions content without the pilot wave's structural
   cost." Candidate: OI does not reproduce quantum statistical predictions from its substratum
   (Main.md:694; F1 retired, `PROGRAMME.md`:521). Its compatibility constructions either store the
   quantum state in a hidden register (Main.md:574, 590) or take the outcome laws as supplied input
   (Main.md:490, 694).

6. **papers/Main.md:716.** "QBism/relational QM: ... this framework provides a structural *why* and
   quantitative predictions." Candidate: a self-assessment not traced to an established result for the
   measurement-relevant content. It may also conflict with AGENTS.md §A.32 (self-assessment outside
   status labels).

Lower-severity wording risk, not an error: **papers/Main.md:694**, "The Born rule, often treated as an
independent postulate, is here part of the exact fixed-basis representation dictionary ... rather
than an additional stochastic axiom". This is literally accurate (definitional), but it can be read as
a derivation. QB3-EVIDENCE.md:5 records that OI has not yet been shown to derive the Born rule.

Checked and not listed: Main.md:74 and :80 on C2-structural. These state retention of record
information by reversibility and admit routing (Main.md:74), so they do not claim persistence at a
location.

***

Nothing in this report establishes that OI reproduces quantum mechanics or resolves the measurement
problem. The body shows only that OI posits definite configurations, that definite reversible
dynamics is compatible with supplied finite quantum statistics, and that OI's stated observer
interface is operationally classical. It also identifies the conditional and missing steps listed
above.

***

## Review corrections in r2: correction-to-finding mapping

| Correction | Report sections changed | Change | Verdict or conclusion affected (old -> new) |
|---|---|---|---|
| R1 | Covering summary (ontological level; Q2 and Q3 verdicts); 2.1; 3.4; 3.5; 3.8 rows Repeatability and Observer agreement; 4.3(a); 4.4 Definiteness and Inter-observer agreement; 7 | Distinguishes (a) definite configuration, (b) encoding of an outcome, (c) later accessibility. Only (a) follows from the ontology. C2-structural is restated as information retention in the global state (Main.md:74), not persistence at a location. "Agreement is automatic because there is one configuration" is removed: a single configuration fixes a fact of the matter, but records agree only if they encode the same outcome and stay accessible. | "Records are definite; persistence by reversibility; agreement automatic in the classical class" -> "configurations are definite; encoding and accessibility need record-forming and retaining dynamics (native apparatus NOT PASSED); reversibility preserves information globally, not at a location; agreement is not automatic" |
| R2 | Covering summary (Q1); 2.2; 2.3 pressure test; 2.4; 6.1 Bohm; 7; 9 item 5 | Two compatibility results with different inputs. Dilation: supplied finite outcome laws -> a definite reversible realization, no density matrix stored (Main.md:490, 694). Gluing: supplied quantum instruments and initial state -> one adaptive realization to the stated accuracy, with the density matrix stored (Main.md:574–590). Neither derives interference. | "The one construction reproducing interference stores the quantum state" -> "two compatibility constructions; only the gluing one stores the state; neither derives interference" |
| R3 | Covering summary (operational level); 2.3; 2.4; 3.9; 5; 7 | Separates `permTheory` (physically sourced; nonnegativity-bounded; no phases) from the monomial `substratumClass` (complex phases stipulated; effects diagonal by derivation). States the exact hypotheses of `substratum_plus_control_qm`: `ExtendsSubstratum`, `StructurallyClosed`, `DrivesElementary`. Separates necessary resources (leaving the nonnegativity-bounded class; phases and dense control; a non-monomial operator for layer flows) from sufficient completion conditions. | "Exact QM follows if one adds a continuously tunable state-mixing operation" -> "it follows for a structurally closed extension that drives the elementary transitions (flows at all real t for all pairs, swaps, quarter phases, at every carrier); necessary and sufficient resources stated separately" |
| R4 | Covering summary (statistical level; Q3); 4.2; 4.5; 5; 7 | Conditioning on available information is defined without any theory of awareness. Dependence on available information is separated from dependence on a theory of knowing. The claim "only if conditioning is on physical records alone" is removed. The open question is restated as which information the weights condition on, and whether posit (iv) is physically motivated. Stage 1 R2 does not make Witten's problem necessary for the Born rule or the measure. | "Without a theory of knowing only if conditioning is on records alone" -> "probabilities need no theory of knowing; which information the quantum weights condition on is open, and so are the measure and the Born rule, for reasons unrelated to knowing" |
| R5 | Covering summary (Q3); 4.4; 4.5; 7 | Local-friendliness conclusion stated conditionally: IF an OI completion reproduces the violating correlations, satisfies the precise absoluteness condition (including readback consistency) and retains no-superdeterminism for that experiment, THEN it violates Locality. Definite configurations alone do not establish full absoluteness. The measurement-independence posit is not shown to cover the extended experiment. The Bell branch suggests a direction only. | "Under OI's posits, Locality is the assumption to drop" -> "conditional: Locality must fail if the three antecedents hold; none is established" |
| R6 | Covering summary (new two-question split and three endpoints; Q4); 5 (restructured); 7 (restructured) | Three endpoints: (i) quantum operations added as a premise (conditional quantum model); (ii) operations derived from the substratum (physical reconstruction); (iii) kinematics and probability rules also derived. "Resolving the measurement problem" and "deriving QM" are evaluated separately. Native sourcing is treated as a reconstruction target, not excluded from success. | "Unresolved even if F2 succeeds: whether the resource is derived; the reversal fails" -> "resolution (Bohmian strategy) is possible under endpoint (i) paired with a definite realization; per-experiment compatibility is established today; derivation needs (ii) or (iii); all three endpoints open" |
| R7 | 1 (classification note); 2.4; 3.6; 3.9; 4.5; 5; 6.1 Spekkens; 6.2; 6.3; 8; 9 preamble | Diagonal effects do not exclude Spekkens-type analogues, since that theory is itself a restricted classical theory. Distinctiveness is restricted to the formal architecture and the literature checked. Ledger rows are marked [unreviewed draft ledger]. Textual readings are labelled "source reading" rather than "paper proof". Manuscript candidates are marked findings for separate verification. | "OI does not reach even Spekkens' analogues" -> "not shown either way"; several "paper proof" labels -> "source reading"; candidates -> "findings for separate verification" |
| Reviewer's three tiers | Covering summary; 2.3; 5; 7 | Adopts: (1) trivial, no collapse in classical stochastic theories; (2) established, compatibility of definite reversible dynamics with supplied finite quantum statistics; (3) unachieved, derivation of quantum measurement behaviour. "Merely trivial" wording is removed. Verified that the principal obstruction is (3), not knowing. | "OI explains definite records only in the trivial sense" -> "tiers (1) and (2) established; (3) not achieved" |

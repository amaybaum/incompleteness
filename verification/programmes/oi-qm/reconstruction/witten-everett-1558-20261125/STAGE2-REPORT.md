# #1558 Stage 2 — Can OI provide a structural resolution of the quantum measurement problem?

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

**Owner's hypothesis, evaluated rather than assumed.** If all three levels can be established
without a theory of subjective knowing, OI gives a substantive structural resolution of the physical
measurement problem. The antecedent is not met today: levels 2 and 3 are not established. The
analysis below finds that even a successful reconstruction along the programme's active route (F2)
would meet it only in a qualified form (Section 5).

### Verdicts by level

**Ontological level: addressed by premise, not by derivation.**
- Records are definite because OI's ontology is a set of configurations evolved by a bijection
  (Definition, Main.md:42; determinism A2, Substratum.md:94; single trajectory, Substratum.md:465).
  This is a premise of the same kind as Bohmian positions or 't Hooft's ontological states.
- The substantive established content at this level is a consistency result: a definite reversible
  ontology can realize any finite table of record statistics.
  - Every finite stochastic law has a finite reversible realization (kernel: `S_imp_D`, within
    `finite_horizon_equivalence`).
  - Every finite action-labelled family has one too (paper proof, Main.md:490).
  - The realization is per law and per horizon. No fixed finite realization reproduces even one
    qubit exactly (Main.md:496, 568).
- Registration needs no knower: a detector is a registering locus (Main.md:36).

**Operational level: not established; obstructed in the stated architecture; conditional beyond it.**
- The operation classes available to an embedded observer under the stated architecture are
  operationally classical.
  - Kernel theorems: `obsTheory_nonnegBounded`, `frozen_sourcing_verdict`, `nonnegBounded_verdict`,
    `substratumGen_not_control`, `obs_not_layerFlowExecutable`.
  - Derivation (Stage 1 R5): every effect is diagonal.
- In that class "no collapse is needed" is trivially true and carries no information about quantum
  measurement.
- Interference from the substratum dynamics is stated open: Main.md:694, Substratum.md:463, and
  ledger row B-P4-MEAS-5 (UO).
- Exact finite operational QM follows only if one adds a continuously tunable state-mixing operation
  (kernel: `substratum_plus_control_qm`). That holds within complex matrix kinematics taken as given,
  whose derivation is open (Main.md:572).
- The programme has retired the equivalence endpoint F1 for the stated architecture
  (`verification/programmes/oi-qm/PROGRAMME.md`:40, :521). The active F2 extension is open.

**Statistical level: not established.**
- The Born form is part of the definition of `Q_fb` (Main.md:18, 564). Its exponent is not selected
  (Main.md:226, 564).
- The corpus record states: "OI has not yet been shown to derive the Born rule or select the
  physical probability measure"
  (`verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md`:5).
- Lüders update is established only as Bayesian conditioning in the diagonal sector (Main.md:664).
- The weights are conditional laws given records, and possibly further knowledge (Stage 1 R2). Which
  conditioning the quantum state corresponds to is open.

### Verdicts by question

1. **Definite outcomes.**
   - OI explains definite records without collapse only in the trivial sense: its ontology is definite
     by premise, and its stated observer interface cannot produce coherence-sensitive statistics.
   - No substantive resolution, one that reproduces interference from the definite substratum through
     admissible observer operations, is established.
   - The one corpus construction that reproduces interference statistics stores the quantum state in
     the hidden sector as supplied data (Main.md:590).

2. **Measurement rules.**
   - Born rule and basis selection: Born form definitional; exponent and measure open; the
     configuration basis is privileged by premise.
   - State update: conditioning in the diagonal sector; Kraus update only under the completion
     conditions.
   - Repeatability: definitional for a definite configuration; physical apparatus sourcing NOT PASSED.
   - Observer agreement: a joint law exists for the ordinary Wigner's friend; genuinely quantum
     extended protocols are not modelled.
   - Contextuality: inherited only with supplied data; the native fragment is simplex-embeddable
     under named hypotheses.
   - Bell: ceiling of 2 for a screened local completion; the adopted branch needs ontic parameter
     dependence; H-Bell open.

   The exact missing mechanisms are listed in the status table (Section 3.8).

3. **Observation and knowledge.**
   - Definiteness and the operation classes need no notion of knowing.
   - The stochastic weights depend on conditioning on records (R2).
   - The closed-eyes detector case separates registration (ontological) from learning (conditioning)
     in OI's models. So does a classical theory: the case does not discriminate OI, and it says
     nothing about why the registered statistics are quantum.
   - If OI reproduced extended-Wigner's-friend predictions, its definite substratum (absoluteness of
     observed events) and its measurement-independence posit (no-superdeterminism) would leave
     Locality as the assumption to drop. This matches the corpus's adopted ontic-parameter-dependent
     Bell branch. It is conditional on reconstruction and on H-Bell, both open.

4. **Structural resolution.**
   - Already addressed: definiteness, by premise; no branching, by A2; the diagonal-sector
     conditioning account.
   - Conditional on reconstruction: Kraus instruments and update, the trace-form outcome rule within
     the given kinematics, contextuality and Bell violation (the last only with H-Bell).
   - Unresolved even then: derivation of the complex kinematics, the Born exponent and measure, and
     whether the added coherent resource is derived from definite dynamics rather than posited.
     Without that derivation the reversal of explanatory direction is not achieved.

5. **Distinctiveness.**
   - What is genuinely distinctive is negative and sharp: a kernel-checked proof that
     configuration-level embedded observation, for every microscopic rule, gives a nonnegativity-bounded
     (classical) operation class (`sourcing_rule_independent`). This locates exactly what an
     embedded-observer explanation must add.
   - The positive representation equivalence is exact but universal: it includes Markov chains.
   - The definite-ontology account of outcomes is shared with Bohm, 't Hooft and Barandes.
   - OI's Bell placement (measurement independence kept, ontic parameter dependence) differs from
     't Hooft's superdeterminism and resembles Bohmian nonlocality.

### Main uncertainties
- External texts were retrieved at abstract level only (Section 1).
- R5's "effects are diagonal" is a derivation from the definitions, not a kernel theorem.
- Whether an extended architecture sources coherence is open; this report does not prejudge it.
- The exact definition of Locality in Bong et al. is [background].

### What is NOT shown
- That OI reproduces quantum interference, the Born rule, contextuality or Bell violation from its
  substratum.
- That OI resolves or dissolves the measurement problem.
- That any of OI's no-collapse statements apply beyond the operationally classical sector.

***

## 1. Sources and pin

**Corpus.**
- Read from pinned objects only, at `e2e2a623265187a28ebec604ab8bcc672742888f`, the head of `main`.
- No later commit is relied on. Line numbers are at the pin unless stated otherwise.
- Main areas read:
  - `papers/Main.md` (§§1.2, 3.1–3.4, 4.1–4.5)
  - `papers/Substratum.md` (§§6.3–6.4)
  - `papers/GR.md` (Appendix A)
  - `book/ch01-observation.md`, `book/ch18-beyond.md`, `book/ch19-open-problems.md`,
    `book/appendix-c-objections.md`
  - `verification/programmes/oi-qm/PROGRAMME.md`
  - `verification/lean-mathlib/OIBridge/FrozenSourcing.lean`, `ImplementationLocality.lean`,
    `OperationalAssembly.lean`
  - Under `verification/programmes/oi-qm/reconstruction/`: `measurement-record-formation/`,
    `repeatable-measurement-feasibility-20261118/DECISION.md`, `meas-q-20261120/RESULT.md`,
    `born-sel-b-measure-20261104/QB3-EVIDENCE.md`, `oa-1-20261112/STATUS.md`,
    `oa-2-20261112/STATUS.md`, `drafts/unified-ledger-20261114/LEDGER-r9.md`
  - The accepted Stage 1 report.
- No Lean build or computation was run.

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
the exact definitions of (Q), (C), (S) and Locality.

***

## 2. Question 1: definite outcomes

### 2.1 Where definiteness comes from

- **The Definition** (Main.md:42) makes an observation a triple `(S, phi, V)`. `V` is a proper
  subsystem with finitely many distinguishable states.
- **A2** makes `phi` a bijection (Substratum.md:94).
- **Single trajectory.** "A fixed bijection on a finite set has exactly one trajectory from any
  initial state. There is no point at which the trajectory splits" (Substratum.md:465).
- So a record at time t is the value of V's configuration at t, an element of a set. It is definite
  by construction.
- This is a premise of the ontology, as for Bohmian positions or 't Hooft's ontological basis
  [background]. It is not derived from anything weaker.
- **Skeptical reading.** "OI explains definite outcomes" can mean only "OI posits a definite ontology
  and shows it is consistent with the record statistics". The second half is substantive (2.2); the
  first is stipulation.

### 2.2 What the corpus establishes about definite ontology and record statistics

- **Finite realization.** Every finite stochastic law on a finite alphabet and horizon has a finite
  reversible deterministic realization.
  - Kernel: `S_imp_D`, assembled in `finite_horizon_equivalence`
    (`verification/lean-mathlib/OIBridge/Equivalence.lean:462`).
  - This includes the record statistics of any fixed finite quantum experiment, given its
    probabilities (Main.md:20, 80 item 3).
- **Interventions.** Every finite action-labelled family has one realization with permutation
  instruments (paper proof, Main.md:490).
  - It reproduces Leggett–Garg violations, such as `K = 3/2`, because the instruments are invasive
    (Main.md:494; exact probe `lg_comb_probes.py`).
- **Quantum envelopes.** One finite reversible realization reproduces a bounded quantum instrument
  envelope to accuracy epsilon, given supplied quantum data (paper proof, Main.md:574–590).
- **Limits.**
  - No fixed finite realization carries the whole instrument algebra (Main.md:496).
  - No horizon-independent intervened representation exists at fixed dimension (Main.md:502).
  - No fixed finite carrier is exactly operationally equivalent to one qubit's full theory
    (Main.md:568). The factorization half is proved there; the unboundedness is imported.

### 2.3 The trivial case versus a substantive resolution

**Trivial case (established).** In the stated architecture the available operations are operationally
classical.
- **Kernel:**
  - `obsTheory_nonnegBounded` and `permTheory_nonnegBounded` (`FrozenSourcing.lean`): every
    available operation preserves nonnegative entries.
  - `frozen_sourcing_verdict` (`FrozenSourcing.lean:318`): no phases, no dense unitary control.
  - `sourcing_rule_independent` (`FrozenSourcing.lean:295`) and `obsTheory_rule_independent`
    (`SubstratumInterfaceAudit.lean:780`): the verdict does not depend on the microscopic rule.
  - `substratumGen_not_control` (`StructuralClosure.lean:330`) and `obs_not_layerFlowExecutable`
    (`ExecSource.lean:129`): no composite unitary control or layer flow.
  - `coherentLiftClass_eq_substratumClass` (`LiftSource.lean:164`): coherent lifts add nothing beyond
    the monomial class.
- **Stage 1 R5 (derivation from the definitions):** every Kraus operator is monomial, so every effect
  is diagonal.
- In this class a "measurement" is classical conditioning. Main.md:664 states that the Lüders rule
  "transcribes Bayesian updating ... for the represented diagonal sector".
- That "no collapse is needed" is then a property of every classical stochastic theory. It says
  nothing about the quantum measurement problem, whose content is the coexistence of definite outcomes
  with interference between alternatives.

**Substantive resolution (not established).** It would need coherence-sensitive statistics: a
non-diagonal effect, or a preparation reaching a superposition, generated by admissible observer
operations on the definite substratum.
- **Corpus status.**
  - "a derivation of the two-slit interference pattern from the substratum dynamics is open"
    (Main.md:694; also Substratum.md:463).
  - "*operational* interference and entanglement predictions require in addition the instrument and
    observable structure of the operational bridge, characterized conditionally and with its
    physical sourcing open" (Main.md:666).
  - Ledger row B-P4-MEAS-5 classifies the derivation of the double-slit pattern as UO.
  - The programme frontier is F2, the sourcing of a nonclassical resource by an extended architecture
    (`PROGRAMME.md`:40).
  - Native attempts on record report no sourced coherent instrument:
    - F2-1: no admissible map `Theta*`.
    - PC-1: void, 25 candidates screened.
    - MR-1: stage-1 token `GAP`, provisional
      (`reconstruction/measurement-record-formation/README.md`:35; preregistration §2.3).

**The pressure test.** The one corpus construction that reproduces interference statistics from
definite configurations is the gluing theorem and its single-controlled-dynamics corollary.
- Its hidden sector holds "the unnormalized branch matrix (a density register)" (Main.md:574).
- "Quantum mechanics enters as the instrument data and as the state held in the hidden register"
  (Main.md:590).
- The superposition is therefore an input of the realization, stored digitally in definite
  configurations, not an output derived from them.
- This is a definite-ontology encoding of a supplied quantum state, analogous in role to a stored
  pilot wave. It shows compatibility, not the reversal of explanatory direction.

**Representation route.** `S <=> D <=> Q_fb` does give a unitary Born representation of any visible
law, but it does not carry the reversal.
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
| Records are definite configurations | conditional consequence | Main.md:42; Substratum.md:94, 465 | Definition and A2 (premises; A1 open and not adopted, not needed here) |
| Every finite stochastic law has a finite reversible realization | kernel theorem | `S_imp_D`, `finite_horizon_equivalence` (Equivalence.lean:462) | finite alphabet and horizon; realization depends on law and horizon |
| Finite action-labelled families, including LG-violating ones, have one permutation-instrument realization | paper proof | Main.md:490, 494 | per finite menu and horizon |
| No fixed finite realization is exactly equivalent to a qubit | paper proof (factorization half); imported unboundedness | Main.md:568 | factorization interface |
| The stated observer interface is operationally classical (nonnegativity-bounded; no phases; no dense control) | kernel theorem | `obsTheory_nonnegBounded`, `frozen_sourcing_verdict`, `nonnegBounded_verdict`, `sourcing_rule_independent`, `substratumGen_not_control`, `obs_not_layerFlowExecutable` | finite carriers; stated architecture; every rule |
| Every effect in the monomial class is diagonal | paper proof (Stage 1 R5 derivation from the definitions; not a stated kernel theorem) | `InstAvail` (ImplementationLocality.lean:268), `preservesDiag_conj_of_monomial` | same scope |
| "No collapse needed" in this class is the trivial classical case | paper proof (this report, from the two rows above) | Main.md:664 | stated architecture |
| Interference derived from substratum dynamics | open question | Main.md:666, 694; Substratum.md:463; ledger B-P4-MEAS-5 | — |
| Interference statistics reproducible by a definite reversible machine | conditional consequence | Main.md:574–590 | supplied quantum instrument data and initial state in the hidden register; finite accuracy; finite menu |
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
- **If reconstruction succeeds.**
  - Under the five completion conditions, available families are exactly the normalized Kraus
    instruments (kernel: `exactAll_iff_physical_general`, GeneralCarrier.lean:100).
  - Outcome probabilities then have trace form, but only within complex matrix kinematics "taken as
    given", whose derivation "is open" (Main.md:572).
  - So even the conditional route inherits the trace rule from the kinematics rather than deriving
    it.
  - Gleason-type routes [background] are cited (Main.md, ref. [54]) but are not developed as an OI
    derivation in any passage traced.

### 3.2 Measurement-basis selection

- **Today.** The configuration basis of V is privileged by the ontology. Every available effect is
  diagonal in it (R5). This answers preferred-basis questions only in the trivial sense: no other
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
  - Reading a definite configuration twice, with no intervening change, gives the same value. This is
    definitional.
  - Passive reading is a projection and so idempotent (kernel: `internal_branch_eq_blockPart`).
  - Record persistence until readback holds by reversibility in every bijective realization (paper,
    Main.md:18, 80: C2-structural).
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
    (paper, Main.md:698–704; ledger B-P4-MEAS-2 DM).
  - Nested trace-outs agree (GR.md:729–751, Theorems A.1–A.4). Corollary A.3, Hamiltonian
    consistency, is conditional on H-BG and the §3.3 hypotheses.
  - In the operationally classical class, agreement on comparing records is automatic: there is one
    configuration.
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
    research record).
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
    only a preregistration. Ledger A-BELL is UO.
- **If reconstruction succeeds and H-Bell holds.** Quantum CHSH values become reachable with
  operational no-signalling. Tsirelson selection (BELL-QSET) is a further open obligation.

### 3.8 Measurement rules status table

| Rule | Status today | If reconstruction succeeds | Missing mechanism or premise (corpus record) |
|---|---|---|---|
| Born rule | Definitional in `Q_fb`; exponent not selected; physical measure posited by (iv); "not yet shown to derive" | Trace-form probabilities for all Kraus instruments, within complex matrix kinematics taken as given | Derivation of the kinematics (Main.md:572); exponent and measure selection (`born-sel-b-measure-20261104/QB3-EVIDENCE.md`; ledger B-QM-11 UO) |
| Basis selection | Configuration basis privileged by premise; only diagonal effects available (trivial) | Basis set by the available coupling before readout | Native apparatus or record formation: `repeatable-measurement-feasibility-20261118/DECISION.md` (NOT PASSED); `measurement-record-formation/` (`GAP` provisional); `meas-q-20261120/RESULT.md` |
| State update | Bayesian conditioning, diagonal sector (Main.md:664); passive reading `P_o rho P_o` (kernel); local Lüders readout from spectator independence (kernel) | General Kraus update | Sourcing of non-commuting instruments: F2, `PROGRAMME.md`:40; coherent-input update, "operational bridge" (Main.md:664) |
| Repeatability | Definitional for configurations; idempotent passive reading (kernel); persistence by reversibility (paper) | Projective repeatability within QM | Native record surviving re-arming (`repeatable-measurement-feasibility-20261118/DECISION.md`); MEAS-Q MQ4 record erasure |
| Observer agreement | Joint law for ordinary Wigner's friend (paper); nested trace-out consistency (paper, partly conditional); trivial in classical class | Extended-Wigner protocols computable | Superobserver coherent operations (unsourced); FR and local-friendliness premise analysis (Main.md:704; appendix-c C.3; open) |
| Contextuality | KS contextuality only with supplied data (Main.md:580); native fragment simplex-embeddable under OA-2 hypotheses; classical gbit at bounded horizons | Inherited from QM | A native non-simplex-embeddable fragment (`oa-2-20261112/STATUS.md`; "Open: G3 for admissible non-affine rules") |
| Bell correlations | CHSH <= 2 for screened local completion; PR boxes in bare OI; adopted branch: ontic parameter dependence; H-Bell open | Quantum CHSH with no-signalling, if H-Bell holds | H-Bell (i)–(iii) (Substratum.md:131–133; `h-bell/round-hb-1-obligation-shape/`, preregistration only); BELL-QSET and Tsirelson selection (ledger A-BELL UO) |

### 3.9 Classification (Question 2)

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| Born form part of `Q_fb` | paper proof (definitional) | Main.md:18, 288–290, 564 | fixed-basis class |
| Born exponent not selected | paper proof (construction is exponent-blind) | Main.md:564; probe check 6 | — |
| Born rule or physical measure derived | open question | QB3-EVIDENCE.md:5; ledger B-QM-11 | — |
| Kraus instruments iff five conditions | kernel theorem | `exactAll_iff_physical_general` (GeneralCarrier.lean:100) | complex matrix kinematics taken as given; finite carrier |
| Monomial class plus tunable state mixing gives exact finite operational QM | kernel theorem / conditional consequence | `substratum_plus_control_qm` (StructuralClosure.lean:397) | added operation (unsourced) |
| Diagonal-sector Lüders = conditioning | paper proof | Main.md:664 | diagonal sector |
| Passive reading `P_o rho P_o` | kernel theorem | `internal_branch_eq_blockPart`, `internal_outcome_law` | matrix kinematics |
| Readout is local Lüders | kernel theorem | `readout_is_localLuders` | `FiniteOperationalTheory` rule (e) |
| Native repeatable apparatus | missing mechanism | `repeatable-measurement-feasibility-20261118/DECISION.md`:3 | fixed ring interface |
| Ordinary Wigner's friend joint law | paper proof | Main.md:698–704 | common joint preparation |
| KS contextuality of deterministic reproductions | conditional consequence | Main.md:580; KS [background] | supplied quantum data, `d >= 3` |
| Native fragment simplex-embeddable | conditional consequence (research record) | OA-2 STATUS:62 | (H1), H-AR, (H3), (H4), (SP), (xiv) |
| Stated architecture's prepare–measure theory simplex-embeddable | paper proof (this report; from R5) | R5; arXiv:1911.10386 | finite carriers, monomial class |
| CHSH <= 2 for screened local completion | paper proof | Main.md:370–397 | conditions (i)–(iv) |
| Measurement independence | posit | Main.md:410–416 | — |
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
  (Stage 1 N3). That concerns Axiom 1's warrant, not definiteness of physical records.

### 4.2 Do the weights depend on epistemic conditioning?

- **Yes.** Stage 1 R2 holds: the observer's predictive laws are pushforwards of
  `mu_prep(. | R)` (`pushforward_identity`, HiddenMemory.lean:83). Further knowledge K gives
  `mu_prep(. | R, K)`.
- Posit (iv) selects "the maximal-entropy invariant measure compatible with the observer's records",
  labelled "a standard but substantive epistemic postulate" (Main.md:736).
- Which conditioned law the quantum state corresponds to is open.
- For this report the consequence is specific. Even at the statistical level, "without a theory of
  knowing" holds only if the conditioning is on physical records `R` alone. Whether quantum weights
  are `mu_prep(. | R)` and never `mu_prep(. | R, K)` is not settled.
- In the trivial classical class, the "collapse" when an observer learns is Bayesian conditioning.
  This is not specific to quantum mechanics.

### 4.3 The closed-eyes detector case

Three events: (1) system–detector interaction, (2) the detector registers, (3) the scientist learns.

**(a) Is the detector an observational locus?** Yes.
- "the Definition covers every registering locus, and for a detector or a horizon that a registering
  occurs is a physical fact" (Main.md:36).
- With the detector as V (Main.md:42), event 2 is the detector's configuration taking a definite
  value. Event 3 is a later coupling of the scientist's configuration to the display.
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
  but trivially: any classical stochastic theory models it.
- With a class containing a non-monomial operation, the same constructors give quantum feed-forward:
  - in the exact theory, via `substratum_plus_control_qm` and `exactAll_iff_physical_general`;
  - in the gluing construction, adaptive protocols to accuracy epsilon with supplied data
    (Main.md:576, 590).
  Both are conditional on unsourced resources.

**(c) Wigner-type agreement and interpretation dependence.**
- In OI's ontology "an outcome already exists" at event 2 is true by premise (Substratum.md:465,
  Main.md:704). In Everett-type readings [background] it is not, and in QBism [background] it is
  agent-relative.
- The case is therefore interpretation-dependent at the ontological level. Stating it does not favour
  OI over Bohmian mechanics, which also has a definite record at event 2 [background].

**(d) Does the case separate the levels?** Yes.
- Events 1–2 are ontological: definite by premise. Event 3 is conditioning.
- Neither says why the detector's statistics, or a larger observer's statistics on detector plus
  system, are quantum. That is the operational and statistical content, which is not established
  (Sections 2–3).
- The owner's reading — knowledge does not make the outcome real, the outcome is acquired because it
  exists, and quantum rules still need derivation — matches OI's premises. The case confirms the
  separation; it does not reduce the operational or statistical burden.

### 4.4 Four notions kept separate; Wigner's friend and local friendliness

**Definiteness** (substratum level). A premise (2.1). It does not rest on irreversibility: OI's
dynamics is a bijection, so no record is fundamentally irreversible. Records persist until readback
by reversibility (Main.md:18). They can be erased: confined classes on rule Q erase their records
(MEAS-Q MQ4).

**Decoherence** (effective-description level). Not derived in any passage traced.
- Main.md:730: on coherent inputs the permutation unitary "carries visible coherence into the hidden
  register". Whether memory is classical "depends on the realization rather than on the visible law".
- So the visible law does not fix coherence properties. Coherent inputs are not available to
  embedded observers in the stated architecture (2.3).

**Irreversibility.** Effective only. The substratum is reversible (A2). Records can be overwritten by
later dynamics while having existed definitely.

**Inter-observer agreement.** For the ordinary Wigner's friend, a joint law exists (3.5). For
genuinely quantum extended protocols it is not modelled.

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
- **Absoluteness of Observed Events.** OI's ontology satisfies it by premise. "In Wigner's friend,
  the Friend has a definite outcome" (Substratum.md:463); one trajectory (Substratum.md:465).
- **No-Superdeterminism.** OI retains measurement independence as a posit (Main.md:410–416).
- **Locality.** Main.md:418 adopts "ontic parameter dependence", one wing's response depending on the
  remote setting, with operational no-signalling required.
- **Conditional conclusion.** If OI reproduced the quantum predictions of an extended Wigner's-friend
  protocol, the assumption it would have to drop is Locality. This matches its adopted Bell branch.
  - Conditions: reconstruction succeeds (F2, open), H-Bell or an equivalent response structure
    (open), and OI's ontic dependence being the kind that violates Bong et al.'s Locality. That
    Locality constrains probabilities of observed events, including friends' events, not only
    operational signalling [background, definition not retrieved in full].
  - Whether that violation is compatible with OI's required operational no-signalling for the
    compared records is open. No corpus passage analyses it.
- **Corpus treatment.**
  - A corpus-wide search found local friendliness only in `book/appendix-c-objections.md` (C.3). It
    says "Observer-relative information alone does not establish which local-friendliness premise a
    proposed completion violates" and that this requires "separate checks".
  - Frauchiger–Renner is stated unresolved (Main.md:704; appendix-c C.3).
  - No paper, Lean module or programme record analyses Bong et al. or Proietti et al.
  - OI keeps (S), single outcomes, by premise. Whether (Q) or (C) fails for an OI completion is
    undetermined [background on the definitions].
- **The essential question.** How can observers have different operational descriptions of one
  reality and agree on comparison? OI answers for the ordinary friend (one joint law). For extended
  protocols it cannot answer yet, and the no-go results indicate the answer must involve ontic
  nonlocality, under OI's own posits.

### 4.5 Classification (Question 3)

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| Definiteness and operation classes need no notion of knowing | paper proof (textual and definitional trace) | Main.md:36, 42; OIRealization.lean:289; Stage 1 §8.3 | search scope of Stage 1 |
| Stochastic weights depend on conditioning on records (and further knowledge) | kernel theorem (pushforward) plus paper | `pushforward_identity`; Main.md:58, 736 | Stage 1 R2 |
| Which conditioned law is the quantum state | open question | Main.md:58 vs 60, 736 | posit (iv) not reinterpreted |
| Detector is a registering locus | paper proof (textual) | Main.md:36, 42 | Definition |
| Feed-forward is modelled (`bind`, `readout`, policy step) | kernel definitions plus paper | ImplementationLocality.lean:268; Main.md:590 | — |
| In the stated class that feed-forward is classical (trivial) | paper proof (from R5) | R5; `frozen_sourcing_verdict` | monomial class |
| Quantum feed-forward | conditional consequence | `substratum_plus_control_qm`; Main.md:574–590 | added coherent operation, or supplied quantum data |
| Closed-eyes case separates ontological from operational and statistical levels, and does not discriminate OI | paper proof (this report) | 4.3 | — |
| Definite record plus superobserver interference exhibited in OI | open question | 2.3 kernel no-go; Main.md:574 | — |
| Under OI's posits a reproduction of extended-Wigner predictions must drop Locality | conditional consequence | arXiv:1907.05607 (abstract); Main.md:410–418; Substratum.md:463–465 | reconstruction (F2), H-Bell, Bong et al.'s exact Locality [background] |
| Compatibility of that with operational no-signalling | open question | appendix-c C.3; no paper analysis | — |
| FR premise failing for OI | open question | Main.md:704; appendix-c C.3 | — |
| Decoherence derived | missing mechanism | Main.md:730 (realization-dependent); no derivation traced | — |

***

## 5. Question 4: structural resolution, organized by level

### Ontological level
- **Established:**
  - definiteness and no branching, by premise (Definition, A2);
  - consistency of a definite reversible ontology with any finite record table (kernel `S_imp_D`;
    paper Main.md:490, 574–590);
  - per-realization nonuniformity (paper Main.md:496, 568).
- **Conditional on reconstruction:** none. This level does not depend on it.
- **Unresolved:** whether the definite ontology is the one nature has (Main.md:732: "what is
  empirically falsifiable is the framework's physical identification of nature"; no memory falsifier
  is established, Main.md:730).

### Operational level
- **Established:** the stated architecture is operationally classical (kernel), so the measurement
  problem's quantum content does not arise there.
- **Conditional:** with an added tunable state-mixing operation, exact finite operational QM follows
  (kernel `substratum_plus_control_qm`; `carrier_general_oiPlus`).
  - Open steps: F2 sourcing (`PROGRAMME.md`:40, Arc D); the physical lift seam to instruments and
    composites (`PROGRAMME.md`:474); Arc E composites and Bell (`PROGRAMME.md`:489).
- **Unresolved even if F2 succeeds as stated:** whether the added resource is derived from definite
  dynamics or posited. The programme states that "assuming the resource as a premise states it
  without sourcing it" (`PROGRAMME.md`:40). If it is posited, superposition is added, not derived, and
  the reversal fails at this level.

### Statistical level
- **Established:** Born form by definition; diagonal-sector conditioning; Lüders readout form within
  `FiniteOperationalTheory` (kernel).
- **Conditional:** trace-form probabilities and Kraus update, within the given complex kinematics.
- **Unresolved even then:**
  - the kinematics' derivation (Main.md:572);
  - Born exponent and measure (QB3-EVIDENCE.md:5);
  - whether quantum weights are record-conditioned laws free of non-record knowledge (R2).

### Evaluation of the owner's hypothesis
- The antecedent requires all three levels without a theory of subjective knowing.
- Today level 1 holds by premise, level 2 fails in the stated architecture, and level 3 is
  definitional only.
- If F2 succeeded by positing a coherent resource within given complex kinematics, levels 2–3 would
  hold conditionally. The result would then be a hidden-variable-type account with ontic
  nonlocality, comparable in explanatory structure to Bohmian mechanics.
- "Without subjective knowing" would hold for levels 1–2. For level 3 it would turn on the open
  status of `mu_H` (R2).
- The reversal of explanatory direction — superposition from definite reality — would be achieved
  only if the coherent resource and the kinematics are derived from the substratum. No corpus result
  indicates how.

### Classification (Question 4)

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| Ontological level addressed by premise | conditional consequence | Main.md:42; Substratum.md:94, 465 | Definition, A2 |
| Operational level not addressed in stated architecture | kernel theorem | `frozen_sourcing_verdict`, `nonnegBounded_verdict`, `substratumGen_not_control` | finite carriers |
| Operational QM given an added mixing operation | conditional consequence (kernel) | `substratum_plus_control_qm`, `exactAll_iff_physical_general` | added operation; given kinematics |
| Statistical level: Born by definition only | paper proof | Main.md:18, 564 | — |
| Kinematics, exponent and measure derivation | open question | Main.md:572; QB3-EVIDENCE.md:5 | — |
| Reversal of explanatory direction achieved | missing mechanism | PROGRAMME.md:40 | native derivation of the coherent resource |

***

## 6. Question 5: distinctiveness

### 6.1 Comparison with other approaches

**Bohmian / pilot-wave** [background].
- Shared: a definite configuration ontology; quantum predictions as statistics; nonlocality (book
  appendix-c:158 says so).
- Bohm derives the full quantum statistics from the guidance equation plus quantum equilibrium. OI
  derives neither.
- OI's only interference-reproducing construction stores the quantum state in a hidden register
  (Main.md:574, 590), a role analogous to the pilot wave.
- The claim that OI "reproduces Bohmian's ... statistical-predictions content without the pilot
  wave's structural cost" (appendix-c:162) is not supported (Section 9).

**'t Hooft cellular automaton** (arXiv:1405.1548v3).
- Both posit deterministic discrete dynamics and claim to dispose of collapse.
- The Bell placement differs: 't Hooft argues superdeterminism can be defended. OI keeps measurement
  independence and adopts ontic parameter dependence (Main.md:410–418, 716).
- Neither, from what was read, derives interference natively for generic rules [background for
  't Hooft's full text].

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
- OI has no derived counterpart of the purity constraint. Its observer theory is
  nonnegativity-bounded.

**Nelson** [background].
- Continuous stochastic process; Wallstrom's quantization objection.
- OI avoids it by not deriving the Schrödinger equation from a process (Main.md:718), which also
  means OI does not derive the Schrödinger dynamics.

**GRW / objective collapse** (contrast) [background].
- Adds stochastic dynamics to make outcomes definite. OI adds nothing dynamical.
- OI's no-collapse is substantive only once interference is reproduced, which it is not (Section 2).

**Everett / relative-state** (contrast) [background].
- OI denies branching by premise (Substratum.md:465).
- Everett's branches are coherent components. OI's stated architecture has no coherent components to
  deny.
- "The Everettian measure problem does not arise" (Main.md:694) is accurate within OI's ontology but
  trivially so (Stage 1 O12).

**Consistent histories** [background].
- OI's substratum fixes one classical measure on configuration histories, in effect a single fixed
  framework.
- Incompatible frameworks (non-commuting history families) have no OI counterpart in the stated
  architecture.

**QBism** (arXiv:1311.5253v1, contrast).
- QBism is agent-centred, with no ontology beneath. OI shares conditioning-dependence of the weights
  (R2) but has a definite ontology.
- OI's claim to provide a "structural why" relative to QBism (Main.md:716) is a self-assessment that
  this report could not trace to an established result (Section 9).

**Spekkens toy theory** (quant-ph/0401052v2).
- The closest precedent for "superposition-like behaviour from restricted knowledge of definite
  states". An epistemic restriction reproduces analogues of interference and noncommutativity but not
  Bell violation or KS.
- OI's stated observer interface does not reach even Spekkens' analogues: only diagonal effects are
  available.
- The corpus itself draws the lesson that "restricted access does not by itself single out quantum
  theory" (appendix-c:214).
- Spekkens' theory is generalized-noncontextual [background], so "interference analogues" are not a
  sufficient test. A substantive resolution must produce a non-simplex-embeddable fragment
  (arXiv:1911.10386).

### 6.2 What is genuinely distinctive
1. A kernel-checked, rule-independent proof that configuration-level embedded observation yields a
   nonnegativity-bounded, hence classical, operation class (`sourcing_rule_independent`,
   `frozen_sourcing_verdict`). This identifies exactly what any embedded-observer explanation of QM
   must add. It is a sharp negative result, not a resolution.
2. An exact finite equivalence `S <=> D <=> Q_fb` with an internal proof. It is universal, so it does
   not discriminate quantum from classical (Main.md:18).
3. The C4 history-readback characterization of a memory-bearing sector (Main.md:18, 97). Its content
   is classical memory, not coherence.
4. An explicit Bell placement with a quantitative measurement-dependence bound (Main.md:429–433).

None of these is a distinctive mechanism for producing quantum measurement behaviour from definite
outcomes.

### 6.3 Classification (Question 5)

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| Definite-ontology account of outcomes is shared with Bohm, 't Hooft, Barandes | paper proof (comparison) | 6.1; external abstracts; [background] | — |
| OI's interference reproduction stores the quantum state (pilot-wave-like role) | paper proof (textual) | Main.md:574, 590 | gluing construction |
| OI instantiates Barandes' tuple; interference term not fixed by visible data | kernel theorem (TI1) plus audit determination (SA2) | PROGRAMME.md:284, 308 | Source A direct branch |
| Bell placement differs from 't Hooft | paper proof | Main.md:410–418, 716; arXiv:1405.1548 | — |
| Rule-independent classical ceiling of configuration-level observation | kernel theorem | `sourcing_rule_independent`, `nonnegBounded_verdict` | stated architecture |
| A non-simplex-embeddable native fragment | open question | OA-2 STATUS ("Open: G3 for admissible non-affine rules") | — |

***

## 7. Three-way partition

### Already addressed (today)
- **Ontological:**
  - definite records and no branching (premise: Definition, A2);
  - a definite reversible ontology is consistent with any finite record table (kernel `S_imp_D`;
    paper Main.md:490, 574–590);
  - registration needs no knower (Main.md:36).
- **Operational:** that the stated architecture is operationally classical (kernel). The measurement
  problem's quantum content therefore does not arise there, trivially.
- **Statistical:**
  - Born form by definition (Main.md:18);
  - diagonal-sector Lüders as conditioning (Main.md:664);
  - passive reading `P_o rho P_o` and local Lüders readout (kernel, matrix kinematics);
  - the ordinary Wigner's-friend joint law (paper).

### Conditional on reconstruction (with the open step named)
- **Operational:** exact finite operational QM, including Kraus instruments, incompatible
  measurements and quantum feed-forward. Requires the added continuously tunable mixing operation
  (`substratum_plus_control_qm`).
  - Open steps: F2 sourcing (`PROGRAMME.md`:40); physical lift seam (`PROGRAMME.md`:474); Arc E
    (`PROGRAMME.md`:489).
- **Operational:** KS and generalized contextuality, inherited from QM.
  - Open step: a native non-simplex-embeddable fragment (OA-2 "Open").
- **Operational:** quantum Bell correlations with operational no-signalling.
  - Open steps: H-Bell (i)–(iii), Substratum.md:131–133; BELL-QSET and Tsirelson (ledger A-BELL).
- **Statistical:** trace-form outcome rule and general update, within the given kinematics
  (`exactAll_iff_physical_general`).
- **Agreement:** extended Wigner's-friend protocols computable. Under OI's posits, Locality would be
  the assumption violated (Section 4.4); the analysis is open.

### Unresolved even if reconstruction succeeds
- Derivation of complex matrix kinematics (Main.md:572).
- Born exponent and physical measure (QB3-EVIDENCE.md:5; ledger B-QM-11).
- Whether the coherent resource is derived from definite dynamics or posited (`PROGRAMME.md`:40).
  This decides whether the reversal of explanatory direction is achieved.
- Whether quantum weights are record-conditioned laws only (`mu_prep(. | R)`) or depend on further
  knowledge (R2; posit (iv) status).
- Compatibility of the required ontic nonlocality with operational no-signalling in extended-Wigner
  protocols (no corpus analysis).
- A native repeatable apparatus with records that survive re-arming
  (`repeatable-measurement-feasibility-20261118/DECISION.md`). This is an engineering-level physical
  sourcing question within the substratum, not supplied by abstract reconstruction.

***

## 8. Limitations

- External sources were read at abstract level. The exact definitions of the Frauchiger–Renner (Q),
  (C), (S) and of Bong et al.'s Locality were not retrieved. The Locality conclusion in 4.4 is
  conditional on them.
- Bohm, GRW, Everett, Nelson, consistent histories, Gleason, Kochen–Specker and PBR are
  [background].
- R5's diagonal-effect statement and this report's simplex-embeddability and feed-forward
  observations are derivations from definitions, not kernel theorems. No Lean was built.
- Research records were read at their stated standing:
  - MEAS-Q, OA-1, OA-2 and QB3 are research records reviewed by agents, not established claims.
  - The unified ledger directory is marked unreviewed; r9 is pending review and r5 is
    owner-accepted.
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

1. **papers/Main.md:692** (mirror Main.tex:5189). "Their quantum behavior is a downstream consequence
   of the trace-out." This is stronger than the evidence. The trace-out gives a representation that is
   universal, Markov included (Main.md:18). Operational quantum behaviour requires the unsourced
   operational bridge (Main.md:666, 694). Kernel: `frozen_sourcing_verdict`. Pattern: representation
   promoted to behaviour.

2. **papers/Substratum.md:463** (mirror Substratum.tex near :2651). Two problems:
   - "The wave function ... is a derived object." The representation exists, but it is non-unique
     (Main.md:656; padding theorem, `PROGRAMME.md`:216) and fixed-basis/diagonal only.
   - "Wigner's superposition reflects his epistemic deficit." Epistemic incompleteness gives a
     mixture. A coherent superposition of Friend's states is not derived as a reduced description,
     and the stated interface cannot distinguish the two (R5).

   Partly right. Related passages:
   - `book/appendix-c-objections.md`:323 ("superpositions are reduced descriptions used by embedded
     observers with incomplete information"; mirror FULL.md:6478, FULL.tex:25426);
   - `book/ch19-open-problems.md`:64 (labelled a proposed interpretation; lower severity).

3. **book/ch01-observation.md:286** (mirror FULL.md:619, FULL.tex:2745). "the modified game whose
   rational odds sheet carries interference terms". The terms are P-indivisibility discrepancies. On
   the Barandes route an interference round is "not well posed" until a candidate is selected
   (`PROGRAMME.md`:377), and native interference is open (Main.md:694).
   - Also ch01:292: "so there was never anything to collapse". This holds only in the operationally
     classical sector.

4. **book/ch18-beyond.md:110** (mirror FULL.md:4841). "Quantum indeterminacy is the cost of partial
   observation, not a feature of reality." In the stated architecture partial observation yields
   classical stochasticity (kernel `nonnegBounded_verdict`). Whether it yields quantum indeterminacy
   (contextual, Bell-violating) is open.

5. **book/appendix-c-objections.md:162** (mirror in FULL.md). "The framework reproduces Bohmian's
   deterministic-substratum and statistical-predictions content without the pilot wave's structural
   cost." OI does not reproduce quantum statistical predictions from its substratum (Main.md:694;
   F1 retired, `PROGRAMME.md`:521). Its only interference-reproducing construction carries the quantum
   state in a hidden register (Main.md:574, 590).

6. **papers/Main.md:716.** "QBism/relational QM: ... this framework provides a structural *why* and
   quantitative predictions." This is a self-assessment not traced to an established result for the
   measurement-relevant content. It may also conflict with AGENTS.md §A.32 (self-assessment outside
   status labels).

Lower-severity wording risk, not an error: **papers/Main.md:694**, "The Born rule, often treated as an
independent postulate, is here part of the exact fixed-basis representation dictionary ... rather
than an additional stochastic axiom". This is literally accurate (definitional), but it can be read as
a derivation. QB3-EVIDENCE.md:5 records that OI has not yet been shown to derive the Born rule.

***

Nothing in this report establishes that OI reproduces quantum mechanics or resolves the measurement
problem; the body shows only that OI posits definite records, proves that its stated observer
interface is operationally classical, and identifies the conditional and missing steps listed above.

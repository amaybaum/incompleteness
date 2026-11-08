# FHE-SEL-1 P-CONTROL: temporal subdivision of interventions (Stage 1A preregistration)

**Standing.** WIP / UNVERIFIED. This is a Stage 1A preregistration under #1169. It contains no derivation,
computation, simulation, Lean build or V3 execution. It adopts no premise and promotes no claim. Independent
review is pending. Writer: Claude Code subagent (P-CONTROL writer). This writer did not read or coordinate with
the P-MIX or P-OBS writers or their branches.

**Authority.**

- Owner decision, #1169 c.6720450946 (amaybaum, 2026-11-08T10:38:44Z), recorded from chat. Stage 1A is approved
  and Stage 1B is gated. The owner's words, in part:
  > **Stage 1A — Approve now.** … It must establish, before any construction's result is evaluated: Independent
  > physical motivation and exact Stage 0 freedom targeted by each construction. Fixed carrier, microscopic rule,
  > observer access, resources and assumptions. … Frozen success, partial-success and failure criteria, including
  > classical-imitation controls. A commitment to report all three outcomes, including negative and inconclusive
  > results.

  The same record sets the portfolio's research question for P-CONTROL: "Can an independently motivated physical
  access mechanism provide new executable interventions?" It also sets the safeguard distinctions (a)–(c) and the
  robustness requirement quoted in §9.
- Planning clarification, #1169 c.6720342295 (amaybaum, 2026-11-08T10:26:34Z). It states the P-CONTROL question:
  "Which independently motivated physical principle of access or intervention, if any, supplies additional
  controllability?" Its safeguards are: "Must not restate completion condition (iv). Must not assume a quantum gate
  repertoire." It defines three statuses: proposed, mathematically sufficient, and derived from native OI. It also
  fixes the order of work: "First, independent physical motivation. Second, evaluation of consequences. Third,
  comparison with the quantum completion conditions. The order is never reversed."
- FHE-SEL-1 decisions, #1169 c.6719386464 (amaybaum, 2026-11-08T08:41:15Z). The owner's words: "Every candidate
  physical restriction must have an independent physical motivation established before evaluating whether it
  selects quantum behaviour. A restriction that eliminates an unwanted classical model is not automatically
  evidence that nature obeys that restriction."
- Coordinator addendum (Stage 1A, binding on this file): a section on explanatory quality under AGENTS.md §A.29 (§11).

**Source snapshot.** Every repository citation is to `main` at `9c201475ba6fd8f341591d14dd8e88db2e2aaa90`.
`Main:N` is `papers/Main.md` line N, and `Sub:N` is `papers/Substratum.md` line N. Lean citations are
`verification/lean-mathlib/OIBridge/<File>.lean:N`, written `<File>:N`. The Stage 0 map (#1169 c.6719708521;
review c.6719720616; confirmation c.6719723538) pins `f88c1842`. Between that commit and `9c201475` there is no
change to `papers/`, `verification/lean-mathlib/OIBridge/`, `mechanism-2-20261108/` or `apparatus-1-20261107/`,
so its line numbers carry over.

Record abbreviations, under `verification/`:

- `M2D` = `programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md`;
- `AP1` = `programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`;
- `ESA` = `audits/foundations/exec-source-audit.md`;
- `LSA` = `audits/foundations/lift-source-audit.md`;
- `CCA` = `audits/foundations/coherent-continuum-source-audit.md`;
- `RPF` = `audits/foundations/real-pair-flow-audit.md`;
- `CTL` = `programmes/oi-qm/reconstruction/physical-controller-20261107/LEAD.md`.

`MI` is M-INACC, `minacc-1-20261108/RESULT.md` with amendments A1–A3, on branch `research/oi-qm-minacc-20261108`
(#1198). It is off main and provisional. `Q3-C2` is the classification standard of PR #1202 (head `25384b13`),
`q3-a6-offsets-20261108/amendments/A1-prereg-review.md` §3, clause C2. It is off main; §3.2 restates it in full.

***

## 0. Summary

- **Selection.** The census (§4) lists 17 candidate principles of access or intervention, from the corpus and the
  literature. The selection rule (§3) was fixed before the census verdicts were written. Under it, exactly one
  candidate is admissible: **TS, temporal subdivision of reversible interventions**. Every other candidate is
  either a restriction, which by its form adds no operation; or configuration-level, which by an on-main
  definitional fact adds nothing to the stated intervention class; or has a motivation that is target-adjacent or
  target-defined; or restates condition (iv).
- **The principle (TS).** A reversible physical process that the observer can carry out can also be carried out
  in two equal halves: some available intervention on the same system, applied twice, equals it. The statement
  names no unitary, gate, rotation, phase or continuity of a family.
- **Motivation.** In classical continuum mechanics, physical change is subdivisible in time: an evolution over a
  duration is the composite of two evolutions over half that duration. Classified **independent**, with three
  qualifications carried throughout:
  1. a nativeness tension: OI's substratum is a discrete-time bijection, and Main:274 states that a continuous
     interpolation of a finite permutation is "additional structure, chosen rather than derived";
  2. a target-informed origin, disclosed in §11.5;
  3. a reclassification rule fixed in advance (§7.3).
- **Stage 0 rows targeted.** Row 9, the access or intervention model, and the §5 entry "(iv) / reversible
  control (9, 13)", at the open alternative "fractional-time layer-flow access" from the trace's Open list
  (c.6713653816). The reach tests (§11.3) also bear on rows 7 (the relating evolution and the branch of the
  logarithm) and 5 (the hidden clock).
- **Ceiling.** Any positive is recorded as (b) at best (§9.3), because the candidate was selected from a census.
  This file sets out what Stage 1B would test. It is not a claim that TS supplies anything.

***

## 1. The question, its safeguards and its anchors

**Question** (c.6720342295). Which independently motivated physical principle of access or intervention, if any,
supplies additional controllability?

**Safeguards.**

- **G-1.** The principle must not restate completion condition (iv): `HasCompositeUnitaryControl`
  (OperationalAssembly:665; Main:564), "conjugation by every unitary on the carrier of every ancilla level is
  available as a single-outcome operation".
- **G-2.** The principle must not assume a quantum gate repertoire.

**Anchors.**

- (iv) fails natively. On the two-state carrier the stated-intervention theory lacks it (`substratumGen_not_control`,
  StructuralClosure:348). In the access model it fails on every nonempty carrier (`permTheory_not_control`,
  SubstratumInterfaceAudit:708). By the trace, it fails on carriers with two or more states by composition, via
  `substratumTheory_not_avail_gateFlow_half` (ExecSource:113). The one-state carrier is not covered.
- Stage 0 places the residual in the access/intervention model, not in the rule. The access model is defined
  without the rule (`obsTheory_rule_independent`, SubstratumInterfaceAudit:780, `rfl`).
- The only existing corpus candidate is Main:590's layer-flow executability, together with its equivalent form,
  "the continuously tunable state-mixing operation … as an empirical controllability resource". Stage 0 classifies
  it as target-adjacent. §4 rows K-1 and K-2 face that classification directly.

***

## 2. Constraints fixed by existing records (cited, not re-derived)

- **C-1. Maximality of the stated class at configuration level.**
  - `ConfigurationLevel 𝓘` means that every operator in 𝓘 is monomial (ManuscriptAxioms:125).
  - The substratum class is exactly the monomial class (StructuralClosure:180).
  - A class is therefore configuration-level exactly when it is contained in the stated class
    (`configurationLevel_iff_le_substratum`, ManuscriptAxioms:134, `Iff.rfl`).
  - This is definitional. Its physical content is the interface reading under which a process acting on
    configurations is represented by monomial operators, or by a channel with monomial Kraus operators:
    - read-write operators are monomial (`readWriteOperator_supplied`, StructuralClosure:336);
    - a classical stochastic map has one exhibited monomial Kraus form (`stochasticChannel_kraus_monomial`,
      LiftSource:251).

    LSA does not claim that every Kraus realization is monomial.
  - **Consequence used for selection.** No access principle whose added operations are configuration-level adds
    an operation to the stated-intervention theory.
- **C-2. Necessary conditions for layer-flow executability.**
  - Executing a layer flow requires a non-monomial admissible operator at level one
    (`exists_nonMonomial_of_layerFlowExecutable`, ExecSource:52).
  - It also requires an uncountable family of non-monomial rays (`uncountable_of_layerFlowExecutable`,
    PolarizationClosure:135).
  - A theory that preserves diagonal states executes none (`not_layerFlowExecutable_of_preservesDiag`,
    LiftSource:70).
  - These enter **only** as comparison facts and as the cardinality check of §11.3. No selection criterion refers
    to them.
- **C-3. MECH-2 Theorem NC** (M2D:65–71, node 4 at M2D:483).
  - Statement: under Lemma F's operation set, an injective identification and spanning-read certification, the
    configuration model is a noncontextual model of the whole encoded theory, for any dynamics.
  - TS changes the access. It adds operations that are not in Lemma F's operation set (attach, apply the rule,
    feedback, discard, condition). So NC's operation-set hypothesis fails for the TS-extended theory, and NC does
    not by itself supply a classical imitation.
  - The classical-imitation countercontrol (§10, CI-1 to CI-3) must therefore exhibit an imitation or exclude
    one.
- **C-4. Finite carriers.**
  - Theorem U2 (M2D:55, node 3 at M2D:349): on R1^⊗n under H-LIFT, the encoded unitaries induced by a fixed
    bijection lie in `A_4 ≀ S_n`.
  - AP1's C-ROT (AP1:772): `rot` is unavailable under R1.
  - TS's added operations are not induced by a fixed bijection. A Stage 1B claim that an encoded operation lies
    outside U2's group must name the U2 hypothesis that fails.
  - No claim of exact continuous rotations may rest on a change of representation.
  - Q-B is not activated.
- **C-5. M-INACC** (provisional; off main). Under `G_σ`, registration and refill leak the "protected"
  functional. P-GK is the only listed premise that blocks every exhibited exposure, and it is degenerate. PROT-R′
  (A3) is offered to successor units. Any Stage 1B step that needs hidden data to stay inaccessible inherits
  M-INACC's missing premise unless that step sources it.
- **C-6. Supplied versus generated.** TS is a supplied access principle. Its ledger entry stays "supplied" until
  a derivation from `(S, φ)` with native access exists (§6.4).
- **C-7. Discrete substratum.** "A finite permutation does not by itself generate a continuous flow … any
  continuous one-parameter interpolation is *additional structure*, chosen rather than derived" (Main:274). TS is
  weaker than an interpolation, but it is of the same kind and is recorded as added structure.
- **C-8. Lean.** No `readWriteSourced_*` identifier is cited (#1188). Main:590's clause "even with genuine
  hidden-memory and readback behavior, does not itself generate quantum state mixing" cites
  `readWriteSourced_not_qm`, which is vacuous. Nothing here relies on that clause.
- **C-9. Alphabet.** `q = 2` throughout, so nothing is conditional on #1193. A `q = 4` variant enters only as a
  robustness check (R-4).

***

## 3. Selection rule and classification standard

### 3.1 Selection rule

This rule was fixed before any census verdict was written. A candidate is **admissible** iff all six clauses hold.

- **S1, kind.** It is a principle of access or intervention. It says what an embedded observer can do, not what
  the microscopic rule is.
- **S2, generativity.** As stated, it adds at least one intervention to the stated-intervention theory
  `genTheory substratumClass`, or it is not decided by C-1 to add none. A pure restriction answers the question
  "no" by its form. A principle whose added operations are configuration-level adds nothing, by C-1.
- **S3, motivation.** Its motivation is classified **independent** under §3.2, judged on the principle alone.
  Mixed candidates are recorded but not admitted.
- **S4, safeguards.** It is not condition (iv), and not a statement that includes unitary conjugations,
  non-monomial operators, layer flows or a named gate set (G-1, G-2). It also passes the functional test of §3.2.
- **S5, carrier.** It can be stated on a finite carrier at `q = 2` without a change of representation, or it
  states its carrier explicitly.
- **S6, reuse.** Its consequence for this question is not already decided on main for the same class (owner
  refinement 2, c.6719386464: "Existing evidence is reused, not redone").

If no candidate is admissible, the preregistered outcome is the null (§5). If more than one is admissible, the
tie-break is fixed in advance and is target-blind:

1. fewer added primitives;
2. then native expressibility (stated using only `(S, φ)`, the stated access and the interface).

### 3.2 Classification standard (Q3-C2, adapted)

Q3-C2 is adapted with `T` = "condition (iv), or quantum behaviour, or the completion conditions". The assumption is
judged **on its own**: what it yields together with the closure goes into the consequences, never into the
classification. No clause counts deriving or failing to derive `T` as a merit or a demerit.

- **independent.** The stated motivation and its support do not presuppose `T`, and are not designed to exclude a
  particular construction.
- **target-adjacent.** Taken on its own, the assumption or its motivation:
  - presupposes `T`;
  - is logically equivalent to `T` on the class at issue; or
  - is supported only by a consequence of `T`.
- **target-defined.** Either of the following:
  - The stated reason is to obtain `T` or to exclude a particular construction.
  - **The functional test** (after Q3-C2's F5): the assumption's statement is itself an inclusion of operations of
    the class that (iv) adds (unitary conjugations; non-monomial or non-diagonal-preserving operators; layer
    flows), and it has no stated effect outside that class.
- **mixed.** An independent component together with a target-adjacent component, each identified.
- **none found.** No motivation located after the search (§4 lists the search).

**Calibration, fixed in advance and checked at Stage 1B before any outcome (C-CAL).**

- (a) A3's locality motivation (Sub:96) must classify as independent.
- (b) Main:590's layer-flow executability must classify as target-adjacent or target-defined.
- (c) The target-tuned countercontrol TS⁺ (§10, TT) must classify as target-adjacent or target-defined.

If any calibration fails, the standard is miscalibrated. No outcome is then rendered until a disclosed amendment
repairs it.

***

## 4. Census of candidates (owner distinction (b): selection made visible)

**Searched.**

- Corpus: `papers/*.md`, `book/*.md`, `verification/` and the Lean modules, for access, intervention, control,
  controllability, subdivision, square root, intermediate time, divisible, wave lift, settings and constructor.
- Every candidate in the corpus's three sourcing censuses: ESA X1–X8, CCA S1–S9 and RPF S1–S4.
- Literature as listed in the References.

No corpus record states a subdivision principle for interventions. The phrase "subdividing … through the group
law" in RPF:200 and README:1506 is a proof step inside the pair-flow reduction, not a principle.

**Column key.** "Dec." means decided on main, or by C-1. "Disposition" gives the clauses failed.

| # | Candidate (source) | Kind | Motivation and classification (§3.2) | Generative? / Dec. | Disposition |
|---|---|---|---|---|---|
| K-1 | Layer-flow executability (Main:590; `derivedOI_qm_iff_layerFlowExecutable'`, DerivedQ3:222) | access | "an assumption not derived"; in the corpus, its role is to complete the characterization. Target-defined under the functional test: its statement includes layer flows and has no other stated effect. Logically equivalent to QM given the closure: target-adjacent | yes / stipulation; unsourced (`obs_not_layerFlowExecutable`, ExecSource:129; `substratumTheory_not_layerFlowExecutable`, LiftAudit:200) | Rejected: S3, S4 (G-1 in substance) |
| K-2 | Continuously tunable state-mixing operation "as an empirical controllability resource" (Main:590; `substratum_plus_control_qm`, StructuralClosure:414; CCA S8) | intervention | Motivated by the observed controllability of quantum systems: target-adjacent. With the closure it equals QM. Functional test: target-defined | yes / stipulation | Rejected: S3, S4 (G-1, G-2) |
| K-3 | Real pair flow: a continuous one-parameter real-orthogonal action on one pair (RPF; `PairFlow`, RealPairFlow:41) | intervention | Orthogonality is preservation of a Euclidean (`ℓ²`) norm on an amplitude pair. Preserving the `ℓ²` norm under nontrivial linear maps is the quantum case, against `ℓ¹` for stochastic maps (Aaronson 2004). The motivation presupposes an amplitude carrier: target-adjacent | yes / sourcing negative (RPF outcome 2) | Rejected: S3, S5, S6 |
| K-4 | Continuous reversibility between pure states (Hardy 2001, Axiom 5; Masanes–Müller 2011) | access | Introduced in those works as the axiom that separates quantum from classical theory. Hardy notes that dropping "continuous" gives classical probability. The stated reason includes obtaining `T`: target-defined | yes / — | Rejected: S3 |
| K-5 | Fractional-time access to the substratum's own layers (ESA "next decision"; trace Open list) | access | In the corpus its stated reason is to source the layer flow: target-defined as stated there. TS (K-17) is a separately motivated principle of the same kind | yes / not decided | Rejected as stated: S3. See K-17 |
| K-6 | Observer-level wave lift `φ → L_obs` (SM:232; ESA X7; LSA; CCA S7) | access / identification | Its purpose in SM:232 is emergent field propagation, the target's emergent description: target-adjacent. The independent component is linear coupling to collective amplitudes (classical linear response). Mixed. The amplitude space is a change of carrier, and at `q = 2` its `ℤ₂`-linear form is configuration-level. Classical waves admit an exact classical description (Spreeuw 1998) | underdetermined on main (LSA:351–355) | Rejected: S3 (mixed), S5 |
| K-7 | Locality of interventions; implementation locality (A3, Sub:96; `validity_of_implementationLocality`) | restriction | Relativistic causality, action by contact: independent | no: restricts | Rejected: S2. Kept as a constraint on TS (§6.3) |
| K-8 | Thermodynamic and finite-resource limits on control (Landauer 1961; Bennett 1982; third law, Masanes–Oppenheim 2017) | restriction | Independent | no: restricts | Rejected: S2. Kept as the resource ledger (§6.4) |
| K-9 | Wigner–Araki–Yanase limits on measurement and control under conservation laws (Araki–Yanase 1960) | restriction | Stated for quantum operations: target-adjacent | no | Rejected: S2, S3 |
| K-10 | Causal intervention: hard and soft interventions, modularity (Pearl 2009; Woodward 2003; Eberhardt–Scheines 2007) | intervention | Independent. Its interventions replace mechanisms by stochastic kernels on variables: configuration-level | no, by C-1 | Rejected: S2 |
| K-11 | Continuous macroscopic settings: a real-valued control knob (ESA X3; `ReadWriteFamily`) | access | Independent (classical control) | no: permutation-valued at every parameter (`bijectionLevel_not_layerFlowExecutable`, ExecSource:89; CCA S3) | Rejected: S2, S6 |
| K-12 | Constructor-theoretic closure of possible tasks (Deutsch 2013; Deutsch–Marletto 2015) | access | The composition closure is independent. Interoperability and superinformation media are introduced to recover quantum-information features: target-adjacent. Mixed. On a finite bijective substrate the closure stays inside the permutations | no, by C-1 (closure part) | Rejected: S2, S3 |
| K-13 | Control mediated by hidden memory: act on visible cells through the hidden sector's write-then-read (C4; Main:82) | intervention | Independent: indirect control through a coupled environment. Its operations are permutations of `C_V × C_H` followed by discard: configuration-level | no, by C-1. Not decided by the vacuous `readWriteSourced_not_qm` (C-8) | Rejected: S2 |
| K-14 | Kalman or reachability controllability of the finite dynamics (Kalman 1960) | criterion | Independent. It is a property to evaluate, not an added access | no | Rejected: S1, S2 |
| K-15 | Predictive-state identification: the observer's state is its predictive content (Main:622, K7; Shalizi–Crutchfield 2001; Jaeger 2000) | identification | Operational equivalence: independent. It adds no intervention and re-represents existing ones, which on a finite carrier C-4 bars as a source of rotations | no | Rejected: S1, S2. It bears on identification, which is outside this question |
| K-16 | Knowledge-balance restriction (Spekkens 2007; AP1 P2) | restriction | Proposed to reproduce quantum phenomena: target-adjacent | no | Rejected: S2, S3 |
| K-17 | **TS: temporal subdivision of reversible interventions** (this file, §6.2) | access / intervention | Subdivisibility in time of physical change (classical flows): independent, with the qualifications of §7 | not decided by C-1. Its additions are not configuration-level by statement; whether they are is F1/F2 (§9). Not decided on main (search above) | **Admitted** |

**Tally.**

| Outcome | Rows |
|---|---|
| Rejected for target-adjacent, target-defined or mixed motivation | K-1 to K-6, K-9, K-12, K-16 |
| Rejected as restrictions, as configuration-level, or as not an access principle | K-7, K-8, K-10, K-11, K-13 to K-15 |
| Admitted | K-17 |

**Which clause did the work.** S2 is the clause that removes the independent but configuration-level candidates
(K-10, K-11, K-13). It does so through C-1, which is definitional. The question's word "additional" relative to the
stated class therefore coincides with the necessary condition C-2 for the target. That coincidence follows from the
question's wording and C-1, and the criterion does not cite C-2. Even so, it narrows the census toward the target's
necessary condition. It is recorded as a selection effect, and it is one reason for the (b) ceiling in §9.3.

***

## 5. Selection outcome, and the null

The admissible set is {K-17}. Had it been empty, the preregistered outcome would have been:

> **P-CONTROL null.** No principle of access or intervention in the corpus or the cited literature is generative
> relative to the stated-intervention theory, expressible on a finite carrier, undecided on main and
> independently motivated. The residual of Stage 0 row 9 stays open with no candidate.

The null remains the outcome in three cases:

- Stage 1A review reclassifies TS's motivation as other than independent;
- the C-CAL calibration fails and is not repaired; or
- the owner declines Stage 1B for P-CONTROL.

In each case the report states the null in the words above and names the census row that would come next under
§3.1. There is none: every other row fails S2 or S3.

***

## 6. The construction PC-TS

### 6.1 Carrier and microscopic rule

- **Operational carrier.** A nonempty finite set `S`, used inside the finite operational interface of Main:564
  (`FiniteOperationalTheory`, OperationalAssembly), with the ancilla levels `S × Fin n`. The interface's complex
  matrix kinematics is imported (§6.4, row L-7).
- **Two scopes, both fixed now.**
  - **Scope Φ (native processes).** `S` is the configuration set of the wave substratum
    (`waveSubstratum`, SubstratumInterfaceAudit:177), with `d = 1`, `q = 2` and ring length `L` in {3, 4, 5}. The
    rule is `waveRule` (:164): second-order, linear, centre-free and translation invariant. It satisfies A1 to A5,
    and its layers are the shear and swap layers.
  - **Scope A (all reversible interventions).** Every nonempty finite carrier. The two-state carrier `Fin 2` is the
    minimal instance and the one on which `substratumGen_not_control` is proved.
- **Base access.** Two theories, both fixed:
  - (b) the stated-intervention theory `genTheory substratumClass` (StructuralClosure:180; ImplementationLocality:852),
    which contains the permutations, the phases and the read-write operators;
  - (a) the access model `obsTheory 𝒮 = permTheory 𝒮.Conf` (SubstratumInterfaceAudit:780), for scope Φ.

### 6.2 The access principle TS (frozen wording)

> **TS (temporal subdivision).** For every operation `T` in the domain `D`, at every ancilla level `n`, there is
> a single-outcome operation `H` available at the same level with `H ∘ H = T` (composition of channels).

- **Domain.**
  - Scope Φ: `D_Φ` is the substratum's own update and its two layers, as available single-outcome operations at
    each level (`obs_dynamics_avail`, `obs_shear_avail`, `obs_swap_avail`, SubstratumInterfaceAudit:790, :800,
    :806).
  - Scope A: `D_A` is every single-outcome operation of the base theory that is conjugation by a monomial unitary
    (permutation times unimodular phases).
- **Not stated.** TS does not say that `H` is unitary, a conjugation, unique, continuous in any parameter, or part
  of a one-parameter family. It names no gate or rotation.
- **The extended theory.** A **TS-extension** of a base theory is a theory that:
  - contains the base theory;
  - satisfies rules (a)–(f) of `FiniteOperationalTheory` (Main:564); and
  - satisfies TS.

  Several roots may exist. TS is existential, and Stage 1B does not choose a root (§11.2, A-root).

### 6.3 Observer access, preparation, records and resources

- **Observer access.** The base theory's operations together with the TS roots. Implementation locality (K-7) is
  kept as a constraint: a root of an operation supported on a region acts on that region and as the identity on a
  spectator (condition (iii) form).
- **Preparation.** The interface's uniformly mixed ancilla attachment (rule (d)). No other preparation is
  supplied.
- **Records.** The interface's ancilla readout (rule (e), `readout_is_localLuders`, OperationalAssembly:658). No
  record mechanism is added. Record retention and leakage belong to P-OBS and are not modelled here.
- **Resources.** Time is counted in operation applications. TS treats a root as one operation, so the resource
  ledger counts the half-step as one supplied primitive per element of the domain (L-5).

### 6.4 Source ledger

| # | Element | Class |
|---|---|---|
| L-1 | Finite configuration carrier (A1) | native |
| L-2 | Bijective rule and its layers (A2; `waveRule`) | native |
| L-3 | The stated access: every permutation (access model), or read-write and bijective interventions (theory (b)) | supplied (the stated access; Main:590) |
| L-4 | The phase intervention | supplied ("a stated intervention principle", Main:590) |
| L-5 | TS roots | supplied (the proposed principle) |
| L-6 | Ancilla attachment, readout, discard (rules (d)–(f)) | supplied (interface) |
| L-7 | Complex matrix kinematics of the interface | imported ("taken as given … derivation from operational premises is open", Main:564) |
| L-8 | Identification of `S` with configurations (identity map) | representation |

### 6.5 Assumptions, named with their status

| Name | Content | Status |
|---|---|---|
| H-TS | TS itself | proposed; supplied |
| H-INT | The finite operational interface is the model of embedded access | open (trace Open list, c.6713653816) |
| H-ID | Identity identification of the operational carrier with configurations | representation choice |

A5 holds for `waveRule`. It is used only to fix scope Φ's rule, never as a motivation for TS.

***

## 7. Independent physical motivation and its classification

### 7.1 Motivation, stated without reference to the target

In classical continuum mechanics the time evolution of a closed system over a duration `t` is the composite of two
evolutions over `t/2`. The same holds for every Hamiltonian flow and for every deterministic autonomous evolution
with continuous time. A physical process that takes time can be interrupted at its midpoint, and the system then
remains a system of the same kind. Applied to an embedded observer: when the observer can carry out a reversible
process on a system, carrying out half of it is also within reach, and doing that half twice gives the whole.

In this reading the motivation is a property of time evolution. It says nothing about probabilities, amplitudes,
norms or operation sets beyond roots.

### 7.2 Classification under §3.2: independent

- It does not presuppose `T`. It is satisfied by classical flows.
- It is not designed to exclude a construction.
- It is not supported only by a consequence of `T`. Its support is classical continuum dynamics.
- Functional test: TS's statement is an inclusion of roots of reversible operations. It is not an inclusion of
  unitary conjugations, non-monomial operators or layer flows. Its domain includes phases, whose roots lie inside
  the monomial class, and permutations, whose roots may or may not. Whether TS has an effect outside the class
  that (iv) adds is an F2 question (§9). The test is applied to the statement and passes.

**Qualifications carried with the classification.**

- **Q-N, nativeness.** OI's substratum is discrete in time (A2; Main:274). The motivation's premise, continuous
  time, is not native. TS is therefore an access-level principle and is added structure (C-7). "Derived from
  native OI" requires a derivation of TS from `(S, φ)` with the native access (§12).
- **Q-O, origin.** Disclosed in §11.5. It does not change the classification, which judges the motivation, and it
  does not relax the independence requirement.
- **Q-L, literature proximity.** TS is weaker than Hardy's continuity axiom (K-4). It asserts no path, no
  transitivity on pure states and no continuity, but it is of the same family. The reviewer is asked to decide
  whether this proximity makes the motivation target-adjacent under §3.2.

### 7.3 Reclassification rule, fixed in advance

TS is reclassified **target-adjacent** if Stage 1B establishes either of the following:

- **(R1, equivalence).** On scope A, base (b), with the closure: a well-formed theory extending the base satisfies
  TS iff it satisfies (iv).
- **(R2, sole support).** The only well-formed TS-extensions are the finite operational quantum theories, and TS
  has no other consequence on the carrier.

A one-directional result (TS ⇒ (iv), or (iv) ⇒ TS) does not by itself reclassify, and it is recorded as that
direction only (§A.34).

***

## 8. Stage 0 rows targeted

- **Row 9.** Measurement interface. Its residual freedom is "which instruments, and which access or intervention
  model". TS is a proposed access model.
- **Row 13 and §5 entry "(iv) / reversible control (9, 13)".** The open alternative "fractional-time layer-flow
  access", from the trace's Open list (c.6713653816), quoted in the map's §5. TS is an
  independently motivated principle of that kind. It is not the stipulation `LayerFlowExecutable` (LiftAudit:112).
- **Reach rows (tests, §11.3), not targets.**
  - Row 7: the relating evolution, and the branch of `log`.
  - Row 5: the hidden clock.

***

## 9. Stage 1B questions and frozen criteria

### 9.1 Questions, in the fixed order

The questions follow the order motivation → consequences → comparison. F0–F3 and F5 make no reference to the
target. F4 records the comparison only.

- **F0, consistency.** For each scope and base theory, does a TS-extension exist?
- **F1, generativity.** Does the base theory itself violate TS on the scope? If it does not, TS adds nothing.
- **F2, forced content.** What do all TS-extensions contain beyond the base, at each level? Stage 1B records:
  - whether the forced content is configuration-level (monomial) and whether it preserves diagonal states;
  - how many inequivalent minimal TS-extensions exist (the freedom of choosing a root).
- **F3, classical imitation.** Is there a configuration-level realization of some TS-extension's operational
  theory on the carrier, under the identification in use? This is CI-1 to CI-3 of §10.
- **F4, comparison** (recorded only, after F0–F3). Which of (i)–(v) do the minimal TS-extensions satisfy? Is (iv)
  among them? On which carriers?
- **F5, C2 recheck.** Do R1 or R2 of §7.3 hold?

### 9.2 Outcome classes, fixed before any result

"Additional controllability" means F1 holds and F0 holds: the base violates TS, and some TS-extension exists.

| Outcome | Condition |
|---|---|
| **Positive** | F0 and F1 hold on scope Φ or scope A. F2's forced content is nonempty and not configuration-level. F3 finds no classical imitation (CI-1 to CI-3 all fail to reproduce a TS-extension). F5 does not reclassify. Every control in §10 is green |
| **Partial** | F0 and F1 hold, and one of the following: F2's forced content is nonempty but F3 is undecided; positive on one scope only; positive at some levels only; or the conclusion needs an added clause beyond TS (for example continuity), which is then classified separately under §3.2 and named |
| **(c)-type** | F0 and F1 hold, and F3 exhibits a classical imitation that reproduces a TS-extension's operational theory exactly. This class applies whatever F4 finds, including (iv) |
| **Negative** | Any one of: F1 fails (TS is satisfied within the base, so nothing is added); F0 fails (TS is inconsistent with the interface rules); or F5 reclassifies TS as target-adjacent. In the last case the outcome reads "restatement of the target in substance", a failure of safeguard G-1 |
| **Inconclusive** | Stage 1B cannot decide F0, F1 or F3. The missing lemma is named |

### 9.3 Mapping to the owner's distinctions and to the ladder

- **(a)** "An independently predicted positive result". This class is **not attainable** in this unit. TS was
  selected from a census, under a rule whose S2 clause coincides with the target's necessary condition (§4), and
  its origin is target-informed (§11.5).
- **(b)** "A positive result obtained only after selecting among multiple candidates". This is the ceiling for a
  Positive or a Partial outcome. The selection is recorded across 17 candidates within this construction. The
  portfolio record adds selection across the three constructions.
- **(c)** "Reproduces quantum statistics but admits an equivalent classical imitation". This is the (c)-type row.
  It is also recorded whenever F4 finds (iv) and F3 finds an imitation.
- **Robustness.** No Positive is promoted without R-1 to R-5 (§10) and a separate replication (R-5).
- **Ladder.** The rung is recorded by the rules of §11.4, beside (a)/(b)/(c).

***

## 10. Controls

Every computational or derivational verdict is printed only over green controls. A verdict rendered over a failed
control is void (AGENTS.md §A.29).

- **OFF, mechanism-off.** With TS removed, the base theory (b) on `Fin 2` must reproduce `substratumGen_not_control`
  (StructuralClosure:348). The access model (a) must reproduce `permTheory_not_control` (:708). TS restricted to
  phases (the part of `D_A` whose roots lie in the monomial class) must change no conclusion about permutations.
  If OFF fails, Stage 1B's modelling of the base is wrong and every verdict is void.
- **CI, classical-imitation countercontrols.**
  - **CI-1, hidden intermediate states.** A classical model realizes each half-step as a permutation of an
    enlarged configuration set that carries intermediate configurations, a hidden clock. Stage 1B must exhibit
    this model explicitly for the domain in scope, or prove that none reproduces the TS-extension's operational
    theory on `S`. The model may not assume that the intermediate data are inaccessible beyond what the
    operational theory's own definition excludes (C-5).
  - **CI-2, Theorem NC.** Stage 1B states whether the TS-extension changes the identification. If it applies NC,
    it must check each hypothesis of NC. C-3 records that the operation-set hypothesis fails for TS as stated.
  - **CI-3, classical interface.** TS is evaluated in the classical diagonal interface: `diagTheory`
    (DiagonalTheory:246), and stochastic matrices on `S`. If TS is satisfiable there, or only on an enlarged
    carrier, that is recorded. Embedding and root problems for stochastic matrices (Elfving 1937; Kingman 1962;
    Higham–Lin 2011) are cited, and any fact used from them is re-established in Stage 1B.
- **TI, target-import check.** No criterion in §9.1–§9.2 except F4 refers to (iv), unitaries, the completion
  conditions or QM. F4 is recorded after F0–F3 and changes no outcome class except through the (c)-type
  annotation. The reviewer checks this by reading §9.
- **TT, target-tuned countercontrol, which must be rejected.** TS⁺: "for every `T` in `D` and every real `t` in
  [0, 1], an available `T_t` on the same carrier, the family a continuous one-parameter group with `T_1 = T`".
  This is the layer-flow and pair-flow form. §3.2 must classify TS⁺ as target-adjacent or target-defined (C-CAL
  (c)). The variant TS-U, "the root `H` is a unitary conjugation", must classify as target-defined by the
  functional test. If either is not rejected, the classification standard is void (§3.2).
- **R, robustness.** Required before any Positive is promoted.
  - **R-1.** Both scopes and both base theories.
  - **R-2.** Ring lengths `L` in {3, 4, 5} for scope Φ.
  - **R-3.** Domain and order variants A-dom and A-ord (§11.2).
  - **R-4.** `q = 4` for scope Φ.
  - **R-5.** An independent replication of F0–F3 by a writer who did not write the original derivation.

***

## 11. Explanatory quality (AGENTS.md §A.29)

### 11.1 Preserved results (they become controls)

| Preserved result | Where | Control |
|---|---|---|
| (iv) fails for the base theories | `substratumGen_not_control`, `permTheory_not_control` | OFF |
| The five-condition characterization; OI⁺ ⇔ QM | `exactAll_iff_physical_general` (GeneralCarrier:100); `qm_of_oiPlus`, `oiPlus_of_qm` (CarrierGeneralOIPlus:191, :198) | F4 is read through it; TS is never presented as an alternative proof of QM |
| Theorem U2 and AP1's C-ROT | M2D:55, :404; AP1:772 | C-4: a claimed encoded operation outside `A_4 ≀ S_n` must name the failing U2 hypothesis |
| Theorem NC | M2D:65, :485 | CI-2 |
| M-INACC leakage (provisional) | MI §1, §8; A3 | CI-1 may not assume inaccessible hidden data; a claim that OI realizes TS natively through hidden intermediates inherits M-INACC's missing premise |
| C1–C4 as diagnostics: C2-structural persistence by reversibility, the C3 capacity bound, C4 readback | Main:82 | A TS-extension's realization, if one is claimed, must keep each diagnostic. A violation is recorded as a failure of that realization |
| Continuous interpolation is added structure | Main:274 | C-7; ledger L-5 stays supplied |
| The classical-dimension obstruction | Main:560 | A TS-extension claimed to equal a qubit's full theory cannot have a fixed finite ontic realization. If CI-1 appears to give one, CI-1 is in error or the claim is |
| Complete passive observation is commutative | `complete_passive_iff_commutative` (CentralObservation:620); Main:592 | TS adds active operations only. No passive claim is made |
| Necessary conditions for layer flows | C-2 | Cardinality check (§11.3, X-3) |

### 11.2 Variation analysis (rules only; nothing predicted)

The load-bearing assumptions are listed below. For each, Stage 1B evaluates the consequence class (§9.2) under the
stated variation.

- **Easy to vary.** The variation preserves the claimed consequence while the assumption could be adjusted without
  an independent reason, or the consequence changes with an arbitrary choice.
- **Hard to vary.** The variation destroys the consequence, and the assumption is fixed by its independent
  motivation.

| Assumption | Variation evaluated | Decision rule |
|---|---|---|
| A-car: the root acts on the same operational carrier `S` (built into "available at the same level") | Root allowed on `S` plus hidden intermediates, with the visible carrier unchanged (CI-1) | If the consequence survives the enlargement, A-car is not load-bearing. If it disappears, A-car carries the consequence. A-car is hard to vary only if §7.1's motivation (the system stays of the same kind at the midpoint) fixes `S` rather than `S` plus intermediates. Otherwise it is easy to vary |
| A-dom: domain `D_Φ` or `D_A` | `D_Φ`, `D_A`, permutations only, and all available single-outcome operations | Hard to vary if every domain that contains one configuration-moving reversible process gives the same consequence class. Easy to vary if the class depends on choosing the domain |
| A-ord: square roots | `k`-th roots for one fixed `k ≥ 3`; roots of all orders | Hard to vary if the consequence class is the same for every order. Easy to vary if it holds for some orders and not others with no reason from §7.1 |
| A-root: existence, not choice, of a root | Fix one root per `T` by a stated rule, against the existential form | Easy to vary if the consequence depends on which root is chosen (row 7 freedom) |
| A-intf: the complex-matrix interface (L-7) | The classical stochastic interface (CI-3) | If TS is satisfiable in the complex interface only because the interface admits non-monomial channels, the consequence is carried by L-7 (imported), and the outcome is recorded as representation-carried, not as a property of TS |
| A-base: base theory (a) or (b) | Both | Hard to vary if the class is the same for both. Otherwise the dependence is recorded |
| A-rule: the wave rule | Any other fixed bijection at `q = 2`, for example `G_SM` (M2D §1) in scope Φ | If the consequence does not depend on the rule, record "rule-independent" (as for `obsTheory`). The mechanism then does not use the rule, and the explanation cannot rest on the substratum's dynamics |

**Verdict rule.** If every load-bearing assumption is easy to vary, the outcome is "poor explanation", whatever F4
records. If any assumption carries the consequence and is fixed by an independent motivation, that assumption is
named as the hard-to-vary core.

### 11.3 Reach (tests the construction can fail)

- **X-1, row 7 (relating evolution).** Does TS, with the closure, fix the root, up to the equivalence the
  interface cannot detect? Or does it leave a free choice of branch? It fails reach if the freedom of row 7 is
  untouched.
- **X-2, row 5 (hidden clock).** Does TS distinguish subdivision on `S` from subdivision through a hidden
  intermediate (clock) configuration (CI-1)? It fails reach if the two give the same operational theory on `S`.
- **X-3, cardinality and the completion conditions.** Stage 1B records:
  - the cardinality of the operations TS adds over the base;
  - whether the TS-extension satisfies (iii) and (v) with the roots included (closure under spectators and
    iterated ancillas).

  It fails reach if adding roots breaks a condition that the base satisfies.
- **No independently checkable empirical consequence is preregistered.** None was identified in advance. L3
  (§11.4) is therefore unattainable in this unit. A consequence found during Stage 1B is recorded as post hoc and
  may be preregistered by a successor unit.

### 11.4 Assessment ladder

Each outcome is recorded at one rung, beside (a)/(b)/(c).

| Rung | Rule |
|---|---|
| L0 | The construction reproduces the target: F4 finds (iv), or the full five conditions, for a TS-extension. Recorded as reached, not as explained |
| L1 | L0 is reached only through assumptions classified easy to vary in §11.2, or arbitrary: a chosen root, a chosen domain or a chosen order |
| L2 | An independently motivated core (§11.2 verdict rule) fixes several features (at least F2's forced content and one of X-1 to X-3), and F3 excludes the classical imitation |
| L3 | L2 plus a novel, independently checkable consequence. Not attainable here (§11.3) |

A Negative, a (c)-type or an Inconclusive outcome is recorded at the rung its partial results reach. For example,
a (c)-type outcome that reaches (iv) is L0 with (c).

### 11.5 Origin disclosure

The conjecture came from three target-informed sources.

1. Main:590 and ESA:299 name the open question as one of finding "a physical principle for fractional-time access
   to the substratum's own layers". The principle was therefore sought in a direction the target already
   indicates.
2. This writer knew in advance of two facts:
   - a transposition has no square root among stochastic matrices (the embedding and root problem, Kingman 1962;
     Higham–Lin 2011);
   - the transposition has a unitary square root, a standard two-level quantum operation.

   This knowledge suggested that subdivision is a point where classical and quantum operation sets may part. It
   was the reason TS was formulated at all.
3. Hardy's continuity axiom (K-4) is the known separator in reconstruction programmes. TS was written as a weaker
   relative of it.

The motivation of §7.1 is stated separately and must stand on its own. This disclosure does not relax the
requirement that it be independent. The reviewer is asked to judge whether §7.1 would have been offered without
the knowledge in items 1–3. If not, the classification should become mixed, and §5's null applies.

***

## 12. Commitment to report, and the three statuses

Stage 1B, if authorized, reports its outcome whatever it is: Positive, Partial, (c)-type, Negative or
Inconclusive. Each report includes:

- the rung (§11.4) and the (a)/(b)/(c) annotation;
- the variation verdicts (§11.2) and the reach results (§11.3);
- every control (§10), green or red.

A null at selection (§5) is reported the same way.

**Statuses, recorded separately for TS.**

| Status | Requirement | Present value |
|---|---|---|
| Proposed | §7.2 classification confirmed independent by the Stage 1A review, and C-CAL passes | pending review |
| Mathematically sufficient | Stage 1B proves the F0–F2 consequences under the named hypotheses H-TS, H-INT and H-ID, with every control green | not evaluated |
| Derived from native OI | TS itself is derived from `(S, φ)` with native access, not supplied. Q-N and Main:274 record the tension | not evaluated; ledger L-5 is supplied |

***

## 13. Invariant → checkpoint table (§A.41)

| Invariant asserted | Checkpoint that measures it |
|---|---|
| Stage 1A adds exactly one file and no derivation | CK-1: the commit's diff lists only this file (`git show --stat`) |
| Pins resolve | CK-2: `git cat-file -e` on `9c201475`; every cited Lean identifier found by `grep` at the pin (run by the writer before commit) |
| No `readWriteSourced_*` identifier is cited as support | CK-3: `grep readWriteSourced` on this file returns only C-8's statement that it is not used |
| No odd-`q` statement | CK-4: `q` values in this file are 2, or 4 for R-4 |
| The selection rule precedes the census verdicts, and every rejection cites a clause | CK-5: review reads §3.1 before §4 and checks each row's Disposition against S1–S6 |
| The motivation does not mention the target | CK-6: review greps §7.1 for unitary, Born, completely positive, quantum, gate, (iv) and completion. Expected: no hit |
| The criteria do not import the target | CK-7 = TI (§10), at Stage 1A review and again before any Stage 1B verdict |
| The classification standard is calibrated | CK-8 = C-CAL, at Stage 1B before any outcome |
| Mechanism-off reproduces the known negatives | CK-9 = OFF, at Stage 1B before any outcome |
| The target-tuned variants are rejected | CK-10 = TT, at Stage 1B before any outcome |
| No Positive is promoted without robustness and replication | CK-11 = R-1 to R-5, before promotion |
| Neutral register | CK-12: review scans this file for the §A.32/§A.33 phrase families |

***

## 14. §A.42 item 8: references off main

| Reference | Claim it is attached to | Class |
|---|---|---|
| #1169 c.6720450946, c.6720342295, c.6719386464 | Authority; question; safeguards; criteria (quoted) | Provenance. The quoted owner words are reproduced here |
| #1169 c.6719708521, c.6719720616, c.6719723538 (Stage 0 map, review, confirmation) | Rows targeted (§8) | Provenance. The rows' content is restated here with its main-pinned sources |
| #1169 c.6713653816 (the (i)–(v) trace) | Carrier scopes of the (iv) failure; the Open-list alternative | Support on main: `permTheory_not_control`, `substratumGen_not_control` and `substratumTheory_not_avail_gateFlow_half` exist at the pin. The Open list is used as provenance for the row only |
| #1198, MI at `4ac0a7e6` / `f649b347` | C-5; the preserved-result row | **Support off main: a gap.** Used only as a constraint that restricts what CI-1 may assume. No claim of this file rests on it |
| PR #1202, `25384b13`, Q3-C2 | Classification standard (§3.2) | Provenance. The standard is restated in full in §3.2, which is what this file uses |
| #1188 | C-8 (not citing `readWriteSourced_*`) | Provenance (Issue) |
| #866 | Context of the accountable area (c.6720450946) | Provenance (Issue). CTL is on main |
| Literature (References) | Census motivations; CI-3 | External sources. Any fact used in Stage 1B is re-established there |

***

## 15. What this file does not do

- It derives, computes or simulates nothing.
- It adopts no premise. TS is proposed for testing only.
- It changes no manuscript.
- It does not activate Q-B or authorize Stage 1B.
- It does not claim that TS supplies (iv), any completion condition or quantum behaviour.
- It does not claim that TS fails to supply them.
- It does not read or depend on the P-MIX or P-OBS designs.

***

## References

- Aaronson, S. (2004). Is quantum mechanics an island in theoryspace? arXiv:quant-ph/0401062.
- Araki, H., Yanase, M. M. (1960). Measurement of quantum mechanical operators. *Phys. Rev.* 120, 622.
- Bennett, C. H. (1982). The thermodynamics of computation — a review. *Int. J. Theor. Phys.* 21, 905.
- Deutsch, D. (2013). Constructor theory. *Synthese* 190, 4331.
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
- Pearl, J. (2009). *Causality*, 2nd ed. Cambridge University Press.
- Shalizi, C. R., Crutchfield, J. P. (2001). Computational mechanics: pattern and prediction, structure and
  simplicity. *J. Stat. Phys.* 104, 817.
- Spekkens, R. W. (2007). Evidence for the epistemic view of quantum states: a toy theory. *Phys. Rev. A* 75,
  032110.
- Spreeuw, R. J. C. (1998). A classical analogy of entanglement. *Found. Phys.* 28, 361.
- Woodward, J. (2003). *Making Things Happen*. Oxford University Press.

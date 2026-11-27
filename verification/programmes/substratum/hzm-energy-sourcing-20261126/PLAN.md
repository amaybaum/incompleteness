# HZM-ENERGY-SOURCING, unit C (lane 3): do existing premises supply H-ZM and the SM:811 energy? Plan

**WIP / UNVERIFIED. Model-written research record, paper-only. Committed before any search result
or derivation. Nothing here is adopted, proposed for the manuscripts or authorized beyond the unit
scope. No premise is adopted, weakened or changed. Adopting H-ZM, or choosing an energy, would be a
premise change (§A.29, §A.50 item 6); this unit only searches and derives.**

- **Accountable Issues:** #1217 (COMPLEX-CARRIER-1, tier foundational) and #1049 (linear vs affine
  microscopic dynamics, tier foundational); programme #1169.
- **Authorization:** owner decision quoted in #1169 comment 7189139613 (comment author amaybaum,
  created 2026-11-26T10:16:17Z; the comment records the decision as "received
  2026-11-26T10:16Z, coordinating session"). Quoted from the owner's text:
  - "| 3 | Physical sourcing of H-ZM and SM:811 energy (#1217, #1049) | Determine whether existing
    premises already supply these conditions. |"
  - "Lane 3: Either derive the required conditions from existing premises or establish exactly
    what remains unsourced. Failure to find a source must not be presented as proof that none can
    exist."
  - "Use separate writers and independent reviewers, with distinct research artifacts for lanes 1
    and 3 to avoid conflicting work."
  - "Do not authorize computation or adopt additional premises through the new research units."
  - "The previous results should be described as reviewed paper derivations, not independently
    verified theorems."

  The writer assignment comes from the same comment's coordinator text, which follows the quoted
  decision and is not owner wording: "Unit C (lane 3, sourcing of H-ZM and the SM:811 energy,
  #1217 and #1049): `writer-hzm-energy`; branch `research/hzm-energy-sourcing-20261126`."
- **Goal link (§A.47):**
  - **#1217.** Decides whether H-ZM is supplied by a premise stated on `main`, for the constant
    and the staggered static mode separately. Lane 2's exclusion of the null sector on the torus
    consumes H-ZM (Proposition 5 of its REPORT-r2). For each mode the verdict is one of: sourced,
    partially sourced with the gap named, contradicted by a stated premise, or unsourced within
    the searched scope.
  - **#1049.** Decides whether SM:811 and SM:292–296 define or require a particular conserved
    energy: the total invariant Q′, the non-uniform energy E_⊥, E_⊥ + f(Q′_0), or another. This
    settles whether lane 1's class-(c) placement of D5 rests on a reading the manuscript states
    or on an unstated choice.
  - **Not decided.** The link names what the unit decides, not the outcome expected. A1
    retirement remains the highest operational priority. This unit runs as one of the three
    lanes the owner authorized in the decision quoted above.
- **Pinned main commit [P]:** `353a066f18766837fed8c7f58507e09ff549b1a4`. Every file:line below is
  at [P].
  - Lanes 1 and 2 pinned `b6c6b80bbd4a878452e54759cc85f16c9ffb72da`. Between the two pins,
    `papers/SM.md` differs only at lines 1394 and 1472. So the SM lines cited here and by the
    lanes (SM:130, 224–240, 286–344, 360–374, 493, 505, 809, 811) carry the same text at both
    pins.
- **Writer:** `writer-hzm-energy`. The writer makes no commit, push or GitHub write. The
  coordinator commits the writer's texts verbatim on `research/hzm-energy-sourcing-20261126`.
- **Dependency on unit A** (`writer-t5-ledger`, Theorem 5 premise ledger). Unit C does not decide
  which premises Theorem 5 consumes, nor whether it needs kinetic or full dynamical symmetry
  (Q4b). Nor does it decide whether Theorem 5's argument needs the null-sector exclusion at all.
  If unit A's ledger lands on `main` during this unit, its rows may be read as candidate
  pointers. No verdict here depends on them, and neither unit edits the other's artifacts.

## 1. Inputs (all on `main` at [P])

| Label | Source at [P] | Content used |
| --- | --- | --- |
| L2-P | `verification/programmes/oi-qm/reconstruction/complex-carrier-20261126/REPORT-r2.md`, Propositions 3–6, §5 table, §8 O1 | Definition of H-ZM; the static subspace L_0; the constraint w = 0 vs the E-null quotient; the d = 1, 2 energy-completion remark; the keyword search "zero mode, shift symmetry, uniform shift" over papers/ |
| L2-S | same directory, `PRESERVATION.md`, `PLAN.md` | Scope and status of lane 2 |
| L1-R | `verification/programmes/substratum/a5-linear-affine-20261104/qbeta-trace-20261126/REPORT-r2.md`, §2.4, §3 rows D4 and D5, §8 | Q′, E_⊥, E_⊥ + f(Q′_0); D5's placement; D4's link-difference readout |
| SM-232 | SM:232 | α = 1/d is observer level; the map from φ to L_obs is unproved (the SM:232 bridge) |
| SM-240 | SM:240; Main §4.5 ledger item (vii) | Linearity A5, a further restriction beyond the affine condition |
| SM-292 | SM:292 | "a specified real positive-definite quadratic shell; it requires an energy, a limiting regime and treatment of zero modes"; on the real lift E is positive semidefinite at α = 1/d, with constant and (even L) staggered null modes; noncompact shells "unless additional constraints are imposed" |
| SM-294 | SM:294 | Further invariants beyond total energy; ways out (i) and (ii) |
| SM-296 | SM:296 | F(u, v) = (v, Av − u); conserved E, Q_B, P_C |
| SM-811 | SM:811 | "the uniform measure *on the energy shell* of a real-valued conserved energy"; the gauge map on link differences |
| SYN | #1169 comment 7189143747 | Successor 3 of the synthesis: question, flag and productivity test. Provenance only (§A.42 item 8 classification: provenance); nothing below rests on it. |

Lane 1 and lane 2 records are model-written research records with reviewed paper derivations.
They define the targets here. No verdict uses them as established premises (§A.46 item 7).
Every statement of theirs that a verdict relies on is re-derived in REPORT.md or cited as
unverified.

## 2. Targets

**Setting inputs, inherited and not counted as gaps.** These belong to the setting in which the
targets are stated, and no target verdict counts them as missing:
- LIN, the lift is linear, by A5 or by POSIT-MIN D1(b);
- LIFT, the real lift exists as the observer-level description;
- the SM:232 bridge;
- A symmetric and translation-invariant;
- the normalization α = 1/d (κ = 2).

Every such input is carried into each conclusion that uses it. Any other open hypothesis that a
derivation needs counts as a gap.

- **(T1) H-ZM, constant static mode.** On the real lift on carrier T = (Z/L)^d, at α = 1/d, does
  any stated premise make the static constant shift (u, v) ↦ (u + c𝟙⊗e, v + c𝟙⊗e) unobservable,
  for every real c and every component direction e?
  - **(T1a) Invariance:** every quantity the observer of SM §4.1 registers, including the measure
    SM:292 and SM:811 propose, is invariant under the shift.
  - **(T1b) Quotient:** the observer-level state space, or its topology, is the quotient by the
    constant part of L_0 (the energy-seminorm reading).
  - Lane 2's Proposition 5 consumes the quotient. REPORT.md states whether T1a and T1b coincide
    for the observer as the corpus defines it, and the verdict for T1 is the verdict for what
    Proposition 5 consumes.
  - The constraint w = 0 is not part of T1. It is the positive control C+1.
- **(T2) H-ZM, staggered (period-two) static mode.** The same questions (T2a, T2b) for the static
  shift by (1, −1)(−1)^{abs(n)}⊗e on T with L even. Its level 0 alone is F-invariant, since the
  shift anticommutes with F.
- **(T1Z, T2Z), secondary.** On carrier Z = l²(Z^d) the corresponding question is whether a
  stated premise fixes the topology: lane 2's H-top, the one-particle space K, or the energy
  completion. These are recorded under the same rule but are not required by the stopping rule
  (§8).
- **(T3) The SM:811 energy.** Which conserved energy do SM:811 and SM:292–296 define or require?
  - **(T3a)** Do they define it, by formula or by reference?
  - **(T3b)** Which properties do they require? Candidates named in advance: real-valued,
    conserved by the real lift, quadratic, positive-definite, with compact shells after the
    constraints, with zero-mode treatment.
  - **(T3c)** In the linear case (b = 0), is the energy SM-296's E? Then T3 inherits T1 and T2
    through SM:292's semidefiniteness at α = 1/d.
  - **(T3d)** In the affine case at resonance (lane 1 D5): which of Q′, E_⊥, E_⊥ + f(Q′_0)
    (f bounded below), or another conserved function, meets the requirements of T3b? Does any
    stated premise select among them, for example Main's measure selection on a finite
    representative (uniform on the orbit, maximal entropy compatible with records, the Liouville
    limit) or SM:294's ways out?

The Z/q analogue (lane 1 §2.4's σ_c at κ ≡ 2) is not a target. Where a candidate source is
substratum-level, its reach to the real lift goes through the SM:232 bridge and is stated so.

## 3. What "supplies" means

A target is **supplied** when REPORT.md writes out a derivation whose conclusion is the target
statement on the stated carrier and level, with every hypothesis carried into the conclusion.
Each premise of the derivation is one of the following:
- (a) stated on `main` at [P] (an axiom, the Definition, a ledger posit, or a named hypothesis),
  quoted verbatim with file:line and with its stated status; or
- (b) a result whose proof is on `main`, traced to that proof under §A.42 item 8 and §A.46 item 7,
  with its evidence layer stated.

None of the following supplies a target:
- **Mention or requirement:** a passage that names the condition as needed (for example SM:292's
  "treatment of zero modes").
- **Stipulation:** a passage that imposes the condition or restricts to a sector without
  derivation (for example "on a sector where the inverse exists"). It is recorded as "stated,
  not derived", and its gap is the missing justification.
- **Symmetry of the dynamics:** that a shift commutes with F does not make it unobservable, since
  a symmetry is not a redundancy (control C−3).
- **Invariance of one observable:** for example the link-difference readout of the SM §6 gauge map
  (lane 1 D4). It is necessary for T1a and not sufficient for it. REPORT.md decides whether the
  corpus makes that readout the observer's complete register; until then it is a partial source.
- **Wrong scope:** a result on another carrier, dimension (for example d = 1, 2 only), level or
  parameter range. It is recorded at its own scope.
- **Unverified record:** a model-written research record not meeting §A.46 item 1. It may point
  to a source but is not one.

## 4. Search protocol

The search is exhaustive relative to the scope, reading set, term list and citation closure fixed
here. It may be widened during the work, with each widening recorded in REPORT.md, and is never
narrowed. Text search at [P] is source reading; no other code is run.

### 4.1 Corpus scope

- (A) `papers/`: every text file at [P] (all `.md`, including subdirectory READMEs). The generated
  `.tex` and `.pdf` files are excluded as derived artifacts.
- (B) `book/`: every `.md`, including `book/The-Incompleteness-of-Observation-FULL.md`.
- (C) the Lean modules under `verification/lean/` and `verification/lean-mathlib/`, and the census
  registry `verification/lean-manuscript-census.json`.
- (D) every other text file under `verification/`: records, JSON, scripts and outputs.

### 4.2 Stages

- **S1, premise-by-premise reading.** Every premise is read in full and gets one row in
  REPORT.md. The row asks one fixed question: does this premise, alone or with other stated
  premises, entail T1a, T1b, T2a, T2b, a selection for T3, or the negation of any of them? Each
  row records:
  - the verbatim premise, with file:line;
  - its stated status;
  - a verdict: entails; entails under a named extra condition; contradicts; does not entail (with
    the reason, or a countermodel where one is cheap on paper); or irrelevant (with the reason).

  The reading set:
  - Main §1.2 (the two axioms, the Definition, Lemmas 1–3, the status Remark including the measure
    selection), §1.3 ((C1)–(C4)), §3.3 (coupling graph and readout regions), §3.4 (the Remark
    *scope of the equivalence*, item (v)) and every item of the §4.5 posit ledger.
  - SM: SM:222–240 (substratum setup, form lemma, SM:232 scope, A5), SM §3.1 (state-dependent
    graph, uniform initial conditions), SM:286–308 (§4.2 measure remarks, Theorem 3), SM:312–344
    (K-component update, Proposition 4b, Theorem 5 setting), SM:360–374 (H-link, Theorem 7), the
    SM §6 opening through SM:811, and every named-hypothesis list and status table in SM.
  - `papers/Substratum.md`: every stated posit or assumption, and every passage that defines the
    update, the alphabet, gauge or redundancy, or the observer's readout.
  - `papers/Structure.md`, `papers/GR.md`, `papers/Introduction.md` and `papers/Methodology.md`:
    every passage that defines the observer's readout, the trace-out, coarse-graining, relational
    or difference observables, or measure selection.
- **S2, observer-interface reading.** H-ZM is an unobservability claim, so the primary candidate
  class is the corpus's definition of what an observer registers. Every definition of a readout
  map, partition, trace-out or coarse-graining in (A) and (C) is listed and read against T1a/T2a.
  A definition that fixes the complete register decides T1a/T2a for its scope.
- **S3, citation closure.** Backward: everything that SM:292, 294, 296 and 811, SM §4.1 and the
  SM §6 gauge map cite, by section, label, theorem or bracket reference. Forward: every passage in
  (A)–(D) that cites them. The closure is iterated until no new passage is added, and the sites
  are listed.
- **S4, mechanical term sweep.** The sweep runs `git grep -n -i -I -E` at [P] over (A)–(D), with
  the term list of §4.3 in both raw-Unicode and LaTeX spellings. REPORT.md records the exact
  command per term and the hit count per term per scope, so that the sweep is reproducible.
  - Group N hits: every hit line is read in every scope. In (A)–(C), and in `.md` records of (D),
    the surrounding paragraph is read too. In `.py`, `.json`, `.out`, `.log` and `.txt` files the
    line alone is read, escalating to context when the line states a premise or result about the
    target objects.
  - Group B hits: every hit is read in (A), in the appendices of (B) and in (C). In (D) only those
    in the S3 closure set and in the records named in S6.
  - The unswept remainder of Group B in (D) is named in REPORT.md as unswept.
- **S5, mirrors and Lean.**
  - Mirrors: for every candidate found in (A), the book mirror is checked for divergence (§A.14).
    A candidate found only in (B) is traced to a proof before it is counted.
  - Lean: every module in (C) is listed. Docstrings and statements are read for every module whose
    census family, name or docstring concerns the wave or linear update, energy, shifts, gauge or
    redundancy, or observer readout, together with every S4 hit.
- **S6, records in full.** These are read in full:
  - the lane 1 and lane 2 directories;
  - their parent records cited at [P] by L1-R and L2-P (A5-LA, POSIT-MIN, Q3/Q4, BRIDGE-UNIT1 if
    on `main`);
  - every `verification/` record whose title or scope names zero modes, null modes, shift
    symmetry, the energy shell, the SM:811 measure or the stationary law.

### 4.3 Term list (fixed)

- **Group N (narrow):**
  - zero mode, zero-mode, null mode, null direction, null sector, null space;
  - constant mode, uniform mode, uniform sector, uniform shift, constant shift, static shift;
  - shift symmetry, shift invariance, field translation, global shift, Goldstone;
  - staggered mode, alternating mode, period-two, period two;
  - pi mode, π-mode, \pi, (-1)^{, (−1)^, k = 0, k=0, zero momentum;
  - Dirichlet, energy norm, energy seminorm, seminorm, quotient, modulo constants, up to a
    constant, up to gauge;
  - link difference, first difference, difference observable, relational observable;
  - noncompact shell, positive definite, positive-definite, positive semidefinite;
  - energy shell, on-shell, microcanonical, conserved energy, real-valued;
  - E_⊥, E_\perp, Q′, Q', quadratic invariant;
  - Liouville, maximal entropy, maximum entropy, stationary law.
- **Group B (broad):** gauge, observable, unobservable, invariant, redundan, energy, Hamiltonian,
  shell, regulari, "where the inverse exists".

### 4.4 Candidate source classes (fixed)

- (K1) axiom or Definition;
- (K2) posit-ledger item;
- (K3) definition of the observer's register, readout or trace-out;
- (K4) theorem or lemma with a proof on `main`;
- (K5) named hypothesis with stated status;
- (K6) gauge or redundancy statement;
- (K7) preparation, initial-condition or boundary statement;
- (K8) normalization, regularization or sector convention;
- (K9) measure-selection statement;
- (K10) Lean theorem.

Each candidate is assigned one class and judged under §3.

## 5. Decision rule (preregistered rule, not expected results)

For each of T1 and T2, and for each sub-question:

- **Sourced:** a derivation meeting §3 exists. The verdict states its premises with their status,
  and any setting input of §2 it uses.
- **Partially sourced:** the derivation reaches a strictly weaker statement, for example:
  - T1a for a subset of observables;
  - one mode only;
  - d = 1, 2 only;
  - carrier Z only;
  - conditional on an open hypothesis beyond the setting inputs.

  The gap is named as the exact missing statement.
- **Contradicted:** a stated premise, or a proved result on `main`, entails that the shift is
  observable. The conflict is reported; this does not by itself settle the physics.
- **Unsourced within the searched scope:** no candidate passes. The verdict names the searched
  scope (§4.1, stages completed, the unswept remainder), the closest candidates and what each
  lacks. It is never reported as impossibility, and never as evidence that no premise could
  supply the condition. Failure to find a source is not proof that none can exist.

For T3:

- **Defined:** the text fixes one energy, by formula or reference. Its required properties (T3b)
  are checked on the linear and the affine resonant cases.
- **Required but underdetermined:** the text states requirements that more than one candidate
  meets. The candidate set is named, together with the extra condition that would select among
  them, and whether any stated premise supplies that condition (then it is "selected by" that
  premise).
- **Inconsistent or unspecified:** no conserved function meets the stated requirements on the
  stated case, or the text states none. The case and the failing requirement are named.

No verdict is printed over a failed control (§6).

## 6. Controls

Verdicts print only over green controls. A failed control voids the verdicts of the targets it
covers. The protocol is repaired, the repair recorded, and the affected stages rerun.

- **C+1 (positive, T1 machinery).** The protocol must find A5 (Main §4.5 item (vii), SM:240).
  From it, it must derive b = 0, conservation of the constant-mode momentum w, and hence, with
  stationarity, the constraint w = 0 (the constraint half of lane 2 Proposition 5). It must then
  classify this as supplying the constraint, conditional on A5 and stationarity, and not the
  quotient (T1b). It covers T1 and T2.
- **C+2 (positive, T3).** The protocol must find SM:296's E and its conservation for symmetric A,
  and SM:292's statement of E's definiteness on the real lift. It must classify E as the energy
  SM:292 names for the linear real lift. It covers T3.
- **C+3 (positive, sweep).** The S4 sweep must return SM:292's "treatment of zero modes" and
  SM:811's "real-valued conserved energy". It covers S4.
- **C−1 (requirement, not supply).** SM:292's "it requires an energy, a limiting regime and
  treatment of zero modes" must be rejected as a source of T1/T2 (class: mention or requirement).
- **C−2 (scope and evidence layer).** Lane 2's Proposition 6(c), that the energy completion
  performs the H-ZM quotient for d = 1, 2 on Z, must be rejected as a source of T1/T2 on T and for
  d = 3. It is a model-written record, and §A.46 item 7 bars it as an established premise.
- **C−3 (planted non-source: symmetry is not redundancy).** That the constant shift commutes with
  F (and the standard shift symmetry of a massless scalar) must be rejected as a source of T1a or
  T1b on its own.
- **C−4 (verbatim check).** Every accepted or partial source carries a verbatim quote with
  file:line at [P]. The reviewer re-extracts each quote with `git show` at [P]; a mismatch voids
  that row.
- **C−5 (conserved is not "the energy").** The Q_B and P_C families of SM:296 must not be accepted
  as SM:811's energy merely because they are conserved and quadratic. A candidate must meet the
  T3b requirements as the text states them.

## 7. Productivity test (fixed before work, §A.31)

The unit is a gem iff both of the following hold:

1. At least one target reaches a verdict strictly stronger than the lanes' prior status, which is:
   - lane 2: "not supplied", from a keyword search of papers/;
   - lane 1: "the energy reading is not stated; both branches recorded".

   A stronger verdict is one of:
   - a derivation that sources a target, or sources it partially with an exact gap;
   - a contradiction branch;
   - a selection or exact underdetermination for T3 with the selecting condition named;
   - an unsourced verdict over the full §4 protocol with green controls that names, for each
     closest candidate, the exact missing statement.
2. The verdict either constrains something, or exposes a hidden assumption (for example a
   symmetry–redundancy conflation, or an energy choice SM makes tacitly). Constraining something
   means deciding whether lane 2's Proposition 5 exclusion, or lane 1's D5 placement, rests on a
   stated premise or on an unstated choice.

Restating "not found" over a wider keyword list alone is a non-gem. Output is classified NEW,
POSITIVE, ELABORATING, CONFIRMING or BORDERLINE (§A.31). A result favorable to the framework (a
source found) gets maximum skepticism: the reviewer re-derives it independently.

## 8. Stopping rule

Stop when the first of these occurs:

- (a) Stages S1–S6 are complete for T1, T2 and T3, every control is evaluated, and each of T1, T2
  and T3 has a §5 verdict.
- (b) Three to four consecutive passes yield no NEW finding. A pass is one re-reading of the
  reading set for one target against a new candidate class.
- (c) A resource limit is reached (§A.40, §A.51). The partial state is returned with the unswept
  scope named, and every verdict is scoped to the part swept.
- (d) A control failure cannot be repaired. The unit halts, and the affected verdicts are reported
  void.

## 9. Independent review

REPORT.md is not presented as accepted until an independent non-author reviewer has reviewed its
exact pushed SHA. The reviewer is an agent other than the writers of units A, B and C. The review
is recorded on the guiding draft PR (§A.43), and the reviewer:

1. reruns the S4 commands at [P] and matches the hit counts;
2. re-extracts every quoted source (C−4);
3. checks every control and its classification;
4. re-derives every derivation step, independently for any favorable verdict;
5. checks that every negative statement carries its searched scope and none is phrased as
   impossibility;
6. checks the §A.42 item 8 tracing of every reference to content not on `main`.

Results remain reviewed paper derivations, not independently verified theorems. The outstanding
verification obligations named by the owner are preserved: exact finite controls, Lean where
applicable, independent non-model verification, and re-derivation of inherited inputs.

## 10. Exclusions

The unit makes:
- no manuscript edit;
- no adoption, weakening or change of any premise;
- no choice of energy;
- no computation experiment and no Lean build;
- no GitHub write by the writer;
- no edit to unit A's or unit B's artifacts;
- no claim about the fundamental Z/q level beyond recording how a substratum-level candidate
  reaches the lift.

## 11. Deliverables

1. This PLAN.md (first commit).
2. REPORT.md in this directory, containing:
   - the sweep log (commands and counts);
   - the S1/S2 premise rows;
   - the S3 closure list;
   - the S5 Lean and mirror findings;
   - the controls with their outcomes;
   - the verdict per target and sub-question, with its scope;
   - the productivity verdict;
   - the open nodes;
   - the evidence layer of each result (mathematical derivation on paper or source reading).

## 12. References not on `main` (§A.42 item 8)

- #1169 comment 7189139613: the authorization. Provenance, no scientific content used.
- #1169 comment 7189143747: provenance.
- #1217 and #1049: accountable Issues. Planning only.
- Lane records cited in §1: on `main` at [P].

# GATE-A r5: the inclusion target QM ⊆ OI + E, consolidated (proposal)

**WIP / UNVERIFIED. Proposal only; not adopted.** This paper-only record proposes a restatement of
the model-level target. The restatement takes effect only if the owner adopts its exact statement
(§2) by an explicit decision. Until then the governing typed contract on `main` stays
`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md` (blob `d9d92e03`), which
this record does not edit, replace or reinterpret. It proves no clause of the target, adopts no
extension E, no sector condition C and no physical premise, and changes no scientific status.
Physical source remains NOT PASSED. No independent review has been made yet.

Tracking: Issue #1502 (linked to #1169); draft PR #PR.

## 1. Pins, sources and authority

- **Base.** `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed`. `EP:n` is line n of
  `oi-qm-ext-1/endpoints.md` (blob `d9d92e038a8022e854586101067ce4de9789fdf6`); `Main:n`, `Sub:n`
  are lines of `papers/Main.md`, `papers/Substratum.md` at that base.
- **r4.** `GATE-A-AMEND-r4.md` on `research/gate-a-amendment-1169-20261114` at
  `3a1c8e978cc6c4ea35322d6a7d801dd8d05a529b` (PR #1289, closed unmerged; carried by Issue #1428).
  `r4:n` is its line n. Its closing confirmation `CONFIRM-r4.md` is a model review (ACCEPT); it is
  not an owner adoption. Off-`main` content is provenance here (§A.42 item 8): every r4 clause used
  below is restated in full in this record.
- **Owner records read (all from the owner account; read in full, #1169 and #914 paginated).**

| Record | Date | What it fixes for the target |
|---|---|---|
| #914 c.6875046763 | 2026-11-14 | Five decisions: extension form; exact as ultimate target; Bell a mandatory separate track; complex matrices only as conditional input; Lean for final claims. "the target cannot assume one fixed finite total carrier"; "Finite access by an embedded observer must remain distinct from finiteness of the underlying dynamics." |
| #914 c.6875548603 | 2026-11-14 | Replaces the two-way sentence: **Inclusion** "QM_fin ⟹ OI + E on one common substratum–observer realization. Required."; **Sector** for a physically justified C, with two directions; **Gravity**. "Not required. That every OI model behaves quantum-mechanically." |
| #1169 c.6876591512 | 2026-11-14 | Answers to the four r4 questions: (1) C applies to the underlying model, with its consequences for experiment families defined explicitly; (2) coverage and soundness required, necessity optional; (3) "One fixed model, with one common extension E, must support subsystems realizing every quantum carrier in the agreed scope ... arbitrarily large finite carriers, with the permitted encodings and resource requirements stated explicitly"; one common architecture an intermediate milestone; (4) quantum behaviour for every physically performable experiment within C (access closure kept). "adoption of the amended target requires an explicit owner decision." |
| #914 c.6877420015 (pointer #1169 c.6877420524) | 2026-11-14 | Part 4 (unified downstream derivation) and joint satisfiability as a mandatory condition; Gate A "should remain the quantum-sector proof gate"; r4 unadopted "until reconciled with the strengthened target"; satisfying Gate A "is necessary for the unified endpoint but insufficient for Part 4". |
| #1169 c.6877981234, c.6878199016, c.6880022363 | 2026-11-14 | S-J (confinement) and EXACT accountable on #1169, tier Foundational; S-A row added. |
| #1169 c.6891338304 | 2026-11-15 | C/Q distinction, "target amended": Q is the quantum zone (descriptive); C is defined by the limits of embedded observation, with no reference to quantum outcomes. Coverage required; agreement with performed experiments required; "This amends the soundness requirement in the Gate A answers (c.6876591512). Soundness is now an open question"; "Excluding PR is no longer a goal." |
| #1169 c.7057297534, c.7058446475 | 2026-11-21 | A1 retired by design (execution pending in #1477): "No restriction is imposed on its cardinality; $\mathcal S$ may be finite or infinite."; "Finiteness stays explicit wherever an individual theorem requires it"; the definition "does not imply that results established only for finite systems apply to arbitrary configuration spaces". |
| #1169 c.7064843184, c.7064859041 | 2026-11-21 | (N)/(I) labelling of every finding; the three questions; the scalability safeguard; U1 authorized as preparation and independent review; the 14 November decisions are authoritative inputs; r5 not adopted until the owner reviews its exact statement. |

**A1 is not retired on `main`.** At the base, `Sub:92` reads "(A1) **Finiteness.** The configuration
space $S$ is finite." The retirement is pending in #1477 and is not treated as landed anywhere below.
This record touches no file, line or record directory of #1477 or #1483.

## 2. The proposed r5 statement

> **I★ (quantum inclusion, single-model form).** There is one model
> M* = (Ω, Φ, Λ, μ, ι, R, τ, E) in the sense of the EP:73 schema, with one extension E, one
> label rule 𝓛 and one resource policy, and there is an encoding rule A ↦ β_A, a fixed bijection
> β_A : A ≃ Fin |A| for every nonempty finite type A, computed from the type alone, such that for
> every nonempty finite A:
>
> - **(scale)** the A-subsystem of M*, read through β_A and the fixed join reindexing, carries
>   every object B_n = A × Fin n (n > 0) of `J_exact(A)` as a level of M*'s interface on the
>   singleton carrier, so that M*|_A is the restriction of one interface, not a model per size;
> - **(I-1, coherence)** one label interpretation 𝓛_A, transported from 𝓛 along β_A, covers every
>   preparation p, protocol π and history h of `J_exact(A)` and preserves sequential and
>   outcome-dependent composition, conditioning, helper attachment, spectators and discard;
> - **(I-4, exactness)** p_{M*|_A}(h | π, p) = p_{T_A}(h | π, p) for every p, π, h of
>   `J_exact(A)`, where T_A is the trace law of EP:110 on `J_exact(A)`;
> - **(I-2★, one construction)** Φ, Λ, μ, ι, R, τ, 𝓛 and the resource policy do not depend on A;
>   A enters only through β_A; nothing is computed from the values of p_{T_A}; the resource
>   policy states, as one rule, the records, controller, ancilla supply and any completion for
>   arbitrarily large finite carriers (EP:106);
> - **(I-3, physical sourcing)** E and each clause of the model carry a source status; a proof
>   that uses an unsourced or posited clause establishes the conditional inclusion I★[H] with H
>   named, and does not discharge I★.
>
> **Cardinality.** I★ imposes no cardinality on Ω. Lemma L-H (§4) shows that any model meeting
> I★ has infinitely many response classes on a qubit level; that is a consequence of exactness,
> stated as a necessary condition, not an assumption of the target. Finiteness of the carrier A,
> of each finite adaptive history and of each finite resource used is a local hypothesis of the
> clause that uses it.
>
> **Milestone forms (not the target).** I-arch: one architecture with a model M_A per carrier A,
> each meeting I-1, I-3, I-4 on `J_exact(A)` (r4 §5.1, the intermediate milestone of answer 3).
> I-ε: the approximation target of EP:121 (Main:574–610). Neither discharges I★.
>
> **Scope.** `J_exact(A)` only (endomorphic operations, helper attachment and discard, finite
> adaptive histories). Changes of system type and multi-wing protocols are the untyped remainder
> of part 1 (r4 §5.1 Scope), open.

How r5 expresses the scalability safeguard: through (scale) and I-2★. `J_exact(A)` already
contains every level B_n = A × Fin n with no upper bound (EP:33, EP:41), so a single model for one
carrier must already realize arbitrarily large finite carriers with one dynamics and fixed joins;
Lemma L-T (§5) shows that I★ is the I-arch obligation at the singleton carrier together with the
transported label rule. A separate model per size fails I-2★ by definition, and fails I-1 already
at a single carrier, because the levels of `J_exact(A)` are joined by helper attachment inside one
model.

### 2.1 The other parts, carried from r4 with the owner answers folded in

| Clause | r5 form | Required? | Source |
|---|---|---|---|
| C, type | C-model: a physically stated condition on the native data of M, with its consequences for experiment families stated explicitly; defined by the limits of embedded observation, with no reference to quantum outcomes; r4's admissibility conditions C-1 to C-5 kept | definition | answer 1; c.6891338304 |
| S⇐ (coverage) | for every A, M*|_A satisfies C and meets I★'s clauses; S⇐ implies I★ | required | answer 2; c.6891338304 |
| S-D (agreement with data) | every prediction of M* inside C for an experiment already performed matches the raw-direct data (§A.24) | required | c.6891338304 |
| S⇒ (soundness) | as r4 §5.2 | **conflict, owner decision D2**: required by answer 2; "an open question" reported as a finding by c.6891338304 | |
| S-A (access closure) | as r4 §5.2 | **conflict, owner decision D2**: required by answer 4; c.6891338304 says "Excluding PR is no longer a goal" | |
| S⇐ᴺ (necessity) | as r4 §5.2 | optional future theorem | answer 2 |
| S-J (confinement) | as r4 §5.2 | required; tier Foundational | c.6878199016 |
| B (Bell) | B⇐ required; B⇒ subject to D2 | mandatory separate track | decision 3 of c.6875046763; c.6891338304 (BELL-QSET text left pending) |
| G (gravity) | r4 §5.3 G-1 to G-3, on the same M* | required | c.6875548603 |
| Part 4, joint satisfiability | outside Gate A: Gate A is necessary for the unified endpoint and insufficient for Part 4 | required, not a Gate A clause | c.6877420015 |

## 3. Clause ledger with directional witnesses (§A.34)

For a clause of a target, the two directions are kept apart: **sufficient** = what would discharge
the clause, and the existing results that discharge it at a narrower scope; **necessary** = what
every witness of the clause must satisfy, with the result that forces it. (N) = proved from OI's
native assumptions; (I) = conditional, imported assumptions named. Layers: K Lean kernel on
`main`; X exact algebra; P paper; R research record.

| Clause | Kind | Status | Sufficient direction | Necessary direction | Dependencies |
|---|---|---|---|---|---|
| I★ as a whole | mathematical statement; physical content through I-3 | open | none exists. Conditional route: `substratum_plus_control_qm` (StructuralClosure.lean:397, K) gives exact finite endomorphic QM on every nonempty finite carrier for the generated theory, assuming `ExtendsSubstratum`, `StructurallyClosed`, `DrivesElementary`; that is an interface-level theory, not a model of the EP:73 schema, so it is a sufficient condition for a different object. (I): imports complex matrix kinematics (decision 4) and elementary drivability | L-H (§4): infinitely many response classes on a qubit level; Main:568 (P, unboundedness imported [55]); L-T (§5): I★ ⟺ I-arch at the singleton with transported labels | E; A1 retirement (§6); H-∞ (`verification/ROADMAP.md`:81) for any completion route |
| (scale) | mathematical (interface typing) | proposed definition | satisfied by construction of `J_exact(A)` (EP:33, EP:41) once one model is given | L-T: any I★ witness restricts to an I-arch witness at the singleton that already carries all levels | EP:33, EP:41, EP:106 |
| I-1 coherence | mathematical | open | none | EP:67, EP:104, EP:112 (contract requirements) | label rule 𝓛 |
| I-2★ one construction | mathematical + resource accounting | open | none | a per-size family fails it by definition; L-T shows the per-size loophole is already closed by I-1 at one carrier | resource policy (EP:106); A1 retirement for an unbounded resource family inside the substratum |
| I-3 physical sourcing | physical/operational | open; NOT PASSED | none. Earliest assumed mechanism: elementary drivability (continuously tunable state mixing) in a structurally closed class (Main:598; `substratum_plus_control_qm` hypothesis `hd`); native preparation, readout and records (`verification/programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md`:21 and `verification/programmes/oi-qm/reconstruction/meas-q-20261120/RESULT.md`:33 record physical sourcing NOT PASSED) | the monomial class lacks composite control: `substratumGen_not_control` (StructuralClosure.lean:330, K; two-state carrier), `substratumTheory_not_layerFlowExecutable` (LiftAudit.lean:200, K). These are (N)-type no-gos for the specified monomial implementation class only | E; native coherent operation; native preparation, readout and records |
| I-4 exactness | mathematical | open | none for the full interface. I-ε is proved at bounded menu and horizon (Main:574–610, P) with supplied quantum data: it does not discharge I-4 | L-H (§4, P, this record, unreviewed); Main:568 (P + import [55]); the all-time periodicity obstruction of a fixed finite bijection with a fixed prior (Main:650, P) at its own autonomous multi-time scope | A1 retirement (§6); setting and preparation isolation EP:79, EP:81–90 |
| ⇐ of `qm_generated_by_substratum_extension` (StructuralClosure.lean:406) | assumption-watch marker | K | — | its witness is `fullClass`, for which `ExtendsSubstratum` holds by `trivial` (`fullClass_extendsSubstratum`); this direction carries no substratum content and is not evidence for I-3 | — |

## 4. Lemma L-H: a necessary condition for exactness (paper; depth-first, §A.31)

**Productivity test, fixed before the attempt.** The investigation is a gem iff it yields a
necessary condition on every witness of I★ (or of I-arch at one carrier) that is strictly
stronger than the restatement "Ω is infinite" of Main:568, and it either constrains the
architecture or exposes a hidden assumption. A restatement of Main:568 is a non-gem, recorded only.

**Setting.** A model M meeting I-1 and I-4 at a carrier containing a qubit level (any A with
|A| ≥ 2, or any level B_n with |A|·n ≥ 2; by L-T, every I★ witness has one). Fix two orthonormal
basis vectors a₁, a₂ of that level and countably many pairwise non-parallel unit vectors ψ_k in
their span. In `J_exact`, take the single-shot protocols π_k: prepare the pure state ψ_k (or ψ_j),
apply once the three-outcome projective instrument {P_k = |ψ_k⟩⟨ψ_k|, P_k⊥ = |ψ_k⊥⟩⟨ψ_k⊥|,
1 − P_k − P_k⊥}, record the outcome.

**Hypotheses on M (all from the contract, none quantum).**
- **H-ISO** (EP:79, literal): for a fixed preparation, the law of the uncontrolled variables U is
  unchanged by the choice of later setting until the declared interaction. So each preparation p
  induces one law ν_p on U, the same for every π_k.
- **H-PI** (a reading of EP:79 and EP:90, not stated there in these words): the response of a
  fixed instrument label is a measurable function ξ_{k,o}(u) ∈ [0, 1] of the uncontrolled variables
  and of that instrument's own controller fields; it does not read a record of the preparation
  label. EP:90 restricts an operation's dependence to "its declared inputs and retained past"; a
  single-shot protocol whose retained past held the preparation label would leave H-PI open. This
  is the hidden assumption the node N2 below exposes.
- **Exactness** (I-4): p_M(o | π_k, p) = Tr(P_o ρ_p) exactly.

**Statement.** Let κ(u) = (ξ_{k,o}(u))_{k,o} be the response vector of u over this countable
family. Under H-ISO, H-PI and I-4, κ takes infinitely many values on the union of the supports
of ν_{ψ_k}. In particular the set of response classes {u ~ u' iff κ(u) = κ(u')} reachable by
preparations of one qubit level is infinite.

**Proof.** Suppose κ takes finitely many values, so U splits into finitely many measurable
classes U_1, …, U_N on which every ξ_{k,o} is constant. For each k let S_k ⊆ {1, …, N} be the
classes of positive ν_{ψ_k}-mass. There are at most 2^N such sets and infinitely many k, so
S_j = S_k for some j ≠ k. By I-4, p_M(k⊥ | π_k, ψ_k) = |⟨ψ_k⊥|ψ_k⟩|² = 0, and by H-ISO and
H-PI this equals Σ_{i ∈ S_k} ν_{ψ_k}(U_i) ξ_{k,k⊥}|_{U_i}. Every term is nonnegative and every
weight positive, so ξ_{k,k⊥} = 0 on every class in S_k = S_j. Then
p_M(k⊥ | π_k, ψ_j) = Σ_{i ∈ S_j} ν_{ψ_j}(U_i) ξ_{k,k⊥}|_{U_i} = 0. By I-4 it equals
|⟨ψ_k⊥|ψ_j⟩|², which is nonzero because ψ_j is not parallel to ψ_k in a two-dimensional space.
Contradiction. ∎

This is the argument of Hardy's ontological-excess-baggage theorem [Har04, cited at
`papers/Introduction.md`:250], applied to response classes of the EP:73 schema rather than to
ontic states. It uses only pure preparations, one projective instrument per protocol and exact
zeros; it uses no nonnegative-rank import.

**Depth-first nodes and verdicts.**
- **N1. Is L-H strictly stronger than "Ω is infinite"?** Check: a model with infinite Ω whose
  readout couples to finitely many response classes (an infinite hidden sector the instruments
  never resolve) satisfies "Ω infinite" and violates L-H. Verdict: yes, strictly stronger; it
  constrains the observer interface (ι, R, τ and the coupling), not only the cardinality of Ω.
- **N2. Which hypotheses are load-bearing?** Check, H-ISO dropped: a finite-U model can load u as
  a sample of the quantum outcome given (p, π), reproducing every single-shot law; L-H fails.
  Check, H-PI dropped: an instrument reading a stored preparation label can output the quantum
  law with finite U; L-H fails. Check, exactness dropped: I-ε holds with finite carriers
  (Main:574–610). Verdict: all three are load-bearing; H-PI is not stated literally in EP and is
  the hidden assumption exposed (assumption-watch marker AW-R5-1: "a native instrument does not
  read a record of the preparation label"; it applies to every O3 readout construction).
- **N3. Does L-H conflict with A1 as on `main`?** Check: under Sub:92, S is finite. If U is a
  restriction of the substratum configuration and the controller-noise and ready-record variables
  are finite, κ takes finitely many values, contradicting L-H. Verdict: under A1 as written, I★
  and I-arch are unsatisfiable on any qubit level unless E supplies an infinite uncontrolled
  sector outside the substratum, which the "one common substratum–observer realization" clause and
  I-3 would then have to source. Favourable reading pressure-tested: the A1 retirement removes this
  conflict but does not establish that an infinite sector exists or is consistent (c.7058446475,
  c.7064859041); L-H gives a requirement, not a construction.
- **N4. Does L-H give more than countably many classes?** Check: the proof needs only a countable
  family and yields "infinite"; it does not bound the cardinality from below by the continuum.
  Verdict: no stronger cardinality is claimed.

**Outcome.** Gem by the preregistered test (N1 and N2). Classification: ELABORATING for the
cardinality content (Main:568 already forces an unbounded carrier) and NEW for AW-R5-1 and for
the explicit A1 dependency of the target (N3), which r4 did not record. Label **(I)**: a
conditional theorem about any witness of the target; imported operational assumptions H-ISO
(EP:79), H-PI (reading of EP:79, EP:90) and the comparator law of EP:110 at exact zeros; no
quantum assumption on the OI side. Layer P, this record, unreviewed. No Lean statement of it exists
on `main`; `classical_exposed_ncard_le` (KInfFoundations.lean:947) is a different bound (exposed
points of a body in the N-simplex under a facet hypothesis) and is not duplicated here.

## 5. Lemma L-T: the single-model form at one carrier (paper)

**Statement.** I★ holds iff there is one model M meeting I-1, I-3 and I-4 on `J_exact(Fin 1)` whose
label rule, transported along β_A and the fixed join reindexing, is the label interpretation of
`J_exact(A)` for every nonempty finite A.

- **⇒ (restriction).** An I★ witness restricted to A = Fin 1 is such a model. Witness: the
  definition of I★.
- **⇐ (transport).** Given M at Fin 1, put |A| = k. The bijection
  (A × Fin n) ≃ Fin k × Fin n ≃ Fin (k·n) sends each object of `J_exact(A)` to the level
  B_{kn} of `J_exact(Fin 1)`, and preparations, instruments, helper attachment, spectators and
  discard to the corresponding operations there (EP:33–41: every level n > 0 is present). For
  the mixed-radix reindexing (a, b) ↦ b + n·a the two routes
  (A × Fin n) × Fin m → Fin (k·n·m) agree, since c + m·(b + n·a) = (c + m·b) + (n·m)·a; for any
  other fixed reindexing they differ by a permutation of basis labels, which is itself a unitary
  instrument of `J_exact(Fin 1)` and is absorbed into the transported label. The trace law is
  invariant under conjugation by permutation unitaries, so p_{T_A}(h | π, p) =
  p_{T_{Fin 1}}(h | β(π), β(p)) for every p, π, h. I-4 at Fin 1 then gives I-4 at A for the same
  M. Witness: this exact algebra (layer X, on paper, unreviewed).

**Productivity.** Gem by the §4 test's standard: it shows that the r4 distinction between the
architecture reading and the single-model reading (r4 §7 R2, answer 3) reduces, inside
`J_exact`, to the coherence of the transported label rule, because `J_exact(A)` with unbounded
helper levels already demands one model for every finite carrier size. Label **(N)** in the narrow sense
that the transport algebra imports no quantum or operational assumption: it is a fact about the
target's definitions, not about OI, and says nothing about whether any such model exists. It does not cover the typed two-wing interface:
whether a level B_{kn} counts as two separately addressable subsystems is part of B and of the
remainder of part 1.

## 6. Dependencies stated explicitly

- **A1 retirement (#1477, pending).** I★, I-arch and I-4 are unsatisfiable on any qubit level by
  a model whose uncontrolled sector lies in a finite substratum (L-H, N3). Every clause of r5 that
  needs an infinite uncontrolled sector therefore depends on the retirement landing, or on an E
  that supplies such a sector and sources it. The approved wording, once landed, makes the
  configuration space cardinality-neutral; it does not establish existence or consistency of an
  infinite sector, and finite-only results (all Lean results cited in §3, whose carriers carry
  `[Fintype A]` or `[Fintype S]`) stay scoped to finite carriers.
- **Infinite completion.** Any route through a completed carrier depends on H-∞ (`verification/ROADMAP.md`:81,
  open); `localHom_unique` (QuasilocalCharacterization.lean:248) is a uniqueness theorem, not an
  equivalence (§A.34), and `q3_countermodel` (InstrumentAvailability.lean:335) shows the frozen
  structure does not supply infinite-support coherent operations.
- **Kinematics.** Every sufficient route cited imports complex matrix kinematics (decision 4).
- **The 15 November amendment.** S⇒, S-A and B⇒ depend on decision D2.

## 7. The three questions

1. **Established.** L-H (§4): under H-ISO, H-PI and exactness, every witness of I★ has infinitely
   many response classes on a qubit level (P, unreviewed, (I)). L-T (§5): I★ is equivalent to the
   single-carrier obligation at Fin 1 with the transported label rule (X on paper, unreviewed,
   (N) for the algebra). Nothing in I★ is discharged.
2. **Assumed.** For L-H: H-ISO (EP:79), H-PI (a reading of EP:79, EP:90) and the exact comparator
   law (EP:110). For every sufficient route cited: complex matrix kinematics; elementary drivability
   (`DrivesElementary`, hypothesis `hd` of `substratum_plus_control_qm`); structural closure
   (`StructurallyClosed`); finiteness of the carrier (`[Fintype A]`).
3. **Missing.** The earliest unsupported step of I★ is a physical mechanism: an infinite,
   observer-resolvable uncontrolled sector together with a native, physically sourced operation of
   elementary drivability acting on it (I-3), inside one model. Second, and
   mathematical: an exact single model over all finite carriers with stated encodings and
   resources (I-2★, I-4), for which L-T fixes the form and no existence result is known.

## 8. Reconciliation proposal (for owner decision; nothing edited)

- **Contract on `main`.** `endpoints.md`:51–69 (the class-wide two-direction display) stays
  unchanged. If the owner adopts r5, the landing would add r5 as an append-only forward amendment
  in this record directory, with EP:56–59 read as superseded class-wide (as r4 §4.1(a)), EP:61–64
  read as I without I-2★, I-3 and (scale), and every other EP line kept (r4 §3 residual clause).
- **Off-`main` r4.** r4 (`3a1c8e97`) remains the reviewed amendment proposal and provenance for
  §2.1 and the C-1 to C-5 conditions. Proposal: preserve r4 by reference only; r5 restates every
  clause it uses, so no r4 file needs to land on `main` for r5 to be read (§A.42 item 8).
- **#1428 GATE-A row is stale.** It reads "owner answers to `OWNER-QUESTIONS-r4.md` (four
  questions) ... | blocked: owner questions", and its open-work note says the four questions "are
  open". The four questions were answered at #1169 c.6876591512 (2026-11-14), before #1428 was
  opened (2026-11-19). #1428 is not edited here. Proposed corrected row:

| ID | Item | Tier | Prerequisites | Readiness | Authorization |
|---|---|---|---|---|---|
| GATE-A | Gate A forward amendment for the superset target, r4 and status note r6 (#1289); consolidated as r5 (this record) | supporting (provisional) | owner answers given at #1169 c.6876591512; soundness amended at c.6891338304; owner adoption of the exact r5 statement; A1 retirement (#1477) for the exactness clauses | r5 preparation and independent review | U1 authorized as preparation and review (#1169 c.7064859041); adoption not authorized |

  Proposed replacement for its open-work note: "GATE-A. The four owner questions were answered at
  #1169 c.6876591512, and soundness was amended at c.6891338304. The answers are folded into the
  r5 proposal (Issue #1502, PR #PR), which awaits owner adoption. The contract
  `oi-qm-ext-1/endpoints.md` on `main` is unchanged."

## 9. Owner decisions needed

- **D1.** Adopt, amend or reject the exact statement of I★ in §2, including (scale), I-2★ and the
  reading that Q_exact(A) is the single trace law T_A on `J_exact(A)` (r4 §7 R2).
- **D2.** Reconcile answers 2 and 4 (soundness, access closure required) with c.6891338304
  (soundness an open question; excluding PR no longer a goal): which governs S⇒, S-A and B⇒.
- **D3.** Whether H-PI is part of the contract's isolation requirements (it is load-bearing for
  every exactness obstruction and for every readout construction).
- **D4.** Whether r5 is landed as a forward amendment after independent review, and the #1428
  correction (§8).

## 10. What this record does not do

It edits no manuscript, no `endpoints.md`, no Issue body and nothing of #1477 or #1483; it runs no
computation and dispatches no workflow; it proposes no E and no C; it does not post on #1169.

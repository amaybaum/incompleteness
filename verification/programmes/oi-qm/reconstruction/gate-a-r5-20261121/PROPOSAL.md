# GATE-A r5: the inclusion target QM ⊆ OI + E, consolidated (proposal)

**WIP / UNVERIFIED. Proposal only; not adopted.** This paper-only record proposes a restatement of
the model-level target. The restatement takes effect only if the owner adopts its exact statement
(§2) by an explicit decision. Until then the governing typed contract on `main` stays
`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md` (blob `d9d92e03`), which
this record does not edit, replace or reinterpret. It proves no clause of the target, adopts no
extension E, no sector condition C and no physical premise, and changes no scientific status.
Physical source remains NOT PASSED.

**Revision r5.1.** This text answers the independent review at `95073878` (#1503
c.7065022754, verdict REVISE, blockers B1–B6 and nits). The reviewed text is that commit; the
response to each finding is listed in §11. r5.1 is not yet re-reviewed.

Tracking: Issue #1502 (linked to #1169); draft PR #1503.

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
| #914 c.6875046763 | 2026-11-14 | Five decisions: extension form; exact as ultimate target; Bell a mandatory separate track ("exclude supraquantum ones"); complex matrices only as conditional input; Lean for final claims. "the target cannot assume one fixed finite total carrier"; "Finite access by an embedded observer must remain distinct from finiteness of the underlying dynamics." |
| #914 c.6875548603 | 2026-11-14 | Replaces the two-way sentence: **Inclusion** "QM_fin ⟹ OI + E on one common substratum–observer realization. Required."; **Sector** for a physically justified C, with two directions; **Gravity**. "Not required. That every OI model behaves quantum-mechanically." |
| #1169 c.6876591512 | 2026-11-14 | Answers to the four r4 questions: (1) C applies to the underlying model, with its consequences for experiment families defined explicitly; (2) coverage and soundness required, necessity optional; (3) "One fixed model, with one common extension E, must support subsystems realizing every quantum carrier in the agreed scope ... arbitrarily large finite carriers, with the permitted encodings and resource requirements stated explicitly"; one common architecture an intermediate milestone; (4) quantum behaviour for every physically performable experiment within C (access closure kept); (5) "Prepare r4 for preservation on main through the normal gates." "adoption of the amended target requires an explicit owner decision." |
| #914 c.6877420015 (pointer #1169 c.6877420524) | 2026-11-14 | Part 4 (unified downstream derivation) and joint satisfiability as a mandatory condition; Gate A "should remain the quantum-sector proof gate"; r4 unadopted "until reconciled with the strengthened target"; satisfying Gate A "is necessary for the unified endpoint but insufficient for Part 4". |
| #1169 c.6877981234, c.6878199016, c.6880022363 | 2026-11-14 | S-J (confinement) and EXACT accountable on #1169, tier Foundational; S-A row added. |
| #1169 c.6891338304 | 2026-11-15 | C/Q distinction, "target amended": Q is the quantum zone (descriptive); C is defined by the limits of embedded observation, with no reference to quantum outcomes. Coverage required; agreement with performed experiments required; "This amends the soundness requirement in the Gate A answers (c.6876591512). Soundness is now an open question, subject to the agreement-with-data requirement"; "Excluding PR is no longer a goal"; stronger-than-quantum behaviour in unperformed experiments "would be a testable prediction, not a defect". |
| #1169 c.7057297534, c.7058446475 | 2026-11-21 | A1 retirement design (execution pending in #1477): "No restriction is imposed on its cardinality; $\mathcal S$ may be finite or infinite."; "Finiteness stays explicit wherever an individual theorem requires it"; the definition "does not imply that results established only for finite systems apply to arbitrary configuration spaces". |
| #1169 c.7064843184, c.7064859041 | 2026-11-21 | (N)/(I) labelling of every finding; the three questions; the scalability safeguard ("one coherent, scalable construction ... compatible dynamics and observation interfaces"); U1 authorized as preparation and independent review; "The 14 November decisions are authoritative inputs"; r5 not adopted until the owner reviews its exact statement. |
| #1169 c.7064942473 | 2026-11-21 | "The corpus's existing single-time observation interface is retained and is not redefined"; a broader interface with coherent interventions "would need an independent scientific justification"; "Any reliance on coherent intervention operations beyond the native interface is identified explicitly"; for QM ⊆ OI + E, "The observation interface must be defined precisely before a complete reconstruction or classification is claimed. Equivalence based on single-time observations is weaker than equivalence under arbitrary quantum experiments." |

**Status of A1 on `main`.** At the base, `Sub:92` states "(A1) **Finiteness.** The configuration
space $S$ is finite." and, in the same paragraph, "A1 is an open hypothesis, not adopted ([Main
§4.5], item (ii))"; `Main:60` reads "The two axioms and the Definition leave the cardinality of the
total configuration space open." EP:73 places "finite or infinite resources" in E. So on `main`
the target does not inherit A1. The retirement (#1477, pending) changes how the corpus presents
cardinality; the target's satisfiability does not depend on it (§6). This record touches no file,
line or record directory of #1477 or #1483.

## 2. The proposed r5 statement

> **I★ (quantum inclusion, single-model form).** There is one model
> M* = (Ω, Φ, Λ, μ, ι, R, τ, E) in the sense of the EP:73 schema, a member of
> M(E, `J_exact(A)`) at every carrier it serves (EP:102), with one extension E, and an
> **encoding rule** that assigns to every nonempty finite type A a physical encoding
> enc_A = (X_A, β_A): a declared subsystem X_A of M* (a sector of Ω with its admissible preparation,
> intervention and record procedures, EP:47, EP:75) and a fixed bijection β_A of A with the
> distinguishable alternatives X_A is used to carry (any fixed choice; the trace law is
> permutation-invariant, so the choice is immaterial), such that for every nonempty finite A:
>
> - **(scale)** the objects B_n = A × Fin n (n > 0) of `J_exact(A)` are realized by attaching
>   helper subsystems to X_A inside M*, with the fixed join reindexing (EP:33, EP:41);
> - **(I-1, coherence)** one label interpretation 𝓛_A covers every preparation p, protocol π and
>   history h of `J_exact(A)` and preserves sequential and outcome-dependent composition,
>   conditioning, helper attachment, spectators and discard (EP:67, EP:104, EP:112);
> - **(I-4, exactness)** p_{M*|_A}(h | π, p) = p_{T_A}(h | π, p) for every p, π, h of
>   `J_exact(A)`, where T_A is the trace law of EP:110 on `J_exact(A)` (the single-law reading of
>   `Q_exact(A)`, assumed here and put to the owner under D1);
> - **(I-2★, one construction)** Φ, Λ, μ, ι, R, τ and the resource policy are those of M* and do
>   not depend on A; A enters through enc_A only; nothing is computed from the values of
>   p_{T_A}; the resource policy states, as one rule, records, controller, ancilla supply and any
>   completion for arbitrarily large finite carriers (EP:106);
> - **(I-3, physical sourcing)** E and each clause of M* carry a source status, and the inclusion
>   counts as I★ only if E and M* pass the owner's sourcing test (§2.2, decision D5); a proof that
>   uses an unsourced or posited clause establishes the conditional inclusion I★[H] with H named.
>
> **Interface.** I★ is stated over `J_exact(A)`, which contains every finite-outcome CP instrument
> and every finite adaptive multi-time protocol. That goes beyond the corpus's single-time
> observation interface (c.7064942473): I★ relies on coherent intervention operations beyond the
> native interface, named here as the imported operational assumption **J-coh**. A weaker
> single-time form, I★_st, restricts the comparison to the single-time interface; it is listed as
> an owner option (D6), not proposed in place of I★.
>
> **Cardinality.** I★ quantifies only over finite A and imposes no cardinality on Ω. Lemma L-H
> (§4) derives a necessary condition from exactness; it is a consequence, not an assumption.
> Finiteness of A, of each finite adaptive history and of each finite resource used is a local
> hypothesis of the clause that uses it.
>
> **Milestone forms.** I-arch: one architecture with a model M_A per carrier A, each meeting
> I-1, I-2★ (with membership in M(E, `J_exact(A)`)), I-3 and I-4 on `J_exact(A)` (r4 §5.1, the
> intermediate milestone of answer 3). I-ε: the approximation target of EP:121 (Main:574–610).
> I-ε does not discharge I★. **I-arch does, on this scope:** by Lemma L-T (§5) the member
> M_{Fin 1} of an I-arch witness, with the transported encoding, is an I★ witness. Inside
> `J_exact`, the milestone and the target coincide.
>
> **Scope.** `J_exact(A)` only (endomorphic operations, helper attachment and discard, finite
> adaptive histories). Changes of system type and multi-wing protocols are the untyped remainder
> of part 1 (r4 §5.1 Scope), open.

**Design choices that are not the owner's wording.** The single label rule and the single
resource policy of I-2★ are design choices of this proposal; answer 3 asks for one fixed model,
one E, and the permitted encodings and resource requirements stated explicitly. The encoding rule
enc_A states the encoding physically, as answer 3 requires; an earlier draft of this proposal used
the bare index bijection β_A, which leaves the physical encoding unstated.

### 2.1 The scalability safeguard is nominal inside `J_exact`

The safeguard of c.7064859041 asks for "one coherent, scalable construction for arbitrarily large
finite carriers, with compatible dynamics and observation interfaces". On the scope of I★ it adds
no satisfiability content over r4's I at the singleton carrier: `J_exact(A)` already contains every
level B_n = A × Fin n with no upper bound (EP:33, EP:41), so any single witness at one carrier
already realizes every finite carrier size in one model, and L-T transports it to every A.
(scale), I-2★ and the single label rule therefore express the safeguard, but they do not
strengthen the target. Options that would make it substantive, for the owner (D7), none chosen:

- **SG-1, coexistence.** For A, A′ the model carries X_A and X_{A′} at once as separately
  addressable subsystems with a typed joint interface, so that `J_exact(A × A′)` is realized on
  X_A ⊗ X_{A′} with each factor's local operations those of its own encoding. This is the typing
  that the remainder of part 1 and B need.
- **SG-2, encoding compatibility.** For an injection A ↪ A′, X_A is a subsystem of X_{A′}, the
  operations of `J_exact(A)` on X_A are the restrictions of those on X_{A′}, and the complement is
  an inert spectator (no change of its law under operations on X_A).
- **SG-3, typed system-changing maps.** Isometric embeddings and partial traces between different
  carriers are typed and realized by the same dynamics (EP:41, EP:110 require an explicit
  implementation argument).
- **SG-4, stated resource scaling.** The resource policy gives an explicit bound on records,
  controller and ancilla resources as a function of |A|, the protocol depth and the number of
  outcomes, fixed before comparison.

### 2.2 Where the content of I★ lies: E and I-3

**The D-W witness.** With a trivial E, I★'s mathematical clauses are jointly satisfiable by a
classical simulator that stores the quantum state (the review sketch at c.7065022754 B1; the same
object is #1506's D-W, "a ψ-complete simulator satisfies the typed I-1, I-2, I-4 and the schema
with trivial E"): Ω holds a register with the density matrix of each level, a uniform seed in U, a
controller region and append-only records; Φ applies the requested branch rule to the stored
matrix, sampling the branch from the seed and keeping seed and history so that Φ is reversible; the
label rule is the identity on `J_exact(Fin 1)`, transported by L-T. It meets I-1, I-4 and I-2★ (one
Φ, one resource rule, no table of comparator values), EP:79–90 isolation and EP:102 admission
under trivial E, and L-H (the stored matrix has infinitely many response classes). It is a sketch,
not built and not reviewed as a proof; it is recorded as the sufficient-direction witness for
I-1 ∧ I-2★ ∧ I-4 at trivial E, at layer P.

**Consequence.** I★ is non-trivial only through E and I-3. Neither the label rule nor I-2★
excludes D-W: reading "nothing is computed from the values of p_T" as "Φ does not implement the
trace rule" would also exclude every faithful model unless a precise comparator-independent test
is stated. As written in r5 (and in r4), I-3 assigns a source label and yields I★[H]; it has no
pass/fail test.

**Candidate pass/fail tests for I-3, as owner options (D5); none is chosen here.** Each must be
stated without reference to `Q_exact(A)` (EP:102, r4 C-1).

| Option | Test | Excludes D-W? | Cost or conflict |
|---|---|---|---|
| T-SUB, substratum derivation | Φ is the substratum's dynamics, or its extension by E, and ι, R, τ are procedures of embedded observers on the substratum's visible sector ("one common substratum–observer realization", c.6875548603); no register of M* is defined by its content in a quantum state space | yes, if a register defined as "holds a density matrix" is barred | needs a precise notion of "derived from the substratum"; currently no candidate passes (I-3 NOT PASSED) |
| T-HTV, hard to vary (§A.29) | E states in advance the results it preserves, delivers at least one independent prediction or postdiction beyond the inclusion, and is rejected if adjustable to fit any outcome | yes: D-W's E predicts nothing beyond the comparator | judged per E; not mechanical |
| T-NOQ, no quantum primitive | E's statement contains no complex-matrix, CP-map or trace-rule primitive | yes | conflicts with decision 4 (complex matrices allowed as conditional input) unless the result is then labelled I★[K] |
| T-ACC, native access | every label is realized by procedures available to an embedded observer meeting C1–C4 through the native observation interface, with any reliance on coherent intervention named (c.7064942473) | not by itself: D-W's controller is an admissible loading under EP:75–79 | depends on D6 |

### 2.3 The other parts, carried from r4 with the owner records folded in

| Clause | r5 form | Required? | Source |
|---|---|---|---|
| C, type | C-model: a physically stated condition on the native data of M, with its consequences for experiment families stated explicitly; defined by the limits of embedded observation, with no reference to quantum outcomes; r4's admissibility conditions C-1 to C-5 kept | definition | answer 1; c.6891338304 |
| S⇐ (coverage) | for every A, M*|_A satisfies C and meets I★'s clauses; S⇐ implies I★ | required | answer 2; c.6891338304 |
| S-D (agreement with data) | every prediction of M* inside C for an experiment already performed matches the raw-direct data (§A.24) | required | c.6891338304 |
| S⇒ (soundness) | as r4 §5.2 | open question, reported as a finding, subject to S-D | c.6891338304 amends answer 2 |
| S-A (access closure) | accessibility half: every physically performable experiment within C is included in what is compared (coverage side of answer 4); exclusion half (barring stronger-than-quantum experiments) superseded | accessibility half required; exclusion half not a goal | answer 4 as amended by c.6891338304 ("Excluding PR is no longer a goal") |
| S⇐ᴺ (necessity) | as r4 §5.2 | optional future theorem | answer 2 |
| S-J (confinement) | as r4 §5.2 | required; tier Foundational | c.6878199016 |
| B (Bell) | B⇐ required; B⇒ ("exclude supraquantum ones", decision 3) affected the same way as S⇒; BELL-QSET text left pending by c.6891338304 | B⇐ mandatory; B⇒ per D2 | decision 3 of c.6875046763; c.6891338304 |
| G (gravity) | r4 §5.3 G-1 to G-3, on the same M* | required | c.6875548603 |
| Part 4, joint satisfiability | outside Gate A: Gate A is necessary for the unified endpoint and insufficient for Part 4 | required, not a Gate A clause | c.6877420015 |

## 3. Clause ledger with directional witnesses (§A.34)

For a clause of a target, the two directions are kept apart: **sufficient** = what discharges the
clause, and existing results that discharge it at another scope; **necessary** = what every witness
must satisfy, with the result that forces it. (N) = proved from OI's native assumptions; (I) =
conditional, imported assumptions named. Layers: K Lean kernel on `main`; X exact algebra; P paper;
R research record.

| Clause | Kind | Status | Sufficient direction | Necessary direction | Dependencies |
|---|---|---|---|---|---|
| I★ as a whole | mathematical statement; physical content only through E and I-3 | open | none under a non-trivial E. At trivial E, D-W (§2.2, P, sketch) meets the mathematical clauses. Interface-level route: `substratum_plus_control_qm` (StructuralClosure.lean:397, K) gives exact finite endomorphic QM for the generated theory, assuming `ExtendsSubstratum`, `StructurallyClosed`, `DrivesElementary`; that is a theory, not a model of the EP:73 schema. (I): imports complex matrix kinematics (decision 4), elementary drivability, J-coh | L-H (§4); Main:568 (P, unboundedness imported [55]); the record-capacity node N5 (§4); L-T (§5) | E; I-3 test (D5); J-coh (D6); H-∞ (`verification/ROADMAP.md`:81) for any completion route |
| (scale) | mathematical (interface typing) | proposed | holds once one model at one carrier is given (EP:33, EP:41; L-T) | none beyond I-1 | EP:33, EP:41, EP:106 |
| I-1 coherence | mathematical | open | D-W at trivial E | EP:67, EP:104, EP:112 | encoding rule |
| I-2★ one construction | mathematical + resource accounting | open | D-W at trivial E | a per-size family fails it by definition; by L-T the per-size loophole is already closed by I-1 at one carrier, so I-2★ adds no satisfiability content on this scope (§2.1) | resource policy (EP:106) |
| I-3 physical sourcing | physical/operational | open; NOT PASSED; no pass/fail test stated (D5) | none. Earliest assumed mechanism: elementary drivability (continuously tunable state mixing) in a structurally closed class (Main:598; `substratum_plus_control_qm` hypothesis `hd`); native preparation, readout and records (`verification/programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md`:21 and `verification/programmes/oi-qm/reconstruction/meas-q-20261120/RESULT.md`:33 record physical sourcing NOT PASSED) | the monomial class lacks composite control: `substratumGen_not_control` (StructuralClosure.lean:330, K; two-state carrier), `substratumTheory_not_layerFlowExecutable` (LiftAudit.lean:200, K). (N)-type no-gos for the specified monomial implementation class only | E; native coherent operation; native preparation, readout and records |
| I-4 exactness | mathematical | open | D-W at trivial E; none under a non-trivial E. I-ε (Main:574–610, P) is an approximation with supplied quantum data and does not discharge I-4 | L-H; Main:568; N5; the all-time periodicity obstruction of a fixed finite bijection with a fixed prior (Main:650, P) at its own autonomous multi-time scope | isolation EP:79, EP:81–90; H-PI; J-coh |
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
1 − P_k − P_k⊥}, record the outcome. These measurements in countably many bases are coherent
interventions beyond a fixed-basis single-time readout; L-H relies on J-coh.

**Hypotheses on M (all from the contract, none quantum).**
- **H-ISO** (EP:79, literal): for a fixed preparation, the law of the uncontrolled variables U is
  unchanged by the choice of later setting until the declared interaction. So each preparation p
  induces one law ν_p on U, the same for every π_k.
- **H-PI** (a reading of EP:75, EP:79 and EP:90; not stated there in these words): **the
  controller fields loaded for π_k do not depend on p.** Then, with Φ fixed, the response of
  outcome o of π_k is a measurable function ξ_{k,o}(u) ∈ [0, 1] of the uncontrolled variables
  alone. EP:75 lets ι depend on p, and EP:81 conditions on "p, retained past", so the contract
  does not fix this literally. (The earlier wording, "does not read a record of the preparation
  label", was ill-defined: for a pure preparation the prepared system's own state is such a
  record, as D-W shows.)
- **Exactness** (I-4): p_M(o | π_k, p) = Tr(P_o ρ_p) exactly.

**Statement.** Let κ(u) = (ξ_{k,o}(u))_{k,o} be the response vector of u over this countable
family. Under H-ISO, H-PI and I-4, κ takes infinitely many values on the union of the supports
of ν_{ψ_k}. So the set of response classes {u ~ u′ iff κ(u) = κ(u′)} reachable by preparations
of one qubit level is infinite. This constrains the family of instruments jointly: each single
instrument may have finitely many outcomes, as finite observer access allows (c.6875046763).

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
ontic states. It uses pure preparations, one projective instrument per protocol and exact zeros; it
uses no nonnegative-rank import.

**Depth-first nodes and verdicts.**
- **N1. Is L-H strictly stronger than "Ω is infinite"?** Check: a model with infinite Ω whose
  instruments couple to finitely many response classes (an infinite hidden sector the instruments
  never resolve) satisfies "Ω infinite" and violates L-H. Verdict: yes; it constrains the
  observer interface (ι, R, τ and the coupling), not only the cardinality of Ω.
- **N2. Which hypotheses are load-bearing?** Check, H-ISO dropped: a finite-U model can load u as
  a sample of the quantum outcome given (p, π), reproducing every single-shot law; L-H fails.
  Check, H-PI dropped: ι can write into the controller fields, from (p, π, λ), a sample of the
  quantum outcome, which the instrument then reads; L-H fails (see N5 for its cardinality). Check,
  exactness dropped: I-ε holds with finite carriers (Main:574–610). Verdict: all three are
  load-bearing; H-PI is the assumption exposed (assumption-watch marker AW-R5-1: "the controller
  fields loaded for an instrument do not depend on the preparation"; it applies to every O3
  readout construction).
- **N3. A model that assumes A1.** If a model takes Ω = S finite (A1 assumed for that model, which
  `main` does not do, Sub:92), and H-PI holds, κ takes finitely many values and L-H fails, so such
  a model cannot meet I-4 on a qubit level. Verdict: CONFIRMING. It restates, for response
  classes, what is already on record: Main:568, EP:123, #914 c.6875046763 ("the target cannot
  assume one fixed finite total carrier") and r4 I-4 ("no fixed finite total carrier is assumed",
  r4:208). It is not a dependency of the target on #1477.
- **N4. Does L-H give more than countably many classes?** Check: the proof needs only a countable
  family and yields "infinite". Verdict: no stronger cardinality is claimed.
- **N5. Under a finite Ω, is H-PI dispensable?** Check, single-shot protocols: the seed space Λ is
  separate from Ω in the EP:73 schema and may be infinite; ι(p, π, λ) can write a finite outcome
  sample into a finite controller field with exactly the quantum probabilities, so finiteness of
  Ω alone does not exclude a single-shot exact reproduction once H-PI is dropped. What excludes it
  is EP:75 ("cannot be chosen to fit ... a desired output history") and EP:92 (lookup tables
  "do not count"), which are prose, not a formal hypothesis. Check, the whole of `J_exact(A)`:
  it contains adaptive histories of every finite depth with retained, repeatedly readable records
  (EP:39–40); if the record map R reads the retained record from the configuration at
  termination, distinct histories of depth K need distinct configurations, so |Ω| ≥ 2^K for every
  K and Ω is infinite whether or not H-PI holds. Verdict: H-PI is not dispensable for single-shot
  protocols under finite Ω; an infinite Ω is forced by record capacity alone, with no quantum
  content, under the stated reading of R. This sharpens N1: L-H's own content is the response-class
  condition on a qubit level, not the cardinality of Ω.

**Outcome.** Gem by the test fixed before the attempt (N1, N2, N5). Classification: ELABORATING
for the cardinality content, CONFIRMING for N3, NEW for AW-R5-1 and for N5's separation of
record-capacity infinity from response-class infinity.

**L-H in the three questions.** Label **(I)**.
- Established: the statement above, at layer P, in this record, not independently re-reviewed in
  r5.1 (the review of `95073878` found the proof correct under its hypotheses).
- Assumed: H-ISO (EP:79); H-PI (a reading of EP:75, EP:79, EP:90); exact comparator law at exact
  zeros (EP:110); J-coh (projective measurements in countably many bases). No quantum assumption on
  the OI side. No Lean statement of it exists on `main`; `classical_exposed_ncard_le`
  (KInfFoundations.lean:947) is a different bound (exposed points of a body in the N-simplex under
  a facet hypothesis) and is not duplicated.
- Missing: whether H-PI is a contract requirement (D3); whether the measurements used lie in the
  native interface (D6). Both are decisions about the target, not mathematics.

## 5. Lemma L-T: the single-model form at one carrier (paper)

**Statement.** I★ holds iff there is one model M with
(a) M ∈ M(E, `J_exact(Fin 1)`), admitted independently of the comparator (EP:102);
(b) one resource policy stated as one rule for every level (EP:106), and nothing in Φ, Λ, μ, ι,
R, τ computed from the values of the comparator law;
(c) I-1, I-3 and I-4 on `J_exact(Fin 1)`;
(d) the encoding rule enc_A of I★ taken as the transport of M's level encodings along β_A and the
fixed join reindexing, for every nonempty finite A.

- **⇒ (restriction).** An I★ witness restricted to A = Fin 1 satisfies (a)–(d): (a) and (b) are
  I★'s membership and I-2★ clauses, (c) is I★ at Fin 1, (d) is its encoding rule. Witness: the
  definition of I★.
- **⇐ (transport).** Given M with (a)–(d), put |A| = k. The bijection
  (A × Fin n) ≃ Fin k × Fin n ≃ Fin (k·n) sends each object of `J_exact(A)` to the level
  B_{kn} of `J_exact(Fin 1)`, and preparations, instruments, helper attachment, spectators and
  discard to the corresponding operations there (EP:33–41: every level n > 0 is present). For
  the mixed-radix reindexing (a, b) ↦ b + n·a the two routes
  (A × Fin n) × Fin m → Fin (k·n·m) agree, since c + m·(b + n·a) = (c + m·b) + (n·m)·a; for any
  other fixed reindexing they differ by a permutation of basis labels, which is itself a unitary
  instrument of `J_exact(Fin 1)` and is absorbed into the transported label. The trace law is
  invariant under conjugation by permutation unitaries, so p_{T_A}(h | π, p) =
  p_{T_{Fin 1}}(h | β(π), β(p)) for every p, π, h. So I-1 and I-4 hold at A for the same M; (a)
  gives membership at A because the procedures are the same; (b) gives I-2★ because Φ, Λ, μ, ι,
  R, τ and the resource rule are unchanged and A enters only through enc_A; I-3 is a property of
  M and E, not of A. Witness: this exact algebra (layer X, on paper).

**Consequence.** I-arch at the singleton implies I★ on this scope (§2 Milestone forms), and the
scalability safeguard is nominal inside `J_exact` (§2.1).

**L-T in the three questions.** Label: **definitional**; it uses no OI assumption and is not a
finding about OI under the (N)/(I) scheme.
- Established: the equivalence above, at layer X on paper, unreviewed in r5.1 (the review of
  `95073878` checked the transport algebra).
- Assumed: the EP definitions of `J_exact`, the fixed join reindexing and the trace law.
- Missing: nothing mathematical within its statement; it does not cover separately addressable
  coexisting subsystems (SG-1), which belong to B and to the remainder of part 1.

## 6. Dependencies stated explicitly

- **A1 and #1477.** I★, I-arch and I-4 do not depend on the A1 retirement landing: on `main` A1
  is an open hypothesis, not adopted (Sub:92), the cardinality of the total configuration space is
  left open (Main:60), and EP:73 places finite or infinite resources in E. They require that the
  witness not assume a finite Ω (N3, N5); that requirement is already on record (Main:568, EP:123,
  #914 c.6875046763, r4:208). The retirement, once landed, removes the A1 identifier and states
  cardinality neutrality in the setup; it does not establish existence or consistency of an
  infinite sector (c.7058446475, c.7064859041). Finite-only results cited in §3 carry
  `[Fintype A]` or `[Fintype S]` and stay scoped to finite carriers.
- **Infinite completion.** Any route through a completed carrier depends on H-∞
  (`verification/ROADMAP.md`:81, open); `localHom_unique` (QuasilocalCharacterization.lean:248) is
  a uniqueness theorem, not an equivalence (§A.34), and `q3_countermodel`
  (InstrumentAvailability.lean:335) shows the frozen structure does not supply infinite-support
  coherent operations.
- **Kinematics.** Every sufficient route cited imports complex matrix kinematics (decision 4).
- **Interface.** I★ and L-H rely on J-coh (c.7064942473; D6).
- **Soundness and Bell.** S⇒, S-A and B⇒ follow c.6891338304 by default (§2.3, D2).

## 7. The three questions, for the record as a whole

1. **Established.** L-H (§4, (I)); L-T (§5, definitional); D-W (§2.2, a sketch at layer P, not a
   proof) shows that I★'s mathematical clauses are jointly satisfiable at trivial E. No clause of
   I★ is discharged under a non-trivial E.
2. **Assumed.** For L-H: H-ISO, H-PI, the exact comparator law, J-coh. For every sufficient route
   cited: complex matrix kinematics; elementary drivability (`DrivesElementary`, hypothesis `hd` of
   `substratum_plus_control_qm`); structural closure (`StructurallyClosed`); finiteness of the
   carrier (`[Fintype A]`).
3. **Missing.** The earliest missing step is a decision followed by a physical mechanism. The
   decision is a pass/fail test for I-3 and E that is independent of the comparator (D5): without
   it, D-W meets the mathematical clauses and I★ has no content beyond them. The mechanism is a
   native, physically sourced operation of elementary drivability acting on an observer-accessible
   sector, inside one model, together with native preparation, readout and records (I-3). Existence
   of an exact single model over all finite carriers is not the open mathematical question it was
   stated to be at `95073878`: D-W supplies one at trivial E. The open mathematics is existence
   under a non-trivial E that passes the chosen test, and the typing SG-1 to SG-3 if the owner
   makes the safeguard substantive.

## 8. Reconciliation proposal (for owner decision; nothing edited)

- **Contract on `main`.** `endpoints.md`:51–69 (the class-wide two-direction display) stays
  unchanged. If the owner adopts r5, the landing would add r5 as an append-only forward amendment
  in this record directory, with EP:56–59 read as superseded class-wide (as r4 §4.1(a)), EP:61–64
  read as I without I-2★, I-3, (scale) and the encoding rule, and every other EP line kept (r4 §3
  residual clause).
- **Off-`main` r4. Departure from answer 5, flagged for owner decision (D4).** Answer 5
  (c.6876591512) directs "Prepare r4 for preservation on main through the normal gates". This
  record proposes instead to keep r4 (`3a1c8e97`) on its branch and cite it by reference, since r5
  restates every clause it uses (§A.42 item 8). That is a departure from answer 5, not routine
  housekeeping; the alternative is to land r4 with its status note r6 as answer 5 directs, with r5
  as a later forward amendment.
- **#1428 GATE-A row is stale.** It reads "owner answers to `OWNER-QUESTIONS-r4.md` (four
  questions) ... | blocked: owner questions", and its open-work note says the four questions "are
  open". The four questions were answered at #1169 c.6876591512 (2026-11-14), before #1428 was
  opened (2026-11-19). #1428 is not edited here. Proposed corrected row:

| ID | Item | Tier | Prerequisites | Readiness | Authorization |
|---|---|---|---|---|---|
| GATE-A | Gate A forward amendment for the superset target, r4 and status note r6 (#1289); consolidated as r5 (this record) | supporting (provisional) | owner answers given at #1169 c.6876591512; soundness amended at c.6891338304; owner decisions D1–D7 of the r5 proposal, including the r4 preservation route (answer 5) | r5 preparation and independent review | U1 authorized as preparation and review (#1169 c.7064859041); adoption not authorized |

  Proposed replacement for its open-work note: "GATE-A. The four owner questions were answered at
  #1169 c.6876591512, and soundness was amended at c.6891338304. The answers are folded into the
  r5 proposal (Issue #1502, PR #1503), which awaits owner adoption. The contract
  `oi-qm-ext-1/endpoints.md` on `main` is unchanged."

## 9. Owner decisions needed

- **D1.** Adopt, amend or reject the exact statement of I★ in §2, including the encoding rule,
  the design choices of one label rule and one resource policy, and the single-law reading of
  `Q_exact(A)` assumed in I-4 (EP:43 and EP:110 support it; EP:56 and EP:61's "there exists one T
  in Q_exact(A)" leave it formally open; r4 §7 R2). r5 does not settle that reading.
- **D2.** By default r5 follows c.6891338304: soundness is an open question subject to agreement
  with performed experiments, the exclusion purpose of access closure and of B⇒ is superseded, and
  the accessibility half of answer 4 survives on the coverage side. The residual question: was
  c.7064859041's "The 14 November decisions are authoritative inputs" meant to restore answers 2
  and 4 as they stood before c.6891338304?
- **D3.** Whether H-PI ("the controller fields loaded for an instrument do not depend on the
  preparation") is a contract requirement. It is load-bearing for L-H and for every readout
  construction.
- **D4.** The r4 preservation route (answer 5, or by reference as proposed in §8), the landing of
  r5 after independent review, and the #1428 correction.
- **D5.** The pass/fail test for I-3 and E: one of T-SUB, T-HTV, T-NOQ, T-ACC, a combination, or
  another (§2.2). Without one, I★ is met at trivial E by D-W.
- **D6.** The interface: I★ over `J_exact` with J-coh named, or the weaker single-time form I★_st
  (c.7064942473), or both as stages.
- **D7.** Whether to make the scalability safeguard substantive through SG-1 to SG-4 (§2.1).

## 10. What this record does not do

It edits no manuscript, no `endpoints.md`, no Issue body and nothing of #1477 or #1483; it runs no
computation and dispatches no workflow; it proposes no E and no C and chooses no I-3 test; it does
not post on #1169.

## 11. Response to the review of `95073878` (c.7065022754)

| Finding | Response |
|---|---|
| B1 D-W simulator | §2.2: D-W recorded as the sufficient-direction witness at trivial E (cross-reference #1506 D-W); I★'s content located in E and I-3; I-3 test options T-SUB, T-HTV, T-NOQ, T-ACC put to the owner (D5), none chosen; §7 item 3 corrected |
| B2 A1 misread | §1, §6, N3: A1 is an open hypothesis on `main`; N3 restated as conditional on a model assuming A1, with H-PI carried, classified CONFIRMING with the prior records cited; the dependency on #1477 withdrawn; new node N5 on H-PI under finite Ω |
| B3 L-T and the milestone | §2 Milestone forms: I-arch implies I★ on this scope; L-T's right-hand side now carries membership (EP:102), the one-rule resource policy and non-fitting (EP:106), so ⇐ delivers all of I-2★; §2.1 states that the safeguard is nominal inside `J_exact` and proposes SG-1 to SG-4 (D7) |
| B4 encodings | I★ restates the physical encoding enc_A = (X_A, β_A), "any fixed choice" of bijection; single label rule and resource policy marked as design choices |
| B5 D2 | D2 restated as the residual question raised by c.7064859041; default follows c.6891338304; B⇒ included |
| B6 owner records | c.7064942473 cited (§1, §2 Interface, J-coh, D6); "r4 by reference only" flagged as a departure from answer 5 (§8, D4) |
| Q_exact(A) single law | stated as assumed in I-4 and put to the owner in D1 |
| Nits | L-T labelled definitional; per-result three-question lines for L-H and L-T; "preregistered" replaced by "fixed before the attempt"; "observer-resolvable" replaced by an instrument-family condition compatible with finite access per instrument; H-PI reworded to the controller-field form |

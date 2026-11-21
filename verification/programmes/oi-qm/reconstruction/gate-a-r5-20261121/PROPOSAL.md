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
response to each finding is listed in §11. r5.2 additionally takes D-W in the corrected form of
the #1506 review (c.7065065491 R5) and corrects two nodes of L-H (N2, N5) with a new node N6.
r5.3 answers the delta review at `4649d047` (#1503 c.7065136670, R1–R6). r5.4 answers the
delta review at `dada0c8c` (#1503 c.7065208959: one blocking item on D5, nits N1–N4); r5.5 and
r5.6 answer c.7065233367 and c.7065260286; r5.6 was reviewed at `fd3cb064` (c.7065281854). r5.7
folds the T1/T2 corrections of §2.4 confirmed in #1510 (c.7066267563) under #1169 c.7067233614;
r5.7 is not yet re-reviewed.

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
> single-time form, I★_st, is defined in §2.4 from the corpus's own single-time interface; it is
> listed as an owner option (D6), not proposed in place of I★.
>
> **Cardinality.** I★ quantifies only over finite A and imposes no cardinality on Ω. Lemmas L-H
> and L-H′ (§4) derive necessary conditions from exactness: by L-H′, every exact witness has U
> taking infinitely many values, so Ω is infinite. That is a consequence, not an assumption, and
> it conflicts with nothing on `main`, where A1 is not adopted (Sub:92) and the cardinality of the
> total configuration space is left open (Main:60).
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
strengthen the target. The options below were offered at r5.1. None of them adds a constraint
inside `J_exact(A)`: D-W meets SG-1, SG-2 and SG-4 at trivial E (its register handles tensor
products, restriction and inert complements), and SG-1 to SG-3 are typing beyond `J_exact`
(joint, nested and system-changing interfaces). They are therefore scope decisions that widen the
interface, not sharpenings of I★, and their force against D-W again comes only from E and I-3:

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
- **SG-4, stated resource scaling.** As worded at r5.1 it has no units. By L-H′ every witness
  has infinitely many configurations, so a bound "on records, controller and ancilla resources" is
  vacuous unless counted in native units. A precise form is **SG-4′**: Ω is declared
  site-factorized with a finite local alphabet and finite-range dynamics, and the number of sites
  whose configuration the realization of any protocol of depth K with at most m outcomes per step
  on carrier A reads or writes is at most f(|A|, K, m), for a function f fixed before comparison.
  SG-4′ is a real constraint, but it presupposes a declared site structure (E-content), and #1504's
  Proposition U (on a site-factorized Ω with finite-range dynamics, a native exact qubit needs
  readout cones that lie in no finite region, as reported in the #1506 review c.7065065491 R8; not read here) would make it unsatisfiable for any
  finite f. It is recorded, not recommended.

**Verdict on scalability.** No constraint is stated here that is both precise inside `J_exact` and
known to be satisfiable by some exact model; a substantive scalability safeguard is an **open
question** for the owner (D7), with SG-1 to SG-3 available as interface widenings and SG-4′ as a
precise but probably unsatisfiable resource form.

### 2.2 Where the content of I★ lies: E and I-3

**The D-W witness, in its corrected stepwise form.** With a trivial E, I★'s mathematical clauses
are jointly satisfiable by a classical simulator that stores the quantum state (the review sketch
at c.7065022754 B1; #1506's D-W, as corrected by the #1506 review, c.7065065491 R5). The form
matters. A **precomputed** version, in which ι writes the whole run and Φ only shifts it, is not
admissible: the loaded configuration then encodes outcomes of later instruments, which depend on
the future program, against EP:77 (U includes every uncontrolled variable relevant to later
outcomes) and EP:79 (a future-program change loads only controller fields, with U's law unchanged
until the setting interaction). The **stepwise** version is the witness: Ω = seed tape × simulator
register (holding the density matrix of each level) × isolated program fields × append-only
records, and Φ is one reversible (Bennett-style) step that consumes the seed entry λ_j at step j,
reads only the current instruction, applies that instrument's branch rule to the stored matrix and
appends the outcome. The label rule is the identity on `J_exact(Fin 1)`, transported by L-T. It
plausibly meets I-1, I-4, I-2★ (one Φ, one resource rule, no table of comparator values), EP:77–90
isolation and prefix compatibility, EP:102 admission under trivial E, and L-H and L-H′ (the seed
tape has non-atomic law; the register takes infinitely many values). It is a sketch, not built and
not proved; the #1506 review states its conclusion conditional on this restatement and on the
typed schema including U-completeness and isolation. It is recorded here, on that condition, as
the sufficient-direction witness for I-1 ∧ I-2★ ∧ I-4 at trivial E, at layer P.

**What excludes it.** No clause of I★ and no typable clause of EP. What excludes it is EP's
requirement that ι be "built from the candidate's stated admissible preparation procedures"
(EP:75), the lookup-table clauses (EP:47, EP:92) and comparator-independent admission (EP:102),
together, and only once a **nontrivial E names an admissible procedure class for ι and μ_p that is
independent of the labels' numeric entries** (c.7065065491 R5). A finite-information or
finite-support condition on ι alone does not exclude it: μ_p may depend on p (EP:75, EP:97), so the
label's numeric content can ride in the seed law.

**Consequence.** I★ is non-trivial only through E and I-3. Neither the label rule nor I-2★
excludes D-W: reading "nothing is computed from the values of p_T" as "Φ does not implement the
trace rule" would also exclude every faithful model unless a precise comparator-independent test
is stated. As written in r5 (and in r4), I-3 assigns a source label and yields I★[H]; it has no
pass/fail test.

**Candidate pass/fail tests for I-3, as owner options (D5); none is chosen here.** Each must be
stated without reference to `Q_exact(A)` (EP:102, r4 C-1). Given the corrected D-W, a test
excludes it only by constraining the admissible procedure class of ι and μ_p, or the content of
E, not by a finite-information bound on ι. r5.2's table is corrected below (c.7065136670 R2–R3).
For each option the question is whether a repaired form excludes the stepwise D-W without
excluding legitimate exact OI models. No legitimate exact OI model is known (I-3 NOT PASSED), so
the second half can be checked only against the corpus's own routes: the completion route (a quasilocal
C*-system over finite-region matrix algebras, whose finite-region states are density matrices,
GR:279–284, H-∞) and the extension
characterizations (L3–L5 of §3).

| Option | Test, as offered and as repaired | Excludes the stepwise D-W? | Excludes legitimate exact models? | Verdict |
|---|---|---|---|---|
| T-PROC, admissible procedure class | As offered: procedures generated from a fixed finite repertoire, labels entering only through which operations are applied. Repair attempted: continuous parameters admitted only as durations or strengths of a fixed finite set of native generators fixed in E | as offered, yes; repaired, **no**: a stepwise simulator reads the durations from its program fields and computes the corresponding map on its stored matrix, so any computable label-to-procedure rule is emulated | as offered, **yes, every exact model**: countably many procedures cannot realize a continuum of preparation labels exactly unless the seed law μ_p carries the label, which re-admits D-W | **fails** (dilemma: discrete classes exclude all exact models; continuous classes are emulated) |
| T-SUB, substratum derivation | As offered: Φ is the substratum's dynamics or its extension by E; no register defined by quantum-state content. Repair attempted (T-SUB′): Φ is exactly the substratum's own update, X_A a sector of the substratum configuration, and E adds only observer-access procedures | as offered, evadable by redescription (a register of real amplitudes, or of integers encoding them, is "not defined in a quantum state space"); T-SUB′, yes (D-W's Φ is not the substratum update) | as offered, yes: it bars the corpus's completion route, whose finite-region states are density matrices (GR:279–284); T-SUB′ is the native form, which decision 1 of c.6875046763 makes the sourcing programme rather than the formal target, and the kernel no-gos `substratumGen_not_control`, `substratumTheory_not_layerFlowExecutable` exclude only the specified monomial class at configuration level, not the substratum together with the observer-access procedures T-SUB′ allows; T-SUB′ is **not shown** to exclude any exact model | **fails as offered**; **T-SUB′ is live only with the (iv) dilemma stated** (below): clauses (i)–(iii) exclude a D-W whose Φ is not the substratum update, but a computationally universal substratum can host the stepwise D-W inside Φ, so exclusion rests on (iv). Under decision 1 of c.6875046763 ("Extension form as the formal target; native form as the sourcing programme") it keeps the extension form as the formal target, as the conditional inclusion I★[H], and makes the native form what unconditional I★ requires. Its cost: every existing sufficient route then yields only I★[H], with H naming two hypotheses: `hd` of `substratum_plus_control_qm` (unsourced), and the existence of an EP:73-schema model realizing the generated theory (unconstructed), since the route yields a theory, not a model (§3); the monomial-class no-gos bear on it at their own scope. **Definition of "observer-access procedure" for T-SUB′.** A procedure is an observer-access procedure iff (i) its loading sets only configurations of the substratum's visible sector under the observer partition (setting and program fields included); (ii) every transition it involves, apparatus included, is a step of the substratum update Φ on substratum configurations; (iii) its outcomes and records are functions of visible-sector configurations at declared times; and (iv) the distinguishable alternatives of the encoded carrier X_A are |A| configurations of a substratum sector, and no region used by the procedure holds a configuration that encodes the numeric entries of a state or instrument label (an apparatus running a simulator of a stored state does not count as access). Clause (iv) is load-bearing: without it, a computationally universal substratum could host the stepwise D-W inside Φ and pass (i)–(iii). Whether (iv) itself resists redescription of such a register is not settled here; see the (iv) dilemma below the table |
| T-HTV, hard to vary (§A.29) | Repaired (T-HTV′): at least one independent prediction or postdiction of the raw-direct kind (§A.24) derived from the same clauses of E and M* that the inclusion proof uses (no bolt-on clause), and rejection if the model class can be adjusted to fit any outcome | yes: D-W's clauses yield exactly the comparator's laws and nothing else, and its class reproduces any operational theory by swapping its branch rule | not checkable: no legitimate exact model exists to test; "derived from the same clauses" needs a dependency notion not yet stated | **survives conditionally**, as a judgment criterion, not a decision procedure |
| T-NOQ, no quantum primitive | As offered: E's statement contains no complex-matrix, CP-map or trace-rule primitive. Repair attempted: the condition ranges over M*'s data (Ω, Φ, ι), not only E | as offered, **no** (c.7065136670 R3): D-W's E is trivial and its quantum content sits in Φ and the register; repaired, evadable by redescription as for T-SUB | repaired, yes: conflicts with decision 4 and bars the completion route | **fails** |
| T-ACC, native access | Every label realized by procedures of an embedded observer meeting C1–C4 through the native interface, reliance on coherent intervention named | not by itself: D-W's controller is an admissible loading under EP:75–79 | no | **fails as an exclusion test**; useful only with D6 |

**The (iv) dilemma (c.7065260286).** Clause (iv) has two readings. *(iv)-explicit* (no region holds the entries as a readable numeral or register) is dodged by redescription: the stepwise D-W can hold ρ encrypted, compressed or spread across sites by a fixed bijection, or run lazily from the preparation parameters and the retained instrument history (records EP:39–40 requires anyway), so in a computationally universal substratum it does not exclude D-W. *(iv)-recoverable* (some fixed decoding of the configuration on its support yields the entries) resists redescription and excludes D-W, but it is the definition of a ψ-ontic model; by PBR, any exact model whose independently prepared systems satisfy the Preparation Independence Postulate (PIP) is ψ-ontic for pure states, and `J_exact` contains the two-copy entangled measurements PBR uses (every CP instrument on helper levels), so (iv)-recoverable excludes every exact `J_exact` model that satisfies PIP. This last step is **(I)**, importing [PBR] with PIP named; PIP is not imposed by OI (`papers/Methodology.md`:405: "PBR cannot simply be imported as a theorem about bare OI without first establishing its preparation-independence premise"), and whether EP:41's independent helper attachment with the isolation of EP:79/81 implies PIP at the ontic level is not settled. So T-SUB′ excludes D-W only when the substratum is not computationally universal, or under (iv)-recoverable; under (iv)-explicit it is evadable, and under (iv)-recoverable it also excludes every PIP-satisfying exact model.

**The completion route under (iv).** It is barred under (iv)-recoverable, since its finite-region states are density matrices (GR:279–284), but it lies outside the EP:73 schema altogether (an algebra, with no configurations), so the bar changes nothing for it; it remains a route to I★[H] only.

**Result for D5.** The bar "excludes D-W and is known not to exclude legitimate exact OI models"
cannot be met by any option until a legitimate exact OI model is known, since none is (I-3 NOT
PASSED); it records the state of knowledge, not a defect of the options. On the checks that can
be run: T-PROC, T-NOQ and T-ACC fail, and T-SUB fails as offered. Two options remain live:
**T-SUB′**, subject to the (iv) dilemma: under (iv)-explicit it fails to exclude D-W in a
computationally universal substratum, and under (iv)-recoverable it also excludes every exact
`J_exact` model satisfying PIP (conditional on [PBR]); in either case every existing sufficient
route yields only I★[H]; and **T-HTV′**, a judgment criterion whose
dependency notion ("derived from the same clauses") is not yet stated, and which excludes D-W on two
grounds (no independent prediction; adjustability). The structural pattern behind the failures
(paper argument, not a theorem): a test stated on the label or procedure interface is defeated by
universal emulation, because a stepwise reversible simulator can execute any computable procedure
rule on a stored state; a test stated on the ontic representation is defeated by redescription,
and tying it to the substratum's fixed dynamics (T-SUB′) does not escape this when the substratum
is computationally universal, unless (iv) is read as recoverability, which meets PBR. This record
chooses none of the live options.

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

### 2.4 The single-time form I★_st, defined from the corpus's single-time interface

**The corpus's interface.** The single-time observation interface is fixed in `Sub:249` and in
`familyAt` (`verification/lean-mathlib/OIBridge/SemigroupTransfer.lean`:93): a fixed visible/hidden
interface V × H, a fixed hidden prior ω_H (uniform in `familyAt`), admissible preparations ρ_V on
the visible sector, and the one-time visible channel family
Φ_t(ρ_V) = Tr_H[φ̂^t (ρ_V ⊗ ω_H) φ̂^{−t}], t ∈ ℕ, with φ̂ the permutation unitary of the
substratum bijection. Each time is compared separately; there are no interventions between times
and no multi-time records. `Sub:249` distinguishes the coherent comparison (equality of the
coherent reduced-channel family, written ∼) from population-only comparisons (the rooted
transition probabilities T_ij(t)), stated separately. c.7064942473 retains this interface.

**Source of this subsection's typing.** The T1 and T2 corrections below are folded in from the
T1/T2 record (`verification/programmes/oi-qm/reconstruction/gate-a-r5-t1t2-20261121/PROPOSAL.md`,
PR #1510 at `c45b82cf105386b86e12322de6169abac5a9ff22`, confirmed at #1510 c.7066267563), under the
owner's approval in principle (#1169 c.7067233614). That record carries the proofs and the
failure table in full; only the confirmed typing corrections are carried here, and no claim of
GATE-A is broadened.

**I★_st (two variants, each in Born form and operational form).** The comparator side below is a
design choice of this proposal, put to the owner under D6: neither `Sub:249` nor `familyAt` fixes
it. It takes time-homogeneous families with a finite environment; the corpus also treats
time-inhomogeneous single-time families (`Main:652`, the U(t) = e^{−iσ_x t²} remark), which this
choice leaves out. For every nonempty finite A and every quantum single-time family
Λ_A = {Λ_t}_{t ∈ ℕ} on A of the form Λ_t(ρ) = Tr_K[W^t (ρ ⊗ σ_K) W^{−t}] with K finite, W unitary
and σ_K a density matrix, the one model M* has a visible sector V_A encoded by enc_A, its one
hidden prior and, from the typed data of Λ_A and fixed before comparison, a setting s_Λ of its
controller fields loaded under EP:79, such that, with s_Λ loaded, the conditions below hold
(typing (b); under typing (a), s_Λ is part of a preparation (ρ, s_Λ) whose hidden state may depend
on s_Λ but not on ρ, EP:75).

- **Indexing (T2).** A sector indexed by A alone, with φ and the prior fixed, carries exactly one
  autonomous family, so for |A| ≥ 2 it cannot meet two distinct targets (Λ_t = id and Λ_t = Ad_Z^t
  differ at t = 1 on |+⟩⟨+|); the family is therefore indexed by (A, Λ) through s_Λ. A setting
  cannot change the hidden prior (EP:79). Under typing (b) the family is
  Φ^{(A,Λ)}_t(ρ) = Tr_{C×H}[φ̂^t (enc_A(ρ) ⊗ |c_{s_Λ}⟩⟨c_{s_Λ}| ⊗ ω_H) φ̂^{−t}], read back through
  enc_A, with C the controller fields; under (a), Tr_H[φ̂^t (enc_A(ρ) ⊗ ω_{s_Λ}) φ̂^{−t}]. Both are
  linear in ρ. The interface of `Sub:249` is unchanged.
- **Encodings.** Every family is read through enc_A and the label rule 𝓛_A of the I★ witness; this
  is part of the definitions and is named in FE-ADM below, not a separate assumption.
- **Operational single-time channel.** p_{M*}(E | s_Λ, ρ, t) is the probability of the first
  outcome when ρ is prepared on X_A with s_Λ loaded, the model evolves freely for t steps and the
  readout {E, 1 − E} is applied and recorded; Λ̂^{M*,(A,Λ)}_t is the linear map L_t with
  p_{M*}(E | s_Λ, ρ, t) = Tr(E L_t(ρ)) for every density ρ and effect E, unique when it exists
  (Lemma TC of #1510, mathematical/definitional, no OI assumption).
- **I★_st-coh:** Φ^{(A,Λ)}_t = Λ_t at every t (the ∼ comparison of `Sub:249`, Born form).
  **I★_st-coh^op:** Λ̂^{M*,(A,Λ)}_t = Λ_t at every t.
- **I★_st-pop:** ⟨j|Φ^{(A,Λ)}_t(|i⟩⟨i|)|j⟩ = ⟨j|Λ_t(|i⟩⟨i|)|j⟩ for all i, j ∈ A at every t.
  **I★_st-pop^op:** the same with p_{M*}(|j⟩⟨j| | s_Λ, |i⟩⟨i|, t) in place of the Born-form value.

None of the variants contains instruments, helper levels, adaptive protocols or retained records,
so EP:38–41, (scale), SG-1 to SG-4 and N5 do not apply to them; the operational variants use the
protocols π(ρ, Λ_t, E) (prepare ρ, apply Λ_t, read {E, 1 − E}), which lie in `J_exact(A)` by
EP:37–40. The coherent variants use coherent inputs and arbitrary readouts, and so J-coh; the
population variants do not. The other I★ clauses (one model, one E, enc_A, I-2★ without the
ancilla clause, I-3) carry over.

**Assumptions for the relation to I★ (named, not built into the definitions).**
- **FE-ADM (free evolution as an admissible protocol).** For every A, Λ and t, "load s_Λ, prepare
  ρ, evolve freely under Φ for t steps" is the witness's label interpretation 𝓛_A of "prepare ρ,
  apply Λ_t", and the readout {E, 1 − E} is 𝓛_A's interpretation of the readout instrument. I★
  does not entail it. **FE-ADM does not exclude D-W**: with s_Λ in the controller fields, the
  stepwise D-W meets it by loading the program "apply Λ₁ at each step", so "free evolution" means
  "autonomous Φ with a loaded setting", and FE-ADM is a compatibility assumption, not a sourcing
  test.
- **BF (Born-form agreement), for the Born-form variants only.** Tr(E Φ^{(A,Λ)}_t(ρ)) =
  p_{M*}(E | s_Λ, ρ, t) for every ρ, E, t: the corpus's Born-form representation gives the model's
  operational law (complex kinematics, decision 4, applied to M*).

**Proposition P-ST (#1510; (I); layer X on paper).** Let M* be an I★ witness. (1) Under FE-ADM, M*
satisfies I★_st-coh^op and I★_st-pop^op. (2) Under FE-ADM and BF, M* satisfies I★_st-coh and
I★_st-pop. *Witness for ⇒ (§A.34):* I-4 on π(ρ, Λ_t, E) gives Tr(E Λ_t(ρ)); FE-ADM identifies that
law with p_{M*}(E | s_Λ, ρ, t); Lemma TC gives Λ̂_t = Λ_t; under BF, Lemma TC again gives
Φ^{(A,Λ)}_t = Λ_t. It holds under either typing of s_Λ. No converse is claimed. Imported: FE-ADM;
BF for item 2; J-coh for the coherent variants.

**What fails without each assumption (#1510 §5).**
- Without the T2 indexing, both variants are unsatisfiable for |A| ≥ 2 by every model.
- Without FE-ADM, I★ implies no single-time variant: the stepwise D-W, with no program loaded,
  has the identity as its free family while it meets I★ at trivial E.
- Without BF, I★ implies I★_st-coh^op but not I★_st-coh: by #1508's Lemma S1 ((I), under its
  (a)–(e)), the Born-form channel of a bijection with a fixed countable hidden state is Ad of a
  monomial unitary, so BF and I-4 are jointly unsatisfiable for such models on non-monomial
  targets, and item 2 is vacuous for them.
- An encoding mismatch (Born-form family in the configuration basis, 𝓛_A in a logical basis U) is
  a failure of BF: item 1 is unaffected, and item 2 holds only for the transported target
  Ad_U ∘ Λ_t ∘ Ad_{U†} (#1508 review c.7065957850 CM-2).

**What follows, for the owner's comparison under D6.**
- I★_st-pop compares classical distributions. An L-H′-type count applies with the time t in place
  of the protocol π: if a target population family takes infinitely many distinct values over t,
  a fixed preparation's U-law cannot be finitely supported; if it takes finitely many, finite-atom
  models are not excluded by the count (meeting the target is not shown). D-W-like models meet it.
- I★_st-coh compares coherent channels in the Born form and so presupposes the corpus's Born-form
  representation of the visible sector (complex kinematics, decision 4); its relation to I★ needs
  BF. L-H and L-H′ as stated do not apply, since they use instruments; the all-time periodicity
  obstruction of a fixed finite bijection (Main:650) applies to every finite model at its own
  scope.
- The relation to I★ is P-ST, under FE-ADM and, for the Born-form variants, BF; without those
  assumptions no implication from I★ is claimed. c.7064942473: "Equivalence based on single-time
  observations is weaker than equivalence under arbitrary quantum experiments." Whether any
  variant is satisfiable by a sourced model is not examined here.

## 3. Clause ledger with directional witnesses (§A.34)

For a clause of a target, the two directions are kept apart: **sufficient** = what discharges the
clause, and existing results that discharge it at another scope; **necessary** = what every witness
must satisfy, with the result that forces it. (N) = proved from OI's native assumptions; (I) =
conditional, imported assumptions named. Layers: K Lean kernel on `main`; X exact algebra; P paper;
R research record.

| Clause | Kind | Status | Sufficient direction | Necessary direction | Dependencies |
|---|---|---|---|---|---|
| I★ as a whole | mathematical statement; physical content only through E and I-3 | open | none under a non-trivial E. At trivial E, D-W (§2.2, P, sketch) meets the mathematical clauses. Interface-level route: `substratum_plus_control_qm` (StructuralClosure.lean:397, K) gives exact finite endomorphic QM for the generated theory, assuming `ExtendsSubstratum`, `StructurallyClosed`, `DrivesElementary`; that is a theory, not a model of the EP:73 schema. (I): imports complex matrix kinematics (decision 4), elementary drivability, J-coh | L-H and L-H′ (§4); Main:568 (P, unboundedness imported [55]); the record-capacity node N5 (§4); L-T (§5) | E; I-3 criterion, open (D5); J-coh (D6); H-∞ (`verification/ROADMAP.md`:81) for any completion route |
| (scale) | mathematical (interface typing) | proposed | holds once one model at one carrier is given (EP:33, EP:41; L-T) | none beyond I-1 | EP:33, EP:41, EP:106 |
| I-1 coherence | mathematical | open | D-W at trivial E | EP:67, EP:104, EP:112 | encoding rule |
| I-2★ one construction | mathematical + resource accounting | open | D-W at trivial E | a per-size family fails it by definition; by L-T the per-size loophole is already closed by I-1 at one carrier, so I-2★ adds no satisfiability content on this scope (§2.1) | resource policy (EP:106) |
| I-3 physical sourcing | physical/operational | open; NOT PASSED; no criterion is adopted; two live options, T-SUB′ and T-HTV′ (as a judgment), are put to the owner (§2.2, D5) | none. Earliest assumed mechanism: elementary drivability (continuously tunable state mixing) in a structurally closed class (Main:598; `substratum_plus_control_qm` hypothesis `hd`); native preparation, readout and records (`verification/programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md`:21 and `verification/programmes/oi-qm/reconstruction/meas-q-20261120/RESULT.md`:33 record physical sourcing NOT PASSED) | the monomial class lacks composite control: `substratumGen_not_control` (StructuralClosure.lean:330, K; two-state carrier), `substratumTheory_not_layerFlowExecutable` (LiftAudit.lean:200, K). (N)-type no-gos for the specified monomial implementation class only | E; native coherent operation; native preparation, readout and records |
| I-4 exactness | mathematical | open | D-W at trivial E; none under a non-trivial E. I-ε (Main:574–610, P) is an approximation with supplied quantum data and does not discharge I-4 | L-H′ (infinite U on every exact witness, any carrier, no qubit needed); L-H (with H-PI and J-coh, preparation-independent response classes); Main:568; N5; the all-time periodicity obstruction of a fixed finite bijection with a fixed prior (Main:650, P) at its own autonomous multi-time scope | U-completeness EP:77, isolation EP:79, EP:81–90; H-PI and J-coh only for L-H |
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
  Check, H-PI dropped: the countermodel offered at r5.1, in which ι writes into the controller
  fields a sample of the quantum outcome computed from (p, π, λ), is **not admissible**: fields
  computed from the seed are uncontrolled variables relevant to later outcomes, so EP:77 puts them
  in U, and their dependence on π then violates H-ISO. Check, exactness dropped: I-ε holds with
  finite carriers (Main:574–610). Verdict: H-ISO and exactness are load-bearing; H-PI is not shown
  to be, and N6 shows it is dispensable inside EP's deterministic schema. The assumption-watch
  marker is therefore AW-R5-1: "every exactness obstruction on the schema rests on U-completeness
  (EP:77) and isolation (EP:79)"; it applies to every O3 readout construction.
- **N3. A model that assumes A1.** If a model takes Ω = S finite (A1 assumed for that model, which
  `main` does not do, Sub:92), and H-PI holds, κ takes finitely many values and L-H fails, so such
  a model cannot meet I-4 on a qubit level. Verdict: CONFIRMING. It restates, for response
  classes, what is already on record: Main:568, EP:123, #914 c.6875046763 ("the target cannot
  assume one fixed finite total carrier") and r4 I-4 ("no fixed finite total carrier is assumed",
  r4:208). It is not a dependency of the target on #1477.
- **N4. Does L-H give more than countably many classes?** Check: the proof needs only a countable
  family and yields "infinite". Verdict: no stronger cardinality is claimed.
- **N5. Under a finite Ω, what forces infinity?** Check, single-shot protocols: the seed space Λ
  is separate from Ω in the EP:73 schema and may be infinite, but writing a seed-derived outcome
  sample into a controller field is inadmissible (N2), so this route gives no finite-Ω
  reproduction; N6 settles the single-shot case. Check, the whole of `J_exact(A)`:
  it contains adaptive histories of every finite depth with retained, repeatedly readable records
  (EP:39–40); if the record map R reads the retained record from the configuration at
  termination, distinct histories of depth K need distinct configurations, so |Ω| ≥ 2^K for every
  K and Ω is infinite whether or not H-PI holds. Verdict: an infinite Ω is forced by record
  capacity alone, with no quantum content, under the stated reading of R. This sharpens N1: the
  lemma's own content is the condition on U at a qubit level, not the cardinality of Ω.
- **N6. Is H-PI needed at all? Lemma L-H′.** In the EP:73 schema the history is a deterministic
  function of (λ, π) (EP:97, p_M(h | π, p) = μ_p({λ : H_M(λ, π) = h}), with Φ autonomous and
  reversible). By U-completeness (EP:77) every uncontrolled variable relevant to later outcomes is
  in U; the controller fields are set by the program. So the outcome of a single-shot protocol is a
  function of (u, p, π), and p_M(o | π, p) = ν_p(A_{o,p,π}) for a measurable A_{o,p,π} ⊆ U, with ν_p
  independent of π by H-ISO. **L-H′:** under EP:77, EP:79, EP:97 and I-4, at every carrier
  (including Fin 1) and for every preparation p, ν_p is not finitely supported. *Proof.*
  `J_exact` contains, on any object, the classical-noise instrument {t·id, (1 − t)·id}: it is CP,
  its branches sum to a trace-preserving map, and it gives the first outcome with probability t
  for every t ∈ [0, 1]. If ν_p had N atoms and no other mass, the values ν_p(A) would lie in a set
  of at most 2^N numbers, while I-4 demands every t ∈ [0, 1]. ∎ No qubit, no pure state and no
  coherent intervention is used (c.7065136670 R1). H-ISO is needed: without it each ν_{(p,π)}
  could be a different finite measure. Consequence: every exact witness has U taking infinitely
  many values, so Ω is infinite; with A1 not adopted on `main` this conflicts with nothing. It does
  not discriminate D-W, whose seed tape is non-atomic. Verdict: H-PI is dispensable **for the
  conclusion that U and Ω are infinite**; it is not dispensable for L-H's preparation-independent
  response classes, which are undefined without it. L-H (Hardy form, with H-PI) remains valid at its own hypotheses and gives a
  preparation-independent family of response classes, which L-H′ does not; it is the right form for
  a generalized schema with stochastic responses.

**Outcome.** Gem by the test fixed before the attempt through N1 only: under H-PI, L-H constrains
the observer interface (a preparation-independent infinite family of response classes on a qubit
level), which "Ω is infinite" does not. Classification: CONFIRMING for the infinitude content of
L-H′ (Main:568, EP:123, #1506 review R6), for N3 and for N5 (EP:41 and EP:106 already force
unbounded resources); ELABORATING for N6's observation that H-PI is unnecessary for infinitude;
the load-bearing hypotheses of every exactness obstruction on the schema are U-completeness and
isolation (AW-R5-1). The r5.1 claim that H-PI is load-bearing for infinitude is withdrawn; it
remains load-bearing for L-H.

**L-H and L-H′ in the three questions.** Label **(I)** for both: L-H′ rests on the EP-schema
clauses EP:77, EP:79, EP:97 and exactness only, with no quantum or coherent-intervention content;
L-H adds H-PI and J-coh.
- Established: L-H and L-H′ as stated, at layer P, in this record. The review of `95073878` found
  L-H's proof correct under its hypotheses; the review of `4649d047` (c.7065136670) found L-H′'s
  proof correct and asked for the changes made at r5.3.
- Assumed: for L-H, H-ISO (EP:79), H-PI (a reading of EP:75, EP:79, EP:90), the exact comparator
  law at exact zeros (EP:110) and J-coh (projective measurements in countably many bases). For
  L-H′, U-completeness (EP:77), H-ISO (EP:79), the deterministic history map of the schema (EP:97)
  and the exact comparator law; no H-PI and no J-coh. No quantum assumption on
  the OI side. No Lean statement of it exists on `main`; `classical_exposed_ncard_le`
  (KInfFoundations.lean:947) is a different bound (exposed points of a body in the N-simplex under
  a facet hypothesis) and is not duplicated.
- Missing: for L-H, whether the measurements used lie in the native interface (D6), a decision
  about the target, not mathematics; for both, whether the typed schema states U-completeness and isolation
  formally (c.7065065491 R5 records that the typed `SchemaAdmissible` of #1506 does not yet).

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
- **Interface.** I★ and L-H rely on J-coh (c.7064942473; D6); L-H′ does not.
- **Soundness and Bell.** S⇒, S-A and B⇒ follow c.6891338304 by default (§2.3, D2).

## 7. The three questions, for the record as a whole

1. **Established.** L-H and L-H′ (§4, (I)); L-T (§5, definitional); D-W in its stepwise form
   (§2.2, a sketch at layer P, not a proof, conditional on the typed schema including U-completeness
   and isolation) shows that I★'s mathematical clauses are jointly satisfiable at trivial E. No clause of
   I★ is discharged under a non-trivial E.
2. **Assumed.** For L-H: H-ISO, H-PI, the exact comparator law, J-coh. For L-H′: U-completeness,
   H-ISO, the deterministic history map, the exact comparator law. For every sufficient route
   cited: complex matrix kinematics; elementary drivability (`DrivesElementary`, hypothesis `hd` of
   `substratum_plus_control_qm`); structural closure (`StructurallyClosed`); finiteness of the
   carrier (`[Fintype A]`).
3. **Missing.** The earliest missing step is a decision followed by a physical mechanism. The
   decision is a pass/fail criterion for I-3 and E that is independent of the comparator (D5);
   §2.2 leaves two live options, T-SUB′ and T-HTV′ (as a judgment), and the alternative of
   opening the criterion as a research unit; none is adopted. Without a criterion,
   D-W meets the mathematical clauses and I★ has no content beyond them. The mechanism is a
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
  preparation") is to be a contract requirement. It is dispensable for the conclusion that every
  exact witness has infinite U and Ω (L-H′, N6), and not dispensable for L-H's
  preparation-independent response classes, nor for a schema generalized to stochastic responses.
  The load-bearing contract clauses are U-completeness (EP:77) and isolation (EP:79), which the
  owner may wish to keep as explicit preconditions of every exactness and readout result.
- **D4.** The r4 preservation route (answer 5, or by reference as proposed in §8), the landing of
  r5 after independent review, and the #1428 correction.
- **D5.** The I-3 criterion. §2.2 assesses T-PROC, T-SUB, T-HTV, T-NOQ and T-ACC: T-PROC, T-NOQ
  and T-ACC fail, and T-SUB fails as offered. The options put to the owner, none chosen here:
  (a) adopt T-SUB′ as the I-3 criterion, with observer-access procedures as defined in §2.2 and
  a choice of reading for (iv): under (iv)-explicit, T-SUB′ fails to exclude D-W in a
  computationally universal substratum; under (iv)-recoverable, it excludes D-W but also every
  exact `J_exact` model satisfying PIP (by [PBR], an (I) import), unless PIP is dropped for the
  substratum's independently prepared systems; either way the extension form stays the formal
  target as I★[H], existing sufficient routes yield only I★[H], and H names `hd` (unsourced) and the
  existence of an EP-schema model realizing the generated theory (unconstructed); (b) adopt T-HTV′ provisionally as a judgment
  standard; (c) open the I-3 criterion as a research unit. No option can yet be shown not to exclude
  a legitimate exact model, because none is known. Without a criterion, I★ is met at trivial E by
  D-W.
- **D6.** The interface: I★ over `J_exact` with J-coh named; or one of the single-time variants
  I★_st-coh, I★_st-pop (with their operational forms, related to I★ by P-ST, #1510) defined in §2.4 from `Sub:249` and `familyAt`; or a single-time variant as
  a stage before I★. §2.4 lists what each loses: no instruments, helper levels or records;
  I★_st-pop is a classical comparison that D-W-like models meet and that, for finitely valued
  targets, does not exclude finite-atom models by the count; the homogeneous finite-environment
  comparator form is itself a design choice. Clause (iv) of T-SUB′ bites differently under the two
  arms: under `J_exact`, (iv)-recoverable meets PBR through the entangled measurements on helper
  levels; under I★_st, preparations are laws over visible configurations and there are no
  entangled measurements, so PBR does not apply.
- **D7.** Scalability. Inside `J_exact` the safeguard is nominal (§2.1). SG-1 to SG-3 widen the
  interface (a scope decision, with force against D-W only through E and I-3); SG-4′ is precise but
  presupposes a site structure and is probably unsatisfiable by #1504's Proposition U (as reported
  in the #1506 review c.7065065491 R8; not read here). No
  substantive constraint is proposed; the owner is asked whether to record it as open or to widen
  the interface.

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
| #1506 review R5 (c.7065065491), r5.2 | D-W restated in the stepwise form; the precomputed form recorded as inadmissible; exclusion located in EP:75, EP:47/92 and EP:102 through a nontrivial E naming a procedure class; T-PROC added; finite-information tests noted as insufficient |
| #1510 at `c45b82cf` (c.7066267563), folded under #1169 c.7067233614, r5.7 | §2.4: T1 repaired (P-ST under FE-ADM and BF replaces "strictly weaker"); T2 indexing by a setting typed per EP:79/EP:75; encodings in the definitions, the mismatch a BF failure; FE-ADM's non-exclusion of D-W; D6 cross-reference. No claim broadened; D1–D4 and D7 left open |
| Review c.7065260286, r5.6 | "robustly" removed; the (iv) dilemma stated in §2.2 with both readings, their consequences and the PBR/PIP condition (labelled (I)); completion route noted; §2.2 Result, D5 option (a) and D6 restated; H worded as two hypotheses |
| Final check c.7065233367, r5.5 | n1: H for the existing routes names `hd` and the construction of an EP-schema model; n2: "observer-access procedure" defined for T-SUB′, with the load-bearing clause (iv) and its open redescription question |
| Delta review c.7065208959, r5.4 | blocking item: the D5 bar restated as unmeetable until a legitimate exact model is known; T-SUB′ presented as a live criterion consistent with decision 1, with its cost; §2.2 row and result, §3 I-3 row, §7 item 3 and D5 restated; nits N1–N4 (L-H′ review status, I★_st comparator as a design choice, finite-atom wording, Proposition U caveat in D7) |
| Delta review c.7065136670 R1, r5.3 | L-H′ restated with the noise instrument (any carrier, no qubit, no J-coh); label (I) on EP:77, EP:79, EP:97 and exactness; CONFIRMING; infinite Ω stated as a consequence that conflicts with nothing on `main`; D3 scoped; §3 I-4 row and necessary cells corrected |
| R2–R4, r5.3 | §2.2 table rebuilt: each option assessed as offered and as repaired; T-PROC's dilemma, T-SUB's redescription and completion-route conflict, T-NOQ's failure stated; the I-3 criterion recorded as an open research problem; T-PROC added to D5 |
| R5, r5.3 | §2.1: SG-1 to SG-3 recorded as interface widenings; SG-4 given native units as SG-4′, recorded with its #1504 conflict; substantive scalability recorded as open |
| R6, r5.3 | §2.4 defines I★_st-coh and I★_st-pop from `Sub:249` and `familyAt`, with what each loses |
| Self-correction, r5.2 | N2's H-PI-dropped countermodel violates U-completeness; N5 corrected; N6 adds L-H′ (no H-PI); D3 restated |
| Nits | L-T labelled definitional; per-result three-question lines for L-H and L-T; "preregistered" replaced by "fixed before the attempt"; "observer-resolvable" replaced by an instrument-family condition compatible with finite access per instrument; H-PI reworded to the controller-field form |

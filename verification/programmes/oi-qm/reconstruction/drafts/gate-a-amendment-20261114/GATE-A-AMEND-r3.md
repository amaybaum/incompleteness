# Gate A forward amendment: the three-part target (r3)

Paper-only planning record for #1169. It amends the model-level target of the accepted Gate A
contract forward and leaves that record's text unchanged. It proves no result, adopts no extension
E and no sector condition C, and changes no scientific status (§A.45 rule 1). r3 answers
`REVIEW-r1.md` and `CONFIRM-r2.md`; dispositions are in `RESPONSE-r1.md`; the line trace of the
contract, the dependent statements and the status table of existing results are in
`GATE-A-AMEND-r3-TRACE.md`; the owner questions in plain language are in `OWNER-QUESTIONS-r3.md`.
Not merged.

## 1. Pins and authority

**Contract amended.** `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`,
blob `d9d92e038a8022e854586101067ce4de9789fdf6`, read on `main` at
`c3b5f37a354bb26437e2e0165c576a347a63c153`. The same blob is at `fdc3dd7f7356dc8f83693f1a2bd8b3a12d24b051`
(the head accepted as Gate A, #1169 comment 6686258585) and at `9d24914c5006d775315189dadf56769e1e9cc847`
(the commit the #1169 body links as "The accepted Gate A contract"); it reached `main` in
`dc0b333a1aaee5780d4f3dc514d92337c2c53307` (merge of #1173). `EP:n` below is line n of that blob.

**Owner records implemented.** All three were posted from the owner's account `amaybaum`.

- #914 comment 6875046763, 2026-11-14T09:14:01Z. Owner statement quoted there: "I adopt all five
  decisions and the target theorem; preserve r3 now". The requirements of this comment that stand
  are those listed in #914 c.6875548603: "The other requirements of comment 6875046763 stand: an
  independently physically justified extension E; a compatible model and interface for all parts,
  not constructions chosen per experiment; no assumption of one fixed finite total carrier; the
  configuration-level no-go not read as covering every observer interface; exact as the ultimate
  target; Bell as a separate track that the full result requires." From c.6875046763 itself: "The
  two directions must use a compatible model and operational interface, not unrelated
  constructions selected separately for each experiment." and "Finite access by an embedded
  observer must remain distinct from finiteness of the underlying dynamics."
- #914 comment 6875548603, 2026-11-14T09:56:47Z. Owner statements quoted there: "To be more precise,
  OI should actually be a superset of QM.  OI should include QM and GR." and "Yes proceed as
  suggested." It replaces the two-way sentence by Inclusion ("QM_fin ⟹ OI + E on one common
  substratum–observer realization. Required."), Sector ("For a stated, physically justified
  condition C: within OI + E, the experiment families satisfying C are exactly those of QM_fin …
  (C ⟹ quantum) and (quantum ⟹ C)") and Gravity ("The same substratum and observer yield general
  relativity, consistently with the two parts above"), with "Not required. That every OI model
  behaves quantum-mechanically."
- #1169 comment 6875724719, 2026-11-14T10:12:11Z. It records that the owner "replied **"I
  approve"**" in the coordinating conversation, authorizing "the *paper-only* forward amendment".
  Binding clauses: "Preserve without relaxation: Gate A's exact J_exact(A) operational interface:
  every preparation/instrument, finite adaptive history, retained accessible records,
  causal-prefix/setting independence, coherent composition, resource accounting and exactness
  versus approximation. Identify precisely which former **class-wide** two-way obligations are
  superseded; do not falsely retire the two directions **within C**." "Not authorized: merging,
  experimental/simulation/Lean execution, adopting E or C as a physical premise, scientific status
  promotion, changing board priorities or initiating QB5(a)." "Physical source remains **NOT
  PASSED**."

**References off `main` (§A.42 item 8).** The three comments above: provenance for authority. The
obligations of §5 are defined from #914 c.6875548603 as planning content; that is their only use.
#1169 c.6703342848 is quoted for an explanation the owner approved (§3.2). Branch
`records/target-theorem-914-20261114` at `755f9bffb904635f2c512a42a4dfa88f8591a6b1`
(`TARGET-THEOREM-r3.md`, `README.md`): provenance; its rows T5b ⇒ and T5b ⇐ cite EP:53–59 and
EP:61–64, which this record reads directly, and its line 34 is cited in R2 as a reading. Issue
texts quoted in §4.2 and §6.2: provenance, quoted to identify dependent statements, not as support.

**Tags.** [K] Lean statement on `main`, read with its hypotheses, not rebuilt. [P] manuscript proof.
[R] research record on `main`. [I] Issue text.

## 2. Notation

As in EP: A a nonempty finite carrier; `J_exact(A)` the interface of EP:33–41; `Q_exact(A)` the
quantum class of EP:43 and EP:110; `M(E, J)` the admitted candidate class of EP:102; `p_X(h | π, p)`
the history law of EP:49, EP:97 and EP:110. Write **M ≡ T** for "p_M(h | π, p) = p_T(h | π, p) for
every preparation p, protocol π and history h in `J_exact(A)`" (EP:58, EP:63), conditionals
compared only on histories of positive probability (EP:49).

**𝔄**, the common substratum–observer architecture: the fixed extension E, the substratum data
(Ω, Φ) and the observer-interface rules (Λ, μ, ι, R, τ, label interpretation, resource policy) of
the EP:73 schema, given as one rule for every nonempty finite A, together with its parameter map
(I-2).

## 3. What is kept unchanged

**Residual clause.** Every line of EP not listed in §4.1 as superseded or partly superseded stays
in force unchanged, whether or not it is listed below. `GATE-A-AMEND-r3-TRACE.md` assigns each of
the 113 nonblank lines of EP a disposition; the table below traces the operational requirements and
does not narrow EP.

**Scope of application.** Every requirement below applies to I, S⇒, S-A and S⇐ (§5.1–5.2). For S-J, B
and part 3, which lie outside `J_exact(A)`, the requirements bind the shared architecture 𝔄, and
an interface for those parts carries the same requirements when it is typed.

### 3.1 Requirements of the contract

| Requirement | EP |
| --- | --- |
| Kernel scope: complex kinematics given; structure fields not derived from bare OI; native interpretation of every field an obligation; interface data existence and realization separate obligations; the characterization is not a construction of native models | 21–29 |
| The exact interface `J_exact(A)`: objects A and B_n = A × Fin n, fixed join reindexing | 33 |
| Every density preparation, full complex parameter domain | 37 |
| Every finite-outcome endomorphic CP instrument, full parameter domain, no gate or measurement menu | 38 |
| Finite adaptive histories: trees of every finite depth and branching, no maximum horizon | 39 |
| Retained accessible records: append, retain, repeated read without change, conditioning, relabelling and coarse-graining; compatible finite record/controller resources for every protocol | 40 |
| Helper attachment at every positive level, spectators, discard; dimension-changing maps excluded unless typed separately | 41 |
| No narrowing of preparation availability, menu or horizon under the name `J_exact(A)`; a smaller target is named as restricted | 43 |
| Labels are requests, not postulated native realizations; constructing the native procedure and fixed label interpretation is part of the correspondence | 43 |
| Trace rule is the comparator's definition, not a native postulate; exactness has no preassigned finite menu, horizon bound or ancilla cutoff | 45 |
| Labels interpreted by allowed physical procedures; probability tables are not a realization; `RealizesSealedOICore` not identified with the native admissible class | 47 |
| Native record law separately specified | 49 |
| One fixed, independently specified extension E | 54 |
| Coherent single model: witnesses and label interpretations cover the whole `J_exact(A)` family, not chosen per outcome, setting or experiment; composition and conditioning preserved | 67, 112 |
| Candidate data and admissibility schema | 73 |
| Seed law fixed for the preparation, not chosen to fit settings or outputs; U includes every uncontrolled component, cannot be empty or discard a hidden correlation; no global product decomposition of Ω inferred | 75–77 |
| Loading changes only the specified controller fields; restriction to U unchanged until the declared interaction; held preparation, ready state and public records preserved; differing fields isolated | 79 |
| Setting independence on the loaded physical law, `Law(U, S | p, retained past) = Law(U | p, retained past) × Law(S | p, retained past)` | 81–88 |
| Causal-prefix compatibility | 90 |
| Settings act through specified couplings; records realized by the dynamics; a product factorization or causal/locality structure used by a candidate is stated as a hypothesis | 92 |
| Native history law and fixed model data | 94–100 |
| Admission independent of equality to the comparator; nonemptiness an obligation | 102 |
| J declared before laws are compared; availability gaps not hidden by intersecting experiments; typed labels and composites preserved; equality is operational equivalence, not a bijection of ontic configurations with density matrices | 104 |
| Resource accounting: records, controller, preparation cost, observation times, ancilla supply; no per-experiment enlargement | 106 |
| Comparator law: trace of the sequentially composed branches applied to ρ_p; availability exactly `J_exact(A)`; changes of system type need an explicit implementation/transport argument | 110 |
| Native law and comparator law independently defined until a reconstruction proves agreement | 112 |
| Exact primary target versus separate approximation target; no silent fixed finite carrier; no retrospective replacement | 116–123 |
| Category crosswalk and hypothesis ledger | 129–162 |
| A posited Hilbert kinematics, unitary control or native Born law is disclosed with its limited explanatory content; "The native model reproduces all QM" is not an admissible premise | 164 |
| The kernel theorem is reused only at its nonempty-carrier, endomorphic-operation and given-kinematics scope | 172, 177 |
| Completion adopts no premise; later units separately authorized | 175 |
| Research acceptance criterion | 179 |

### 3.2 Requirements of the owner records

| Owner-record requirement | Source |
| --- | --- |
| No fixed finite total carrier assumed; finite observer access distinct from finiteness of the dynamics | #914 c.6875046763, c.6875548603 |
| The configuration-level no-go not read as covering every observer interface | #914 c.6875046763, c.6875548603 |
| One compatible model and interface for all parts | #914 c.6875548603 |
| Exact as the ultimate target; Bell as a separate track that the full result requires | #914 c.6875548603 |
| Hidden machinery need not be quantum (the explanation the owner approved: "We do not need the hidden machinery itself to be quantum"); deterministic hidden dynamics admissible (the comment's statement) | #1169 c.6703342848 (2026-11-07T06:25:11Z) |

## 4. What is superseded

### 4.1 In the contract

**(a) The class-wide forward direction**, EP:56–59:

> For every M in M(E, J_exact(A)),
>   there exists one T in Q_exact(A) such that
>   p_M(h | π, p) = p_T(h | π, p)
>   for every preparation p, protocol π and history h in J_exact(A).

Replaced by **S⇒** (§5.2): the same statement restricted to members satisfying C. Members of
`M(E, J_exact(A))` outside the sector carry no law-equality obligation. EP:51 is superseded only in
naming the display EP:53–64 as the primary proposed model-level target: the primary model-level
target is §5, of which EP:54 and EP:61–64 remain components; EP:69, EP:112 and EP:120, which refer
back to that display, apply to each direction §5 requires.

**(b) The forward half of ledger row 11**, EP:157: "A consistent whole-process realization and
reverse model coverage … Construct both witness maps and check all histories/compositions in
scope." The forward witness map is required on the sector only; the reverse coverage and the
whole-process realization stand. EP:170 records a completed Gate A deliverable and is not edited;
under this amendment the whole-model obligations are I, S⇒, S-A, S⇐, S-J, B and G, each stated
separately.

**Not superseded.** The reverse direction EP:61–64 is kept and strengthened by part 1. The forward
direction is kept inside C. EP:102, EP:104 and EP:164 apply to C as well as to E (§5.2). Nothing
else in EP is superseded (residual clause, §3).

### 4.2 Dependent statements outside the contract (identified, not edited)

Fourteen entries restate a class-wide forward obligation or a class-wide exclusion of
nonquantum behaviour; they are quoted with sources in `GATE-A-AMEND-r3-TRACE.md` §2 (#1169 body and
c.6703342848, c.6763928950; #1143 body; six entries from five records under `verification/programmes/oi-qm/`). Under
this amendment each reads as its sector form (S⇒ and S-A on the sector, nonquantum exclusion in
the physical sector), and verdicts they record stand at their own scope. The list comes from a search
of `oi-qm/` records and of #1169, #1143 and #914, not a proof that no other restatement exists.
Whether `PROGRAMME.md` F2 (PG:531–537, principles "necessary and sufficient for QM") is to be read
against the amended target is not decided here; F3 (PG:539–543, "OI admits a larger theory space …
identifies the QM subclass") has the shape of part 2, and #1143 holds the selection question.

## 5. The amended model-level target

Fixed throughout: the extension E of EP:54 and one architecture 𝔄 (§2). Every obligation is open.
None is proved here.

### 5.1 Part 1: quantum inclusion

**I.** For every nonempty finite A and every T in `Q_exact(A)` there exists one M_{A,T} in
`M(E, J_exact(A))`, an instance of 𝔄, with M_{A,T} ≡ T.

- **I-1, one model per comparison.** M_{A,T} covers every p, π and h of `J_exact(A)` (EP:67, EP:112).
- **I-2, one architecture.** Φ, the observer-interface rules, the loading map ι, the record maps R
  and τ, the label interpretation and the resource policy are those of 𝔄. Dependence on A or T
  enters only through a parameter map that is part of 𝔄, fixed before any law is compared, and
  computed from the typed data of A and of the requested labels, never from the values of p_T; no
  model is fitted to p_T, and none is constructed separately per protocol (EP:100, EP:102; #914
  c.6875046763).
- **I-3, physical sourcing.** E is independently physically justified. Each clause of 𝔄 carries
  its source status in the EP §4.2 ledger; an inclusion using an unsourced or posited clause is a
  conditional inclusion and carries that clause as a named hypothesis. A conditional inclusion is
  a conditional result; it does not discharge I.
- **I-4, exactness.** Exact law-equality (EP:120); the approximation target stays separate (EP:121);
  any completion or carrier enlargement is declared (EP:123), and no fixed finite total carrier is
  assumed (§3.2).
- **Witness.** A construction of M_{A,T} under I-1 to I-4 and a proof of M_{A,T} ≡ T. EP:61–64 is
  I without the clauses I-2 and I-3.
- **Scope.** I over `J_exact(A)` is the Gate A form of part 1. Finite quantum experiments outside
  it (changes of system type, EP:41 and EP:110; spatially separated multi-wing protocols, B in
  §5.2) are not covered by I and are named as the remainder of part 1, open; each needs a typed
  interface carrying the requirements of §3 before its inclusion is stated. This amendment does
  not type those interfaces.

### 5.2 Part 2: quantum-sector equivalence

**Type of C.** C is a declared predicate whose type is stated with it. Write `M_C(E, A)` for the
members of `M(E, J_exact(A))` satisfying C. The admissible types are C-law and C-model; which one
the target uses is undetermined pending owner decision (§7, R1):

| Type | C is a predicate on | What it commits to |
| --- | --- | --- |
| C-law | the history law p_M over `J_exact(A)` | matches "the experiment families satisfying C" (#914 c.6875548603); S⇐ᴺ then follows from S⇐; C must be a law-level condition stated without reference to `Q_exact(A)` (C-1), and its agreement with the quantum class on OI + E is a theorem to be proved, not a definition |
| C-model | native data (Ω, Φ, Λ, μ, ι, R, τ, E) of M, or a part of them (the substratum law, the realization distribution, the observer embedding, admissible preparations or readouts, or tuples of these, as listed in #1143) | matches "OI models outside C" (#1169 c.6875724719); S⇐ᴺ is a separate, stronger claim |
| C-regime | a model together with a restricted family of its procedures or configurations | not a separate type: admissible only when stated as a predicate of type C-law or C-model, and then subject to C-4; a restriction of the procedures compared is not an admissible C, and a sector result over such a restriction is a named restricted target (EP:43) that does not discharge S⇒, S-A or S⇐ over `J_exact(A)` |

**Admissibility of a sector condition.** A condition C is admissible only if:

- **C-1, independent statement.** C is stated in terms of its declared type before any law is
  compared. It is not defined by law-equality with a member of `Q_exact(A)`, not equivalent to it
  by definition, and not a list of the protocols on which a model matches (the condition EP:102
  places on E, and EP:164). C is not defined by membership in the set of models constructed for I,
  by an enumeration of models or experiment families, or with any parameter, threshold or list
  whose value is fixed by comparison with p_T or with any member of `Q_exact(A)`. If C is stated on
  history laws, it is stated without reference to `Q_exact(A)`, and its equivalence to the quantum
  class, if any, is a theorem to be proved, not a definition.
- **C-2, physical justification.** C is justified independently of the agreement it is used to
  obtain; the confinement obligation is S-J.
- **C-3, hard to vary (§A.29).** C states in advance the existing results it preserves, delivers
  at least one independent prediction or postdiction beyond the sector equivalence, and is rejected
  if it can be adjusted to fit any outcome.
- **C-4, no narrowing of the interface.** C does not remove procedures from `J_exact(A)`. A member
  of `M_C(E, A)` lacking a preparation, instrument, record operation or composite procedure of
  `J_exact(A)` has an availability gap (EP:43, EP:104).
- **C-5, nonvacuity.** Nonemptiness of `M_C(E, A)` is an obligation (EP:102), discharged by S⇐;
  S⇒ and S-A over an empty sector establish nothing.

No condition C is proposed here. Adopting one is a new premise under §A.29 and needs its own owner
authorization.

**S⇒ (soundness; C ⟹ quantum).** For every nonempty finite A and every M in `M(E, J_exact(A))`
with C(M), there exists one T in `Q_exact(A)` such that M ≡ T, with M's own fixed label
interpretation (EP:47) covering every p, π and h of `J_exact(A)` and preserving sequential and
outcome-dependent composition, conditioning and the declared spectator and composite operations
(EP:67, EP:104, EP:112). Witness: a proof quantified over every such M; a proof over a subclass, a
protocol menu or a bounded horizon does not discharge it.

**S-A (access closure; with S⇒, the direction C ⟹ quantum on complete experiment families).** For
every nonempty finite A and every M in `M(E, J_exact(A))` with C(M), every finite adaptive protocol
that M's admissible physical preparation, intervention and record procedures (EP:47, EP:75) can
carry out on the objects of `J_exact(A)` has, with its complete accessible record history, the
history law of some protocol of `J_exact(A)` under M's fixed label interpretation, up to
relabelling of outcomes. Witness: a proof over every such M and every such protocol. S⇒ alone
compares only label-interpreted protocols; S⇒ with S-A gives that the complete experiment family
of each sector member is that of one member of `Q_exact(A)`. Source: #914 c.6875548603 ("the
experiment families satisfying C are exactly those of QM_fin"; "excluding stronger-than-quantum
correlations in the physical sector") and the statements of §4.2 that require accounting for every
admitted operation. EP has no counterpart (R5); whether the target includes S-A is owner question 4
(§8).

**S⇐ (coverage; quantum ⟹ C).** For every nonempty finite A and every T in `Q_exact(A)`, there
exists one M in `M(E, J_exact(A))`, an instance of 𝔄 meeting I-1 to I-4, such that C(M) and
M ≡ T, with one fixed label interpretation covering every p, π and h of `J_exact(A)` and preserving
the same composition, conditioning and composite structure (EP:67, EP:104, EP:112). Witness: for
each T, a construction of such an M with proofs of C(M) and of M ≡ T. S⇐ implies I. S⇒ and S⇐
together give that the `J_exact(A)` history laws of members of `M_C(E, A)` are exactly those of
`Q_exact(A)`; with S-A this is the set equality of #914 c.6875548603 on complete experiment
families. The coverage form is the reading the owner record supports (§7, R1).

**S⇐ᴺ (necessity; an option, not adopted).** For every nonempty finite A and every M in
`M(E, J_exact(A))`, if M ≡ T for some T in `Q_exact(A)`, then C(M). It is not stated in the owner
records, which state the sector on experiment families. With I it implies S⇐. If C is a function
of the history law, S⇐ implies S⇐ᴺ. Otherwise S⇐ᴺ is a further claim about every admitted
realization of quantum behaviour, including distinct models with identical histories, and it
needs its own theorem showing that no admitted model outside the sector reproduces a member of
`Q_exact(A)`. It is a distinct question only if C depends on data beyond the history law. Whether
S⇐ᴺ is part of the target is undetermined pending owner decision (§7, R1).

**S-J (confinement).** A physical justification that observation is confined to `M_C(E, A)` (#914
c.6875548603). It is separate from S⇒, S-A, S⇐ and S⇐ᴺ, is not implied by them, and is required under
every reading.

**B (Bell track; decision 3 of #914 c.6875046763, "Separate research track, mandatory for full
equivalence").** `J_Bell(A₁, A₂)` is a two-wing interface still to be typed. It extends
`J_exact(A₁ × A₂)`, states its locality and setting-independence hypotheses (EP:81–92), and contains
every two-wing protocol that a model's admissible physical procedures (EP:47, EP:75) can carry out,
not only quantum-labelled requests. `M(E, J_Bell(A₁, A₂))` is defined as at EP:102 with
J = `J_Bell(A₁, A₂)`, and a member satisfies C when its restriction to `J_exact(A₁ × A₂)` does.

- **B⇐ (coverage).** For all nonempty finite A₁, A₂ and every T in `Q_exact(A₁ × A₂)`, there exists
  an S⇐ witness M for T whose extension to `J_Bell(A₁, A₂)`, with the same fixed label
  interpretation and meeting I-1 to I-4, reproduces exactly T's law for every quantum two-wing
  protocol and preparation on the quantum-labelled part of `J_Bell(A₁, A₂)`.
- **B⇒ (soundness).** For all nonempty finite A₁, A₂ and every M in `M(E, J_Bell(A₁, A₂))`
  satisfying C, no protocol of `J_Bell(A₁, A₂)` yields correlations outside the quantum set.

Both are required in the physical sector, not in all of OI + E (#914 c.6875548603). `J_Bell` is not
part of `J_exact(A)` as defined at EP:33–41, and this amendment does not type it.

**Permitted.** A member of `M(E, J_exact(A))` outside `M_C(E, A)` need not match any member of
`Q_exact(A)`.

### 5.3 Part 3: gravity compatibility

- **G-1, same architecture.** General relativity is obtained from the substratum and observer of
  the 𝔄 used in parts 1 and 2, not from a second substratum or observer.
- **G-2, consistency.** No hypothesis used for G-1 contradicts E, C or a clause of I, S⇒, S-A, S⇐, S-J
  or B; the regime in which G-1 holds is stated together with the scope of C.
- **G-3, open targets.** The covariant field equations: "The present derivation uses the Einstein
  equations through Jacobson's relation (§3.1) and does not derive them; the covariant field
  equations remain the Level-G3 target (§8.7)" (`papers/GR.md`:162). The G3 matter-coupling and
  source question: #873. Both stay open.

Gate A supplies no part of G: `J_exact(A)` has no spacetime, metric or gravitational observable.
The owner record states part 3 as an inclusion ("GR ⊆ OI"); no two-way form is stated, and none is
added.

## 6. Crosswalk

### 6.1 Obligations of the accepted contract

`GATE-A-AMEND-r3-TRACE.md` §1 gives each of the 113 nonblank lines of EP its disposition; §4.1
lists every line that is superseded or partly superseded, and §3.1 the operational requirements kept.

### 6.2 Existing results bearing on each part

The status table is `GATE-A-AMEND-r3-TRACE.md` §3. Each status is that of its source: the Lean
characterizations are interface-level with complex kinematics taken as given; the ε-realizations
of `papers/Main.md`:596 are an approximation target, not I; the classical-dimension obstruction
(:558) is scoped to the preparation → finite ontic system → measurement interface; `papers/Main.md`:598
states that the finite deterministic class is strictly larger than the quantum class; no result
supplies E, C, S-A, S-J, B or G.

## 7. Points where the accepted contract and the new target do not fit directly

- **R1, the type of C and the reverse sector direction.** #914 c.6875548603 states the sector on
  experiment families ("the experiment families satisfying C are exactly those of QM_fin"), whose
  ⊇ half is the coverage form S⇐; the record supports that reading. #1169 c.6875724719 speaks of
  "OI models outside C". If C is a function of the history law, S⇐ implies S⇐ᴺ and the two forms
  coincide; if C depends on native data beyond the history law, S⇐ᴺ is a separate, stronger claim.
  The owner question is the type of C (§5.2), and with it whether S⇐ᴺ is required; S⇐ is required
  under every answer.
- **R2, scope of "one common architecture".** EP:54 fixes E "For each nonempty finite A". #914
  c.6875548603's proposal reads "every finite quantum experiment is realized by one common OI
  model", and #1169 c.6875724719 reads "one common, physically sourced substratum–observer
  architecture". I as stated (one 𝔄, one instance per (A, T)) is the architecture reading; the
  single-model reading (one model serving every A) is stronger and is undetermined pending owner
  decision. Reading, not a definition: EP:43 and EP:110 give `Q_exact(A)` the standard trace law
  over the whole interface, nothing in EP indexes several members, and `TARGET-THEOREM-r3.md`:34
  reads it as Q_op with the full interface; "for every T" is then at most a quantification over
  label conventions.
- **R3, E versus C, and confinement.** Under EP a condition folded into E restricts the admitted
  class itself; a C with S⇒ and S⇐ folded into E as E ∧ C would meet EP:56–64. The new target keeps
  C separate and adds S-J. EP has no notion of confinement: every member of `M(E, J)` realizes every
  protocol of J (EP:102). What it means physically for a non-sector member to exist while
  observation is confined to the sector is not stated in any record read.
- **R4, earlier verdicts against the forward direction.** The E-AR verdict ("refuted under E-AR",
  `whole-model-bridge.md`:242) concerns the forward correspondence for that candidate (:254) at its
  scope and stands as recorded. Reading (not a result of that record): for any C, it obstructs S⇒
  for every sector member that retains the point-preparation/sign subinterface at a fixed
  finite-dimensional prepared object with preparation-independent test labels
  (`whole-model-bridge.md`:238–240, :247–248); C-4 bars removing that read by definition, so the
  amendment does not reopen the E-AR verdict.
- **R5, nonquantum exclusion.** The statements in §4.2 require excluding nonquantum behaviour for
  every operation the interface admits; under part 2 that exclusion is required in the sector: on
  labelled protocols by S⇒, on every admissible procedure of a sector member by S-A, and on
  two-wing protocols by B⇒. EP itself constrains only label-interpreted protocols (EP:47, EP:102),
  so S-A has no counterpart in the accepted contract.
- **R6, gravity.** Part 3 has no interface in Gate A; its obligations are on 𝔄 and are tracked
  outside the endomorphic comparison.
- **R7, R8.** The owner records quantify over "every finite quantum experiment", I over
  `J_exact(A)` (remainder named in §5.1, Scope); a C defined by the models built for I would make
  S⇒ and S⇐ hold by construction, which C-1 excludes.

## 8. Owner questions carried

1. The type of C. C-law commits to a condition on history laws over `J_exact(A)` stated without
   reference to `Q_exact(A)`, under which S⇐ᴺ follows from S⇐; C-model commits to a condition on
   native data, under which S⇐ᴺ is a separate claim. A regime-formulated condition is admitted
   only as one of these (§5.2).
2. Whether S⇐ᴺ is part of the target; a distinct question only under C-model. Including it
   commits to a theorem that no admitted model outside the sector reproduces any member of
   `Q_exact(A)`; excluding it permits such models.
3. "One common": the architecture reading commits to I as stated (one 𝔄 with a fixed parameter
   map, one instance per (A, T)); the single-model reading commits to one model whose subsystems
   realize every carrier A, one E for every A, typed subsystem embeddings, and each per-A
   comparison as a restriction of that model.
4. Whether the sector's experiment family is every admissible procedure of a sector member (S-A,
   the reading of "experiment families" taken here) or only the label-interpreted protocols of
   `J_exact(A)`; the second commits to a restricted reading under which nonquantum behaviour of
   unlabelled procedures in the sector is permitted, and would be named as such. Bearing on it:
   #1169 c.6703342848 records that the owner approved proceeding after the explanation that
   "success means the same predictions across the complete agreed experimental interface"; the
   same comment states, in its author's words, "a quantum counterpart for every behavior admitted
   by the physical OI interface".

## 9. What this amendment does not do

- It proves nothing: I, S⇒, S-A, S⇐, S⇐ᴺ, S-J, B and G are open, and no member of any class named is
  exhibited. It adopts no extension E and no condition C, and proposes no C.
- It changes no scientific status and promotes no claim; physical source is not passed. It types
  no interface beyond `J_exact(A)`: the remainder of part 1, `J_Bell` and part 3 stay untyped.
- It does not edit `endpoints.md`, `TARGET-THEOREM-r3.md`, `whole-model-bridge.md`, `PROGRAMME.md`
  or any Issue. It authorizes no merge, integration, execution, simulation, Lean change, manuscript
  change, board change or QB5(a) start; integration needs independent non-author review first and
  its own owner authorization.

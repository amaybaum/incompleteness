# Gate A forward amendment: the three-part target (r1)

Paper-only planning record for #1169. It amends the model-level target of the accepted Gate A
contract forward, leaving that record's text unchanged. It proves no result, adopts no extension E
and no sector condition C, and changes no scientific status (§A.45 rule 1). Draft for separate
non-author review; not reviewed, not merged.

## 1. Pins and authority

**Contract amended.** `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`,
blob `d9d92e038a8022e854586101067ce4de9789fdf6`, read on `main` at
`c3b5f37a354bb26437e2e0165c576a347a63c153`. The same blob is at `fdc3dd7f7356dc8f83693f1a2bd8b3a12d24b051`
(the head accepted as Gate A, #1169 comment 6686258585) and at `9d24914c5006d775315189dadf56769e1e9cc847`
(the commit the #1169 body links as "The accepted Gate A contract"); it reached `main` in
`dc0b333a1aaee5780d4f3dc514d92337c2c53307` (merge of #1173). `EP:n` below is line n of that blob.

**Owner records implemented.** All three were posted from the owner's account `amaybaum`.

- #914 comment 6875046763, 2026-11-14T09:14:01Z. Owner statement quoted there: "I adopt all five
  decisions and the target theorem; preserve r3 now". The requirements kept from it include "an
  independently physically justified extension of OI and a single common substratum–observer
  realization" and "The two directions must use a compatible model and operational interface, not
  unrelated constructions selected separately for each experiment."
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

**References off `main` (§A.42 item 8).** The three comments above: provenance for authority only;
no scientific statement here rests on them. Branch `records/target-theorem-914-20261114` at
`755f9bffb904635f2c512a42a4dfa88f8591a6b1` (`TARGET-THEOREM-r3.md`, `README.md`): provenance; its
rows T5b ⇒ and T5b ⇐ cite EP:53–59 and EP:61–64, which this record reads directly. Issue texts
quoted in §4.2: provenance, quoted to identify dependent statements, not as support.

**Tags.** [K] Lean statement on `main`, read with its hypotheses, not rebuilt. [P] manuscript proof.
[R] research record on `main`. [I] Issue text.

## 2. Notation

As in EP: A a nonempty finite carrier; `J_exact(A)` the interface of EP:33–41; `Q_exact(A)` the
quantum class of EP:43; `M(E, J)` the admitted candidate class of EP:102; `p_X(h | π, p)` the history
law of EP:49, EP:97 and EP:110. Write **M ≡ T** for "p_M(h | π, p) = p_T(h | π, p) for every
preparation p, protocol π and history h in `J_exact(A)`" (EP:58, EP:63), conditionals compared only
on histories of positive probability (EP:49).

**𝔄**, the common substratum–observer architecture: the fixed extension E, the substratum data
(Ω, Φ) and the observer-interface rules (Λ, μ, ι, R, τ, label interpretation, resource policy) of
the EP:73 schema, given as one rule for every nonempty finite A.

## 3. What is kept unchanged

Every requirement below survives without relaxation and applies to every part of §5.

| Requirement | EP |
| --- | --- |
| The exact interface `J_exact(A)`: objects A and B_n = A × Fin n, fixed join reindexing | 33 |
| Every density preparation, full complex parameter domain | 37 |
| Every finite-outcome endomorphic CP instrument, full parameter domain, no gate or measurement menu | 38 |
| Finite adaptive histories: trees of every finite depth and branching, no maximum horizon | 39 |
| Retained accessible records: append, retain, repeated read without change, conditioning, coarse-graining | 40 |
| Helper attachment at every positive level, spectators, discard; dimension-changing maps excluded unless typed separately | 41 |
| No narrowing of preparation availability, menu or horizon under the name `J_exact(A)`; a smaller target is named as restricted | 43 |
| Trace rule is the comparator's definition, not a native postulate | 45 |
| Labels interpreted by allowed physical procedures; probability tables are not a realization | 47 |
| Native record law separately specified | 49 |
| One fixed, independently specified extension E | 54 |
| Coherent single model: witnesses and label interpretations cover the whole `J_exact(A)` family, not chosen per outcome, setting or experiment; composition and conditioning preserved | 67, 112 |
| Candidate data and admissibility schema | 73–77 |
| Setting independence on the loaded physical law, `Law(U, S | p, retained past) = Law(U | p, retained past) × Law(S | p, retained past)` | 79–88 |
| Causal-prefix compatibility | 90 |
| Settings act through specified couplings; records realized by the dynamics | 92 |
| Native history law and fixed model data | 94–100 |
| Admission independent of equality to the comparator; nonemptiness an obligation | 102 |
| Availability gaps not hidden by intersecting experiments; typed labels and composites preserved | 104 |
| Resource accounting: records, controller, preparation cost, observation times, ancilla supply; no per-experiment enlargement | 106 |
| Exact primary target versus separate approximation target; no silent fixed finite carrier; no retrospective replacement | 116–123 |
| Category crosswalk and hypothesis ledger | 129–164 |
| "The native model reproduces all QM" is not an admissible premise | 164 |
| Completion adopts no premise; later units separately authorized | 175 |
| Research acceptance criterion | 179 |

## 4. What is superseded

### 4.1 In the contract

**(a) The class-wide forward direction**, EP:56–59:

> For every M in M(E, J_exact(A)),
>   there exists one T in Q_exact(A) such that
>   p_M(h | π, p) = p_T(h | π, p)
>   for every preparation p, protocol π and history h in J_exact(A).

Replaced by **S⇒** (§5.2): the same statement with `M(E, J_exact(A))` replaced by the sector
`M_C(E, A)`. Members of `M(E, J_exact(A))` outside the sector carry no law-equality obligation.

**(b) Its occurrences in the ledger and unit plan, in their forward half only.** EP:157 (ledger
row 11): "A consistent whole-process realization and reverse model coverage … Construct both
witness maps and check all histories/compositions in scope." The forward witness map is required on
`M_C(E, A)` only; the reverse coverage and the whole-process realization stand. EP:170: "both
whole-model obligations stated separately" is replaced by the obligations I, S⇒, S⇐ and G of §5,
each stated separately.

**Not superseded.** The reverse direction EP:61–64 is kept and strengthened by part 1. The forward
direction is kept inside C. EP:102, EP:104 and EP:164 apply to C as well as to E (§5.2).

### 4.2 Dependent statements outside the contract (identified, not edited)

These restate the class-wide forward obligation; under this amendment each reads as its sector form.

| Source | Statement |
| --- | --- |
| #1169 body, Operational success criterion [I] | "Both directions matter: cover the quantum target and account for every operation the proposed physical OI interface admits." |
| #1169 body, Purpose item 2 [I] | "extended OI and the selected QM target are operationally equivalent in both directions" |
| #1169 body, Gate C [I] | "Prove soundness (each extended-OI realization predicts the targeted QM operational law)" |
| #1169 comment 6703342848 [I] | "It requires both target coverage and a quantum counterpart for every behavior admitted by the physical OI interface." |
| #1169 comment 6703342848 and body [I] | "a proposed interface must both permit quantum Bell behavior and exclude nonquantum behavior" (comment); the body's "excluding the latter surplus" |
| `…/oi-qm-ext-1/whole-model-bridge.md`:254 [R] | "Forward model correspondence — Every admitted native model's complete observable histories have one compatible quantum interpretation" |

Whether `verification/programmes/oi-qm/PROGRAMME.md` (F2, PG:531–537: principles "necessary and
sufficient for QM") is to be read against the amended target is not decided here; PG:539–543 (F3,
"OI admits a larger theory space … identifies the QM subclass") states a classification of the
same shape as part 2.

## 5. The amended model-level target

Fixed throughout: each nonempty finite A, the extension E of EP:54, and one architecture 𝔄 (§2).
Every obligation is open. None is proved here.

### 5.1 Part 1: quantum inclusion

**I.** For every nonempty finite A and every T in `Q_exact(A)` there exists one M_{A,T} in
`M(E, J_exact(A))`, an instance of 𝔄, with M_{A,T} ≡ T.

- **I-1, one model per comparison.** M_{A,T} covers every p, π and h of `J_exact(A)` (EP:67, EP:112).
- **I-2, one architecture.** Φ, the observer-interface rules, the loading map ι, the record maps R
  and τ, the label interpretation and the resource policy are those of 𝔄. Dependence on A or T
  enters only through parameters that 𝔄 declares before any law is compared; no model is fitted
  to p_T, and none is constructed separately per protocol (EP:100, EP:102; #914 c.6875046763).
- **I-3, physical sourcing.** E is independently physically justified. Each clause of 𝔄 carries
  its source status in the EP §4.2 ledger; an inclusion using an unsourced or posited clause is a
  conditional inclusion and carries that clause as a named hypothesis.
- **I-4, exactness.** Exact law-equality (EP:120); the approximation target stays separate (EP:121);
  any completion or carrier enlargement is declared (EP:123).
- **Witness.** A construction of M_{A,T} under I-1 to I-4 and a proof of M_{A,T} ≡ T. EP:61–64 is
  I without the clauses I-2 and I-3.

### 5.2 Part 2: quantum-sector equivalence

C is a predicate on members of `M(E, J_exact(A))`. Write `M_C(E, A)` for the members satisfying C.

**Admissibility of a sector condition.** A condition C is admissible only if:

- **C-1, independent statement.** C is defined from the candidate's native data
  (Ω, Φ, Λ, μ, ι, R, τ, E) and physical quantities, before any law is compared. It is not defined
  by law-equality with a member of `Q_exact(A)`, not equivalent to it by definition, and not a list
  of the protocols on which a model matches (the condition EP:102 places on E, and EP:164).
- **C-2, physical justification.** C is justified independently of the agreement it is used to
  obtain, including why observation is confined to the sector (#914 c.6875548603).
- **C-3, hard to vary (§A.29).** C states in advance the existing results it preserves, delivers
  at least one independent prediction or postdiction beyond the sector equivalence, and is rejected
  if it can be adjusted to fit any outcome.
- **C-4, no narrowing of the interface.** C selects models, or physical regimes with their stated
  justification; it does not remove procedures from `J_exact(A)`. A member of `M_C(E, A)` lacking a
  preparation, instrument, record operation or composite procedure of `J_exact(A)` has an
  availability gap (EP:43, EP:104).
- **C-5, nonvacuity.** `M_C(E, A)` is nonempty; S⇐ below supplies this.

No condition C is proposed here. Adopting one is a new premise under §A.29 and needs its own owner
authorization.

**S⇒ (C ⟹ quantum).** For every M in `M_C(E, A)` there exists one T in `Q_exact(A)` with M ≡ T.
Witness: a proof over the whole sector, with the label interpretation of I-2.

**S⇐ (quantum ⟹ C), coverage form.** For every T in `Q_exact(A)`, the inclusion witness M_{A,T} of
I satisfies C. Witness: a proof that C holds of those witnesses. With I, it gives that every quantum
experiment family is the family of some member of `M_C(E, A)`.

**S⇐′ (quantum ⟹ C), necessity form.** For every M in `M(E, J_exact(A))`, if M ≡ T for some T in
`Q_exact(A)`, then C(M). Undetermined pending owner decision (§7, R1): neither adopted nor retired.

**S-J (confinement and Bell).** A justification that observation is confined to `M_C(E, A)`; for
Bell, reproduction of quantum Bell correlations and exclusion of stronger-than-quantum
correlations in the physical sector, not in all of OI + E (#914 c.6875548603; decision 3 of
c.6875046763, "Separate research track, mandatory for full equivalence"). The spatially separated
two-wing comparison is not part of `J_exact(A)` as defined at EP:33–41.

**Permitted.** A member of `M(E, J_exact(A))` outside `M_C(E, A)` need not match any member of
`Q_exact(A)`.

### 5.3 Part 3: gravity compatibility

- **G-1, same architecture.** General relativity is obtained from the substratum and observer of
  the 𝔄 used in parts 1 and 2, not from a second substratum or observer.
- **G-2, consistency.** No hypothesis used for G-1 contradicts E, C or a clause of I, S⇒, S⇐ or
  S-J; the regime in which G-1 holds is stated together with the regime of the sector.
- **G-3, open targets.** The covariant field equations: "The present derivation uses the Einstein
  equations through Jacobson's relation (§3.1) and does not derive them; the covariant field
  equations remain the Level-G3 target (§8.7)" (`papers/GR.md`:162). The G3 matter-coupling and
  source question: #873. Both stay open.

Gate A supplies no part of G: `J_exact(A)` has no spacetime, metric or gravitational observable.
The owner record states part 3 as an inclusion ("GR ⊆ OI"); no two-way form is stated, and none is
added.

## 6. Crosswalk

### 6.1 Obligations of the accepted contract

| EP | Obligation | Under this amendment |
| --- | --- | --- |
| 33–49 | Interface, comparator, label interpretation, native record law | kept |
| 54 | Fixed independently specified E | kept |
| 56–59 | Every admitted model matches one quantum theory | superseded by S⇒, restricted to `M_C(E, A)` |
| 61–64 | Every quantum theory matched by one admitted model | kept; strengthened by I (one architecture, sourcing status); required inside C by S⇐ |
| 67, 112 | Coherent single model for all p, π, h | kept, for I, S⇒ and S⇐ |
| 69 | Directions are proposed obligations; kernel table is interface-level | kept, for all parts |
| 73–100 | Candidate data, loading, setting independence, causal prefix, native law | kept |
| 102 | Admission independent of the comparator; nonemptiness | kept; extended to C by C-1 and C-5 |
| 104 | Availability gaps; preservation of labels and composites | kept; applies inside C by C-4 |
| 106 | Resource accounting | kept |
| 116–123 | Exactness versus approximation | kept |
| 129–164 | Crosswalk and ledger | kept; row 11 (157) forward half superseded as in §4.1(b) |
| 170 | Both whole-model obligations stated separately | replaced by I, S⇒, S⇐, S-J and G stated separately |
| 175, 179 | No premise adopted; acceptance criterion | kept |

### 6.2 Existing results bearing on each part

| Part | Result | Status at its source |
| --- | --- | --- |
| 1 | `exactAll_of_physical_general`, `OIBridge/GeneralCarrier.lean`:93 | [K], interface level, complex matrix kinematics taken as given (`papers/Main.md`:562); "does not discharge either whole-model realization statement" (EP:69) |
| 1 | Uniform continuum realization, `papers/Main.md`:596; single controlled dynamics, :580 | [P], ε-forms at fixed d, m, K; the realization "runs genuine quantum instruments" and "uses no property of the substratum beyond finiteness and reversibility"; approximation target, not I |
| 1 | Classical-dimension obstruction, `papers/Main.md`:558 | [P], unbounded-dimension half imported (:600); excludes I on one fixed finite realization for the full qubit theory |
| 1 | `…/oi-qm-ext-1/whole-model-bridge.md`:257 | [R]: "No such full construction is provided" |
| 2 | `exactAll_iff_physical_general`, `GeneralCarrier.lean`:100, directions `physical_of_exactAll` (`PhysicalCharacterization.lean`:301) and `exactAll_of_physical_general` | [K], both directions separately witnessed, on `FiniteOperationalTheory` with complex kinematics given; an interface-level equivalence, not a sector equivalence over native models; whether its conditions bear on a C is not assessed |
| 2 | OI⁺ ⟺ exact finite endomorphic operational QM, `papers/Main.md`:586–588; `qm_of_oiPlus` :191, `oiPlus_of_qm` :198, `CarrierGeneralOIPlus.lean` | [K], directions separate, kinematics given; "not a claim that bare OI entails the added principles" (:588) |
| 2 | `papers/Main.md`:598: "$D_{\mathrm{finite}}$ is strictly larger" than the quantum class | [P], reason stated (response-table construction); behaviour sets at finite-test level |
| 2 | `oi_alone_not_qm`, `GeneralCarrier.lean`:160 | [K], two-state carrier, theories realizing the sealed OI core; that predicate is not the native admissible class (EP:47) |
| 2 | `papers/Main.md`:582: gluing theorem "not a uniqueness theorem"; :600: "What remains is selection." | [P]; the selection question is the C question of part 2, unanswered |
| 2 | BR-0, `…/oi-qm-ext-1/whole-model-bridge.md`:178, :233–254 | [R], candidate E-AR with the point-preparation/sign subinterface at a fixed typed object; see R4 |
| 2 | Bell, `papers/Main.md` §3.3 (:358), PR negative control (:427) | [P]; S-J open |
| 3 | `papers/GR.md`:162; :352 and :633 ("conditional on the G3 coupling theorem") | [P] for what is derived; field equations and coupling open |

## 7. Points where the accepted contract and the new target do not fit directly

- **R1, the reverse sector direction.** #914 c.6875548603 states the sector both as a set equality
  ("the experiment families satisfying C are exactly those of QM_fin") and as two implications.
  Read on families, (quantum ⟹ C) is S⇐; read on models, it is S⇐′, which is strictly stronger and,
  with I, implies S⇐. Which is intended is an owner question; S⇐ is required under both readings.
- **R2, scope of "one common architecture".** EP:54 fixes E "For each nonempty finite A"; I-2
  reads "one common … architecture" as one 𝔄 for all A. EP does not state what distinguishes members
  of `Q_exact(A)`, so the content of "for every T" beyond the interface of EP:43 is not fixed.
- **R3, E versus C, and confinement.** Under EP a condition folded into E restricts the admitted
  class itself; a C with S⇒ and S⇐ folded into E as E ∧ C would meet EP:56–64. The new target keeps
  C separate and adds S-J. EP has no notion of confinement: every member of `M(E, J)` realizes every
  protocol of J (EP:102). What it means physically for a non-sector member to exist while
  observation is confined to the sector is not stated in any record read.
- **R4, earlier verdicts against the forward direction.** The E-AR verdict ("refuted under E-AR",
  whole-model-bridge.md:242) concerns the forward correspondence for that candidate (:254) at its
  scope and stands as recorded. Reading: for a given C it obstructs S⇒ for every sector member that retains the
  sign subinterface at a fixed typed object, and C-4 excludes removing that read by definition.
- **R5, nonquantum exclusion.** The #1169 statements in §4.2 require excluding nonquantum
  behaviour for the interface as a whole; under part 2 that exclusion is required in the sector.
- **R6, gravity.** Part 3 has no interface in Gate A; its obligations are on 𝔄 and are tracked
  outside the endomorphic comparison.

## 8. What this amendment does not do

- It proves nothing: I, S⇒, S⇐, S⇐′, S-J and G are open, and no member of any of the classes
  named is exhibited.
- It adopts no extension E and no condition C, and proposes no C.
- It changes no scientific status and promotes no claim; physical source is not passed.
- It does not edit `endpoints.md`, `TARGET-THEOREM-r3.md`, `whole-model-bridge.md`,
  `PROGRAMME.md` or any Issue; the statements of §4.2 are identified for separate maintenance.
- It authorizes no merge, integration, execution, simulation, Lean change, manuscript change,
  board change or QB5(a) start; integration needs independent non-author review first and its own
  owner authorization.

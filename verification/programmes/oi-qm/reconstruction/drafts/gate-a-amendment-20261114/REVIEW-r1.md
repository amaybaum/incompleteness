# Review of GATE-A-AMEND-r1.md (with NOTES-r1.md)

Non-author review, paper-only: reading, grep and hand reasoning. Nothing was computed on OI models, no
Lean was built, and nothing in the repository or on GitHub was edited or posted.

**Verdict: REVISE.** One blocking finding and fourteen should-fix findings. All have exact
replacement text below. Once they are applied, a focused confirmation review of the changed
sections is enough. The draft's main structure is sound and should stay: a forward amendment
only, the class-wide forward display EP:56–59 correctly identified as the superseded obligation,
the two directions kept inside C and stated separately, admissibility conditions on C, no E or C
adopted, and gravity kept open.

## 0. What was read

- `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` (`wt-mainread/`). `endpoints.md` (EP) was
  read in full, all 179 lines. Its blob `d9d92e03…` was confirmed at `fdc3dd7f`, `9d24914c` and
  `dc0b333a`, and all three are ancestors of `c3b5f37a`; `dc0b333a` is the #1173 merge. Also
  read: `whole-model-bridge.md` 1–12, 170–262; `composition-source-map.md` 18, 87–91, 168;
  `two-system-interface.md` 183–188, 322–330; `prepared-pair-source.md` 155–181 (grep);
  `observer-access-20261106/ASSESSMENT.md` 1–8, 280–290; `states-dynamics-audit-20261024/REPORT.md`
  1–6, 70–76; `PROGRAMME.md` 35, 40, 527–545; `papers/Main.md` 358, 427, 554–600; `papers/GR.md`
  162, 352, 633 and headings. Lean statements were read, not built:
  `OIBridge/GeneralCarrier.lean` 88–104 and 150–178; `PhysicalCharacterization.lean` 293–305;
  `CarrierGeneralOIPlus.lean` 185–215; `StructuralClosure.lean` 348, 405–430;
  `TypedCompletion.lean` 850 (location only).
- Off `main`, branch `records/target-theorem-914-20261114` at `755f9bff` (`wt-target/`):
  `README.md` in full, and `TARGET-THEOREM-r3.md` by grep (lines 5, 34, 46, 121–129, 234–244).
- GitHub, public API, read 2026-11-14: #914 c.6875046763 and c.6875548603; #1169 c.6875724719,
  c.6686258585 and c.6703342848, all in full; #1173 c.6686122542 (the Gate A ACCEPT) in full; the
  #1169 body in full; every #1169 comment, searched with a regex for two-way and soundness wording;
  the #1143 body, by grep; the #873 body, by grep.

Throughout, `AM:n` is line n of `gatea/GATE-A-AMEND-r1.md` and `EP:n` is line n of the blob
`d9d92e03`.

## 1. Kept requirements (check 1)

I listed the contract's operational requirements myself from EP:1–179 and compared that list with
the AM:68–94 table and the AM:223–238 crosswalk. Nothing the draft lists is weakened. The
following are missing from both tables, or appear only in a compressed form that drops a clause.

**B1 (blocking), AM:64–94 and AM:223–238.** EP:110 appears in neither table. It defines the
comparator's history law, states that its availability is exactly `J_exact(A)`, and requires an
explicit implementation or transport argument for any change of system type. The tables also omit
EP:21–29, the kernel's scope: given complex kinematics, structure fields that are not a derivation
from bare OI, and a native interpretation that remains an obligation. Several further clauses are
dropped from rows that are listed:
- EP:40: relabelling, and "The resource contract must supply compatible finite record/controller
  resources for every such protocol".
- EP:43: labels are requests and "do not postulate that a native procedure realizes a requested
  density matrix or instrument"; constructing the native procedure and its label interpretation
  is part of the correspondence obligation.
- EP:45: "no preassigned finite menu, horizon bound or ancilla cutoff".
- EP:47: `RealizesSealedOICore` is not the native class. AM:251 relies on this clause.
- EP:77: U must include every uncontrolled component and "cannot be empty or discard an
  inconvenient hidden correlation".
- EP:79: loading isolation. The row labels it as setting independence.
- EP:92: a product factorization or causal/locality structure "must state that hypothesis". S-J
  needs this clause.
- EP:104: J is declared before laws are compared; equality is operational, "not a bijection
  between ontic configurations and density matrices".
- EP:112: the native law and the comparator law stay independently defined.
- EP:164: the disclosure duty for posited Hilbert kinematics, control or the Born law.
- EP:172 and EP:177: the kernel is reused only at its nonempty-carrier, endomorphic and
  given-kinematics scope.

The authorization requires every operational requirement to be "explicitly traced". The draft
also has no residual clause, so any line it does not trace has undetermined standing.

Replacement. Insert at AM:66, before the table:

> Every line of EP not listed in §4.1 as superseded stays in force unchanged, whether or not it is
> listed below; the table traces the operational requirements and is not a narrowing of EP.

Add these rows to the AM:68–94 table:

| Requirement | EP |
| --- | --- |
| Kernel scope: complex kinematics given; structure fields not derived from bare OI; native interpretation of every field an obligation; interface data existence and realization separate obligations; the characterization is not a construction of native models | 21–29 |
| Labels are requests, not postulated native realizations; constructing the native procedure and fixed label interpretation is part of the correspondence | 43 |
| Exactness has no preassigned finite menu, horizon bound or ancilla cutoff | 45 |
| `RealizesSealedOICore` not identified with the native admissible class | 47 |
| Seed law fixed for the preparation, not chosen to fit settings or outputs; U includes every uncontrolled component, cannot be empty or discard a hidden correlation; no global product decomposition of Ω inferred | 75–77 |
| Loading changes only the specified controller fields; restriction to U unchanged until the declared interaction; held preparation, ready state and public records preserved; differing fields isolated | 79 |
| A product factorization or causal/locality structure used by a candidate is stated as a hypothesis | 92 |
| Comparator law: trace of the sequentially composed branches applied to ρ_p; availability exactly `J_exact(A)`; changes of system type need an explicit implementation/transport argument | 110 |
| Native law and comparator law independently defined until a reconstruction proves agreement | 112 |
| A posited Hilbert kinematics, unitary control or native Born law is disclosed with its limited explanatory content | 164 |
| The kernel theorem is reused only at its nonempty-carrier, endomorphic-operation and given-kinematics scope | 172, 177 |

Amend these existing rows:
- Row 40: "… repeated read without change, conditioning, relabelling and coarse-graining; compatible finite record/controller resources for every protocol".
- Row 79–88: becomes "81–88".
- Row 104: add "; J declared before laws are compared; equality is operational equivalence, not a bijection of ontic configurations with density matrices".

Add these crosswalk rows to AM:223–238: "| 21–29 | Kernel scope and native-interpretation obligations | kept |" and "| 110 | Comparator law and availability; transport for type changes | kept |". Change "| 175, 179 |" to "| 172, 175, 177, 179 |".

**F1 (should-fix), AM:17–31 and AM:64–94.** The owner records keep requirements that EP does not
state, and the draft does not carry them. #914 c.6875548603 (`amaybaum`, 2026-11-14T09:56:47Z)
lists them: "The other requirements of comment 6875046763 stand: an independently physically
justified extension E; a compatible model and interface for all parts, not constructions chosen
per experiment; no assumption of one fixed finite total carrier; the configuration-level no-go not
read as covering every observer interface; exact as the ultimate target; Bell as a separate track
that the full result requires." C.6875046763 is stronger than EP:123's "not silently used". It
says "the target cannot assume one fixed finite total carrier" and that "Finite access by an
embedded observer must remain distinct from finiteness of the underlying dynamics". #1169
c.6703342848 (2026-11-07T06:25:11Z) records the owner clarification "We do not need the hidden
machinery itself to be quantum".

There is also a provenance problem. AM:21–22 quotes "an independently physically justified
extension of OI and a single common substratum–observer realization" as kept, but those words
come from the target-theorem sentence that c.6875548603 states "is replaced".

Replace AM:21–23 with:

> The requirements of this comment that stand are those listed in #914 c.6875548603: "The other
> requirements of comment 6875046763 stand: an independently physically justified extension E; a
> compatible model and interface for all parts, not constructions chosen per experiment; no
> assumption of one fixed finite total carrier; the configuration-level no-go not read as covering
> every observer interface; exact as the ultimate target; Bell as a separate track that the full
> result requires." From c.6875046763 itself: "The two directions must use a compatible model and
> operational interface, not unrelated constructions selected separately for each experiment." and
> "Finite access by an embedded observer must remain distinct from finiteness of the underlying
> dynamics."

Then add a block below the AM:68–94 table:

> | Owner-record requirement | Source |
> | --- | --- |
> | No fixed finite total carrier assumed; finite observer access distinct from finiteness of the dynamics | #914 c.6875046763, c.6875548603 |
> | The configuration-level no-go not read as covering every observer interface | #914 c.6875046763, c.6875548603 |
> | One compatible model and interface for all parts | #914 c.6875548603 |
> | Hidden machinery need not be quantum; deterministic hidden dynamics admissible | #1169 c.6703342848 |

**F2 (should-fix), AM:66.** "applies to every part of §5" contradicts AM:215, "Gate A supplies
no part of G", and AM:199, which places the two-wing comparison outside `J_exact(A)`. Replace
with:

> Every requirement below applies to I, S⇒ and S⇐ (§5.1–5.2). For S-J and part 3, which lie
> outside `J_exact(A)`, the requirements bind the shared architecture 𝔄, and an interface for
> those parts must carry the same requirements when it is typed.

## 2. Superseded obligations (check 2)

The quotation of EP:56–59 (AM:102–105) is exact and correctly located. The ellipsis quotation of
EP:157 (AM:111–112) is faithful. The draft rightly treats EP:104 and EP:112 ("Both directions",
"In both directions") as constraints on whichever directions are required, so nothing required
inside the sector is superseded. No class-wide obligation that the new target drops is left in
force within EP. Read with the coverage clause of AM:228, the "no-relaxation" statement holds
inside C.

**F3 (should-fix), AM:113–115 versus AM:237.** The two replacement lists for EP:170 differ: one
reads "I, S⇒, S⇐ and G", the other "I, S⇒, S⇐, S-J and G". EP:170 is also a deliverable of the
completed Gate A unit, so it is not superseded as text. Replace AM:113–115 from "EP:170:" onward
with:

> EP:170 records a completed Gate A deliverable and is not edited; under this amendment the
> whole-model obligations are I, S⇒, S⇐, S-J and G, each stated separately.

**F4 (should-fix), AM:120–131.** The list of dependent statements is incomplete. NOTES-r1.md:62–69
acknowledges this. A search finds further restatements of the class-wide forward obligation or of
class-wide nonquantum exclusion:
- #1169 body, "Combined systems" row: "operational no-signalling and exclusion of nonquantum
  correlations".
- #1169 c.6763928950 (2026-11-10T09:34:24Z): "**soundness** (no extra nonquantum complete
  histories) and **completeness** (required quantum preparations/instruments/composites) remain
  **separate open** proof obligations".
- #1143 body: "**Full class equivalence:** both quantified directions hold for the predeclared
  scope, with no non-quantum OI behaviours and no missing target quantum models", and "The current
  “no non-quantum OI behaviours” requirement is read at the complete operational-theory level".
- `composition-source-map.md`:90: "Full #1169 needs all target operations and no extra accessible
  behavior."
- `two-system-interface.md`:187: "A source class admitting these values fails quantum soundness".
- `two-system-interface.md`:325–327: "Its allowed preparation and control class must be physically
  justified and checked for nonquantum behavior."
- `observer-access-20261106/ASSESSMENT.md`:284–286: "the full Gate A interface, with compatible
  resources and both whole-model directions".
- `states-dynamics-audit-20261024/REPORT.md`:75: "Full equivalence | Both soundness (no extra
  operational laws) and completeness".

Add these rows to the AM:124–131 table, tagged [I] or [R] as above, and replace AM:122 with:

> These restate a class-wide forward obligation or a class-wide exclusion of nonquantum behaviour;
> under this amendment each reads as its sector form (S⇒ on `M_C(E, A)`, nonquantum exclusion in
> the physical sector), and verdicts they record stand at their own scope.

Change AM:287 to read "… the statements of §4.2 are identified for separate maintenance; the list
is the result of a search of `oi-qm/` and of #1169, #1143 and #914, not a proof that no other
restatement exists." Also add #1143 to AM:133–136, since it holds the selection question.

## 3. The three-part target (check 3)

**F5 (should-fix), AM:145–159, part 1's quantifier.** The authorization says "every finite quantum
experiment" (#1169 c.6875724719, item 1), and the owner proposal says "every finite quantum
experiment is realized by one common OI model" (#914 c.6875548603). I quantifies over
`J_exact(A)` only, which is endomorphic. It excludes dimension-changing maps (EP:41, EP:110) and
has no spatially separated multi-wing structure (AM:199). EP:43 requires a narrower target to be
named. Add after AM:159:

> - **Scope.** I over `J_exact(A)` is the Gate A form of part 1. Finite quantum experiments
>   outside it (changes of system type, EP:41 and EP:110; spatially separated multi-wing
>   protocols, §5.2 S-J) are not covered by I and are named as the remainder of part 1; each needs
>   a typed interface carrying the requirements of §3 before its inclusion is stated.

**F6 (should-fix), AM:150–152, I-2.** Parameters that depend on T are allowed as long as 𝔄
"declares" them, but nothing stops them from being chosen per T to fit. Replace "Dependence on A or
T enters only through parameters that 𝔄 declares before any law is compared; no model is fitted to
p_T" with:

> Dependence on A or T enters only through a parameter map that is part of 𝔄, fixed before any
> law is compared, and computed from the typed data of A and of the requested labels, never from
> the values of p_T; no model is fitted to p_T

**F7 (should-fix), AM:153–155, I-3.** As written, an inclusion that uses a posited clause could be
read as discharging I. This conflicts with the authorization's "physically sourced" (#1169
c.6875724719, item 1) and with "Physical source remains **NOT PASSED**". Append:

> A conditional inclusion is a conditional result; it does not discharge I.

**F8 (should-fix), AM:163 together with AM:176, type of C.** AM:163 makes C a predicate on models,
and C-1 builds it from native data. The owner record states the sector on experiment families:
"the experiment families satisfying C are exactly those of QM_fin" (#914 c.6875548603). The
authorization says "OI models outside C" (#1169 c.6875724719). C-4 ("C selects models, or physical
regimes") admits a third type. #1143 lists further possible filter targets: "substratum laws `φ`,
realization distributions `μ`, observer embeddings, admissible preparations/readouts, or *tuples*
of these". The type of C is an undecided owner question, and it decides R1 (see §5). Replace AM:163
with:

> C is a declared predicate whose type is stated with it: on members of `M(E, J_exact(A))`
> through their native data, or on their history laws. Write `M_C(E, A)` for the members
> satisfying C. Which type the target uses is undetermined pending owner decision (§7, R1).

In C-4 (AM:176), delete "or physical regimes with their stated justification". A regime selection
is admissible only if it is stated as a predicate of one of the declared types.

**F9 (should-fix), AM:167–170, C-1 noncircularity and fitting.** C-1 does not exclude a C defined
as membership in the image of the inclusion construction of I, or as an enumeration of models.
Such a C makes S⇒ and S⇐ hold by construction. C-1 also allows a C with a free parameter that is
fixed later by comparison. Append to C-1:

> C is not defined by membership in the set of models constructed for I, by an enumeration of
> models or experiment families, or with any parameter, threshold or list whose value is fixed by
> comparison with p_T or with any member of `Q_exact(A)`. If C is stated on history laws, it is
> stated without reference to `Q_exact(A)`, and its equivalence to the quantum class, if any, is a
> theorem to be proved, not a definition.

**F10 (should-fix), AM:180, C-5.** Nonemptiness is supplied by I together with S⇐, which are open
target obligations. As written, admissibility depends on proving the target. Replace with:

> - **C-5, nonvacuity.** Nonemptiness of `M_C(E, A)` is an obligation (EP:102), discharged by S⇐;
>   S⇒ over an empty sector establishes nothing.

**F11 (should-fix), AM:185–193, the S⇒, S⇐ and S⇐′ statements.** First, S⇒'s witness "with the
label interpretation of I-2" is ill-typed. A sector member need not be an instance of 𝔄, so the
clause could be read as restricting S⇒ to instances of 𝔄, which would retire the forward
direction for the other sector members. Second, S⇐ is tied to "the inclusion witness M_{A,T}", so
it is undefined if I has several witnesses. Third, neither statement carries EP:67, EP:104 or
EP:112 explicitly. Fourth, S⇐′ is called "strictly stronger" with no qualification, though its
relation to S⇐ depends on the type of C. Replace AM:185–193 with the text in §4(c) below.

**F12 (should-fix), AM:195–199, S-J.** S-J bundles three obligations of different kinds:
- confinement (#914 c.6875548603);
- reproduction of quantum Bell correlations, which is a coverage-type obligation;
- exclusion of stronger-than-quantum correlations in the physical sector, which is a
  soundness-type obligation.

All three sit on a two-wing interface that is not yet typed. C-2 (AM:172) also repeats the
confinement clause, which leaves unclear whether confinement is a condition of admissibility or a
target. Replace AM:195–199 with:

> **S-J (confinement).** A physical justification that observation is confined to `M_C(E, A)`
> (#914 c.6875548603). It is separate from S⇒ and S⇐ and is not implied by them.
>
> **B (Bell track; decision 3 of #914 c.6875046763, "Separate research track, mandatory for full
> equivalence").** On a two-wing interface `J_Bell` still to be typed, stating its locality and
> setting-independence hypotheses (EP:81–92): B⇐, quantum Bell correlations reproduced by members
> of `M_C(E, A)` meeting I-1 to I-4; B⇒, no member of `M_C(E, A)` produces stronger-than-quantum
> correlations on `J_Bell`. Required in the physical sector, not in all of OI + E (#914
> c.6875548603). `J_Bell` is not part of `J_exact(A)` as defined at EP:33–41.

In C-2 (AM:171–172), replace "including why observation is confined to the sector (#914
c.6875548603)" with "; the confinement obligation is S-J". In AM:282 and AM:237, add B to the
lists of obligations.

**Part 3 (AM:204–217)** is stated as an inclusion only, matching "Gravity (GR ⊆ OI)". The GR.md:162
quotation is exact, and #873 stays open. **Nit N1, AM:209:** "the regime of the sector" assumes a
regime-typed C. Replace it with "the scope of C".

## 4. Coordinator's addition: soundness, coverage and necessity

**(a) What the owner record supports.** #914 c.6875548603 (`amaybaum`, 2026-11-14T09:56:47Z)
states the sector as follows: "For a stated, physically justified condition C: within OI + E, the
experiment families satisfying C are exactly those of QM_fin. This is an equivalence for the sector
and has two directions, each needing its own witness: (C ⟹ quantum) and (quantum ⟹ C)." The
proposal the owner accepted says: "a stated, physically justified condition picks out a part of OI
that is exactly QM". Part 1 is "every finite quantum experiment is realized by one common OI
model". C.6875046763 requires "a compatible model and operational interface, not unrelated
constructions selected separately for each experiment".

In this wording C is applied to experiment families, and the sector is a set equality:
{families of OI + E satisfying C} = {families of QM_fin}. Its ⊇ half, (quantum ⟹ C), says that
every QM_fin family is an OI + E family satisfying C. That is an existence-and-coverage statement.
Nothing in either comment states the model-level necessity form, which would say that every model
with quantum behaviour satisfies C. The record therefore supports the coverage reading.

R1's question ("which is intended is an owner question") is real only in one case: when C depends
on native data that are not determined by the history law. The draft itself creates that case
through AM:163 and C-1. If C is a function of the history law, coverage implies necessity. To see
this, suppose C(M) = c(p_M), and suppose S⇐ gives an M with C(M) and M ≡ T. Then every M′ ≡ T has
p_M′ = p_M, and so C(M′) holds. The owner question is therefore the type of C (F8), not which
reading of "(quantum ⟹ C)" is meant.

The coordinator's proposal has the same content as the coverage reading. The draft should adopt
it as the stated reading and record necessity as an unadopted option, which keeps the planning
status unchanged (§A.45 rule 1).

**(b) The draft's quantifiers.** The draft's S⇐ is the coverage reading, and S⇐′ is the necessity
reading. The quantifiers are not fully spelled out, for three reasons:
- S⇐ quantifies through "the inclusion witness M_{A,T} of I" rather than "there exists M".
- Neither S⇒ nor S⇐ states that A is universally quantified, that one fixed label interpretation
  is used, or that composition, conditioning and composites are preserved (EP:67, EP:104, EP:112).
- S⇒'s witness clause imports I-2's label interpretation (F11).

**(c) Replacement for AM:185–193.**

> **S⇒ (soundness; C ⟹ quantum).** For every nonempty finite A and every M in
> `M(E, J_exact(A))` with C(M), there exists one T in `Q_exact(A)` such that M ≡ T, with M's own
> fixed label interpretation (EP:47) covering every p, π and h of `J_exact(A)` and preserving
> sequential and outcome-dependent composition, conditioning and the declared spectator and
> composite operations (EP:67, EP:104, EP:112). Witness: a proof quantified over every such M; a
> proof over a subclass, a protocol menu or a bounded horizon does not discharge it.
>
> **S⇐ (coverage; quantum ⟹ C).** For every nonempty finite A and every T in `Q_exact(A)`, there
> exists one M in `M(E, J_exact(A))`, an instance of 𝔄 meeting I-1 to I-4, such that C(M) and
> M ≡ T, with one fixed label interpretation covering every p, π and h of `J_exact(A)` and
> preserving the same composition, conditioning and composite structure (EP:67, EP:104, EP:112).
> Witness: for each T, a construction of such an M with proofs of C(M) and of M ≡ T. S⇐ implies
> I. S⇒ and S⇐ together give the set equality of #914 c.6875548603: the history laws of members
> of `M_C(E, A)` are exactly those of `Q_exact(A)`.
>
> **S⇐ᴺ (necessity; an option, not adopted).** For every nonempty finite A and every M in
> `M(E, J_exact(A))`, if M ≡ T for some T in `Q_exact(A)`, then C(M). It is not stated in the
> owner records, which state the sector on experiment families. With I it implies S⇐. If C is a
> function of the history law, S⇐ implies S⇐ᴺ. Otherwise S⇐ᴺ is a further claim about every
> admitted realization of quantum behaviour, including distinct models with identical histories,
> and it needs its own theorem showing that no admitted model outside the sector reproduces a
> member of `Q_exact(A)`. Whether S⇐ᴺ is part of the target is undetermined pending owner
> decision (§7, R1).

**(d) S-J.** In the draft, S-J is separate from S⇒ and S⇐, and the "Permitted" clause (AM:201–202)
is correct. Two defects remain: C-2 repeats the confinement clause, and S-J mixes confinement
with the two Bell directions. Under F12, S-J is confinement alone. It is separate from soundness,
coverage and necessity, and it is required under every reading.

## 5. The draft's reconciliation points (check 4)

**F13 (should-fix), AM:259–262, R1.** Replace with:

> - **R1, the type of C and the reverse sector direction.** #914 c.6875548603 states the sector on
>   experiment families ("the experiment families satisfying C are exactly those of QM_fin"),
>   whose ⊇ half is the coverage form S⇐; the record supports that reading. #1169 c.6875724719
>   speaks of "OI models outside C". If C is a function of the history law, S⇐ implies S⇐ᴺ and
>   the two forms coincide; if C depends on native data beyond the history law, S⇐ᴺ is a separate,
>   stronger claim. The owner question is the type of C (§5.2), and with it whether S⇐ᴺ is
>   required; S⇐ is required under every answer.

**R2 (AM:263–265)** is a real point but cites EP:54 only. Add: "#914 c.6875548603's proposal
reads 'every finite quantum experiment is realized by one common OI model', and #1169
c.6875724719 reads 'one common, physically sourced substratum–observer architecture'. I as stated
(one 𝔄, one instance per (A, T)) is the architecture reading; the single-model reading is
stronger and is undetermined pending owner decision." On the open definition of `Q_exact(A)`,
note that TARGET-THEOREM-r3.md:34 reads it as Q_op with the full interface. EP:43 and EP:110 give
it the standard trace law over the whole interface, and nothing in EP indexes several members.
"For every T" is then at most a quantification over label conventions. State this as a reading,
not a definition.

**R3 (AM:266–270)** is correct. The observation that E ∧ C would meet EP:56–64 is right and worth
keeping. EP has no confinement notion, and AM:268–269 is accurate.

**F14 (should-fix), AM:271–274, R4.** The obstruction has a narrower scope than R4 states.
`whole-model-bridge.md`:238–240 says: "no complete full-interface witness with a fixed
finite-dimensional prepared object and preparation-independent test labels". Replace the
"Reading:" sentence with:

> Reading (not a result of that record): for any C, it obstructs S⇒ for every sector member that
> retains the point-preparation/sign subinterface at a fixed finite-dimensional prepared object
> with preparation-independent test labels (whole-model-bridge.md:238–240, :247–248); C-4 bars
> removing that read by definition, so the amendment does not reopen the E-AR verdict.

**R5 and R6** are correct.

**Reconciliation points the draft missed:**
- The quantifier of part 1 versus `J_exact(A)` (F5).
- The type of C (F8).
- The circularity through the inclusion construction (F9).

## 6. Crosswalk and statuses (check 5)

These were checked at source and are correct:
- `exactAll_of_physical_general` is at GeneralCarrier.lean:93 and `exactAll_iff_physical_general`
  at :100, which pairs `physical_of_exactAll` (PhysicalCharacterization.lean:301) with the
  former. The two directions are separate.
- The Lean characterization is stated with complex kinematics taken as given (Main:562, :584).
- `qm_of_oiPlus` is at :191 and `oiPlus_of_qm` at :198. Main:588's "not a claim that bare OI
  entails the added principles" is quoted exactly.
- `oi_alone_not_qm` is at :160 and is on `Fin 2`.
- The quotations from Main:598 ("strictly larger"), :582 ("not a uniqueness theorem") and :600
  ("What remains is selection.") are exact.
- The quotation from `whole-model-bridge.md`:257 is exact.
- GR.md:633 is quoted exactly, and its "conditional on G3" appears at :352.

**F15 (should-fix), AM:245–246.** The row for Main:596 and :580 omits the qualifiers stated at the
source. Main:600 item (4) reads: "proved in exact arithmetic … at finite $b$ the instrument-level
Rounding Lemma bounds each step, and the bound on the realized law is open". The single-dynamics
corollary's check is a numerical probe (Main:580, check 13). The Main:558 row omits the
interface qualifier ("The factorization interface assumed is the ordinary preparation → finite
ontic system → measurement one"). The owner records require that this no-go not be read "as
covering every observer interface".

In the status cell of AM:245, after "[P], ε-forms at fixed d, m, K", insert: "proved in exact
arithmetic; the finite-b bound on the realized law is open (Main:600 item (4))".

Replace the status cell of AM:246 with: "[P] under the preparation → finite ontic system →
measurement interface, unbounded-dimension half imported (:600); excludes I on one fixed finite
realization with that interface for the full qubit theory; not a no-go for every observer
interface (#914 c.6875548603)".

**F16 (should-fix), AM:252 and AM:244–255.** AM:252 says "the selection question is the C question
of part 2". That identifies two questions without a formal map, which the claim/evidence rules
forbid. Replace it with "the selection question bears on the C question of part 2; no formal
identification is made".

The crosswalk also leaves out the existing results that bear most directly on parts 1 and 2:
- Main:588's substratum-source form: `substratum_plus_control_qm` (StructuralClosure.lean:414) and
  its stated converse `qm_generated_by_substratum_extension` (:423), with `substratumGen_not_control`
  (:348). The converse's witness is `fullClass`, for which `ExtendsSubstratum` holds trivially
  (`fullClass_extendsSubstratum`, :419–420, `fun _ _ _ _ _ => trivial`).
- The typed form `typed_determined_iff` (TypedCompletion.lean:850), which bears on the scope in F5.
- #1143, the selection programme, including its classical-preservation controls.

Add three rows:

> | 1, 2 | Substratum plus one controllability resource, `substratum_plus_control_qm`, StructuralClosure.lean:414; converse `qm_generated_by_substratum_extension` :423; `substratumGen_not_control` :348 (Main:588) | [K], interface level, complex kinematics given; the converse's witness is `fullClass`, whose `ExtendsSubstratum` holds trivially (:419–420); the added operation is "an empirical controllability resource" (Main:588), not sourced |
> | 1 | Typed form, `typed_determined_iff`, TypedCompletion.lean:850 (Main:588) | [K] by location and the manuscript's statement only; interface level; bears on the scope of I beyond endomorphic maps (§5.1) |
> | 2 | #1143 selection questions, including classical-preservation controls and nonquantum countermodels | [I], planning only; no scientific status (§A.45 rule 1) |

## 7. Faithfulness to the authorization and the owner records (check 6)

The quotations at AM:19–41 were checked against the API text. They are exact, apart from dropped
bold markup and marked ellipses. The authors and times are correct: `amaybaum` at
2026-11-14T09:14:01Z, 09:56:47Z and 10:12:11Z. The draft correctly says these comments were posted
from the owner's account and report statements made in coordinating sessions (NOTES-r1.md:54–56).

The draft stays within scope. It adopts no E or C, proposes no C, promotes no status, makes no
merge, manuscript or board change, does not start QB5(a), and says physical source is not passed
(AM:280–290). The pins at AM:10–15 were verified.

The provenance issue at AM:21–22 is covered under F1.

**Nit N2, AM:43–47.** Under §A.42 item 8, the three-part target is attached to #914 c.6875548603
by definition. Add: "The obligations of §5 are defined from #914 c.6875548603 as planning content;
that is their only use."

## 8. Register (check 7)

The register is neutral and technical. I found no self-narration, no reader instruction, no caps
emphasis outside quotations, and no revision-history phrasing in claims. Two nits:
- **N3, AM:261:** "strictly stronger" is superseded by F11 and F13.
- **N4, AM:68–94:** row 79–88 is mislabelled (corrected under B1).

## 9. Summary of findings

| ID | Severity | Location | Subject |
| --- | --- | --- | --- |
| B1 | blocking | AM:64–94, 223–238 | EP:110, EP:21–29 and clauses of 40, 43, 45, 47, 77, 79, 92, 104, 112, 164, 172/177 untraced; no residual clause |
| F1 | should-fix | AM:17–31, 64–94 | Owner standing requirements not carried; quotation taken from the replaced sentence |
| F2 | should-fix | AM:66 | "applies to every part" contradicts AM:199 and AM:215 |
| F3 | should-fix | AM:113–115, 237 | Inconsistent EP:170 replacement lists |
| F4 | should-fix | AM:120–131 | Dependent restatements incomplete (#1169 body and c.6763928950, #1143, five records on `main`) |
| F5 | should-fix | AM:145–159 | Part 1 quantifies over every finite quantum experiment; I covers only `J_exact(A)` |
| F6 | should-fix | AM:150–152 | T-dependent parameters could be fitted |
| F7 | should-fix | AM:153–155 | A conditional inclusion must not discharge I |
| F8 | should-fix | AM:163, 176 | Type of C undetermined (families, models or regimes) |
| F9 | should-fix | AM:167–170 | C-1 allows C defined by the I construction or by later-fixed parameters |
| F10 | should-fix | AM:180 | C-5 makes admissibility depend on the target |
| F11 | should-fix | AM:185–193 | Quantifiers of S⇒, S⇐ and S⇐′; ill-typed witness clause |
| F12 | should-fix | AM:171–172, 195–199 | S-J mixes confinement with the two Bell directions; duplicated in C-2 |
| F13 | should-fix | AM:259–262 | R1 misplaces the owner question |
| F14 | should-fix | AM:271–274 | R4 scope qualifier |
| F15 | should-fix | AM:245–246 | Statuses omit source qualifiers |
| F16 | should-fix | AM:244–255 | Identification without a formal map; most relevant existing results missing |
| N1–N4 | nit | AM:209, 43–47, 261, 68–94 | as stated |

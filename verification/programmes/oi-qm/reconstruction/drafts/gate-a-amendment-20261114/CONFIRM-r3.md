# Focused confirmation of the Gate A amendment r3 at an exact head

**This is a model review of the text at the head below.** It is a non-author, paper-only review:
reading, grep and hand reasoning. It is not independent verification, not a human review and not an
owner decision. Nothing was computed on OI models, no Lean was built, and nothing in the repository
or on GitHub was edited or posted.

**Head.** Branch `research/gate-a-amendment-1169-20261114`, commit
`65b0a9293c1eb15a56409f7d06d22734bb0378ec` (draft PR #1289), checkout `wt-gatea/`.
- `git rev-parse HEAD` returns that SHA, and `git status --porcelain` is empty.
- The commit's single parent is `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- It adds eleven files under
  `verification/programmes/oi-qm/reconstruction/drafts/gate-a-amendment-20261114/` and changes
  nothing else. `endpoints.md` is unchanged from `c3b5f37a`.

`r3:n` is line n of `GATE-A-AMEND-r3.md`, `TR3` is `GATE-A-AMEND-r3-TRACE.md`, `OQ:n` is line n of
`OWNER-QUESTIONS-r3.md`, and `EP:n` is line n of `endpoints.md`, blob `d9d92e03`.

**Verdict: ACCEPT WITH CHANGES.**
- **Part A.** K1–K5 and N1–N4 are applied as described, and both modified applications are right
  on their merits.
- **Part B.** Criterion 1 is met. Criteria 2, 3 and 4 are not fully met; required changes RC1–RC3
  give exact replacement text.
- **Part C.** "Question 2 answers itself" is too strong and is corrected under RC2.
- RC4 is a small residue of K2.

No required change alters a disposition of the contract or any status. Optional suggestions are
listed separately in §4.

## A. The confirmation changes

### Byte identity of the earlier files

In the checkout, `GATE-A-AMEND-r1.md`, `NOTES-r1.md`, `REVIEW-r1.md`, `GATE-A-AMEND-r2.md`,
`GATE-A-AMEND-r2-TRACE.md` and `CONFIRM-r2.md` are byte-identical (`cmp`) to the scratchpad copies.
Those scratchpad copies still have the sizes and modification times they had when I reviewed them:
r1 at 10:20, NOTES at 10:21, REVIEW-r1 at 10:31, r2-TRACE at 10:35, r2 at 10:36 and CONFIRM-r2 at
10:41.

`RESPONSE-r1.md` is the one exception, and it is expected. It has grown by the appended section
"Confirmation review (CONFIRM-r2.md)". I did not byte-compare its first part with the version I
reviewed, because I have no saved copy of that version. I did re-read the last of its earlier
lines, which read as before.

### The trace

The dispositions in TR3 §1 differ from r2's trace only in the EP:51 row. The other textual
differences are these:
- "r2" becomes "the amendment" in rows 56–59, 61–64, 69 and 112.
- S-A is added to row 170's list of obligations and to the introduction of §2.
- The title and companion line are updated.
- A new §3 holds the status table moved from r2 §6.2. A diff against r2:306–320 shows it is
  unchanged except for N2, two cross-reference wordings, and "S-A" added to the Bell row.

### Dispositions

| ID | Applied as RESPONSE-r1 says | Assessment |
| --- | --- | --- |
| K1 | yes (r3:248–259, 265–268, 364–368, 388–395; lists at r3:82, 154, 236, 280, 307, 399; TR3 row 170) | Correct. The added pointer from S-A to owner question 4 is right on the merits: S-A is the reading of "experiment families" taken here, and whether the target includes it is the owner's choice. The quotations from #1169 c.6703342848 at r3:392–395 are exact. |
| K2 | yes, modified (r3:283–298) | The modification is right. S⇐ is quantified per T, so "an S⇐ witness M for T" is the well-typed form, and CONFIRM-r2's "an M meeting S⇐" was loose. One residue remains (RC4). |
| K3 | yes (r3:208–209, 213, 215) | Correct. |
| K4 | yes (r3:377–387) | Applied verbatim; items 1 and 2 change under RC2. |
| K5 | yes (r3:145–148; TR3 row 51) | Correct. |
| N1–N4 | yes (r3:53, 131; TR3 §3; r3:163; r3:325–332) | Correct. |

## B. The four criteria

### B.1 Preservation: met

Every nonblank line of EP has exactly one disposition; I re-checked mechanically that the 113
lines each appear once. The comparator law EP:110 is kept (r3:114, TR3 row 110). Only three lines
are affected: EP:56–59 is superseded, the forward half of EP:157 is superseded, and EP:51 is partly
superseded. The residual clause (r3:77–80) protects anything not listed. Points left open are
named as open: `PROGRAMME.md` F2 at r3:169–171, and the remainder of part 1 at r3:199–203. No
change is required.

### B.2 Domain of C: not fully met

r3 does define a domain for C-law: "the history law p_M over `J_exact(A)`" (r3:213). Three gaps
remain.

- The meaning of "C(M)" for a model is never stated. It is left implicit in "members … satisfying
  C" (r3:207–208).
- r3 uses "experiment family" in two senses. S-A reads it as the complete family of a member's
  admissible procedures (r3:254–255, r3:388–389). The C-law row puts C on the labelled law only,
  while citing "the experiment families satisfying C".
- No single statement fixes that the same meaning is used in S⇒, S-A, S⇐, S⇐ᴺ, S-J and B.

**RC1 (required).**

(a) Insert after r3:68:

> **Fam(M)**, the specified experiment family of a member M of `M(E, J_exact(A))`: the history
> laws, each with its complete accessible record history, of every finite adaptive protocol that
> M's admissible physical preparation, intervention and record procedures (EP:47, EP:75) can carry
> out on the objects of `J_exact(A)`. It contains p_M over `J_exact(A)` through M's fixed label
> interpretation. Under the restricted reading of owner question 4 (§8), Fam(M) is p_M over
> `J_exact(A)` alone. Write **M ≃ T** for "M ≡ T, and every law in Fam(M) is, up to relabelling of
> outcomes, the law of some protocol of `J_exact(A)` under M's fixed label interpretation"; under
> the restricted reading, M ≃ T is M ≡ T. ≃ is the full operational equivalence used below: it has
> the comparator's domain (every p, π and h of `J_exact(A)`, EP:110) and, beyond it, the domain of
> S-A.

(b) Replace r3:207–209 with:

> **Type and domain of C.** C is a declared predicate whose type and domain are stated with it.
> "C(M)", "M satisfies C" and "M is inside C" have one meaning in S⇒, S-A, S⇐, S⇐ᴺ, S-J, B and C-1
> to C-5: under C-law, that Fam(M) satisfies C; under C-model, that the native data of M satisfy C.
> Write `M_C(E, A)` for the members of `M(E, J_exact(A))` satisfying C. The admissible types are
> C-law and C-model; which one the target uses is undetermined pending owner decision (§7, R1):

(c) Replace the C-law row (r3:213) with:

> | C-law | the specified experiment family Fam(M) (§2) | matches "the experiment families satisfying C" (#914 c.6875548603); C must be a family-level condition stated without reference to `Q_exact(A)` (C-1), and its agreement with the quantum class on OI + E is a theorem to be proved, not a definition; S⇐ᴺ follows from S⇐ only if C is ≃-invariant (S⇐ᴺ below), which is automatic when C is a function of p_M over the whole of `J_exact(A)`; a C of that kind cannot separate members that differ only in unlabelled procedures, so S-A is then an obligation on E and 𝔄 |

(d) In r3:253–255, replace "S⇒ with S-A gives that the complete experiment family of each sector
member is that of one member of `Q_exact(A)`." with "S⇒ with S-A gives M ≃ T for one T in
`Q_exact(A)` (§2): the complete experiment family of each sector member is that of one member of
`Q_exact(A)`."

(e) In r3:288, replace "and a member satisfies C when its restriction to `J_exact(A₁ × A₂)` does."
with "and a member satisfies C when its restriction to `J_exact(A₁ × A₂)`, a member of
`M(E, J_exact(A₁ × A₂))`, satisfies C in the sense fixed above."

### B.3 The necessity qualification: not met as worded

r3 says "If C is a function of the history law, S⇐ implies S⇐ᴺ" (r3:272–273, r3:339–340), "follows
from S⇐" (r3:213, r3:378), and "a distinct question only under C-model" (r3:381). These are correct
only when C is a function of p_M over the whole of `J_exact(A)`, for the same A. In that case two
models that both ≡ T have equal laws, and so equal values of C.

The claims fail in the other case, when C depends on unlabelled laws in the family. That case is
the reading of "experiment families" that S-A adopts. Two models that both match T on the labelled
protocols can differ in their other procedures, so coverage does not then give necessity.

There is a second problem with S⇐ᴺ as stated. Its antecedent is "M ≡ T", which is labelled-only.
Combined with S-A, it would force every admitted model with a quantum labelled law to have no
nonquantum unlabelled procedure. That is not the intended option.

The precise statement is this. Coverage, together with S-A where S-A is part of the target, implies
necessity if membership in C is invariant under the full equivalence ≃, for the same carrier and
the same T. Checked by hand: for T, S⇐ gives M₀ with C(M₀) and M₀ ≡ T; S-A gives M₀ ≃ T; then for
any M′ ≃ T, invariance gives C(M′).

**RC2 (required).**

(a) Replace r3:270–277 with:

> **S⇐ᴺ (necessity; an option, not adopted).** For every nonempty finite A and every M in
> `M(E, J_exact(A))`, if M ≃ T for some T in `Q_exact(A)`, then C(M). It is not stated in the owner
> records, which state the sector on experiment families. With I it implies S⇐ when the witnesses
> of I satisfy M_{A,T} ≃ T, which under the restricted reading of question 4 is always. S⇐, with
> S-A where S-A is part of the target, implies S⇐ᴺ if membership in C is ≃-invariant: C(M) ⟺ C(M′)
> whenever M and M′ are members of `M(E, J_exact(A))` for the same A with M ≃ T and M′ ≃ T for the
> same T. The invariance is under the full equivalence ≃, with the comparator's whole domain and
> the domain of S-A; invariance under agreement on a menu, a bounded horizon, a subfamily of
> preparations or a different carrier does not suffice. A C that is a function of p_M over the
> whole of `J_exact(A)` is ≃-invariant. A C that also depends on unlabelled laws in Fam(M), or on
> native data, is ≃-invariant only by a separate proof. Without the invariance, S⇐ᴺ is a further
> claim about every admitted realization of quantum behaviour, including distinct models with
> identical histories, and it needs its own theorem showing that no admitted model outside the
> sector satisfies M ≃ T for any T in `Q_exact(A)`. Whether S⇐ᴺ is part of the target is
> undetermined pending owner decision (§7, R1).

(b) In the C-model row (r3:214), replace "S⇐ᴺ is a separate, stronger claim" with "≃-invariance of
C is not automatic, so S⇐ᴺ is a separate, stronger claim unless the invariance is proved".

(c) In R1 (r3:339–342), replace from "If C is a function of the history law" to the end of the
bullet with:

> If C is ≃-invariant (§5.2, S⇐ᴺ), S⇐ with S-A implies S⇐ᴺ and the two forms coincide; this holds
> for a C that is a function of p_M over the whole of `J_exact(A)`. If C depends on unlabelled laws
> in Fam(M) or on native data, S⇐ᴺ is a separate, stronger claim unless the invariance is proved.
> The owner question is the type and domain of C (§5.2), and with it whether S⇐ᴺ is required; S⇐
> is required under every answer.

(d) Replace §8 items 1 and 2 (r3:377–383) with:

> 1. The type and domain of C. C-law commits to a condition on the specified experiment family
>    Fam(M), stated without reference to `Q_exact(A)`; S⇐ᴺ then follows from S⇐ (with S-A) only if
>    C is ≃-invariant, which is automatic when C is a function of p_M over the whole of
>    `J_exact(A)`. C-model commits to a condition on native data, under which S⇐ᴺ is a separate
>    claim unless ≃-invariance is proved. A regime-formulated condition is admitted only as one of
>    these (§5.2).
> 2. Whether S⇐ᴺ is part of the target; a distinct question whenever C is not ≃-invariant (under
>    C-model, and under C-law when C depends on unlabelled laws). Including it commits to a theorem
>    that no admitted model outside the sector satisfies M ≃ T for any T in `Q_exact(A)`; excluding
>    it permits such models.

(e) `OWNER-QUESTIONS-r3.md`: see C below.

### B.4 Anti-fitting: partly met

C-1 (r3:219–226) already excludes membership in "the set of models constructed for I",
enumerations, and parameters "fixed by comparison with p_T or with any member of `Q_exact(A)`". C-2
and C-3 add justification independent of the agreement and the hard-to-vary rule. Four openings
remain.

- **The architecture's own instances.** A C defined as "is one of the instances of 𝔄" or "is an
  S⇐ witness" is not literally "the set of models constructed for I", but it meets the sector
  obligations by construction in the same way.
- **Choice among candidate conditions.** Picking C from a family of candidates by which one
  yields agreement is not a "parameter, threshold or list".
- **Quantum-derived thresholds.** A threshold set to a quantum-derived constant, such as a quantum
  correlation bound, or to data selected for agreeing with quantum theory, is not literally a
  comparison "with p_T".
- **Folding into E.** R3 notes that a condition folded into E "would meet EP:56–64" (r3:352–353).
  r3 applies EP:102, EP:104 and EP:164 to C (r3:158), but it does not apply C-1 to C-3 to E. A
  fitted or construction-defined condition could therefore be placed in E with a trivial C.

**RC3 (required).**

(a) Replace the sentence at r3:222–224 ("C is not defined by membership … any member of
`Q_exact(A)`.") with:

> C is not defined by membership in the set of models constructed for I or for S⇐, by being one of
> the instances of 𝔄 produced by its parameter map, by an enumeration of models or experiment
> families, or with any parameter, threshold or list whose value is fixed by comparison with p_T,
> with any member of `Q_exact(A)`, with a quantity derived from quantum theory, or with data
> selected for agreeing with it. C is not chosen from a family of candidate conditions according
> to which member yields agreement; a C revised after a comparison is a new condition and meets
> C-1 to C-5 afresh. If a C stated independently coincides with one of the excluded sets, that
> coincidence is a theorem to be proved.

(b) Insert after r3:236:

> C-1 to C-3 apply equally to any condition placed in E: a condition moved from C into E, or
> stated there in the first place, is subject to the same exclusions (EP:102; I-3), so the sector
> obligations are not met by folding a fitted or construction-defined condition into E with a
> trivial C.

With (a) and (b), both routes are closed: (a) C as the image of the inclusion construction, and
(b) parameters selected after matching. No other clause reopens them. C-5's "discharged by S⇐"
does not, because S⇐ needs C(M) for a C that already meets C-1. I-2's parameter map does not,
because it concerns the model, not C, and stays under EP:47, EP:75, EP:92 and EP:100.

### RC4 (required), B⇐, r3:290–293

The S⇐ witness already matches T on all of `J_exact(A₁ × A₂)`. B⇐ therefore adds content only if
the extension is an admitted member for the two-wing interface, meaning it satisfies that
interface's locality and setting-independence hypotheses. The text does not say so. Replace
r3:290–293 with:

> - **B⇐ (coverage).** For all nonempty finite A₁, A₂ and every T in `Q_exact(A₁ × A₂)`, there
>   exists an S⇐ witness M for T whose extension to `J_Bell(A₁, A₂)` is a member of
>   `M(E, J_Bell(A₁, A₂))`, keeps the same fixed label interpretation, meets I-1 to I-4, and
>   reproduces exactly T's law, the trace law of EP:110, for every quantum two-wing protocol and
>   preparation on the quantum-labelled part of `J_Bell(A₁, A₂)`.

## C. OWNER-QUESTIONS-r3.md

**Quotations.** These were checked against the API text and are exact:
- OQ:6–7, from #914 c.6875548603;
- OQ:10 and OQ:25–26, from #1169 c.6875724719;
- OQ:29, from the proposal quoted in #914 c.6875548603;
- OQ:37, OQ:38–39 and OQ:39–40, from #1169 c.6703342848 and #914 c.6875548603.

OQ:21, "No owner record states the "yes" form", is correct for the records read: #914 c.6875046763,
c.6875548603 and #1169 c.6875724719.

**Options and commitments.** Questions 3 and 4 state their options and commitments correctly.
Question 4's recorded positions are quoted neutrally. The phrase "the complete agreed experimental
interface" can be read toward either option, and the file does not assign it to one.

**"Question 2 answers itself" (OQ:8).** This is not correct as stated, given B.3. It holds only
when C depends on nothing but the labelled Gate A statistics, all of them.

**RC2(e) (required).** Replace OQ:6–8 with:

> - *A condition on the observed statistics* (the model's experiment family). This matches #914
>   c.6875548603: "the experiment families satisfying C are exactly those of QM_fin". C must be
>   stated without mentioning quantum theory; agreement with it is a theorem to prove. Question 2
>   answers itself only if C depends on nothing but the statistics of the labelled Gate A
>   experiments, all of them, which are the statistics the comparison with quantum theory uses. If
>   C also depends on the statistics of other experiments the model can perform (question 4, first
>   option), question 2 stays open unless C is shown to give the same answer for any two models
>   fully equivalent to the same quantum theory.

Replace OQ:16–17 with:

> **2. Must every model that reproduces quantum statistics satisfy C?** This is a real question
> under the second option of question 1, and under the first option whenever C depends on more
> than the labelled statistics.

## 4. Optional suggestions (not required)

- **O1, `README.md`:11–12.** "The owner confirmed in the coordinating session that both paper-only
  units of that day were authorized and may continue." No record read states this. #1169
  c.6875724719 says only that the approval came "immediately after the two-work-package
  confirmation request". §A.45 rule 3 wants an authorization tied to a recorded owner comment.
  Either cite the record or replace the sentence with: "That comment states the approval was given
  "immediately after the two-work-package confirmation request"."
- **O2, `README.md`:19.** The trace's dispositions are "kept, record, superseded or partly
  superseded", not "(kept, superseded or replaced)".
- **O3, `README.md`:36–37.** "The trace changes only in the row for EP:51" is more exact as: "The
  trace's dispositions change only in the row for EP:51; row 170's list gains S-A, and §3 is the
  status table moved from r2."
- **O4, OQ:10–11.** "C can then be read physically" is an assessment found in no source. A neutral
  form is: "C is then a statement about the model's physical data, and question 2 becomes a real
  question."
- **O5, OQ:20.** "only coverage is required" would be clearer as "in this direction only coverage
  is required".
- **O6, OQ:28–29.** The quoted sentence is the coordinator's proposal that the owner accepted
  ("Yes proceed as suggested."). The same comment's formal restatement reads "on one common
  substratum–observer realization". Saying "the proposal the owner accepted in #914 c.6875548603"
  is more exact.
- **O7, OQ:37–39.** "its author asks for" would be more exact as "its author states that the
  accepted contract requires".
- **O8, I-2 (r3:185–187).** "computed from the typed data of A and of the requested labels" could
  add "each procedure depending only on its own label, declared inputs and retained past (EP:75,
  EP:90, EP:100)". That would make clear the parameter map cannot tabulate the trace rule across
  future instruments (EP:47, EP:92). The kept lines of EP already require this.

## 5. Register

r3 and the owner-questions file are in a neutral technical register. Outside O4, I found no
self-assessment, no reader instruction and no caps emphasis outside quotations. The replacement
texts above keep the same register.

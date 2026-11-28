# Confirmation review of TARGET-THEOREM-r3 at the exact head

**Exact head.** Draft PR #1287, branch `records/target-theorem-914-20261114`, commit
`755f9bffb904635f2c512a42a4dfa88f8591a6b1`. Checked before reading: `git rev-parse HEAD` equals that
SHA and the working tree is clean. Directory: `verification/programmes/oi-qm/target-theorem-20261114/`.
Sources were read on `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` (`wt-mainread`, clean), and
through the GitHub REST API (read only): the bodies of #1216, #1236, #1169, the titles of #1007 and
#1055, and comments 6875046763 and 6875548603 on #914 and 6876591512 on #1169.

**What this is.** A model review of the text at that head by a non-author. It is not independent
verification, not a human review and not an owner decision. Paper-only: no Lean build, no
computation, no edit to any checkout, nothing posted. "Reading" marks a composition of statements made
in this review that no source states.

**Overall verdict: ACCEPT WITH CHANGES.** r3 applies C1–C6 as `RESPONSE-r1.md` describes, and every
status and witness r3 changed matches its source in statement, hypotheses, carrier and direction. Six
changes are required: one in r3 (a difference between the T5c soundness reading that C4 introduced
and the cited theorem's own docstring), four in `README.md`, and one in `OWNER-BRIEF-r3.md`. None of
them changes a status.

***

## Question 1. Does r3 implement C1–C6 as `RESPONSE-r1.md` describes?

**Verdict: yes.** `diff TARGET-THEOREM-r2.md TARGET-THEOREM-r3.md` has thirteen hunks. Every hunk is
accounted for below, and nothing else changed.

| r3 line | Change | Accounted for by | Matches the text `CONFIRM-r2.md` gave |
|---|---|---|---|
| 1 | title "(r2)" → "(r3)" | revision label | n/a |
| 3 | "r3 answers `REVIEW-r1.md` and `CONFIRM-r2.md`" | revision label | n/a |
| 61 | T0 (ii) ⇒ (iii) Hypotheses cell | C1 | yes, verbatim |
| 74 | T1 (⇐) Hypotheses cell | C1 | yes, verbatim (r2's "a structured prior being used (M:522)" is dropped, as the replacement text does) |
| 80 | T2 header, second sentence | C2 | yes, verbatim |
| 131 | T5c soundness, interface level, Status cell | C4 | yes, verbatim |
| 155 | R5 "What it fixes" and "Bears on" | C3 | yes, with the disclosed extension of the Gate A quotation to "Both directions matter: cover the quantum target and account for every operation the proposed physical OI interface admits", which question 9 quotes |
| 156 | R6 "What it fixes" and "Bears on" | C3 | yes, verbatim |
| 178 | D1, M:588 / GR:260 / RD:320–322 clause | C5 | yes, verbatim |
| 179 | D2, last sentence | C6 | yes, verbatim |
| 232 | §7 first line | C3 | yes, verbatim |
| 235 | question 2 pointer | C3 | yes, with the disclosed addition "titles read" |
| 240, 242 | questions 7 and 9 pointers | C3 | yes, verbatim |
| 246 | question 13 pointer | C3, modified | the modification is right: the current #1169 body contains no occurrence of "Kochen"; Kochen–Specker is attributed to #1236 (R6) only, and Meas-1 to #1169 (R5) |

The list in the §7 first line (1, 2, 4, 6, 7, 8, 9, 10, 12, 13, 14) agrees with the questions that now
carry a pointer: 12 (R6, R7, R8) and 14 (R9) already did in r2; 3, 5, 11 and 15 carry none.

One inaccuracy in `RESPONSE-r1.md`, not in r3: its C6 row says "GR:274–276 cite `typed_determined_iff`,
`typed_determined_of_oiPlusMin`, `typed_determined_of_oiPlusPos`". The three names occur at GR:272, in
the "Typed form" paragraph before the display at GR:274; GR:274 is the display and GR:276 cites none
of them. See optional suggestion O1.

## Question 2. Every status and witness r3 changed or added

**Verdict: all confirmed at source, with one difference to record (required change R1).**

**C1, T1 (⇐) and T0 (ii) ⇒ (iii).** M:518 (Extension, response-table form), read in full: "The
rationality restriction is a property of the uniform-tape presentation, not of realizability"; the
response coordinate $u = (u_c)_c$ over the horizon's finitely many contexts, "product prior
$\mu(u) = \prod_c \mathrm{kern}_c(u_c)$ and deterministic step $x_{k+1} := u_{c(x_{\le k})}$"; the ledger
and clock complete the bijection; $|\mathcal{C}_H| = n^{N}(n{+}1)^K(K{+}1)$, finite; "the prior is a
product and independent of $X_0$"; "The chain rule then reproduces the full multi-time joint for
arbitrary real kernels"; "The characterization below therefore quantifies over general
finite-horizon laws." So:

- *Statement and direction.* M:518 realizes every finite-horizon law as the visible marginal of a
  finite bijection. Q_fb laws are finite-horizon laws, so the cell is the (⇐) direction of T1, QM side
  to OI side, as r3 places it. For T0 it is the (ii) ⇒ (iii) existence step that M:628 takes from the
  dilation theorem.
- *Hypotheses.* Hidden prior independent of the visible initial state, real-valued, a product over
  contexts: as stated. The uniform-tape form needs rational kernels (M:516; prior "uniform on" the tape
  at M:520): as stated. M:516's "Rationality tracks the prior" and the ledger (iv) reading (M:58: on
  the selected bijective carrier the canonical measure "is the uniform probability") support the
  final, reading-tagged sentence.
- *Status.* [P] is right. M:520's kernel note says `S_imp_D` formalizes realization "from an initial
  law on $\mathcal{C}_V \times \mathcal{C}_H$ that may correlate the hidden and visible coordinates; the
  independence of $\mu_H$ from the visible initial state rests on the construction above and the cited
  probes and is not formalized". This agrees with r3's split of T1 (⇐) into [K] (correlated initial
  law) and [P] (independent prior). M:600's "a product prior carrying the quantum conditionals
  (Extension, response-table form)" and M:731's "arbitrary-kernel form via the response-table
  extension" match.
- *Carrier.* M:516 assumes $n = |\mathcal{C}_V| \ge 2$, which M:518 inherits. r3 does not repeat it
  (optional nit O4).

**C2, T2 header.** The current #1216 body contains "Can one mechanism derived from OI approximate …",
"independently justified observer access", Unit 1 question 1 "Do Main's existing approximation
results meet Level A?", Level A "Any specified finite quantum experiment's observable law is
reproduced within ε", and Level B "One reusable mechanism and rule family". M:580 contains "Quantum
mechanics enters as the instrument data and as the state held in the hidden register". The
identification "Main's results, this T2" is r3's: #1216 cites Main ":544, :576, :578", which at
`c3b5f37a` are a section sentence, the Rounding Lemma and a proof, not the theorem at M:596 (optional
suggestion O2).

**C3, R5 and R6.** Every quotation was found in the current Issue bodies: #1169 line 59
("construct-then-reduce"), line 80 ("a proof that assumes Hilbert spaces, arbitrary unitaries, quantum
instruments or the Born rule from the outset is a **conditional reconstruction/embedding**, not a
physical derivation"), line 90 (the Gate A sentence through "admits", the link text of "Gate A
contract" aside), line 121 (Meas-1: "**Born frequencies derived from the stated extension**"); #1236's
owner decision of 2026-11-11 for both added sentences and the "separate obligations" sentence. The
#1169 body was edited at 2026-11-14T11:28:20Z, after r3 was written; all the quoted strings are still
present. #1007 ("SUBSTATE-1: observer-relative finiteness without a finite-total-carrier
requirement") and #1055 ("A1-NECESSITY: can OI's results that use total finiteness be recovered
without the posit A1?") carry question 2's subject, by title.

**C4, T5c soundness at interface level.** Read in the kernel source, not rebuilt:

- `denseFiniteQM_of_denseControl` (OB/DenseInstrumentBridge.lean:495–498): on `Fin 2`, hypotheses
  `DerivedOI T`, `DenseUnitaryControl T`, `KrausSoundExt T`; conclusion `DenseFiniteQM T`, which is
  `KrausSoundExt T ∧ KrausDense T` (OB/DiscreteCompletion.lean:59). `KrausSoundExt` is a hypothesis,
  not a conclusion: confirmed.
- `DerivedOI` (OB/RouteB.lean:146) has first conjunct `ReversibleImplementationLocality T`, which is
  `∃ 𝓘, ImplementationGenerated T 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘 ∧ DaggerStable 𝓘`
  (OB/MicroscopicReversibility.lean:223). `ImplementationGenerated` (OB/ImplementationLocality.lean:352)
  quantifies over `0 < N`.
- `krausSoundExt_of_implementationGenerated` (OB/ImplementationLocality.lean:963): `[Nonempty A]`,
  `ImplementationGenerated T 𝓘 → KrausSoundExt T`. `KrausSoundExt` (OB/CompositeSoundness.lean:123)
  quantifies over levels `n + 1`, matching `0 < N`.

The composition holds as r3 states it, at positive ancilla levels, on a nonempty carrier, marked as a
reading (`DerivedOI.implementationLocality`, OB/RouteB.lean:154, already extracts the first conjunct).
It has a consequence r3 does not record. The docstring of the cited theorem
(OB/DenseInstrumentBridge.lean:492–494) says "a theory satisfying the closure with dense unitary
control may carry a surplus operation that is not Kraus, so soundness is not a consequence of
density", and `verification/audits/operational/dense-instrument-bridge-audit.md`:306 says the same of
`DerivedOI T ∧ DenseUnitaryControl T ∧ KrausSoundExt T → DenseFiniteQM T`. Both soundness and density
in `DenseFiniteQM` are stated at the levels `n + 1` that `ImplementationGenerated` covers. So, if the
reading holds, the hypothesis `KrausSoundExt` follows from the hypothesis `DerivedOI`, and the
docstring's "may carry a surplus operation that is not Kraus" is false for `KrausSoundExt`. No kernel
statement read here exhibits a theory satisfying `DerivedOI` and not `KrausSoundExt`. This is a
difference between documents, the kind r3 §4 records as D1–D4 (required change R1). It is not a
status error in r3, since the cell is tagged as a reading.

**C5, D1.** M:588: "the concrete OI substratum supplies the structural architecture — closure under
composition and coarse-graining, …"; GR:260 as quoted; RD:320–322 "the concrete OI substratum
supplies all of the structural requirements for quantum mechanics but not continuous state-mixing
controllability". "the structural part" is a fair summary of all three.

**C6, D2.** GR:258 is a boxed `⟺` with the quoted sides; GR:274 is a boxed `⟺` with the same left
side and the typed right side. The kernel names for GR:258 are cited at GR:256: `substratum_plus_control_qm`
(OB/StructuralClosure.lean:414; `ExtendsSubstratum` bound to `_`; conclusion `Q_op (genTheory 𝓘 …)`),
`qm_generated_by_substratum_extension` (:423; conclusion `∃ 𝓘, … ∧ ImplementationGenerated T 𝓘`), and
also `substratum_extension_quantum_iff_drives` (:408), an iff between `QuantumArchitecture 𝓘` and
`DrivesElementary 𝓘`, which does not give Q_op from a realization either. D2's conclusion, that the
display is stronger than its cited witnesses (§A.34), holds. The pins "cited at GR:258" and the
GR:274 citations sit at GR:256 and GR:272 (optional suggestion O1).

## Question 3. Does r3 or `OWNER-BRIEF-r3.md` state a status stronger than its source, or recommend a candidate?

**Verdict for r3: no** status stronger than its source was found in the cells r3 changed, nor in spot
checks of T1, T2, T3 (d), T5a and T5c against the same sources. r3 recommends no candidate.

**Verdict for the brief: one statement goes beyond its source (required change R6).** No candidate is
recommended. The candidate summaries in (a) match r3's status columns. Question 3 ("A free datum: T1
holds for all laws") agrees with r3 after C1, with [K] for a correlated initial law and [P] for an
independent prior. In question 15, "Paper proof with independent review: T0 and T2 stand as they are"
says that T0 and T2 already meet that standard. r3 question 15 asks only whether the standard is
sufficient, and no source read here records an independent review of Main's T0 or T2 proofs. T2's
finite-precision bound is open, as the brief's own T2 bullet says. A smaller point: the brief's T1
bullet says "Both directions are checked in Lean" without r3's qualifier that the Lean (⇐) allows an
initial law correlating hidden and visible coordinates (optional suggestion O3).

## Question 4. Does `README.md` describe accurately what was adopted and what r3 is?

**Verdict: mostly yes; four changes are required (R2–R5).**

Accurate:
- The owner's words, "I adopt all five decisions and the target theorem; preserve r3 now", the five
  decision quotations, the target-theorem sentence, the two directions and the compatible-model
  sentence all match comment 6875046763 verbatim.
- "The text adopted, quoted from the proposal the owner relayed" places the adoption on the proposal,
  not on r3. The amendment's quotations, the three parts and "It is not required that every OI model
  behave quantum-mechanically" match comment 6875548603. The `papers/GR.md`:162 pointer is the
  comment's.
- "r3 and the owner brief were written before this amendment and are not edited" is true: commit
  `755f9bffb` touches only `README.md`.
- The README nowhere says the #1169 answers are reflected in r3. It does not mention them at all,
  since it was committed at 09:57Z and comment 6876591512 is from 11:28Z.

Inaccurate or incomplete:
- **Line 10** calls `TARGET-THEOREM-r3.md` "The reviewed text", and line 16 says the six changes "are
  applied in r3". Lines 25–26 say correctly that r3 "has no review of its own". A reader of the
  contents table alone would take r3 to be reviewed (R2).
- **Lines 65–68**, "In the terms of r3 the decision takes the extension form (T3) as the formal
  target", is a reading presented without a tag. Read literally it conflicts with the line before it.
  r3's T3 is proved in both directions in the kernel (kinematics given), while the adopted target
  theorem, which asks for "a single common substratum–observer realization" and an independently
  justified E, is proved in neither direction. That target is a model-level statement of the kind of
  r3's T5b with a stated E, not T3 (R3).
- **Lines 49–63** quote the five decisions and the target sentence but omit two adopted paragraphs of
  comment 6875046763: "Exactness requires special care. …" (no fixed finite total carrier; an
  infinite or completed carrier admissible but its sufficiency not established; finite access
  distinct from finiteness of the dynamics) and "the existing configuration-level no-go result must
  not be mistaken for a no-go covering every possible observer interface". Line 82's "the other
  requirements above stand" points to requirements the README does not show (R4).
- **The amendment section** gives part 2 as "an equivalence for a sector, with two directions each
  needing its own witness". That is accurate for comment 6875548603, but comment 6876591512 on #1169
  later refined it. Answer 1 says C is a condition on the underlying model and "refines the earlier
  wording on #914", and answer 2 says "Necessity remains an optional future theorem". The README
  should point to that comment and say that neither r3, the brief nor the README's account reflects it
  (R5).

## Question 5. Notes for a forward note: r3 read today without the README

These are not errors in r3. r3 is a planning record written before the amendment. Each item says where
r3 would mislead a reader who takes it as the current target.

1. **The target's form.** r3 frames "full equivalence" as a biconditional (title, §1.3, §2 header,
   question 1). The adopted target (6875548603) is a superset: inclusion QM ⊆ OI on one common model,
   a sector of OI cut out by a stated, physically justified condition C, and GR from the same
   substratum and observer. None of T0–T5 is that statement as written. The inclusion is closest to
   T5b (⇐) on one model, and the sector to a T5b (⇒) restricted by C (reading). The gravity part is
   outside r3.
2. **Class-level soundness (O3; T2 ⇒ and T4b ⇒; §5 "a selection principle"; question 9).** The
   amendment removes the obligation that every OI model behave quantum-mechanically, so O3 no longer
   bears on the target. The selection-principle obligation becomes the sector condition C. Per
   6876591512 answer 1 it is a condition on the underlying model, physically stated, with its
   consequences for experiment families defined explicitly. Per answer 2, coverage and soundness are
   required inside C and necessity is an optional future theorem.
3. **Access closure (question 9's R5 pointer; T2 ⇒ "holds for the constructed subclass"; brief
   question 9 "T2's constructed family meets it on paper").** 6876591512 answer 4 requires quantum
   behaviour for every physically performable experiment within C, with access closure "to prevent a
   model from qualifying through selected quantum experiments while also permitting
   stronger-than-quantum experiments". T2's R runs quantum instruments by construction (M:580). Whether
   a subclass cut out that way can be the sector of an independently justified C is not settled by
   T2's [P] result.
4. **The realization quantifier and carriers (questions 2, 5, 6; R3 "F2-reg"; O1, O7; T4c).**
   6876591512 answer 3 makes one single model with one common E the ultimate target, with one common
   architecture an intermediate milestone, and requires the model to accommodate arbitrarily large
   finite carriers. With decision 2 (exact as the ultimate target) and O1/O7, this places the ultimate
   target on an infinite or completed carrier, the territory of r3's T4c. r3 records T4c as not stated
   in the corpus, with both directions open, and the adopted text says its sufficiency "is not
   established". Per-law and per-bound forms (T1, T2) do not meet the inclusion part, and neither does
   R1's reading of M:774 as the theorem-level target.
5. **Converse strength (question 10).** With inclusion on one common model, containment of
   predicates (T5a ⇐) does not meet the target.
6. **Answered questions.** Decisions 1–5 and the amendment answer, in whole or in part, questions 1, 2,
   4, 5, 6, 7, 8, 9, 10, 12 and 15. Their "keep, narrow or supersede" framing in §7 is now historical.
   Question 12's Bell clause is mandatory as a separate track, with exclusion of supraquantum
   correlations "in the physical sector, not in all of OI" (6875548603).
7. **Question 2 and ledger (ii).** The adopted text says that the target cannot assume one fixed
   finite total carrier and that finite access is distinct from finite underlying dynamics. Reading
   question 2's "Does ledger (ii) … stay" as open is now misleading at target level. The posit's role
   in other results is unaffected (#1055).
8. **The README's T3 mapping.** See R3 above. A forward note should not repeat it.

***

## Required changes

### R1 (r3, should-fix). Record the difference between the C4 reading and the cited theorem's docstring

In §4 "Documents that differ", after D4, *insert*:

> - D5. The docstring of `denseFiniteQM_of_denseControl` (OB/DenseInstrumentBridge.lean:492–494)
>   states that "a theory satisfying the closure with dense unitary control may carry a surplus
>   operation that is not Kraus, so soundness is not a consequence of density", and
>   `verification/audits/operational/dense-instrument-bridge-audit.md`:306 says the same of the
>   theorem. `DenseFiniteQM` is `KrausSoundExt T ∧ KrausDense T` (OB/DiscreteCompletion.lean:59), both
>   at levels `n + 1`, and the T5c soundness row derives `KrausSoundExt` from `DerivedOI` at those
>   levels (reading; three kernel statements composed, not rebuilt). If the reading holds, the
>   theorem's hypothesis `KrausSoundExt` follows from its hypothesis `DerivedOI`; no kernel statement
>   read here exhibits a theory satisfying `DerivedOI` and not `KrausSoundExt`.

### R2 (README, line 10). r3 is not reviewed

*Replace* the cell "The reviewed text: the two sides defined, …" with:

> The current text, which applies the confirmation review's six changes and has no review of its own:
> the two sides defined, the candidate target theorems with each direction's status and witness, the
> proved obstructions, what the records already decide, the residual obligations and the open
> questions

*and replace* line 16's cell with:

> Confirmation review of r2: ACCEPT WITH CHANGES; r3 applies its six changes as `RESPONSE-r1.md`
> records

### R3 (README, lines 65–68). Mark the mapping as a reading and separate it from T3

*Replace* "In the terms of r3 the decision takes the extension form (T3) as the formal target and the
native form (T5) as the sourcing programme, with the Bell clause as a separate obligation that the
full equivalence requires." with:

> In the terms of r3 (a reading, not part of the decision): decision 1's "extension form" is the form
> of r3's T3 and its "native form" that of T5, and the Bell clause is a separate obligation that the
> full equivalence requires. The target theorem itself is not T3. T3 relates predicates of an
> operational theory with the kinematics given, and both its directions are proved in the kernel.
> The target asks for an independently justified extension E and a single common
> substratum–observer realization, a model-level statement of the kind of r3's T5b with a stated E,
> and neither of its directions is proved.

### R4 (README, after line 63). Quote the rest of the adopted text

*Insert*, after the sentence ending "selected separately for each experiment."":

> The adopted text continues: "Exactness requires special care. Under the stated finite-system
> obstruction, the target cannot assume one fixed finite total carrier. An infinite or completed
> carrier is an admissible candidate, but its sufficiency is not established. Finite access by an
> embedded observer must remain distinct from finiteness of the underlying dynamics." and "Likewise,
> the existing configuration-level no-go result must not be mistaken for a no-go covering every
> possible observer interface."

### R5 (README, end of the amendment section). Point to the later #1169 answers

*Insert*, before "No part is proved.":

> Four questions on the amended target were answered later the same day on #1169, comment 6876591512
> (`amaybaum`, 2026-11-14): C is a condition on the underlying model, physically stated, with its
> consequences for experiment families defined explicitly, which "refines the earlier wording on
> #914"; coverage and soundness are required and "Necessity remains an optional future theorem"; one
> single model with one common extension E is the ultimate target, one common architecture an
> intermediate milestone; and every physically performable experiment within C must be quantum, with
> access closure. Neither r3, the owner brief nor the account of part 2 above reflects these answers.

### R6 (OWNER-BRIEF-r3.md, question 15). Do not state that T0 and T2 meet a review standard

*Replace* "Paper proof with independent review: T0 and T2 stand as they are." with:

> Paper proof with independent review: T0 and T2 need no formalization, and whether an independent
> review of their proofs is on record is not assessed here; T2's finite-precision bound stays open
> either way.

## Optional suggestions

- **O1 (pins).** In r3 D2, "The two kernel statements cited at GR:258" → "The two kernel statements
  cited at GR:256 for the display at GR:258 (the third name cited there,
  `substratum_extension_quantum_iff_drives`, OB/StructuralClosure.lean:408, relates two architecture
  predicates)"; and "GR:274 … cites the typed determination theorems" → "the typed determination
  theorems cited at GR:272 for the display at GR:274". `RESPONSE-r1.md`'s C6 row has the same pin.
- **O2 (C2).** In the T2 header, mark the identification: "its Unit 1 asks whether Main's
  results (this T2, a reading: #1216 cites Main lines of an earlier revision) meet its Level A".
- **O3 (brief, T1).** Append to the T1 bullet: "In Lean the hidden initial state may be correlated
  with the visible one; with an independent hidden prior, QM ⇒ OI is a paper proof for every law."
- **O4 (r3, T1 ⇐ [P] cell).** Add the carrier hypothesis of M:516, "$|\mathcal{C}_V| \ge 2$", which
  M:518 inherits. The excluded case is trivial.
- **O5 (README line 42, outside the five questions).** "no status in r3 rests on them alone" is too
  broad. R8, five §5 evidence cells (O-RDY, run repetition, the T5c member, the Tsirelson selector,
  the native Bell-availability lemma) and §6 items 2–4 and 6–8 rest on `BL/` and `TL/` records alone,
  tagged [D]. Under §A.42 item 8 a reference is classified one at a time. Suggested text: "Statuses
  tagged [D] in r3 (R8, several §5 evidence cells, §6 items 2–4 and 6–8) rest on these off-`main`
  records and carry their status; no [K], [P] or [R] status in r3 rests on them."
- **O6 (dense-bridge docstring, outside this record).** If R1's reading is confirmed, the
  `denseFiniteQM_of_denseControl` docstring and audit line 306 are a corpus finding for their own
  accountable Issue. This record should not repair them.

## Limits

- Lean statements were read in source at `c3b5f37a` and not rebuilt. R1 and the C4 check are hand
  compositions of kernel statements.
- Issue bodies and comments were read as they stand on 2026-11-14 through the public API. The #1169
  body changed after r3 was written; r3's quotations from it were re-found in the current text.
- Not re-checked here: r3 content unchanged since r2 beyond the spot checks named in question 3, which
  rest on `CONFIRM-r2.md` and `REVIEW-r1.md`; the off-`main` `BL/` and `TL/` records; #875's memo.
- This review does not assess OI, recommend a candidate or adopt anything.

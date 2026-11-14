# Independent review of TRIAGE-r1 (r1)

Non-author, paper-only, read-only review of `triage/TRIAGE-r1.md` and `triage/NOTES-r1.md`.
Nothing was edited, committed, pushed or posted, and no computation on OI models was run. This
review proposes no tier, readiness, authorization or status value (`AGENTS.md` §A.45); every
replacement below is wording for a planning record that the owner decides from.

## 0. Verdict

**ACCEPT WITH CHANGES.** The quotations are accurate and the table is usable as a base. It is not
ready for owner decisions until findings B1–B6 are applied; a focused confirmation of the delta is
enough. Should-fix findings S1–S10 and nits N1–N8 follow.

What holds as written:

- All 294 quoted strings were re-matched against a fresh download of the 90 bodies and 972 comments,
  the amendment files and the decision memo at `acfef447`. All match, and each sits in the source
  the triage attributes it to (two exceptions of placement: S8, N1).
- 90 open Issues, 40 open pull requests; 39 affected and 51 unaffected; every Issue appears once.
- No row proposes a tier, readiness, authorization or scientific-status value.

## 1. What was read

**Target records, in full.** #914 c.6875046763, c.6875548603, c.6876304390; #1169 c.6875724719 and
c.6876591512 (the owner's answers to the four Gate A questions, 2026-11-14T11:28:20Z, posted after
the triage was written); `GATE-A-AMEND-r4.md`, `OWNER-QUESTIONS-r4.md`, §2 of
`GATE-A-AMEND-r3-TRACE.md`; `papers/Main.md`:66 and :598 and `papers/GR.md`:162 in the amendment
worktree; the F2 decision memo at `acfef447` (summary, §1, §2.3, §4.1).

**Issue bodies read in full by this reviewer: all 90.** #865, #866, #867, #868, #869, #870, #871,
#872, #873, #874, #875, #896, #897, #898, #899, #900, #901, #902, #903, #913, #914, #924, #929,
#934, #944, #945, #970, #979, #983, #985, #986, #996, #1004, #1007, #1008, #1010, #1013, #1014,
#1015, #1028, #1029, #1031, #1032, #1037, #1049, #1052, #1055, #1058, #1059, #1060, #1061, #1062,
#1063, #1064, #1065, #1066, #1067, #1068, #1069, #1070, #1071, #1072, #1073, #1090, #1091, #1092,
#1112, #1118, #1141, #1142, #1143, #1147, #1155, #1162, #1163, #1169, #1188, #1190, #1193, #1210,
#1211, #1216, #1217, #1220, #1234, #1236, #1238, #1244, #1245, #1255. Long lines were wrapped, not
cut; the five bodies the writer read with cut lines (#868, #1007, #1010, #1032, #1236) were read
whole. In twelve bodies the standard three-line governance paragraph was skipped after reading it
in the others (it is identical).

**Bodies read only in part by both writer and reviewer: none.**

**Comments.** Read in full: #875 (both); #1238 (all three); #914 c.6563412734, c.6775022284,
c.6776048388, c.6777841157 and the three target comments; #1169 c.6703342848, c.6791556736,
c.6854241002, c.6875724719, c.6876591512; #1143 c.6775039087, c.6863602000; #1216 c.6741763726,
c.6775038456, c.6793397036; #1236 c.6802597845, c.6873565446, c.6875058407; #868 c.6791565399,
c.6791606126, c.6853568040, c.6854708572, c.6873193841, c.6874036684; #873 c.6872959810,
c.6872998421, c.6875553420; #1015 c.6802361539, c.6803560979, c.6803743294, c.6809696031; #1211
c.6740537555 (first half). First lines of every comment on #868, #873, #970, #1015, #1143, #944,
#1064, #1071, #1112, #1147, #1188 and of the last 22 on #1169. Every comment thread of the 51
unaffected Issues was searched for two-way, class-wide, necessity, sector, F2, Tsirelson,
finite-carrier and target wording; the hits (#924, #970, #1015, #1028, #1029, #1031, #1032, #1112,
#1162) were opened.

**Not read.** The remaining comments (about 900 of 972), any pull request, the Project board, the
SEL-ACCESS-1 and SEL-EXCL-1 records (off `main`; taken from #914 c.6776048388 and c.6777841157),
`endpoints.md` itself, the master matrix #914 c.6563412926 beyond three searched passages.

**Provisional status of the split (added criterion 1).** With all 90 bodies read by the reviewer,
the split is not provisional on the ground of unread bodies. It stays provisional in one respect:
it rests on bodies plus the comments listed above, and a restatement of the superseded requirement
in an unread comment would not have been seen. TRIAGE §1 should say so (replacement in B4).

## 2. Blocking findings

### B1. The #914 row maps the `→Q` label onto one target part

- **Location.** §2, row #914, "What changes"; §6 item 11.
- **Source.** #914 body §2: "Directions: `→Q` means OI→QM; `Q→` means QM→OI"; row 20 "Native
  preparation/measurement instrument … | →Q (sourcing)"; rows 8, 9, 11, 12 on what the stated
  access sources; §4, "Which access or interface makes available an operation …". #914
  c.6875548603: "**Inclusion (QM ⊆ OI).** QM_fin ⟹ OI + E on one common substratum–observer
  realization. Required."; "an independently physically justified extension E".
- **Problem.** "`→Q` rows are required on the sector only" holds for rows that state a forward
  implication. The sourcing rows carry the same label, and a physically sourced common realization
  is what inclusion needs; inclusion stays required. TRIAGE itself places row 20's dependants with
  inclusion (D-9, §6 item 5).
- **Replacement cell.** "Goal sentence and F2 endpoint state a class-wide forward requirement. The
  `Dir` label `→Q` does not map onto one part: rows stating a forward implication (for example 3–7,
  17c, 21) are required on the sector only; rows on what OI's own access sources (for example 8, 9,
  11, 12, 20, the last marked "→Q (sourcing)") also serve inclusion, which stays required. No
  record assigns the rows to parts. No rows for C, access closure, confinement or part 3."
- **§6 item 11, replacement.** "#870, #871, #874, #896–#898, #900 and #1070 are unchanged; the
  forward theorem they feed (#914 rows 2–7) is required on the sector, and their text states no
  target."

### B2. The Standard Model branch is treated as the common architecture by default (added criterion 5)

- **Location.** §2 rows #983, #1049, #1211, #1066, #1065; §6 item 1; T7.
- **Source.** #914 c.6875548603: "a compatible model and interface for all parts" (parts are
  inclusion, sector, gravity); "The cosmological constant, the derivation of the Standard Model and
  the black hole information problem are named by the owner as aims this target should serve. This
  record makes no claim about any of them". #1169 c.6876591512, answer 3: "One fixed model, with one
  common extension E, must support subsystems realizing every quantum carrier in the agreed scope.
  Establishing this across one common architecture is an intermediate milestone." No record read
  names the lattice model of the Substratum and SM papers as that model or architecture.
- **Problem.** Five rows and §6 item 1 state as fact that clauses of the lattice branch (A5, the R23
  model, the six-link carrier, the packaged carrier) "are clauses of one object", while T7 asks
  whether that is so. One common model does not select the Standard Model branch; that choice needs
  its own justification.
- **Replacement cells ("What changes").**
  - #983: "None from the amendment as written. If the lattice model R23 concerns is chosen as the
    common model of parts 1–3 (T7), its selection question fixes the substratum those parts share;
    the amendment asks for one model to be exhibited, not for uniqueness."
  - #1049: "None from the amendment as written. If the lattice model whose assumption A5 is at
    issue is chosen as the common model (T7), the linear-or-affine choice is one of its clauses."
  - #1211: "Parent wording "full operational equivalence" predates the amendment; the forward
    direction it audits is required on the sector. Whether the lattice branch it audits is the
    common model is not recorded (T7)."
  - #1066: "None from the amendment as written: the Standard Model is an owner-named aim, not a
    target part. If the six-link lattice branch is chosen as the common model (T7), carrier
    identification is one of its clauses."
  - #1065: "None from the amendment as written. If the manuscripts' lattice substratum is chosen as
    the common model (T7), "Is the manuscripts' physical substratum the packaged carrier" bears on
    that model's substratum."
- **§6 item 1, replacement.** "**One model is required; which one is not recorded.** Parts 1–3 must
  be met by one fixed model with one extension E (#1169 c.6876591512, answer 3; one common
  architecture is an intermediate milestone). The observer (#1062), the physical source (#866) and
  the carrier's cardinality (#1007, #1010, #1055, #1015, #1037) bear on any such model. The update
  rule (#983, #1049, #1234) and the carrier identification (#1065, #1066, #1217, #1211) belong to
  the lattice model of the Substratum and SM papers; they are clauses of the common model only if
  that model is chosen, which needs its own justification (T7)."
- **T7, replacement.** "Which substratum and observer are proposed as the one model of parts 1–3.
  The lattice model of the Substratum and SM papers is one candidate; no record selects it. Until
  one is named, which Issues state clauses of the common model is undetermined."

### B3. Rows that infer a prerequisite, ordering or priority change from a change of target (added criterion 2)

Kind (a) is a change to the ultimate target an Issue serves; kind (b) a change to that unit's
prerequisites, ordering or next step. No record read changes a prerequisite, ordering, board
placement or authorization: #914 c.6875046763 and c.6875548603 each end "No merge, manuscript
change, computation or board change is authorized by this record"; #1169 c.6875724719 lists
"changing board priorities" under "Not authorized"; #1169 c.6876591512 "authorizes no computation,
manuscript change or status change".

**Classification of all 37 rows.**

| Rows | Kind | Note |
| --- | --- | --- |
| #914, #875, #1169, #1143, #1059, #1060, #865/#867/#869, #1052, #1062, #1007, #1010, #1055, #945, #913, #1068, #1245, #1014, #1217, #1210, #1220, #1069 | (a) only, and the row says no more | #945, #1010, #1014, #1220, #1069 are role-only |
| #983, #1049, #1211, #1066, #1065 | (a) only, conditional on T7 | B2 |
| #866 | none shown | S2 |
| #1238 | (a), narrower than stated | S3 |
| #1216, #1236, #872, #868, #1234, #873, #1067, #1061, #1063 | (a), with (b) inferred or implied | replacements below |

**Replacements.**

- **#1216, "Owner question".** Replace "Whether the 2026-11-10 Backlog placement stands" with
  "None new. Decision 2 names approximation a separate milestone; it does not reorder work, and the
  target records authorize no board change, so the 2026-11-10 placement stands as recorded."
- **#1236, "What changes" and "Owner question".** "Role only: a single-qubit, approximate-first
  result is a restricted control for inclusion, not inclusion. The recorded answers stand: #914
  c.6875046763 states "the exact-tunability requirement of #1236 stand[s] as recorded" and
  c.6875058407 "this Issue's requirements stand as recorded"; c.6802597845 itself says ""Approximate
  first" leaves the exact form for later"." Owner question: "None new."
- **#872, "What changes" and "Owner question".** "Kind (a) only. The decision admits "An infinite
  or completed carrier" as a candidate for the exact finite-system target; #872 concerns lifting
  the finite characterization to infinite-dimensional or QFT-like systems. No record relates the two
  limits, so no change to the "finite reconstruction" prerequisite follows." Owner question: "None
  that follows from the records; whether the two limit constructions are related is a research
  question, not a planning change." Delete "part 3 also uses continuum structure" from D-8 or mark
  it *reading*.
- **#868, "Owner question".** Replace "Bell-first parking versus decision 3" with "None new. The
  target records change no priority; "The Bell-first priority is unchanged." (c.6854708572,
  2026-11-13) is the last record."
- **#1234, "What changes".** "Kind (a) only. The target requires that the common model eventually
  carry both its update-rule class and a Bell route. Premise question 6 is unchanged: option (c)
  remains available as the manuscript's present statement, and it then records an incompatibility
  the target would require to be resolved."
- **#873.** See B5.
- **#1067, "What changes".** "Kind (a) only (*reading*): the seam it tracks lies between the GR
  conditions and the quantum Level III states, so it falls under part 3's "consistently with the two
  parts above". ROADMAP's ordering phrase "downstream of the core OI→QM question" is unchanged."
- **#1061, "Owner question".** Replace with "None that follows from the records: no record says
  whether a finite realization datum at one cut assumes a finite total carrier."
- **#1063, "What changes".** "Wording only: in "OI → QM → continuum/local QFT" the first arrow
  reads, under the amendment, as the quantum sector of OI. The prerequisite (#872) and readiness
  entries are unchanged."
- **T4.** Replace with "No conflict is recorded between the Bell-first parking and decision 3: the
  parking is a priority, decision 3 a statement about the target, and the target records change no
  priority. Listed for the owner's information only."
- **T5.** Delete. The #1216 half is answered by "No … board change is authorized by this record";
  the #1236 half by #914 c.6875046763 and #1236 c.6875058407.
- **T11.** Delete (see #872 above).
- **T12.** See B5.

### B4. Unaffected list: two Issues to move, one conditional, and an uneven criterion

- **Location.** §2, §4, §6 items 1 and 3; §1 "Test for "affected"".
- **Problem.** The grounds "clause of the common architecture" and role-only change are applied to
  some Issues and not to others with the same claim. #1055, #1010 and #1014 are listed because results that consume
  total finiteness may not be available on a carrier that is not finite; #1015 and #1037 hold the
  same dependency audit and are listed as unaffected.
- **Move #1015 to §2 (role only).** Sources: body, "Run a term/dependency matrix over `Main`,
  `Substratum`, `SM`, `GR`, `Explainer`, ch01/ch02, FULL book and §4.5 posit ledger: tag each
  finite-`S` use as assumption, theorem, selected representative, finite-horizon surrogate or
  observable-relative fact"; c.6809696031 (2026-11-11), "Still open under this Issue: GR's claim
  that an infinite deep sector gives the same visible law (`GR.md:136`, `:142`, `:589`;
  `appendix-b:195`; `ch18:170`)". #1007's decision names #1015 under "Required follow-through", and
  #1245 names it for the deep-sector corollary. Row: "#1015 | exactness; G (consistency) | Role
  only: its finite-`S` dependency matrix and its open GR infinite-deep-sector item are the
  inventory of what a model without a finite total carrier must recover, on the quantum and the
  gravity side | Landed wording (#1243); "does not authorize adopting infinite `S`" | None new".
- **Move #1037 to §2 (role only).** Sources: body, "Can an embedded observer infer the total
  carrier's cardinality?"; "### U4 — Which finiteness-dependent results survive? (dependency audit,
  not source editing)"; "Quantifier trap: `for every finite K there exists a matching finite F_K`
  is not `there exists one finite F matching all K`"; U6, "no claim that this alone completes
  operational OI ⇔ QM, physical instrument sourcing, Yang–Mills or GR". The quantifier distinction
  is the one #1169 c.6876591512 answer 3 now draws between the intermediate milestone and the
  ultimate single model. Row: "#1037 | exactness; one model | Role only: U1 and U4 separate
  per-horizon finite models from one model for all horizons, which is the distinction between the
  architecture milestone and the single-model target | All units unstarted and separately gated;
  finite-branch theorems kept | None new".
- **#1071, conditional.** Body: "Is the A1–A4, ¬A5 class that contains round H-B's reversible fluid
  witness admissible as OI physics? This is an owner decision." If the #1049 row is kept in any
  form, #1071 belongs beside it: under "OI may contain non-quantum behaviour" the pending
  admissibility decision has two readings (admissible in OI; admissible in the model that carries
  parts 1–3). If the #1049 row is reduced as in B2, #1071 stays unaffected with that reason
  stated. Suggested §4 line: "#1071: hydrodynamics; its pending H-B admissibility decision concerns
  the ¬A5 class and meets the target only if A5 is a clause of the common model (T7)."
- **Judged unaffected, confirmed after full reading:** #870, #871, #874, #896, #897, #898, #900,
  #1070, #899, #901, #979, #985, #986, #902, #903, #924, #929, #934, #1092, #944, #970, #996, #1004,
  #1008, #1058, #1141, #1142, #1013, #1028, #1029, #1031, #1032, #1147, #1064, #1072, #1073, #1090,
  #1091, #1118, #1155, #1162, #1163, #1190, #1193, #1112, #1188, #1244, #1255. Reasons for the ten
  flagged by the first pass:
  - #1064: its two-way question compares a gauge quotient with complete-record equivalence of
    lifts, not OI with QM; no formal map to the target's equivalence is recorded (§6 item 13 is
    right not to assert one).
  - #899: bounds a uniqueness theorem's converse; states no requirement.
  - #944: audits what is established. By parity with #1069 (D-37, a *reading*), workstream 6 ("What
    would discriminate OI from standard quantum theory and general relativity?") has the same
    contact with confinement; either add it beside #1069 or drop the #1069 row to §4. Not a move.
  - #1112, #1142, #1188, #1013: no target wording; #1188's owner note ("do not broaden the two-state
    result into a universal claim without further proof") agrees with the decision.
  - #1147, #1032, #1031: sourcing obligations required before and after; the common-realization
    requirement they serve predates the amendment (#1169 body). State this criterion in §4.
- **§4 corrections.**
  - #970: "its Bell and gravity tracks point to Issues listed in §2" is reversed. #970 names none of
    #1060, #868, #873; #1060, #1066 and #983 name #970. Replace with "#970: research backlog;
    #1060, #1066 and #983 name its tracks 6, 1 and R23 as related; its own text states no target."
  - §6 item 3, last sentence: #1142, #1244 and #1255 do not cover the two lines the target records
    cite (`GR.md`:162, `Main.md`:598). Replace with "#1142, #1244 and #1255 audit other gravity-side
    manuscript statements (GR §3.2, §7.2, §8.5; SM §3.1; Main §1.4); none covers `GR.md`:162 or
    `Main.md`:598."
- **§1, add after "Count".** "The split rests on all 90 bodies and on the comments NOTES lists. It
  is provisional with respect to comments not read: a restatement of the superseded requirement
  there would not have been seen."

### B5. #873: what the "not a prerequisite" sentence governs (added criterion 4)

- **Source, with context.** #873 body, under "## Calculation milestone before explanatory
  outreach": "Keep the explanatory note to Philip Mannheim as a working draft until a concrete
  gravity result has been derived and reviewed. The calculation to pursue is: … Full OI–QM
  equivalence is a separate obligation: it is not a prerequisite for this gravity calculation, and
  completing it alone would not discharge G3." #914 c.6875548603: "The same substratum and observer
  yield general relativity, consistently with the two parts above." #873 c.6875553420: "This changes
  no status on this Issue: G3 remains (C), the QB5(a) preregistration stays frozen at `8dd0de90`,
  and its execution is not authorized."
- **Finding.** The sentence governs the sequencing of one unit, the weak-field calculation that
  precedes outreach (kind (b)). The amendment makes gravity part of the ultimate target (kind (a))
  and places a condition on the finished result. It does not make either part a prerequisite of the
  other's work, so the sentence is **not contradicted**. Its second half ("completing it alone would
  not discharge G3") agrees with gravity being its own part. Only the scope needs stating.
- **Replacement cell ("What changes").** "Kind (a) only: the open field equation is part of the
  target. The body's "not a prerequisite" sentence governs the sequencing of this calculation and
  is not contradicted; quantum and gravity work may proceed in either order. What part 3 adds is a
  condition on the finished result: the completion the calculation specifies must in the end be the
  same substratum and observer as parts 1–2."
- **Owner question, replacement.** "None for sequencing. Whether the completion named in the first
  calculation item is required to be the common model already at the calculation stage is not
  recorded."
- **T12, replacement.** "Whether a completion used for G3 must already be the common model at the
  calculation stage. The QB5(a) preregistration is frozen and its execution not authorized (#873
  c.6872998421, c.6875553420; #1169 c.6875724719 and c.6876591512); no change to it follows."
- **§5 item 10.** Delete "whether its execution criteria need part 3's same-architecture clause is
  an owner question"; a frozen preregistration changes only by an amendment in its own file.

### B6. The owner's answers of 11:28Z settle parts of the triage (revised criterion 6)

- **Source.** #1169 c.6876591512: "I adopt all five Gate A dispositions". Answers: (1) "C applies to
  the underlying model. It should be a physically stated condition, with its consequences for
  experiment families defined explicitly."; (2) "Require coverage and soundness. Necessity remains
  an optional future theorem. Models outside C may also reproduce quantum statistics."; (3) "Make
  one model the ultimate target. One fixed model, with one common extension E, must support
  subsystems realizing every quantum carrier in the agreed scope. Establishing this across one
  common architecture is an intermediate milestone. The ultimate model must accommodate arbitrarily
  large finite carriers, with the permitted encodings and resource requirements stated
  explicitly."; (4) "Require quantum behaviour for every physically performable experiment within
  C. … Access closure must prevent a model from qualifying through selected quantum experiments
  while also permitting stronger-than-quantum experiments." Also: "`GATE-A-AMEND-r4.md` is not
  edited by these answers. It remains the reviewed amendment proposal"; "No sector condition C and
  no extension E is proposed or adopted"; "adoption of the amended target requires an explicit
  owner decision".
- **What follows for each statement the triage marks as depending on an open choice.**

| TRIAGE statement | Status now |
| --- | --- |
| §1: necessity "an option, not adopted"; §6 item 7 "S⇐ᴺ (amendment, not adopted)" | Settled: not required; "an optional future theorem" |
| §1 "Readings": "its questions 1–4 … the triage carries the question"; §7 "Carried from `OWNER-QUESTIONS-r4.md`" | Settled; replace §7's first paragraph with the four answers and the citation |
| #1169 row, owner question "Amendment questions 1–4" | Settled. Replace with "None of the four remains. Open: adoption of the amended target text, which "requires an explicit owner decision"" |
| #1143 row, "type of C"; D-4, "which is amendment question 1 (type of C)" | Settled at the level of model or statistics: C is on the model. Which native data it filters (#1143's list) stays open |
| §5 item 4, "amendment question 4 (S-A or labelled protocols only)" | Settled: every physically performable experiment within C. The 2026-11-07 record agrees |
| §5 item 6, "is amendment question 3" | Settled: one model is the ultimate target, one architecture an intermediate milestone |
| Rows naming access closure (#1169, #866, #913); §6 items 5 and 8; T6 | No longer conditional: access closure is required. T6's question on its accountable home stands |
| Rows naming one "architecture" (𝔄) as the requirement | Changed: the requirement is one fixed model; one architecture is the intermediate milestone. Reword "one architecture" to "one model (architecture as milestone)" in §1, #1234, #1062, #1055, #1210, §6 items 1 and 4 |
| D-2, "a different statement from S⇐ᴺ" | Stands; necessity of C is now an optional theorem, N1/N3′ unchanged |

- **T-questions.** T2: changed (the type is settled; whether `M_OI` is the set of models
  satisfying C is still unrecorded, and the model-level reading is now the type-compatible one).
  T3: stands and is sharper: both E and C are now model-level conditions, one restricting every
  admitted model and one picking out the sector. T6: stands; its access-closure half is no longer
  conditional. T7: reworded (B2). T13: stands; answer 4 does not address confinement. T1: stands,
  with a new element (below). T8, T9, T10: unaffected. T4, T5, T11, T12: see B3 and B5.
- **Needed question now missing.** Answer 3 speaks of "every quantum carrier in the agreed scope"
  and "permitted encodings and resource requirements stated explicitly". No record states the
  agreed scope or the permitted encodings. Add: "T14. What the agreed scope of carriers and the
  permitted encodings are (#1169 c.6876591512, answer 3), and how #875 decision (a)'s qubit-power
  registers and #898's descent to every finite carrier relate to it."
- **Still proposal, and to be marked as such where used.** The amendment's own clause labels and
  definitions (I-1 to I-4, C-1 to C-5, G-1 to G-3, the two-wing interface, Fam). Add to the §2
  header: "Clause labels are those of `GATE-A-AMEND-r4.md`, a reviewed proposal that is not adopted
  as the target text; the four answers of #1169 c.6876591512 are owner decisions."

## 3. Should-fix findings

**S1. D-2: "with no counterpart among G1–G8" is wrong.** Source: memo §2.3 at `acfef447`, lines
184–191: G2 "(i) An independently meaningful physical statement, (ii) its own sourcing argument,
and (iii) at least one consequence beyond compatibility"; G6 "At least one independent prediction
or postdiction"; G7 "no knobs". Replacement: "the amendment proposal's C-1 to C-5 are stated for C
and G1–G8 for the extension X. In content G2, G6 and G7 overlap C-1 to C-3; C-4 (no narrowing of
the interface) and C-5 (nonvacuity) have no gate; G3, G4 and G8 have no clause among C-1 to C-5."
Also: the memo labels the quoted form "F2-fin(X)"; decision (a) adopts its register-scoped case.
Add decision (c), which D-2 omits: "(c) Monitored law: M1, preserved on the retained original
protocols only." It is not touched by the amendment.

**S2. D-12 and the #866 row: the amendment is silent on P0's freedom.** Source: #866 body, "What
independently justified observable carrier and additional physical structure select, constrain or
render redundant the remaining evolution freedom?"; no target record mentions it. Replacement
cell: "None to P0's question: the amendment does not mention the evolution freedom. What it adds
for #866 is context: the common model must be physically sourced, and the access rules #866 tracks
feed access closure, which is required (#1169 c.6876591512, answer 4)." Owner question: "None new."

**S3. D-7 and the #1238 row overstate the difference.** Source: `papers/Main.md`:66 on `main`, "The
framework proposes that quantum mechanics emerges for an embedded observer under the conditions
below." That is emergence under stated conditions, the shape of the sector's soundness direction;
it does not say every OI model is quantum. Only the Issue-body sentence uses "identification".
Replacement cell: "Wording only. The proposal sentence on `main` states emergence under named
conditions; it states neither inclusion nor coverage, and no record says those conditions are C.
The body's "identification" wording differs from a superset target." D-7 "Change": "the proposal
states one direction under named conditions; the target has three parts. No conflict with "Not
required" is shown for the sentence on `main`."

**S4. §5 item 2 misreads decision 9 and the standing of F2.** Source: #914 c.6563412734. "F2 is open
on all three obligations" stands under "**Standing status, unchanged by this record:**"; it is not
one of the nine numbered owner decisions. Decision 9, "**Recovery criterion.** Exact recovery
comes first …", follows decision 8 ("**P2-G.** … Exact and approximate recoverability get separate
verdicts") and sets the criterion for that recoverability audit. No record read ties it to the
exact-or-approximate form of the target. Replacement for the last sentence: "The F2 endpoint is a
standing status carried from ROADMAP, not one of that comment's nine decisions. Decision 9 there
concerns the recovery criterion of the P2-G audit and is not a counterpart of decision 2."

**S5. §5 does not say, per record, whether the owner's words are quoted and what the amendment does
to it.** Proposed table (author of every comment is the account `amaybaum`; "verbatim" means the
owner's words are quoted in the record):

| Record | Owner decision; form | Triage quotation | Effect of the amendment |
| --- | --- | --- | --- |
| #875 body, 2026-10-17, (a)–(d) | Yes; reported in the body ("adopted … explicitly, one by one"), memo marks "DEC-ADOPTED (owner, 2026-10-17)" | Exact; (c) omitted | (a) narrowed: the class-wide forward form is required on the sector unless X is read as E with C; (b) context; (c) untouched; (d) context |
| #914 F2 endpoint (body §1; c.6563412734, 2026-11-01) | Standing status, not a numbered decision | Exact | Narrowed: "removes the obligation that the OI side as a class imply QM"; adds inclusion, which F2 does not state |
| #914 c.6775022284, 2026-11-10 | Yes; verbatim instruction | Exact; the comment lists seven approaches, the triage names four | Context only; no board change authorized |
| #1169 c.6703342848, 2026-11-07 | Record that the owner "approved proceeding"; only "We do not need the hidden machinery itself to be quantum." is verbatim | Exact | Context only; agrees with answer 4 |
| #1169 c.6791556736, 2026-11-11 | Coordinator's report ("The current owner direction in ChatGPT"); no verbatim words. Confirmed by #868 c.6791606126 ("Confirm: Claude writes (Recommended)") | Exact | Context only; not contradicted |
| #1169 c.6875724719, 2026-11-14 | Yes ("I approve") | Exact | Consistent by construction |
| #1143 body: framing 2026-11-05; reformulation 2026-11-09 | Reported in the body, each labelled a research hypothesis or planning clarification | Exact | 2026-11-05 display: narrowed to the sector if `M_OI` is every admitted model. 2026-11-09: context only |
| #1216 c.6741763726 (2026-11-09), c.6775038456 (2026-11-10) | Yes; first quotes the chosen option, second reports the request | Exact; dates missing in §5 item 8 | Context only |
| #1236 c.6802597845, 2026-11-11 | Yes; verbatim "Yes, record those answers on Issue #1236" | Exact | Context only; "stand as recorded" |
| #1007 body, 2026-10-30 | Reported in the body | Exact | Context only; agrees |
| #873 c.6872998421, 2026-11-14T06:18:37Z | Yes; verbatim | Exact | Untouched |
| #868 c.6791565399 (2026-11-11), c.6854708572 (2026-11-13) | First is a coordinator's contract; second quotes "Full ladder as relayed" | Exact | Context only: stage 7 reads on the sector |
| #1238 c.6802020554, 2026-11-11 | Yes; "Proceed as suggested" to a quoted suggestion | Exact | Context only (S3) |
| #1211 c.6740537555, 2026-11-09 | Yes; verbatim | Not quoted in the triage | Context only; agrees with decision 4 |
| #1210 body, 2026-11-09 | Yes; verbatim | Exact | Context only; agrees |

No listed decision is contradicted. Two are narrowed (#875 (a), the F2 endpoint) and one
conditionally (#1143, 2026-11-05).

**S6. D-4 gives #1143 one verdict (added criterion 3).** Replace the "Superseded wording" paragraph
with a table of dispositions:

| #1143 claim or result | Disposition |
| --- | --- |
| "Keep full finite operational OI↔QM equivalence as the scientific target, with explicit model-class quantifiers." | Superseded as stated for the class of all admitted models; applicable within the sector |
| Display, first half ("For every M in M_OI, there exists T in Q with B(M) = B(T)") | Applicable within the sector (soundness); superseded if `M_OI` is every admitted model (T2) |
| Display, second half ("for every T in Q, there exists M in M_OI with B(T) = B(M)") | Still applicable (coverage), now with the witness in the sector of one model |
| "A single witness theory must match all operations and histories in scope, coherently." | Still applicable unchanged |
| Outcome 1 | Superseded as stated; applicable within the sector |
| Outcome 2 ("Proper-subclass selection") | Still applicable unchanged: a failure of coverage |
| Outcome 3 ("an OI model has no operational match in `Q`; full quantum equivalence fails") | Superseded as stated: an unmatched model outside the sector is permitted. Applicable within the sector |
| Outcome 4 | Still applicable unchanged |
| Framing of 2026-11-05 (a class of quantum theories, possibly several QFTs); Levels 2–3 | Open; not addressed by the target records |
| Reformulation of 2026-11-09: the selection question; classical-preservation controls | Still applicable; identifying the restriction is the question of identifying C. One difference to record: #1143 asks for a restriction from "OI's intrinsic consistency and access constraints", the target for a "physically justified" condition |
| "no non-quantum OI behaviours" read at the complete operational-theory level | Applicable within the sector, for every physically performable experiment (#1169 c.6876591512, answer 4) |
| #1139 witness; M-1; M-2 and C-pers (UNSOURCED); S8-A (UNSOURCED); specification verdict UNSOURCED | Still applicable unchanged at their scopes |
| SEL-ACCESS-1 (#1224); SEL-EXCL-1 (#1228) | Still applicable unchanged at their scopes, and bearing on any candidate C: the first shows passive criteria insufficient in its class, the second supplies a stronger-than-quantum control that a candidate sector must exclude. Both off `main` and not opened in this review |
| The "material failure" definition | Still applicable (a failure of coverage for the common model) |
| c.6863602000, "the *smallest target-neutral restriction*" | Open; a search for a candidate condition |

**S7. Access closure and the reverse direction were presented as fixed parts before they were.**
Now moot for access closure and for coverage (B6). Keep the marker for the proposal's own clause
labels (B6, last item).

**S8. D-19 and the #1007 row place a #914 sentence in #1007.** "`oiPlusMin_iff_qm` as the target"
is in #914 §4, not in #1007, and no record says the control "is restated". Replacement cell: "The
2026-10-30 decision and the decision of 2026-11-14 agree. Answer 3 adds that the one model "must
accommodate arbitrarily large finite carriers" (#1169 c.6876591512). #914 §4 lists
"`oiPlusMin_iff_qm` as the target" among this candidate's controls; whether that wording is kept
belongs to T1."

**S9. Statements to mark as readings or make conditional.**
- #1052 row: "outcome 3 (OI-admissible violators) is permitted outside the sector" assumes (G4) is
  part of what makes a model quantum. Replace with "outcome 3 would not by itself count against the
  target if the violators lie outside the sector; whether (G4) belongs to E or to C is not
  recorded."
- D-9: "inside the sector the laws are quantum by S⇒" → "inside the sector the laws are required
  to be quantum (soundness, open)".
- #1068 row and #913 row ("Gates map to parts"): mark *reading*.
- #1220 row: "coincides with part 1" → "is of the same kind as part 1, for a specified family".
- §6 item 5: add "(*reading*; c.6777841157 states soundness for every physically admitted
  procedure, which under the amendment is required within C)".

**S10. T7's second half is answered by the record the row cites.** #914 c.6875548603 names the
Standard Model derivation as an aim and "makes no claim" about it; the #1066 row itself says "not a
target part". Remove "and whether the Standard Model derivation is inside the target" (done in the
B2 replacement).

## 4. Nits

- **N1.** §2 row #872 quotes "no fixed finite total carrier", which is the proposal's wording. The
  owner record reads "no assumption of one fixed finite total carrier" (c.6875548603).
- **N2.** The #1169 row says seven statements; D-3 quotes five. The trace's other two are "operational
  no-signalling and exclusion of nonquantum correlations" and "avoids the former restriction while
  excluding the latter surplus" (both in the body). The body's unit table has an eighth:
  "stronger-than-quantum exclusion and common-model composition remain obligations".
- **N3.** §5 item 3: the portfolio lists seven approaches (#1169, #1143, #1211, #1059, #1210,
  #1220, #1216).
- **N4.** #1210 row, "Whether a sector condition is a B-principle": "B" here is #1210's arm B, not
  the Bell clause. Write "a principle of #1210's arm B". "have no class for a sector condition" is
  arguable: "candidate strengthened principle" could hold it.
- **N5.** §6 item 6: #970 track 6 and #903 also carry Bell-side questions.
- **N6.** §6 item 8: #1064 and #1147 also hold access prerequisites.
- **N7.** §4, #1028 and #1029: cite #1028 c.6658060093 (2026-11-05) for the retitle.
- **N8.** The #868 row's "would bear on required coverage for its class" was true before the
  amendment; say "unchanged".

## 5. Summary against the brief and the added criteria

1. **Unaffected list.** All 51 bodies read in full. Two moves (#1015, #1037), one conditional
   (#1071), one parity note (#944), two wrong reasons in §4 and §6 (#970; #1142, #1244, #1255).
2. **Affected table.** Quotations confirmed. No tier, readiness, authorization or status value is
   proposed. Nine rows and four T-questions infer ordering or priority from a change of target
   (B3, B5); five rows take the lattice branch as the common model (B2); one row misdescribes
   #914's `→Q` rows (B1).
3. **Owner decisions.** None contradicted; two narrowed, one conditionally (S5). One mis-citation
   (S4).
4. **T1–T13.** Delete T5 and T11; reduce T4 to a note; reword T7 and T12; T2, T3, T6 change under
   the 11:28Z answers; add T14.
5. **Cross-Issue links.** §6 item 1 rewritten (B2); item 3 corrected (B4); items 5, 7, 8 updated
   (B6, S9).
6. **Added criteria.** 1: §1 and B4. 2: B3. 3: S6. 4: B5. 5: B2. 6, as revised: B6.

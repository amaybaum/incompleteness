# REVIEW-QB5A-PREREG-r2: independent preregistration review of G3 QB5(a), r2

**Verdict: ACCEPT WITH CHANGES.** r2 resolves QR-1 to QR-26 in substance. Neither the decision rule (§6–§8)
nor the outcome classes need further structural change. Eleven findings remain, and each comes with
replacement text:

- Five are blocking: they must be applied before freeze. One sends a witness consideration into Stage 2.
  One leaves the blind second reading leaky. One leaves OQ-2's owner qualification only partly met. One is
  a text control that is red as written. One mixes the statuses of sourcing and non-sourcing statements.
- Six are should-fix and should be applied with them.
- Four are nits.

Once the replacement texts are applied, a check of those edits is enough; this review is the full round for
them. Freeze then waits on the owner's recorded answers and designation (OQ-5).

**Target.** Branch `research/g3-offset-873-20261113` at `c2b754afaa46be76856642f4eaf17faf94136b9c`, parent
`660152911`, fetched by branch name.

- The commit adds three files:
  - `qb5a/G3-QB5A-PREREG-r2.md` (1227 lines, "r2:n");
  - `qb5a/NOTES-QB5A-r2.md` (180 lines, "N2:n");
  - `qb5a/RESPONSE-QB5A-r1.md` (152 lines, "RESP:n").
- `660152911` adds `qb5a/REVIEW-QB5A-PREREG-r1.md`, byte-identical to the review I issued (`cmp`).
- Corpus lines refer to `main` at `c3b5f37a`.

**Method.**

- I worked by reading and hand logic only, and ran no computation on OI rules.
- I re-ran every rule-level control by hand (§2).
- I checked the locations of the new inventory lines and of the excluded search hits, by their opening
  characters only.
- I classify no inventory passage and state no expected outcome.
- As instructed, I reviewed r2 with the recommended OQ answers applied, together with the owner's two
  qualifications (OQ-2 and OQ-7). Those answers are not yet on record.

**Reviewer provenance.** As in r1: I read r5 in full when writing the r1 review. R2-6 and R2-10 concern
texts that resemble or sit near inventory sentences. In each, I propose a procedure or a neutral rewording,
never a value for an inventory passage.

***

## 1. What holds

- **QR-1 to QR-7.**
  - The role test is now independent of presentation (r2:392–404).
  - As is a commitment on both sides (r2:493–494, r2:575, r2:615).
  - Every carve is a predicate on attributes (r2:667–680).
  - The diachronic exemption is confined to F4-dia (r2:602–608).
  - The headline rule combines all coordinates (r2:776–786).
  - W-b and W-d are relabelled as consistency checks. W-e and X-18 are added.
  - TC-U has a `w*` row.
- **QR-8 to QR-26.** All are applied. GRT-4 is now operational (r2:653–662). The text controls and flips
  X5–X12 exercise the per-term tests and the sensitivities r1 lacked. The checkpoint table now measures
  every property the execution asserts, except as noted in R2-1 and R2-3.
- **I-SYM.**
  - Every clause of §6–§8 is a predicate on attribute values.
  - No carve predicate and no U cell reads A3 (r2:122, r2:587–588).
  - The witness rows get the same tests and are read twice (X-18 at Q-8).
  - The corpus's own offset rows, T-GR352 and T-GR577, are ordinary corpus rows.
- **Reachability.**
  - Every Stage-2 class and every B_G outcome is reached by a toy (§2).
  - (C) absorbs exactly what §8.5 (iv) and §8.4 say it absorbs, and that is stated.
  - R and (A) rest on universal negatives over a finite, committed list (r2:686–689).
  - §8.5 (i) states openly that (A) requires F5 to be rejected.

***

## 2. Controls, re-run by hand

| Control | Result | Note |
|---|---|---|
| RC-P (TC-R) | green | p1 is rejecting for F4, F4-law and F4-null; every carve fails GRT-1. F5 is Admissible and F4-dia Rejected. Class R; Stage 3 gives (B). |
| RC-N (TC-N) | green | Class C. F4-law and F4-null fail GRT-1. F5 and F4-dia are Admissible. Stage 3 gives (C). |
| X1 | green | n2 is rejecting for F4; class R. |
| X2 | green | p1's definiens becomes C, so U = N and the class is C. |
| X3 | green | F5 Admissible; F4 and F4-dia grounding-content; (C). |
| X4 | green | Δκ fails GRT-1; class R. |
| X5 | green | p1 leaves `Dom`; class C. |
| X6 | green | Class R, because every main-table variant is synchronic. F4-dia goes from Rejected to Admissible (slice-local gives U = N under diachronic relata). |
| X7 | green | p1 is not rejecting; class C. |
| X8 | green | Conflict with U = Y makes p1 potentially rejecting, so F4 is Undetermined; class U. |
| X9 | green | Δκ fails GRT-2; class R. |
| X10 | green | Δκ fails GRT-3; class R. |
| X11 | green | As ∈ `Com`, so n2 is rejecting; class R. Under OQ-7's fallback, n2 is potentially rejecting and the class is U. |
| X12 | green | A class {c1} that leaves out c3, which Ax-κ's reason covers, fails GRT-5; class R. |
| RC-W W-a | green (weak) | It catches a row-naming clause only. |
| RC-W W-c | green | Δ† fails GRT-1 in both forms, and GRT-5 in the row-identity form. |
| RC-W W-e | green | Δ1–Δ8 read only A1, A1c, A1q, A2, A2p and A2§, and U reads `Dom`, A2 and A2t. The check is non-vacuous where it matters: at Q-6c it tests the Δ9.k predicates, which are written at execution. |
| W-b, W-d | green, **vacuous by design** | They are correctly labelled consistency checks (r2:965–971) and are not counted as countercontrols. |
| RC-U (TC-U) | green | Stage 2 gives U, with u1's A2 named. The resolutions are: M (closing) gives R and so (B); M (slice-local) gives R, but F4-dia is Admissible and grounding-content, so (C); C gives C and so (C). They disagree, so the outcome is (C), with u1's A2 named. |
| RC-U (TC-K) | green | F4[Δk] is Undetermined, so the class is U. A pass gives (C) and a fail gives R and so (B); the outcome is (C), with GRT-4 named. |
| RC-T TX-1 to TX-4 | green | TX-4 needs "gravitate" to match "gravitates" (R2-13). |
| RC-T TX-5 | green, but must be reworded | It closely paraphrases a Group V sentence (R2-6). |
| RC-T TX-6 to TX-12 | green | The replacements TX-8, TX-10 and TX-12 test the same attribute values as the r1 sentences (§3). |
| RC-T TX-13 | **red as written** | "The Komar mass of the solution." states no evaluation of a law, so A1q's test (r2:380–381) returns no where yes is required (R2-4). |

The claim at r2:900 holds: every class and every outcome is reached [A]. Under r2:911, TX-13 is a failed
control, so the rule cannot be frozen until R2-4 is applied.

***

## 3. The writer's departures

1. **F4-dia, included and sorted at Stage 3 (r2:213–216). Acceptable.**
   - It is r5's own variant (node F4-3).
   - It has the same domain as F4. So it carves no domain, and GRT, which tests carves, does not apply to
     it.
   - It is subject to the rejecting predicates and to K1–K5, like every formalization of §3 (r2:697, r2:986).
   - It is reported beside the summary class, not inside it.
   - Omitting it would remove a grounding-content option, and including it removes a bias. It brings no new
     tilt.
   - For transparency, the headline should say whether any grid cell depends on F4-dia (R2-12, a nit).
2. **The headline covers routes as well as branches (r2:599–600, r2:778–780). Acceptable and necessary.**
   - Per-route roles (QR-1) can make Stage 2 route-dependent.
   - Treating route and branch alike under the no-selection clause is the symmetric choice.
3. **X-18 extended to A3x and to the W0 rows at Q-8. Acceptable.**
   - A3x is a decisive cell, so it should be double-read.
   - The W0 rows are read after the Stage-2 commit, so reading them cannot contaminate Stage 2.
   - The reading list remains leaky (R2-2).
4. **TX-8, TX-10 and TX-12 replaced (RESP:77–86). Acceptable, and correct.**
   - My r1 sentences resembled the witness's horizon mode count and corpus constructions. A required
     control value on a near-paraphrase pre-sets a cell.
   - Each replacement tests the same attribute value: M-set with A2p yes; M-geo; NS.
   - Applied consistently, the same criterion also catches TX-5 (R2-6).
5. **Execution nodes renumbered (Q-6a, Q-6b, Q-6c). Acceptable as numbering.** The placement of Q-6a after
   classification, however, leaves OQ-2's qualification only partly met (R2-3).
6. **Three rows added by the recorded search (G-SM120, C-GR458, C-GR468). Acceptable, with one inconsistency
   to fix.**
   - Each opens with content that bears on Q5, the same-quantity table or the definition of `ρ_E`, and each
     came from a recorded grep.
   - GR:416 and GR:458 both sit in the Corollary's subsection and both hit the search. GR:458 is added;
     GR:416 is excluded as a "lead-in" (N2:118–119). The two decisions rest on reasons that are not one
     uniform criterion.
   - The exclusion of summary and conclusion surfaces is stated only in NOTES, which do not bind the
     executor (R2-10).

***

## 4. Provenance

**The four leans of r1 are fixed.**

1. **Default for unqualified assertions.** Fixed. As is a commitment on both sides, and the fallback makes
   it potentially rejecting (r2:615, r2:1207–1214).
2. **Hedging vocabulary.** Fixed in substance. Two phrases specific to the corpus remain, "not presently
   derived" and "does not adjudicate" (r2:518–519). Both came from my own r1 list. They are covered by the
   generic stems "not derived" and "not adjudicated", so they are redundant but harmless (R2-13).
3. **D-9.** Fixed (r2:506; N2:73–75).
4. **Δ8.** Fixed. Its candidacy rests on F4's statement alone, and GRT decides it (r2:683–685).

**New leans.** None in the rule's decisive logic. Three procedural openings remain, each closed below:

- **The decoupling skeptical node (R2-1).** It refers to W0 rows at Stage 2. That asks the executor to
  anticipate witness membership before the Stage-2 commit.
- **The Δ9.k enumeration after classification (R2-3).** Writing predicates while the attribute table is
  visible leaves latitude to aim a carve.
- **The inclusion of search hits (R2-10).** The writer, who has read r5's readings, made the include and
  exclude decisions without one uniform criterion. The direction of any effect is not something this review
  assesses.

***

## 5. The owner's qualifications

- **OQ-2: "Δ9 must not become a route to a favourable exception after the result is seen".**
  - **Partly met.** r2 commits the Δ9.k list before any GRT verdict, and routes a reason that cannot be
    written on §5's attributes to the deviation procedure (r2:1038, r2:1142). A deviation never changes a
    rendered verdict (r2:1148).
  - **Not met.** Q-6a runs after Q-2. The sentences are enumerated, and their predicates written, once the
    executor can see every attribute cell. Translating a reason into a Boolean predicate is a judgment, and
    with the table in view it can be aimed.
  - R2-3 moves the enumeration before classification and adds an independent translation. A residual
    disagreement goes to the deviation procedure.
- **OQ-7: "hedged statements, conditional derivations and imported assumptions keep their distinct
  statuses; plain claims are never treated as no claim".**
  - **Met in the main.** Ps, In, ND and Op stay distinct values (r2:495, r2:536). D|cond carries its
    conditions (r2:533, r2:634). As is never Ns, under both the applied answer and the fallback.
  - **Two gaps.**
    - An assertion stated as conditional, with no D word, has no value. It falls to As and loses its
      conditions (R2-7).
    - In β1, the Ps entry "on the … proposal" turns the branch's own condition into a hedge (R2-8).
  - Note also that Conflict is an aggregate. The per-row statuses must stay visible in the table and in the
    verdict's citations (R2-15).

***

## 6. Findings

### Blocking (required before freeze; replacement text given; an edit check suffices)

#### R2-1. The decoupling skeptical node consults W0 rows at Stage 2

**Where.** r2:1045–1046; Q-7 at r2:1026; X-7 at r2:1105; I-BLIND item 4 at r2:134–135.

**Evidence.**

- "Decoupling: it makes F4, or a variant that is grounding-content with respect to a W0 row, Admissible."
- Skeptical nodes run at Q-7, before the Stage-2 commit. Whether a variant is grounding-content with respect
  to a W0 row is decided only at Q-8, from the W0 rows' attributes.
- The clause therefore has the executor anticipate the witness's classification before Stage 2 closes.
  I-BLIND item 4 forbids that. It would also put witness vocabulary into the Stage-2 text, against
  X-5(iii).

**Replacement** (r2:1045–1046):

> - **decoupling:** it makes F4, F4-dia or a carve variant Admissible or Undetermined rather than Rejected.
>   No W0 row is consulted at Stage 2 (X-7).

#### R2-2. The blind second reading can still reach r5's per-passage readings

**Where.** X-18 at r2:1116; I-BLIND item 6 at r2:138–139.

**Evidence.**

- X-18 bars r5 §0, §2.4 and §6–§9, CONFIRM-BG-r2 to r4, and NOTES-BG-r1 to r5. It leaves open several
  files and sections that state readings of inventory passages:
  - r5 §1.3, which gives F4-c candidate verdicts that name GR:426 and partition-definedness (r5:215–223);
  - r5 §3.4, on GR:374, GR:400, GR:633 and GR:354 (r5:439–447);
  - r5 §4.2, which sorts passages into consistent with co-constraint or with grounding (r5:480–486);
  - unit 2(a)'s record, which reads GR:374, GR:378 and GR:400 (for example U2Ar3:333–338 and :690–693);
  - REVIEW-BG-r1, RESPONSE-BG-r1 to r4, and the unit 1 reviews.
- A list of exclusions will always miss some file. A list of inclusions does not.
- The tests the second reader applies need no definitions beyond r2 §2.1, §3 and §5.

**Replacement** for the third and fourth sentences of X-18's checkpoint cell:

> The second reader is a different agent from the executor. Before the Stage-2 commit it reads only the
> frozen preregistration and the corpus at `c3b5f37a`. It reads no other file of the programme directory:
> no record, review, confirmation, response or notes file of units 1, 2(a) or 2(b), and none of this
> unit's NOTES, RESPONSE or REVIEW files. At Q-8 it may also read the definition lines §4.4 cites. It
> classifies the text controls first.

In I-BLIND item 6, replace "without having read r5's per-passage readings" with "reading only the frozen
preregistration and the corpus (X-18)".

#### R2-3. The Δ9.k enumeration runs after classification (OQ-2's qualification)

**Where.** r2:1021, r2:1023, r2:1031–1039; X-19 at r2:1117; I-BLIND item 1 at r2:126–129.

**Evidence.** See §5, OQ-2. Enumerating the sentences is lexical and needs no cell, so it can run before
Q-2. Translating each sentence into a predicate on §5's attributes defines a class; it does not read cell
values. Done before classification, by two readers, the step leaves no room to aim a carve at a known
table.

**Replacement.**

1. Move Q-6a to a new node, **Q-1b**, between Q-1 and Q-2, and replace its text (r2:1031–1039) with:

   > **Q-1b (enumeration and translation, committed before any row is classified).**
   > - List every sentence of a §4.2 row that contains a reason connective ("because", "since",
   >   "therefore", "hence", "so", "in virtue of", "as a consequence", "is a property of … and
   >   therefore"), and whose conclusion is that a quantity does or does not source, gravitate, ground or
   >   enter the field equation.
   > - The executor and the second reader (X-18) each write, independently, the predicate each sentence
   >   induces as a Boolean combination of §5's attributes. They do not consult each other or any
   >   attribute cell.
   > - They reconcile once, by citation. A predicate both writers agree on, and that equals one of
   >   Δ1–Δ8's, is merged with it. Any other agreed predicate is a Δ9.k.
   > - A sentence whose predicate stays in disagreement, or cannot be written on §5's attributes, is a
   >   deviation (§14.2), with a sensitivity line. It is not a Δ9.k, and it never changes the frozen rule.
   > - The list and both translations land in a commit before Q-2.

2. Make these consequential edits:
   - In Q-4 (r2:1021), replace "any stated reason for a scope (an input to Q-6a)" with "the Δ3 and Δ4
     reasons as committed at Q-1b".
   - In X-19, replace "the Δ9.k list (Q-6a) lands before any GRT verdict" with "the Δ9.k list and both
     translations (Q-1b) land before any row is classified".
   - In I-BLIND item 1 and in X-6(iii), replace "Q-6a" with "Q-1b".
   - In W-e (r2:963–964), replace "after the Δ9.k list is committed" with "on the Δ9.k list committed at
     Q-1b".

#### R2-4. TX-13 is red as written

**Where.** r2:1008; A1q at r2:380–381; r2:417.

**Evidence.** A1q is yes only if "a passage states the quantity's value or identity as obtained by evaluating
a law of the gravitational dynamics … on a given solution". "The Komar mass of the solution." states no
such evaluation. On a literal reading it returns no, so the control fails (r2:911). The defect is in my own
r1 sentence.

**Replacement.**

- Replace TX-13's sentence with:

  > "The mass of the Schwarzschild solution, obtained by evaluating the field equation on that solution and
  > integrating over a sphere at infinity (the Komar mass)."

  Keep its required values, "A1q yes; no role T".

- At r2:417, add after "The Komar mass of a Schwarzschild solution": "stated as obtained by evaluating the
  field equation on that solution".

#### R2-5. Non-sourcing statements: mixed statuses, and asymmetric effects of hedges

**Where.** r2:399–401 (NS); r2:405–409 (role aggregation); r2:527–536 (A3 aggregation).

**Evidence.**

- **Mixed statuses.** An NS row's status is "read by §5.3, with 'non-sourcing' in place of 'source role'"
  and stored in A3. A3's aggregation then pools it with the statuses of T rows on the same quantity. A
  committed sourcing statement and a hedged non-sourcing statement would aggregate to Conflict, although
  neither hedges the other.
- **Asymmetric hedges.** "T and NS on one quantity give Conflict-R" whatever the statuses. A hedged NS row
  can therefore make `Dom` membership Und and turn a determinate rejection into U. A hedged T row has no
  matching effect on a committed NS row.
- **IC with NS.** IC and NS on one quantity give IC, so the non-sourcing statement is discarded. That is the
  defect QR-12 removed for T.
- These are flaws in my own QR-12 text.

**Replacement.**

1. NS bullet (r2:399–400):

   > - **NS** if a passage states that the quantity does not source, gravitate or enter the field equation.
   >   Its status is recorded in **A3n**, read by §5.3 with "non-sourcing" in place of "source role". A3
   >   aggregates only the rows that give T or IC; A3n aggregates only the rows that give NS.

2. Role aggregation (r2:406–409):

   > - Let a role be committed when its aggregated status (A3 for T or IC, A3n for NS) is a commitment value
   >   (§5.3) or Conflict.
   > - If T or IC is committed and NS is committed, the role is Conflict-R, and `Dom(v)` membership is Und,
   >   unless the two are scoped to different branches (§6.1).
   > - Otherwise the committed role prevails, with IC over T. If no role is committed: IC if any row gives
   >   IC; else T if any row gives T; else NS if any row gives NS; else Dep; else N.

3. Add A3n to X-18's list of cells, and to X-5(i).

### Should-fix

#### R2-6. TX-5 closely paraphrases a Group V sentence, and the role of a question-form passage is unset

**Where.** r2:1000, r2:551; r2:275.

**Evidence.**

- TX-5, "Whether the axion background sources curvature is not settled here", follows almost word for word
  the clause that §4.2 locates in T-GR577 ("Whether the offset sources curvature is not settled",
  r2:275).
- The writer's own criterion replaced TX-8, TX-10 and TX-12 for less (RESP:77–86). It applies here with
  more force, because T-GR577 is a row of the disputed vacuum-offset coupling.
- TX-5 also fixes no A1 value. The lexical T trigger "says it 'sources'" fires on the word even inside an
  open question.

**Replacement.**

- TX-5 and its §5.3 example (r2:551):

  > "The coupling of the axion background to spacetime curvature remains an open problem in this model."
  > Required: A3 Op; A1 not fixed by this sentence.

- Add to §5.1's test, after the NS bullet:

  > - A passage that states only that whether the quantity sources is open gives no role value. The role is
  >   taken from the other rows on the quantity, and is Und if none gives one. The passage's status is
  >   recorded in A3.

#### R2-7. A conditional assertion with no D word has no value (OQ-7's qualification)

**Where.** r2:492, r2:512–513, r2:527–535, r2:615.

**Evidence.**

- D|cond requires a D word. A sourcing statement made "conditional on …" with no D word therefore falls to
  As, and its conditions are lost. "Conditional" is in AGENTS.md §A.25's status vocabulary.
- OQ-7's qualification requires conditional claims to keep their own status.

**Replacement.**

- In the word map (r2:512–513):

  > - **D|cond:** a D word with "conditional on …" or "under …" naming conditions, or an inherited status
  >   note naming conditions.
  > - **As|cond:** an assertion with no D word, stated as conditional on named conditions ("conditional on
  >   …", "given …", "under …").

- Add As|cond to the commitment values (r2:527) and to `Com` (r2:615). In the aggregation, read "D|cond or
  As|cond, with the union of the named conditions".
- Extend the labels at r2:632–635 so that a rejection resting on As|cond carries both its conditions and the
  "rests on unqualified assertion" label.
- Under OQ-7's fallback, As|cond joins As in the potentially rejecting clause.

#### R2-8. In β1, the geometry-first phrase is both the branch condition and a Ps hedge

**Where.** r2:597–598; Ps at r2:515–516.

**Evidence.**

- A statement made "on the geometry-first proposal" enters β1 only. In β1 that proposal is in force by the
  branch's definition.
- The Ps entry "on the … proposal" would still classify the same words as a posit. Two readers can then
  give Ps or the statement's other status in β1.

**Replacement.** Add to §6.1's geometry-first bullet:

> In β1, the phrase placing the statement on the geometry-first proposal, or on §8.3's identification, is
> the branch condition, not a Ps hedge. The statement's status is read from its remaining status words,
> with that condition recorded among its conditions.

#### R2-9. Group K passages with excluded clauses must all be split

**Where.** r2:319–322.

**Evidence.**

- GR:340 is split by sentence, but K-GR342 is one row with "its excluded clauses: A3x = yes". GR:342 also
  carries N3-G's premise clause, "QM is emergent" (r2:152).
- With A3x = yes the row's non-excluded clauses are lost. With A3x = no its excluded clauses could decide a
  step.
- K-Sub385, K-Sub387 and K-Sub389 each mix separation clauses with other content.

**Replacement** (r2:314–315 and r2:319–322):

> Every Group K passage that contains a clause on §2.2's list is split into the excluded clause or clauses
> (A3x = yes, by §5.3's rule) and the remainder (a row of its own). This applies to K-GR340, K-GR342 and
> K-Sub385 to K-Sub389.

#### R2-10. Summary surfaces and search hits need one binding criterion in the preregistration

**Where.** N2:113–119 (the exclusions); r2:303, r2:306 (C-GR418, C-GR458); §4.5.

**Evidence.**

- GR:26, :549, :703 and :705 are excluded as "propagation surfaces". The executor is told that "a status
  disagreement seen there is recorded as a finding", but only in NOTES, which do not bind execution.
- GR:416 and GR:458 sit in the same subsection, and both hit the search. One is added, the other excluded,
  for reasons that do not form one criterion.
- AGENTS.md §A.25 treats summaries and conclusions as surfaces that must agree with the body. A binding,
  non-decisive treatment keeps them visible without letting them decide.

**Replacement.**

- Add C-GR416 to Group C, with the reason "the Corollary's lead-in; same subsection as C-GR418 and
  C-GR458".
- Add to §4.2:

  > **Group P: propagation surfaces (not decisive).** GR:26, GR:549, GR:703 and GR:705. They are classified
  > at Q-2, and by the second reader, like every row. They do not enter the decisive table. Every verdict
  > states whether it would differ with them included (a sensitivity line). A status that differs from the
  > aggregate of the decisive rows on the same quantity is recorded as a finding.

- In X-4, add "Group P rows appear only in the sensitivity lines".

#### R2-11. §15's alternatives: one is incomplete and one is not neutral

**Where.** r2:1168–1214.

- **OQ-1's alternative is incomplete.** It also needs these edits:
  - its exemption clause should read "are not rejecting and not potentially rejecting for any F4
    variant";
  - X-10's last sentence (r2:1108) is deleted;
  - an exception is added to I-SYM's "None names a row" (r2:120–121): "except the QB7(a) exemption of
    §2.2, adopted by owner decision".

  Without these, the alternative contradicts I-SYM and X-10 at once.
- **OQ-2's alternative is incomplete.** If F4-law and F4-null are not subject to GRT, an admissible F4-null
  with no stated reason would satisfy Cc ("an F4-c class specified that passes the grounding-relevance
  test") without passing that test. It also needs these edits:
  - in §8.2, add "F4-law and F4-null count as carve variants for R and U only, not for Cc";
  - in §9 (r2:814–815, :846 and :894), delete "Rejected by GRT-1" for F4-law and F4-null, replacing it with
    the verdicts from their rows. The toy outcomes are unchanged: I re-ran TC-N and TC-A under the
    alternative and get (C) and (A).
  - Add a note that no alternative to the finite-list relativity is offered: an open schema makes R and
    (A) unreachable (CONFIRM-BG-r4 DF-2).
- **OQ-3's alternative is not neutral.** It drops from Stage 3 an admissible carve whose class contains the
  witness's term, which would be CoC-content. It still counts a carve whose class leaves the witness's term
  in its domain, which is grounding-content. Only one side is removed, which favours (A) and (C) over (B).
  Replace it with:

  > In §3, replace the sorting bullets with: "Carve variants F4[Δ] are reported at Stage 3 and counted on
  > neither side." In §8.5 (v), delete both consequences.

- **OQ-4, OQ-5 and OQ-7.** Their alternatives are complete and minimal.

### Nits

- **R2-12. F4-dia's weight in the headline** (r2:776–786). Add to §8.4: "The headline states whether any
  grid cell's outcome changes if F4-dia is omitted."
- **R2-13. Word map matching** (r2:510–519). Add "Words match by stem and inflection ('gravitate' matches
  'gravitates')." Drop "not presently derived" and "does not adjudicate", which "not derived" and "not
  adjudicated" cover.
- **R2-14. Wording of X-7 and the inventory.**
  - X-7 (r2:1105): replace "whose tree has no W0 classification" with "in which the unit's record files
    contain no W0 classification". The branch tree contains the unit 2(a) and r5 records.
  - The inventory's "A3x = yes" notes (r2:292, r2:319–322) follow mechanically from §2.2 and §5.3. Write
    them as "on §2.2's list", so that §4 renders no cell (X-15).
- **R2-15. Per-row statuses are kept** (r2:530–531). Add: "Each row's own status stays in the table and in
  the verdict's citations; Conflict is the per-quantity aggregate only."

***

## 7. Owner questions, with the recommended answers applied

- **OQ-1.** The writer's reading stands, with the sensitivity line (r2:728–731). Complete once R2-11 is
  applied to the alternative.
- **OQ-2.** Accept, subject to the owner's qualification, which R2-3 makes fully met.
- **OQ-3.** Accept. The recommended text is symmetric (§8.5 (v), both mirror consequences). Its alternative
  needs R2-11.
- **OQ-4.** Accept, with R2-9 and R2-10.
- **OQ-5.** The owner designates F on #873 after this acceptance is recorded, and after the edits are checked.
- **OQ-6.** Answered (c.6872277416).
- **OQ-7.** Accept, subject to the owner's qualification, which R2-7, R2-8 and R2-15 make fully met.

***

## 8. Disposition

**ACCEPT WITH CHANGES.**

- **Before freeze:**
  - apply R2-1 to R2-5;
  - apply R2-6 to R2-11 with them;
  - apply the nits R2-12 to R2-15 as convenient.
- **Check.** A check of the edits against the replacement text is enough. This review is the full round for
  every text it supplies.
- **Then:** re-run TX-5 and TX-13 as reworded at Q-0. The owner records the answers to OQ-1 to OQ-5 and
  OQ-7, and designates F.

No inventory passage is classified in this review, and no expected outcome is stated. No manuscript change
is proposed, and no premise is adopted.

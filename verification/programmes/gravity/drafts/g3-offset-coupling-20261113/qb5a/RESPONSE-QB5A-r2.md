# RESPONSE-QB5A-r2: dispositions for REVIEW-QB5A-PREREG-r2

**Target.** `qb5a/REVIEW-QB5A-PREREG-r2.md` at `c006bf2a` (ACCEPT WITH CHANGES), reviewing
`qb5a/G3-QB5A-PREREG-r2.md` at `c2b754af`.

**Result.** `qb5a/G3-QB5A-PREREG-r3.md`, 1273 lines, cited as "r3:n". r2 is not edited.

**How the findings are applied.**

- All fifteen findings are applied: R2-1 to R2-11 and the nits R2-12 to R2-15.
- The review's replacement text is used verbatim, apart from the two changes listed under §3: a blank line
  after the Q-1b heading, and the bookkeeping edits.
- Nothing outside these findings is changed, apart from the bookkeeping edits listed in §3.
- OQ-1 to OQ-5 and OQ-7 remain marked "(pending owner decision OQ-n)".
- No inventory passage is classified, and no outcome is predicted.

***

## 1. Blocking findings

### R2-1. The decoupling skeptical node

Replacement text:

> - **decoupling:** it makes F4, F4-dia or a carve variant Admissible or Undetermined rather than Rejected.
>   No W0 row is consulted at Stage 2 (X-7).

**Now at** r3:1085–1086.

### R2-2. The blind second reading: an inclusion list

X-18, third and fourth sentences:

> The second reader is a different agent from the executor. Before the Stage-2 commit it reads only the
> frozen preregistration and the corpus at `c3b5f37a`. It reads no other file of the programme directory:
> no record, review, confirmation, response or notes file of units 1, 2(a) or 2(b), and none of this
> unit's NOTES, RESPONSE or REVIEW files. At Q-8 it may also read the definition lines §4.4 cites. It
> classifies the text controls first.

**Now at** r3:1156, the X-18 cell.

I-BLIND item 6: "reading only the frozen preregistration and the corpus (X-18)". **Now at** r3:142–143.

### R2-3. The Δ9.k enumeration moves to Q-1b

The new node:

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

**Now at** r3:1066–1079. Its table row is at r3:1053, between Q-1 and Q-2. The old Q-6a row is
removed.

Consequential edits:

| Edit | Text | r3 |
|---|---|---|
| Q-4 | "the Δ3 and Δ4 reasons as committed at Q-1b" | r3:1057 |
| X-19 | "the Δ9.k list and both translations (Q-1b) land before any row is classified" | r3:1157 |
| I-BLIND item 1 | "Q-6a" → "Q-1b" (with "any GRT verdict" → "any row is classified", to match X-19) | r3:130–132 |
| X-6(iii) | "Q-6a" → "Q-1b" | r3:1144 |
| W-e | "on the Δ9.k list committed at Q-1b" | r3:999 |

Two further consequential edits replace "Q-6a" with "Q-1b", so that no reference to the removed node
survives: the §7.2 Δ9.k row (r3:713) and the §14.2 deviation bullet (r3:1182).

### R2-4. TX-13 is red

TX-13's sentence:

> "The mass of the Schwarzschild solution, obtained by evaluating the field equation on that solution and
> integrating over a sphere at infinity (the Komar mass)."

Its required values are kept: A1q yes; no role T. **Now at** r3:1043.

§5.1's example gains "stated as obtained by evaluating the field equation on that solution". **Now at**
r3:439–440.

### R2-5. Non-sourcing statements

1. The NS bullet:

   > - **NS** if a passage states that the quantity does not source, gravitate or enter the field equation.
   >   Its status is recorded in **A3n**, read by §5.3 with "non-sourcing" in place of "source role". A3
   >   aggregates only the rows that give T or IC; A3n aggregates only the rows that give NS.

   **Now at** r3:415–417.

2. Role aggregation:

   > - Let a role be committed when its aggregated status (A3 for T or IC, A3n for NS) is a commitment value
   >   (§5.3) or Conflict.
   > - If T or IC is committed and NS is committed, the role is Conflict-R, and `Dom(v)` membership is Und,
   >   unless the two are scoped to different branches (§6.1).
   > - Otherwise the committed role prevails, with IC over T. If no role is committed: IC if any row gives
   >   IC; else T if any row gives T; else NS if any row gives NS; else Dep; else N.

   **Now at** r3:426–431.

3. A3n is added to X-18's list of cells and to X-5(i). **Now at** r3:1156 and r3:1143.

***

## 2. Should-fix findings

### R2-6. TX-5 and the question-form passage

TX-5:

> "The coupling of the axion background to spacetime curvature remains an open problem in this model."
> Required: A3 Op; A1 not fixed by this sentence.

**Now at** r3:1035, and at r3:580–581 as §5.3's example.

The bullet after NS:

> - A passage that states only that whether the quantity sources is open gives no role value. The role is
>   taken from the other rows on the quantity, and is Und if none gives one. The passage's status is
>   recorded in A3.

**Now at** r3:418–420.

### R2-7. As|cond

Word map:

> - **D|cond:** a D word with "conditional on …" or "under …" naming conditions, or an inherited status
>   note naming conditions.
> - **As|cond:** an assertion with no D word, stated as conditional on named conditions ("conditional on
>   …", "given …", "under …").

**Now at** r3:536–539.

Other edits:

| Edit | r3 |
|---|---|
| As|cond added to the values list | r3:518 |
| As|cond added to the commitment values | r3:554–555 |
| As|cond added to `Com` | r3:648 |
| Aggregation: "D|cond or As|cond … with the union of the named conditions" | r3:560 |
| Labels: an As|cond rejection carries its conditions and the "rests on unqualified assertion" label | r3:665–669 |
| OQ-7's fallback: As|cond joins As in the potentially rejecting clause | r3:1256–1259 |

### R2-8. The β1 branch condition is not a Ps hedge

> In β1, the phrase placing the statement on the geometry-first proposal, or on §8.3's identification, is
> the branch condition, not a Ps hedge. The statement's status is read from its remaining status words,
> with that condition recorded among its conditions.

**Now at** r3:628–631.

### R2-9. Split the Group K passages

> Every Group K passage that contains a clause on §2.2's list is split into the excluded clause or clauses
> (A3x = yes, by §5.3's rule) and the remainder (a row of its own). This applies to K-GR340, K-GR342 and
> K-Sub385 to K-Sub389.

**Now at** r3:319–321. The table is re-cut accordingly at r3:323–333:

- GR:340 s.1 splits into ·s1x and ·s1r; s.2 is its own row;
- GR:342 splits into ·x and ·r;
- Substratum.md:385, :387 and :389 each split into ·x and ·r.

### R2-10. Group P and C-GR416

C-GR416: "the Corollary's lead-in; same subsection as C-GR418 and C-GR458". **Now at** r3:307.

> **Group P: propagation surfaces (not decisive).** GR:26, GR:549, GR:703 and GR:705. They are classified
> at Q-2, and by the second reader, like every row. They do not enter the decisive table. Every verdict
> states whether it would differ with them included (a sensitivity line). A status that differs from the
> aggregate of the decisive rows on the same quantity is recorded as a finding.

**Now at** r3:335–338.

X-4: "Group P rows appear only in the sensitivity lines". **Now at** r3:1142.

### R2-11. The §15 alternatives

**OQ-1's alternative** (r3:1213–1220):

- "are not rejecting and not potentially rejecting for any F4 variant";
- "Delete X-10's last sentence";
- the I-SYM exception, "except the QB7(a) exemption of §2.2, adopted by owner decision".

**OQ-2's alternative** (r3:1227–1235):

- "F4-law and F4-null count as carve variants for R and U only, not for Cc";
- the §9 edits, with the toy outcomes unchanged ((C) for TC-N, (A) for TC-A);
- the note that no alternative to the finite-list relativity is offered (CONFIRM-BG-r4 DF-2).

**OQ-3's alternative** (r3:1239–1240):

> In §3, replace the sorting bullets with: "Carve variants F4[Δ] are reported at Stage 3 and counted on
> neither side." In §8.5 (v), delete both consequences.

***

## 3. Nits, and edits outside the findings

**Nits.**

| Nit | Text | r3 |
|---|---|---|
| R2-12 | "The headline states whether any grid cell's outcome changes if F4-dia is omitted." | r3:820 |
| R2-13 | "Words match by stem and inflection ('gravitate' matches 'gravitates')." "not presently derived" and "does not adjudicate" are dropped | r3:546; ND r3:544; Op r3:545 |
| R2-14 | X-7: "in which the unit's record files contain no W0 classification" | r3:1145 |
| R2-14 | The inventory's "A3x = yes" notes become "on §2.2's list": E-GR575 and the Group K rows | r3:296; r3:325–333 |
| R2-15 | "Each row's own status stays in the table and in the verdict's citations; Conflict is the per-quantity aggregate only." | r3:564–565 |

R2-9's rule sentence keeps "(A3x = yes, by §5.3's rule)" verbatim (r3:320). It states a rule, not a cell.

**Edits outside the findings.** These are bookkeeping only.

- The title is "r3" (r3:1).
- Two revision-history bullets name r2, its review and r3 (r3:27–30).
- "r2 carries" becomes "r3 carries" (r3:31).
- OQ-4's applied answer now lists R2-10's additions (r3:1242–1244), so that it stays consistent with
  §4.2.
- A blank line follows the Q-1b heading (r3:1067).

***

## 4. r2 → r3 diff summary

The `diff` has 42 hunks. Every hunk maps to a finding above or to the bookkeeping list in §3.

| Area | r2 | r3 |
|---|---|---|
| Stage 2 and the witness | The decoupling skeptical node referred to W0 rows | It names F4, F4-dia and carve variants only; no W0 row is consulted (R2-1) |
| Second reader | Exclusion list | Inclusion list: the frozen preregistration and the corpus only; the §4.4 definition lines at Q-8 (R2-2) |
| Δ9.k | Enumerated at Q-6a, after classification, by the executor alone | Enumerated at Q-1b, before classification, translated independently by the executor and the second reader, with disagreements sent to deviations (R2-3) |
| Text controls | TX-13 red; TX-5 a near-paraphrase of T-GR577 | TX-13 states the evaluation; TX-5 reworded (R2-4, R2-6) |
| Non-sourcing | One status cell; Conflict-R regardless of status; IC discarded NS | A3n; status-respecting role aggregation; a question-form passage gives no role (R2-5, R2-6) |
| Status values | No conditional assertion; the β1 phrase read as Ps | As|cond, added to `Com`; the β1 phrase is the branch condition (R2-7, R2-8) |
| Word map | Two corpus-specific hedge phrases; no matching rule | Both dropped; stem and inflection matching (R2-13) |
| Per-row statuses | Implicit | Kept in the table and citations (R2-15) |
| Inventory | K-GR342 and K-Sub385–389 unsplit; GR:416 and the summary surfaces handled only in NOTES; the "A3x = yes" notes in §4 | All split; C-GR416 added; Group P binding and non-decisive; the notes read "on §2.2's list" (R2-9, R2-10, R2-14) |
| Headline | Silent on F4-dia's weight | States whether any cell changes without F4-dia (R2-12) |
| X-7 | "whose tree has no W0 classification" | "in which the unit's record files contain no W0 classification" (R2-14) |
| §15 alternatives | OQ-1 and OQ-2 incomplete; OQ-3 one-sided | Complete and neutral (R2-11) |

Not changed: §6.2, §7.1, §8.1–§8.3, §8.5, §9, §10.1–§10.6 apart from W-e's node reference, §12 and §16.

**Before freeze, per REVIEW-QB5A-PREREG-r2 §8.**

- A check of these edits against the replacement texts.
- TX-5 and TX-13 re-run as reworded, at Q-0.
- The owner's recorded answers to OQ-1 to OQ-5 and OQ-7, and the owner's designation of F.

# CONFIRM-QB5A-PREREG-r4: check of G3 QB5(a) r4 at `3607d5f9`, the CF3 edits and the owner's answers

**Verdict: ACCEPT WITH CHANGES.**

- **CF3-1 and CF3-2.** Applied verbatim.
- **Marker resolution.** It changes only the citations, the §0 summary, the freeze bullet, the history and
  §15. Every quotation matches #873 c.6872827835 exactly.
- **Remaining defects.**
  - **CF4-1** (OQ-1). The sensitivity line falls short of the owner's decision. This is required.
  - **CF4-2** (OQ-7). The decision's last sentence is missing from the rule text. This is required.
  - **CF4-3** (§14.1). One line is stale and would be frozen into F. This is required.
  - **CF4-4** (OQ-5). The acceptance chain should be named. This is should-fix.
  - **CF4-5.** A nit.
- **OQ-2.** Its qualification is met; no change is needed.

Each change has exact replacement text, and each affects only reporting or bookkeeping: no decision clause,
test or control changes. Once they are applied, a check of the edits against the text below is enough, and
an ACCEPT on that head gives the SHA to post for the owner's designation of F. Head `3607d5f9` itself is
not ready for designation.

**Target.** Branch `research/g3-offset-873-20261113` at `3607d5f98feea7565a2bfd23e23e569ddeb5bcfd`, fetched by
branch name.

- **Parent `2afc1c3373a7c339c7fb28b98010f220bdbc7075`.** It adds:
  - `qb5a/G3-QB5A-PREREG-r4.md`;
  - `NOTES-QB5A-r4.md`;
  - `RESPONSE-QB5A-r3.md`;
  - `CONFIRM-QB5A-PREREG-r3.md`, byte-identical to the check I issued (`cmp`).
- **`3607d5f9`.** It edits `G3-QB5A-PREREG-r4.md` in place (1332 lines, "r4:n" below) and `NOTES-QB5A-r4.md`.
- **Comparisons.** "r3" is the file at `4a157f19`. "r4a" is r4 at `2afc1c33`.

**Method.**

- I compared the files hunk by hunk.
- I read the owner's comment first-hand (#873 c.6872827835, `amaybaum`, 2026-11-14T06:05:54Z). I checked
  each quotation against it as an exact string match over the line-joined text.
- I re-ran the affected controls by hand.
- No classification, no prediction, no computation on OI rules, and nothing written to the repository.

***

## 1. CF3-1 and CF3-2 (r3 → r4a: 7 hunks)

| Item | r4 | Check |
|---|---|---|
| CF3-1 (1), the Group P sentence | r4:341–345 | verbatim |
| CF3-1 (2), X-4 | the X-4 cell | verbatim ("§4.2 less Group P, together with §4.4") |
| CF3-1 (3), the A3x bullet | after the A3x bullets of §5.3 | verbatim |
| CF3-2 (1), I-SYM | r4:130–132 | verbatim |
| CF3-2 (2), §6's opening | r4:628 | verbatim |
| Title and history | r4:1, r4:32–35 | bookkeeping only |

No hunk falls outside these.

**Controls.**

- Only X7 touches CF3-1. With A3x = yes, TC-R's p1 now enters no aggregation and no rejecting predicate, so
  it neither rejects nor sits in a domain. F4 is Admissible and the class is C, as required: **green**.
- No toy uses Group P. CF3-2 is wording only. W-e's rows are single-row quantities.
- Every other control is unchanged from CONFIRM-QB5A-PREREG-r3 §2: all green. W-b and W-d remain vacuous
  consistency checks by design.

***

## 2. Marker resolution (r4a → r4 at `3607d5f9`: 18 hunks)

**Scope.** Every hunk falls in one of these places:

- the history (r4:36–39);
- the §0 summary (r4:89–90);
- a citation replacing a marker (r4:197, :229, :617, :660, :734–735, :774–777, :839–840, :844–845, :985);
- the freeze bullet (r4:1186–1188);
- §15 (r4:1218–1315).

At r4:985, X11's text "under the fallback, not adopted, U" is a citation edit and stays within scope. No
"pending owner decision" marker remains. The one other occurrence of "pending" (r4:259) is inside a quoted
corpus phrase. NOTES-QB5A-r4 §7's table of lines agrees with the diff.

**Quotations.** These all match c.6872827835 exactly:

- the owner's confirmation sentence;
- the OQ-1 to OQ-5 and OQ-7 decisions;
- OQ-6's "Already answered; no new decision.";
- the OQ-2 and OQ-7 qualifications;
- the confirmation's freeze sentences.

**Applied texts.** They are unchanged from r3. Each alternative is marked "not adopted; record only".

***

## 3. The gaps the writer reported

### OQ-1. A real gap; required (CF4-1)

**What the decision says.** The decision reads "Report sensitivity whenever their treatment changes the
verdict." The running-vacuum rows' treatment reaches a verdict through more than their A3 cells:

- their role, which sets domain membership;
- GRT-4, where a running-vacuum row can fail or undetermine a carve;
- the aggregation on their quantity, through Conflict and Conflict-R;
- any Δ9.k drawn from their sentences.

**What r4 reports.** The §8.2 line (r4:774–777) reports only one direction: their A3 cells set
non-committal. The counterfactual in the other direction, those rows taken as committed sources, is the
subject of QB7(a), and r5 reported exactly that consequence (r5:643–650). Reporting it adopts nothing, so
long as it is labelled as a counterfactual and is never the rendered verdict.

**The fix.** Report both directions, together with complete removal. That bounds the rows' influence
without selecting a direction.

### OQ-2. Met; no change

The decision asks for "mechanically defined predicates and no open-ended carve-out selection during verdict
assessment", with Δ9 instances "enumerated and committed before applying the grounding tests". Under r4:

- Every Δ1–Δ8 is a Boolean predicate on §5 attribute values (§7.2).
- Every Δ9.k is committed as such a predicate at Q-1b, before any row is classified and so before any
  grounding test (r4 Q-1b; X-19). Once committed, every predicate is evaluated mechanically.
- The one step of judgment is translating a sentence into a predicate. It happens before any cell or verdict
  exists, two readers do it independently, and a disagreement goes to the deviation procedure, never into
  the rule (Q-1b; §14.2).
- No carve can be selected during verdict assessment: one found later is a deviation (I-BLIND item 1).
- The owner's safeguard, "Δ9 cannot become a way to invent a favourable exception after seeing the result",
  is therefore met by construction. "Mechanically defined" is met in the sense that matters: what is frozen
  and applied is a mechanical predicate.

### OQ-7. Required (CF4-2)

The sentence "This is not independent physical verification of the assertion" belongs to the decision
itself. It limits what a labelled verdict means. It appears only in §15's quotation, and §15 is a record.
The label at §6.3 and the limits at §16 are where a reader of a verdict will look, so the sentence belongs
there.

### The stale line at r4:1184. Required (CF4-3)

"An owner answer to a pending OQ is applied by the alternative text of §15" describes a procedure that no
longer exists: no OQ is pending, and no alternative is adopted. F freezes this file, so a stale procedural
sentence would be frozen with it. Replace it.

### OQ-5. Handled correctly in substance; should-fix (CF4-4)

The decision names "the complete r2 rule and its controls". The confirmation adds "The preregistration must
first reach r4, with CF3-1 and CF3-2 applied and independently confirmed", and "Once that check returns
ACCEPT, provide the exact r4 commit SHA."

The freeze bullet (r4:1186–1188) states both, and r2's full-round review is that acceptance of the complete
r2 rule. The bullet should name the chain and say which commit F is, so that X-3 can be checked against it.

***

## 4. Findings and replacement text

### Required

#### CF4-1. The QB7(a) sensitivity must cover every way the running-vacuum rows reach a verdict

**Where.** r4:774–777 (§8.2); r4:197 (§2.2); X-10 at r4:1160.

**Replacement.**

1. Replace r4:774–777 with:

   > - **QB7(a) sensitivity (owner decision OQ-1, #873 c.6872827835).** Let RV be the rows that the
   >   same-quantity table identifies with GR:376's `Λ_eff(H)` or with GR:400 Reading 1's quantity. Each
   >   Stage-2 verdict, and each cell of the Stage-3 grid, is recomputed three ways, with every other row as
   >   rendered:
   >   - (i) every A3 cell of RV non-committal (Ns);
   >   - (ii) RV taken as committed sources, with role T and A3 = D, and their other cells as rendered. This
   >     is a counterfactual, never the rendered verdict: running-vacuum sourcing is not adopted (QB7(a));
   >   - (iii) RV removed from every decisive step: the rejecting predicates, the aggregations of §5.1 and
   >     §5.3, GRT-4, and any Δ9.k drawn only from RV's sentences.
   >
   >   Wherever any of the three differs from the rendered result, the verdict is reported with the differing
   >   results beside it, labelled "sensitive to the running-vacuum rows (QB7(a))". Where (i) differs, it is
   >   also labelled "rests on the corpus text's commitment to running-vacuum sourcing (QB7(a))".

2. At r4:197, replace "§8.2 carries the QB7(a) sensitivity line." with "§8.2 carries the QB7(a)
   sensitivity."
3. In X-10's checkpoint cell, replace "The §8.2 sensitivity line is present wherever it applies" with:

   > The three §8.2 sensitivity computations are recorded for every verdict, and the label is present
   > wherever one differs. The reviewer recomputes them (X-21).

4. In Q-7's row (r4:1073), replace "the QB7(a) sensitivity line" with "the QB7(a) sensitivity".
5. At r4:1231 (§15, OQ-1, text applied), replace "§8.2's QB7(a) sensitivity line shows whether a verdict
   reaches QB7(a)'s subject through the text." with:

   > §8.2's QB7(a) sensitivity reports, in both directions and with the rows removed, whenever their
   > treatment changes the verdict.

#### CF4-2. State the scope of OQ-7 in the rule text

**Where.** §6.3 labels (r4:677–681); §16 (r4:1323–1332).

**Replacement.**

1. After the first label bullet (r4:677–678), add:

   > - The label reports a textual commitment of the corpus. It is not independent physical verification of
   >   the assertion (owner decision OQ-7, #873 c.6872827835).

2. In §16, after "(A) requires an explicit grounding commitment or a failed F5 control (§8.5 (i)).", add:

   > - A verdict resting on As or As|cond rows reports what the corpus asserts. It is not independent
   >   physical verification of the assertion (OQ-7).

#### CF4-3. Replace the stale procedural line in §14.1

**Where.** r4:1184–1185.

**Replacement.** Replace the bullet "An owner answer to a pending OQ is applied by the alternative text of
§15. It is reviewed by a check of that edit alone, unless it changes text outside the marked points of use."
with:

> - The owner's answers to OQ-1 to OQ-7 are applied as §15 records (#873 c.6872827835). A change to an
>   applied answer before F is a new revision, reviewed under this section.

### Should-fix

#### CF4-4. Name the acceptance chain and the commit that F is

**Where.** r4:1186–1188.

**Replacement.**

> - **Freeze F (owner decision OQ-5, #873 c.6872827835).** The owner designates F on #873 after
>   independent acceptance.
>   - The decision names "the complete r2 rule and its controls".
>   - The owner's confirmation requires r4, with CF3-1 and CF3-2 applied and independently confirmed.
>   - The acceptance consists of REVIEW-QB5A-PREREG-r2 (the full round on the rule and its controls),
>     CONFIRM-QB5A-PREREG-r3, and the check of r4 that returns ACCEPT FOR FREEZE on the head it names.
>   - F is that head, by its full SHA.

### Nit

#### CF4-5. Two small accuracy points

- **OQ-3's mirror rule.** The decision states it generally: "an admissible grounding carve-out excluding the
  witness blocks outcome (B)". §8.3 item 3 already enforces it generally, but §8.5 (v)'s second consequence
  (r4:848–849) states it only for a metric-defined W0 quantity. Replace it with:

  > - if a carve whose class excludes the W0 quantity passes GRT and is Admissible, it is grounding-content
  >   with respect to that quantity and blocks (B) (§8.3 item 3). This holds for a metric-defined W0
  >   quantity in particular.

- **The time of the owner record.** At r4:36–37 and r4:1218, write "2026-11-14T06:05:54Z" for "2026-11-14",
  so that the record carries author and time (§A.42 item 7), as NOTES-QB5A-r4 §7 already does.

***

## 5. Readiness

Head `3607d5f98feea7565a2bfd23e23e569ddeb5bcfd` is **not yet** ready for designation as F. It becomes
ready once:

- CF4-1, CF4-2 and CF4-3 are applied, with CF4-4 and, as convenient, CF4-5;
- a check of those edits against the replacement text above returns ACCEPT FOR FREEZE on the new head. That
  check is the last link in the acceptance chain.

The changes touch only reporting, a limits line and a procedural bullet. No decision clause, test, control
or inventory row changes, so no full round is needed. The full SHA of the accepted head is then the one to
post on #873 for the owner's designation of F.

No inventory passage is classified here, and no expected outcome is stated. No manuscript change is
proposed, and no premise is adopted.

# Quick confirmation review of GAMMA-1 unit G1 r7

**Object.** The review covers three files, retained on PR #1294 at `5c955b32b`. The local copies match
these blobs.

| File | Blob |
|---|---|
| `GAMMA-G1-r7.md` | `995611d8` |
| `RESPONSE-OWNER-G2Q1.md` | `72f053fe` |
| `GAMMA-G1-r6.md` (the base, unchanged) | `3d56aa18` |

**Decision source.** #1169 c.6894553525 (`amaybaum`, 2026-11-15T12:48:31Z), row "G2 question 1
(GAMMA-1)". The reviewer read it through the REST API.

**Method.** The reviewer read the full r6→r7 diff (96 lines) and r7 §13. The review is read-only.

## Verdict: ACCEPT WITH CHANGES (minor)

The decision is carried exactly. Nothing else changed. One inconsistency in the G2 status list needs
correcting.

## 1. The decision as recorded

- **Quotation.** The owner's text is quoted verbatim at the header, §7.1 and §12. Its three bullets
  are joined by semicolons, and the text says so.
- **Three conditions.** §7.1 restates them faithfully:
  1. `b_j` is the value the source specifies.
  2. `b_j` is not invented for a family without an all-paths-blocked measurement. In r7's words:
     "`𝒜_10` has no all-paths-blocked protocol, so `b_j` is taken from the source and never set for
     it".
  3. The void clause tests separation from `−b_j`, not from 0.
- **Dark-process clause.** It is carried at §7.1: "does not depend on which paths are open, as the
  derivation above assumes". It is also carried at §12 and in the §13 question-1 row.
- **Scope.** "Reconciles the definitions only" is carried at §7.1. So are "no control is evaluated
  here" and "neither C0 nor PC-wave is established to pass or fail an experimental test". §10 says
  that the decision "establishes no control result". §12 says that a comparison "may now use the
  `−b_j` reference under them; none is made here".
- **Holds lifted.** r6's holds are replaced at every place r6 marked them: §7.1 (C0 and PC-wave),
  NC-γ6, §10, §12 and §13. No "pending" text about `−b_j` remains. The one remaining occurrence, at
  line 22, is r6's own revision note, kept with "r7 records the owner's answer" appended.

## 2. Nothing else changed

- Every diff hunk is either the header note or one of the held passages listed above.
- No definition, rule, number or control changed outside them.
- No comparison is made, and no verdict on γ or D-1 appears.

## 3. G2 status changes

`RESPONSE-OWNER-G2Q1.md` lists five G2 r3 status changes. All are right in substance:

| G2 r3 item | Status after the decision |
|---|---|
| Question 1 | answered yes |
| §6.1's three conditions and "0 replaced by `−b_j`" | owner-adopted; G2's opening-independence assumption is the owner's dark-process clause |
| §6.1, "changes no definition" | still true of G2 |
| G2-F7's control statement | owner-adopted |
| Condition 6 and greenness | the criterion is settled; the controls are not green and the candidate stays a candidate |

They also agree with the G2 r3 text: §6.1 states the opening-independence assumption.

**Change needed (minor).** r7 §13 updates only the question-1 row and the condition-6 row. Its §6.1
("One characterization") row and its G2-F7 row still carry r5's wording ("a statement about r4 …";
"for r5 the control statement … is G1's own"). They do not record the owner adoption that the response
lists. So the response and r7 §13 disagree on two rows.

Two ways to correct this:
- Bring those two rows in line with the response. Optionally retitle the §13 status column, which
  still reads "Under r5".
- Alternatively, state in the response that those two status changes are recorded there only.

***

## r8 addendum

**Object.** The addendum covers `GAMMA-G1-r8.md` and `RESPONSE-GAMMA-G1-r7.md`, read from the local
folder. The reviewer read the full r7→r8 diff.

**Verdict: ACCEPT.**

**Nothing else changed.** The diff has three parts:
- the title line;
- the r8 revision note;
- the §13 rows for §6.1 ("One characterization") and G2-F7.

**The two rows now match `RESPONSE-OWNER-G2Q1.md` and the owner record:**
- they mark the item owner-adopted under c.6894553525;
- they give the three conditions;
- they carry the dark-process clause;
- they say that the "disagree" clause describes r4 only;
- they say that no control result follows.

**The "Under r5" column title.** It is now somewhat misleading, though not wrong in substance:
- at least four rows record states after r5, including the §6.1, G2-F7, question-1 and condition-6
  rows;
- these states include the owner decision, which postdates r6;
- so a reader could take an owner-adopted status as r5's.

Retitling the column "Under r8" or "Status in this revision" is recommended. It does not block
acceptance.

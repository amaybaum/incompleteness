# RESPONSE to the focused confirmation of C3-RLIN-r2

**Object.** `CONFIRM-r2.md` (verdict ACCEPT WITH CHANGES), reviewing r2 at `ee4db4f1` on branch
`research/c3-rlin-xiii-1169-20261113`. r1 and r2 files and `RESPONSE-r1.md` are left unchanged. r3 is
`C3-RLIN-r3.md` (cited `r3:n`) and `NOTES-r3.md`.

**Standing.** WIP / UNVERIFIED. Paper-only. No premise adopted, no rule changed, nothing committed,
pushed or posted.

**Scope of r3.** The reviewer's text for C1 (optional heading note), C2, C3, C4 and the nit is applied as
given, adapted only to the surrounding sentence. Nothing else changes apart from the title and revision
lines of each file. No verdict changes.

***

## Dispositions

| Item | Disposition | r3 location |
|---|---|---|
| **C1** delta rows of RESPONSE-r1 omit the removal of the reading enumerations | Accepted. RESPONSE-r1 is frozen, so the correction is recorded below. The optional heading note is applied: "outcome clauses (A)–(C) as in r1; reading enumerations replaced by the criterion" | r3:193; this file, "C1 correction" |
| **C2** R1s's (B) has no §2 control | Accepted: "(the §2 control cannot be met under R1s, N3.3; the verdict rests on the proof N2 alone)" added to the N2 verdict line, N7's R1s row and §4 bullet 1 | r3:266–267, :426, :442–444 |
| **C3** R1s bearing omits the rule-class condition; carrier remark in the list of conditions | Accepted: "if the owner fixes R1s with use time `t_p` and confirms the R-lin reading of the class (owner question 4), and the result survives independent review, … (N2 holds for every carrier of §1.1, so owner question 5 does not affect it)" | r3:476–480 |
| **C4** W2′ is a `d = 1` instance | Accepted: "at site level in `d = 1` (W2′)" in §4 bullet 2 and N7 rows R1v, R2(iii); Q5 adds W2′'s `d = 1` scope | r3:427, :430, :447, :543–544 |
| **Nit** NOTES-r2:183 "odd `q`" | Accepted: NOTES-r3 §6 reads "`q ≠ 2` (at `q = 4` the label-free cell `2a` separates `a = 0` from `a = 1`)", in line with r2:376 / r3:379 "other `q` open" | NOTES-r3:184 |

## C1 correction to RESPONSE-r1's r1 → r2 delta table

RESPONSE-r1 is not edited. Its delta table is to be read with these two rows corrected:

| r1 lines | r2 lines | Change (corrected) | Finding |
|---|---|---|---|
| 154, 156 | 191, 193 | §2 heading notes unchanged outcome clauses; "For each reading R": reading enumeration dropped | 10 |
| 168–174 | 205–221 | class-level clause: the enumerated list "(R1, R2(i), R2(ii))" replaced by its criterion (finding 10); control clause; "Standing and limits of the rule" | 3, 10 |

## Size of the change

- `diff -u C3-RLIN-r2.md C3-RLIN-r3.md`: 86 lines, 30 changed lines (`+` or `-`, headers excluded),
  7 hunks.
- `diff -u NOTES-r2.md NOTES-r3.md`: 23 lines, 7 changed lines, 2 hunks.

## Full `diff -u`, r2 → r3

```diff
--- C3-RLIN-r2.md	2026-11-13 20:48:28.205755553 +0000
+++ C3-RLIN-r3.md	2026-11-13 20:57:18.893787098 +0000
@@ -1,6 +1,8 @@
-# C3 for R-lin with (xiii): label-cell-only retention (paper-only check, r2)
+# C3 for R-lin with (xiii): label-cell-only retention (paper-only check, r3)
 
-**Revision.** r2 applies findings 1–11 of the independent review of r1 (verdict REVISE,
+**Revision.** r3 applies changes C2–C4 of the focused confirmation of r2 (verdict ACCEPT WITH
+CHANGES, `CONFIRM-r2.md`, r2 at `ee4db4f1`), with the dispositions in `RESPONSE-r2.md`; C1 is
+applied in the §2 heading note and recorded in `RESPONSE-r2.md`. r2 applies findings 1–11 of the independent review of r1 (verdict REVISE,
 `REVIEW-r1.md` at `a03af682`, branch `research/c3-rlin-xiii-1169-20261113`; r1 at `00c84af2`). The
 dispositions are in `RESPONSE-r1.md`. The readings R1v and R2(iii) and the reviewer's label sets were
 re-derived by hand before use. The class-level verdict (C) is unchanged; its grounds change.
@@ -188,7 +190,7 @@
 
 ***
 
-## 2. Decision rule (fixed after §1 and before §3; outcome clauses as in r1)
+## 2. Decision rule (fixed after §1 and before §3; outcome clauses (A)–(C) as in r1; reading enumerations replaced by the criterion)
 
 For each reading R:
 
@@ -261,7 +263,8 @@
 simplex embedding of the C-PM fragment, under H-xiv, one direction only, transformation
 noncontextuality not claimed [P on P0, R-off]. `D_0` is not used in N2 itself; (H3) is used (N1).
 
-Verdict: (B) under R1s with use time `t_p` [P]; (C) under R1s with use at each effect's read.
+Verdict: (B) under R1s with use time `t_p` [P] (the §2 control cannot be met under R1s, N3.3; the
+verdict rests on the proof N2 alone); (C) under R1s with use at each effect's read.
 
 ### N3. Pressure test of N2 (favourable to closure) [P]
 
@@ -420,11 +423,11 @@
 
 | Reading | Precedent-consistent | Verdict | Node |
 |---|---|---|---|
-| R1s | yes | (B) at use time `t_p`, all of §1.1's scope; (C) with use at each effect's read | N2 |
-| R1v | yes | (A): W1 (`d = 1`, `d = 3`, every `q`), W2′ (site level) | N4, N5 |
+| R1s | yes | (B) at use time `t_p`, all of §1.1's scope (the §2 control cannot be met under R1s, N3.3; the verdict rests on the proof N2 alone); (C) with use at each effect's read | N2 |
+| R1v | yes | (A): W1 (`d = 1`, `d = 3`, every `q`), W2′ (site level in `d = 1`) | N4, N5 |
 | R2(i) | yes | (A): W1 `d = 1`; `d = 3`: W1's embedding classical, enlarged observer a gbit at `q = 2`, other `q` open | N4, N5 |
 | R2(ii) | yes | (C), N6 gap | N6 |
-| R2(iii) | yes | (A): W1 (`d = 1`, `d = 3`, every `q`), W2′ (site level) | N4, N5 |
+| R2(iii) | yes | (A): W1 (`d = 1`, `d = 3`, every `q`), W2′ (site level in `d = 1`) | N4, N5 |
 | R3 | no (fails N8.2(b)) | (A): W1 (`d = 1, 3`), W2′ | N4, N5 |
 
 The precedent-consistent readings disagree on W1 itself. By §2 the class-level verdict is (C).
@@ -437,10 +440,11 @@
 
 - Under R1s (structural exact move) with use time `t_p`, label-cell-only retention cannot occur for
   R-lin with (xiii): label status survives at most one tick past the use time (N1, N2). (LF) and C3
-  hold for the class.
+  hold for the class (the §2 control cannot be met under R1s, N3.3; the verdict rests on the proof
+  N2 alone).
 - Under R1v (exact move on the support), R2(i) and R2(iii), W1 is an R-lin instance of the class with
   label-cell-only retention and lost common effects, and the fragment is a gbit (N4). Under R1v and
-  R2(iii) this holds in `d = 1` and `d = 3` for every `q`, and at site level (W2′).
+  R2(iii) this holds in `d = 1` and `d = 3` for every `q`, and at site level in `d = 1` (W2′).
 - Under R2(ii), and under R1s with use at each effect's read, the question is open (N2, N6).
 - The remaining gap is the delimitation itself: which cells of `V(τ)`, `τ > t_p`, C-PM counts as
   preparation labels when records are held in `V` (SY:201–202, MM-2 item 3). The precedents leave two
@@ -469,10 +473,11 @@
 **P0.** P0 stays **O-U**. Its unresolved check (P0:424–427) is now located: C3 for R-lin turns on the
 label delimitation (N4, N5) and, under R1s, on the use-time convention. Conditional bearings, neither
 adopted:
-- if the owner fixes R1s with use time `t_p`, the carrier question (owner question 5) leaves R1s's
-  result unchanged, and the result survives independent review, the C3 and C4 checks pass for the
+- if the owner fixes R1s with use time `t_p` and confirms the R-lin reading of the class (owner
+  question 4), and the result survives independent review, the C3 and C4 checks pass for the
   class, P0's pass condition (P0:67–71) is met with C1–C2 (P0 N1, N4), subject to P4, and the ordering
-  rule (R9:317–320) hands Q4 to AW-OA2-1;
+  rule (R9:317–320) hands Q4 to AW-OA2-1 (N2 holds for every carrier of §1.1, so owner question 5
+  does not affect it);
 - if the owner fixes R1v or R2(iii) (any carrier treated), or R2(i) with a ring carrier, W1 is an
   in-class contextual counterexample, which P0:74–76 permits in place of O-U; whether a
   reading-produced gbit counts (compare OA3:445–455) is a separate decision.
@@ -535,7 +540,8 @@
 5. **Carrier.** Does the class admit rings and other `d`, as P0's instances use (P0:392, :402), or only
    the simple cubic lattice (P:85–86; Main:724 (x))? R1s's (B) holds for all of them. Under R1v and
    R2(iii) W1 is a gbit in `d = 1` and `d = 3`; under R2(i) only in `d = 1` and, with an enlarged
-   observer, in `d = 3` at `q = 2`.
+   observer, in `d = 3` at `q = 2`. W2′ (site level) is a `d = 1` instance; W2′ in `d = 3` is not
+   examined.
 6. **Use time under R1s.** With use at each effect's read, which cells of `V(τ)` hold the herald? N2
    holds for use time `t_p` only.
 
```

```diff
--- NOTES-r2.md	2026-11-13 20:49:22.025758752 +0000
+++ NOTES-r3.md	2026-11-13 20:57:23.193787354 +0000
@@ -1,7 +1,8 @@
-# NOTES (r2) for C3-RLIN-r2.md
+# NOTES (r3) for C3-RLIN-r3.md
 
-**Standing.** Working notes for the paper-only C3 check, r2. WIP / UNVERIFIED, unreviewed. Hand
-reasoning only.
+**Standing.** Working notes for the paper-only C3 check, r3. WIP / UNVERIFIED, unreviewed. Hand
+reasoning only. r3 changes only the title, this paragraph and §6's first bullet (the nit of
+`CONFIRM-r2.md`); the rest is NOTES-r2 unchanged.
 
 ## 0. Sources and commands
 
@@ -180,7 +181,7 @@
 
 ## 6. Not done
 
-- R2(i) in `d = 3` for odd `q`; R2(i) at site level beyond W2′; R2(ii) beyond one geometry.
+- R2(i) in `d = 3` for `q ≠ 2` (at `q = 4` the label-free cell `2a` separates `a = 0` from `a = 1`); R2(i) at site level beyond W2′; R2(ii) beyond one geometry.
 - R1s with use at each effect's read.
 - W2′ in `d = 3`.
 - No check of whether further delimitations agree with every precedent.
```

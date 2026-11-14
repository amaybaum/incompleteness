# Focused confirmation r2: Bell support and ladder landing plan (#868)

**Object.** Branch `records/bell-landing-plan-868-20261114` at
`0ff08c129732daab02b813004a5b9ee81137498b`. Its parent `8b03a04c` adds review r1. The diff from
`ed61696d` was read for `LANDING-PLAN.md` (LP), `STATUS-BS.md` (SBS), `STATUS-SB-L3.md` (SL3),
`STATUS-LADDER.md` (SLD) and `NOTES-PLAN.md` (NP), together with `RESPONSE-BELL-PLAN-r1.md`. Line
numbers are at `0ff08c12`.

**Reviewer.** The author of review r1. Read-only. No computation and no write to the repository
or host. This confirmation is not verification (§A.46 item 7) and authorizes nothing.

**Review file.** `REVIEW-BELL-PLAN-r1.md` at `8b03a04c` is byte-identical to the review as
written (`cmp`), and `0ff08c12` does not change it.

## Verdict: ACCEPT WITH CHANGES (minor)

All 27 findings of r1 are applied at the cited lines, including B1, B2, S1–S14 and N1–N11. The
writer's correction of fact under S14 is right, and I accept it. Two should-fix items remain, and
both arose from the replacement text that r1 itself supplied:
- **C1** concerns BS's evidence-tag line.
- **C2** concerns the self-referential `<sha>` placeholder.

There are also two nits. Nothing blocks.

***

## 1. Resolution of each finding

| Finding | Resolved? | Checked at |
|---|---|---|
| B1 | Yes; see §3. | SBS:3–4, :197–206; SL3:3–7, :26–29, :163–166, :174–176; SLD:3–4, :178–181, :208–209; LP §6.3 row "`LANDING-PLAN.md`, `NOTES-PLAN.md`" |
| B2 | Yes; see §4. | SLD:59–75 |
| S1 | Yes. Check 2 gives PR reachability; Main:360's general sentence and Main:416 cover the absence of a selector. Main:360's construction is stated to keep measurement independence. | LP §2.1 stage-7 row, §2.5 LD:104 row, §2.5 consequences, §4 reason 2, §6.1 N4 row; SLD:53, :130, :165–171, :191 |
| S2 | Yes. The LD:284 row matches OC:509. SLD lists all four uses. | LP §2.5; SLD:161–162 |
| S3 | Yes. The sentence stays support off `main` and is stated with QH's conditions (QH:68, :85–86, :212, :215, which I checked). LD:300's gap label is kept. No r4. The owner route is put as OQ-6. | SLD:149, :187–194; LP §4, §6.1; NP:119–125 |
| S4 | Yes for the process: G1 (i′), and G3 with a forward note and a focused check. The wording introduces C2. | LP:52, :54; SBS, SL3 and SLD Landing sections |
| S5 | Yes. All five conditions apply in full; historical authorization is provenance. | LP §7 lead-in and last row; SBS:201–205; SL3:157–159, :174–176; SLD:215–217 |
| S6 | Yes. The wording is "puts on `main` the … on which OC's narrowed row … is conditioned", OC stays conditional, and SLL still needs L2. | LP §2.3, §3.5, §5.2, §7; SBS:214–217; SL3:168–171 |
| S7 | Yes. Content and resolution table as specified. The B1 row adds a sentence, which is C3. | SL3:16–23, :128–130; LP §5.2, §6.3 |
| S8 | Yes. | SL3:67–71 |
| S9 | Yes. | LP "Inside G2"; NP:54–55, :112–118 |
| S10 | Yes, in Limitations, the probe row and the dependency row. The "What the record supports" table (SBS:49–58) still shows [X] for G1–G7 without the caveat; Limitations covers it, so this is acceptable. | SBS:101–104, :135, :151 |
| S11 | Yes. | LP §2.4; SLD:145; SL3:149–152 |
| S12 | Yes. | LP:51; SBS:198–203; SL3:155–157; SLD:213–215 |
| S13 | Applied. The SLD entry is correct. The SBS entry over-reaches, which is C1. | SLD:196–198; SBS:188–190 |
| S14 | Yes, with the writer's correction; see §2. | LP §2.5 L3 paragraph; SL3:41–43 |
| N1–N11 | Yes, each at the place RESPONSE names. The N2 drift bullet (SBS:160–162) correctly maps BS's 366–393 → 364–391, of which 364–389 is the theorem through □. | as listed in RESPONSE |

## 2. The correction of fact under S14

**Accepted.** `diff` of `b94b283a`:153–157 against `86a413c8`:167–171 shows lines 1–4 identical.
Line 5 (r1:157 / r2:171) differs only by r2's appended sentence: "The independent re-review of
Bell-scope r2 records the same point as a nonblocking note (review 5857981727, §6)." In r1 I compared
only the L3 paragraph (S:169) and overstated the match as covering lines 167–171. The corrected
statement at SL3:41–43 and LP §2.5 is exact. The conclusion is unchanged: the appended sentence is
a citation, not part of L3's statement or argument.

## 3. B1: are the STATUS notes self-contained?

Yes. In SBS, SL3 and SLD at `0ff08c12`, a search for `LANDING-PLAN`, `NOTES-PLAN`, `OQ-`,
`RESPONSE-BELL`, `REVIEW-BELL`, `this plan` and `bell-landing` returns no hit. The N′ justification
is now stated in SL3 itself (SL3:26–29), and so is the N4 scope analysis in SLD (SLD:156–176). The
only remaining pointers are to on-`main` records, to the package's own records, to accountable
Issues and owner comments (governance provenance), and to `<sha>` (C2). LP §6.3's added row and
corrected closing sentence are accurate.

## 4. B2: does the scoped claim carry every hypothesis?

Yes. SLD:59–75 now carries every conjunct of the controlling condition:
- (D) "one deterministic map";
- (F) "a finite site-factorized space";
- (Gen) "settings read from disjoint generator regions";
- (Rec) "complete local record windows";
- every-run outputs with a fixed local failure rule;
- a finite menu with every pair jointly admissible;
- no postselection;
- directed (Sep);
- measurement independence for the response-complete variable, which is BS:196's convention: Ω
  under (GI), λ\* otherwise.

The AL clause carries finite abelian site groups, (vii) as a conditional posit, coset-uniform laws,
cell-valued settings with every pair of positive probability, complete fixed-region histories and
complete-history NS. This matches LD:189–205 and SLD:79–89.

## 5. New text: anything wrong or stronger than its source?

Nothing is stronger than its source. Four items need attention, C1–C4.

**C1 (should-fix). SBS:188–190 marks BS lines 21–24 as superseded as a whole.** BS:22's
"**D** draft off `main`" still describes BS's one [D]-tagged item. That item is #1210's A6.1 at
BS:183 ("(D, off `main`), is provenance only"), and it stays off `main`. Only the "unreviewed" in
BS:22–23's **A** definition is superseded. My S13 replacement text invited the over-reach. LD's [D]
items are BS, SB and QH, so for SLD the entry is right.

*Replacement* for SBS:188–190: "- Line 23 (\"**A** derivation in this file, unreviewed\"): the
record's [A] items have been reviewed as listed above; the record is on `main` as a research record,
model-reviewed and not verified (§A.46 item 7). Line 22's \"**D** draft off `main`\" still describes
its one [D] item, A6.1 of #1210 (BS:183), which stays off `main`."

**C2 (should-fix). The `<sha>` placeholder cannot be filled as written.** The affected lines are
SBS:212, :216, :224; SL3:166, :170, :181; and SLD:222, :227, :232. Each note is part of the package
head, and a commit cannot name its own id. Filling `<sha>` with any other commit would make the
statement false or ambiguous. LP G2 does not say how the placeholder is filled. My S4 replacement
text introduced this.

*Replacement* for each "at the package head `<sha>`, no package-level review [or merge decision] is
recorded" clause: "in this note as landed, no package-level review [or merge decision] is recorded".
Each Owner-record line then reads: "In this note as landed, no package-level review or merge
decision is recorded; the merge decision and the package's reviews are quoted, with their commits,
in the forward note added after landing." Add to LP G3: "the forward note names the reviewed
package head and the merge commit". The wording still states the condition at the reviewed head
without moving it (S4's purpose).

**C3 (nit). SL3:129 and LP §6.3 say "B1's hidden sequence is infinite, so the consequence applies
to it only within the finite-depth limit".** Read literally, this suggests B1 lies outside the
consequence. Model B1 (recursive-substates `README.md`:23) acts only on `(b_0, b_m)` for one fixed
finite `m`, and the rest of the sequence is fixed and unread. The consequence therefore applies to
B1 through that finite factor.

*Replacement* for the parenthesis: "(B1 reads and writes only `b_0` and `b_m` for one fixed finite
`m`, README.md:23; the remainder of its sequence is fixed and unread, so the finite-depth
consequence applies to B1 through that finite factor)."

**C4 (nit). SBS:70 is now one line of 174 characters.** Re-wrap it to the file's width.

## 6. OQ recommendations in NOTES-PLAN

They are recorded correctly. NP:84–167 gives each owner question a separate "Reviewer" line, and
each matches r1's table in substance. The OQ-6 record ("the same") correctly carries the
recommendation to record the sentence under §A.42 item 8's final sentence, given the question's
wording. OQ-7 ("required before G2; … fold it into the G2 merge decision") and OQ-8 ((a) ratify;
(b) replay as a package check) are verbatim in substance. The "(done)" marks at OQ-4, OQ-11 and
OQ-14 are accurate at `0ff08c12`. NP:47–48 describes the review's identity checks correctly.

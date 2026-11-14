# Confirmation review of `L54-r5.md` at its exact head

**Head reviewed.** Branch `research/tune1-paper-units-1236-20261114`, commit
`f4a54a20fc041e446f2467bce38361cb02efeec0` (draft PR #1288), parent `a1508006`. `git rev-parse HEAD`
returned that SHA and `git status --short` was empty. Directory under review:
`verification/programmes/oi-qm/reconstruction/drafts/tune1-paper-units-20261114/` (`l54/` and the
`README.md`). The previous confirmation is `l54/CONFIRM-r4.md` (of r4 at `de22ceab`), findings
F1–F9.

**What this confirmation is.** A model review of the text at that head by a non-author, who did not
write r5, r4, the independent check or any earlier revision. It compares texts, checks that each
correction carries its source's content and scope, and checks statuses and the scoped verdict. It is
not independent verification of the mathematics: no derivation was re-done beyond reading the proof
of Lemma S in `CHECK-RULEFREE.md` §3.1 and `CONFIRM-r2.md` §6 to check that the stated hypotheses
cover the steps that use them. No computation was run on any OI rule or model. Nothing was edited,
committed, pushed or posted. The scope is the four questions below; findings outside them are not
reopened.

## Overall verdict: ACCEPT WITH CHANGES

`L54-r5.md` and `SUMMARY-r5.md` are accepted as the final text of this correction cycle. The one
required change is a count in the parent `README.md` (R1 below). It touches neither r5, nor
`SUMMARY-r5.md`, nor `RESPONSE-CONFIRM-r4.md`, nor any statement of a result.

***

## Question 1. Does r5 implement F1–F7 and F9? **Yes.**

`diff L54-r4.md L54-r5.md` has twelve hunks. Every one is accounted for:

| r5 location | Change | Source | Finding |
|---|---|---|---|
| title | r4 → r5 | bookkeeping | accounted (`RESPONSE-CONFIRM-r4.md`, "Other changes") |
| headline | "through property (T) (Lemmas 1 and 5)" | F2 | replacement as given |
| standing paragraph | review state to r5; authorization for r4 and r5; unchanged-files list; attribution of `CONFIRM-r4.md`; "No proof step of Theorem 1 changed in r2–r5"; disclosure | F9, bookkeeping | accounted; F9 in modified form (below) |
| §0, closing paragraph | "through property (T)"; Proposition E clause narrowed to "in exchange mode under H-write" | F2 ("everywhere it appears") | accounted; a narrowing |
| §7 assessment item 2 | "an obstruction specific to additive dynamics through property (T)" | F2 | accounted |
| §8 item 7 | "r5 as a whole has not been reviewed" | bookkeeping | accounted |
| §9.2, last sentence | R1 "a related constraint from the same overlap (two configurations at `1 − 2ε` for each first label)" | F5 | replacement as given |
| §9.3, Lemma S (S5) | per-label cross test, both cross tests for both labels | F1 | replacement as given |
| §9.3, end of Corollary S1 paragraph | "neither shows by itself that any rule fails, outside the `τ = 1` corner; Lemma S remains a necessary condition every pair-form rule must meet" | F4 | replacement as given |
| §9.4, Statement | pointer to CF:285–294 and `CHECK-RULEFREE.md` §4.1, with `CF:n` defined in place | F7 | as given, plus the citation-form definition (needed: `CF` is not in r5's citation-forms list) |
| §9.4, Initial-condition mode | "the case `τ ≥ 2` is open (`τ = 1` is decided by Corollary S1)" | F6 | replacement as given |
| §9.6 items 3 and 4 | item 3 as given in F2; item 4 carries the F4 correction | F2, F4 | accounted |

**F1 in detail.** `CHECK-RULEFREE.md` §3.1 lists hypotheses (h1)–(h5). Its proof uses: the copy
`f(h_1) = f′(h_2)` (h1–h3); the product form `L_uv`, rank-one projectors, `|a·b| ≤ 1/2` and
`q_v(·|k)` supported in class `k` and the same in every test (h4), to get
`π(k_2|k*) = (1 ± a·b)/2 ≥ 1/4`; credit `ε < 1/32` on one cross test `(c_u, c_v)`, `u ≠ v`, to fix
`x°` from `B_0, B_1`, so that `x°` depends on `q_v` only (h5, steps 3–5); and credit on the test in
which the conclusion is wanted (h5, step 6). The configuration for label `c_v` comes only from the
cross test whose second label is `c_v`. r5's list covers each use: (S1) ↔ (h1), (S2) ↔ (h2),
(S3) and the non-empty `D` of (S6) ↔ (h3), (S4) and (S6) ↔ (h4), and (S5) ↔ (h5). r5's (S5) names,
for the label `c_v` in the conclusion, the cross test `(c_u, c_v)`, `u ≠ v`, and the conclusion's
test, and for the statement's "for each read label `c_v`" both tests `(c_a, c_b)` and `(c_b, c_a)`,
which is `CONFIRM-r2.md` (S5). The statement is therefore covered for both labels. r5 asks for one
state on both tests where (h5) allows the cross test's state to differ; that is a stronger
hypothesis than the proof needs and matches `CONFIRM-r2.md` (S5), so it is safe. **F1 is resolved.**

**F9.** The reviewer's wording was replaced by "no repository edit by the writer beyond the files
of this revision; nothing pushed or posted by the writer". It removes the false "nothing committed"
and claims nothing about commits, and it is scoped to the writer, which the README's "applied here"
for F8 makes consistent. Who pushed is a disclosure this review cannot check. **Resolved in modified
form.**

**Theorem 1.** No hunk falls in its statement, hypotheses 1–8, constants (`1/96`, `1/128`), proof
steps, Corollary 1a, Proposition 2 or Lemmas 1–5.

## Question 2. Does the README identify r5 and describe the corrections accurately? **Yes, with one count error.**

`git diff a1508006 f4a54a20 -- README.md` adds a row "`L54-r5.md`, `SUMMARY-r5.md` | The current
text and its summary", changes the r3 row to "The revision before the independent check's
corrections", adds a row for `RESPONSE-CONFIRM-r4.md`, appends "(the checker's Proposition M: one
derivation, not checked)" to the verdict row, applies the "applied as worded" note in the r4
paragraph as F8 worded it, and extends that paragraph with r5. The F8 item that would have called r4
"The current text" is correctly not applied, since r5 is now current; the new r5 row does that job.

The r4 paragraph says "`L54-r5.md` applies the seven that concern the text (F1–F7, F9) … the eighth
concerns this README". F1–F7 and F9 are eight findings, and F8 is the ninth of nine (one medium,
eight low, as the same paragraph says). This is required change R1. The phrase "both cross tests" is
in quotation marks but does not occur in r5; R1 drops the marks.

## Question 3. Does `RESPONSE-CONFIRM-r4.md` resolve the response-table findings, with the frozen files unchanged? **Yes.**

`CONFIRM-r4.md` asked for four changes to `RESPONSE-CHECK.md`: F1 (row 2: record the (S5)
restatement), F5 (row 1: record the R1 sentence), F7 (row 3: "fully specified by CF:285–294 with
this completion") and F9 (last line: disclosure). `RESPONSE-CONFIRM-r4.md` records each in its own
table instead: F1 with a crosswalk of the r3 → r4 restatement and its r5 reversal, F5 as a writer
addition in r4 corrected in r5, F7 with the row 3 wording, and F9 by stating that the r5 correction
applies to `RESPONSE-CHECK.md`'s last line. Each carries the content `CONFIRM-r4.md` asked for.

`git diff a1508006 f4a54a20 --stat` lists four files for the whole tree: `README.md` (modified) and
`l54/L54-r5.md`, `l54/RESPONSE-CONFIRM-r4.md`, `l54/SUMMARY-r5.md` (added). `RESPONSE-CHECK.md`,
`L54-r4.md`, `SUMMARY-r4.md`, `CONFIRM-r2.md`, `CONFIRM-r4.md`, `CHECK-RULEFREE.md`, `L54-r3.md` and
every earlier file are byte-identical to the parent; `git diff --quiet` confirmed this for each file
named in the question.

## Question 4. New claims, Theorem 1, the scoped verdict, statuses? **None introduced; consistent.**

- **New claims.** None. "Through property (T) (Lemmas 1 and 5)", the `τ = 1` exception, "a
  necessary condition every pair-form rule must meet" and "in exchange mode under H-write" all come
  from `CONFIRM-r4.md` F2, F4, K7 and Proposition E's own statement. The §0 and §7 changes narrow.
- **Theorem 1.** Statement, hypotheses, constants and proof unchanged in r5. `SUMMARY-r5.md`'s
  Theorem 1 paragraph is byte-identical to `SUMMARY-r4.md`'s.
- **Scoped verdict** (§9.6, headline, §0, summary): A, B, C fail Q5′ under the stated
  additive-rule/target/record conditions; L5.4–L5.6 decided only within that scope; not a
  rule-independent no-go, now qualified by mode and the `τ = 1` corner; rule-free lemma
  definitional, with its necessary-condition role stated; the non-additive example witnesses only
  Q5′, fails Q3′, Q6′ and Q2, and is not class D; memory compatible with selection under the fixed
  label-independent split (one derivation, not checked); R-nl, the gate question, other record
  conventions and class D open. Each matches.
- **Statuses.** Confirmed reviewer results (Lemma S, Corollary S1, Proposition E for Q5′, Q3′ and
  Q6′ failure) carry "one author, one independent check". Q2 failure and the memory split carry
  "one derivation, not checked", in r5 and now in `SUMMARY-r5.md`. Correct.

***

## Required change

**R1 (parent `README.md`, r4 paragraph).** Replace

> `L54-r5.md` applies the seven that concern the text (F1–F7, F9),
> restoring the rule-free lemma's hypothesis to "both cross tests"; the eighth concerns this README
> and is applied here.

by

> `L54-r5.md` applies the eight that concern the text (F1–F7, F9),
> restoring the rule-free lemma's hypothesis to both cross tests; the ninth, F8, concerns this
> README and is applied here, with the r4 row left as it was and a new row naming r5 as the current
> text.

## Optional suggestions (not required)

1. `L54-r5.md` §9.4, Statement: the line ending "(`CF:n` = `CONFIRM-r2.md`). The rule is reversible,
   as every pair-form rule is, and not" runs past the file's line width; rewrap. Alternatively move
   the `CF:n` definition into the citation-forms paragraph.
2. `L54-r5.md` §7 item 2: "meets Q5′ in exchange mode (§9.4 …)" could read "in exchange mode under
   H-write", as §0 and §9.6 item 3 now do.
3. `SUMMARY-r5.md` status line: r4's summary said r3 is unreviewed; r5's summary drops that word.
   r5's standing paragraph keeps it; the summary could too.
4. `RESPONSE-CONFIRM-r4.md` F8 row reads "Not acted on; passed to the coordinator"; R1's sentence in
   the README now records how F8 was applied, so no change there is needed, but a pointer from the
   row to the README would close the loop.
5. `README.md`: the "Headline of r3" paragraph and the pre-existing verdict rows ("a definitional
   corner of the schema, not evidence about dynamics"; "A universal interface obstruction is
   refuted") predate F2 and F4 and describe r3 and the check; a pointer to r5's §9.6 would keep a
   reader from taking them as the current verdict. Two long lines in the r4 paragraph could be
   rewrapped.

***

**Read.** At the head: `CONFIRM-r4.md` (whole); `diff L54-r4.md L54-r5.md` (every hunk);
`L54-r5.md` standing paragraph, §0 closing paragraph, §7 assessment, §8 item 7, §§9.2–9.6;
`CHECK-RULEFREE.md` §§3.1–3.4 and §9 K2–K6; `CONFIRM-r2.md` Lemma S (hypotheses, statement, proof);
`RESPONSE-CONFIRM-r4.md`, `SUMMARY-r5.md` and `diff SUMMARY-r4.md SUMMARY-r5.md`; the README diff
and the whole README; the commit messages of the head and its two predecessors. Commands:
`git rev-parse`, `git status`, `git diff` (with `--stat`, `--name-status`, `--quiet`), `git log`,
`diff`, `sed -n`, `grep`, `cat`, `ls`. This is a model review of the text at
`f4a54a20fc041e446f2467bce38361cb02efeec0`, not independent verification of the mathematics.

# Confirmation review of `L54-r4.md` at its exact head

**Head reviewed.** Branch `research/tune1-paper-units-1236-20261114`, commit
`de22ceabee2bb45fbfb75d5232ce9c38bba8c7e9` (draft PR #1288), parent `da393029`. The checkout was at
that commit with a clean working tree. Sources on `main` were read at `c3b5f37a`. Directory under
review: `verification/programmes/oi-qm/reconstruction/drafts/tune1-paper-units-20261114/l54/`, plus
its parent `README.md`.

**Authorization checked against.** PR #1288 comment 6875725169 (`amaybaum`,
2026-11-14T10:12:13Z), read through the GitHub API.

**What this confirmation is.** A model review of the text at that head by a non-author, who did not
write r4, the independent check or any earlier revision. It compares texts, checks that the
corrections carry their source's content and scope, and checks statuses and the scoped verdict
against the authorization. It is not independent verification of the mathematics: no derivation
was re-done beyond reading proofs to check whether a stated hypothesis covers the step that uses it.
No computation was run on any OI rule or model. Nothing was edited, committed, pushed or posted.

## Verdict: ACCEPT WITH CHANGES

Preservation holds. Theorem 1, its proof, its hypotheses and its constants are unchanged. Every
change from r3 is accounted for by K1–K8, the scoped verdict or the status line, except two small
writer additions (findings F1 and F5). Statuses are applied correctly in r4. The scoped verdict
matches the authorization item by item, with three wording points (F2, F3, F4). One finding is
Medium (F1). The rest are Low. None blocks an integration proposal once applied, and none touches
Theorem 1.

***

## 1. Preservation

`git diff da393029 de22ceab --stat` lists four files: `l54/L54-r4.md` (new), `l54/RESPONSE-CHECK.md`
(new), `l54/SUMMARY-r4.md` (new) and `README.md` (11 lines added). No other file changes.
`CONFIRM-r2.md`, `L54-r3.md`, `SUMMARY-r3.md`, `CHECK-RULEFREE.md`, `L54-r1.md`, `L54-r2.md`,
`NOTES-r1.md`, `REVIEW-r1.md` and `RESPONSE-r1.md` are byte-identical to the parent. The sha256 values
of `CONFIRM-r2.md`, `L54-r3.md` and `SUMMARY-r3.md` begin `28af758d`, `0536038a` and `f398f897`,
as `RESPONSE-CHECK.md` states. **Holds.**

## 2. The eight corrections

| K | Claimed | Finding |
|---|---|---|
| K1 | as worded | Text matches §9 K1, with `D` defined for both modes (faithful). r4 adds one sentence that is not in K1 and is not accounted for: "R1 of §7 is a weaker form of the same constraint" (F5) |
| K2 | as worded | (S6) and both Corollary S1 sentences match. The authorized "definitional" sentence is added and accounted for (wording point F4). Lemma S's (S5) was also restated, which `RESPONSE-CHECK.md` does not record, and the restatement loses which cross test is needed (F1) |
| K3 | adapted | Content preserved (`G_{r_N} = x_{r_{N−1}}`, not reached within the horizon). r4 does not reproduce or point to the rest of the rule, so the row's "fully specified as cited" has nothing to cite (F7) |
| K4 | as worded, plus status tags | Matches verbatim. Q3′ and Q6′ are tagged one author, one independent check (CF:331, confirmed in the check's §4.4). Q2 is tagged one derivation, not checked. **Faithful** |
| K5 | adapted | The three features are restated without their parentheticals and without "so that nothing but the class passes between rounds". Both omissions are harmless. "Under the uniform law" is narrowed to "under the uniform product law in initial-condition mode", which is the Remark's own scope (CF:271). The replacement sentence is kept. **Preserves content and scope** (the narrowing matches the cited Remark) |
| K6 | adapted (table to prose) | Both forms are present with their consequences and owner-decision status, and so is the "only if" condition for readmitting the decoder. The closing "under it Theorem 1 is unchanged. It is unchecked" becomes "Theorem 1's bound is stated to hold with the same constant … one derivation, not checked", which is equivalent. The unrestricted-form reduction is tagged not checked, the more conservative of the two labels available. **Preserves content and scope**; nothing is strengthened |
| K7 | as worded, plus status tags | Matches. "Quantum target" becomes "target", which does not matter. The closing paragraph saying the items change neither the statement nor the proof of Theorem 1 is accurate. **Faithful** |
| K8 | as worded | "(ii)" is restated as the question it names, which is accounted for. The opening "At other `τ`" is dropped, so "this case is open" reads as all of initial-condition mode, including the `τ = 1` corner that Corollary S1 decides (F6) |

## 3. r3 → r4 delta

Every hunk of `diff L54-r3.md L54-r4.md` was read. The title, standing line, `S1:n` citation form,
§0 outcome label and closing paragraph, §6 opening, scope sentence, target-form and class-D
bullets, prior-art item (2), §7 R1 and assessment items 2–3, §8 items 5, 7 and 8, and the
replacement of §9 are all accounted for by `RESPONSE-CHECK.md` or the scoped verdict. The
exceptions are the (S5) restatement (F1) and the R1 sentence in §9.2 (F5). **Theorem 1's
statement, hypotheses 1–8, constants (`1/96`, `1/128`), proof steps, Corollary 1a, Proposition 2
and Lemmas 1–5 are untouched.** In §0, hypothesis 7 is described as "the product form of the target
given the classes". That matches its text ("conditional record laws that depend on label and class
only") and does not change it.

## 4. Statuses

- Results of `CONFIRM-r2.md` §6 that the check confirmed (§9.1, §9.2, Lemma S, Corollary S1, the
  Remark, Proposition E for Q5′, Q3′ and Q6′ failure, the two-round class-level example, the
  duplicated-slice removal) are labelled "one author, one independent check". **Correct.**
- All eight items of the check's §8 are listed in r4 §9's status paragraph as "one derivation, not
  checked". Where they are used (Proposition M and its countercase, E′, Q2 failure, the `1/296` and
  `(2 − √3)/72` bounds, the unrestricted-form reduction), they carry that tag. **Correct.**
- None enters the proof of Theorem 1, and r4 §9 and §9.5 say so. None is presented as verified in
  r4. **`SUMMARY-r4.md` states Q2 failure without its status** (F3).

## 5. Scoped verdict (r4 §9.6, headline, §0; `SUMMARY-r4.md`)

| Authorization item | r4 | Finding |
|---|---|---|
| A, B, C fail Q5′ under the stated additive-rule/target/record conditions | §9.6 item 1, headline, §0, §6 | matches |
| L5.4–L5.6 decided only within that scope | item 2, headline, §6, prior art | matches |
| not a rule-independent interface no-go | item 3, headline, §0, §7 item 2 | matches. "Specific to additive dynamics" should carry "through property (T)" everywhere it appears (F2), and item 3's "the interface does not make every pair-form rule fail" needs the mode in which that holds (F2) |
| rule-free lemma definitional | item 4, §9.3 | matches. "Evidence about no rule" understates Lemma S's role as a necessary condition (F4) |
| non-additive example witnesses only Q5′, fails other conditions, not class D | item 5, §9.4, §6 | matches in r4. In the summary, "fails the other conditions" is unqualified (F3) |
| retained memory compatible with selection under the fixed label-independent split | item 6, §9.5 | matches, correctly tagged not checked |
| rounded non-linear rule, gate question, other record conventions, class D open | item 7; summary "Still open" | matches |

## 6. README

The new rows and the "Revision r4" paragraph match the files: four changed files, rows 3, 5 and 6
adapted, the frozen files unchanged, the status labels, and r4 unreviewed. Two points remain (F8):
the file table still calls `L54-r3.md` "The final text", and "five are applied as worded" is
slightly generous for K1 (one added sentence). The pre-existing verdict row "Theorem 1 then holds
unchanged" (from da393029, not in this diff) states a checker addition without its status. It is
listed under F8 as optional.

***

## Findings, with replacement text

**F1 (Medium; `L54-r4.md` §9.3, Lemma S hypothesis (S5); `RESPONSE-CHECK.md` row 2).** r3 had both
cross tests. r4's "on a cross test" does not cover its statement "for each read label `c_v`".
Steps 3–5 of the proof determine `x^in_v` only from the cross test whose *second* label is `c_v`.
With `(c_a, c_b)` alone, `x^in_a` is not obtained. The change is not recorded in the crosswalk.
Replace

> (S5) one state credited at `ε < 1/32` on a cross test and on the test in which the conclusion is wanted;

by

> (S5) for the label `c_v` in the conclusion, one state credited at `ε < 1/32` on the cross test `(c_u, c_v)`, `u ≠ v`, and on the test in which the conclusion is wanted (for both read labels: the tests `(c_a, c_b)` and `(c_b, c_a)`, as in `CONFIRM-r2.md` (S5));

and append to row 2's "Change made" cell: "(S5) is restated in the checker's form (h5)
(`CHECK-RULEFREE.md` §3.1), keeping the cross test that ends in `c_v`."

**F2 (Low; `L54-r4.md` headline line 4–5, §0, §9.6 item 3; `SUMMARY-r4.md` "What it is not").**
The check's outcome (i) holds only in the (T) form. Any rule with (T) fails (Lemma 5), and at `τ = 1`
in initial-condition mode every pair-form rule fails (Corollary S1). Headline: replace "The
obstruction is specific to additive dynamics; it is not a rule-independent interface no-go (§9.6)."
by

> The obstruction is specific to additive dynamics through property (T) (Lemmas 1 and 5); it is not a rule-independent interface no-go (§9.6).

§9.6 item 3: replace "the interface does not make every pair-form rule fail Q5′ (Proposition E, one
author, one independent check)." by

> the interface does not make every pair-form rule fail Q5′: in exchange mode under H-write a designed rule passes (Proposition E, one author, one independent check); the exception is the `τ = 1` initial-condition corner of Corollary S1, a property of the definitions.

Summary: replace "It is specific to additive dynamics, not a no-go for every rule under this
interface." by "It is specific to additive dynamics, through a property additivity implies, and is
not a no-go for every rule under this interface."

**F3 (Low; `SUMMARY-r4.md` "What it is not").** Q2 failure is a checker addition with no check, and
Q1 was not examined. Replace "A designed non-additive rule outside the schema meets Q5′ (one author,
one independent check); it fails the other conditions and is not in class D" by

> A designed non-additive rule outside the schema meets Q5′ in exchange mode under H-write (one author, one independent check); it fails Q3′ and Q6′ (one author, one independent check) and Q2 (one derivation, not checked), and is not in class D

**F4 (Low; `L54-r4.md` §9.3 end of Corollary S1 paragraph).** K7 itself calls Lemma S "a
constraint on every pair-form rule", and the Remark uses it to bound R-lin. Replace "and they are
evidence about no rule." by

> and neither shows by itself that any rule fails, outside the `τ = 1` corner; Lemma S remains a necessary condition every pair-form rule must meet.

**F5 (Low; `L54-r4.md` §9.2 last sentence; unaccounted writer addition).** Neither result implies the
other. R1 gives two configurations at `1 − 2ε` per first label. Lemma S gives one at `1 − 17ε`, and
only where `ε < 1/32`. Replace "R1 of §7 is a weaker form of the same constraint." by

> R1 of §7 is a related constraint from the same overlap (two configurations at `1 − 2ε` for each first label).

and record it in `RESPONSE-CHECK.md` row 1.

**F6 (Low; `L54-r4.md` §9.4 "Initial-condition mode").** This restores K8's "other `τ`". Replace "and
until it is checked this case is open." by

> and until it is checked the case `τ ≥ 2` is open (`τ = 1` is decided by Corollary S1).

**F7 (Low; `L54-r4.md` §9.4 Statement; `RESPONSE-CHECK.md` row 3).** After "(correction K3)." insert

> The full rule is at CF:285–294 with this completion, and is re-stated in `CHECK-RULEFREE.md` §4.1.

In row 3, replace "Proposition E's rule is now fully specified as cited" by "Proposition E's rule is
fully specified by CF:285–294 with this completion".

**F8 (Low; parent `README.md`).** In the file table, replace "`L54-r3.md` | The final text" by
"`L54-r3.md` | The revision before the independent check's corrections", and the r4 row's "r3 with
the independent check's eight corrections" by "The current text: r3 with the independent check's
eight corrections". In the r4 paragraph, replace "five are applied as worded" by "five are applied
as worded (K1 with one added cross-reference, K4 and K7 with status tags)". Optional: in the verdict
table, append "(Proposition M: one derivation, not checked)" to "and Theorem 1 then holds unchanged".

**F9 (Low; `L54-r4.md` standing line; `RESPONSE-CHECK.md` last line).** The disclosures say nothing
was edited, committed or pushed, but these files sit in commit `de22ceab` on the PR branch. In r4,
replace "no repository edit, nothing committed, pushed or posted." by

> no edit outside this directory and the parent README; the files reach the branch only as a WIP checkpoint commit, and nothing was posted.

In `RESPONSE-CHECK.md`, replace "nothing in the repository or either worktree edited, committed,
pushed or posted." by

> no file edited outside the four this revision adds or extends; nothing posted.

***

**Read.** The owner comment; at the head: `CHECK-RULEFREE.md` (whole), `RESPONSE-CHECK.md`,
`SUMMARY-r4.md`, `L54-r4.md` §§0, 6–9 and the diff against r3, `CONFIRM-r2.md` §6 (CF:175–445),
and the README diff and its review-status section. On `main`: `TUNE-1-STEP2-SESSION1.md` 280–287
and `TUNE-1-STEP2-PROPOSAL.md` 199–202. Commands: `git rev-parse`, `git status`, `git diff`,
`git log`, `git merge-base`, `sha256sum`, `diff`, `sed -n`, `grep`, `find`, `ls`, `wc`, and one `curl`
read of the GitHub API.

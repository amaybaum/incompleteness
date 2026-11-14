# Response to `CONFIRM-r4.md` (exact-head confirmation of `L54-r4.md` at `de22ceab`)

`L54-r5.md` and `SUMMARY-r5.md` apply the findings that concern r4's own text. `L54-r4.md`,
`SUMMARY-r4.md`, `RESPONSE-CHECK.md`, `CONFIRM-r2.md`, `CHECK-RULEFREE.md`, `CONFIRM-r4.md` and every
earlier file are unchanged. Changes that `CONFIRM-r4.md` asks for in `RESPONSE-CHECK.md` are
recorded here instead, since that file is kept as it was confirmed. Authorization: owner, PR #1288
comment 6875725169 (`amaybaum`, `OWNER`, 2026-11-14T10:12:13Z), paper-only revision. No proof step
of Theorem 1, Corollary 1a, Proposition 2 or Lemmas 1–5 changed.

| # | Finding | Check at source | Disposition | Location |
|---|---|---|---|---|
| F1 | (S5) of Lemma S reads "a cross test", which does not cover "for each read label `c_v`"; the r3 → r4 change was not recorded | Confirmed. The proof determines `x^in_v` from the cross test whose second label is `c_v` (`CHECK-RULEFREE.md` §3.1 (h5), proof steps 3–5); `CONFIRM-r2.md` (S5) names both cross tests `(a, b)` and `(b, a)` | **Applied**, replacement as given. **Crosswalk of the change and its reversal:** r3 §9 stated Lemma S "with one state credited … on the tests `(c_a, c_b)` and `(c_b, c_a)`". r4 §9.3 restated (S5) as "on a cross test and on the test in which the conclusion is wanted", taken from (h5) but without saying which cross test, and `RESPONSE-CHECK.md` row 2 did not record it. r5 restores the form the statement needs: the cross test ending in `c_v` for that label, hence both cross tests for both labels. This entry stands in place of the addition `CONFIRM-r4.md` proposes for `RESPONSE-CHECK.md` row 2 | r5 §9.3, Lemma S |
| F2 | "Specific to additive dynamics" should carry "through property (T)"; verdict item 3 needs the mode and the `τ = 1` exception | Confirmed against `CHECK-RULEFREE.md` §7.2 (i), Lemma 5 and Corollary S1 | **Applied** in the headline and verdict item 3 as given, and in the summary as given. Also applied, for "everywhere it appears", in §0 (with "in exchange mode under H-write" added to the Proposition E clause) and §7 assessment item 2 | r5 headline, §0, §7 item 2, §9.6 item 3; SUMMARY-r5 "What it is not" |
| F3 | The summary states the example "fails the other conditions" without status; Q2 failure is the checker's own | Confirmed (`CHECK-RULEFREE.md` §4.4 and §8) | **Applied**, replacement as given | SUMMARY-r5 "What it is not" |
| F4 | "Evidence about no rule" understates Lemma S's role as a necessary condition | Confirmed: K7 calls Lemma S a constraint on every pair-form rule | **Applied** at the end of the Corollary S1 paragraph as given. The same correction is made in verdict item 4, which said "not evidence about any dynamics" | r5 §9.3; §9.6 item 4 |
| F5 | Unaccounted sentence: "R1 of §7 is a weaker form of the same constraint" | Confirmed: R1 gives two configurations at `1 − 2ε`; Lemma S gives one at `1 − 17ε` for `ε < 1/32`; neither implies the other | **Applied**, replacement as given. Recorded here in place of `RESPONSE-CHECK.md` row 1: the sentence was a writer addition in r4, not part of K1, and r5 corrects it | r5 §9.2, last sentence |
| F6 | K8's "At other `τ`" was dropped, so "this case is open" covered `τ = 1` | Confirmed against `CHECK-RULEFREE.md` §9 K8 | **Applied**, replacement as given | r5 §9.4, "Initial-condition mode" |
| F7 | No pointer to the full rule of Proposition E | Confirmed: `CONFIRM-r2.md` lines 285–294 give the construction and the rule; `CHECK-RULEFREE.md` §4.1 restates it | **Applied** with the citation form `CF:n` = `CONFIRM-r2.md` defined in the inserted sentence. The `RESPONSE-CHECK.md` row 3 wording is corrected here instead: Proposition E's rule is fully specified by CF:285–294 with the K3 completion | r5 §9.4, Statement |
| F8 | Parent `README.md`: file table and the r4 paragraph; optional status tag on the verdict row | Not checked here: the README is not in this folder and not in this writer's remit | **Not acted on; passed to the coordinator** (see below) | — |
| F9 | Disclosure says "nothing committed", but the files are in commit `de22ceab` | Confirmed | **Applied in modified form**, with the coordinator's wording instead of the reviewer's: "no repository edit by the writer beyond the files of this revision; nothing pushed or posted by the writer". The `RESPONSE-CHECK.md` replacement is not made, because that file is kept unchanged; the same correction applies to its last line and is recorded here | r5 standing paragraph |

**Other changes in r5.** The title; the standing line (r4 confirmed at `de22ceab`, ACCEPT WITH
CHANGES; r5 applies those changes and is itself unreviewed); the review-attribution sentence (the
first review and `CONFIRM-r2.md` by one reviewer, `CONFIRM-r4.md` by a further non-author who
re-derived nothing); "No proof step of Theorem 1 changed in r2–r5"; §8 item 7 ("r5 as a whole has
not been reviewed"); SUMMARY-r5's status line.

**For the coordinator (parent `README.md`, F8).** Proposed by `CONFIRM-r4.md`, not applied by this
writer:
1. File table: "`L54-r3.md` | The final text" → "`L54-r3.md` | The revision before the independent
   check's corrections"; the r4 row's "r3 with the independent check's eight corrections" → "The
   current text: r3 with the independent check's eight corrections" (with r5 now present, the
   current text is `L54-r5.md`, and the table needs rows for r5, SUMMARY-r5, `CONFIRM-r4.md` and this
   file).
2. r4 paragraph: "five are applied as worded" → "five are applied as worded (K1 with one added
   cross-reference, K4 and K7 with status tags)".
3. Optional: in the verdict table, append "(Proposition M: one derivation, not checked)" to "and
   Theorem 1 then holds unchanged".

**Reading and disclosure.** Read: `CONFIRM-r4.md`, whole; `CONFIRM-r2.md` lines 285–294;
`L54-r4.md` at the passages each finding cites; `CHECK-RULEFREE.md` §§3.1, 4.4, 7.2, 8, 9 (read for
r4). Commands: `ls`, `sha256sum`, `wc`, `sed`, `grep`, `cut`, `cp`, and Python text substitutions
that build `L54-r5.md` from `L54-r4.md` and `SUMMARY-r5.md` from `SUMMARY-r4.md`. No computation on
any OI rule or model. No repository edit by the writer beyond the files of this revision; nothing
pushed or posted by the writer.

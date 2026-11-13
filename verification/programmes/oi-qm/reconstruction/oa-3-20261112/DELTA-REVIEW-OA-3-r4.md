# Delta review of OA-3 r3 → r4

**Reviewer standing.** Focused exact-text delta review, read-only and paper-only: no computation, no
commit or push, no GitHub write.

**Objects.**

| Short form | What it names |
|---|---|
| r3 | `OA-3-REPORT-r3.md`, blob `ad0756ca` (committed on `research/oa1-w1-1-20261112`) |
| r4 | scratchpad `oa3/OA-3-REPORT-r4.md`, blob `b6164dd6` (checked with `git hash-object`) |
| `OA2:n` | OA-2 r3 at `815d6a8e`, as in OA-3's citation forms |
| `OA2r4:n` | `OA-2-REPORT-r4.md` at `4b087b1e` |
| `DR2` | `DELTA-REVIEW-OA-2-r3.md` at `4b087b1e` |

`diff r3 r4` has four hunks:
- the title, with the new Standing (r4) block;
- r3:358–359 → r4:362–364 (N3, Node 4);
- r3:748–749 → r4:753–754 (Disagreements, D1);
- the appended "Change map r4" (r4:819–832).

Nothing else changed.

## Verdict: **ACCEPT WITH CHANGES**

The two edited sentences are correct as far as they go. Three points need changes:

- **Scope of "another model".** One more clause inherits (CVX) and is left unconditional.
- **Proposition B "for every law".** One unedited sentence still asserts every part of Proposition B
  for every law, which OA-2 r4 no longer does.
- **Citations.** The (CVX) citation points to the status row rather than to the statement, and the
  form `OA-2 r4 §3.3` is not defined.

No conclusion, quantifier or label of OA-3 moves under the edits below.

## 1. Checks

**(1) The (CVX) qualifier and "with or without (CVX), this proof route fails".**

- **The hypothesis.** OA-2 r4 states (CVX) in Proposition B(ii): in the display (OA2r4:249–250) and as
  proof step 4 (OA2r4:280–283). The wording is "the available effects are closed under mixing with
  weights in `q^{−m}ℤ`, realized by a coin independent of, and not read with, the prepared cells".
  §3.3 (OA2r4:747) records where (CVX) holds: "where a cell uniform, independent of the prepared cells
  and not otherwise read serves as the coin (𝔊_K's bath is one); not shown for native rules".
- **The citation.** The edits cite only "OA-2 r4 §3.3" for the hypothesis itself. That points to the
  status row, not to the statement. "Closed under mixing" is an acceptable shorthand, but it drops the
  independent coin, which is the content that §3.3 says is not shown for native rules such as `G_SM`.
  → **R1**.
- **"With or without (CVX), this proof route fails": true.** With complete effects, `ρ` is injective
  iff `W = ℝ^U` (r4:361; linear algebra). So `W ⊊ ℝ^U` removes (⇐)'s hypothesis, and the route
  through B(i) and B(ii) (⇐) (r4:335–338) is unavailable whatever holds of (CVX). This agrees with
  DR2 §2.5 ("'This proof route fails' needs only that (⇐) does not apply").
- **Defect.** The next sentence, r4:364–365, reads: "Embeddability then rests on another model, and
  is not decided here".
  - "Then" now follows "with or without (CVX)". "Rests on another model" holds only under (CVX). That
    hypothesis is what makes the configuration model contextual.
  - Without (CVX), the configuration model can be measurement-noncontextual even though `ρ` is not
    injective. OA-2 r4's own two-point example shows this (OA2r4:293–294).
  - "Not decided here" holds either way.
  - The Change map r4 says the conclusions do not use (⇒). That is true of "fails" and "not decided"
    but not of "rests on another model". DR2 §2.5 did not name this clause, but it inherits (CVX) for
    the same reason. → **R1**, **R4**.
- **D1 (r4:752–754).** D1 has no "another model" clause. Its conclusion "the proof route fails" is
  correct with or without (CVX). Only its citation and line length need changes. → **R2**.

**(2) Other OA-3 text that uses or asserts B(ii) (⇒).** I grepped r4 for "Proposition B", "(⇒)",
"OA2:730" and "B′".

- **Uses.** Only r4:362 and :753 use (⇒). Theorem S uses B(i) and B(ii) (⇐) only (r4:335–340).
  - E(b) step 5 also uses only (⇐) (r4:465).
  - The ELABORATING labels (r4:384, :621, :641) rest on (i) and (⇐).
  - §1's definition list (r4:107–109) only names Proposition B.
  - Corollary B′ (OA2:301–312) does not rest on (⇒).
- **Assertion.** r4:348, in N3's "Measure" bullet, reads: "Proposition B holds for every law
  (OA2:730)". OA2:730 is OA-2 r3's §3.3 row. OA-2 r4 splits that row: B except (ii) (⇒) holds for
  every law (OA2r4:746), while (⇒) "needs (CVX)" under μ-G and is "not established" under μ-R and μ-O
  (OA2r4:747).
  - The sentence does not use (⇒).
  - It does assert (⇒) for every law, which OA-2 r4 no longer does.
  - Theorem S's measure scope is unaffected, because it needs only the parts that still hold for every
    law. → **R3**.

**(3) Nothing else changed, and nothing moved.** The four hunks are the only differences. The r3
Standing block is kept beneath the new r4 block and still reads as r3's record, which is acceptable.
The following are unchanged:
- every verdict;
- every label (NEW, ELABORATING, CONFIRMING, OPEN);
- every quantifier (any initial law under (PT); μ-G and μ-O for every stage);
- every effect class (MP-0b, V-ii-H, V-ii-U).

Two wording points in the Standing (r4) block:
- **"Required by `DELTA-REVIEW-OA-2-r3.md`".** DR2 §2.5 says "flagged so that OA-3's next revision
  carries the hypothesis". "Flagged in … §2.5" is the exact wording.
- **"r1–r3 are unchanged"** is ambiguous between the files and the r1–r3 text. Both fixes are in
  **R4**.

**(4) Citing OA-2 r4 beside OA-2 r3 line numbers.** Mixing the two is acceptable.

- `OA2:n` stays pinned to OA-2 r3 at `815d6a8e`, and every existing `OA2:n` citation remains accurate
  for the r3 text it cites.
- "OA-2 r4 §3.3" is not a defined form and names no commit. A citation-form note is needed. To keep
  r4's change local, it can go in the Standing (r4) block as `OA2r4:n`. → **R4**.

**(5) Line length.** r4:364 is 121 characters and r4:754 is 169. In this file, prose lines that run
past about 100 characters are wrapped, and only table rows are long. Reflowing these two lines is
cheap, and R1 and R2 below do it.

## 2. Required edits

**R1 (N3 Node 4).** Replace r4:362–366, from "`W ⊊ ℝ^U`, Proposition B(ii) (⇒)" through "short preparations
is not decided.", with:

```
    `W ⊊ ℝ^U`, Proposition B(ii) (⇒) (OA2:257–275), under its hypothesis (CVX) that the available
    effects are closed under mixing by an independent coin (OA2r4:280–283; not shown for native
    rules, OA2r4:747), makes the configuration model measurement-contextual, and embeddability then
    rests on another model. With or without (CVX), this proof route fails, and embeddability is not
    decided here (OA2:276–278). Whether `W ⊊ ℝ^U` actually occurs for a given initial law with
    short preparations is not decided.
```

**R2 (Disagreements D1).** Replace r4:753–756, from "Proposition B(ii) (⇒) (OA2:257–275), under its
hypothesis" through "is disputed.", with:

```
  Proposition B(ii) (⇒) (OA2:257–275), under its hypothesis (CVX) (OA2r4:280–283, :747), makes
  the configuration model measurement-contextual; with or without (CVX), the proof route fails. r2
  therefore states the generalization under (PT) (N3) rather than "for every μ" unqualified, and
  conditions amendment 2's MP-0a admissibility on (PT). No other required change is disputed.
```

**R3 (N3 Measure bullet, r4:348).** Replace "Proposition B holds for every law (OA2:730)." with
"Proposition B(i) and B(ii) (⇐), the parts the proof uses, hold for every law (OA2:730;
OA2r4:746)."

**R4 (Standing (r4) block and Change map r4).**

Replace r4:3–5 with:

```
**Standing (r4).** WIP / UNVERIFIED. r4 carries OA-2 r4's hypothesis (CVX) for Proposition B(ii) (⇒)
into the passages that use (⇒) (N3 Node 4; Disagreements D1), as flagged in
`DELTA-REVIEW-OA-2-r3.md` §2.5, and restricts N3's Measure bullet to the parts of Proposition B the
proof uses. `OA2r4:n` = line `n` of `.../oa-2-20261112/OA-2-REPORT-r4.md` at `4b087b1e`. The files
`OA-3-REPORT.md`, `-r2.md` and `-r3.md` are unchanged. r4's edits were given a focused delta review,
`DELTA-REVIEW-OA-3-r4.md` (ACCEPT WITH CHANGES, R1–R4), whose edits are applied here; those edits
are unreviewed.
```

This replacement contains the sentence that replaces "r4's edits await a focused delta review."
On its own, that sentence is:

> r4's edits were given a focused delta review, `DELTA-REVIEW-OA-3-r4.md` (ACCEPT WITH CHANGES,
> R1–R4), whose edits are applied here; those edits are unreviewed.

In "Change map r4", replace the paragraph at r4:824–826 with:

```
`DELTA-REVIEW-OA-2-r3.md` §2.5 found that OA-2's general proof of Proposition B(ii) (⇒) needs
hypothesis (CVX) (available effects closed under mixing by an independent coin); OA-2 r4 states it
(OA2r4:280–283) and records where it holds (OA2r4:747). The passages that use (⇒) now carry it.
"This proof route fails" and embeddability "not decided" do not use (⇒) and are unchanged;
"embeddability then rests on another model" uses it and is now stated under (CVX).
```

Then add two rows to its table:

```
| Theorem S, Measure bullet: Proposition B restricted to (i) and (ii) (⇐) (OA2r4:746) | §2 N3, "Measure" bullet |
| Delta review `DELTA-REVIEW-OA-3-r4.md`, R1–R4 | Standing (r4); N3 Node 4 and Measure bullet; Disagreements D1; this map |
```

## 3. Optional

- **O1.** After R1–R3, the Change map row "Title and Standing (r4) | :1; :3–5" will need its line
  range updated to the final block, :3–9.

**Confirmation of r4 (blob `b65e6d9c`): ACCEPT.** I compared `.r4-pre.md` (blob `b6164dd6`) with
`OA-3-REPORT-r4.md`, and the diff is exactly R1–R4 and O1 as written above, with nothing else changed.

- **R3.** It stands on a single line, :352. Reflowing it is optional.
- **Standing.** The block should record this confirmation. In it, replace "whose edits are applied
  here; those edits\nare unreviewed." with:

  > whose edits are applied here verbatim, as confirmed in that review; the edits are the reviewer's
  > own text and have not been reviewed independently.

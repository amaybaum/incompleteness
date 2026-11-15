# Confirmation of change map A1C r6-min

**Reviewer.** The independent reviewer of r1–r5. Paper-only: nothing in the repository was edited, committed, pushed or posted, and no Lean, build, guard or census run was made. Base: the worktree of `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`.

## Verdict

**CONFIRMED WITH NITS.**
- R1, R2, N1 and N2 are applied correctly and minimally. Each adds no claim and keeps A1 open, neither established nor disproved.
- Declining the four recommended sites is acceptable under the policy.
- The r5 → r6 diff introduces no new error.
- The counts are right.
- One stale sentence remains in the header (nit 1).

## 1. R1, R2, N1, N2

All four left-hand quotations match the text at the base.

| Item | r6 row | Check |
|---|---|---|
| R1 | N-G04 (GR:58) | Correct. H-count becomes "that the total system is finite (A1) and that the energy-dependent entropy of the whole hidden sector at the shell scale is the boundary count", so A1 is a conjunct, not a scope limit. Every result stated "under H-count", or citing GR §8.5(b) (whose own text says "If, in addition, H-count holds …"), now visibly requires A1. The first-sentence fix ("Under A1, restrict …") is kept. H-count stays a hypothesis: the only sentence that speaks of H-count holding is GR:673, and it is conditional ("if in addition H-count holds"). No text asserts H-count, so no text asserts A1. |
| R1 | N-K07-52 (ch07:52) | Correct mirror, with the same conjunct. |
| R2 | N-K07-16 (ch07:16) | Correct. "…and satisfying H-slope and H-count (Section 7.3) at its horizon" is one clause, adds no claim, and points to the section that defines H-count. |
| N1 | N-P03 (Computation:118) | Correct. The name "total-finiteness posit" is kept with the single status phrase "an open hypothesis, not adopted". "would take $S$ finite" keeps the sentence conditional. |
| N2 | N-K09-106 (ch09:106) | Correct and minimal. "— as a claim about nature, the open hypothesis A1, not adopted" separates the class condition of ch09:104 (left unedited) from A1's status for nature. |

## 2. The four declined sites

Each still states only "conditional on H-slope", but each points to where H-count, which now carries A1, is defined:

- **glossary:73:** "Developed in Chapter 7 §7.3", the section containing ch07:52. The pointer reaches H-count.
- **ch07:305:** "(Sections 7.3–7.4)", which includes §7.3. It reaches.
- **Substratum:195:** directly follows Theorem 23 (Sub:193), whose calibration clause reads "conditional on H-slope and the further conditions of [GR §8.5(b)]". It reaches in one hop.
- **glossary:17:** "fixed by the horizon calibration of Chapter 7 (conditional on H-slope) … Developed in Chapter 7 §7.5". This is the weakest pointer: §7.5 does not contain ch07:52, and "the horizon calibration of Chapter 7" names the calibration rather than a section. A reader who follows it reaches ch07:12, whose condition list names H-count. So it reaches in two steps.

The omission of the name H-count at all four sites predates A1. The pointers carry A1 to a reader who follows them. Under Q11 (a) and the minimum-change policy, the writer's decision not to edit them is acceptable.

Optional (nit 2): glossary:17 could take "and H-count", given its weaker pointer. It is not required.

## 3. Diff r5-min → r6-min and recount

The diff changes only the status line, the OQ-2 header row, the counts line, N-G04, N-P03, N-K07-52, the new N-K07-16, N-K09-106 and the new Part J. Each change traces to R1, R2, N1, N2 or the recommendation. No other row moves.

**Nit 1.** The OQ-2 header row still describes the anchor in its r5 form: 'H-count "for a finite total system (A1)"'. The same cell then says "H-count carries A1 as a conjunct, not as a scope limit", and N-G04 is in the conjunct form. Update the parenthesis to the N-G04 wording, so the map does not describe the superseded scope form.

**Recount.**
- Part A: 133 rows (119 K, 14 C); no duplicate IDs.
- Part F: 244 drops, unchanged.
- Part H: 235 rows (120 corrected, 115 not unsupported), unchanged.
- Part E: 20 splits, unchanged.

The map's figures are confirmed.

**Registry.** No change. GR:58's bold lead is a paragraph title, not a census statement, and ch07:16 and ch07:52 are book text. N-D2d (Main:760) remains the only ledger re-affirmation.

## What I could not check

- No guard, census, coverage or build run.
- The reach analysis rests on the calibration-statement search described in the r5 recheck. A statement of the calibration in words, without those patterns, would not have been found.

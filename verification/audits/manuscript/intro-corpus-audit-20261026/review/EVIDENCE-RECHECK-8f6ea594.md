*Recorded by the coordinator from the independent reviewer's report, verbatim. `S` in paths below is the session scratch directory, not retained.*

# Re-check 2: the step-7 evidence layer at 8f6ea594 (the author's response to RECHECK.md)

Reviewed object: `audit/intro-corpus-20261026` at `8f6ea5948407c2a5deb375d34bccd758b24da406` (parent 818bcd60), in a
fresh detached worktree. `AUD` below is `verification/audits/manuscript/intro-corpus-audit-20261026/`, and `E4` is
`AUD/evidence/scripts/E4_aggregate.py`. The review was read-only: no commits, pushes, comments or dispatches. Every
statement below was checked against the code and the data, not the commit message. The commit touches no file under
`papers/` or `book/`.

## Verdict: ACCEPT WITH CHANGES

- N1, N2 and N3 are resolved.
- All five optional items I raised are resolved.
- An independent re-implementation agrees with `evidence.json` on all 409 rows.
- The full pipeline regenerates every artifact byte for byte, and all three `--check` modes pass.

One required change remains (C1 below). It is a one-line fix to an incorrect gap text in EVIDENCE.md, and it changes
no level. Two small optional items follow it.

The levels are now 44 reproduced, 127 certificate-checked, 235 traced-only and 3 failed, matching the commit message.

## N1–N3

| Item | Status | Evidence (file:line at 8f6ea594) |
|---|---|---|
| N1 | **Resolved** | See below. |
| N2 | **Resolved** | See below. |
| N3 | **Resolved** | See below. |

### N1: the four relabels to paper-derivation

- The relabels for I-042, I-052, I-258 and I-281 are removed. `matrix/chain-relabels.json` now holds only I-063,
  I-282, I-309 and I-044, and its `_note` explains why.
- The links are back on the kernel layer. With their paper-line sources, they match no item. The gap reads "kernel-layer link without a declaration source; no item names its file" (EVIDENCE.md:81, 83-84, 95).
- I-052 and I-258 are now traced-only, basis "unmatched kernel". I-042 and I-281 were traced-only already and stay
  so. I-281's artifact level drops from certificate-checked to traced-only.

### N2: I-227

- The new clause is in `contradicted()` (E4:96-110). A computation link that names manuscript lines and no record or
  probe is matched only by an item that names the same manuscript file.
- I-227 links 0 (GR.md:833) and 2 (book ch07:126) are now unmatched. Link 1, the BHb record, still matches E2-07 and
  E3-18, and I-227 is traced-only.

### N3: the chain drift checks

- `merge_matrix.py --check` (`merge_matrix.py:89-95`) compares `matrix.json` with the merge of the parts.
- E4 `--check` (E4:422-431) checks that every relabel is applied, with `layer`, `mapper_layer` and `source` all
  matching. It also checks that the number of relabelled links equals the number of entries.
- My mutation runs follow.

| Mutation | E4 --check | render --check | merge --check |
|---|---|---|---|
| baseline | pass | pass | pass |
| row level changed in matrix.json, counts updated | FAIL | FAIL | FAIL |
| row basis changed | FAIL | FAIL | FAIL |
| chain layer edited in matrix.json | FAIL | pass | FAIL |
| relabel `to` edited | FAIL | pass | FAIL |
| relabel edited, then E4 regenerated (my RECHECK.md N3 case) | FAIL | pass | FAIL |
| relabel removed, then E4 regenerated | FAIL | pass | FAIL |
| relabel added, then E4 regenerated | FAIL | pass | FAIL |
| part-B3.json chain edited only | pass | pass | FAIL |
| part-B3.json chain edited, then E4 regenerated | pass | pass | FAIL |
| resolutions.json edited | pass | pass | FAIL |
| inventory claims.json text edited | pass | FAIL | pass |
| `not_covered` removed from E1-71 | FAIL | pass | pass |
| evidence.json row edited | FAIL | FAIL | FAIL |

Every mutation is caught by at least one of the three checks. Drift in the part files is caught only by `merge
--check`, so the three checks have to be run together. E4's docstring (E4:43-45) says so.

## The optional items from RECHECK.md

| Item | Status | Evidence |
|---|---|---|
| O-1, docstring | **Resolved** | E4:17-18 states the type restriction, with no part restriction, which matches E4:178. E4:30-32 states that a proved-kernel row's computation links are recorded without grading it. The manuscript clause is stated (E4:20-22). The EVIDENCE.md rule text matches. My literal re-implementation of the new docstring gives 0 differences (below). |
| O-2, I-088 reason | **Resolved** | The reason now reads "not the finite order of the bijection", and E1-98's limits name I-088 and I-089 apart. `E1_build_part.py` and `part-E1.json` hold identical strings: I extracted the dict with `ast` and compared, and the four rows (I-129, I-088, I-149, I-071) and their texts are identical. |
| O-3, I-149 | **Resolved: conservative** | E1-71 now carries `not_covered` for I-149 (`part-E1.json:1837`), so I-149 is traced-only. The reason says the cocycle condition is vacuous. Because it is vacuous, the kernel's witnesses satisfy "compose exactly" trivially, so "covered (vacuously)" would also have been defensible. Not covered is the safer reading, and I accept it. |
| O-4, E2_bh02 permutation not applied | **Resolved** | CC-c (`E2_bh02.py:62-94, :138`) counts the (permutation, configuration) pairs whose orbit has length 1, and requires that count to equal N!. The count is the sum of fixed points over all permutations, which is N!. My mutant that never applies the permutation now gives 96 and 322,560 against 24 and 40,320, so the controls fail (`controls_fire` false). The leak and mixing mutants also fail CC-c (18 and 35,280). The unmutated run gives 24 and 40,320, and every check is true. |
| O-5, b5_check exit | **Resolved** | `b5_check.py:222-225` exits 1 when a countercontrol, or the a/(2−a) check, fails. Three mutants (CMI conditioned on X0, `c3 := a/(1+a)`, `c3 := 1 + a/(2−a)`) each exit 1. The unmutated script exits 0. |
| O-6, E2-11 scope | **Resolved** | `failure_scope` (`part-E2.json:227`) now reads "fails on one reading of L30: 'exhaustive' as exhaustive over a class of laws". I-071's and I-054's bases carry it. |
| O-7, I-384 and I-385 listing | **Resolved** | E3-16 lists both (`part-E3.json:334-335`). E3-17, the BH-01 review chain, lists I-384 (:372). E3-18, BH-02, lists I-385 (:403). Each record is listed by its own item. Both rows are graded on their chains of none links, and both are *reproduced*: E3-16, E3-17 and E3-18 regenerate what they check, with git trees, sha256 and the replay. I-044, a claim of the same kind, stays certificate-checked because E3-19 also lists it. This follows the weakest-item rule. |

## Points checked for new defects

### The manuscript-path rule in `contradicted()`

- I compared every link of every row between 818bcd60 and 8f6ea594. The rule changes exactly three links:
  - **I-227 links 0 and 2:** they lose E2-07 and E3-18, which name neither GR.md nor book ch07. This is correct (N2).
  - **I-193 link 1** (book ch07:191-193): it loses E2-17, which does not name ch07, and keeps E2-18, which does. The
    link stays *reproduced*. This is correct: E2-18 is the item that names the book's convention range.
- No other link changes. My re-implementation without the clause differs from `evidence.json` only on I-227.
- The match is by file, not by line. An item that names one line of `papers/Main.md` matches a link to another line
  of the same file. I checked the cases where the lines differ:
  - I-355 and I-357 cite Main.md:606, while E2-12 names Main.md:178-198;
  - I-366 cites Introduction.md:247, while E2-12 names Introduction.md:219-253.

  Main.md:606 states the same XOR example with "I(X_0;X_2|X_1) = 1 bit" that E2-12 checks for B.2, so the matches
  are right. Today no level depends on the match being by file; see O-b.

### E2-12's added book source

`part-E2.json:269` adds `book/ch01-observation.md:277-280@eae01647`. I read ch01 at eae01647. Lines 277-280 are the
table rows under the header at line 275:

| Line | Book row | Value |
|---|---|---|
| 277 | one shuffle, then showdown | 1/2 |
| 278 | two shuffles, then showdown | 1 (certain) |
| 279 | two shuffles, odds chained through the unobserved middle | 1/2 |
| 280 | two shuffles with a peek (and forced re-burn) in the middle | 1/2 |

These are the four values of the Introduction's table (I-361 to I-364), in a different row order: the book puts the
chained (Markov) row before the peek row.

- The book's peek is the overwriting peek ("forced re-burn"). That matches E2-12's computation that the overwrite peek
  gives 1/2 (I-368).
- E2-12's statement "(1/2, 1, 1/2 chained through the middle, 1/2 with a peek)" is accurate.
- The link I-361 to I-364 cite, "ch01:265 (table at ch01:277–280)", now matches E2-12 through `book/ch01-observation.md`. Those rows keep *reproduced*, which is correct.

### `merge_matrix.py --check` and E4's relabel check

See the mutation table under N3. One gap: `merge --check` fails on `missing` rows but not on `extra` ones. Because the
check compares bytes, an extra row also shows up as a difference, so this is not a hole.

### `b5_check.py`'s new exit path

- It exits correctly on a failed control.
- The values the script prints are not themselves asserted. A mutant that sets B2 to `cmi(J) + 1` prints 2 and
  exits 0.
- This is acceptable. `E2_appendixB.py`, which is independent, asserts every value through its `ok` flags, and
  b5_check is the audit's own cross-check.
- The values are also printed before the exit, so a failed run still prints them, followed by the failure message.

## Required change

**C1. The gap text for I-227 is wrong.**

- **Location:** E4:162-163. Rendered at EVIDENCE.md:93-94.
- **What is wrong:** for I-227 links 0 and 2 the gap reads "no computation item for this link (listed items name other
  records or probes: E2-07, E3-18)". These links name no record or probe. E2-07 and E3-18 are rejected under the new
  manuscript clause, because they do not name GR.md or book ch07. The published reason is therefore false.
- **Fix:** have `contradicted()` return its reason, or test which clause fired, and render "listed items do not name
  this manuscript file: …" for the manuscript case.

## Optional changes

**O-a. I-227's artifact level is now traced-only.**

- Links 0 and 2 still bear load and are unmatched, so the artifact level is the weakest over all three links.
- The fact that E2-07 and E3-18 reproduced the sweeps cited at link 1 is therefore not recorded at row level.
- I-216, which has the same pattern, records artifact level *reproduced*, because its proof link is `paper-derivation`
  and does not count.
- As a result, I-227 is missing from EVIDENCE.md's "Traced-only rows whose checked artifacts reach a higher level".
- Either relabel I-227 links 0 and 2 as `paper-derivation`, as I first suggested, or note the difference.

**O-b. The manuscript clause matches by file, not by line.** No row's level depends on this today. Stating it in the
rule, or matching line ranges, would stop a future item that names one passage of a paper from reaching a link to
another passage.

## Independent re-implementation

`scripts/reagg3.py` imports only `json`, `re`, `sys` and `collections`, nothing from E4. It implements the 8f6ea594
docstring as written: the type-restricted file-source matching, with no part restriction, plus the manuscript clause.

| Run | Differences from `evidence.json` | Counts |
|---|---|---|
| As written | 0 of 409 rows | 44 reproduced / 127 certificate-checked / 235 traced-only / 3 failed |
| As written, file-source matching restricted to E1 and E3 | 0 | same |
| Without the manuscript clause (`reagg2_typed.py`) | 1: I-227 (reproduced against traced-only) | — |

No failed row has an open, conditional, conjecture or unsupported status.

The level changes from 818bcd60 to 8f6ea594:

| Row | Level change |
|---|---|
| I-052, I-258 (N1) | certificate-checked → traced-only |
| I-149 (O-3) | certificate-checked → traced-only |
| I-227 (N2) | reproduced → traced-only |
| I-384, I-385 (O-7) | traced-only → reproduced |
| I-281 | level unchanged; artifact level certificate-checked → traced-only |

## What I ran

All runs used `python3 -I -B`.

| Check | Result |
|---|---|
| `E4_aggregate.py --check`, `render_matrix.py --check`, `merge_matrix.py --check` at 8f6ea594 | All pass. |
| Full pipeline from scratch: evidence.json, EVIDENCE.md and MATRIX.md deleted, then merge → E4 → merge → render | All four files byte-identical. |
| Drift mutations, `scripts/mutate2.sh` | Table under N3; output in `outputs/drift-mutations-2.txt`. |
| All eight `E2_*.py` scripts | All exit 0. Seven give output byte-identical to their 818bcd60 runs. `E2_bh02` adds CC-c (24 and 40,320, true), with `all_as_reported` true. |
| E2_bh02 mutants, `scripts/bh02_mutants.py` | Output in `outputs/bh02-mutants-2.txt`. All five mutants caught, including the one that does not apply the permutation. |
| b5_check exit path, 4 mutants | Output in `outputs/b5-exit.txt`. |
| Link-by-link comparison of `evidence.json`, 818bcd60 against 8f6ea594 | Every changed link and level is listed above. |
| Book ch01 at eae01647, lines 262-284 | Read against E2-12's statement and Introduction L242-245. |
| `NOT_COVERED` in `E1_build_part.py` against `part-E1.json` | Identical. |

**Files.** Reports and scripts are in
`S/rereview-e/`:

- this report, `RECHECK2.md`;
- `scripts/`: `reagg3.py`, `mutate2.sh`, `bh02_mutants.py` and the earlier scripts;
- `outputs/`.

The worktree `wt2` and the scratch copies were removed.

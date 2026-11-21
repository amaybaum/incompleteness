# A1-EXIT regression comparison (#1468): preregistration of the before/after comparison

**Status.** Writer's preregistration, WIP / UNVERIFIED. It is frozen before any after-state exists:
the A1 deletion has not been executed. Nothing here has been run against a Step-2 head or a deletion
head. The only runs were the baseline against itself and synthetic edits of the pinned corpus (§6).
Independent non-author review is required before use.

**Authorization.** Owner `amaybaum`, #1169 comment 7058783437, 2026-11-21T06:42:54Z: "**Regression
comparison: approved for preparation now.** The before/after comparison against the preserved baseline
is conditionally authorized once the deletion has been executed and independently reviewed. Its verdict
requires separate scientific evaluation." The same record: "Removing the global finiteness assumption
must not be presented as proof that the theory works for every infinite system. Each result keeps its
own mathematical conditions."

This record authorizes nothing further. Running §2 requires the condition quoted above: the deletion
executed and independently reviewed.

**Goal link (§A.47).** A1-exit objective (#1169), owner requirement 6 (#1169 c.7048255658): "A final
regression audit shows that removing A1 has not weakened, strengthened or changed any physical
prediction without explicit justification." This preregistration fixes the procedure and the decision
rules that will decide that. It does not decide the outcome.

**Baseline.** The read-only before-baseline of #1471, landed on `main` (merge `0adc410c`) in
`verification/audits/foundations/a1exit-regression-20261121/`. It is pinned at
`1c7eedc402eafd2bac654484fa790874a33f444d`, with snapshot sha256
`2db7832d7cb95b0ba77b42afad965696390d4ad67a6835b2c45f045bd04f88c8`. Drafting base for this record:
`main` at `7f28886f4cc96fbfa7407af1fdc37de2f0e562e5`, where all five Step-2 units have landed.

## 1. Frozen tools

`FROZEN.json` records the SHA-256 of three files:
- `baseline.py`: `e0749fb9…`;
- `snapshot.json`: `2db7832d…`;
- `compare/verdict.py`, the collection, classification and verdict tool.

Control C0 refuses a run in which any of the three differs. None of the three changes after this
record's review except by an amendment in `compare/amendments/` made before the comparison is run.

## 2. Procedure

**H.** The execution head is the commit the owner designates as the executed A1 deletion, after its
independent review.

**Checkout.** The tools are run from a checkout of `main` that contains this record. The deletion
branch is not used as the checkout. `verdict.py` writes into a working directory `DIR` outside the
repository.

1. **Collect.** Run

   ```
   python3 -I -B verification/audits/foundations/a1exit-regression-20261121/compare/verdict.py collect --head <H> --out <DIR>
   ```

   It runs, and records as exit statuses in `DIR/controls.json`:
   - C0, the frozen-tools check;
   - C4, `verdict.py self-test`;
   - C1, `baseline.py check`;
   - C2, `baseline.py self-test`;
   - C3, `baseline.py --compare 1c7eedc4…`, the baseline against itself;
   - the comparison itself, `baseline.py --compare <H> --json <DIR>/compare.json`;
   - the countercontrol C5 (§5).

   The comparison command and the schema of `compare.json` (`a1exit-regression-compare/1`) are those of
   `baseline.py` as frozen, specified in the baseline's amendment A1 (R1, R4, R6).
2. **Compile the justification sources** into `DIR/edits.json` (schema `a1exit-compare-edits/1`, §4).
   Then run `verdict.py check-edits --edits <DIR>/edits.json --commit <main commit>`. It must report
   0 edits not found in their source.
3. **Classify.** Every reported item of `compare.json` (§3) is entered in `DIR/classify.json`
   (schema `a1exit-compare-classify/1`) as J or R, with its cited edits and ledger row, or is left out,
   in which case it counts as U.
4. **Verdict.** Run

   ```
   python3 -I -B verification/audits/foundations/a1exit-regression-20261121/compare/verdict.py verdict --dir <DIR> --edits <DIR>/edits.json --classify <DIR>/classify.json
   ```

   It checks every J and R claim against the rules of §3, classifies the countercontrol run with the
   same files, and writes `DIR/verdict.json` (schema `a1exit-compare-verdict/1`). It prints the
   verdict text, which is generated from the counts. Exit status: 0 PASS, 1 FAIL, 3 PENDING, 4 VOID.
   The verdict is read from `verdict.json` and the exit status, never from log text (§A.44).
5. **Record.** `compare.json`, `controls.json`, `edits.json`, `classify.json` and `verdict.json` land
   in this directory under a result note. `--compare-tree` reports are not committed, because they
   name only a temporary tree.

The schemas are stated in the usage text of `verdict.py` and of `baseline.py`.

## 3. Decision rule for each reported change class

**Reported items.** The reported items are:
- every entry whose status is not `unchanged`;
- every entry that is `relocated`;
- every `unaccounted` line;
- every `deleted` line.

An entry moved within one file and otherwise unchanged is not reported (baseline amendment A1, R4).

**Classes.** Each reported item takes exactly one class:
- **J, justified by a landed Step-2 unit or by the deletion edit.** The citation names the unit's PR,
  the edit ID and the ledger row. `verdict.py` accepts J only when the citation passes the mechanical
  rule for every change kind the item carries (J1–J9 below).
- **R, needs scientific review.** The writer may mark any item R. An item whose J citation passes the
  string rule but fails J9, or that is relocated out of Main (J7), is R automatically. An R item is
  resolved only by an independent review recorded on the result PR. The resolution is entered as
  `{"outcome": "justified"|"unjustified", "review": <link>}`, and an unjustified outcome counts as U.
- **U, unjustified.** Every item that is not J or R. In particular, an item that is not classified,
  or whose citation fails J1–J8, is U.

**What counts as justification.** Let `e` be a cited edit with old string `o` and new string `n`, and
compare whitespace-normalized texts. `e` must come from §4's sources: one of the five Step-2 PRs or
the deletion edit. Its file must be the item's file. A chapter edit also covers that chapter's FULL
mirror.

| Rule | Change class | `e` justifies the item only if |
|---|---|---|
| J1 | text changed | `o` occurs in the baseline text and `n` occurs in the after text |
| J2 | value changed | J1, and every number token removed from the line occurs in `o`, and every number token added occurs in `n`: the reviewed edit changed exactly that value |
| J3 | label changed | J1, and J9 |
| J4 | removed | the baseline text lies within `o`, or `o` lies within the baseline text (a rewrite beyond the pairing threshold) |
| J5 | unaccounted | `n` lies within the line, or the line lies within `n` |
| J6 | deleted | `o` lies within the line, or the line lies within `o` |
| J7 | relocated | `o` contains the text in the source file, or `n` contains it in the destination file. Relocated from Main: never plain J, always R, because Main must stay independent of downstream papers (AGENTS.md, Code Review Rules) |
| J8 | several kinds | every kind the item carries is covered by a cited edit |
| J9 | label or scope | the cited ledger row is a row of the cited edit, and the after text matches the row's accepted disposition in the A1-EXIT ledger (`rows.json`): an F row keeps a finite-scope term; an O row carries an open, conditional or hypothesis term; a J row does not lose an open, conditional or hypothesis term that the baseline text had (no silent promotion). Otherwise R |

A justification that is not mechanically checkable, such as a reviewer's argument with no covering
edit, is R, never J.

**Scientific evaluation flag.** An item is flagged `scientific_evaluation` when it changes a physical
prediction or an empirical comparison. That means:
- its categories include C-TAB (prediction or status tables), C-PROSE, C-FINL, C-CDO, C-CAL, C-OBS or
  C-OPEN;
- or, for an unaccounted or deleted line, it carries the flag `numbers` or `marker`.

The flag is set whatever the class. A J item that is flagged is still listed for the separate
scientific evaluation that the owner record requires.

## 4. Justification sources (inputs)

All are on `main` at the drafting base, except the deletion edit list, which lands with the deletion.

| Unit | PR (merge) | Record | Edit strings |
|---|---|---|---|
| S2-A | #1470 (`0cd5d5bf`) | `verification/audits/manuscript/a1exit-s2a-20261121/` | `checks/s2a_edits.json` (base and amending entries) |
| S2-B | #1473 (`a1f38284`) | `verification/audits/manuscript/a1exit-s2b-20261121/` | `PREREG.md`, `amendments/A1-round1.md`, `A2-return-form.md`, `A3-cptp-register.md` |
| S2-C | #1474 (`0ba358cc`) | `verification/audits/manuscript/a1exit-s2c-20261121/` | `PREREG.md` §5, `amendments/A1.md`, and RESULT §9.1 (resolved catch-up lines) |
| S2-D | #1472 (`4de2eabd`) | `verification/audits/manuscript/a1exit-s2d-20261121/` | `PREREG.md`, `amendments/A1.md`, and RESULT §8a (catch-up) |
| S2-E | #1475 (`7f28886f`) | `verification/audits/manuscript/a1exit-s2e-20261121/` | `checks/s2e_edits.json`, `checks/s2e_amend1.json`, and RESULT §9 (catch-up) |
| Deletion | the executed deletion PR, from the plan of #1477 | `verification/audits/foundations/a1exit-deletion-20261121/` as landed | `edits.json` as landed with the executed deletion, unit `DEL` |

**Compiling the sources.** Each compiled edit records:
- `key` (`<unit>:<id>`), `unit`, `pr`, `id`;
- `file` and `files` (with the FULL mirror where the record names one);
- `old`, `new`, `rows`;
- `source_path`, the record file that holds its strings.

`check-edits` verifies each compiled edit against its source:
- **JSON source:** an object in the source file has the same `old` and `new`;
- **Markdown source:** both strings occur verbatim in the file.

An edit that fails this check cannot justify anything. Its items are U or R.

**What is not a source.**
- #1476 changed CI only and is not a source.
- Any manuscript change that reaches H from a PR not listed here has no source, so its items are U
  unless reviewed as R.

## 5. Controls

All must pass, or the verdict is VOID.

| Control | What | Pass condition |
|---|---|---|
| C0 | Frozen tools and baseline (`FROZEN.json`) | all three digests equal |
| C1 | `baseline.py check` at the run | exit 0 (snapshot regenerates byte for byte from the pin) |
| C2 | `baseline.py self-test` | exit 0 |
| C3 | Baseline against itself: `baseline.py --compare 1c7eedc4…` | exit 0, no change reported |
| C4 | `verdict.py self-test` (T1–T11 on synthetic data) | exit 0 |
| C5 | Countercontrol: H's corpus copied to a temporary directory, one unjustified value change injected (the first unchanged entry of a prediction table, the last digit of its first decimal token), compared with `--compare-tree`, and classified with the same `edits.json` and `classify.json` | the injected entry is U, and the U count is exactly the main run's U count plus one |

## 6. Verdict rule (owner requirement 6)

| Verdict | Condition |
|---|---|
| **VOID** | any control fails |
| **FAIL** | there is at least one U item |
| **PENDING** | there is no U, and at least one R item is unresolved |
| **PASS** | there is no U item, and every R item is resolved as justified by an independent review |

The verdict text is generated by `verdict.py` from the counts, in the form:
`VERDICT <v>: <n> reported changes; J <a>, R resolved as justified <b>, R unresolved <c>, U <d>;
<k> flagged for scientific evaluation; controls <pass|FAIL>; countercontrol <pass|FAIL>.`

**What PASS does not settle.** A PASS does not settle the flagged items. Every item flagged
`scientific_evaluation`, J or not, goes to the separate scientific evaluation the owner record
requires. A PASS is not presented as showing that any result holds for infinite systems; each result
keeps its own conditions.

**Preparation runs.** These were run in preparation, on the pin and on synthetic data only:
- `verdict.py self-test`: T1–T11 PASS;
- `verdict.py collect --head 1c7eedc4…`, that is, the baseline against itself: every control passed,
  C5 injected FULL:1642 `0.3183` → `0.3184`, and the verdict was `VERDICT PASS: 0 reported changes; …;
  countercontrol pass`;
- `check-edits` on a three-edit test list: it found the one altered edit.

No Step-2 head or deletion head was compared.

## 7. Limits

- The J rules are string rules. They show that a cited reviewed edit produced the change. They do not
  show that the edit is scientifically right; that is the job of the flag and of the separate
  evaluation.
- J9 checks scope and status terms against the ledger disposition lexically. Anything finer goes to R.
- The comparison inherits the baseline's limits (baseline RESULT §4). A prediction stated without a
  marker or number form is not an entry, but a change to it is still reported as a flagged
  `unaccounted` or `deleted` line.

## 8. Off-`main` references (§A.42 item 8)

| Reference | Claim | Classification |
|---|---|---|
| #1169 c.7058783437, c.7048255658 | Authorization, requirement 6 | provenance, quoted with author and time |
| #1477 and its branch | The deletion plan whose landed `edits.json` becomes a source | provenance now. Its edit list is used only as landed with the executed deletion; until then it is not a source |
| The preparation runs (§6) | The tool works on the pin and on synthetic data | provenance; the claim rests on `verdict.py self-test`, reproducible from `main` once this record lands |
| PR records #1470–#1475 | Justification sources | support on `main` (merges listed in §4) |

## 9. Verification status (§A.46 item 4)

- **Evidence level:** a preregistration with a tested tool. There is no result yet.
- **Missing:** independent review of this preregistration and of `verdict.py`.
- **Accountable Issue:** #1468.
- **Remaining gate:** the comparison runs only after the A1 deletion is executed and independently
  reviewed (owner record above). The verdict's flagged items need a separate scientific evaluation.

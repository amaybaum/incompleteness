# Guard repair round GR-2 — post-landing scoping of `R7-GR1`'s two live-tree assertions: RESULT

Executed from the certified merge of this round's control plane and from nothing else. The
execution's first act verified this round's preregistration blob at that base.

- **`B` (mandated execution base)** — `c9e6d56379923195382fa8c797c464397bcedaa5`
- **Freeze blob at `B`** — `f6438114f8b633b70bcc50b6cadd5eb94768e5a3` at
  `verification/infrastructure/round-gr-2-post-landing-scoping/preregistration.md`, verified
  before any edit
- **Shape** — NON-SEALING, `E` → `L`, no `P`. No manifest record, no prospective declaration, no
  baseline change; `GR1.json` remains owed to a later round that names it.

***

## `GR2-0` — the start state at `B`: HOLD

Read from git at `B`: both superseded segments present with their frozen hashes and each present
exactly once; `GR-1` `LANDED-UNRECORDED` with `E_GR1 = 8d08f8c913f4bb9ef413114ecceb2f72d72d8213`
and `L_GR1 = 13ffc7372d52c16bdb0e24935aa617deb67e7c51` recoverable and `L_GR1`'s second parent
equal to `E_GR1`; all six pinned paths carrying their pinned blobs at `E_GR1` and at `L_GR1`; the
seals tree `92e0956ad6b187fddf77068f33c66e69a012f074`; the declarations at `B` act 28's. The
control plane's own preconditions were evaluated over the same facts in mode `M` before its merge
and in mode `B` against the landed commit, 42 rows each time, no failure.

***

## The two supersessions, as executed

### `S1` — the declaration contract

The **frozen superseded segment** is the three lines hashing to
`9c1493dbab4b81f46a685ea71fcef8e52af50c3509cda4139c8e76630e6ee6a7`. It was extracted from the
base's own guard text, hashed and found exactly once before anything was changed.

Installed in its place: `_GR1_DECL_NAMES` and `_GR1_DECL_FROZEN`; `_gr1_decls`, which reads the
two values out of the guard file at a revision by walking module-level assignments of that
historical source; `_gr1_decl_verdicts`, carrying both regimes; and the call site. Both check keys
are unchanged, so the failure vocabulary in the log is the one a reader already knows. While
`GR-1` is `EXECUTION` the values are read from the live module exactly as before; in every other
state they are required to equal the frozen table in the guard file at `GR-1`'s recovered `E`
**and** `L`. Fail-closed on an unrecoverable revision, a source that does not parse, a name
assigned twice, a value that is not a literal, and a missing name.

### `S2` — the pinned-artifact family

The **frozen superseded segment** is the five-line loop hashing to
`26c4c7c6a8727e23a2547305205d045ff88090b2bff7d122f80dd46f2cc1369e`, likewise extracted from the
base's own guard text, hashed, and present once.

Installed in its place: `_GR1_PIN_LIVE`, the three paths `GR-1`'s placement contract names as
checked on the current tree after landing — act 28's preregistration, act 28's result note and
`verification/seals/PFR.json` — and `_gr1_pin_ok`, the per-path verdict. Every pinned path is
required to carry its pinned blob at `GR-1`'s recovered `E` and `L`; the three above are required
to carry it at the resolved head as well, read at the same revision the superseded loop read. The
six `landed-pin:<full path>` key identities and every pinned value are unchanged, and the guard
and the ROADMAP remain excluded under their own contracts.

### Placement, stated exactly

Module-level definitions must precede the lifecycle split, and the only frozen segment before that
split is `S1`'s. `S2`'s two objects are therefore introduced **in that pre-split replacement
span**, while `S2`'s own span carries the loop's changed verdict. The freeze constrains what the
two replacements are and that nothing else in the region is touched; it leaves placement open.

Two terms are kept apart throughout this note:

- the **frozen superseded segment** — for `S1`, the three lines hashing to `9c1493db…`; for `S2`,
  the five lines hashing to `26c4c7c6…`;
- the **replacement / restoration span** — the larger contiguous region that must be written back
  for the base to be reproduced byte for byte. For `S1` that span is 123 lines, running through
  the blank separation the inserted block needs; stopping at the last statement left two blank
  lines behind on restoration.

Stage 2's incremental change is exactly `S2` — its two objects and its changed loop verdict — and
nothing else. The two replacements are **not** independently reversible in the textual sense:
restoring the `S1` span also removes the `S2` definitions that live inside it. What is
established, and what the budget contract requires, is that **the two frozen supersessions are
independently identifiable and hashed, and that restoring both superseded base segments and
removing the `R7-GR2` block reconstructs the base guard byte for byte.**

***

## `GR2-1` — suite A: SUITE-A-AS-FROZEN

Nine rows, the old side being the base's extracted code compiled and executed in a controlled
namespace rather than a paraphrase. Every row returned its frozen pair of verdicts.

| row | configuration | old | new |
|---|---|---|---|
| A1 | `EXECUTION`, live `GR-1` | accept | accept |
| A2 | `EXECUTION`, live successor | reject | reject |
| A3 | landed, live `GR-1`, history `GR-1` | accept | accept |
| A4 | landed, live act 29 both lines, history `GR-1` | **reject** | **accept** |
| A5 | landed, successor baseline only | reject | accept |
| A6 | landed, successor prospective only | reject | accept |
| A7 | landed, baseline mutated at `E` | accept | **reject** |
| A8 | landed, prospective mutated at `L` | accept | **reject** |
| A9 | landed, `E` unrecoverable | accept | reject (fail-closed) |

`A4` is the state act 29's candidate merge is in. `A7` and `A8` mutate one declaration each, so
each row requires the mutated key to fail and the other to stand.

## `GR2-2` — suite B and the composition row: SUITE-B-AS-FROZEN

The eight frozen rows are measured as nine, `B8` being exercised for an unrecoverable `E` and for
an unrecoverable `L` separately. Every row returned its frozen pair.

| row | configuration | old | new |
|---|---|---|---|
| B1 | all six pinned, both classes | accept | accept |
| B2 | protected three changed live | reject | **reject** |
| B3 | `AGENTS.md` changed live | **reject** | **accept** |
| B4 | `OIBridge/ProductLocusFreedom.lean` changed live | **reject** | **accept** |
| B5 | act 29's preregistration changed live | **reject** | **accept** |
| B6 | protected three mutated at `E` | accept | **reject** |
| B7 | historical-only three mutated at `L` | accept | **reject** |
| B8 | `E` unrecoverable / `L` unrecoverable | accept | reject (fail-closed) |

**`C1`, the composition row**: one repository in which both declarations carry act 29's values
**and** one historical-only path is changed, with `E` and `L` intact — both contracts pass in that
same run, and the superseded pair fails on both counts in that same repository. The two repairs
compose; they are not merely passing apart.

## The fixtures

`G5` (fail-closed reader: assigned twice, non-literal, unparsable, absent), `G6` (the verdict
follows the history, not the process, where the two disagree), `G7` (non-vacuity: the frozen table
is not the successor values the rows use), `P5` (a pinned path absent at `E` fails closed) and
`P6` (the classification: `_GR1_PIN_LIVE` exactly the three protected paths, each a pinned key;
the six emitted key identities exactly those the base's own loop emits; the base's pinned table,
parsed from the base's source, equal to the live one; the guard and the ROADMAP excluded) are
measured in their own right.

The frozen list's other eight names — `G1`–`G4`, `P1`–`P4` — name cases suite A and suite B
already measure. They are recorded under the freeze's own names as **aliases resolving to those
specific measured rows** (`G1` → `A1`, `A2`; `G2` → `A4`; `G3` → `A5`, `A6`; `G4` → `A7`, `A8`;
`P1` → `B1`; `P2` → `B2`; `P3` → `B3`, `B4`, `B5`; `P4` → `B6`, `B7`), not to an aggregate
verdict, and not as second measurements of the same repositories.

***

## The negative suite: thirteen families, each failing for its named reason

Each row builds the mutant the freeze names, runs it on a case the real implementation gets right,
and requires the two to **disagree**, so no row can pass by controlling nothing.

| | mutation | the named reason it must fail |
|---|---|---|
| N1 | drop the `EXECUTION` regime | reads history while the round is still executing |
| N2 | read `L` and not `E` | a baseline mutated at `E` is accepted |
| N3 | accept `None` from either reader | an unrecoverable revision is accepted |
| N4 | take the first of duplicate assignments | the second assignment is never seen |
| N5 | compare declaration source text | a reformatting that changed no value is rejected |
| N6 | `_GR1_PIN_LIVE` omits a protected path | a changed protected artifact is accepted |
| N7 | `_GR1_PIN_LIVE` admits a fourth path | a legitimate successor's edit is rejected |
| N8 | drop the historical leg for protected pins | a protected artifact mutated at `E` is accepted |
| N9 | drop the live leg for protected pins | that artifact changed on the current tree is accepted |
| N10 | change a pinned value | a pristine tree is rejected against the moved pin |
| N11 | key `landed-pin` by basename | six verdicts collapse to five and one is overwritten |
| N12 | a budget tolerating an unrelated edit in the region | the whole-file equality stops being a budget |
| N13 | a `_GR2_BASE`, `_GR2_SEALED_HEAD` or `_GR2_MERGE` name | `SI-3`'s standing contract is violated |

`N11`'s mutant is the basename keying `GR-1`'s Amendment 2 repaired; that defect is now a standing
control in this block.

***

## `GR2-3` — the budget: BUDGET-HELD

This file, with the `R7-GR2` block removed and both superseded segments restored to the base's
text, equals the base's guard file byte for byte — measured at every stage before its commit, and
measured by the block itself on every build, whole-file while the round executes and against the
recovered `E` after landing.

The round's whole diff to the guard file is the two replacement spans and the `R7-GR2` block. No
other file is touched: no Lean file, no manuscript, no ROADMAP row, no census entry, no seal
record, and none of the six pinned paths, `AGENTS.md` included.

## `GR2-4` — the verdict map: MAP-PRESERVED

`gr2-tagmap.json` carries two columns. The **base column** is the base's own guard file run at `B`
in a detached temporary worktree with the git and pull-request environment variables removed; the
**head column** is the same tags' verdicts from the stage-3 dry run, the run at which this block is
present and these artifacts are not, so the column does not depend on the file it is written into.

- base column: **102 tags, every one `PASS`**
- head column: the same 102 tags, **every verdict identical**
- tags new at the head: **exactly one, `R7-GR2`**; tags absent at the head: none

### A recorded discrepancy: the predicted cardinality

The freeze predicted, at moderate strength, that the base would emit 93 tags and the head 94, with
the rule and not the number governing. The measured counts are **102 and 103**. The difference is
a counting rule, and it is recorded rather than repaired: at `B` there are **93 `check('` call
sites**, which is the number the prediction carried forward from `GR-1`'s freeze, and **102 printed
verdict lines**, which is what this map collects. The nine additional entries are `R1`–`R9`,
emitted through a different call form, together with `R7-GR1`, which `GR-1`'s own map excluded
because that map covered the tags pre-existing at its base. No tag changed verdict under either
counting rule, and the frozen comparison — every base tag identical at the head, exactly one new
tag — holds on the measured data.

***

## `R7-GR1` at this head

86 checks, 24 control groups, chronology `LANDED-UNRECORDED`, **failures: none**. The repaired
declaration and pin contracts pass on the real repository, against `GR-1`'s recovered history.

## `R7-GR2` at this head

63 checks, 7 control groups, chronology `EXECUTION`, failures: none. At the stage-3 checkpoint the
same block was the round's sole failure with its failure set exactly `result-note` and `tag-map`,
the two artifacts this stage writes.

***

## Implementation and debugging findings

These are execution discoveries in the block's own scaffolding. None changed `S1`, `S2`, either
suite's frozen verdicts, or any frozen outcome; each was found and fixed before the commit it
belongs to.

1. The base's `_GR1_PINS` table has two **name** keys, the guard path and the ROADMAP path, so
   `literal_eval` refuses it; the parse walks the dict node by node with those two resolved.
2. The superseded pin loop reads `_GR1_PINS` from its own namespace. A synthetic row must hand it
   that row's own pinned values, or the old side compares synthetic blobs against the real pins
   and rejects everything. Found when all of suite B failed at once.
3. Rows `A7` and `A8` mutate one declaration each, so a uniform "every key fails" assertion is
   wrong: a baseline-only mutation leaves `prospective-untouched` true.
4. A row about a mutated history must not let that mutation leak into the current tree, or the old
   side rejects for the wrong reason and the row measures nothing.

A fifth finding concerns the stage-3 commit itself: the negative suite as first committed covered
four of the thirteen frozen families, with a fifth family present only as fixture `G5`. It was
found in owner review of the stage-3 report and the suite was made exhaustive before this stage
began, in a second commit on stage 3.

***

## What this round does not license

It does not reopen `GR-1`'s substantive `_pfr_road_ok` contract. It states nothing about act 29's
targets, its outcome vector or its landing, and neither reads nor reports them. It does not treat
`GR1.json` as written. It does not license editing act 28's preregistration, its result note or
`PFR.json`, which stay pinned live and whose protection this round's own fixtures require. It does
not license a later round changing a landed round's contract without its own freeze.

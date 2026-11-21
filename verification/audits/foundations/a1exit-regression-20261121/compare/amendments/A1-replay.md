# Amendment A1 to the comparison preregistration: replay rule and round-1 review answers

**Status.** An amendment to `../PREREG.md`, which keeps its text as pushed at `cecbf672`. It answers
the independent review of `cecbf672` (REVISE), recorded on #1483. It was written before any after-state
exists. Nothing here was run against a Step-2 head or a deletion head, and the replay of the real
S2-A–S2-E edits has not been run at all (§9). Where this amendment and PREREG differ, this amendment
governs.

**Authorization.** Unchanged: owner `amaybaum`, #1169 comment 7058783437. That record approves
preparation; running the comparison waits on the executed and independently reviewed A1 deletion.

**Goal link (§A.47).** Unchanged. It is owner requirement 6, through #1468.

## 1. The replay rule (replaces PREREG §3 J1–J6 and J8)

**Replayed state R.** Start from the pinned corpus (`1c7eedc4`) and apply every compiled edit in order:
- the frozen S2-A–S2-E list `edits/S2.json`, then the deletion list compiled at H;
- units in landing order: S2-A #1470, S2-B #1473, S2-C #1474, S2-D #1472, S2-E #1475, then DEL;
- within a unit, in the order of its records: the base list, then each amendment, or the order a record
  states ("The splices are applied in the order …").

An amending edit's old string is text produced by its base edit, so sequential application composes it
onto its base.

**Application rules.**

| Kind | Applied when | Notes |
|---|---|---|
| `replace` | its old string occurs exactly once in each target | The old string is matched with every whitespace run treated as `\s+`. The new string is inserted verbatim |
| `replace-each` | the old string occurs at least once and at most as many times as the record lists sites in that file | For a multi-site record, such as S2-C A1-1. Every occurrence is replaced |
| `resolve` | a line in the target file has a normalized similarity of at least 0.5 to the resolved text | Records the line as resolved at a landing catch-up ("Resolved line `F:n`, in full:"). The most similar line becomes the resolved text. Applied after that unit's other edits |

An edit that cannot apply is logged as unapplied and left out of R.

**FULL scope.** A target in `book/The-Incompleteness-of-Observation-FULL.md` carries the book file whose
FULL span contains it. The span runs from that file's first heading line in FULL to the next file's. An
edit applies to FULL only inside that span, so a chapter's edit can cover only that chapter's FULL
mirror.

**Classification against H.** The executed head H is compared with R line by line, per file, after
whitespace normalization (`difflib`). Every reported item of `compare.json` (the baseline against H)
is classified:
- **Changed or relocated entries and unaccounted lines.** J-candidate only if the item's line in H lies
  in an equal block against R, so the replay reproduces the after text exactly. A relocated entry must
  also be relocated to the same file in the replay.
- **Removed entries.** J-candidate only if the replay also removes the entry.
- **Deleted lines.** J-candidate only if the replay also deletes the same text from the same file.
- **Anything else is U.**

**Replay-missing items.** These are also U:
- a line of H that differs from R but is the baseline's line, so the replay changed it and H did not;
- a replayed line with no counterpart in H.

**Every difference from the replay is U.** No hand citation can make an item J, and `classify.json` can
no longer supply J. It can only mark a J-candidate R, and resolve R items.

## 2. J9, tightened

A J-candidate with a label change is checked against every ledger row in the entry's own `ledger_rows`,
in the baseline snapshot, that exists in the frozen ledger state (§5). Each row's disposition sets the
test:

| Disposition | The after text must |
|---|---|
| F | keep at least as many occurrences of "finite" as the baseline line had, and lose none of the baseline line's open, conditional, hypothesis, assumed, posit, not-established, not-derived, conjecture or unverified terms (no promotion) |
| O | carry such a term |
| J | lose none of the baseline line's such terms |

Any failure makes the item R. A J-candidate relocated out of Main is R (PREREG J7, unchanged).

## 3. R resolutions

A resolution counts only if it is recorded as all of:
- `{"outcome": "justified"|"unjustified", ...}`;
- `"review"`: the URL of a recorded review on this repository, matching
  `https://github.com/amaybaum/incompleteness/(pull|issues)/<n>#(issuecomment-<id>|pullrequestreview-<id>|discussion_r<id>)`;
- `"reviewer"` and `"author"` logins, which must differ.

Anything else is ignored, and the item stays R. An "unjustified" outcome counts as U.

## 4. Compiled edit lists, frozen

`edits/S2.json` (schema `a1exit-compare-edits/2`) holds 168 edits, compiled at
`7f28886f4cc96fbfa7407af1fdc37de2f0e562e5`.

| Unit | Edits | Source records (the per-unit allowlist) | Parsing |
|---|---|---|---|
| S2-A | 22 (17 base, 5 amending, linked by `amends`) | `checks/s2a_edits.json` | JSON objects |
| S2-B | 42 | `PREREG.md` (28), `amendments/A1-round1.md` (9), `A2-return-form.md` (2), `A3-cptp-register.md` (3) | headings with Old/New fenced pairs; Old/New table |
| S2-C | 33 | `PREREG.md` §5 (27), `amendments/A1.md` (3; order A1-3, A1-1, A1-2), `RESULT.md` §9.1 (3 resolved lines) | Old/New table; old/new bullets; resolved lines |
| S2-D | 21 | `PREREG.md` (18, of which E15, E16 and E18 are "identical to" mirrors), `amendments/A1.md` (3) | headings with Old/New fenced pairs |
| S2-E | 50 (45 base, 5 amending, linked by `amends`) | `checks/s2e_edits.json`, `checks/s2e_amend1.json` | JSON objects |
| DEL | compiled at H | `verification/audits/foundations/a1exit-deletion-20261121/edits.json` | JSON objects |

All record paths are under `verification/audits/manuscript/a1exit-s2<x>-20261121/` except DEL's.

**`check-edits`.** It recompiles the named units, from only their allowlisted paths, at a pinned
commit, and requires byte-identical agreement with the given list:
- for S2, the commit is `7f28886f`;
- for DEL, the commit is H.

It fails on a missing source, on an empty list, and on an edit record without an old string or a
target. It is recorded in `controls.json` as two controls:
- C6-check-edits-S2;
- C6-check-edits-DEL.

At drafting, `check-edits` on `edits/S2.json` reports `PASS (168 edits; identical to recompilation at
7f28886f)`.

**`verdict.json`.** It records the SHA-256 of `compare.json`, `injected-compare.json`, `controls.json`,
`edits-del.json`, `edits/S2.json`, `classify.json` and the ledger `rows.json` it read.

## 5. Ledger state used by J9

J9 reads `verification/audits/foundations/a1exit-ledger-20261120/rows.json` at
`7f28886f4cc96fbfa7407af1fdc37de2f0e562e5`, from the Git objects. Its SHA-256 is
`39e51d0cfd8d6855f17ef3d7253a43d372fae608a9dcae083fbeb52471b512a0`, recorded in `FROZEN.json` and checked
by C0. This is the ledger as accepted before the post-Step-2 reconciliation. A reconciled ledger is
used only if a further amendment, made before the comparison is run, names its commit and digest.

## 6. Controls (additions to PREREG §5)

- **C0** now covers `edits/S2.json` and the ledger digest as well as the three tools.
- **C6, check-edits** for S2 and for DEL (§4). At a head without a deletion record, C6-DEL fails, and
  the run is VOID.
- **C7, bad-citation countercontrol** (run by `verdict`). The first J item with an after-state line has
  that line perturbed in a copy of H (" [perturbed]" appended) and is reclassified against the same R.
  It must become U, and the U count must rise by exactly one. If there is no J item, C7 is recorded as
  not applicable.
- **Fresh output.** `collect` refuses unless `--out` does not exist or is empty, and records
  `out_was_fresh`. `verdict` requires `out_was_fresh` and requires `compare.json` to name H and the
  pin; otherwise the controls fail and the verdict is VOID.
- **C4, the self-test.** It covers T1–T3, the review's G1, G2, G3, G4b, G5b, G6 and G7 (each must give U),
  and also:
  - a reproduced promotion on an F row, which gives R;
  - an O-row label change with an open term, reproduced, which gives J;
  - a FULL edit outside its chapter span (unapplied, U) and inside it (J);
  - a reviewed edit missing from H (replay-missing, U);
  - R resolutions (a valid review gives R-justified; no URL, or a self-review, leaves it R);
  - a relocation out of Main (R);
  - the C7 mechanism;
  - VOID;
  - the three Markdown parsers on fixed samples.

## 7. Scientific-evaluation flag, widened

An item is flagged when any of these holds:
- it carries `value changed`;
- its before or after text contains a decimal, a power of ten (`10^n`, `\times 10`, `× 10`), a number
  with a recognized unit, or a comparison marker (the baseline's `PROSE_MARK_W`);
- it lies in C-TAB (prediction or status tables), C-PROSE, C-FINL, C-CDO, C-CAL, C-OBS or C-OPEN, as
  before.

Replay-missing items are flagged by the same text test. The review counted 51 entries that the old
flag would miss but did not list them. SM:735–740, the A·B(N) table rows with decimals, are flagged by
the widened test. The other 50 are not checked one by one here.

## 8. Changed commands and schemas

| Mode | Command |
|---|---|
| collect | `verdict.py collect --head <H> --out <DIR>` (unchanged) |
| verdict | `verdict.py verdict --dir <DIR> [--classify <file>]`. The edit lists are the frozen `edits/S2.json` and `<DIR>/edits-del.json` |
| compile | `verdict.py compile --units <U,...> --commit <rev> --out <file>` |
| check-edits | `verdict.py check-edits --edits <file> --units <U,...> --commit <rev>` |

The schemas are now `a1exit-compare-edits/2`, `-classify/2`, `-controls/2`, `-verdict/2` and
`-frozen/2`, stated in the usage text of `verdict.py`. The PREREG §2 step "compile the justification
sources" is replaced by §4 above.

## 9. What was run, and what was not

**Run.**
- `verdict.py self-test`: every case PASS.
- `check-edits` on `edits/S2.json` at `7f28886f`: PASS.
- `collect --head 1c7eedc4` into a fresh directory, which compares the baseline with itself:
  - C0–C5 and C6-S2 pass;
  - C6-DEL fails as designed, because the pin has no deletion record, so `collect` exits 4;
  - a second `collect` into the same directory is refused.

**Not run.**
- `verdict` on real inputs.
- Any replay of the compiled S2-A–S2-E edits, against `7f28886f` or anything else. That replay needs an
  owner decision first.
- Any comparison against a Step-2 head or a deletion head.

**Known risk for the later replay.** Some compiled S2 edits may not apply in sequence where a later
unit's string was written against `1c7eedc4` and an earlier unit changed the same span. The three S2-C
resolved lines cover the conflicts that the records name. Any other gap shows up as U at execution,
which is the intended strictness. It would be seen early if the owner authorizes a replay against
`7f28886f`.

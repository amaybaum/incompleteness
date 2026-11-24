# Commit-independent A1-EXIT ledger coverage tool: design

Status: paper-only design. No code, branch, commit or GitHub write is made under it. Implementation
needs a separate recorded owner authorization (AGENTS.md sec. A.45 rule 3).

Goal link (sec. A.47): supporting verification tooling for the A1-EXIT ledger record. It decides
whether a given tree's manuscript sites are still accounted for by the frozen ledger and the
authorized edits applied since; it decides no scientific question and no row's disposition.

Accountable Issue: #1169 (the defects of the existing tool are recorded there).

Notation. `E` = e837e3dbaa605efc867a213f3345cee14c36d8f5 (the ledger pin). `H` =
53c6601a10419b6b333cc992474272501ab542af (ledger base of the retirement plan). `T1'` =
14ac71b4b0a0c0aa2d7068d6799a73f474097060 (H plus the 399 ledgered splices). `P` =
4c79be642ca631573f06b444903be75ec4f5e2b6 (plan commit holding `ledger.json` and `edits.json`).
`R` = the frozen record directory `verification/audits/foundations/a1exit-ledger-20261120/`, tree
b05efdca935a42b9c94ef1748c964696bf58fcd9 (identical at 9882df8f2d41eee47790560b0e22aac03e95370f,
at H and at the current `main`).

***

## 1. Purpose and non-goals

Purpose. Two separate operations:

- **A, verify-record.** Show that the frozen ledger record `R` is correct relative to its own pin
  `E`, by replaying the frozen tool on a materialization of `E`, and derive from it a
  content-anchored site map held only in memory and in the caller's output directory.
- **B, check-coverage.** Show, for any candidate commit `C`, that every site of the frozen map is
  accounted for in `C` (unchanged and possibly moved, or rewritten by an identified authorized
  splice), and that every line of `C` matching the ledger's pattern sets is held by a site or by a
  content-anchored classification. B never regenerates, rewrites or re-renders `R`.

Non-goals.

- It does not establish scientific correctness. Content matching shows only that bytes are where,
  and what, an authorized record says. Whether a moved sentence keeps its meaning in new context,
  or whether an authorized replacement keeps the finite-only, conditional or open qualification
  the ledger requires, is decided by the reviews the ledger and the retirement plan already
  require: the plan's preservation checks and mirror-parity checks, the independent non-author
  review of the exact head (PREREG of `R`, sec. 6 item 5), and the owner's decision. B's pass is
  necessary for coverage, never sufficient for correctness.
- It is not a preservation checker for non-manuscript files. Lean, Python, JSON, the coverage
  ledger and TeX/PDF stay with the retirement plan's own `preserve_check.py`. B covers
  `papers/*.md` and `book/*.md` (the frozen tool's `corpus_files()` set) only.
- It does not reclassify rows. Row, correction code and owner are carried from the frozen
  `sitemap.json`; the frozen `assign()` and `s3()` are not re-run on later trees.
- It does not modify the frozen tool or any file in `R`, and is not a replacement record.
- It is not an A1-retirement gate (sec. 12).

## 2. What the existing tool does (grounding)

`ledger_check.py` in `R`:

- `build()` relocates the Phase-0 sites (`relocate()`: exact quote, then nearest-of-several
  duplicates `exact-dup`, then Phase-1/2 `splice_map()` text substitution, then 60-character
  head/tail anchors, then `difflib` fuzzy match >= 0.5 within +-150 lines), adds every pattern hit
  from `scan()` as `new`, adds Phase-2 census sites keyed `file:line`, and adds every
  `rows.json` `site_overrides` key as an `extra` site at that line number. `assign()` applies
  overrides by `file:line` key, checking only that the override's `anchor` is a substring of the
  line now at that number; `new_site_rules` accept a hit only if its `file:line` is in the rule's
  `read` list. The frozen map at `E` has 697 sites: 435 `exact`, 83 `anchor`, 32 `splice`, 16
  `fuzzy`, 109 `extra`, 11 `new`, 11 `p2-census`.
- `check()` (CK1-CK8, CKa) evaluates the map; `main('check')` first compares
  `manuscript_digest()` and refuses any other tree (PIN MISMATCH), then requires `build()` to equal
  the tracked `sitemap.json` and `render()` to equal the tracked `LEDGER.md` blocks, then prints
  only the first 20 lines of `extended_unmapped()`. `main('build')` and `main('render')` write the
  tracked `sitemap.json` and `LEDGER.md` in place. Results exist only as printed text.
- `self_test()` has four countercontrols; countercontrol 4 calls `build()` on the working tree, so
  the self-test is meaningful only at the pin. There is no line-shift control.

Additional defect observed in this design work: on a materialization of `H` with the frozen
`sitemap.json`, `main('check')` raises `TypeError` while printing the PIN MISMATCH diagnostics
(line 523, sorting `(file, line, row)` tuples in which `row` is `None`), so the mismatch report
is not even produced.

Measured (method in sec. 9.4): at `E` the frozen check passes (0 errors, extended scan 0, frozen
self-test true). After `build()` on a materialization of `H`: 32 errors (14 CKa, 11 CK3, 7 CK4),
extended scan 8, and the `LEDGER.md` render differs; on `T1'`: 154 (55 CKa, 52 CK3, 43 CK4, 3 CK7,
1 CK5), extended scan 30. Of the 135 overrides, the anchor is at its key line for 121 at `H` (10
stale by +4, 4 anchors absent) and for 80 at `T1'` (39 at +2, 10 at +6, 1 at +4, 1 duplicated at
-98/+2, the same 4 absent). These reproduce the figures recorded on #1169.

## 3. Architecture

### 3.1 Inputs (all read from the git object store; the working tree is never read)

| Input | Form | Integrity check |
|---|---|---|
| repository | `--repo DIR` (default: the repository containing the tool's invocation directory) | `git rev-parse --git-dir` succeeds |
| pin | `--pin REV`, must resolve to `E` | equality with the pin recorded in `R/sitemap.json` and `R/rows.json` |
| record | `--record REV` (a commit holding `R`) | tree id of `R` at REV equals the constant b05efdca...; `R/sitemap.json` `manuscript_digest` equals the digest of the pin's corpus |
| Phase records | `a1-scope-phase0-20261120/`, `a1-scope-phase2-20261120/` at the record commit | blob ids recorded in the output |
| candidate | `--commit REV` | resolved once to a full commit id; every read is `(commit, path)` |
| segments | `--segment FROM..TO` or `--segment FROM..TO=LREV:LPATH` (repeatable, ordered) | chain is contiguous from pin to candidate; see 3.3 |
| adjudications | `--adjudication REV:PATH` (optional, repeatable) | schema-valid; every fingerprint must match exactly (sec. 4.6) |
| prior | `--prior REV` (optional) | REV must be a segment endpoint |
| output | `--out DIR` | must not exist or be empty; must not lie inside any worktree of the repository (checked with `git rev-parse --show-toplevel` from DIR and by path prefix against every `git worktree list` entry) |

The tool writes only under `--out`: `result.json`, the derived `anchors.json`, and for op A the
materialized pin tree under `--out/replay/`. It never writes a tracked file, never runs `git`
commands that change refs, the index, the object store or worktrees, and never calls the frozen
tool's `main()`.

### 3.2 Operation A (verify-record)

1. Resolve `--pin`, `--record`; check the record tree id and pins.
2. Materialize under `--out/replay/`: every `papers/*.md` and `book/*.md` blob at the pin, and the
   files of `R` and the two Phase directories at the record commit, by `git cat-file --batch`.
   (`git archive` is unusable here: `.gitattributes` marks `verification/audits` export-ignore.)
3. Import the frozen `ledger_check.py` from the materialization (`python3 -I -B`, `sys.path` set to
   that copy only). Call, and record as structured values: `manuscript_digest()` versus the
   frozen `sitemap.json`; `build()` versus the frozen `sitemap.json` (deep equality); `render()`
   spliced into the frozen `LEDGER.md` with `splice_block()` versus the frozen bytes;
   `check(sm, rows, quiet=True)` (the returned list); `extended_unmapped(sm)` (the full list);
   `self_test()` (its boolean return). No printed text is read.
4. Derive the anchor map (sec. 4.2) from the frozen `sitemap.json`, `rows.json` and the pin blobs,
   and write it to `--out/anchors.json`, with its SHA-256 in the result.
5. Verdict `HOLDS` iff every item of step 3 is equal / empty / true and step 4 raises no pin-time
   finding.

A accepts only the pin. It never evaluates the frozen record against a later tree: that
comparison is meaningless by construction, which is the third defect on #1169.

### 3.3 Operation B (check-coverage)

Data flow: `anchors.json` (rebuilt in memory exactly as in A step 4, from the record and pin
objects; A's replay is not re-run) -> segment chain -> per-site state -> hit scan -> findings ->
verdict.

A segment is `FROM..TO`, either **ledgered** (`=LREV:LPATH` names an exact-edit ledger of the
`ledger.json` form, schema `a1exit deletion exact-edit ledger v2`) or **unledgered**. The chain
must start at the pin and end at `--commit`; consecutive endpoints must be equal. For a ledgered
segment: the ledger's `base` must equal FROM; if `edits_sha256` is present, the `edits.json`
beside the ledger at LREV must hash to it (true at `P`: 528f146d...); every splice's
`old_sha256` must equal the SHA-256 of FROM's bytes `[start, end)` and `new_sha256` that of
`new` (UTF-8); splices in one file must not overlap; each ledgered corpus file's `base_sha256`
must equal FROM's blob. Any failure here is an input-integrity error (exit 3), not a finding.

Site state carried between segments: `resolved` (current file, byte span, bytes) or `unresolved`
(with the segment where it became so). An unresolved site stays unresolved in later segments and
its finding is carried forward, tagged with its origin segment.

## 4. Anchor algorithm

### 4.1 Normalization

Matching uses **identity normalization**: the anchor is the exact UTF-8 bytes of the site's line
at the pin, without its terminating LF. A file that is not valid UTF-8 or contains CR is an input
error. A **diagnostic normalization** (Unicode NFC, every whitespace run replaced by one space,
leading and trailing space removed) is computed only to label a failing site `whitespace_only`;
it never makes a site pass. Markdown whitespace can change rendering (line breaks, code blocks),
so a whitespace change is not presumed meaning-free.

### 4.2 Anchor definition (derived at the pin; never stored in the repository)

For every site of the frozen map:

- `site_id`: `"<file>:<line>@e837e3db"` (the pin key; stable because it names the pin) and
  `anchor_sha256` = SHA-256 of the pin line bytes;
- `pin_count`: number of lines in the file at the pin with identical bytes;
- `ordinal`: 1-based index of this line among them, ordered by byte offset;
- `context_sha256`: SHA-256 of (nearest non-blank line before) + 0x00 + (nearest non-blank line
  after), pin bytes;
- carried classification: `row`, `code`, `owner`, `p0_id`, `mirror_of`, `relocation` from the
  frozen record;
- for an override: its `anchor` string, checked once at the pin to be a substring of the pin
  line. The override is bound to the site id, so it is never searched for later.

Every `new_site_rules[*].read` entry is converted at the pin into `(file, line_sha256)`. Every
Phase-2 census key is already a frozen-map site and needs no conversion.

Measured at `E`: all 697 site lines are unique in their file (`pin_count` = 1 for 697 of 697); all
135 override anchors are substrings of their pin lines; 2 override anchor strings occur twice in
their file (FULL:4927 and ch18:196, each with a copy 100 lines earlier). The frozen tool resolved
those through the key line; under this design they need no search at all, because the override
is bound to its site.

### 4.3 Relocation within a ledgered segment (exact, no search)

For each resolved site in a file the ledger touches:

1. **File conformance first.** Rebuild the expected TO file from FROM and the file's splices
   (ascending `start`, as the plan's `preserve_check.expected()` does). If TO's blob differs,
   emit `unauthorized-edit` for every differing byte range outside all splice images
   (computed by a deterministic `difflib.SequenceMatcher(autojunk=False)` comparison of
   expected and actual, reported as TO line ranges), and process that file's sites by the
   unledgered rules of 4.4 instead.
2. **No overlap.** If the site's span `[a, b]` (line bytes plus its LF) meets no splice span,
   translate it by the cumulative length change of the preceding splices. Cross-check: the bytes
   at the translated span equal the anchor bytes, and a content search (4.4) finds exactly that
   line; any disagreement is `ambiguous` (fail). Status `unchanged` if the line number is the
   same, else `moved` (with `line_delta`).
3. **Overlap.** Let the region be the union of the site line and every overlapping splice span,
   extended to whole lines. The expected new region is FROM's region with those splices applied;
   its image in TO is located by offset translation and must equal it byte for byte. Status
   `authorized-replacement` with `splice_ids`, each `old_sha256`/`new_sha256`, the new line
   range and `new_region_sha256`, and the review aid `anchor_survives` (whether the pin line is
   still a substring of the new region). If the new region is empty, status `authorized-removal`.
   The site's current bytes become the new region for later segments.

Files not in the ledger must be byte-identical between FROM and TO; a difference is
`unledgered-file-change` and that file's sites take the rules of 4.4.

### 4.4 Relocation within an unledgered segment (search)

Per file: if the blob is unchanged, every site is carried unchanged. Otherwise for each resolved
site with current bytes `t` (one line, or a multi-line region after an earlier replacement):

- count occurrences `n` of `t` as whole lines in TO;
- `n == 1` and the pin/previous count was 1: `unchanged` or `moved`;
- `n == 0`: unresolved. Diagnostic only: the deterministic line diff of FROM against TO maps the
  site's line to a replacement hunk (`unauthorized-change`, with `whitespace_only`) or to a
  deletion with no replacement (`missing`);
- `n` differs from the previous count (e.g. 1 -> 2): `duplicated`, unresolved, regardless of
  context;
- `n` equals a previous count > 1: keep only occurrences whose `context_sha256` matches; resolved
  iff exactly one remains **and** its ordinal equals the recorded ordinal; otherwise `ambiguous`.

Nothing is ever chosen by proximity to an old line number, and no fuzzy score resolves a site.

### 4.5 Context changes

For a resolved site whose `context_sha256` differs from the pin, `context_changed: true` is
reported for review. It is not a failure (identity is not in doubt), but it is the marker that
the meaning of an unchanged sentence may have changed around it (sec. 1, non-goals). Owner
question Q3 asks whether it should fail instead.

### 4.6 Adjudications (reviewed records, read-only input)

An unresolved site, or an unmapped hit, is resolved only by an adjudication entry whose
fingerprint matches exactly: for a site, `{site_id, segment, from_sha256, to_region_sha256,
row, code, owner, reason, reviewer, owner_record}`, where `to_region_sha256` occurs exactly once
in TO; for a hit, `{file, line_sha256, patterns, row, code, reason, reviewer, owner_record}`. A
non-matching entry resolves nothing and is itself reported (`stale-adjudication`, a finding).
Status `adjudicated` is distinct from `moved` and `authorized-replacement` in every count. The
tool never writes adjudications; each is a separately reviewed record under sec. A.36 placement.

### 4.7 Pattern hits (coverage completeness)

On TO, scan every corpus line with the Phase-0 `core_patterns` and `paraphrase_patterns` and the
frozen `EXTENDED_PATTERNS` (read from `R`'s tool source at the record commit, not retyped). A hit
line is `held` if it lies in a resolved site's current region, or its `line_sha256` is in the
converted `read` set and the matching `new_site_rules` regex still matches, or an adjudication
covers it; otherwise `unmapped-hit`, attributed as `in-authorized-text` (inside a splice image),
`in-unledgered-change`, or `pre-existing` (with `--prior`: identical text unheld at the prior
endpoint, or inside a splice whose FROM region was an unheld hit line). Every hit is listed;
nothing is truncated.

## 5. CLI contract

```
ledger_coverage.py verify-record  --pin REV --record REV --out DIR [--repo DIR]
ledger_coverage.py check-coverage --pin REV --record REV --commit REV
                                  [--segment FROM..TO[=LREV:LPATH]]... [--prior REV]
                                  [--adjudication REV:PATH]... --out DIR [--repo DIR]
ledger_coverage.py self-test      --out DIR [--repo DIR] [--real-trees]
```

With no `--segment`, `check-coverage` uses one unledgered segment `pin..commit`.
`self-test` without `--real-trees` uses only synthetic in-memory trees (local smoke, sec. A.40);
with it, also the real-tree controls of 7.3 (CI).

| Exit | Meaning | `verdict` |
|---|---|---|
| 0 | all checks hold, controls green | `HOLDS` |
| 1 | at least one finding | `FAILS` |
| 2 | usage error, or `--out` refused | `ERROR` |
| 3 | input integrity error (object missing, record tree or pin mismatch, ledger hash/span/base mismatch, encoding) | `ERROR` |
| 4 | a preflight or self-test control failed; any verdict is void | `VOID` |

Every run of `verify-record` and `check-coverage` first runs the cheap preflight controls U1-U4
(sec. 7.1) in memory; if one fails, the run exits 4 without evaluating. The exit status and
`result.json` always agree; consumers read `result.json` (sec. A.44), never stdout, which carries
a one-line human summary only.

## 6. JSON schema (`result.json`, schema id `oi-ledger-coverage/1`)

```
{
  "schema": "oi-ledger-coverage/1",
  "tool": {"path": str, "blob_sha256": str},
  "operation": "verify-record" | "check-coverage" | "self-test",
  "inputs": {"repo_head": str|null, "pin": sha, "record": {"commit": sha, "tree": sha},
             "candidate": sha|null,
             "segments": [{"index": int, "from": sha, "to": sha, "kind": "ledgered"|"unledgered",
                           "ledger": {"rev": sha, "path": str, "sha256": str,
                                      "edits_sha256_ok": bool}|null}],
             "prior": sha|null, "adjudications": [{"rev": sha, "path": str, "sha256": str}],
             "anchors_sha256": str},
  "preflight": [{"id": str, "passed": bool}],
  "record_checks": {"digest_equal": bool, "rebuild_equal": bool, "render_equal": bool,
                    "ck_errors": [str], "extended_unmapped": [str], "frozen_self_test": bool}|null,
  "sites": [{"site_id": str, "anchor_sha256": str, "row": str|null, "code": str|null,
             "owner": str, "status": "unchanged"|"moved"|"authorized-replacement"|
             "authorized-removal"|"adjudicated"|"unauthorized-change"|"missing"|
             "duplicated"|"ambiguous", "origin_segment": int|null,
             "current": {"file": str, "lines": [int, int], "sha256": str}|null,
             "line_delta": int|null, "splices": [{"id": str, "old_sha256": str,
             "new_sha256": str}], "anchor_survives": bool|null, "whitespace_only": bool|null,
             "context_changed": bool, "pre_existing": bool|null}],
  "file_conformance": [{"segment": int, "file": str, "status": "identical"|"conforms"|
                        "unauthorized-edit"|"unledgered-file-change",
                        "ranges": [[int, int]]}],
  "hits": [{"file": str, "line": int, "line_sha256": str, "patterns": [str],
            "status": "held"|"unmapped-hit", "held_by": str|null, "attribution": str|null}],
  "findings": [{"fingerprint": str, "class": str, "subject": str, "segment": int|null,
                "pre_existing": bool|null, "detail": str}],
  "counts": {"<status or class>": int},
  "verdict": "HOLDS"|"FAILS"|"ERROR"|"VOID",
  "exit_status": int
}
```

`verdict` is computed only from `preflight`, `record_checks` and `findings`: `HOLDS` iff every
preflight passed, `record_checks` (op A) are all equal/empty/true, and `findings` is empty. A
finding's `fingerprint` is SHA-256 over `(class, subject, segment, from bytes sha, to bytes sha)`
so that it is reproducible and matchable by adjudications. Lists are sorted by
`(file, line, site_id)`; no timestamps, durations or host data appear (sec. A.42 item 1). A JSON
Schema file for `oi-ledger-coverage/1` ships with the tool; any incompatible change bumps the
version.

## 7. Failure conditions (all fail closed)

Findings (exit 1): `unauthorized-change`, `missing`, `duplicated`, `ambiguous` (including a
translation/search disagreement in 4.3), `unauthorized-edit` (ledgered file differs from
FROM+splices), `unledgered-file-change` in a ledgered segment, `unmapped-hit`,
`stale-adjudication`, `pin-anchor` (op A: a pin line not unique, an override anchor not in its pin
line, a `read` key with no line); op A `record_checks` not all holding.

Errors (exit 3): unresolvable REV or missing blob; record tree id or pin mismatch; manuscript
digest mismatch at the pin; ledger `base` not FROM; splice hash, span, overlap or base-blob
mismatch; `edits_sha256` mismatch; broken segment chain; invalid UTF-8 or CR in a corpus file;
schema-invalid adjudication. Usage (exit 2): unknown flag; `--out` non-empty or inside a worktree.
Void (exit 4): any preflight or self-test control fails.

There is no warning that can turn a failure into a pass, and no flag lowers the bar: a caller
wanting only "new since H" reads `findings[*].pre_existing` from the JSON; the exit status still
reports every finding.

## 8. Test matrix

### 8.1 Unit controls (synthetic in-memory trees; also the preflight U1-U4)

| Id | Case | Expected |
|---|---|---|
| U1 | candidate = pin | HOLDS; all `unchanged` |
| U2 | three lines inserted above a site, unledgered | HOLDS; site `moved`, `line_delta` 3 |
| U3 | same shift produced by a ledgered splice elsewhere in the file | HOLDS; `moved` via translation, search agrees |
| U4 | one word changed in a site line, unledgered | FAILS `unauthorized-change` |
| U5 | site line copied elsewhere in the file | FAILS `duplicated` (context not consulted) |
| U6 | pin-duplicated line, counts unchanged, context matches ordinal | HOLDS |
| U7 | as U6 but the two copies' contexts swapped | FAILS `ambiguous` |
| U8 | site line deleted | FAILS `missing` |
| U9 | whitespace-only change in a site line | FAILS, `whitespace_only` true |
| U10 | ledgered splice rewriting a site line | HOLDS; `authorized-replacement`, splice ids and hashes reported |
| U11 | ledgered splice deleting a site line | HOLDS; `authorized-removal` |
| U12 | new pattern hit on a non-site line | FAILS `unmapped-hit` |
| U13 | hit on a line whose sha is in a converted `read` entry, after a shift | HOLDS (`held_by` read) |
| U14 | matching adjudication for U4 | HOLDS; status `adjudicated` |
| U15 | adjudication whose `to_region_sha256` is wrong | FAILS (`unauthorized-change` and `stale-adjudication`) |

### 8.2 Mutation controls (each run in both directions: the mutant fails, the restored tree holds)

| Id | Mutation | Expected |
|---|---|---|
| M1 | word changed inside a ledgered file outside every splice, not on a site | FAILS `unauthorized-edit` with that range |
| M2 | a splice applied with altered `new` text | FAILS `unauthorized-edit` |
| M3 | ledger `old_sha256` altered | ERROR 3 |
| M4 | ledger span shifted by one byte | ERROR 3 |
| M5 | ledger `base` not FROM | ERROR 3 |
| M6 | site line moved to another file | FAILS `missing` (source file) |
| M7 | frozen `sitemap.json` row value altered (op A) | FAILS `rebuild_equal` false |
| M8 | frozen `LEDGER.md` cell altered (op A) | FAILS `render_equal` false |
| M9 | record tree id not the pinned one | ERROR 3 |
| M10 | `--out` inside the repository checkout | ERROR 2, nothing written |
| M11 | CR inserted into a corpus file | ERROR 3 |

Synthetic cases U* and M1-M6, M10, M11 build trees in memory through the same object-reader
interface used for git; M7-M9 alter in-memory copies of the frozen record; nothing is committed.

### 8.3 Real-tree controls (CI; outcomes stated as rules, prototype counts for reference)

The decision rules are preregistered; the counts below are from a throwaway prototype (sec. 9.4)
and the implementation's own counts are reported, not fitted. A deviation is investigated as a
defect in one or the other, never resolved by tuning the rule.

| Id | Run | Rule | Prototype reference |
|---|---|---|---|
| RT-A | `verify-record --pin E --record H` | HOLDS | digest, rebuild, render equal; CK errors 0; extended 0; frozen self-test true; 697 anchors unique; 135/135 override anchors in pin line |
| RT-A' | `verify-record --pin H --record H` | ERROR 3 (pin mismatch) | n/a |
| RT-E | `check-coverage --commit E` | HOLDS | 697 `unchanged`; 595 hit lines, all held |
| RT-H | `check-coverage --commit H` (one unledgered segment) | FAILS; every finding is a site text changed between E and H or a hit those changes created; 0 `duplicated`/`ambiguous` | 584 resolved (unchanged or moved), 113 `unauthorized-change` (none whitespace-only; the Step-2 merges #1470, #1472-#1475, #1494, which have no exact-edit ledger), about 110 unmapped hit lines |
| RT-T | `check-coverage --commit T1' --segment E..H --segment H..T1'=P:.../a1exit-deletion-20261121/ledger.json --prior H` | FAILS; segment H..T1': 0 `unauthorized-edit`, 0 `unledgered-file-change`, 0 unauthorized site changes; all non-pre-existing findings are `unmapped-hit` `in-authorized-text` | all 23 ledgered corpus files conform, other corpus files identical; of the 584 sites resolved at H: 383 unchanged (215 same line, 168 moved), 197 `authorized-replacement` (each replacement region unique in T1'), 4 `authorized-removal`; 113 carried from E..H; 116 unheld hit lines, of which 93 also unheld at H, 16 inside splices on lines already unheld at H, 7 new hits in replacement text on non-site lines (splices D237, D238, D241, D242, D246, D247, D388) |
| RT-M | RT-T with mutation M1 applied to the in-memory T1' `papers/Main.md` | FAILS with exactly one added `unauthorized-edit` | n/a |

RT-H and RT-T are expected to fail. That is the correct outcome: E..H changed 113 site lines
without an exact-edit ledger, and the retirement's replacement text contains new pattern hits
that no classification covers yet. A clean result at H or T1' requires reviewed adjudication
records (4.6), which are separate work (Q1).

## 9. Demonstration plan

### 9.1 What it shows

That a pure line shift passes and a meaningful unauthorized change fails, on real objects:

1. RT-E (HOLDS) and RT-T segment H..T1': 168 site lines moved by authorized splices elsewhere in
   their files resolve as `moved`, where the frozen tool reported 55 CKa and 52 CK3 errors.
2. A shift-only mutant of `E` (one blank line prepended to `papers/Main.md` and FULL, in memory):
   HOLDS, every site in those files `moved` by 1; the frozen tool on the same tree would fail
   with PIN MISMATCH.
3. A meaning mutant of `E` (one qualifying word, "finite", deleted from one Main site line):
   FAILS with exactly one `unauthorized-change` for that site id.
4. M1 on T1': FAILS with exactly one `unauthorized-edit`.

### 9.2 Reviewer reproduction

From a clean clone of `main` at the landing commit, with no other state:

```
python3 -I -B <tool> self-test --real-trees --out <empty dir outside the clone>
```

The run writes `result.json` per control under the given directory; the reviewer checks
`verdict` and `exit_status` per control against 8.1-8.3, and that `git status --porcelain` in the
clone is empty afterwards. The same commands run in CI on the landing commit (sec. A.40).

### 9.3 What the demonstration cannot show

That moved or authorized text means what the ledger says. Sec. 1 non-goals; the review of each
`authorized-replacement` against its splice's reason, and of each `context_changed` site, stays
with the reviewers.

### 9.4 How the reference figures were measured (read-only)

- Frozen tool: each tree's `papers/*.md` and `book/*.md`, plus `R` and the two Phase directories
  from H, were written via `git show REV:path` into a disposable directory (not `git archive`,
  see 3.2), `ledger_check.py` was imported there and `check(..., quiet=True)` called directly,
  after `build()` for H and T1'.
- Prototype relocation: site line bytes at E compared as whole lines at H and T1'; for H..T1',
  overlap of each site's H byte span with `ledger.json` splice spans, the splices applied to the
  line-extended region and the result counted in T1'. All 399 splice `old_sha256` match H; 33
  splices span several lines; every ledgered corpus file of T1' equals its `expected_sha256`.
- Hit attribution: Phase-0 and extended patterns on each tree, held sets as in 4.7.

## 10. Implementation steps and acceptance criteria

| Step | Work | Acceptance |
|---|---|---|
| S0 | Preregistration: decision rules of 4-8, schema, control list | owner-reviewed before any code; rules frozen, numbers not |
| S1 | Object reader (`git cat-file --batch`), REV resolution, `--out` guard | byte equality with `git show` on 50 sampled blobs; M10 passes; no write outside `--out` (checked by a tree listing before and after) |
| S2 | Op A replay and record checks | RT-A holds, RT-A' errors, M7-M9 fail; replay reads no printed text |
| S3 | Anchor map derivation | 697 sites, deterministic `anchors_sha256` across two runs and two Python versions; pin findings 0 |
| S4 | Ledgered segment engine | reproduces the 23 T1' corpus files byte for byte from H and `ledger.json`; translation and search agree on all sites; M1-M5 behave |
| S5 | Unledgered segment engine and duplicate rules | U1-U9 behave; no code path uses line-number proximity or a similarity score to resolve |
| S6 | Hit scan and attribution | full lists; RT-E 0 unmapped; patterns read from the record, not retyped |
| S7 | `result.json`, schema file, exit codes | every output validates; verdict recomputed from `findings` by an independent 20-line checker equals the tool's |
| S8 | Self-test and mutation suite | all U*, M* green in both directions; preflight wired into every run |
| S9 | Real-tree controls in CI | RT-* meet their rules; counts recorded in the landing record with the commit and command (sec. A.42 item 1) |
| S10 | Independent non-author review and owner merge decision | review recorded on the guiding PR; landing per sec. 12 |

## 11. Rollback

The tool adds new files only (the tool, its schema, its self-test fixtures, its preregistration);
it modifies no existing file, adds no release-gate step and no workflow trigger in its first
landing, and nothing else imports it. Rollback is a revert of the landing commit, which removes
the tool and leaves the frozen record, the retirement plan and every gate exactly as before.
Outputs exist only in caller-chosen directories outside the repository, so there is no tracked
state to clean up. Each `result.json` names the tool's blob SHA-256, so results from a defective
version are identifiable after a forward fix. Wiring the tool into the release gate, if ever
wanted, is a separate change with its own review.

## 12. Governance

- The tool is not an A1-retirement gate. It does not decide, condition or delay the A1
  retirement, and does not substitute for the pending sec. 11 item 2 exception of the retirement
  plan, which is decided by the owner on its own record.
- It lands only after the A1 retirement lands, as a separate pull request with its own
  independent review and a separate recorded owner merge decision (sec. A.45 rule 7).
- The frozen record `R` and its `ledger_check.py` stay byte-identical (sec. A.42 item 6, sec.
  A.46); the new tool reads them and never replaces them.
- Placement under sec. A.36: a new audit directory under `verification/audits/foundations/`
  (proposed), or `tools/` if the owner prefers (Q4).
- Its output is verification evidence for coverage only; a `HOLDS` strengthens no claim and moves
  no row (sec. A.22, A.46 item 1).

## 13. Open questions for the owner

- Q1. E..H changed 113 site lines through the Step-2 merges without an exact-edit ledger. Should
  they be resolved by reviewed adjudication records (4.6), or by an exact-edit ledger
  reconstructed for E..H and reviewed against the Step-2 records? Until one exists, every
  candidate after E fails B by design.
- Q2. The 7 new pattern hits in T1' replacement text (and any like them): classified by
  adjudication records, or by an amendment of the ledger's `new_site_rules` in a new record?
- Q3. Should `context_changed` on an unchanged site fail closed rather than be reported?
- Q4. Placement: audit directory or `tools/`; and whether B should ever cover non-manuscript
  ledgered files (currently left to `preserve_check.py`).

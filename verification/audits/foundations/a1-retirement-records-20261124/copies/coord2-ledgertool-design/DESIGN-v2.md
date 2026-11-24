# Commit-independent ledger and terminology verification tool: design v2

Status: paper-only design. Nothing is implemented, committed or published under it.
Implementation needs a separate recorded owner authorization (AGENTS.md sec. A.45 rule 3).
`DESIGN.md` (v1) stays as written. This document supersedes it where the two differ.

Goal link (sec. A.47): supporting verification tooling. The tool decides whether a tree's
manuscript sites, ledgered replacements and terminology hits are accounted for. It decides no
scientific question, and no row disposition. Accountable Issue: #1169.

Notation as in v1:

- `E` = e837e3db... is the ledger pin.
- `H` = 53c6601a... is the base of the retirement ledger.
- `T1'` = 14ac71b4... is the executed trial tree.
- `P` = 4c79be64... is the plan commit.
- `R` is the frozen ledger record directory, tree b05efdca....

***

## 0. What changed from v1, and why

| Change | Reason |
|---|---|
| Three-state outcome: PASS / REVIEW_REQUIRED / FAIL (plus ERROR, VOID). New exit codes (sec. 5) | Owner: unresolved review must block acceptance without being reported as a violation |
| E..H site changes are resolved by **provenance adjudications**: reviewed records checked against the first-parent merges of #1470, #1472-#1475 and #1494. They form a separate obligation class `HP` (sec. 4) | Owner Q1. There is no retrospective ledger. Insufficient provenance is a FAIL. These changes are never attributed to the A1 retirement |
| New pattern hits in authorized replacement text are REVIEW_REQUIRED until each is classified individually | Owner Q2. A splice's provenance is not semantic correctness |
| Context changes are always reported. A context change is a FAIL when context is needed for identity or for meaning (sec. 3.4) | Owner Q3 |
| The executable lives under `tools/`. Immutable records (rule files, adjudications, scan profiles) live in a separate audit directory (sec. 11) | Owner Q4 |
| A pin mismatch is the structured error `PIN_MISMATCH`. Any uncaught exception becomes the structured error `INTERNAL`, never a traceback-only exit | Owner. The frozen `ledger_check.py` raises `TypeError` in its PIN MISMATCH report at `H` |
| **Reviewed classification rules** (sec. 6): a versioned rule file whose rules carry fingerprints, scope, reviewer and owner record. A rule that stops matching becomes REVIEW_REQUIRED or FAIL | Owner scope extension: discriminating false positives |
| One framework with four operations over one engine: `record` (A), `coverage` (B), `execution` (C) and `terms` (D) (sec. 2) | Owner. The retirement plan's `edits_check.py` treats these cases separately, and two of its modes check the wrong tree (sec. 1) |
| Every site, hit and file receives a machine-readable `explanation` (sec. 7) | Owner: auditable classification |
| Adversarial tests, including rule abuse and a disguised reintroduction of the retired claim (sec. 9) | Owner |
| Four distinct trees, each with its own invariants: the scientific base `H`, the integration base `M` (current `main`), the candidate retirement tree `X`, and the landing merge `L` (sec. 13) | Owner: the tool lands on `main` before the retirement, and the amended plan uses it. The plan's `preserve_check.py --base W` failed on the execution commit, because it compared the candidate with a moved `main` |
| Landing order reversed: the tool lands before the A1 retirement (sec. 11) | Owner |

Unchanged from v1, and restated only briefly here:

- Identity anchors: the exact pin line bytes, with the pin count, ordinal and context hash. Overrides
  are bound to site ids. `read` entries are converted to line hashes.
- Ledgered segments: file conformance to base plus splices, offset translation cross-checked by
  search, and authorized replacement and removal.
- Unledgered segments: exact search only, with nothing chosen by line proximity or fuzzy score.
  A count change is `duplicated`.
- Operation A replays the frozen tool only at its pin.
- Writes go only to `--out`, which lies outside every worktree. Reads come from the object store
  only.
- The rollback and governance provisions of v1 sec. 11-12 stand.

## 1. Grounding: what the retirement plan's checker does (`edits_check.py` at `P`)

- **`--commit REV`** runs `check()`, which requires each edit's `old` (or `old_step2`) to occur
  exactly once at REV. That is a precondition test for a tree *before* execution. On an executed
  tree the old strings are gone, so it fails by construction. It cannot verify that the
  replacements were made.
- **`--pins`** runs `pins_check(data, a.commit or data['drafting_base'])`. The literals of tracked
  Python checks are compared before and after `apply_edits()` at the given REV. Run at the
  executed tree or its parent, it evaluates the edits against the wrong pre-edit text. The correct
  pre-edit tree is the ledger's `base`, which is not necessarily the executed commit's parent.
- **`--repo-scan`** with `classify()` explains hits by `EXPLAINED` entries `(path, substring,
  class, reason)`. An entry with substring `None`, or with a path ending in `/`, explains *every*
  hit in that file or directory. Examples are `tools/citation_roles_check.py` and
  `papers/oi_lattice_code/`. A substring entry deletes its text from the line and then re-tests
  the line, which is a residual check, but it is unanchored. The entry still applies if the line
  around it changes. Nothing detects an entry that no longer matches. This is the rule-abuse
  surface that sec. 6 closes.
- The **count checks** of `identifier_sim()` (lines 331-335) forbid the retired counts. Examples are
  `are six structural properties of the substratum` and `six structural assumptions`. A broader
  count scan would also hit the legitimate "six structural properties *of the bijection*"
  (isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation
  count). Those are worked examples W1 and W2 in sec. 6.4.

## 2. One framework

**Engine.** The tool has one engine with five parts:

- An object reader (`git cat-file --batch`).
- A segment chain from a stated origin to the candidate.
- A site model (v1 anchors).
- A hit model (scan profiles plus classification rules).
- One result writer (sec. 7).

Every operation is a configuration of the engine, not a separate code path.

| Op | Subcommand | Question | Origin | Uses |
|---|---|---|---|---|
| A | `record` | Is the frozen record `R` correct at its own pin? | pin `E` | frozen-tool replay (v1 sec. 3.2), anchor derivation |
| B | `coverage` | Is every site of `R` accounted for at commit C, and every hit classified? | pin `E` | segments, provenance adjudications, rules |
| C | `execution` | Is candidate `X` exactly `H` plus the ledger, with its preconditions met at `H` and its pins intact? Does landing `L` compose current `main` with `X` exactly (sec. 13)? | ledger `base` = `H` | one ledgered segment, pins, terms on the replacement text |
| D | `terms` | Is every terminology hit at C classified, with no deny-rule match? | none (whole tree) | scan profiles, rules |

**Op C (replacement verification on an executed tree)** runs these checks:

1. Resolve the pre-edit tree as the ledger's `base`, which must be `H`. Never use `main`, and never
   use whatever commit happens to be checked out. The candidate's parentage and the landing merge
   are checked under the tree roles of sec. 13.
2. Check the preconditions at the base:
   - Every splice `old_sha256` matches its span.
   - Every `edits.json` `old` occurs exactly once at the base, which is the `--commit`
     test moved to the right tree.
   - `edits_sha256` matches.
   - Every edit id maps to exactly one splice, with equal hashes. The `retained_unchanged`
     edits (D032, D039) map to none, and their site text is unchanged at C.
3. Check the postconditions at C:
   - Every ledgered file conforms to base plus splices (v1 sec. 4.3).
   - Every splice's `new` lies at its translated span.
   - Every non-ledgered file is identical to the base, except paths in the plan's **delegation
     list** (derived TeX/PDF, regenerated artifacts, the plan's own record directory). Those
     are `delegated`. They PASS only when the named checker's structured result at C (exit status
     and a JSON field, sec. A.44) is supplied with `--delegated-result`. Otherwise they are
     REVIEW_REQUIRED.
4. Check the pins. For each string literal of each tracked Python check at C, compare its presence
   in the ledgered targets at the base and at C. A literal present at the base and absent at C
   PASSes only if a guard-pin splice changed it or a recorded reason allows it (`PIN_OK`). Every
   pin updated by a splice must occur in its target at C. The literals are extracted with `ast`,
   as `py_literals()` does.
5. Run op D restricted to the text of every replacement region. Hits there are REVIEW_REQUIRED
   unless a rule classifies them (owner Q2).

**Scan profiles.** These are named regex sets loaded from their source records by extraction,
never retyped:

| Profile | Source and extraction |
|---|---|
| `p0-core`, `p0-para` | Phase-0 `sites.json` |
| `ledger-ext` | `EXTENDED_PATTERNS` in `R/ledger_check.py`, by `ast` |
| `ptr`, `repo` | `PTR` and `REPO_PAT` in the plan's `edits_check.py`, by `ast` |
| `posit-count` | a new reviewed profile file, for count-of-assumptions phrasing |

A profile records its source blob id and the SHA-256 of the extracted pattern. A changed source
is an input error, unless the profile file is re-reviewed.

## 3. Site and hit decisions (B, C, D)

### 3.1 Sites

The v1 statuses are kept. The decision column is new.

| Status | Decision |
|---|---|
| `unchanged`, `moved` (identity verified, context unchanged or not needed) | PASS |
| `authorized-replacement`, `authorized-removal` | PASS for coverage. A hit in the new region goes to sec. 3.2 |
| `provenance-adjudicated` (sec. 4) | PASS |
| `unauthorized-change`, `missing`, `duplicated`, `ambiguous` | FAIL |
| E..H change with no provenance adjudication | FAIL, class `HP` |

### 3.2 Hits

The first matching row decides.

| Condition | Decision |
|---|---|
| a deny rule matches the hit's sentence | FAIL |
| held by a resolved site whose classification still applies (unchanged bytes) | PASS |
| an allow rule applies with every check of sec. 6.2 met | PASS |
| an allow rule's scope and matcher apply, but its fingerprint or context no longer matches | REVIEW_REQUIRED (`rule-fingerprint-mismatch`) |
| in authorized replacement text, with no rule | REVIEW_REQUIRED (`unclassified-in-authorized-text`) |
| anywhere else, with no rule | REVIEW_REQUIRED (`unclassified`) |

### 3.3 Rules and records

| Condition | Decision |
|---|---|
| a rule's fingerprinted instance occurs nowhere in the tree | REVIEW_REQUIRED (`rule-stale`) |
| an allow rule matches more instances than its `max_instances` | FAIL (`rule-overreach`) |
| a rule file fails lint (sec. 6.3) | FAIL (`rule-invalid`) |
| an adjudication's fingerprint matches nothing | FAIL (`stale-adjudication`) |

### 3.4 Context

`context_sha256` is the hash of the nearest non-blank lines before and after. The sentence context
is the full line. Both are recorded at the pin, or in the rule fingerprint. Whenever either
differs, `context_changed: true` and both hashes are reported.

The context change is a FAIL in two cases:

- **Identity.** The anchor had more than one occurrence at the pin, so the context hash is part of
  the disambiguator (v1 sec. 4.4).
- **Meaning.** The classification depends on the context. This applies to an allow rule with
  `context_required: true`, to an adjudication with `meaning_context: true`, and to a site whose
  frozen S3 column cites a qualification outside its own line. Such a site carries
  `meaning_context: true` in the anchor map. It is derived at the pin from the frozen `s3`
  string; a site whose `s3` is `not determined` is treated as needing context.

Otherwise the change is reported, and relocation stands on verified identity with byte-identical
line text.

## 4. Historical provenance obligation `HP` (E..H)

The 113 site lines changed between `E` and `H` are not part of any exact-edit ledger. A prototype
walk of `H`'s first-parent chain (14 commits) finds the first commit at which each E line stops
being present exactly once. Each of the 113 first changes falls at one of five merges:

| Merge | Sites |
|---|---|
| #1475 | 48 |
| #1474 | 23 |
| #1470 | 15 |
| #1473 | 15 |
| #1472 | 12 |
| #1494 | 0 (first changes) |

**Adjudication entry.** Each entry has the kind `provenance` and these fields:

- `site_id`
- `steps`: a list of `{merge, pre_sha256, post_region_sha256}`, one per first-parent commit that
  changes the site's text, in order
- `row`, `code` and `owner` as now applicable
- `semantic_classification`: whether the finite-only, conditional or open qualification is
  visible, with a reason
- `meaning_context`
- `reviewer`, `review_record` and `owner_record`

**Verification by the tool.** Every check must hold:

1. Each `merge` is on `H`'s first-parent chain strictly after `E`, and is the merge commit of one
   of #1470, #1472-#1475 or #1494. The tool resolves each PR number to its commit from the merge
   subject. A given commit id must agree with it.
2. The tool's own first-parent walk reproduces the step list exactly. The site text before step k
   occurs once at that merge's first parent. The `post_region_sha256` occurs exactly once at the
   merge, and persists unchanged until the next step. The last step's region occurs at `H`.
3. No step is skipped. If the walk finds a text change between listed steps, that is a FAIL
   (`provenance-gap`).
4. A change at a commit outside the six named merges is a FAIL (`provenance-foreign`).
5. A region that is not unique at a step is a FAIL (`provenance-ambiguous`).

Provenance shows *where* the text came from. The `semantic_classification` is the reviewer's
judgement of what the text means, and the tool checks only that it is present and fingerprinted.

**Reporting.** Every `HP` item carries `obligation: "HP"` and `segment: "E..H"`. Results group
findings by obligation: `HP`, `RET` (the retirement ledger segment), `TERMS` and `RECORD`. No
`HP` item is counted under `RET`.

## 5. Outcomes, exit codes and precedence

| Outcome | Exit | Meaning | Accepted? |
|---|---|---|---|
| PASS | 0 | every check holds, controls green | yes |
| FAIL | 1 | at least one FAIL item | no |
| REVIEW_REQUIRED | 2 | no FAIL item, at least one REVIEW item | no: blocks until each item is resolved by a reviewed record |
| USAGE | 64 | bad arguments, or `--out` refused | no |
| ERROR | 65 | input integrity: `PIN_MISMATCH`, `RECORD_TREE_MISMATCH`, `BASE_DRIFT`, ledger hash, span or overlap, `SOURCE_CHANGED`, encoding | no |
| VOID | 70 | a preflight or self-test control failed; no verdict | no |
| INTERNAL | 71 | an uncaught exception, recorded with its type and the failing stage | no |

Precedence: VOID > INTERNAL > ERROR > FAIL > REVIEW_REQUIRED > PASS.

Only exit 0 is acceptance. No flag converts REVIEW_REQUIRED to PASS. A caller that wants "new
since prior" reads `items[*].pre_existing` from the JSON.

`PIN_MISMATCH` carries these fields: `expected_pin`, `record_digest`, `computed_digest`,
`candidate`. It is produced before any frozen code runs.

## 6. Reviewed classification rules

### 6.1 Rule file

A rule file has the schema `oi-term-rules/1`. It is an immutable record in the audit directory.
A change is a new file that names the file it supersedes. Each file has these fields:

- `version`
- `supersedes`: `{path, blob_sha256}` or null
- `rules`

Each rule has these fields:

| Field | Content |
|---|---|
| `id` | `TR-nnn`, never reused across versions |
| `kind` | `allow` (a verified false positive) or `deny` (a retired or prohibited claim) |
| `profiles` | the scan profiles whose hits it addresses |
| `scope.files` | exact paths. No prefixes, globs or `None` |
| `matcher.literal` | the exact phrase. It must contain the profile's trigger span |
| `matcher.requires` | literals that must co-occur in the same sentence (for example the enumerated list) |
| `matcher.forbids` | literals whose presence voids the rule |
| `context_required` | bool (sec. 3.4) |
| `max_instances` | int, equal to the number of fingerprints |
| `fingerprints` | a list of `{file, sentence_sha256, context_sha256}`, recorded at a stated commit |
| `reason` | the semantic reason in one or two sentences, for example "counts the bijection's six properties, listed; distinct from the retired posit count" |
| `reviewer`, `review_record` | the non-author reviewer, and a link to the review |
| `owner_record` | the owner decision, quoted with its author and time (sec. A.42 item 7) |
| `recorded_at` | the commit at which the fingerprints were taken |

Sentences are split by a fixed rule: a period, question mark or exclamation mark followed by
whitespace and a capital letter, outside `$...$`, at a line boundary. The split is part of the
schema version.

### 6.2 Applying an allow rule (every check must hold, else see 3.2)

1. The hit's file is in `scope.files`.
2. `literal` occurs in the hit's sentence and covers the profile match span.
3. Every `requires` literal is present, and no `forbids` literal is present.
4. The sentence's SHA-256 equals a fingerprint for that file. If `context_required` is set, so does
   the context hash.
5. **Residual test.** With `literal` removed from the sentence, no pattern of *any* profile
   matches the remainder.
6. No deny rule matches the sentence. Deny takes precedence.

The explanation records each check with its result (sec. 7).

### 6.3 Rule lint (FAIL `rule-invalid`)

The lint fails a rule file on any of these:

- a path prefix or a missing scope
- a literal shorter than 8 characters, or one that does not contain the trigger
- zero fingerprints, or `max_instances` different from the fingerprint count
- a missing reviewer, review record or owner record, or a reviewer equal to the rule author
- a duplicate or reused id
- a `supersedes` hash mismatch

**Widening** also fails the lint unless the rule carries `widening_review`, a separate review
record. Widening means, against the superseded version:

- added files
- a shorter or changed literal
- fewer `requires` or `forbids` literals
- more fingerprints, or a larger `max_instances`
- `context_required` turned off

### 6.4 Worked examples at `T1'` (seed rules, to be reviewed; listed here, not adopted)

**W1. "six structural properties" counting the bijection's properties.** `posit-count` hits at
`T1'`:

- `papers/SM.md:1394` ("every bijection satisfying the six structural properties")
- `book/ch09-universality.md:137` ("the six structural properties developed in Chapter 5
  (isotropy, sublattice structure, link content, anomaly cancellation, taste content,
  generation count)")
- `book/ch19-open-problems.md:198` ("one of the framework's six structural properties of the
  bijection")
- `book/ch19-open-problems.md:212` ("six structural properties of the bijection (developed
  across Chapters 5-7)")
- the FULL mirrors at 2554, 5270 and 5284

Proposed rules: one allow rule per distinct sentence, with these settings:

- `requires` the list or "of the bijection", where the sentence carries it. For SM:1394, whose
  sentence carries neither, `context_required: true` and the reason cites SM's own definition
  of the six properties.
- `forbids` `A1`, `A1-A6`, `finite`, `assumptions` and `axioms`.

A deny rule carries the retired forms in `identifier_sim()` lines 331-335.

**W2. Anomaly condition "(A1)".** `ptr` and `repo` hits at `book/appendix-b-derivations.md:235`
and `:246`, and FULL 5914 and 5925. Allow rules have the literal `(A1) $\mathrm{SU}(3)^3$
anomaly` or `(A1) is automatically satisfied`, `requires` `SU(3)`, and `forbids` `finite`,
`posit` and `substratum`. These replace the `EXPLAINED` and `RESIDUAL_ALLOW` substring entries
by fingerprinted ones.

## 7. Result schema `oi-ledger-coverage/2`

The result keeps the v1 fields (`inputs`, `preflight`, `record_checks`, `sites`,
`file_conformance`, `hits`, `counts`) and makes these changes:

- `outcome` and `exit_status` replace `verdict`.
- `items` replaces `findings`. Each item has these fields:
  - `fingerprint`
  - `decision`: `FAIL` or `REVIEW_REQUIRED`
  - `class`
  - `obligation`: `HP`, `RET`, `TERMS` or `RECORD`
  - `subject`, `segment` and `pre_existing`
- `inputs` adds `operation`, `rule_files[{path, rev, blob_sha256, version}]`,
  `profiles[{name, source_blob, pattern_sha256}]` and `delegated_results`.
- `pins[{check_file, literal_sha256, target, base_present, c_present, resolution}]` is added
  (op C).

Every site, hit, file and pin carries an `explanation`:

```
"explanation": {
  "decision": "PASS"|"REVIEW_REQUIRED"|"FAIL",
  "basis": "anchor-identity"|"ledger-splice"|"provenance"|"rule"|"site-held"|"none",
  "evidence": [{"kind": "anchor"|"translation"|"search"|"splice"|"merge"|"rule"|"fingerprint"|
                "context"|"residual"|"deny"|"delegated", "ref": str, "expected": str|null,
                "observed": str|null, "passed": bool}],
  "rule_ids": [str], "splice_ids": [str], "merges": [str],
  "context_changed": bool, "context_role": "none"|"identity"|"meaning"
}
```

`outcome` is a pure function of `preflight`, `record_checks` and `items`. An independent checker of
about 30 lines recomputes it from the JSON (acceptance criterion S7). The output has no
timestamps or host data, and lists are sorted.

## 8. Failure and review conditions (complete list)

**FAIL** in each of these cases:

- `unauthorized-change`, `missing`, `duplicated` or `ambiguous`
- a context-needed change (sec. 3.4)
- `unauthorized-edit`, or `unledgered-file-change` in a ledgered segment
- `HP` with no adjudication, `provenance-gap`, `provenance-foreign` or `provenance-ambiguous`
- a deny-rule match
- `rule-overreach` or `rule-invalid`
- `stale-adjudication`
- `pin-broken`, or `pin-target-missing` (op C)
- a `retained-changed` site (D032 and D039 must be unchanged)
- op A record checks not holding

**REVIEW_REQUIRED** in each of these cases:

- `unclassified`
- `unclassified-in-authorized-text`
- `rule-fingerprint-mismatch`
- `rule-stale`
- `delegated` without a structured result

The ERROR, VOID and INTERNAL cases are those of sec. 5.

## 9. Test matrix

### 9.1 Kept from v1 (unchanged expected decisions)

U1-U13 and M1-M11. U4, U5, U7, U8 and U9 FAIL. U12 now expects REVIEW_REQUIRED (an
unclassified hit). U14 and U15 apply to provenance adjudications in place of the generic ones.

### 9.2 Adversarial controls (synthetic, in memory; each also restored, to show it flips)

| Id | Case | Expected |
|---|---|---|
| L1 | the W1 sentence shifted by 40 lines | PASS (`rule`, fingerprint and context equal) |
| L2 | the W2 lines moved with the rest of appendix B | PASS |
| L3 | an authorized splice inserting a copy of a fingerprinted sentence into a file in the rule's scope | FAIL `rule-overreach` (the instance count exceeds `max_instances`) |
| V1 | W1's file gets "the six structural properties of the substratum" | FAIL (deny) |
| V2 | "six structural properties of the bijection (isotropy, ..., generation count), one of which is total finiteness" | FAIL (fingerprint mismatch, residual `ptr` match, deny `total finiteness` as a premise) |
| V3 | in appendix B: "(A1) the substratum is finite in total" | FAIL (`forbids` and the residual test) |
| V4 | a legitimate-looking reintroduction: "the framework's sixth structural property, finiteness of the bijection" | FAIL (deny form "sixth ... structural") |
| A1r | a rule widened to a path prefix `book/` | FAIL `rule-invalid` |
| A2r | a literal shortened to "(A1)" | FAIL `rule-invalid` (widening without review) |
| A3r | a fingerprint swapped for a violating sentence's hash without `widening_review` | FAIL `rule-invalid` |
| A4r | the same swap with a forged `widening_review` naming the author as reviewer | FAIL `rule-invalid` |
| A5r | an allow rule fingerprinting a sentence that also matches a deny rule | FAIL (deny precedence) |
| A6r | an allow rule whose literal lies elsewhere in the line than the trigger | FAIL `rule-invalid` (literal must cover the trigger) |
| A7r | a reused rule id in a superseding file | FAIL `rule-invalid` |
| S1r | a fingerprinted sentence edited by one word | REVIEW_REQUIRED `rule-fingerprint-mismatch` |
| S2r | a fingerprinted sentence deleted | REVIEW_REQUIRED `rule-stale` |
| P1 | provenance naming #1473 for a site the walk attributes to #1474 | FAIL |
| P2 | provenance listing one step where the walk finds two | FAIL `provenance-gap` |
| P3 | a site changed by a non-named commit | FAIL `provenance-foreign` |
| C1 | op C on the executed synthetic tree | PASS. The v1 uniqueness test at C would fail; it is applied at the base |
| C2 | op C where C's parent differs from the base in a ledgered file | ERROR `BASE_DRIFT` |
| C3 | a pin literal removed by an edit without a guard-pin splice | FAIL `pin-broken` |
| X1 | `--pin H` on op A | ERROR `PIN_MISMATCH` (structured, exit 65) |
| X2 | an injected exception inside the hit stage | INTERNAL (exit 71) with its stage recorded |

### 9.3 Real-tree controls (CI; decision rules preregistered, prototype counts for reference)

| Id | Run | Rule | Reference |
|---|---|---|---|
| RT-A | `record --pin E --record H` | PASS | as v1 |
| RT-E | `coverage --commit E` | PASS | 697 sites unchanged |
| RT-H0 | `coverage --commit H`, no adjudications | FAIL; every FAIL item is `HP` | 113 `HP` |
| RT-H | the same, with the reviewed provenance file | PASS for sites iff each walk matches; hits REVIEW_REQUIRED until classified | 113 adjudicated (48, 23, 15, 15, 12 as in sec. 4) |
| RT-T | `coverage --commit T1'`, segments `E..H`, `H..T1'=P:ledger.json`, with the provenance file and the seed rules | no `RET` FAIL item; outcome REVIEW_REQUIRED while hits in replacement text are unclassified | 383 unchanged (168 moved), 197 replaced, 4 removed; 7 new hits in replacement text (D237, D238, D241, D242, D246, D247, D388); W1's 7 lines and W2's 4 lines PASS by rule |
| RT-C | `execution --commit T1' --ledger P:ledger.json` | REVIEW_REQUIRED, or PASS once the delegated results are supplied and the replacement-text hits are classified | 399 splices with old hashes verified at `H`; 44 ledgered files, 43 conform byte-exact, plus `verification/coverage/LEDGER.json` (regenerated: delegated); 26 non-ledgered changes (9 TeX, 9 PDF, the plan's record directory, one regenerated SC-42 result): delegated |
| RT-D | `terms --commit T1'` with the seed rules | no deny match; W1 and W2 PASS | as RT-T for the corpus |

The counts are the implementation's to report. A deviation is investigated as a defect, never
fitted.

## 10. Demonstration and implementation deltas

The demonstration keeps v1 sec. 9 and adds these cases:

- W1 and W2 shifted: PASS.
- V1-V4 and A1r-A7r: FAIL.
- S1r: REVIEW_REQUIRED.

A reviewer reproduces all of them with `tools/<tool> self-test --real-trees --out <empty dir>`
and reads `outcome` per control.

Implementation steps are added to v1 sec. 10:

| Step | Work | Acceptance |
|---|---|---|
| S4b | Op C: base resolution, preconditions, postconditions, pins, delegation | C1-C3 and RT-C behave; the v1 uniqueness test reproduces `edits_check.check()` results at `H` (0 failures) |
| S5b | Provenance walk and the `HP` adjudication check | P1-P3 behave; the walk reproduces the sec. 4 attribution |
| S6b | Scan profiles by extraction; the rule engine and lint | the profile hash is stable; L, V, A and S controls behave; the residual test is mutation-tested |
| S7 (revised) | Schema `/2`, explanations, outcome checker | the independent checker agrees on every control's JSON |
| S11 | Reviewed seed rule file and provenance file, as records in the audit directory | non-author review recorded; owner record quoted |
| S12 | Tree roles and the landing composition check (sec. 13) | R1-R14 and RT-X/RT-L behave; the tool's own landing diff touches no ledgered path (checked by the tool on its own landing PR head against `H`) |

## 11. Placement and governance

- The executable `tools/ledger_coverage.py` and its JSON schemas carry the self-test fixtures as
  in-memory data, so no fixture files are tracked.
- The immutable records go in a new audit directory under `verification/audits/foundations/`
  (sec. A.36):
  - the scan-profile file for `posit-count`
  - the rule files `oi-term-rules/1`
  - the provenance adjudications for `HP`
  - the hit classifications for replacement text
  - the landing record of the real-tree runs (commit, command, result: sec. A.42 item 1)
- The tool lands on `main` before the A1 retirement, by its own independent review and its own
  owner merge decision. The retirement plan is then amended, as a separate reviewed record, to use
  it with every check passing as written.
- Landing the tool by itself decides nothing about the retirement. It does not substitute for the
  pending sec. 11 item 2 exception, which the owner decides on its own record.
- The tool's landing may add files only under `tools/` and its audit directory. It may not touch
  any file that the retirement ledger touches. This is checked in S12 and sec. 13.2, so that the
  landing cannot drift the base of the retirement.
- The `HP` obligation is a separate historical-provenance obligation. It is tracked on its own
  accountable Issue, or as its own row on #1169 (owner's choice), and is never attributed to the
  retirement.
- Rule and adjudication records strengthen no claim. A PASS is necessary for coverage, never
  sufficient for correctness. Semantic correctness of replacement text stays with the retirement
  plan's preservation checks, the independent non-author review of the exact head, and the
  owner's decision.

## 12. Open points (minor; for implementation preregistration)

- Where the delegation list comes from: the plan's PREREG table, or a structured file. The
  delegated checkers' structured outputs must exist (sec. A.44). Whether `preserve_check.py`
  emits one is to be confirmed.
- Whether `posit-count` belongs in this tool's profile file or in the retirement plan's
  successor record.

## 13. Four trees and their invariants

The tool lands on `main` before the retirement, so `main` moves relative to `H`. It moves at
least by the tool's own landing, by W = 413b0bb88f39cad901befcf4684355c7ee39480b (which changes only
`.github/workflows/a1exit-trial-verify.yml` relative to `H`), and by the plan's amendment. The plan's
`preserve_check.py --base REV` compares the candidate with REV and refuses REV unless the ledgered
files agree. Given W, it compared the execution commit's unledgered workflow file (`H`'s
eight-PDF copy) with W's nine-PDF copy, and so failed on a change that was never a retirement
edit. The cause is that one comparison base was asked to do two jobs. The tool gives each job its
own named tree and invariants, and never substitutes one tree for another.

### 13.1 Roles (flags of `execution`; each resolved once to a full commit id)

| Role | Flag | Example | Decides |
|---|---|---|---|
| Scientific base | `--scientific-base H` | 53c6601a | what the retirement edits are relative to: spans, old hashes, pins, sites |
| Integration base | `--main M` | W today; later `main` with the tool and the plan amendment | which unrelated authorized changes the landing must carry |
| Candidate | `--candidate X` | `T1'`; later the execution commit | the retirement's own tree |
| Landing | `--landing L` (optional) | the merge commit, or an in-memory merge for prediction | the tree that enters `main` |

### 13.2 Invariants (each is a named check with an explanation; failures are listed in brackets)

**Scientific base `H`:**

- `H` equals the ledger's `base` [ERROR `SCIENTIFIC_BASE_MISMATCH`].
- Every ledgered file's blob at `H` hashes to its `base_sha256` [ERROR].
- The anchors and the `HP` provenance chain end at `H`.
- `H` is never re-derived from `M`, `X` or `L`.

**Integration base `M`:**

- `H` is on `M`'s first-parent chain [ERROR `MAIN_NOT_DESCENDANT`].
- Every path that differs between `H` and `M` is listed as a **side change**, with the first-parent
  merge on `M` that made it.
- A side change touching no ledgered path is `unrelated-authorized`. It is reported under
  obligation `MAIN`, never under `RET`, and is not a retirement edit. Examples are W's workflow, the
  tool's landing and the plan amendment.
- A side change touching a ledgered path is `base-drift`, and the retirement's spans no longer
  describe `M`. It is a FAIL for the landing, unless a reviewed reconciliation record (13.3) covers
  it. It never makes `X` fail.
- A side change to a corpus file is also checked by op B as an unledgered segment `H..M`. Its
  items carry obligation `MAIN`.

**Candidate `X`:**

- `X` has exactly one parent, and it is `H` [FAIL `candidate-parent`].
- Every ledgered file equals `H` plus its splices.
- Every other path equals `H`, or is delegated.
- The pins and preconditions are evaluated at `H`, and the postconditions at `X`.
- `M` is not read for any of these checks. A side change is therefore never mistaken for a
  reverted retirement edit.

**Landing `L`:**

- `L` has exactly two parents: the first is `M`, the second is `X` [FAIL `landing-parents`].
- `M` is the `--main` given, and the landing record states it.
- For every path `p`, with `dX = X[p] != H[p]` and `dM = M[p] != H[p]`:
  - neither changed: `L[p] = H[p]`
  - only `X` changed: `L[p] = X[p]`
  - only `M` changed: `L[p] = M[p]` [FAIL `landing-drops-main-change` otherwise]
  - both changed:
    - if `X[p] = M[p]`, then `L[p]` equals that blob (for example the plan's record directory,
      if it lands identically on both)
    - otherwise, `L[p]` must equal the blob named in a reconciliation record [FAIL
      `landing-conflict-unresolved`]
  - Any other path content is a FAIL [`landing-extra-change`].
- **Exactly the execution's own diff.** The diff `M..L`, restricted to paths that `M` did not
  change, equals the diff `H..X` (sec. A.39). The diff `X..L` equals the side changes `H..M`, except
  on reconciled paths.
- Delegated derived artifacts (TeX/PDF) of a ledgered source that `M` also changed are `both
  changed`. They need a regeneration result at `L` (delegated, structured) or a reconciliation
  record.
- Op B on `L` uses the chain `E..H` (`HP`), `H..X` (ledger, `RET`) and `X..L` (unledgered,
  `MAIN`). The landing therefore keeps the coverage result of `X`, and adds only `M`'s side
  changes.

### 13.3 Reconciliation record

A reconciliation record is reviewed and immutable, and lives in the audit directory. It contains
the following:

- `M`, `X` and the paths it covers
- for each path: `H`, `M`, `X` and `L` blob ids, and the resolution
- for a ledgered path, the splices that still apply to `M`'s text. These are re-verified by hash
  and span against `M` and translated by `M`'s own change.
- the reviewer and the owner record

The record resolves conflicts by merits (sec. A.39). It never relabels a side change as a
retirement edit, and never the reverse.

### 13.4 Tree-role controls (added to the test matrix, sec. 9)

| Id | Case (synthetic unless stated) | Expected |
|---|---|---|
| R1 | `M` = `H` plus a workflow change; `X` = `H` plus splices | `X` PASS; side change `unrelated-authorized` under `MAIN` |
| R2 | the same, with the old-style comparison of `X` against `M` run as a countercontrol | the countercontrol reports the workflow path: that comparison is not used |
| R3 | `X` with parent `M`, not `H` | FAIL `candidate-parent` |
| R4 | `X` as a merge (two parents) | FAIL `candidate-parent` |
| R5 | ledger `base` not equal to `--scientific-base` | ERROR `SCIENTIFIC_BASE_MISMATCH` |
| R6 | `M` not descending from `H` | ERROR `MAIN_NOT_DESCENDANT` |
| R7 | `M` changes a ledgered file outside the splices; no reconciliation record | `X` PASS; landing FAIL `landing-conflict-unresolved`; item `base-drift` under `MAIN` |
| R8 | R7 with a reviewed reconciliation record whose `L` blob matches | landing PASS |
| R9 | `L` with its parents swapped | FAIL `landing-parents` |
| R10 | `L` that drops `M`'s workflow change (carries `H`'s copy) | FAIL `landing-drops-main-change` |
| R11 | `L` with one extra word in an unledgered file | FAIL `landing-extra-change` |
| R12 | `L` that loses one splice of `X` | FAIL (the diff `M..L` differs from `H..X`) |
| R13 | `M` contains the tool's own landing (`tools/` and the audit directory only) | `unrelated-authorized`; `X` and `L` PASS |
| R14 | the tool's landing touches a ledgered path | FAIL `base-drift` at S12 |
| RT-X | real objects: `--scientific-base H --main W --candidate T1'` | candidate checks as RT-C; one side change (`.github/workflows/a1exit-trial-verify.yml`) `unrelated-authorized`; no `RET` item from it |
| RT-L | real objects: an in-memory landing with parents (W, `T1'`), built by the composition rule and never committed | composition PASS; the workflow at `L` equals W's blob; the mutant with `H`'s copy FAILs `landing-drops-main-change` |
| RT-L2 | after the tool lands: the same with `--main` set to the `main` that contains it | side changes = W, the tool and the plan amendment, all `unrelated-authorized`; otherwise as RT-L |

The in-memory landing for RT-L and RT-L2 is a synthetic commit object held by the tool's reader. No
merge or ref is created in the repository.

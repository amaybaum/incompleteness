# Batch collector: trust boundary for served-file parsing and output publication

**Status: design only.** The independent design review of `3c0e1d72` approved it with required amendments A1 to
A7. This text includes them, together with the review's D1 recommendation and the owner's decisions on PR #862
(comments 6247145466 and 6247194704): a per-file catch of a scan's conversion error (`ValueError`), and a boundary
by stage and error kind that sends host failures to ABORTED. The table at the end shows where each one landed.

**Revision after the acceptance review of `a77c85a5` [rev D1, D2, D3].** The design confirmed at `ab2a17fb` is
implemented at `a77c85a5`. Its acceptance review returned two blockers, AR-B1 and AR-B2 (section 0). The owner's
decision on PR #862 (comment 6247938850) authorized one design-first revision with three directions: D1, the
inventory precedes every interpretation; D2, a strict integer schema for the jobs list; D3, five named host-failure
regressions with old-behaviour mutants. Every block this revision changes or adds carries the marker
`[rev Dn]`, naming the direction it implements. `[rev AR-N1]` and `[rev AR-N2]` mark the two non-blocking notes of
the acceptance review that it also closes; its notes are called AR-N1 to AR-N6 here, to keep them apart from the N1
to N3 of the review of `09d439d0`. A block without a marker is as confirmed at `ab2a17fb`.

Nothing in the revision is implemented. The design was first written against commit `09d439d0`, and every unmarked
"now" statement below describes the code at that commit. Each one cites `batchx/collect.py` as `collect.py:N`, or
names the other file it is in. The revision's own citations are to the implementation and are written
`a77c85a5:collect.py:N`. After design review, one bounded correction (section 8) follows, and then a fresh exact-SHA
acceptance review. If that review finds a fail-open escape, an incomplete published inventory or a substantive design
contradiction, the work returns to the owner. It is not patched again.

The owner's binding invariants (PR #862, comment 6246308787) are restated where they are enforced, so each one
can be checked against a mechanism:

- **I-PARSE.** Strictly parse the *entire* served JSON object before any semantic interpretation. Reject
  duplicate keys at every depth, unknown fields and wrong field types. The only allowed top-level keys are the
  required `job_id`, `logs_content` and `original_length`, plus an optional `message` that must equal the tool's
  exact success response. No first-wins or last-wins shadow content.
- **I-QUAR.** Any schema, attribution, completeness or validation failure quarantines the entire collection, and
  the collection then yields no usable runs or results. Tests read the output on disk.
- **I-PUB.** A pre-existing output directory never exposes stale usable files as a current result. Output is
  published through a fresh output location, transactionally. Every rejected file that can be hashed is traceable
  by name and digest, and missing expected files are recorded as a separate category.
- **I-SET.** The full preregistered 223-run target is retained. A collection marks runs usable only if its whole
  predeclared expected set succeeds.
- **Governing invariant.** A run may be marked usable only when the complete evidence collection succeeds and every
  relevant served file has been identified, validated and reconciled.

## 0. The defect, and what the design must make true

**H1 (review of `09d439d0`, §4).** `parse_served` (`collect.py:141-151`) calls `json.loads`. That keeps the last of
any duplicated key and ignores unknown keys. `identity` (`collect.py:136-138`) covers only the three values the
parser kept. So content the collector never saw could sit in an accepted file. D5, D1b and X3 each ended
`COLLECT HOLDS` with 6 usable runs.

**Three related gaps, found while writing this design.** Each was confirmed with a scratch probe against
`09d439d0`. The scratch tools are outside the repository.

- **B1. Non-standard constants reach a published result.** A result block containing `NaN` or `Infinity`, with a
  matching SHA256 line, passes the canonical round-trip at `collect.py:283-285`, because
  `json.dumps(float("nan"))` writes `NaN`. The collection HOLDS with 6 usable runs, and `ci/800/results.json`
  contains `NaN`.
- **J1. The jobs list is parsed last-wins, and its ids need not be distinct** (`collect.py:1081-1082`, `:126-130`).
  A job object `{"id": 5, …, "id": 6}` indexes job 6. One id under two shard names, `{1: 5, 2: 5}`, is accepted with
  no problem recorded.
- **E-esc. The outcome depends on how a name is spelled in JSON.** Take genuine S3 with an indented trailer line
  `BATCH SHARD 1/3 …`. Spelled plainly, it voids shards 1 and 3 (FAILS). Spelled with `\u0042ATCH`, its decoded
  `logs_content` is byte-identical, yet it HOLDS with 6 usable runs. The byte scan (`raw_named`, `collect.py:199-210`)
  does not decode JSON escapes of letters. The parsed reading (`shards_named`, `:164-178`) is anchored at the line
  start. No shard-1 result is taken from S3's file, so no wrong result is published. But a file that names
  shard 1 leaves shard 1 usable, which DESIGN.md:184-185 says cannot happen.

**Two findings of the acceptance review of `a77c85a5` [rev D1, D2, D3].** Neither is a usability escape: every input
the review tried gave zero usable runs. Both break a guarantee of this design.

- **AR-B1. A malformed jobs list loses the inventory.** `JOBS_DECODER` admits floats
  (`a77c85a5:collect.py:213-214`), so a `total_count` of `1e400` decodes to `inf`. The `"%d"` at
  `a77c85a5:collect.py:145` raises `OverflowError`, which the `except (KeyError, TypeError, AttributeError)` at `:162`
  does not catch. S10 publishes an `internal` quarantine at stage S3, exit 1, with `files: []` and both
  `collection.inputs.runs_json` and `collection.inputs.jobs_list` null. The served files were never read, and the
  pinned runs.json, which was read correctly, is not recorded. That contradicts section 1 (such a jobs list is an
  `input` rejection with its digest), section 3's N2 note ("lists every served file"), "S5 always runs" and I-PUB.
  The cause is in the design: each input was read in the state that interprets it, and S10 can record only what had
  been read. The implementation's declared deviation (4) is the same mechanism inside S5: an unforeseen exception at
  one argument publishes a record without it and every later argument. D1 reorders the states so that every input
  is inventoried before any is interpreted (2.5, section 3); D2 refuses the input itself (2.3).
- **AR-B2. Five boundary mutants survive.** The host-failure boundary of 2.5 is implemented as designed, but no
  test notices if the decoded-scan or the parsed-readings catch is widened to `Exception` (the review's X1 and X2),
  if `lstat` records every `OSError` as `missing` (X6), if `open` records every `OSError` as `unreadable` (X7), or if
  a host failure while hashing a symbolic link's target is swallowed (X14). Each would publish a host failure as a
  file's rejection. `[TB-SCANX]` injects only into the byte scan and `os.read`, and mutant L18 widens all three
  catches at once. D3 adds one named test and one independent old-behaviour mutant for each (section 6).

**The review's six non-blocking notes [rev D1, D2, D3].**
- **AR-N1, the `RUN` line's `outcome` printed raw.** Closed. A3(b) already required it escaped (section 3).
  `[TB-OUTC]` tests it, and `[TB-EMIT]` tests the backstop on its own, so the review's X9 is now killed (L32, L33).
- **AR-N2, `Infinity` in `collected.json`.** Closed by D2, which refuses every float in the jobs list, and by strict
  serialization (section 5), `[TB-NANOUT]` and L31.
- **AR-N3, unbounded reason length.** Closed for the review's case: a jobs-list `id` is a validated integer before
  any message names it, and the schema's problems carry no input text (2.3). Carried for the other reasons that
  quote input-derived text (`duplicate key <names>`, `key set <keys>`): their length is bounded only by the file cap.
  They stay one JSON-escaped line, so this is not an injection or a fail-open path.
- **AR-N4, a 3,000-deep result block.** Carried, unchanged. It gives `internal` at S8, not `failed_files`; that
  fails closed, and every file is recorded and judged by then (R10 of the design review stays not adopted).
- **AR-N5, `--self-test` with collection arguments exits 0 and publishes nothing.** Carried, unchanged. The
  self-test is a separate mode, and reader check 2 still requires a `COLLECT PUBLISHED` line. A regression test
  for a refusal would, under its own reverting mutant, run the whole self-test recursively inside the self-test.
- **AR-N6, low disk on the host.** Carried, as an environmental condition. The new tests write only small files
  (`[TB-CAP]`'s sparse file is unchanged), the snapshots of S2b are held in memory, not on disk, and the two-worker
  mutant phase holds two copies of `batchx/` at a time, under 1 MB. A disk or timeout failure is reported as
  infrastructure.

**The closure property the design must deliver.** `collected.json` at the published location says HOLDS only if
all of the following hold:

1. `runs.json` is the pinned file.
2. The jobs list parsed strictly and gave a one-to-one index of the 32 shard jobs. Every job of the list is of one
   run, at `--head`, on the launch branch, of this workflow.
3. Every served argument is a regular file that passed the strict grammar of section 2.
4. Every accepted answer's job id is an index job.
5. Every index job has at least one accepted answer, and all its answers have one identity.
6. That answer passed every `read_shard` check, including the strict parse of each of its blocks.
7. Neither the bytes nor the decoded text of any accepted answer names a shard other than its own job's.
8. All 223 runs are eligible, each from exactly one shard.
9. Nothing else failed.

Under the strict grammar, the identity `(job_id, logs_content, original_length)` covers every byte of an accepted
file that carries content. The only other bytes are JSON structure (punctuation, whitespace, escape spellings that
decode to the same text) and the fixed `message` constant. So no byte of any served file reaches a HOLDS collection
without being validated and reconciled. H1 broke exactly this property.

**The inventory property [rev D1].** The closure property is about HOLDS. This one holds for every published record,
whatever its verdict, and AR-B1 broke it:

1. A `collected.json` is written only after the inventory (S2b, section 3) has reached its checkpoint, INVENTORY
   COMPLETE: every input of the invocation has been read with the bounded, safe read of 2.5 and has its entry.
2. Every published record lists that whole inventory: exactly one `files` entry per `--served` argument, in argument
   order, each with its name, kind, size and sha256; and, when `main` ran, a non-null
   `collection.inputs.runs_json` and `collection.inputs.jobs_list` with the same four facts. A digest and a size are
   null only for a file whose bytes could not be obtained: a missing path, a non-regular file, a file whose own
   access is refused, or a symbolic link whose target could not be hashed.
3. An invocation that cannot reach the checkpoint publishes nothing: ABORTED, exit 4. No record ever presents a
   partial inventory as complete.

## 1. Inputs and trust levels

| Input | Who produces it | Trusted | Untrusted | Gate |
|---|---|---|---|---|
| `batchx/runs.json` | reviewed, committed | its content, once its bytes equal the pin `RUNS_SHA256` (`collect.py:79`) | anything not equal to the pin | read and hashed in the inventory (S2b) before anything is parsed; sha256 against the pin, then the strict loader (S3) [rev D1] |
| `batchx/crosscheck.json` | reviewed, committed | — | — | not read by the collector. `assemble.py` reads it in CI under its own pin, and it never decides a verdict (DESIGN §7) |
| jobs list (`--run-jobs`) | GitHub jobs API via `gh api`, saved by the operator | the API's values: job ids, names, run id, head, branch, workflow. The design assumes the file is the API's answer. It does not authenticate it | the file's bytes: integrity, encoding, duplicates, shape, and the type and range of every value the collector reads [rev D2] | read and hashed in the inventory (S2b); then the strict loader, which refuses every fraction, exponent and constant, and the integer schema (2.3), before `build_job_index` reads any value (S4) [rev D1, D2] |
| `--head` | the operator | — | the value | 40 lower-case hex digits (`collect.py:112`), and equal to every job's `head_sha` |
| served files (`--served`) | the job-log tool's answer, saved verbatim by the harness or by `from_transcript.py` | the tool's `job_id` and `original_length`, *as values*, once the file passes the strict grammar | everything else: the bytes, the encoding, the shape, the log text | path checks and hashing in the inventory (S2b); then strict grammar, raw and decoded scans, the job rule, `read_shard` [rev D1] |
| host metadata (`fetch-record.json`, run and jobs records) | `host.py` in CI | pinned code under a pinned workflow | — | never seen by the collector. It reaches the session only through what `assemble.py` prints into the shard log |
| shard outputs (the assembler's lines inside `logs_content`) | `assemble.py` in CI | nothing by itself. The SHA256 lines detect corruption, not authorship, because they travel in the same log | the whole text | `read_shard` (`collect.py:213-332`), against the pins and `runs.json` |
| the output location (`--out`) and its parent directory | the operator's filesystem | — | any pre-existing state | must not exist (section 4) |
| the collector's own code | the session's checkout | recorded, not trusted: `collector_identity` (`collect.py:339-357`) | — | — |

**Served files: every malformation and where it is stopped.** Each line names the state of section 3 that stops
it. Every case is rejected and quarantines the collection unless the line says otherwise. [rev D1] The path and
size conditions are found in the inventory (S2b), which records them and goes on to the next argument; S5 then
takes them as that file's rejection. Every other line is found in S5, on the bytes the inventory read.

- **Not a regular file (S2b).** A directory (review E12), a missing path (E13), a FIFO or a device: rejected
  without reading. A symbolic link: rejected and never parsed. The regular file it points to is hashed for the
  record only. A path that names nothing is rejected as `missing`: `lstat` gives `ENOENT`, or, for a mistyped
  or mangled path, `ENOTDIR` (a component is not a directory) or `ENAMETOOLONG`. A file whose own access is refused
  (`EACCES`, `EPERM`) is rejected as `unreadable`. Any other `OSError` while reading is a host failure, which gives
  ABORTED (2.5, the boundary).
- **Too large (S2b).** Over `MAX_SERVED_BYTES = 16 MiB`. The largest saved answer seen is 812 KB. The file is
  hashed by streaming and never parsed.
- **Encoding (S5).**
  - Bytes that are not valid UTF-8 (G1d).
  - UTF-16 or UTF-32 (E1, E2).
  - A UTF-8 byte-order mark before the object (E7).
  - A JSON escape that decodes to a lone surrogate (`\ud800`). Python accepts it, and it fails later in
    `body.encode` with a traceback.

  A U+FEFF that is the first character of `logs_content` is the real format and is accepted (section 2.1).
- **Not one object (S5).**
  - An empty file (E3).
  - Whitespace only (E9).
  - `null` (E10).
  - An array (E11).
  - Leading whitespace.
  - Two concatenated objects (E8).
  - A trailing payload or a trailing newline after the closing brace.
  - Nesting deep enough to raise `RecursionError`, which escapes `parse_served` now with a traceback.
- **Duplicate keys at any depth (S5).** D1, D1b, D1c, D2, D3, D4, D5 and D5r, plus a duplicate inside a nested
  value. Keys are compared after unescaping, so `"job\u005fid"` duplicates `"job_id"`.
- **Unknown keys (S5).** X1, X2, a tool envelope (G1c), `Message` (wrong case), and the tool's other answer shape,
  a run's failed-jobs listing (`failed_jobs`, `logs`, `message`, `return_format`, `run_id`, `total_jobs`).
- **Wrong types or ranges (S5).**
  - A `job_id` that is a float, an exponent form, a bool, a string, negative, zero, or more than 16 digits long
    (T1). The grammar refuses huge integers before `int()` runs.
  - An `original_length` that is a float, negative or more than 16 digits long (T2).
  - A `logs_content` that is not a string (T3).
  - A `message` that is not the success string (X3).
- **A file on which a scan raises a conversion error (S5).** The scans (`raw_named`, unchanged, and the parsed
  readings `shard_of` and `shards_named`) convert the digits they find after a `"job_id"` key or a shard name with
  `int()`. Python refuses more than 4,300 digits there and raises `ValueError`. So a 5,000-digit `job_id` or shard
  number raises in the byte scan, which runs before the grammar. That `ValueError`, on one file, rejects that file
  (the per-file catch of 2.5), and the intake goes on to the next argument. A 5,000-digit `job_id` is therefore
  reported as `byte scan failed (ValueError)`, not as the grammar's `integer out of range`; its outcome is the
  same: rejected, recorded, and the collection quarantined.
- **Non-standard constants (S5).** `NaN`, `Infinity` and `-Infinity`.
- **The same file served twice (S5).**
  - The same path twice (C2), or a hard link: accepted. Both arguments are recorded, and the second is marked as
    the same file.
  - Byte-identical copies under two names (C1): accepted and taken once.
  - Byte-distinct copies with one identity (C3, indented; C4s, with and without the success `message`): accepted.
    C4s is not the review's C4, whose second copy carries the `message` `"m"` and is therefore rejected.
    Every copy's digest is recorded (N3, section 5).
  - Two different files with the same basename in two directories: rejected, because the record names files by
    basename.
- **Raw control characters inside a string (S5).** Rejected by the decoder's `strict=True`. The real format writes
  them as escapes.
- **Content that parses but contradicts (S6-S9, existing rules, unchanged).** A foreign job, a job under two shards,
  copies that differ, a bannerless copy, a log naming another shard (now also in decoded form: E-esc), and every
  `read_shard` check (`collect.py:213-332`). A non-standard constant or a duplicate key inside a result block (B1)
  becomes a validation failure.

**The jobs list: every malformation.**

- Non-UTF-8, a byte-order mark, non-standard constants, or duplicate keys at any depth (J1). Rejected.
- Not an object, `jobs` not a list, or a missing field. Rejected, as now (`collect.py:132-133`).
- `total_count` different from the number of jobs, or jobs of several runs. Rejected (`:116-120`).
- A job at another head, branch or workflow. Rejected (`:121-123`).
- No job, or two jobs, named `Extract shard K`, or an id that is not an int. Rejected (`:125-130`).
- **New:** the 32 shard job ids must be distinct (J1).
- **Numbers that are not bounded integers [rev D2].** Each is rejected at S4, as an `input` quarantine carrying the
  jobs list's digest, in a record that holds the full inventory. None reaches a format, a lookup, a comparison or
  arithmetic.
  - Refused by `JOBS_DECODER` itself, anywhere in the file: a fraction or an exponent (`1e400`, `-1e400`, `1.0`,
    `33.0`, `3.3e1`), so no jobs-list number ever becomes a float or `inf`; `NaN`, `Infinity` and `-Infinity`; an
    integer of more than 20 digits.
  - Refused by the integer schema of 2.3, before `build_job_index` reads any value: a `total_count` that is a bool, a
    string, null, negative or over 1,000; a `jobs` that is not a list of at most 1,000 objects; a job whose `id` or
    `run_id` is absent, a bool, a string, null, an array or an object, below 1, or more than 16 digits long; a job
    whose `name`, `head_sha`, `head_branch` or `workflow_name` is absent or not a string.

Unknown fields are allowed here, because the API object carries many. Whitespace around the value is allowed,
because the file is written by `gh api`, not by the job-log tool. All 388 jobs lists saved in the session's work
area (`cier-work/api-jobs/*.json`) parse under this loader, each with distinct ids. [rev D2] They also pass the
integer schema of 2.3, measured in scratch for this revision. The 388 lists hold 5,933 jobs, and every job has the
same 23 keys, with `name`, `head_sha`, `head_branch` and `workflow_name` strings. No list contains a fraction, an
exponent, a constant, a bool or a negative number. The longest integer has 12 digits, the largest `total_count` is
37, and the only nulls are the runner fields of 38 jobs, which the collector does not read. Each list is compact, in
the API's key order, with no trailing newline.

**runs.json.** Its bytes are pinned before parsing, so no malformation reaches the parser. It parses under the
strict loader as it stands (checked: no duplicate keys, no constants), and the loader is applied to it anyway.

## 2. Strict parse specification

### 2.1 The real tool format (measured)

**The evidence.**
- The session's saved `get_job_logs` results: 371 single-job answers and one answer of the tool's failed-jobs mode.
- The eight `cier-work/tr-*.json` answers the review checked (REVIEW-09d439d0 §4, H1). These are the tool's text
  as `from_transcript.py` writes it: the text verbatim, with no trailing newline.

Together these are 379 single-job answer files. Some answers were saved twice, so they hold 360 distinct byte
contents. The 8 `cier-work` answers are not among the 371.

**What every one of the 379 single-job answers shows:**
- **Key set.** Exactly `{job_id, logs_content, message, original_length}`.
- **`message`.** Exactly `Job logs content retrieved successfully`. This is the success string
  `SUCCESS_MESSAGE`. The failed-jobs answer carries `Retrieved logs for 12 failed jobs` and other keys.
- **Layout.** It matches this byte pattern:

  ```
  \A\{"job_id":(0|[1-9][0-9]*),"logs_content":"(?:[^"\\\x00-\x1f]|\\.)*",
     "message":"Job logs content retrieved successfully","original_length":(0|[1-9][0-9]*)\}\Z
  ```

  The pattern is one line; it is broken here for width. So the answer is compact, with sorted keys, no BOM, and
  no leading or trailing byte.
- **Canonical form.** The bytes equal `json.dumps(obj, ensure_ascii=False, separators=(",", ":"),
  sort_keys=True)`, with `<`, `>`, `&`, U+2028 and U+2029 written as `\u003c`, `\u003e`, `\u0026`, `\u2028` and
  `\u2029`. This holds for 379 of 379 answers. The pattern is consistent with Go's `encoding/json` defaults; that
  is an inference about the server, and nothing below depends on it. No answer contained U+2028, U+2029, `\b` or
  `\f`, so those parts of the canonical form are unexercised.
- **Content of `logs_content`.** Non-ASCII characters are written raw in UTF-8. ANSI codes appear as `\u001b`. No
  answer contains `\r`. No answer ends in `\n`.
- **Whole answers and tails.** 110 of the 379 answers are whole (108 saved results and 2 `cier-work` answers):
  `len(logs_content.split("\n")) == original_length`. All 110 begin with U+FEFF, the log's byte-order mark, written
  raw inside the string. The 269 tails have fewer lines than `original_length`, and none begins with U+FEFF. Every
  `job_id` has 12 digits.

### 2.2 Served files: the accepted grammar

A served file is accepted exactly when all of the following hold, checked in this order on the one byte string read
from it:

1. It is a regular file, of at most `MAX_SERVED_BYTES`.
2. Its first bytes are not `EF BB BF`.
3. It decodes as UTF-8, strictly.
4. Its first character is `{`.
5. One call, `DECODER.raw_decode(text, 0)`, returns `(obj, end)` with `end == len(text)`. `DECODER` is
   `json.JSONDecoder(strict=True, object_pairs_hook=…, parse_constant=…, parse_float=…, parse_int=…)` with these
   hooks:
   - **`object_pairs_hook`** raises on any key that occurs twice in one object. It names the duplicated keys,
     sorted. Python calls it for every object, nested ones included, as each one closes, so the check covers every
     depth and runs before any type check.
   - **`parse_constant`** always raises, so `NaN`, `Infinity` and `-Infinity` are refused.
   - **`parse_float`** always raises. A number with a fraction or exponent is refused, so `77001.0` and `7e4` are
     not integers.
   - **`parse_int`** accepts only `0|[1-9][0-9]{0,15}`. Negative numbers, `-0` and values of 10^16 or more are
     refused before `int()` runs.
   - **`ValueError` and `RecursionError`** are both caught as a rejection.
6. `obj` is a dict whose key set is `{job_id, logs_content, original_length}` or that set plus `message`.
7. Types:
   - `type(job_id) is int` and `job_id >= 1`;
   - `type(original_length) is int` (bool is refused by `type(...) is int`; the parse hook already refuses
     negatives);
   - `type(logs_content) is str`;
   - if present, `message == SUCCESS_MESSAGE`, compared exactly after decoding.
8. `logs_content.encode("utf-8")` succeeds, so there is no lone surrogate.

**What a rejection records.** Each rejection carries one reason, from the first check that fires.
- Checks 1 to 4 run first, in that order. Check 1 runs when the file is read (2.5, step 1); checks 2 to 4 follow
  the byte scan (2.5, step 3). A file on which the byte scan raises `ValueError` is rejected with `byte scan failed
  (ValueError)`, and check 2 and everything after it are not reached.
- During step 5 the hooks fire in byte-reading order: the number and constant hooks fire as the scanner reaches each
  token, and `object_pairs_hook` fires as each object closes. So a duplicate key followed later in the same object by
  `NaN` gives `non-standard constant NaN`, not `duplicate key`.
- `data after the object` comes next, then rules 6 to 8 in order.

A file with several faults therefore has a reason that depends on where the faults sit. Every fixture whose reason a
test asserts has exactly one fault (section 6). The reasons:

- `not a regular file (<kind>)`
- `over the size cap`
- `byte-order mark before the object`
- `not UTF-8`
- `does not begin with '{'`
- `not JSON: <decoder message>`
- `duplicate key <names>`
- `non-standard constant <c>`
- `non-integer number`
- `integer out of range`
- `nested too deeply`
- `data after the object`
- `key set <sorted keys>`
- `<field> has the wrong type`
- `message is not the tool's success message`
- `lone surrogate in logs_content`
- `byte scan failed (<class>)`, `decoded scan failed (<class>)` and `parsed scan failed (<class>)`: that scan
  raised `ValueError` or one of its subclasses, `<class>` being the raising class's name (the per-file catch of 2.5).
  No other exception gives a reason here.

**What the grammar does not require.** Canonical bytes, compactness, key order and the presence of `message` are not
required. The fixtures and the review's clean controls (P0 with Python's default separators, C3 indented, a fixture
without `message`) must keep holding. Section 9, item D2, puts the stronger canonical-bytes rule to the reviewer.

**Checked in scratch** (not in the repository): this grammar accepts all 379 real answers and the fixtures P0, P0m
and C3. It rejects the failed-jobs answer, each of D1, D1b, D4, D5, X2 and X3, a duplicate key at depth 2, an
escaped duplicate key, `NaN`, the float and exponent forms, a bool, a negative id, 17- and 5,000-digit ids, the BOM,
UTF-16, a 0xff byte, a lone surrogate, concatenation, a trailing newline, leading space, an empty file, `null`, `[]`,
100,000-deep nesting and a raw control character. Each rejection gives the reason listed above.

### 2.3 The jobs list, runs.json and result blocks

There are three decoder objects, and each mutant in section 6 names the one it changes.

- `SERVED_DECODER` is the decoder of 2.2.
- `JOBS_DECODER` reads the jobs list and runs.json.
- `BLOCK_DECODER` reads result blocks.

The last two share `object_pairs_hook` and `parse_constant` with `SERVED_DECODER`, but each is its own object. All
three hooks raise exceptions that subclass `ValueError`, so the existing `except` tuple at `collect.py:291` also
catches them.

- **The jobs list, through `JOBS_DECODER` [rev D2].**
  - Steps 1 to 3 of 2.2 apply, to the bytes the inventory read (S2b).
  - The value is read with `raw_decode`, and the rest must be JSON whitespace.
  - `parse_int` accepts `-?(0|[1-9][0-9]{0,19})`, as before.
  - `parse_float` always raises, with the reason `non-integer number`, exactly as in `SERVED_DECODER`. A number with
    a fraction or an exponent is refused wherever it stands in the file, so `1e400` is refused as text and never
    becomes `inf`. At `a77c85a5`, floats were allowed (`a77c85a5:collect.py:213-214`), which is how AR-B1's `1e400`
    reached the `"%d"` at `:145`.
  - Unknown keys are allowed. Before `build_job_index` reads any value, the integer schema below checks every field
    it reads. The 32 shard job ids must be distinct.
- **runs.json, through `JOBS_DECODER`.** The pin is checked first. [rev D2] runs.json contains no fraction and no
  exponent (checked for this revision), so refusing floats changes nothing for the pinned file.

**The jobs-list integer schema [rev D2].** `jobs_schema(value)` runs on the decoded jobs list in S4. It runs before
`build_job_index` reads any value, so before any `"%d"` or other interpolation, any set or dict lookup, any comparison
and any arithmetic on a jobs-list value. It runs whether or not runs.json loaded, because it needs no run set. The
rules are checked in the order J-1 to J-5. J-4 checks every job, in list order, before J-5 checks any, and within a
job the fields are checked in the order given. The first check that fails gives the one recorded problem, and
`build_job_index` does not run:

| Rule | Requirement | The problem recorded |
|---|---|---|
| J-1 | the value is an object with the keys `total_count` and `jobs` | `the jobs list is not an object with total_count and jobs` |
| J-2 | `type(total_count) is int` and `0 <= total_count <= 1000` (`MAX_JOBS`) | `total_count is not an integer from 0 to 1000` |
| J-3 | `type(jobs) is list`, `len(jobs) <= 1000`, and every element is an object | `jobs is not a list of at most 1000 objects` |
| J-4 | for each job, `id` and then `run_id`: present, `type(v) is int`, and `1 <= v <= 9999999999999999` (`MAX_ID`, 16 digits) | `job <n>: <field> is not an integer from 1 to 9999999999999999` |
| J-5 | for each job, `name`, `head_sha`, `head_branch` and `workflow_name`: present, and `type(v) is str` | `job <n>: <field> is not a string` |

- **Text in the problems.** `<n>` is the job's position in the list and `<field>` one of the six field names. Both
  come from the collector, never from the input, so every problem has a bounded length. This closes AR-N3 for its
  source: `build_job_index` echoed a job's `id` through `json.dumps(j.get("id"))` (`a77c85a5:collect.py:151`), and
  that `id` is now a validated integer.
- **Bools.** `type(v) is int` refuses `true` and `false`. A bool is an int subclass: as a key of the job index,
  `True` would equal job id 1.
- **Floats.** `JOBS_DECODER` already refuses every float. The schema's `type(v) is int` would refuse one again.
- **The bounds.**
  - `MAX_ID` is the range of a served `job_id` (2.2: at most 16 digits, at least 1), so every index id can be matched
    by an answer. Real ids have 11 or 12 digits.
  - `MAX_JOBS` is a sanity bound. This workflow's run has 33 jobs, and the largest saved list has 37. A run with more
    jobs is refused, never truncated.
  - A value outside a bound is refused, never clipped.
- **Fields the collector does not read** (`run_attempt`, `steps`, the runner fields and the rest) are not checked
  beyond the decoder. The decoder still refuses every fraction, exponent and constant in them.

After the schema, `build_job_index` runs as now when `doc` exists: the `--head` check, `total_count == len(jobs)`,
one run, every job at the head on the branch of this workflow, one job named `Extract shard K` per shard, and
distinct ids. Every value it reads is then a validated integer or string, so its `"%d"` formats, its set of run ids
and the job index's keys are safe. The `run_id` it returns, which becomes `collected.json`'s `extraction_run`, is a
validated integer too (AR-N2).

**What is not the fix.** Catching `OverflowError` after an unsafe format is not the fix. `build_job_index`'s
`except (KeyError, TypeError, AttributeError)` (`a77c85a5:collect.py:162`) stays as it is, and no class is added to
it: not `OverflowError`, not `ValueError`, not `Exception`. After the schema, no input can reach that clause.
Mutant L29 is the label fix, and `[TB-INVJ]` and `[TB-JNUM]` must kill it.
- **Result blocks** (`collect.py:282-292`), through `BLOCK_DECODER`.
  - `json.loads(body)` is replaced by `BLOCK_DECODER`. Duplicates at every depth and non-standard constants are
    refused.
  - Numbers keep Python's default parsing, because real blocks carry floats (`extract_result.py` writes
    `'seconds': float(...)`). An integer over Python's digit limit raises `ValueError`, which is a rejection.
  - The canonical round-trip `body == json.dumps(r, indent=1, sort_keys=True) + "\n"` stays.
  - `expected` must be a dict whose `outcome` is a string. This makes review cases K1 and K2 validation failures
    recorded in `failed_files`, not the `TypeError` at `collect.py:508`.

### 2.4 `original_length` and `logs_content`

`original_length` is the line count of the log as the server holds it. It can be derived from `logs_content` only
for a whole answer. A tail does not determine it. For a whole answer the measured relation is exact:
`original_length == logs_content.count("\n") + 1`, and `logs_content` does not end in `"\n"`.

The collector requires that relation. It drops the tolerance at `collect.py:219-220`, which pops one trailing empty
line and so accepts two spellings of one log. No observed answer and no fixture ends in `"\n"`. The tail and
length checks themselves are unchanged (`collect.py:221-224`).

Requiring a leading U+FEFF on a whole answer is not part of this design (section 9, item D3).

### 2.5 Order of operations, and why it matters

**Two phases, split at one checkpoint [rev D1].** At `a77c85a5` each input was read in the state that interprets it:
runs.json in S3, the jobs list in S4, and each served argument in S5, just before its scans. Under this revision,
steps 1 and 2 below run for every input before step 3 runs for any.

- **The inventory (S2b): steps 1 and 2, for every input.** The order is `--runs`, then `--run-jobs` (both only when
  `main` runs), then every `--served` argument in argument order. Nothing in this phase decodes, scans, parses or
  compares content. The one derived fact is runs.json's `pinned`, a comparison of its digest with `RUNS_SHA256`. Each
  input gets its entry (section 3, S2b), and an input that is a file-specific condition is recorded with its kind
  and reason; the inventory then goes on to the next input. The phase ends at the checkpoint **INVENTORY COMPLETE**,
  when every input has its entry.
- **The interpretation (S3-S5): steps 3 to 5, and every other reading of content.** It runs on the bytes the
  inventory read, never on a second read. S3 and S4 interpret runs.json and the jobs list. S5 takes each served
  argument through steps 3 to 5.

**The snapshots.** They stay in memory from S2b until S5 has finished with them. Each regular file within the cap is
still read exactly once, but all of a collection's inputs are now held at the same time. Their total is bounded by
the number of inputs times `MAX_SERVED_BYTES`; real answers are under 1 MB each. A `MemoryError` while snapshotting
is a host failure under the boundary below: ABORTED, and nothing is published.

For each input in S2b, and then for each served argument in S5, in argument order:

1. (S2b) `lstat`, open with `O_RDONLY | O_NOFOLLOW | O_NONBLOCK`, and `fstat`. The file must be regular and within the
   cap. It is then read once into memory. All later steps use that one buffer, so the file cannot change between
   hashing and parsing.
2. (S2b) sha256 and size. Every file that can be read is traceable even if every later step rejects it.
3. (S5) The raw byte scan (`raw_named`, unchanged), when the run set and index are known. A rejected file still
   records the shards it names. The scan only adds shards a file is involved with, so it can never make a run usable.
4. (S5) The strict grammar (2.2). No semantic function (`shard_of`, `shards_named`, `identity`, `read_shard`) ever
   sees an object that has not passed it. H1 was semantics applied to a last-wins object.
5. (S5) For accepted answers only: the decoded scan, `raw_named(obj["logs_content"].encode("utf-8"), …)`, joined
   with step 3. Under 2.2, `logs_content` is the only free text in an accepted file, so its decoded form is complete.
   This closes E-esc.

   The real format escapes only quotes, backslashes, control characters and `<`, `>`, `&`, never a letter or a
   digit. So on a genuine log the decoded scan finds the same names as the byte scan, **once the answer's own
   `"job_id":N` envelope is excluded**. The byte scan reads that envelope through `RAW_ID`, `RAW_LONG` and `RAW_JOB`,
   and the decoded scan of `logs_content` never sees it. The review measured this on the 379 real answers: 0
   differences with the envelope excluded, and 129 with it included, because there the envelope id is a bridge job of
   `runs.json`. controls.py's extended `[N1]` check compares the two scans on the same basis.

**The parsed readings run in the intake.** For an accepted answer, step 5 also computes `shard_of(obj)` and
`shards_named(obj, doc)`, the two readings the job rule uses (`collect.py:418-419` at `09d439d0`). They run inside
the per-file catch, like the two scans.

**The per-file catch.** Each of the three scan stages of one argument runs inside its own catch of `ValueError`,
and of nothing else:
- the byte scan (step 3);
- the decoded scan (step 5);
- the parsed readings `shard_of` and `shards_named` (step 5).

A `ValueError` raised by a scan is a fact about that file's content, not about the host or the collection. The
case it exists for: the unchanged `raw_named`, `shard_of` and `shards_named` call `int()` on the digits they find,
and Python raises `ValueError` beyond 4,300 digits. `ValueError` includes its subclasses: `UnicodeError`, raised
when a decoded `logs_content` cannot be encoded, and the decoders' own errors. No other class is caught.

- **What the file gets.** It is rejected, with the reason `byte scan failed (ValueError)`, `decoded scan failed
  (ValueError)` or `parsed scan failed (ValueError)`. The name is that of the raising class, which is `ValueError`
  or one of its subclasses. Its `files` entry keeps the name, kind, size and sha256 that steps 1 and 2 recorded.
  Its `names_shards` is null, meaning unknown, because a scan that raised found an unknown set; this holds even when
  the byte scan finished and only a later scan raised. It quarantines the collection like any other rejected file.
- **No fall-through.** A file whose byte scan raised never reaches the grammar. A file whose decoded scan or parsed
  reading raised is never taken as an answer. It never reaches the job rule, a copy, `read_shard` or a result.
- **What happens next.** The intake continues with the next argument, so S5 still judges every served argument.
  [rev D1] Every argument was already hashed and recorded in S2b.
- **What it does not cover.** Every exception other than `ValueError` propagates. The table below says where.

**The boundary, by stage and error kind.** Every condition met while one input file is taken in falls into exactly
one of three classes. It applies to the served files in S5 and, by the same rules, to runs.json in S3 and the jobs
list in S4. [rev D1] Steps 1 and 2 of all three now run in S2b, under the same classes.

| Class | Conditions | Stage | Outcome |
|---|---|---|---|
| **File-specific condition** (an attributed rejection, existing S5 rules) | the path names nothing (`lstat` gives `ENOENT`, `ENOTDIR` or `ENAMETOOLONG`; kind `missing`); it is a directory, a symbolic link, a FIFO, a device or another non-regular kind; it is over the cap; the file's own access is refused (`EACCES` or `EPERM` from `lstat`, `open` or `read`), or it became a link between `lstat` and `open` (`ELOOP`); every grammar rejection of 2.2 | step 1, in S2b (the kinds `missing`, `directory`, `symlink`, `other`, `unreadable`), and step 4, in S5 [rev D1] | the file is rejected with its kind and reason, recorded with what steps 1 and 2 established, and the collection is quarantined. The inventory, or the intake, continues [rev D1] |
| **Recoverable scan or conversion error** (the per-file catch above) | `ValueError`, with its subclasses, raised by the byte scan, the decoded scan or the parsed readings | steps 3 and 5 | the file is rejected with `byte scan failed`, `decoded scan failed` or `parsed scan failed`, and `names_shards` is null. The collection is quarantined, and the intake continues |
| **Host failure** (the infrastructure route) | `MemoryError`; any `OSError` that is not one of the file-specific errors above, for example `EIO`, `ENOSPC`, `ENOMEM`, `EMFILE` or `ENFILE`, at any step; an interrupt, or any `BaseException` that is not an `Exception` | any step of S2b, S3, S4 or S5, and any later state [rev D1] | ABORTED, exit 4. The stdout lines and the existing guarantees apply: no `COLLECT PUBLISHED` line, and `--out` not created by this invocation. The `COLLECT FILE` lines are printed before the `COLLECT ABORTED` line: one per served argument inventoried before the failure, when it comes in S2b, and one per served argument, when it comes later (section 3, "Safe names on stdout") [rev D1]. Nothing is published, so a host failure is never recorded as a file's rejection, never counted as an evidence failure, and never leaves a current HOLDS |

Any other exception, a bug for example (`TypeError`, `KeyError`, `RecursionError`), is neither a file's condition
nor a host failure. [rev D1] Where it is raised decides its outcome:
- **In S2b,** it leaves the inventory incomplete. The outcome is ABORTED, exit 4, as for a host failure. An
  incomplete inventory is never published, and no record claims to be complete when it is not.
- **In S3-S10,** after INVENTORY COMPLETE, it keeps the existing rule: S10's `internal` quarantine, published with
  exit 1 and zero usable runs, its record naming the stage and the exception type, not a file. The record holds the
  full inventory (section 3, S10).
- **In S11 or S12,** it is ABORTED, exit 4, as A1 confirmed. The writer that would publish the record is the one
  that failed. The owner's D1 ("may publish an explicitly quarantined `collected.json`") covers S3-S10; it does not
  ask the failed writer to publish.

**Declared deviation (4) of `a77c85a5`, resolved [rev D1].** At `a77c85a5`, a served argument's `files` entry was
made only when its whole intake had completed (`a77c85a5:collect.py:762-776`). An internal error at one argument in
S5 therefore published a record without that argument and every later one, and an internal error in S3 or S4
published a record with no entries at all (AR-B1). Under this revision every entry is made in S2b, and:
- an unforeseen exception inside the inventory loop is ABORTED (above), because the inventory is then incomplete;
- an unforeseen exception inside a later per-file step (the byte scan, the grammar, the decoded scan, the parsed
  readings, the same-name rule) is S10's `internal` quarantine. Its record lists every argument: those S5 had judged
  with their status and reason, and the rest with the status `unjudged` and their inventory facts (section 5);
- a host failure or an interrupt at either point is ABORTED, as before.

The deviation is withdrawn, and the per-file entries no longer depend on the intake completing.

The catch never makes anything usable: a file it rejects has failed, and its collection is quarantined. An
exception after S5 (for example a 5,000-digit `RUNS` count, which only `read_shard` converts, at S8) reaches S10's
`internal` quarantine, as `[TB-INT]` shows. Every file is already recorded by then.

Only after every argument has finished steps 1 to 5: the job rule, completeness, validation, reconciliation and the
verdict (`collect.py:425-520`). They are set-based, as now, so the result cannot depend on argument order or on
file names (`collect.py:401`; the `[RP]` tests).

## 3. Fail-closed state machine

**Terminal outcomes.**

| Exit | Outcome | What is at `--out` |
|---|---|---|
| 0 | PUBLISHED, verdict HOLDS | `collected.json`, and `ci/<run>/results.json` for each of the 223 runs |
| 1 | PUBLISHED, QUARANTINED, verdict FAILS | `collected.json` only; no `ci/` directory |
| 2 | PUBLISHED, QUARANTINED, verdict UNVERIFIED | `collected.json` only; no `ci/` directory |
| 3 | REFUSED. Nothing was read and nothing was written | not created by this invocation. If it exists it is untouched, and it is not a result of this invocation |
| 4 | ABORTED: an error of any kind, after S2 and before the rename in S12 completes, that the states below do not turn into a quarantine. [rev D1] That is: any failure in S2b other than a file's own condition, a bug included; a host failure or an interrupt in any later state; and any exception in S11 or S12 | not created by this invocation; it may hold another process's content (section 4). The staging directory may remain beside it, and is never a result |
| 5 | PUBLISHED, durability not confirmed: the rename completed, then the parent `fsync` or a later step failed or was interrupted | present and complete: this invocation's collection, of whatever verdict |

**What each code guarantees.**
- **0** means stdout carries a `COLLECT PUBLISHED` line followed by a final `COLLECT HOLDS` line. In collection
  mode no other path exits 0. The separate `--self-test` mode exits 0 when its tests pass.
- **1, 2 and 5** also follow a `COLLECT PUBLISHED` line.
- **3 and 4** print no `COLLECT PUBLISHED` line. A wrapper that sees one of them has no result from this
  invocation, whatever is at `--out`.

QUARANTINED is exactly `verdict != "HOLDS"`. `collected.json` gains `"quarantined": <bool>`, written in the same
place as the verdict. The verdict vocabulary and the meaning of exit codes 0 to 2 are unchanged, so the existing
tests keep their meaning.

**Every path gets a code (A1).**
- **Argument errors exit 3.** At `09d439d0`, `ap.error` exits 2 (`collect.py:1072-1073`), the code UNVERIFIED also
  uses. Now `ArgumentParser.error` is overridden to raise, and `main` returns 3.
- **No help exit.** The parser is built with `add_help=False`. Then `-h` and `--help` are unknown arguments and give
  3, never `parser.exit()` with 0. `--self-test` remains a separate mode with its own 0/1 result.
- **One catch from S0 on.** `main` catches `BaseException`, so `KeyboardInterrupt` and every non-`OSError`
  exception are included:
  - before S2: 3;
  - from S2 until the rename in S12 completes: 4. [rev D1] In S2b every exception that is not a file's own
    condition reaches 4, a bug included, because the inventory is then incomplete. A `ValueError` raised by a scan
    of one served file is first turned into that file's rejection by the per-file catch of 2.5. A host failure,
    that is a `MemoryError` or an `OSError` other than a file's own conditions (2.5, the boundary), reaches 4 from
    any state, S3-S10 included: nothing is published. Any other exception in S3-S10 is turned into an `internal`
    quarantine by S10, and the collection goes on to be published, with the full inventory [rev D1]. In S11 or S12 every exception reaches 4, an example being a
    `UnicodeEncodeError` from the ASCII result write. An interrupt always reaches 4;
  - after the rename: 5.
- **No uncaught exit.** An exception never leaves `main` uncaught, because Python's default exit code 1 would
  collide with the FAILS-and-published code.

**States.** Each state passes on success to the next. A failure is recorded as an entry and processing continues,
so that one record holds every failure. The table lists each failure edge and what it writes.

| State | Does | Failure edge | Written on that edge |
|---|---|---|---|
| S0 ARGS | parse argv with `add_help=False`; `--runs`, `--run-jobs`, `--head`, at least one `--served`, `--out` | → REFUSED (3) | stdout `COLLECT REFUSED <reason>; --out is not a result of this invocation`; no file anywhere |
| S1 TARGET | `out = abspath(--out)`; its parent exists and is a directory; `os.path.lexists(out)` is false | → REFUSED (3) | stdout `COLLECT REFUSED the output location exists (or: its parent is not a directory); --out is not a result of this invocation`; `--out` and its contents untouched |
| S2 STAGED | `nonce = os.urandom(16).hex()`; `os.mkdir(parent/".<name>.staging-<nonce>", 0o700)` | → ABORTED (4) | stdout `COLLECT ABORTED <exception type or errno name>`; nothing else |
| **S2b INVENTORY** [rev D1] | 2.5 steps 1-2 for every input, before any input is interpreted: `--runs`, then `--run-jobs` (through `main`), then every `--served` argument in argument order. Each input gets its entry. runs.json gets `collection.inputs.runs_json` `{name, kind, size, sha256, pinned}`, with `pinned` the digest's equality with the pin. The jobs list gets `collection.inputs.jobs_list` `{name, kind, size, sha256}`. A served argument gets `files[i]`, with `arg`, `name`, `kind`, `size`, `sha256` and `same_file_as`. Its `status` is `unjudged` and its `reason` null, or, for a file-specific condition, its `status` is `rejected` with that condition's reason. Ends at the checkpoint INVENTORY COMPLETE | a file's own condition (2.5, the boundary) → its entry records the kind and the reason, with `size` and `sha256` null where no bytes could be obtained, and the inventory continues. Anything else → ABORTED (4): a host failure, an interrupt, or any other exception, a bug included | for ABORTED: one `COLLECT FILE` line per served argument inventoried before the failure, then `COLLECT ABORTED <exception type or errno name>`; nothing at `--out` |
| S3 RUNS | [rev D1] from the snapshot S2b took: the file-specific condition S2b recorded, if any; the pin; the strict load | → quarantine `{kind: "input", input: "runs.json"}` with name, size, sha256 (or kind and no digest), `pinned`, reason; `doc = None` | carried into the record; S4 and S5 still run |
| S4 INDEX | [rev D1, D2] from the snapshot S2b took: the file-specific condition S2b recorded, if any; the strict load (no fraction, exponent or constant, 2.3); the integer schema of 2.3, whether or not `doc` exists; then, when `doc` exists, `build_job_index` with distinct ids, and the `--head` check | → quarantine `{kind: "input", input: "jobs list"}` with name, size, sha256, and every problem (the schema gives one); `index = None` | as S3 |
| S5 INTAKE | [rev D1] 2.5 steps 3-5 for **every** served argument, on its snapshot, whatever S3 and S4 gave, its scans inside the per-file catch of 2.5; scans need `doc` and `index`. An argument S2b rejected keeps that rejection. At its end, one `COLLECT FILE` line per argument on stdout (below) | → per file, including a scan that raised `ValueError`: `files[i].status = "rejected"`, and quarantine `{kind: "unattributable", file, sha256 or null, size, reason, names_shards}`; the intake continues with the next argument | as S3, and the `COLLECT FILE` lines |
| S6 ATTRIBUTED | runs only if `doc` and `index` exist: the job rule (`collect.py:425-458`), unchanged except that the decoded scan joins `named` | existing edges: a foreign job naming no shard → quarantine (`:432-437`); a foreign job naming shards → FAILS and voids (`:438-444`); several shards → FAILS and voids; copies differ, or a copy has no banner → voids | `voided_shards`, quarantine |
| S7 COMPLETE | each shard K = 1…N has an accepted answer of job `index[K]` (`collect.py:480-483`) | → quarantine `{kind: "missing", shard, job_id, expected}`, plus `expected[K].status = "missing"` | as S3 |
| S8 VALIDATED | `read_shard` on one copy of each surviving shard, with the strict blocks and the `expected.outcome` check | → `failed_files` `{file, sha256, sha256s, shard, problems}`; FAILS | as S3 |
| S9 RECONCILED | each run seen in exactly one shard; no run outside `runs.json` (`collect.py:501`, `:512-514`); all runs eligible | → FAILS (extra run) or UNVERIFIED (a run not eligible, a shard not collected) | `runs[*].reason` |
| S10 DECIDED | `v` as at `collect.py:519-520`; `quarantined = v != "HOLDS"`. An exception raised in S3-S10 that no check foresaw is caught here, except a host failure (`MemoryError`, or an `OSError` that is not a file's own condition), which is not caught and gives ABORTED (4). [rev D1] An interrupt is not caught either. The internal record keeps the whole inventory of S2b, which nothing in S3-S10 resets: `collection.inputs` and every `files` entry. The arguments S5 had judged keep their status and reason; the rest stay `unjudged`. If S5 had not yet printed the `COLLECT FILE` lines, S10 prints them. The handler's fallback, which rebuilds the run table, catches `Exception` less host failures: at `a77c85a5:collect.py:745` a `MemoryError` there would have been swallowed | an internal error → quarantine `{kind: "internal", stage, exception: <type name>}`, `v = "FAILS"` | as S3 |
| S11 WRITTEN | `write_collection` into the staging directory. The only usable-run rule stays at `collect.py:367`, character for character. Result files only under HOLDS, opened `"x"`; `collected.json` written last, with the manifest; flush and `fsync` each file and the directories when `durable` | any exception or interrupt → ABORTED (4) | stdout `COLLECT ABORTED <exception type or errno name>`; `--out` not created by this invocation; the staging directory is left in place |
| S12 PUBLISHED | `os.rename(staging, out)`, then `fsync` the parent when `durable` | the rename raises, or an interrupt arrives before it completes → ABORTED (4), as S11. The parent `fsync` fails, or anything later fails or is interrupted → PUBLISHED, durability not confirmed (5) | for 5: the `COLLECT PUBLISHED` line, with the nonce and digest, then `COLLECT NOT DURABLE <exception type or errno name>`, then `COLLECT <verdict>` |

After S12, stdout carries the existing `RUN` and `COLLECT n of m` lines, then `COLLECT PUBLISHED <out> nonce <nonce>
collected.json sha256 <hex>`. The last line is `COLLECT <verdict>`, as now.

**Safe names on stdout (A3).**
- **The file lines.** At the end of S5, the collector prints one line per served argument:
  `COLLECT FILE <json>`. The JSON is `json.dumps({arg, name, kind, size, sha256, status, reason},
  sort_keys=True, ensure_ascii=True, allow_nan=False)`, the fields of `files[i]` in section 5. An ABORTED run (4)
  publishes no record, so these lines are its trace of every file, read and judged.

  [rev D1] The lines are printed exactly once, and always before `COLLECT PUBLISHED` or `COLLECT ABORTED`, by
  whichever comes first:
  - the end of S5;
  - S10, for an internal error raised before the end of S5;
  - the ABORTED path, for a host failure or an interrupt after INVENTORY COMPLETE and before the end of S5.

  Each argument carries the status it has at that moment, `unjudged` if S5 had not judged it. An ABORTED in S2b
  prints one line per served argument inventoried before the failure. So whenever the inventory completed, an ABORTED
  run's trace names every served argument with its kind, size and sha256. Only an ABORTED inside the inventory traces
  fewer.
- **No injected lines.** The rule covers **every line the collector writes to stdout or stderr**, whatever its
  prefix. In each such line, every value that comes from an input is written with `json.dumps(...,
  ensure_ascii=True)`: a file name, a path, a reason built from either, a decoder message, the `--head` value as
  given. That includes:
  - the `COLLECT FAIL` lines (`collect.py:439-440`, `:453`, `:457`, `:470`, `:488`);
  - the `COLLECT PUBLISHED` path;
  - the `RUN` lines (`collect.py:524-526`). Under quarantine their reason joins the quarantined files' names
    (`collect.py:497-498`). For stdout, that reason is built from the JSON-escaped names.
  - [rev AR-N1] a usable run's `outcome` on its `RUN` line. It comes from a served result block, so it is written
    `esc(outcome)`. `a77c85a5:collect.py:956` printed it raw and relied on the backstop alone (acceptance review N1).

  [rev AR-N2] Every `json.dumps` that writes output passes `allow_nan=False`: `esc`, the `COLLECT FILE` lines and
  `collected.json` (section 5, "Strict serialization").

  **The backstop.** Every line goes out through one function, `emit`. It writes printable ASCII only: any character
  outside U+0020–U+007E that still reaches it is written as its JSON escape. So no character of any value can end a
  line, whether a line feed, a carriage return, a form feed, U+0085, U+2028 or U+2029. One output line is always
  exactly one `emit` call. Values in `collected.json` are unaffected, because `json.dump` already encodes them.

  A name can therefore never inject a line, and names are not restricted otherwise.

**Closing the review's notes.**
- **N1 (stale output).** S1 refuses any existing `--out` before any input is read:
  - O1 and O2: a directory holding a stale `ci/800/results.json`, or a stale HOLDS `collected.json`;
  - an empty directory;
  - a file, a symbolic link, or a dangling link.

  Nothing is ever written into an existing directory. Hence `os.makedirs(out, exist_ok=True)` at
  `collect.py:364` goes away.
- **N2 (failures that leave no record).** Each one now publishes a QUARANTINED `collected.json` (exit 1) that names
  the failing input by name, size and digest, and lists every served file:
  - `main`'s early exits at `collect.py:1076-1087`, reached through S3 and S4 (a runs.json other than the pinned
    file; a jobs list omitting a shard, malformed, or with repeated ids; a bad `--head`);
  - a jobs list that is not JSON or not UTF-8, which is a traceback at `09d439d0`;
  - a served directory or missing path, reached through S5 (E12, E13);
  - a null or non-object `expected`, reached through S8 (K1, K2);
  - an unforeseen exception, reached through S10;
  - [rev D1, D2] a jobs list with a fraction, an exponent or a constant, such as AR-B1's `total_count` of `1e400`,
    or one that breaks the integer schema of 2.3, reached through S4. At `a77c85a5` the `1e400` case reached S10
    with no inventory; under this revision it is an `input` rejection, and an unforeseen exception there would still
    publish the full inventory.

  Only the REFUSED and ABORTED outcomes publish nothing. REFUSED has read nothing. [rev D1] ABORTED is a failure of
  the writer, of the host, or of an inventory that could not complete. Whenever the inventory completed, its
  `COLLECT FILE` lines trace every served file; an ABORTED inside S2b traces the arguments inventoried before it.

**S5 always runs.** [rev D1] Every served argument is hashed in S2b, before S3 or S4 reads anything, and is
grammar-checked in S5 even when S3 or S4 failed. A scan's `ValueError` on one file rejects that file and does not
stop the intake (the per-file catch of 2.5). A collection refused early is therefore still traceable file by file.
A host failure ends S5 early: a `MemoryError`, an `OSError` that is not a file's own condition, or an interrupt. Each
gives ABORTED, exit 4, with nothing published. An unforeseen exception in S3-S5 also ends S5 early, and S10 then
publishes the full inventory, with the arguments S5 had not judged marked `unjudged`. Whether an argument is hashed
never depends on what S3, S4 or another argument gave.
With no index, `files[i].shard` is null and `expected[*].status` is `"undetermined"`. With no run set, `expected` is null and `runs` is `[]`.

## 4. Transactional publication

- **A fresh location, refused if it exists.** S1 requires `--out` not to exist, using `lexists`, so a dangling link
  also counts. The operator gives a new path for every collection, for example `out-<n>`. The collector never
  deletes or replaces anything. The rebuild alternative named in I-PUB is not taken, because it would mean
  replacing the old directory.
- **Staging.** S2 creates `.<basename>.staging-<nonce>` in `--out`'s parent directory. It is on the same
  filesystem, so the rename is atomic, and it is created with `os.mkdir`, which fails if the name exists. Every file
  of the collection is written there, in this order:
  1. the result files, only under HOLDS;
  2. `collected.json`, last.
- **One atomic rename.** `os.rename(staging, out)` is the commit point. On Linux, `rename(2)` with a directory as
  its source has three cases:
  - if the target does not exist, the rename succeeds;
  - if the target is an empty directory, it replaces it;
  - if the target is a non-empty directory, a file or a symbolic link, the rename fails (`ENOTEMPTY`, `EEXIST`,
    `ENOTDIR`).

  So suppose another process creates `--out` between S1 and S12. Then either the rename fails, the outcome is
  ABORTED and this invocation publishes nothing, or the rename replaces an empty directory. It never merges into
  existing content.

  In the failing case, the other process's content stays at `--out`. That content may be a stale HOLDS collection.
  The collector cannot remove it and does not report it as its own: exit 4, and no `COLLECT PUBLISHED` line. The
  reader check below rejects it, because its nonce was printed by no invocation the reader acts on.
- **No partial results on failure.** Under any verdict but HOLDS, no `ci/` directory is created, even in staging
  (S11). Under HOLDS, a failure while writing the result files means this invocation never creates `--out`
  (ABORTED).
- **Durability.** `fsync` runs only when `durable` is true. `main` passes true; the self-test passes false, except
  in the two tests that check it, `[TB-SYNC]` and `[TB-NDUR]` (section 6). This is the only difference between the self-test and production,
  and it decides nothing: visibility comes from the rename, not from `fsync`. It exists because each self-test run
  makes about 300 collections, and controls.py repeats the suite once per mutant.
- **Leftover staging directories.** An ABORTED run may leave `.<name>.staging-<nonce>` behind. It is never a result:
  readers read only `--out`, and the name marks it. The collector does not remove it, and the operator may.

**How a reader tells a current `collected.json` from a stale one.** The new top-level block `collection` records:

- `nonce`: 32 hex characters, fresh for each invocation;
- `started_utc` and `written_utc`;
- `out_name`: the basename of `--out`;
- `inputs`:
  - `runs_json`: `{name, kind, size, sha256, pinned}`, or null when `collect()` is called directly with a `doc` (A2);
  - `jobs_list`: `{name, kind, size, sha256}`, or null when `collect()` is called directly;
  - [rev D1] both are written in S2b, before either file is parsed, and nothing later resets them. `kind` is the
    inventory's kind (`regular`, `missing`, `unreadable`, …), and `size` and `sha256` are null only where the
    file's bytes could not be obtained. At `a77c85a5` they were set only once both files had been interpreted, which
    is why AR-B1's record has them null;
  - `head`: as given, cut to 100 characters;
- `manifest`: one `{path, size, sha256}` for every other file published in `--out`. It is `[]` unless the verdict
  is HOLDS.

The served files' digests are in `files` (section 5). The collector prints the nonce and `collected.json`'s own
sha256 on its `COLLECT PUBLISHED` line.

**The top-level `runs_sha256` (A2).** At `collect.py:376`, the top-level `runs_sha256` is written as the constant
`RUNS_SHA256` whatever `doc` was used. Under this design it records what was actually loaded:
- after `main` loads and pins the file, it is the sha256 of the runs.json bytes;
- in a direct `collect(doc, …)` call, which has no file, it is null.

So a record made from a synthetic run set, the self-test's 6-run `doc` for example, never carries the pin.

A reader, such as the archive's tranche step, accepts a collection as current only if all of these hold:

1. `--out` is a directory that it named itself for this collection.
2. `collected.json`'s `collection.nonce` and sha256 equal the values printed on the `COLLECT PUBLISHED` line of the
   invocation it is acting on, and that invocation exited 0.
3. The inputs are the ones it means to rely on, and the run set is the pinned one:
   - `collection.inputs` is complete: no field of it is null;
   - `collection.inputs.runs_json.sha256 == RUNS_SHA256` and `pinned == true`, and the top-level `runs_sha256`
     equals the same value;
   - `collection.inputs.jobs_list.sha256` and every `files[i].sha256` equal the sha256 of the files it means to
     rely on.

   A record whose `inputs.runs_json` or `inputs.jobs_list` is null comes from a direct call. It is never current.
4. The listing of `--out` is exactly `collected.json` plus the `manifest` paths, and each digest matches.
5. `verdict == "HOLDS"`, `quarantined == false`, `runs` has 223 entries, and every entry has `usable == true`.

**What each check catches.**
- A stale directory, including one left in place by a REFUSED invocation or created by another process during an
  ABORTED one, fails check 2, check 3, or both.
- A record from a synthetic run set fails check 3.
- A directory with a planted extra file fails check 4.

The procedure is mandatory before any result is used. DESIGN.md §8 says so (section 8). The design does not add a
`--verify` mode; mechanizing the procedure belongs to the archive's own tooling (section 7).

## 5. Traceability record

`collected.json` keeps every field it has now (`collect.py:376-391`), and adds `schema`, `quarantined`,
`collection`, `files` and `expected`. Two existing fields change meaning:
- `runs_sha256` records the digest of the runs.json bytes actually loaded, or null (section 4, A2);
- in a quarantined record, `runs[*]` loses two fields (the `runs[*]` bullet below).

- **`schema`.** The value is `"batchx-collected/2"`.
- **`files`.** One entry per `--served` argument, in argument order:

  ```
  {"arg": i, "name": <basename>, "kind": "regular"|"symlink"|"directory"|"missing"|"other"|"unreadable",
   "size": <int>|null, "sha256": <hex>|null, "status": "accepted"|"rejected"|"unjudged", "reason": <str>|null,
   "job_id": <int>|null, "shard": <int>|null, "names_shards": [<int>, ...]|null, "same_file_as": <arg>|null}
  ```

  - [rev D1] The entry is made in S2b. `arg`, `name`, `kind`, `size`, `sha256` and `same_file_as` are fixed there,
    and so are `status` and `reason` for a file-specific condition (`rejected`). For every other argument S2b sets
    `status` to `unjudged` and `reason` to null, and S5 replaces them with its judgement.
  - [rev D1] `unjudged` means inventoried but not judged. It appears only in a record whose `quarantine` holds an
    `internal` entry, for the arguments S5 had not reached, and in the `COLLECT FILE` lines of an ABORTED run. An
    `unjudged` file adds no `unattributable` entry, because the `internal` entry already quarantines the collection.
    It is never `accepted`, so no run can be usable through it. A HOLDS record has none.

  - The digest is of the raw bytes. That is the same value as `served_sha256` now, because a UTF-8 decode and
    re-encode is the identity.
  - For a regular file the digest is always present, even when the file is over the cap (streamed) or rejected.
  - For a symbolic link, the digest and size are those of the regular file it points to, read for the record
    only, if it is within the cap.
  - A directory, a missing path or another kind has `size` and `sha256` null, and its `kind` says why.
  - `names_shards` is the union of the raw and decoded scans. It is null, meaning unknown, when no scan could run
    (the file was not read, or there is no run set or index), and when any scan of the file raised (2.5): a null
    `names_shards` is never an empty set.
  - `same_file_as` marks an argument naming the same `(st_dev, st_ino)` as an earlier one.
  - Paths are not recorded, only basenames. `collected.json` may be committed to the public repository, and paths
    would leak local directories. Two different files with one basename are rejected (section 1), so basenames are
    unambiguous.
- **`expected`.** One entry per shard K of the run set:

  ```
  {"shard": K, "job_name": "Extract shard K", "job_id": <int>|null,
   "status": "present"|"missing"|"undetermined",
   "copies": [{"arg": i, "name": ..., "size": ..., "sha256": ...}, ...],
   "candidates": [<arg>, ...]}
  ```

  - `present` means at least one accepted answer of `index[K]`. `copies` lists **every** accepted copy, with all
    its distinct digests. This closes N3; at `collect.py:465` and `:476`, only the first copy's digest is kept.
  - `missing` means no accepted answer.
  - `candidates` lists the rejected files whose scans are known to name shard K. A non-empty list means something
    was served for K and rejected. An empty list means no rejected file is known to name K. That is not the same
    as "nothing was served for K": a rejected file whose `names_shards` is null names an unknown set of shards, so
    it appears in no `candidates` list, though it is in `files` and its rejection quarantines the collection. This
    is how a missing expected file is told apart from a rejected one, as far as the scans can tell.
  - `undetermined` means the index could not be built.
- **`shards[K]`** gains `sha256s`: every distinct digest among its copies.
- **`failed_files[*]`** gains `sha256s` for the same reason.
- **Strict serialization [rev AR-N2, D2].** `collected.json` is written with `json.dumps(record, indent=1,
  sort_keys=True, allow_nan=False)`. The `COLLECT FILE` lines and `esc` pass `allow_nan=False` too (section 3). So no
  published record and no output line contains `NaN`, `Infinity` or `-Infinity`. Under D2 no such value can come from
  an input: the served grammar, the jobs list and runs.json admit no float, and a result block's float must
  round-trip canonically (2.3). Only a direct `collect()` call given a non-finite value in its `doc` or `run_id` can
  produce one. Its `ValueError` is raised in S11, which is ABORTED (exit 4), and nothing is published. At
  `a77c85a5`, a jobs-list `run_id` of `1e400` put `"extraction_run": Infinity` into a published record (AR-N2).
- **`quarantine`** keeps its two kinds, `unattributable` and `missing`, and adds `input` (S3, S4) and `internal`
  (S10). Every entry names its file or input, its digest when one exists, and its reason. A quarantine entry of any
  kind sets `eligible = false` for every run, as now (`collect.py:496-498`). Under I-QUAR, `failed_files` and
  `voided_shards` also make the collection QUARANTINED. They keep per-run `eligible` as a diagnostic that licenses
  nothing, as now (section 9, item D1).
- **`runs[*]` in a quarantined record** (the review's D1 recommendation). At `collect.py:507-508`, an eligible run's
  entry gets `sha256` (the digest of its result block) and `outcome` (the block's `expected.outcome`). These are
  result content, not diagnostics.
  - When `quarantined` is true, every entry keeps the other fields it has now. That is `run_id`, `shard`,
    `expires`, `eligible`, `usable` (false), `verdict` and `reason`, plus `file`, `job_id` and `served_sha256` where
    they are set now. It has **no** `sha256` and **no** `outcome` key.
  - When the verdict is HOLDS, every entry carries both, as now.

  No existing test count depends on them, and the `RUN` line prints `outcome` only for a usable run
  (`collect.py:525`).

## 6. Test plan

**Harness rules, enforced for every collection the self-test makes.** The `case()` and `outcome_of()` helpers are
extended so that each rule is asserted, not only stated.

1. **Read from disk.** Each test reads `--out/collected.json` from disk (`collect.py:644` does this now). [rev AR-N2]
   It reads it with a strict decoder that refuses `NaN`, `Infinity`, `-Infinity` and duplicate keys at any depth, in
   place of `json.load`, so the strict read costs nothing extra.
2. **One verdict view.** `quarantined == (verdict != "HOLDS")`, and the count of usable runs is the number of
   runs under HOLDS and 0 otherwise.
3. **Exact listing.** The listing of `--out` is exactly `collected.json` plus the `manifest` paths, with matching
   digests. With no usable run there is no `ci/` directory at all.
4. **No staging left.** No `.out.staging-*` remains in the test's directory after a published outcome.
5. **Every file recorded.** Every served file the test wrote appears in `files` with the size and sha256 the
   test computed itself with `hashlib`, independently of the collector. [rev D1] `files` has exactly one entry per
   `--served` argument, and `files[i]["arg"] == i`. Through `main`, `collection.inputs.runs_json` and
   `collection.inputs.jobs_list` are non-null, and their `size` and `sha256` are those the test computes over the
   bytes it wrote. They are null only for an input the test made unreadable.
6. **The file lines match.** stdout carries exactly one `COLLECT FILE` line per argument, and each one parses as JSON
   equal to the matching fields of `files[i]` (A3).
7. **One-line output.** The harness captures stdout and stderr separately. Every line on stdout is printable ASCII
   (U+0020–U+007E), as `emit` guarantees. In collection mode the collector writes nothing to stderr: every
   message, the `COLLECT REFUSED` and `COLLECT ABORTED` lines included, goes to stdout through `emit`. So the
   harness asserts that stderr is empty (A3).

Tests that drive `main` run it in-process, with argv, stdout and stderr redirected; `main` returns a code and never calls
`sys.exit`. They read the result from disk the same way.

**Required tests.** Each test names the invariant it proves. Unless it says otherwise, each case yields zero usable
runs, no `ci/` directory, and its file recorded with its reason. The reason is asserted by its fixed prefix, so a
test also proves which rule fired. Every fixture whose reason is asserted has exactly one fault, because with
several faults the reason depends on their positions (2.2, A6).

**Existing exact-record tests whose expectations move.** `[I1]` asserts the whole quarantine dict, old reason string
included, and the new entries add `size` and specific reasons. Its expected dict is updated to the new record, and
so is `[I5]`'s if its dict changes. Both keep their names, so the existing mutants that name them still apply.

[rev D1] **`[TB-SCANX]`'s line expectation moves.** Its name and every other assertion stay. The byte-scan cases
(a), (b), (c) and (f) now fail in S5, after INVENTORY COMPLETE, so they print a `COLLECT FILE` line for each of the
four arguments. Arguments 0 to 2 are `accepted`, and argument 3 is `unjudged` with a null reason. The read cases (d)
and (e) now fail in S2b, so they print lines for arguments 0 to 2 only, each `unjudged`. In every case no line gives
argument 3 a reason. L18, L19 and L20 still fail it, for the same reasons as before.

*Strict grammar (I-PARSE)*

| Test | Case | Proves |
|---|---|---|
| `[TB-D5]` | D5: two `logs_content` keys (a contradicting S1, then genuine S1), as shard 1's only file; and D5r, with the keys in reverse order | duplicates are refused whatever their order; reason `duplicate key 'logs_content', 'original_length'`; `expected[1]` missing, with the file as a candidate |
| `[TB-D1]` | D1: `job_id` 99999 first, 77001 last; the review's D2: `job_id` 77003 (another indexed job) first, 77001 last; the review's D3: an earlier `logs_content` holding shard 3's log | no last-wins job id or log |
| `[TB-D1b]` | D1b: the foreign answer with a trailing `"job_id": 77001`, as shard 1's only file; and D1c, the same beside genuine S1 | the foreign-job rule cannot be bypassed by a duplicate |
| `[TB-D4]` | D4: an earlier `logs_content` naming no shard | shadowed content that names nothing is still refused |
| `[TB-X3]` | X3: genuine S1 with `message` holding a contradicting log. Also: the review's X1 (`message` holding shard 3's RUNSET line); the review's C4 (S1 twice, one copy with the `message` `"m"`); a `message` differing by one character, by case or by a trailing space; a non-string `message` | `message` is the constant or nothing |
| `[TB-DEEP2a]` | a served file whose `logs_content` value is an object with a duplicated key | reason `duplicate key 'a'`: the duplicate check in `SERVED_DECODER` fires before the type check |
| `[TB-DEEP2b]` | a jobs list with a duplicated `id` inside a job object, run through `main` and read back from `collected.json` on disk | `quarantine` kind `input`, with the jobs list's digest: `JOBS_DECODER` refuses duplicates at depth 2 (J1) |
| `[TB-DEEP2c]` | a result block with a duplicated key inside `run` and a matching SHA256 line | `failed_files`. This is defence in depth: the canonical round-trip already refuses such a block, so this test is not a must-fail of any block-loader duplicate mutant |
| `[TB-NL]` | a whole answer whose `logs_content` ends in `"\n"`, with `original_length` the count of non-empty lines | refused as not whole (2.4): one accepted text per log |
| `[TB-KEY]` | X2, `Message`, G1c, and the failed-jobs answer shape | unknown keys are refused |
| `[TB-TYPE]` | T1 (`job_id` float, `7e4`, bool, string, 0, negative, 17 digits), T2 (`original_length` float or negative), T3 (`logs_content` a list), null values. A 5,000-digit `job_id` belongs to `[TB-SCAN]`: the byte scan raises on it before the grammar sees it | types and ranges are enforced |
| `[TB-NAN]` | `NaN`, `Infinity` and `-Infinity` as `original_length`; and B1, `NaN` and `Infinity` inside a result block | constants are refused in served files and in blocks; B1 is closed |
| `[TB-BOM]` | E7, a BOM before `{` | the leading BOM is refused (its positive pair is `[TB-REAL]`) |
| `[TB-UTF8]` | G1d (a 0xff byte), E1 (UTF-16, UTF-16-LE, UTF-16-BE, UTF-32), E2 (shard 2's only answer in UTF-16), a lone surrogate escape | strict UTF-8, and no lone surrogates |
| `[TB-TRAIL]` | E8, `}x`, a trailing newline, a leading space | exactly one object; no trailing payload |
| `[TB-EMPTY]` | E3, E9, E10, E11 | an empty or non-object file is refused, with its digest |
| `[TB-NEST]` | 100,000-deep nesting | refused with a reason; no traceback |
| `[TB-CAP]` | a regular file one byte over the cap | refused; its streamed digest equals `hashlib` over the file |
| `[TB-SCAN]` | beside genuine S1, S2 and S3, one extra file on which a scan raises `ValueError`, in four runs: (a) a 5,000-digit `job_id`, on which the byte scan raises before the grammar; (b) an answer whose `logs_content` holds `BATCH SHARD`, a 5,000-digit shard number and a slash, on which the byte scan raises; (c) an accepted answer whose `logs_content` holds `"job_id": ` followed by 5,000 digits, each written as a JSON escape, on which only the decoded scan raises; (d) an accepted answer whose `logs_content` is `EXTRACT SHARD` followed by 5,000 digits and no slash, on which both scans pass and only the parsed reading `shards_named` raises | in each run, exit 1. **On disk**, read from `collected.json`: `verdict == "FAILS"`, `quarantined == true`, every `runs[*].usable` false, no `ci/` directory; all 4 files recorded in `files` with the size and sha256 the test computes; the extra file rejected with the reason `byte scan failed (ValueError)` for (a) and (b), `decoded scan failed (ValueError)` for (c) and `parsed scan failed (ValueError)` for (d), with `names_shards` null, and quarantined by name; no `internal` quarantine entry. **On stdout**, as in `[TB-INJ]`: no line other than the last equals `COLLECT HOLDS`, and the last is `COLLECT FAILS`; exactly one line starts with `COLLECT PUBLISHED`, and its nonce and digest are those of `collected.json` on disk; every line is printable ASCII. **stderr** is empty. So a 5,000-digit `job_id` is reported as a scan's conversion failure, never as `integer out of range`, with the same negative outcome and full accounting |
| `[TB-SCANX]` | the adversarial host-failure case at intake: beside genuine S1, S2 and S3, one extra well-formed answer, with a host failure injected while that file is taken in: (a) `MemoryError` and (b) `OSError(ENOSPC)` and (c) `OSError(EIO)` raised by `raw_named` when it scans that file; (d) `OSError(EIO)` and (e) `MemoryError` raised by the read of that file (`os.read`, step 1); (f) `KeyboardInterrupt` raised by `raw_named` | in every case: exit 4; `--out` absent, so no `collected.json`, no `ci/` and no HOLDS is published; no `COLLECT PUBLISHED` line; the last line `COLLECT ABORTED` with the exception type; no stdout line gives that file a reason (`byte scan failed`, `decoded scan failed`, `parsed scan failed` or `unreadable`); the `COLLECT FILE` lines of the files taken in before it are printed; stderr empty. A host failure is never counted as an evidence failure |
| `[TB-ESC]` | E-esc: genuine S3 with an indented `\u0042ATCH SHARD 1/3` trailer line, beside S1 and S2; and its plain-spelled control | both give FAILS, with shards 1 and 3 voided; the outcome no longer depends on JSON spelling |

*Paths and copies (I-PARSE, I-PUB)*

| Test | Case | Proves |
|---|---|---|
| `[TB-DIR]` | E12, a served directory | `kind: "directory"`, no digest, published QUARANTINED |
| `[TB-MISS]` | E13, a missing path; a path through a regular file (`served-0.json/x`, so `lstat` gives `ENOTDIR`); a path whose last component is longer than the filesystem allows (`ENAMETOOLONG`) | each one `kind: "missing"`, rejected as `not a regular file (missing)` and never a host failure: published QUARANTINED, exit 1; told apart from a missing *expected* answer |
| `[TB-LINK]` | a symbolic link to genuine S1, as shard 1's only file | refused; the target's digest is recorded |
| `[TB-FIFO]` | a FIFO | refused without blocking |
| `[TB-SAME]` | C2, the same path twice; and a hard link | HOLDS with 6 usable; both arguments recorded; `same_file_as` set |
| `[TB-NAME]` | two different files with one basename in two directories | QUARANTINED |
| `[TB-N3]` | C3 (compact and indented S1) and C4s (S1 with and without the success `message`) | HOLDS with 6 usable; `expected[1].copies`, `shards["1"].sha256s` and `files` list every name and every distinct digest |

*Early failures, traceability (I-QUAR, N2)*

| Test | Case | Proves |
|---|---|---|
| `[TB-RUNS]` | `main` with a runs.json other than the pinned file | published, exit 1; the runs.json digest recorded with `pinned: false`; every served file in `files` |
| `[TB-JOBS]` | `main` with the real runs.json and a jobs list omitting shard 32 (the review's probe); a jobs list that is not JSON; one that is not UTF-8; one with a BOM | published, exit 1; the jobs list recorded by digest; `expected[*].status` is `undetermined` |
| `[TB-JOBID]` | a jobs list giving one id to `Extract shard 1` and `Extract shard 2`, run through `main` and read back from `collected.json` on disk | J1 is closed |
| `[TB-SYNTH]` | a direct `collect(doc, …)` call with the 6-run `doc` | `collection.inputs.runs_json` and the top-level `runs_sha256` are null, never the pin (A2) |
| `[TB-HEAD]` | `--head` that is not 40 hex digits | published QUARANTINED |
| `[TB-ARGS]` | `--out` missing; no `--served`; `-h` and `--help` | exit 3; nothing created, staging included; no exit 0 without a published HOLDS (A1) |
| `[TB-K1]` / `[TB-K2]` / `[TB-K3]` | a canonical block whose `expected` is null; one where it is a string; one where `expected.outcome` is absent or not a string | each is a validation failure in `failed_files`, with the digest; no traceback |
| `[TB-INT]` | `read_shard` replaced, in the test, by a function that raises | `quarantine` kind `internal`; published, exit 1 |
| `[TB-CAND]` | shard 2 not served, against shard 2's only file rejected | `expected[2].status` is `missing` in both cases; `candidates` is empty in the first and names the file in the second |
| `[G1a]` (extended) | the existing case | also asserts the file's `names_shards`, computed by the test (review N4, R1) |

*Stale output and publication (I-PUB, N1)*

| Test | Case | Proves |
|---|---|---|
| `[TB-O1]` | O1: a FAILS collection into an existing `--out` holding a stale `ci/800/results.json` | exit 3; the stale file's bytes and mtime are unchanged; no `collected.json` is created; no staging directory remains |
| `[TB-O2]` | O2: the same with a stale HOLDS `collected.json` | the same; no traceback |
| `[TB-O3]` | `--out` an empty directory; a regular file; a symbolic link; a dangling link | exit 3, untouched |
| `[TB-O5]` | a HOLDS collection whose staging is complete, with `os.rename` made to raise | exit 4; `--out` absent, since no other process runs in the test; no `COLLECT PUBLISHED` line |
| `[TB-O6]` | a HOLDS collection with the third result-file write made to raise `ENOSPC` | exit 4; `--out` absent; no `collected.json` anywhere at `--out`; stdout's `COLLECT FILE` lines trace every served file by name, kind, size, sha256, status and reason (A3) |
| `[TB-O6x]` | the same with the write made to raise a non-`OSError` (`UnicodeEncodeError`), and with `KeyboardInterrupt` | exit 4 in both; no uncaught exception; `--out` absent (A1) |
| `[TB-NDUR]` | a HOLDS collection whose parent `fsync` after the rename is made to raise | exit 5; `--out` present and complete; the `COLLECT PUBLISHED` line, with the nonce and the digest of the file on disk, then `COLLECT NOT DURABLE` (A1) |
| `[TB-INJ]` | beside genuine S1, S2 and S3, one extra **rejected** file (content `not json`), run twice with two basenames: one with a line feed, `COLLECT HOLDS` and a line feed in the middle (as in the review's `probe_inj.py`), and one with a line feed, `COLLECT PUBLISHED x nonce y` and a line feed in the middle. The rejection quarantines the collection, so the quarantine reason reaches the `RUN` lines | exit 1, and the record is published. **On disk**, read from `--out/collected.json`: `verdict == "FAILS"`; `quarantined == true`; every `runs[*].usable` is false; no `ci/` directory exists under `--out`; and the fixture's `files[i]` has `status: "rejected"`, with `name` equal to the embedded-newline basename the test wrote. **On stdout:** no line other than the last equals `COLLECT HOLDS`, and the last is `COLLECT FAILS`; exactly one line starts with `COLLECT PUBLISHED`; its nonce equals `collection.nonce`, and its `collected.json` sha256 equals the sha256 the test computes over the file on disk, as in `[TB-NDUR]`; every line is printable ASCII; and each line that names the file carries its name JSON-escaped, the `RUN` lines included. **stderr** is empty (harness rule 7) (A3) |
| `[TB-O7]` | a QUARANTINED collection | the listing of `--out` is exactly `["collected.json"]` |
| `[TB-O8]` | two collections of the same inputs into two fresh locations | distinct nonces; `collection.inputs` and `files` equal the on-disk digests; `manifest` equals the listing |
| `[TB-SYNC]` | `durable=True`, with `os.fsync` counted | each published file, the staging directory and the parent are synced |

*Positive controls (non-vacuity)*

| Test | Case | Proves |
|---|---|---|
| `[I3]` | the existing control, and every existing clean case: whole shards in either order, C1, C2, 4,999 lines, the `[RP]` clean scenario | each still HOLDS with exactly 6 usable and `ci/800…805` byte-identical to the canonical blocks |
| `[TB-P0m]` | every answer with the success `message` | HOLDS with 6 usable |
| `[TB-REAL]` | all three shards in the real byte format of 2.1 (compact, sorted keys, the success `message`, raw UTF-8, `\u003c`, `\u003e`, `\u0026`, `\u001b`, and U+FEFF as the first character of `logs_content`) | HOLDS with 6 usable. The fixture writer's output must also match the layout pattern of 2.1, so the control is shown to be in the real format |
| controls.py end to end | `assemble.py`'s real output, serialized in the real byte format, through the full intake (strict grammar, then `read_shard`). `[N1]` extended to the decoded scan | the real assembler output passes the new boundary, and genuine logs name only their own shard in decoded form as well |

*Host failures at every intake stage, the inventory, the jobs-list integers and output (D1, D2, D3, AR-N1, AR-N2)
[rev D1, D2, D3]*

**Common to the host-failure tests.** In these tests the target is argument 1 of
`[S1, target, S2, S3]`, so that arguments come after it, as in the acceptance review's injection matrix. The target
is a well-formed answer of job 77001 whose `logs_content` is `scanx-marker`, or, in `[TB-LINKX]` and `[TB-LINKC]`, a
symbolic link to such an answer written outside the served set. Each injection patches one call, raises only when
that call is made on the target, and records that it fired. Every test asserts that it fired, so a mistargeted
injection fails the test instead of passing it vacuously. A test named `…X` expects ABORTED. In each of its cases it
asserts all of the following:
- exit 4;
- `--out` does not exist (`os.path.lexists` is false);
- no `collected.json` and no `ci/` exist anywhere in the test's directory, the staging directory this invocation
  left included, so no stale or partial output exists;
- no line starts with `COLLECT PUBLISHED`, and no line equals `COLLECT HOLDS`;
- the last line is `COLLECT ABORTED <name>`, with the injected errno's name or exception class;
- the `COLLECT FILE` lines are exactly those the test states;
- no stdout line gives the target a reason: no `missing`, `unreadable`, `symlink`, `scan failed` or other reason on
  any line naming it;
- stderr is empty.

So a host failure is never counted as a file's rejection or an evidence failure, and never yields a success or a
usable run. A test named `…C` is that stage's control. It injects the file-specific errnos at the same call and
expects a published, quarantined record, read back from disk under harness rules 1 to 7. The record gives the
target its kind and reason, records all four files, and quarantines the target by name: the `rej()` check of the
existing tests, exit 1. The controls show that the injection point distinguishes a file's condition from a host
failure, and that a regression to "every error is the file's" fails a named test.

| Test | Case | Proves |
|---|---|---|
| `[TB-SCANXd]` | the decoded scan: `raw_named` raises when it scans the target's decoded `logs_content` (the call whose data does not begin with `{`), with (a) `MemoryError`, (b) `OSError(ENOSPC)`, (c) `OSError(EIO)`. The test also asserts that the byte scan of the target ran and returned | ABORTED as above. `COLLECT FILE` lines for arguments 0-3: 0 `accepted`, 1-3 `unjudged`, with null reasons. A host failure in the decoded scan is never `decoded scan failed` (the review's X1) |
| `[TB-SCANXp]` | the parsed readings: (a) `MemoryError`, (b) `OSError(ENOSPC)` and (c) `OSError(EIO)` from `shard_of` on the target, and (d) `OSError(EIO)` from `shards_named` on the target | ABORTED, with the lines of `[TB-SCANXd]`. Never `parsed scan failed` (X2) |
| `[TB-LSTATX]` | `os.lstat` of the target raises (a) `OSError(EIO)`, (b) `OSError(ENOSPC)`, (c) `MemoryError`; and (d), with no injection, a target path through a symbolic-link loop (`ELOOP` from `lstat`, a host failure under 13.2 of the design review) | ABORTED in S2b. One `COLLECT FILE` line, argument 0's, `unjudged`. Never `missing` (X6) |
| `[TB-LSTATC]` | `os.lstat` of the target raises (a) `OSError(ENOENT)`, (b) `OSError(EACCES)` | published, exit 1. The target is `kind: "missing"`, reason `not a regular file (missing)`, in (a), and `kind: "unreadable"`, reason `not a regular file (unreadable: EACCES)`, in (b) |
| `[TB-OPENX]` | `lstat` succeeds and `os.open` of the target raises (a) `OSError(EIO)`, (b) `OSError(ENOSPC)`, (c) `MemoryError` | ABORTED in S2b, with the line of `[TB-LSTATX]`. Never `unreadable` (X7) |
| `[TB-OPENC]` | `os.open` of the target raises (a) `OSError(EACCES)`, (b) `OSError(ELOOP)` (it became a link) | published, exit 1. The target is `kind: "unreadable"`, with reason `not a regular file (unreadable: EACCES)` or `(unreadable: ELOOP)` |
| `[TB-LINKX]` | the target is a link to a regular answer: (a) `os.stat` of the link raises `OSError(EIO)`; (b) `os.read` of the link target's descriptor raises `OSError(ENOSPC)`; (c) the same read raises `MemoryError` | ABORTED in S2b, with the line of `[TB-LSTATX]`. A host failure while hashing a link's target is never swallowed into a `symlink` record with a null digest (X14) |
| `[TB-LINKC]` | (a) a dangling link; (b) a link whose `os.open` raises `OSError(EACCES)` | published, exit 1. The target is `kind: "symlink"`, reason `not a regular file (symlink)`, `size` and `sha256` null. `[TB-LINK]` remains the case in which the target's digest is recorded |
| `[TB-INVJ]` | AR-B1's input, through `main` with the real runs.json: the `jobs_list(32)` fixture with `"total_count": 33` written as `"total_count": 1e400` in the bytes, and S1, S2 and S3 served | published, exit 1, under harness rules 1-7. Exactly one `input` entry for `jobs list`, with the test's sha256 and size of those bytes and `problems == ["non-integer number"]`; no `internal` entry. `collection.inputs.runs_json` is `{name: "runs.json", kind: "regular", size, sha256: RUNS_SHA256, pinned: true}`, and `collection.inputs.jobs_list` has the test's size and sha256. `files` has 3 entries with the test's digests, each `accepted`; `expected` has 32 entries, all `undetermined`. The stdout checks of `[TB-INJ]` hold, and the strict read finds no `Infinity` or `NaN`. A malformed jobs list yields the full inventory (D1) and is refused at the jobs-input gate (D2) |
| `[TB-INVINT]` | through `main` with the real runs.json, `jobs_list(32)` and S1, S2, S3, with `jobs_schema` replaced in the test by a function that raises `TypeError` | published, exit 1. An `internal` entry with `stage: "S4"` and `exception: "TypeError"`. Both `collection.inputs` are non-null with the test's digests. `files` has 3 entries with the test's digests, each `unjudged` with a null reason, and there are 3 `COLLECT FILE` lines. An unforeseen exception while a jobs list is interpreted publishes the full inventory (AR-B1's mechanism) |
| `[TB-INVINTf]` | a direct collection of `[S1, target, S2, S3]`, with `parse_served` replaced in the test by a function that raises `TypeError` on the target's bytes | published, exit 1. An `internal` entry with `stage: "S5"`. `files` has 4 entries with the test's digests: argument 0 `accepted`, arguments 1-3 `unjudged` with null reasons; no `unattributable` entry; 4 `COLLECT FILE` lines; the stdout checks of `[TB-INJ]`. Declared deviation (4) is gone |
| `[TB-INVX]` | a direct collection of `[S1, target, S2, S3]`, with `read_input` (the inventory's read) replaced in the test by a function that raises `TypeError` on the target's path | ABORTED in S2b, as in the common assertions: exit 4, `--out` absent, no `collected.json` anywhere, last line `COLLECT ABORTED TypeError`, and one `COLLECT FILE` line, argument 0's, `unjudged`. A bug that prevents a complete inventory never publishes a partial one |
| `[TB-JNUM]` | (i) **unit:** `JOBS_DECODER` and then `jobs_schema` applied to `jobs_list(32)` with one value's JSON text replaced, one fault per fixture. `total_count`: `1e400`, `-1e400`, `1.0`, `33.0`, `3.3e1`, `NaN`, `Infinity`, `-Infinity`, `true`, `false`, `null`, `"33"`, `-1`, `1001`, and a 21-digit integer. The `id` of the job named `Extract shard 1`: `1e11`, `101.0`, `true`, `"101"`, `null`, `0`, `-101`, `10000000000000000`, the array `[[101]]` (AR-N3's shape: whatever an array holds, its problem is the fixed J-4 text), and the key absent. The `run_id` of the first job: `5.0`, `1e400`, `true`, `"5"`, `0`, `-5`, `10000000000000000`. The `name` of a job: `5`. The `head_sha` of a job: `null`. (ii) **through `main`,** with [TB-RUNS]'s two-line runs.json, which is not pinned, so the record stays small: the `id` `true`, the `run_id` `5.0` and the `total_count` `NaN` | (i) Each form is refused, and nothing raises. A fraction or an exponent gives `non-integer number`; `NaN`, `Infinity` and `-Infinity` give `non-standard constant <c>`; the 21-digit integer gives `integer out of range`; every other form gives the exact J-1 to J-5 problem of 2.3. (ii) Each is published, exit 1, with one `input` entry for `jobs list` carrying the test's sha256 and that problem, both `collection.inputs` non-null, and every served file recorded. The schema runs even when runs.json is not loaded |
| `[TB-JREAL]` | the positive control: a jobs list in the provider's exact shape. It has 33 jobs, 32 named `Extract shard K` and one `Self-tests and controls`, each with the 23 keys of the saved lists in the API's order, and a `steps` list whose objects carry an integer `number`. Ids have 12 digits and the run id 11. One job has null `runner_id`, `runner_name` and `runner_group_id`. The list is serialized compact, with no trailing newline. (i) **unit:** the decoder, `jobs_schema` and `build_job_index` with 32 shards. (ii) **through `main`,** with the real runs.json and S1 served | (i) No problem, and an index of the 32 distinct ids. (ii) Published, exit 1 (31 shards are not served). No `input` entry for the jobs list. `expected` has 32 entries whose `job_id`s are the list's, none `undetermined`. `collection.inputs.jobs_list` has the test's digest. A genuine provider record passes the jobs-input gate |
| `[TB-NANOUT]` | a direct collection of S1, S2 and S3 with `run_id=float("inf")`, which no input can produce | exit 4, `--out` absent, no `COLLECT PUBLISHED` line, last line `COLLECT ABORTED ValueError`. A non-finite number is never published (AR-N2) |
| `[TB-OUTC]` | S1 with run 800's block carrying an `expected.outcome` made of `gate`, a line feed, `COLLECT FAILS`, U+2028 and `x` (a canonical block with its SHA256 line), beside S2 and S3 | HOLDS with 6 usable. Run 800's `RUN` line ends with `esc(outcome)`, no line equals `COLLECT FAILS`, and every line is printable ASCII (AR-N1) |
| `[TB-EMIT]` | **unit:** `emit` into a buffer with a line holding a line feed, a carriage return, a form feed, U+0085, U+2028, U+2029 and U+00E9 | the buffer holds exactly one line, printable ASCII, each of those characters written as its JSON escape. The backstop is tested on its own (the review's X9) |

The `…X` tests and `[TB-INVX]` publish nothing, so they cannot use harness rules 1 to 7. They assert the
filesystem directly, as listed above. Every other new test reads its record back from disk under the harness rules.
Each test must fail by assertion under its mutant, not by a traceback, because controls.py counts a crashed suite
as not specific (L16's rule).

**Mutants.** These are added to controls.py's `MUTANTS`, each with the exact names of the tests it must fail.

| Mutant | Old behaviour restored | Must fail |
|---|---|---|
| L1 | lenient parsing inside the new interface: the body of the new `parse_served` (bytes in; object or rejection reason out) replaced by `09d439d0`'s reading. That is `json.loads(text)` on the UTF-8 decode, then only the three old `isinstance` checks (`collect.py:145-147`), returning the object on success and a fixed reason otherwise. So the suites run without a traceback | `[TB-D5]`, `[TB-D1]`, `[TB-D1b]`, `[TB-D4]`, `[TB-X3]`, `[TB-KEY]` |
| L2 | `SERVED_DECODER`'s `object_pairs_hook` replaced by `dict` (last-wins); the other two decoders unchanged | `[TB-D5]`, `[TB-D1]`, `[TB-D1b]`, `[TB-D4]`, `[TB-DEEP2a]` |
| L2j | `JOBS_DECODER`'s `object_pairs_hook` replaced by `dict` (last-wins in the jobs list and runs.json); the other two decoders unchanged | `[TB-DEEP2b]` |
| L3 | `SERVED_DECODER`'s hook keeps the first value of a duplicated key (first-wins); the other two decoders unchanged | `[TB-D5]` (its D5r half), `[TB-D1b]` |
| L4 | the key-set check relaxed to required ⊆ keys (extra keys allowed) | `[TB-KEY]` |
| L5 | the `message` value not checked | `[TB-X3]` |
| L6 | `BLOCK_DECODER`'s `parse_constant` removed; `SERVED_DECODER` and `JOBS_DECODER` unchanged | `[TB-NAN]` (its block half) |
| L7 | the step-2 check of 2.2 (`EF BB BF`) removed **and** decoding with `utf-8-sig` (BOM tolerated) | `[TB-BOM]` |
| L8 | the `end == len(text)` check removed | `[TB-TRAIL]` |
| L9 | no staging: `write_collection` writes the result files and `collected.json` directly into `--out` (created with `exist_ok=True`), and the rename is skipped; S1 stays | `[TB-O5]`, `[TB-O6]` (each needs `--out` absent after a failure). `[TB-O1]` and `[TB-O2]` are not on this list: S1 refuses them before any write, so they pass under L9 |
| L10 | the S1 existence check removed | `[TB-O1]`, `[TB-O2]`, `[TB-O3]` |
| L11 | the early S3 and S4 exits return before publishing (the `09d439d0` `main`) | `[TB-RUNS]`, `[TB-JOBS]` |
| L12 | first copy's digest only (N3) | `[TB-N3]` |
| L13 | the decoded scan removed | `[TB-ESC]` |
| L14 | jobs-list ids not required distinct | `[TB-JOBID]` |
| L15 | the trailing-`"\n"` tolerance restored | `[TB-NL]` |
| L16 | the `expected.outcome` check removed | `[TB-K1]` (it must fail by assertion, not by a crash: the harness counts a traceback as not specific) |
| L17 | the per-file catch of 2.5 removed, so a scan's `ValueError` reaches S10's `internal` quarantine and stops the intake | `[TB-SCAN]` |
| L18 | the per-file catch widened from `ValueError` to `Exception` (the blanket catch the owner excluded) | `[TB-SCANX]` |
| L19 | S10 catches a host failure (`MemoryError`, `OSError`) as an `internal` quarantine and publishes it | `[TB-SCANX]` |
| L20 | step 1 records every `OSError` of a read as the file's `unreadable` kind, `EIO` included | `[TB-SCANX]` |
| L21 [rev D3] | the review's X1: the decoded scan's catch widened from `SCAN_ERRORS` to `Exception`; the other two catches unchanged | `[TB-SCANXd]` |
| L22 [rev D3] | the review's X2: the parsed readings' catch widened from `SCAN_ERRORS` to `Exception`; the other two catches unchanged | `[TB-SCANXp]` |
| L23 [rev D3] | the review's X6: every `OSError` from `lstat` recorded as `missing`, `EIO` included (the `NAMES_NOTHING` test replaced by `True`) | `[TB-LSTATX]`, `[TB-LSTATC]` (its `EACCES` case becomes `missing`) |
| L24 [rev D3] | the review's X7: every `OSError` from `open` recorded as `unreadable` (the re-raise after the `OWN_ACCESS + (ELOOP,)` test removed) | `[TB-OPENX]` |
| L25 [rev D3] | the review's X14: every `OSError` while hashing a link's target swallowed, so the link is recorded with a null digest (the re-raise after the `NAMES_NOTHING + OWN_ACCESS + (ELOOP,)` test removed) | `[TB-LINKX]` |
| L26 [rev D1] | `a77c85a5`'s order: the served arguments are inventoried only after S3 and S4 have interpreted runs.json and the jobs list, so an internal error in S3 or S4 publishes a record with no `files` entries | `[TB-INVINT]` |
| L27 [rev D1] | an exception inside S2b that is neither a file's condition, a host failure nor an interrupt is turned into S10's `internal` quarantine, and the entries made so far are published | `[TB-INVX]` |
| L28 [rev D1] | declared deviation (4) restored: an internal error's record keeps only the `files` entries S5 had judged, and drops the `unjudged` ones | `[TB-INVINTf]`, `[TB-INVINT]` |
| L29 [rev D2] | the label fix: `JOBS_DECODER` admits floats again, `jobs_schema` is skipped, and `OverflowError` is added to `build_job_index`'s `except` tuple | `[TB-INVJ]` (the problem is no longer `non-integer number`), `[TB-JNUM]` (for example `"total_count": 33.0` beside 33 jobs is accepted) |
| L30 [rev D2] | the integer schema's type and range conditions removed (J-2, J-4 and J-5 test presence only); the decoder still refuses floats | `[TB-JNUM]` |
| L31 [rev AR-N2] | `allow_nan=False` dropped from the serialization of `collected.json` | `[TB-NANOUT]` |
| L32 [rev AR-N1] | the review's X9: the `emit` backstop removed (the line printed as given) | `[TB-EMIT]` |
| L33 [rev AR-N1] | a usable run's `outcome` printed raw on its `RUN` line (`a77c85a5:collect.py:956`) | `[TB-OUTC]` |

The 71 existing mutants stay. If a change of code text moves an anchor, the mutant is re-anchored with the same
meaning. A mutant whose target code is removed (the lenient `parse_served`) is replaced by its counterpart on the
new code. Each replacement is listed by number in the implementation's change note. The 71/71 and earlier
clean controls certify nothing about this design; only the fresh acceptance review does.

[rev D3] At `a77c85a5`, `MUTANTS` holds 92 entries: the 71 and the 21 of L1-L20 with L2j. All 92 stay. Any whose
text the correction moves is re-anchored with the same meaning and listed in the change note. L21-L33 are added,
105 in all, 85 of them on `collect.py`. L21-L25 are independent mutants: each restores one of the review's X1, X2,
X6, X7 and X14 alone, and L18 is not reused for any of them. The 17 new tests, `[TB-SCANXd]` to `[TB-EMIT]`, take
the collect self-test from 162 cases to 179.
The positive controls `[I3]`, `[TB-P0m]`, `[TB-REAL]`, `[TB-JREAL]` and controls.py's end-to-end check must keep
holding.

**Runtime budget (workflow unchanged).**
- **The baseline.** At `09d439d0`, controls.py takes 11 min 37 s locally (review §1). The selftest step's timeout
  is 15 minutes (`.github/workflows/ci-batch-extract.yml:64`), and the job's is 20 (`:44`). One collect self-test
  takes 6.5 s locally, measured for this design.
- **The saving.** The implementation changes `controls.selftests` so that a mutant of `collect.py` runs only the
  collect suite. Neither of the other suites reads `collect.py`. A mutant of `host.py` still runs both host and
  assemble, since `assemble.py`'s self-test reads `host.py` (`assemble.py:1294`), and the unmutated copy runs all
  three. This saves about 3 s per `collect.py` mutant, and the self-test passes `durable=False`.
- **The limit.** The implementation must report the measured local wall time of the full selftest step sequence
  (`.github/workflows/ci-batch-extract.yml:66-71`). If it exceeds 10 minutes, the implementation stops and returns
  to the owner rather than editing the workflow. With the 21 new mutants, the design review estimates about 9
  minutes, so this stop condition may fire.
- **This revision's cost, and two workers for the mutant phase [rev D3].**
  - **Measured for this revision,** at `a77c85a5`, on the local host (4 cores), with a scratch timing probe. One
    collect self-test takes 4.4 s alone. A collection of four files that aborts takes about 5 ms. One that publishes
    takes 7 to 10 ms. One through `main` with the real runs.json takes about 25 ms. The 17 new tests make about 35
    collections, three of them through `main` with the real runs.json. They add about 0.25 to 0.3 s to each collect
    self-test.
  - **The baseline.** The acceptance review measured about 490 s for the full selftest step sequence. controls.py
    took 482 s of it, with the review's probes running alongside; the implementer reported 465 s. So a `collect.py`
    mutant costs about 6 s inside controls.py.
  - **Run serially, the revision would add about 115 s.** The 13 new mutants cost about 6.3 s each, about 82 s. The
    collect suite runs 87 times (the workflow's own step, the unmutated copy and 85 mutants), each about 0.4 s
    slower inside controls.py, about 35 s more. The total would be 580 to 605 s. That is at the 10-minute stop rule,
    and would probably trip it.
  - **So the correction runs controls.py's mutant phase with two workers.** At most two mutants' self-tests run at
    a time, each in its own copy of `batchx/` and its own temporary directory under the work directory, as now.
    The suites already isolate themselves: every self-test makes its own `mkdtemp` under `--work`, and `host.py`'s
    local servers bind port 0. The plan check, the end-to-end check and the unmutated copy still run first, serially,
    as now. Each mutant's result is collected and printed in `MUTANTS` order. So the output, the kill rule (every
    named test failing by exact name, no traceback) and the table are what one worker gives. The estimated wall time
    of the full step sequence is then 330 to 370 s.
  - **The stop rule stands.** If the measured local wall time of the full selftest step sequence exceeds 10 minutes,
    the correction stops and returns to the owner. A disk or timeout problem is reported as infrastructure, never as
    a verdict. The workflow, with its 15-minute step timeout, is unchanged.

## 7. Scope and non-goals

The design defends the boundary between the bytes the operator saves and the results the collector publishes. It
does not defend against:

- **A compromised session host or filesystem.** That includes a process that rewrites `--out` after publication.
  The reader's digest checks (section 4) detect such a rewrite, but nothing prevents it.
- **Forged GitHub data.** A job-log tool answer that is internally consistent but false, or a jobs list that is
  valid but forged. The SHA256 lines detect corruption in transit, not authorship. Authenticity rests on the tool
  and on the GitHub API.
- **A compromised CI runner,** or a change to the pinned workflow, scripts or extractor. Those are covered by the
  pins and by controls.py's plan check, not by this boundary.
- **Concurrent writers to the same parent directory.** Section 4 bounds the effect: no stale file is ever exposed.
  It does not make concurrent collections coordinate.
- **Network filesystems and operating systems** whose `rename` lacks the POSIX directory semantics described in
  section 4.
- **The archive's acceptance of `cited-bridge` results** (DESIGN §9, question 1), and a mechanical `--verify` mode
  for readers.
- **JSON parsing in CI by `host.py` and `assemble.py`** (for example `host.py:91`, `assemble.py:261-266`). Those
  inputs come from the GitHub API over TLS, inside the pinned workflow, and nothing they parse is published without
  passing this collector.

**What is claimed.** The design claims the closure property of section 0, for the inputs and states listed here,
and nothing beyond it. That property is a target until the implementation and the fresh acceptance review exist.

## 8. Implementation bound

**The correction after the acceptance review of `a77c85a5` [rev D1, D2, D3].** The first implementation is
`a77c85a5`, bounded as described from "One commit" below. The correction is one commit. It is a single-parent child
of the commit at which the design review confirms this revision, which is itself a child of `a77c85a5`, so
`a77c85a5` is amended forward, never rewritten or deleted. It touches exactly `batchx/collect.py`,
`batchx/controls.py` and `DESIGN.md`: `git diff --name-status <confirmed> <correction>` shows those three `M` lines
and nothing else. Every other file is byte-identical, `TRUST-BOUNDARY.md` included. Its content:

- **`batchx/collect.py`.**
  - **The inventory (S2b).** A new `inventory(...)` calls `read_input` for `--runs`, `--run-jobs` and every
    `--served` argument, in that order. It returns the entries of section 3 and the snapshots. `load_inputs` is split
    in two: the inventory part moves into S2b, and the interpretation of the two snapshots stays in S3 and S4.
    `collect()`'s direct form inventories only the served arguments.
  - **The intake (S5).** `_take_in` takes an inventory entry and its snapshot, and runs steps 3 to 5 only.
  - **`run_collection` and `evaluate`.** They follow the revised state machine: S2b, its checkpoint, and ABORTED
    for every non-file exception in S2b. The `COLLECT FILE` lines are printed once, by the rule of section 3. The
    internal record keeps the inventory and the `unjudged` statuses. The fallback in S10's handler does not catch a
    host failure.
  - **The jobs list.** `JOBS_DECODER` gets `parse_float=_no_float`. A new `jobs_schema` holds rules J-1 to J-5
    (`MAX_JOBS = 1000`, `MAX_ID = 10**16 - 1`). `build_job_index` is unchanged in its rules, and its `except` tuple
    is unchanged.
  - **Output.** `allow_nan=False` in `write_collection`'s `json.dumps`, in `esc`, and in the `COLLECT FILE` lines.
    `esc(outcome)` on the `RUN` line.
  - **`self_test`.** Harness rules 1 and 5 as revised; the 17 tests of section 6; the moved `[TB-SCANX]` line
    expectation; and a genuine-shape jobs-list fixture for `[TB-JREAL]`.
  - **Unchanged.** `raw_named` and its patterns, byte for byte, together with `shards_named`, `shard_of`,
    `identity`, `strip`, `runset_digest`, `read_shard`, `git_blob_id`, `collector_identity`, every pin constant,
    `SERVED_DECODER`, `BLOCK_DECODER` and the grammar of 2.2. `read_input` and `_read_fd` are unchanged too, so the
    inventory classifies errnos exactly as the acceptance review's injection matrix verified, and so is `emit`.
- **`batchx/controls.py`.** L21-L33 in `MUTANTS`, with their must-fail lists; existing entries re-anchored only
  where their text moved; the two-worker mutant phase of section 6. `plan_problems`, `FILES`, `SUITES` and
  `end_to_end` are unchanged.
- **`DESIGN.md`** (AGENTS.md §A.25). The changed statements are propagated:
  - §4 "Global, in the session": every input is read and hashed before any is interpreted; the jobs list admits no
    fraction, exponent or constant, and its consumed fields pass the integer schema; an unforeseen exception after
    the inventory publishes the full inventory, and one during it publishes nothing.
  - §4's `collected.json` field list: `files[*].status` can be `unjudged`, and `collection.inputs` entries carry
    `kind`.
  - §7: the collect self-test's 179 cases; the 105 mutants with L21-L33; the two workers.
  - §8 "After the run": exit 4 now also covers an inventory that could not complete.

**The fresh acceptance review of the correction [rev D1, D2, D3]** expects, beyond the list at the end of this
section:
- **AR-B1's input** (`total_count` `1e400`), and every form of `[TB-JNUM]`: an `input` rejection with the jobs
  list's digest. Both `collection.inputs` are non-null, every served file is recorded, there is no `internal` entry,
  and no `Infinity` appears in the record.
- **An unforeseen exception** in S3, S4 or S5: published `internal`, with the full inventory and `unjudged` statuses.
  The same exception inside S2b: ABORTED, nothing published.
- **The review's injection matrix**, re-run, with the target as argument 1. Every host-failure cell (`EIO`,
  `ENOSPC`, `EMFILE`, `ENFILE`, `ENOMEM`, `MemoryError`, `KeyboardInterrupt`) is ABORTED at every stage, the
  link target's hashing included. Every `EACCES`/`EPERM` and `ENOENT` cell stays as the review found it. The old
  **I** column (`TypeError`, one file of four recorded) becomes: ABORTED for `lstat`, `open`, `fstat` and `read`,
  which are in S2b, and published `internal` with all four files recorded for every later stage.
- **The review's X1, X2, X6, X7 and X14, re-applied:** each killed by its named test. X9 is killed by `[TB-EMIT]`.
- **The positive controls** hold: `[I3]`, `[TB-P0m]`, `[TB-REAL]`, `[TB-JREAL]` and controls.py's end-to-end check.

**The first implementation (`a77c85a5`), as bounded before this revision.**

One commit, a single-parent child of the commit the design review accepts. It touches exactly these three files.

**`batchx/collect.py`**
- New:
  - `SUCCESS_MESSAGE`, `MAX_SERVED_BYTES`, and the three decoders `SERVED_DECODER`, `JOBS_DECODER` and
    `BLOCK_DECODER` (2.3);
  - `read_input(path, cap)`, which performs 2.5 steps 1-2 and returns the record and the bytes;
  - `open_staging(out)` (S1-S2) and `publish(...)` (S11-S12);
  - `evaluate(...)`, the body of the current `collect`, made pure: it returns the record and writes nothing. Its
    intake runs each argument's scans and parsed readings inside the per-file catch of 2.5, which catches
    `ValueError` only.
- Changed:
  - `parse_served`, which now takes bytes and returns either the object or a rejection reason;
  - `build_job_index`, which adds the distinct-ids rule;
  - `read_shard`, which adds the block loader and the `expected.outcome` check, and drops the trailing-line pop at
    `:219-220`;
  - `write_collection`, which writes into staging, with the manifest and the new fields. The usable-run line at
    `:367` is unchanged. It also changes two things: `runs_sha256` becomes the loaded file's digest or null (A2),
    and a quarantined record's `runs[*]` lose `sha256` and `outcome` (section 5);
  - `collect`, which becomes `open_staging`, `evaluate`, `publish`, with its signature kept and a `durable`
    parameter added. A direct call records `inputs.runs_json` as null;
  - `main`, which follows S0-S12 and returns 0 to 5. It builds the parser with `add_help=False`, catches
    `BaseException` as section 3 prescribes, prints the `COLLECT FILE` lines, and sends every output line through `emit`,
    with every input-derived value JSON-escaped, the `RUN` lines included (A1, A3);
  - `_shard_text`, which gains the real-byte-format option;
  - `self_test`, which gains the harness rules and the tests of section 6;
  - the module docstring, for the corpus statements.
- Unchanged:
  - `raw_named` and its patterns, byte for byte: its `ValueError` is handled by the intake's per-file catch;
  - `shards_named`, `shard_of`, `identity`, `strip` and `runset_digest`;
  - `git_blob_id` and `collector_identity`;
  - every pin constant.

**`batchx/controls.py`**
- `MUTANTS`: re-anchored where text moved, plus L1-L20 and L2j: 21 new mutants.
- `selftests`: the per-file suite selection of section 6.
- `end_to_end`: the real-format intake and the decoded `[N1]` check.
- `plan_problems` and `FILES` are unchanged.

**`DESIGN.md`**
- Propagate the changed statements (AGENTS.md §A.25):
  - §4 "Global, in the session" and the `collected.json` field list;
  - the raw-scan invariant at DESIGN.md:184-206, which is restated as what the strict grammar plus both scans
    enforce;
  - §7, the suite counts;
  - §8 "After the run", which gets: a fresh `--out` per collection; exit codes 0-5 and what each guarantees
    (section 3); serving exactly the 32 shard answers; and the reader's currentness check of section 4, stated as
    **mandatory before any result is used**. An `--out` left in place by a REFUSED or ABORTED invocation is
    excluded only by that check (A1e).

  On serving: the selftest job's answer is not served. Its job id is in the jobs list but not in the index, and its
  log names shards (its test names contain `EXTRACT SHARD 2/3`). So serving it takes the foreign-job path at
  `collect.py:438-444`, which FAILS and voids the shards it names, not the quarantine at `:432-437`. Either way no
  run is usable.

**What stays unchanged.**
- `.github/workflows/ci-batch-extract.yml`, `batchx/host.py`, `batchx/assemble.py`, `batchx/runs.json`,
  `batchx/crosscheck.json`.
- `TRUST-BOUNDARY.md` itself. A divergence found during implementation is a stop condition, reported to the owner.

Why the five stay unchanged:
- The collector runs only in the session.
- `collect.py`'s pins (`ASSEMBLER_BLOB`, `HOST_BLOB`, `EXTRACT_RESULT_BLOB`, `MAIN_COMMIT`, `RUNS_SHA256`) stay
  valid because those files do not change, and controls.py's plan check verifies them.
- The workflow already runs `collect.py --self-test` and `controls.py` in its selftest job. Its text pins neither
  file.
- The one condition under which the workflow would have to change, its timeout, is handled by the runtime budget
  of section 6 as a stop condition.

**Acceptance review.** The fresh acceptance review at the exact implementation SHA re-runs the review's probes
(`batchx-review5/tools/probe5.py`, `probe5b.py`) and expects:
- **D1, D1b, D1c, D2, D3, D4, D5, D5r, X1, X2, X3:** QUARANTINED, each with its file and reason.
- **E1-E13, T1-T3:** QUARANTINED, published, with no traceback.
- **O1, O2:** REFUSED, untouched.
- **K1, K2:** QUARANTINED, with a `failed_files` entry.
- **P0, P0m, C1, C2, C3, C4s:** HOLDS with 6 usable. **C4** (the review's case: a copy with the `message` `"m"`):
  QUARANTINED.
- **B1, J1, E-esc** (section 0): QUARANTINED.
- **A file on which a scan raises `ValueError`** (`[TB-SCAN]`, cases a-d): that file rejected with its reason and
  `names_shards` null, every argument recorded, and the collection QUARANTINED, with no `internal` entry. A
  `MemoryError`, `ENOSPC` or `EIO` injected at intake, or an interrupt (`[TB-SCANX]`): ABORTED, exit 4, nothing
  published, never a file's rejection.
- **Exit codes:** every path of section 3 gives its stated code. `-h` gives 3. No path exits 0 without a
  `COLLECT PUBLISHED` line followed by `COLLECT HOLDS`.
- **Zero invariant violations** under the review's read-back rule.

## 9. Decisions (ruled by the design review of `3c0e1d72`)

The review accepted D1 to D5 as written. For D1 it also recommended the change to quarantined `runs[*]`, which
section 5 adopts.

- **D1. "Quarantines the entire collection" and per-run `eligible`.** This design reads I-QUAR as a property of the
  collection: no usable run, and no results directory. It keeps per-run `eligible` after a validation failure as a
  diagnostic that licenses nothing, as the owner earlier accepted. Clearing `eligible` under every failure would
  change the expected counts of 67 existing `case()` tests (54 FAILS and 13 UNVERIFIED, as the review counted them
  with an instrumented copy), 7 `[RP]` permutation scenarios, and the `[I2]` and `[I2b]` checks. Those counts are
  what show voiding is precise and order-independent. Clearing them would weaken the tests without changing what is
  usable. A quarantined record keeps `eligible`, but drops the result content `outcome` and the block `sha256`
  (section 5).
- **D2. Canonical bytes.** Requiring each served file to equal the canonical encoding of 2.1 would hold for all 379
  real answers. It would also close the remaining spelling freedom by construction, including E-esc and N3. But it
  rejects the review's clean controls P0 (Python's separators) and C3 (indented), which I-PARSE's instruction to
  preserve the clean positive controls keeps holding. It also rests on an encoding that is only partly exercised
  (U+2028, `\b`, `\f`). This design therefore takes the strict grammar plus the decoded scan.
- **D3. A leading U+FEFF as a whole-log marker.** All 110 whole answers begin with it, and no tail does. Requiring
  it would add a second whole-log check. It is left out: the fixtures lack it, and it rests on observation, not on
  a documented guarantee.
- **D4. Whitespace around a served object** is refused. That is stricter than "no trailing payload". No real answer
  has any, so the only cost is a re-save by the operator.
- **D5. Message optional.** Every real answer carries the `message`, but I-PARSE makes it optional. An answer
  saved without it is accepted. It carries no content, and the identity excludes it.

## Amendments from the design review of `3c0e1d72`

| Amendment | What it required | Sections changed |
|---|---|---|
| A1 | every path has an exit code; accurate exit-4 rows; a durability failure after the rename is its own outcome; `-h` never exits 0; exit 0 means `COLLECT PUBLISHED` then `COLLECT HOLDS`; REFUSED says `--out` is not a result | 3 (exit table, "What each code guarantees", "Every path gets a code", S0, S1, S2, S11, S12, N2 note); 4 (the rename race, no partial results, mandatory reader check); 6 (`[TB-ARGS]`, `[TB-O5]`, `[TB-O6x]`, `[TB-NDUR]`); 8 (`main`, the DESIGN.md §8 propagation, the acceptance list) |
| A2 | reader check 3 requires the pinned run set; a direct `collect()` call never records the pin | 4 (`inputs.runs_json`, top-level `runs_sha256`, reader checks 2, 3 and 5); 5 (field meanings); 6 (`[TB-SYNTH]`); 8 (`write_collection`, `collect`) |
| A3 | `COLLECT FILE` lines trace every file on ABORTED; names cannot inject lines | 3 (S5, "Safe names on stdout", N2 note); 6 (harness rule 6, `[TB-O6]`, `[TB-INJ]`); 8 (`main`) |
| A4 | L1 inside the new interface; L2j; L9's must-fail list; L7 removes step 2; `[TB-DEEP2c]` as defence in depth; which decoder L2, L3 and L6 mutate | 2.3 (the three named decoders); 6 (`[TB-DEEP2a]`/`b`/`c`, the mutant table); 8 (decoder names, mutant count) |
| A5 | C4s against C4; X1, C4, D2 and D3 named as test cases; `[TB-NL]` in the required tables; `[TB-JOBID]` and `[TB-DEEP2b]` through `main`, read from disk | 1 (copies); 6 (`[TB-D1]`, `[TB-X3]`, `[TB-NL]`, `[TB-N3]`, `[TB-JOBID]`, `[TB-DEEP2b]`, the exact-record tests `[I1]` and `[I5]`); 8 (the acceptance list) |
| A6 | the order of rejection reasons; single-fault fixtures | 2.2 ("What a rejection records"); 6 (required tests) |
| A7 | (a) the D1 counts; (b) the selftest-log path; (c) the decoded and byte scans compared without the `job_id` envelope | 9 (D1); 8 (DESIGN.md propagation); 2.5 (step 5) |
| D1 recommendation | a quarantined record's `runs[*]` drop `outcome` and the block `sha256` | 5 (the `runs[*]` bullet and field meanings); 8 (`write_collection`); 9 (D1) |
| Text repair (not an amendment) | in `3c0e1d72`, the escape sequences intended in six places were stored as the characters they denote, among them a raw U+2028 and U+2029 in 2.1. Restored as escapes | 0 (E-esc); 1 (escaped duplicate key); 2.1 (canonical form); 6 (`[TB-ESC]`, `[TB-REAL]`) |
| A3(b) closure (confirmation pass at `ffa383e6`) | the escaping rule covers every output line, the `RUN` lines (`collect.py:524-526`, reason built at `:497-498`) included, with one `emit` backstop; `[TB-INJ]` uses a rejected file and asserts on every stdout line; two text slips (the two `durable=True` tests; "in collection mode") | 3 ("What each code guarantees", "Safe names on stdout"); 4 ("Durability"); 6 (harness rule 7, `[TB-INJ]`); 8 (`main`) |
| `[TB-INJ]` on-disk assertions (confirmation pass at `e5cbf62e`) | `[TB-INJ]` asserts the quarantine from `collected.json` on disk (FAILS, `quarantined`, no usable run, no `ci/`, the rejected file under its embedded-newline name) and the PUBLISHED line's digest against the file on disk; harness rule 7 captures stderr and asserts it is empty, since collection mode writes nothing there | 6 (harness rule 7, the in-process `main` note, `[TB-INJ]`) |
| Per-file catch for intake-step failures (owner's option 2, after the implementation halted at `1f0b3abe`) | the unchanged `raw_named` raises `ValueError` on more than 4,300 digits after a `"job_id"` key or a shard name, before the grammar; any exception in a per-file intake step now rejects that file with its reason, records it, and lets the intake continue, so S5 still traces every argument; `[TB-SCAN]` and mutant L17 test it; the 5,000-digit `job_id` moves from `[TB-TYPE]` to `[TB-SCAN]` | 1 (malformations); 2.2 (rejection order, the reasons); 2.5 (the per-file catch); 3 ("Every path gets a code", S5, "S5 always runs"); 6 (`[TB-TYPE]`, `[TB-SCAN]`, L17, the mutant count); 8 (`evaluate`, `raw_named`, `MUTANTS`, the acceptance list); the status line |
| Per-file catch narrowed; the boundary by stage and error kind (confirmation pass at `08b1ac45`; the owner's comments 6247145466 and 6247194704) | the catch covers only `ValueError` (with its subclasses) from the byte scan, the decoded scan and the parsed readings `shard_of` and `shards_named`, which now run in the intake; the catch-all `intake failed` reason removed; a three-class boundary: file-specific conditions (missing, non-regular, over the cap, the file's own `EACCES`/`EPERM`/`ELOOP`, grammar rejections) stay attributed rejections, recoverable scan errors are per-file rejections, and host failures (`MemoryError`, any other `OSError` such as `EIO` or `ENOSPC`, interrupts) at any step are ABORTED (exit 4), never published and never a file's rejection; S10 no longer catches host failures; other exceptions keep S10's `internal` quarantine; `names_shards` null whenever a scan raised; `candidates` qualified; the huge-integer case stated as a scan conversion failure with no fall-through; `[TB-SCAN]` gains case (d) and the `[TB-INJ]` stdout checks; `[TB-SCANX]` injects `MemoryError`, `ENOSPC` and `EIO` at the scan and at the read; mutants L18-L20; the §1 bullet moved after X3 | status line; 1 (malformations, not a regular file); 2.2 (rejection order, the reasons); 2.5 (the parsed readings, the per-file catch, the boundary table); 3 ("Every path gets a code", S5, S10, "S5 always runs"); 5 (`names_shards`, `candidates`); 6 (`[TB-SCAN]`, `[TB-SCANX]`, L17-L20, the mutant count); 8 (`evaluate`, `raw_named`, `MUTANTS`, the acceptance list) |
| N2 wording and path errnos (confirmation pass at `3db007b3`) | §3's N2 note made consistent with 2.5: an ABORTED after S5 traces every served file, and one that a host failure ends during S5 traces the files taken in before it; a mistyped or mangled `--served` path (`ENOTDIR`, `ENAMETOOLONG` from `lstat`) is a file-specific `missing` condition, not a host failure; `[TB-MISS]` gains both cases; the status paragraph rewrapped | status paragraph; 1 (not a regular file); 2.5 (the boundary table); 3 (the N2 note); 6 (`[TB-MISS]`) |
| Inventory first, strict jobs-list integers, five host-failure regressions (owner's comment 6247938850, D1-D3, after the acceptance review of `a77c85a5`) [rev D1, D2, D3] | D1: a new state S2b inventories every input (runs.json, the jobs list, every served argument) with 2.5 steps 1-2 before anything is interpreted; any non-file exception in S2b is ABORTED, so no incomplete inventory is published; an unforeseen exception in S3-S10 publishes the full inventory, with `unjudged` arguments; `collection.inputs` are written in S2b and gain `kind`; declared deviation (4) is withdrawn; the `COLLECT FILE` lines are printed once by a stated rule. D2: `JOBS_DECODER` refuses floats; the integer schema J-1 to J-5 runs before `build_job_index` reads any value; no `except` is widened; `allow_nan=False` on every output serialization. D3: `[TB-SCANXd]`, `[TB-SCANXp]`, `[TB-LSTATX]`, `[TB-OPENX]` and `[TB-LINKX]` with their controls, and the independent mutants L21-L25 for the review's X1, X2, X6, X7 and X14. Also: `[TB-INVJ]`, `[TB-INVINT]`, `[TB-INVINTf]`, `[TB-INVX]`, `[TB-JNUM]`, `[TB-JREAL]`, `[TB-NANOUT]`, `[TB-OUTC]` and `[TB-EMIT]`, with mutants L26-L33; AR-N1 (the `RUN` line's `outcome` escaped; X9) and AR-N2 (non-finite output) closed, AR-N3 closed for the jobs list; harness rules 1 and 5 strengthened; the `[TB-SCANX]` line expectation moved; the two-worker mutant phase for the runtime bound | status paragraph; 0 (AR-B1, AR-B2, the inventory property); 1 (the input table, served malformations, the jobs list); 2.3 (`JOBS_DECODER`, the integer schema); 2.5 (the two phases, the steps, the per-file catch, the boundary table, other exceptions, deviation (4)); 3 (exit 4, "Every path gets a code", S2b, S3, S4, S5, S10, the file lines, the `RUN` outcome, the N2 note, "S5 always runs"); 4 (`collection.inputs`); 5 (`files`, `unjudged`, strict serialization); 6 (harness rules 1 and 5, the moved `[TB-SCANX]` expectation, the new tests, L21-L33, the mutant count, the runtime budget); 8 (the correction and its acceptance list) |

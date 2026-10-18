# Batch collector: trust boundary for served-file parsing and output publication

**Status: design only.** The independent design review of `3c0e1d72` approved it with required amendments A1 to A7.
This text includes them, together with the review's D1 recommendation; the table at the end shows where each one
landed. Nothing here is implemented. The design was written against commit `09d439d0`, and every "now" statement
below describes the code at that commit. Each one cites
`batchx/collect.py` as `collect.py:N`, or names the other file it is in. After design review, one bounded
implementation (section 8) follows, and then a fresh exact-SHA acceptance review. If that review finds a fail-open
escape, the work returns to the owner. It is not patched again.

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

## 1. Inputs and trust levels

| Input | Who produces it | Trusted | Untrusted | Gate |
|---|---|---|---|---|
| `batchx/runs.json` | reviewed, committed | its content, once its bytes equal the pin `RUNS_SHA256` (`collect.py:79`) | anything not equal to the pin | sha256 before parsing (`collect.py:1076`), then the strict loader |
| `batchx/crosscheck.json` | reviewed, committed | — | — | not read by the collector. `assemble.py` reads it in CI under its own pin, and it never decides a verdict (DESIGN §7) |
| jobs list (`--run-jobs`) | GitHub jobs API via `gh api`, saved by the operator | the API's values: job ids, names, run id, head, branch, workflow. The design assumes the file is the API's answer. It does not authenticate it | the file's bytes: integrity, encoding, duplicates, shape | strict loader (section 2.3), then `build_job_index` |
| `--head` | the operator | — | the value | 40 lower-case hex digits (`collect.py:112`), and equal to every job's `head_sha` |
| served files (`--served`) | the job-log tool's answer, saved verbatim by the harness or by `from_transcript.py` | the tool's `job_id` and `original_length`, *as values*, once the file passes the strict grammar | everything else: the bytes, the encoding, the shape, the log text | path checks, strict grammar, raw and decoded scans, the job rule, `read_shard` |
| host metadata (`fetch-record.json`, run and jobs records) | `host.py` in CI | pinned code under a pinned workflow | — | never seen by the collector. It reaches the session only through what `assemble.py` prints into the shard log |
| shard outputs (the assembler's lines inside `logs_content`) | `assemble.py` in CI | nothing by itself. The SHA256 lines detect corruption, not authorship, because they travel in the same log | the whole text | `read_shard` (`collect.py:213-332`), against the pins and `runs.json` |
| the output location (`--out`) and its parent directory | the operator's filesystem | — | any pre-existing state | must not exist (section 4) |
| the collector's own code | the session's checkout | recorded, not trusted: `collector_identity` (`collect.py:339-357`) | — | — |

**Served files: every malformation and where it is stopped.** Each line names the state of section 3 that stops
it. Every case is rejected and quarantines the collection unless the line says otherwise.

- **Not a regular file (S5).** A directory (review E12), a missing path (E13), a FIFO or a device: rejected
  without reading. A symbolic link: rejected and never parsed. The regular file it points to is hashed for the
  record only.
- **Too large (S5).** Over `MAX_SERVED_BYTES = 16 MiB`. The largest saved answer seen is 812 KB. The file is
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
    (T1). Huge integers are refused before `int()` runs.
  - An `original_length` that is a float, negative or more than 16 digits long (T2).
  - A `logs_content` that is not a string (T3).
  - A `message` that is not the success string (X3).
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

Unknown fields are allowed here, because the API object carries many. Whitespace around the value is allowed,
because the file is written by `gh api`, not by the job-log tool. All 388 jobs lists saved in the session's work
area (`cier-work/api-jobs/*.json`) parse under this loader, each with distinct ids.

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
- Checks 1 to 4 run first, in that order.
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

- **The jobs list, through `JOBS_DECODER`.**
  - Steps 1 to 3 of 2.2 apply.
  - The value is read with `raw_decode`, and the rest must be JSON whitespace.
  - `parse_int` accepts `-?(0|[1-9][0-9]{0,19})`. Floats are allowed.
  - Unknown keys are allowed. The fields `build_job_index` reads are type-checked as now, and the 32 shard job ids
    must be distinct.
- **runs.json, through `JOBS_DECODER`.** The pin is checked first.
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

For each served argument, in argument order:

1. `lstat`, open with `O_RDONLY | O_NOFOLLOW | O_NONBLOCK`, and `fstat`. The file must be regular and within the
   cap. It is then read once into memory. All later steps use that one buffer, so the file cannot change between
   hashing and parsing.
2. sha256 and size. Every file that can be read is traceable even if every later step rejects it.
3. The raw byte scan (`raw_named`, unchanged), when the run set and index are known. A rejected file still records
   the shards it names. The scan only adds shards a file is involved with, so it can never make a run usable.
4. The strict grammar (2.2). No semantic function (`shard_of`, `shards_named`, `identity`, `read_shard`) ever sees an
   object that has not passed it. H1 was semantics applied to a last-wins object.
5. For accepted answers only: the decoded scan, `raw_named(obj["logs_content"].encode("utf-8"), …)`, joined with
   step 3. Under 2.2, `logs_content` is the only free text in an accepted file, so its decoded form is complete.
   This closes E-esc.

   The real format escapes only quotes, backslashes, control characters and `<`, `>`, `&`, never a letter or a
   digit. So on a genuine log the decoded scan finds the same names as the byte scan, **once the answer's own
   `"job_id":N` envelope is excluded**. The byte scan reads that envelope through `RAW_ID`, `RAW_LONG` and `RAW_JOB`,
   and the decoded scan of `logs_content` never sees it. The review measured this on the 379 real answers: 0
   differences with the envelope excluded, and 129 with it included, because there the envelope id is a bridge job of
   `runs.json`. controls.py's extended `[N1]` check compares the two scans on the same basis.

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
| 4 | ABORTED: an error of any kind, after S2 and before the rename in S12 completes, that the states below do not turn into a quarantine | not created by this invocation; it may hold another process's content (section 4). The staging directory may remain beside it, and is never a result |
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
  - from S2 until the rename in S12 completes: 4. An exception in S3-S10 is first turned into an `internal`
    quarantine by S10 and goes on to be published; only one raised in S11 or S12, or an interrupt, reaches 4. An
    example is a `UnicodeEncodeError` from the ASCII result write;
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
| S3 RUNS | read `--runs` as in 2.5 steps 1-2; pin; strict load | → quarantine `{kind: "input", input: "runs.json"}` with name, size, sha256 (or kind and no digest), `pinned`, reason; `doc = None` | carried into the record; S4 and S5 still run |
| S4 INDEX | read `--run-jobs` as in 2.5 steps 1-2; strict load; `build_job_index` with distinct ids; `--head` check | → quarantine `{kind: "input", input: "jobs list"}` with name, size, sha256, and every problem; `index = None` | as S3 |
| S5 INTAKE | 2.5 steps 1-5 for **every** served argument, whatever S3 and S4 gave; scans need `doc` and `index`. At its end, one `COLLECT FILE` line per argument on stdout (below) | → per file: `files[i].status = "rejected"`, and quarantine `{kind: "unattributable", file, sha256 or null, size, reason, names_shards}` | as S3, and the `COLLECT FILE` lines |
| S6 ATTRIBUTED | runs only if `doc` and `index` exist: the job rule (`collect.py:425-458`), unchanged except that the decoded scan joins `named` | existing edges: a foreign job naming no shard → quarantine (`:432-437`); a foreign job naming shards → FAILS and voids (`:438-444`); several shards → FAILS and voids; copies differ, or a copy has no banner → voids | `voided_shards`, quarantine |
| S7 COMPLETE | each shard K = 1…N has an accepted answer of job `index[K]` (`collect.py:480-483`) | → quarantine `{kind: "missing", shard, job_id, expected}`, plus `expected[K].status = "missing"` | as S3 |
| S8 VALIDATED | `read_shard` on one copy of each surviving shard, with the strict blocks and the `expected.outcome` check | → `failed_files` `{file, sha256, sha256s, shard, problems}`; FAILS | as S3 |
| S9 RECONCILED | each run seen in exactly one shard; no run outside `runs.json` (`collect.py:501`, `:512-514`); all runs eligible | → FAILS (extra run) or UNVERIFIED (a run not eligible, a shard not collected) | `runs[*].reason` |
| S10 DECIDED | `v` as at `collect.py:519-520`; `quarantined = v != "HOLDS"`. An exception raised in S3-S10 that no check foresaw is caught here | an internal error → quarantine `{kind: "internal", stage, exception: <type name>}`, `v = "FAILS"` | as S3 |
| S11 WRITTEN | `write_collection` into the staging directory. The only usable-run rule stays at `collect.py:367`, character for character. Result files only under HOLDS, opened `"x"`; `collected.json` written last, with the manifest; flush and `fsync` each file and the directories when `durable` | any exception or interrupt → ABORTED (4) | stdout `COLLECT ABORTED <exception type or errno name>`; `--out` not created by this invocation; the staging directory is left in place |
| S12 PUBLISHED | `os.rename(staging, out)`, then `fsync` the parent when `durable` | the rename raises, or an interrupt arrives before it completes → ABORTED (4), as S11. The parent `fsync` fails, or anything later fails or is interrupted → PUBLISHED, durability not confirmed (5) | for 5: the `COLLECT PUBLISHED` line, with the nonce and digest, then `COLLECT NOT DURABLE <exception type or errno name>`, then `COLLECT <verdict>` |

After S12, stdout carries the existing `RUN` and `COLLECT n of m` lines, then `COLLECT PUBLISHED <out> nonce <nonce>
collected.json sha256 <hex>`. The last line is `COLLECT <verdict>`, as now.

**Safe names on stdout (A3).**
- **The file lines.** At the end of S5, the collector prints one line per served argument:
  `COLLECT FILE <json>`. The JSON is `json.dumps({arg, name, kind, size, sha256, status, reason},
  sort_keys=True, ensure_ascii=True)`, the fields of `files[i]` in section 5. An ABORTED run (4) publishes no
  record, so these lines are its trace of every file, read and judged.
- **No injected lines.** The rule covers **every line the collector writes to stdout or stderr**, whatever its
  prefix. In each such line, every value that comes from an input is written with `json.dumps(...,
  ensure_ascii=True)`: a file name, a path, a reason built from either, a decoder message, the `--head` value as
  given. That includes:
  - the `COLLECT FAIL` lines (`collect.py:439-440`, `:453`, `:457`, `:470`, `:488`);
  - the `COLLECT PUBLISHED` path;
  - the `RUN` lines (`collect.py:524-526`). Under quarantine their reason joins the quarantined files' names
    (`collect.py:497-498`). For stdout, that reason is built from the JSON-escaped names.

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
  - an unforeseen exception, reached through S10.

  Only the REFUSED and ABORTED outcomes publish nothing. REFUSED has read nothing. ABORTED is a failure of the
  writer itself, and its `COLLECT FILE` lines still trace every served file on stdout.

**S5 always runs.** Every served argument is hashed and grammar-checked even when S3 or S4 failed. A collection
refused early is therefore still traceable file by file. With no index, `files[i].shard` is null and
`expected[*].status` is `"undetermined"`. With no run set, `expected` is null and `runs` is `[]`.

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
  - `runs_json`: `{name, size, sha256, pinned}`, or null when `collect()` is called directly with a `doc` (A2);
  - `jobs_list`: `{name, size, sha256}`, or null when `collect()` is called directly;
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
   "size": <int>|null, "sha256": <hex>|null, "status": "accepted"|"rejected", "reason": <str>|null,
   "job_id": <int>|null, "shard": <int>|null, "names_shards": [<int>, ...]|null, "same_file_as": <arg>|null}
  ```

  - The digest is of the raw bytes. That is the same value as `served_sha256` now, because a UTF-8 decode and
    re-encode is the identity.
  - For a regular file the digest is always present, even when the file is over the cap (streamed) or rejected.
  - For a symbolic link, the digest and size are those of the regular file it points to, read for the record
    only, if it is within the cap.
  - A directory, a missing path or another kind has `size` and `sha256` null, and its `kind` says why.
  - `names_shards` is the union of the raw and decoded scans, or null when no scan could run.
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
  - `candidates` lists the rejected files whose scans name shard K. An empty list means nothing was served for K; a
    non-empty one means something was served for K and rejected. This is how a missing expected file is told apart
    from a rejected one.
  - `undetermined` means the index could not be built.
- **`shards[K]`** gains `sha256s`: every distinct digest among its copies.
- **`failed_files[*]`** gains `sha256s` for the same reason.
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

1. **Read from disk.** Each test reads `--out/collected.json` from disk (`collect.py:644` does this now).
2. **One verdict view.** `quarantined == (verdict != "HOLDS")`, and the count of usable runs is the number of
   runs under HOLDS and 0 otherwise.
3. **Exact listing.** The listing of `--out` is exactly `collected.json` plus the `manifest` paths, with matching
   digests. With no usable run there is no `ci/` directory at all.
4. **No staging left.** No `.out.staging-*` remains in the test's directory after a published outcome.
5. **Every file recorded.** Every served file the test wrote appears in `files` with the size and sha256 the
   test computed itself with `hashlib`, independently of the collector.
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
| `[TB-TYPE]` | T1 (`job_id` float, `7e4`, bool, string, 0, negative, 17 digits, 5,000 digits), T2 (`original_length` float or negative), T3 (`logs_content` a list), null values | types and ranges are enforced |
| `[TB-NAN]` | `NaN`, `Infinity` and `-Infinity` as `original_length`; and B1, `NaN` and `Infinity` inside a result block | constants are refused in served files and in blocks; B1 is closed |
| `[TB-BOM]` | E7, a BOM before `{` | the leading BOM is refused (its positive pair is `[TB-REAL]`) |
| `[TB-UTF8]` | G1d (a 0xff byte), E1 (UTF-16, UTF-16-LE, UTF-16-BE, UTF-32), E2 (shard 2's only answer in UTF-16), a lone surrogate escape | strict UTF-8, and no lone surrogates |
| `[TB-TRAIL]` | E8, `}x`, a trailing newline, a leading space | exactly one object; no trailing payload |
| `[TB-EMPTY]` | E3, E9, E10, E11 | an empty or non-object file is refused, with its digest |
| `[TB-NEST]` | 100,000-deep nesting | refused with a reason; no traceback |
| `[TB-CAP]` | a regular file one byte over the cap | refused; its streamed digest equals `hashlib` over the file |
| `[TB-ESC]` | E-esc: genuine S3 with an indented `\u0042ATCH SHARD 1/3` trailer line, beside S1 and S2; and its plain-spelled control | both give FAILS, with shards 1 and 3 voided; the outcome no longer depends on JSON spelling |

*Paths and copies (I-PARSE, I-PUB)*

| Test | Case | Proves |
|---|---|---|
| `[TB-DIR]` | E12, a served directory | `kind: "directory"`, no digest, published QUARANTINED |
| `[TB-MISS]` | E13, a missing path | `kind: "missing"`, told apart from a missing *expected* answer |
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

The 71 existing mutants stay. If a change of code text moves an anchor, the mutant is re-anchored with the same
meaning. A mutant whose target code is removed (the lenient `parse_served`) is replaced by its counterpart on the
new code. Each replacement is listed by number in the implementation's change note. The 71/71 and earlier
clean controls certify nothing about this design; only the fresh acceptance review does.

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
  to the owner rather than editing the workflow. With the 17 new mutants, the design review estimates about 9
  minutes, so this stop condition may fire.

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

One commit, a single-parent child of the commit the design review accepts. It touches exactly these three files.

**`batchx/collect.py`**
- New:
  - `SUCCESS_MESSAGE`, `MAX_SERVED_BYTES`, and the three decoders `SERVED_DECODER`, `JOBS_DECODER` and
    `BLOCK_DECODER` (2.3);
  - `read_input(path, cap)`, which performs 2.5 steps 1-2 and returns the record and the bytes;
  - `open_staging(out)` (S1-S2) and `publish(...)` (S11-S12);
  - `evaluate(...)`, the body of the current `collect`, made pure: it returns the record and writes nothing.
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
  - `raw_named` and its patterns;
  - `shards_named`, `shard_of`, `identity`, `strip` and `runset_digest`;
  - `git_blob_id` and `collector_identity`;
  - every pin constant.

**`batchx/controls.py`**
- `MUTANTS`: re-anchored where text moved, plus L1-L16 and L2j: 17 new mutants.
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

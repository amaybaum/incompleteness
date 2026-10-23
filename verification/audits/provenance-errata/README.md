# Provenance errata: cited run heads that name no commit

Five citing lines, in four frozen files, cite a CI run's head commit by an id that names no object. In each case the
run executed at its real head, which the host's run and job records name. The cited id shares its first 7 or 8 hex
digits with the real head and is not a prefix of it. The errors are of attribution, not of execution.

The records keep their bytes (AGENTS §A.42 item 6). This table records the attribution errors and the verified heads;
a correction of a frozen record's own text is a native round's (`G13`). Whether a mutable pointer, such as the
evidence-retention manifest, should reference these errata is moot: that archive is read from `main`'s history, not the tree (AGENTS §A.42).

A count discrepancy of a different kind, Act 37's `lean-axioms` figure for its base run (4829 stated, 4803 recorded), is
recorded in [`ACT37-CI-COUNT.md`](ACT37-CI-COUNT.md); it is outside the table below and the checker.

| id | location | run, attempt | cited id | real head | shared digits | verdict | explanation | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PE-1 | verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/preregistration.md:710 | 36257341185, 1 | `4c4155da7ccc2cf47d63bfe2ce7d8c4cba7f0ff2` | `4c4155da059388a4724039fd5e60aaa96965f7c3` | 8 | confirmed | confirmed | holds |
| PE-2 | verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/preregistration.md:711 | 36257659584, 1 | `cff3c1560f4c0fc09aba2c8af06e9f00e0fc0cd7` | `cff3c1566228158acbf6cb710dbdf4ba4c5db91f` | 8 | confirmed | confirmed | holds |
| PE-3 | verification/programmes/oi-qm/track-b/act-35-dita-hull/result.md:218 | 36310787113, 1 | `2ae4dbeef5d9a1c9f0fcf3fbbf1ceaf4de4d3a0d` | `2ae4dbeeceae2b2e66bd43658045b67da0f0e650` | 8 | confirmed | incomplete | partly holds |
| PE-4 | verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/preregistration.md:400 | 36612901341, 1 | `ad64b60319e1ff2d40a5a5eed8e3aa4bfcf30b0e` | `ad64b603b7a1dac18b7246d339abaf43a3642dd3` | 8 | confirmed | confirmed | holds |
| PE-5 | verification/programmes/oi-qm/reconstruction/round-k1-sharp-tests-1/preregistration.md:214 | 37494787556, 1 | `0850281a` | `0850281082f0dd1cf2c6c906afa57726ab31b076` | 7 | confirmed | confirmed | holds |

**How to read the columns:**
- **Verdict** is whether the row's outcome, what the run's jobs concluded, is confirmed: `confirmed` or `not confirmed`.
- **Explanation** is whether the row's account of that outcome (its counts, causes and listed kinds) is `confirmed`,
  `incomplete` or `not confirmed`.
- **Status** follows from the two by the rule `errata.json` states: a verdict not confirmed does not hold; a confirmed
  verdict holds when its explanation is confirmed, and partly holds otherwise.
- **Shared digits** is the number of leading hex digits the cited id shares with the real head.
- **Every run** is a `workflow_dispatch` of `.github/workflows/verify.yml`.
- **`errata.json`** gives, for each entry:
  - the citing line verbatim (`assertion_verbatim`) with its sha256, and a shortened `summary` of it;
  - the content checks, the outcome evidence, the disposition and the cross-references.

## The rows

None is a designated `F` or `E`, and none is a certification:
- **PE-1 and PE-2** are act 33's elaboration runs, design evidence in its preregistration before `F`.
- **PE-3** is a failed first proof pass on act 35's development branch, in its result note's design history.
- **PE-4** is act 45's predicted-tree run, design evidence in its preregistration before `F` that the predicted
  execution tree is green.
- **PE-5** is run b of K1-SHARP-TESTS-1's pre-round evidence, which its preregistration calls supporting history only.

## Which commit each run tested

- **Host records.** Each run's `head_sha`, and every job's `head_sha`, equal the real head, at `run_attempt` 1; none
  equals the cited id. GitHub's commit endpoint answers "No commit found" for each cited id.
- **PE-4 checkout.** The served log of job 109558562779 shows the checkout fetching
  `+ad64b603b7a1dac18b7246d339abaf43a3642dd3` and `git log -1` printing that id.
- **PE-4 tree.** The real head's tree is the tree the row cites, `12a695df`.
- **PE-5 parent.** The real head's parent is `92a09a1c961dea73a95cbf91b2ca4f0c882f77f0`. That is the head the run and
  job records of run a (37492945459) name, the row on the line above the citing line.
- **On the host** (`git ls-remote`, 2026-10-17, 1238 refs):
  - the real heads of PE-1 to PE-4 are reachable from no ref;
  - PE-5's real head, and run a's, are reachable from the disposable branch `claude/twole-design`.

  A clone of `main` has none of the five.

## What holds

- **PE-1, PE-2, PE-4 and PE-5:** every content statement holds for the real heads, checked against their objects. So
  does every outcome statement, checked against the job records and the served logs.
- **PE-1 inference.** That the notation is outside the import closure is read from the single parse error at line 358,
  column 25 (`⋊[φ]`). It is consistent with PE-2, where adding the import makes the probe elaborate.
- **PE-4, the workflow.** "`D`'s with the frozen edit" is checked byte for byte:
  - the workflow blob `876f2e6d` is `D`'s `d9e372f1` with the five `(old, new)` replacements of `WORKFLOW_EDITS` in act
    45's `controls.py` applied, each anchor occurring once;
  - the preregistration lists `D`'s workflow blob `d9e372f1` at line 149 and freezes `controls.py` at blob `95ee78b2`
    at line 599; lines 46-49 describe the edit.
- **PE-4, the PDFs.** The page counts 87, 67 and 540 are derived facts: `pdfinfo` 24.02.0 on the three PDF blobs at the
  real head. E3 checks that those blobs are at their paths; the PDFs (2.7 MB) are not retained, so E3 does not check
  the counts.
- **PE-4, the durations.** 3 minutes 23 seconds and 11 seconds are the job records' start and completion times.
- **PE-5:**
  - the diff from run a's head is exactly the `variable` line: `Type*` over `AddCommGroup`/`Module` becomes `Type`
    over `NormedAddCommGroup`/`NormedSpace`;
  - the module carries ten `#print axioms` lines, and the served log reports each within
    `[propext, Classical.choice, Quot.sound]`;
  - all 32 jobs succeeded on the real head; the release gate passed with `lean-axioms` at 5753.
- **PE-3:** the run executed at its real head and failed with 41 errors.
  - Every error kind the row names occurred. The row's one "whnf timeout in the witness core" is two errors, at 272:0
    and 284:532.
  - The row's list is incomplete: at least seven errors are ones it does not account for:
    - a whnf timeout and a tactic timeout in `a35_shared_f4_flat` (74:10, 71:387);
    - a Hermitian orientation mismatch (237:43);
    - two function-expected errors on the two-argument diagonal field (236:65, 248:6);
    - the unsolved goals they leave (236:58, 245:329).
  - The row's count is confirmed: 52 theorem declarations were counted, and the module has 52 `#print axioms` lines.
    But 30 carry `sorryAx`: in run 36310787113, 30 of the 52 axiom reports list it. The evidence is job 108596164217,
    served text sha256 `8bcc3331…`, lines 522-3375. Their presence cannot be described as 52 established proofs.
  - The other 22 reports come from the same failed build:
    - 21 are within `[propext, Classical.choice, Quot.sound]`. One of them, `a35_shared_mod_core`, has an error inside
      its own declaration: 491:2, "No goals to be solved" (served line 1455), the line before its report (1456).
    - `a35_shared_wit_core` reports no axioms (served line 656). That report comes with its own two whnf timeouts:
      272:0 at the declaration (served line 651) and 284:532 (646).

  The failure verdict and the error count are confirmed; an exhaustive classification is not established.

## The retained objects

`objects/` holds the git objects E3 reads, 52 files, 444,060 bytes. Each file is a git object exactly as git hashes
it: the header `<type> <size>\0`, then the uncompressed body. The file's name is its id.

**Form: complete.** Each file is byte-identical to the host's object of that id, and E5 verifies every file by
its id. The objects are:
- **7 commits:**
  - the five real heads;
  - the two diff bases not on `main`: `28d9978b`, PE-3's parent, and `92a09a1c`, PE-5's parent and run a's head.
    PE-2's base is PE-1's real head.
- **37 trees:** those along each checked path and, for each diff, both sides' trees along the paths that differ. A
  `blob_at` check reads only the trees along its path.
- **8 blobs**, those whose contents a check reads:
  - `OrbitIsometryGroup.lean` at PE-1's and PE-2's heads;
  - `OIBridge.lean` at PE-1's;
  - `DitaHull.lean` at PE-3's;
  - `TrackBQfbBridge.lean` and the workflow at PE-4's;
  - `TwoSharpTests.lean` at PE-5's head and its parent.

The commits on `main` the checks compare with are read from the repository, which every clone of `main` has: PE-1's
parent `db82376d`, act 45's `D` `fa6ddf77` and its `E` `a5696e37`. `errata.json`'s `object_store` lists each object
with its type, its size and where the stored commits reach it.

**Public-repository scan (§A.42 item 4).** Every stored object was scanned before commit:
- **No match** for access keys, tokens, private keys, bearer or JWT strings, signed-URL parameters, credentials in URLs,
  secret assignments, or IPv4 and IPv6 addresses.
- **E-mail:** 21 matches, all `noreply@anthropic.com`, in the seven commits' author and committer lines and
  `Co-Authored-By` trailers.
- **Signatures:** seven `BEGIN SSH SIGNATURE` blocks, one per commit, each a public signature.
- **URLs:** each of the seven commit messages carries one `Claude-Session:` trailer, its only URL. All seven name the
  same claude.ai session link (`session_01XEQMD5kRhaU9WyeZt6dmM1`). It is a session link, not a credential, and 696
  commit messages on `main` at `66a981d5` carry the same trailer.

Commits on `main` carry the same address, signatures and trailer. No redaction was made, and none could be, since a redacted
object would no longer have its id.

## Dispositions and cross-references

`xref_census.py` searched every tracked text file at `66a981d5`, `.tex` included, for:
- each cited id;
- each real head;
- every prefix of either of 7 or more digits;
- each run id.

Each occurrence is classified as frozen, integrity-bound (the evidence-retention archive), mutable, or this directory.
The output is `census-66a981d5.json`.

- **Each cited id occurs once on `main`, at its own citing line.** No other prefix of a cited id or of a real head
  occurs anywhere, and no real head is named.
- **Every citing line is in a frozen record and stays byte-identical:**
  - PE-1 and PE-2 are in act 33's preregistration. That control-plane file is pinned by blob in
    `verification/receipts/A33.json`.
  - PE-4 is in act 45's preregistration, pinned in `verification/receipts/A45.json`.
  - PE-5 is in K1-SHARP-TESTS-1's preregistration, pinned by blob `bddfa340` in
    `verification/receipts/K1-SHARP-TESTS-1.json`.
  - PE-3 is in act 35's result note. At A35's receipt commit `cc8d2aed` it has the blob it has now.
  - All four files are inside record directories `G13` keeps. The receipt pins stay valid only while the bytes are
    unchanged.
- **Mutable dependents: none.** No summary, roadmap, manuscript, manifest or archive entry names any of the five.
- **Run ids without a head.** Each run id occurs only at its citing line, with one exception: run 36612901341 is also
  named, without a head, at two lines of act 45. Both hold for the real head:
  - `preregistration.md:402` states the run is evidence for the blobs it names and nothing else. Those blobs are in
    the real head's tree.
  - `result.md:53` states that the three `.tex` files rebuilt at stage 3 are byte-identical to those of the predicted
    tree. At A45's `E`, `papers/Main.tex`, `papers/Explainer.tex` and `book/The-Incompleteness-of-Observation-FULL.tex`
    have the blob ids they have in tree `12a695df`.

## How the five were found

`collision_scan.py COMMIT LISTING` compares hex tokens on `main` with the heads of the GitHub runs listing: all 2,200
runs, read 2026-10-16, sha256 `e4ce15ee…`, not committed. It runs two passes:
- **Same line.** On each line naming a listed run id, each hex token of 7 to 40 digits is compared with the heads of
  the runs the line names.
- **Corpus-wide.** Every hex token on every scanned line is compared with every listed head, whether or not the line
  names a run.

A token is a collision when it meets all three conditions:
- it is not a prefix of the head;
- it shares its first 7 hex digits with the head;
- it names no object in the clone the scan runs in.

The 40-hex columns are `--full-only`, which restricts tokens to 40 digits.

| | `fc5abade`, 40 hex | `fc5abade`, 7-40 hex | `66a981d5`, 40 hex | `66a981d5`, 7-40 hex |
| --- | --- | --- | --- | --- |
| Lines naming a listed run and a hex token | 138 | 308 | 209 | 396 |
| Tokens equal to the run's head | 114 | 114 | 185 | 185 |
| Tokens abbreviating the run's head | - | 142 | - | 155 |
| Prefix collisions | 4 (PE-1 to PE-4) | 5 | 4 (PE-1 to PE-4) | 5 |
| Other tokens (blobs, trees, other commits, job ids) | 85 | 275 | 85 | 279 |
| Corpus-wide collisions | | 5 | | 5 |

- **The same five at both commits.** The corpus-wide pass finds no other.
- **No cited run is outside the listing.** At both commits, every 11-digit decimal token that is not part of a
  decimal fraction is a listed run id.

## Checking

`python3 -I check_errata.py` checks the repository and `objects/`; its `CODES` table names every sub-code:
- **E0:** the ids are well formed.
- **E1:** the citing record.
  - Each citing file has its recorded blob at `HEAD` and the receipt's pin: a control-plane pin or, for a result note,
    the record directory at the receipt commit.
  - The cited line is the recorded verbatim line, with its sha256, and it names the run and the cited id.
- **E2:** each cited id is 7 to 40 hex digits, names no object, and is not the real head or a prefix of it. It shares
  at least its first 7 hex digits with the real head, the recorded number.
- **E3:** each real head's tree, parent and content checks.
  - These are read from `objects/` alone, and the commits on `main` from the repository, so E3 runs in a clone of
    `main`.
  - Every object read must be well formed and of the type its use requires.
  - Where the real heads are also in the repository, each check is repeated through git commands. The two routes must
    agree, and so must the stored objects and the repository's.
- **E4:** the README and the outcome records.
  - The entry ids are the ids the checker pins, `PE-1` to `PE-5` in order, so removing an entry from `errata.json`
    and the README alike still fails.
  - Each README row is parsed and compared cell by cell with `errata.json`.
  - The ids and the rows are in bijection, and their number is `expected_count`, which is the pinned count.
  - Verdicts and explanations are in their vocabularies, each status follows by the rule, and the outcome records are
    well formed.
- **E5:** each stored file hashes to its name, the manifest lists exactly the files, and every stored object is read
  by some check.

**Verdicts.**
- **HOLDS** (exit 0): nothing fails and nothing is unchecked.
- **UNCHECKED** (exit 2): an object a check needs is neither stored nor on `main`. `--require-objects` makes that a
  failure.
- **FAILS** (exit 1): anything else.

`--self-test` applies at least one mutation for each place in the checker that reports a failure, and each mutation
must be caught by its own sub-code. It also requires that a missing blob, or a missing real-head commit, leaves the
verdict UNCHECKED with a nonzero exit. The git cross-check's mutation runs only where the real heads are present.

## Not retained here

- **Job conclusions, job times and served-log facts.** These are host records read through the API on 2026-10-16/17.
  They are given in `errata.json` with job ids and the sha256 of the served text each fact was read from.
- **The served text itself.** It is a tail of at most 5000 lines, not the original log, and is not committed.
- **The runs listing and the ref listing.** These are host records, given by digest.
- **PE-4's PDF blobs.** Their page counts are derived facts.

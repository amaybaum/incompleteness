# Provenance errata: cited run heads that name no commit

Four frozen records cite a CI run's head commit by a 40-hex id that names no object. In each case the run executed
at its real head, which the host's run and job records name and which shares the cited id's first 8 hex digits.
The errors are of attribution, not of execution. The records keep their bytes (AGENTS §A.42 item 4), and this table
is the correction. A correction of a frozen record's own text is a new native round's (`G13`).

| id | location | run, attempt | cited head | verified head | verdict | explanation | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PE-1 | verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/preregistration.md:710 | 36257341185, 1 | `4c4155da7ccc2cf47d63bfe2ce7d8c4cba7f0ff2` | `4c4155da059388a4724039fd5e60aaa96965f7c3` | confirmed | confirmed | holds |
| PE-2 | verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/preregistration.md:711 | 36257659584, 1 | `cff3c1560f4c0fc09aba2c8af06e9f00e0fc0cd7` | `cff3c1566228158acbf6cb710dbdf4ba4c5db91f` | confirmed | confirmed | holds |
| PE-3 | verification/programmes/oi-qm/track-b/act-35-dita-hull/result.md:218 | 36310787113, 1 | `2ae4dbeef5d9a1c9f0fcf3fbbf1ceaf4de4d3a0d` | `2ae4dbeeceae2b2e66bd43658045b67da0f0e650` | confirmed | incomplete | partly holds |
| PE-4 | verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/preregistration.md:400 | 36612901341, 1 | `ad64b60319e1ff2d40a5a5eed8e3aa4bfcf30b0e` | `ad64b603b7a1dac18b7246d339abaf43a3642dd3` | confirmed | confirmed | holds |

**How to read the columns:**
- **Verdict** is the row's outcome: what the run's jobs concluded.
- **Explanation** is the row's account of that outcome: its counts, causes and listed kinds.
- **Status** combines the two.
- **Every run** is a `workflow_dispatch` of `.github/workflows/verify.yml`.
- **`errata.json`** gives, for each entry, the original assertion in full, the content checks, the outcome evidence, the disposition and the cross-references.

## The rows

None is a designated `F` or `E`, and none is a certification:
- **PE-1 and PE-2** are act 33's elaboration runs, design evidence in its preregistration before `F`.
- **PE-3** is a failed first proof pass on act 35's development branch, in its result note's design history.
- **PE-4** is act 45's predicted-tree run, design evidence in its preregistration before `F` that the predicted execution tree is green.

## Which commit each run tested

- **Host records.** The run's `head_sha` in the runs listing, and every job's `head_sha` in the jobs listing, equal the verified head; none equals the cited id. GitHub's commit endpoint answers "No commit found" for each cited id.
- **PE-4 checkout.** The served log of job 109558562779 shows the checkout fetching `+ad64b603b7a1dac18b7246d339abaf43a3642dd3` and `git log -1` printing that id.
- **PE-4 tree.** The verified head's tree is the tree the row cites, `12a695df`, and the 13 blobs the row names are in it at their paths.

## What holds

- **PE-1, PE-2 and PE-4:** every content statement holds for the verified heads, checked against the commits' objects. So does every outcome statement, checked against the job records and the served logs.
- **PE-1 inference.** That the notation is outside the import closure is read from the single parse error at line 358, column 25 (`⋊[φ]`). It is consistent with PE-2, where adding the import makes the probe elaborate.
- **PE-3:** the run executed at its verified GitHub head and failed with 41 errors. Every error category named in the original record occurred. However, the category list is incomplete: at least seven errors belong to additional categories:
  - two timeouts in `a35_shared_f4_flat`;
  - a Hermitian orientation mismatch;
  - two function-expected errors on the two-argument diagonal field;
  - the unsolved goals they leave.

  The failure verdict and error count are confirmed; an exhaustive classification is not established. The module's 52 theorems hold as stated.

## Dispositions and cross-references

`xref_census.py` searched every tracked text file at `66a981d5` for:
- each cited id;
- each verified head;
- every 7- to 39-digit prefix of either;
- each run id.

Each occurrence is classified as frozen, integrity-bound (the evidence-retention archive), mutable, or this directory. The output is `census-66a981d5.json`.

- **Each cited id occurs once on `main`, at its own citing line.** No prefix of a cited id or of a verified head occurs anywhere, and no verified head is named.
- **Every citing line is in a frozen record and stays byte-identical:**
  - PE-1 and PE-2 are in act 33's preregistration. That control-plane file is pinned by blob in `verification/receipts/A33.json`.
  - PE-4 is in act 45's preregistration, pinned in `verification/receipts/A45.json`.
  - PE-3 is in act 35's record directory.
  - All three files are inside record directories `G13` keeps. The receipt pins stay valid only while the bytes are unchanged.
- **Mutable dependents: none.** No summary, roadmap, manuscript, manifest or archive entry names any of the four.
- **Run ids without a head.** Each run id occurs only at its citing line, with one exception: run 36612901341 is also named, without a head, at two lines of act 45. Both hold for the verified head:
  - `preregistration.md:402` states the run is evidence for the blobs it names and nothing else. Those blobs are in the verified head's tree.
  - `result.md:53` states the three `.tex` rebuilt at stage 3 are byte-identical to those of the predicted tree. At A45's `E`, `papers/Main.tex`, `papers/Explainer.tex` and `book/The-Incompleteness-of-Observation-FULL.tex` have the blob ids they have in tree `12a695df`.

## How the four were found

Every line on `main` naming a listed run id and a 40-hex token was compared with that run's head in the runs listing. At `fc5abade`:

| | Count |
| --- | --- |
| Such lines | 138 |
| Tokens equal to the run's head | 114 |
| Prefix collisions (these four) | 4 |
| Other tokens (blobs, trees and other commits on the same lines) | 85 |

At `66a981d5` the same four are the only collisions.

## Checking

`python3 -I check_errata.py` checks, from the repository:
- **E1:** each citing record still has its pinned blob and the cited line.
- **E2:** each cited id names no object and is a prefix collision with the verified head.
- **E3:** each verified head has its recorded tree and parent, and its content checks hold.
- **E4:** the table here matches `errata.json`.

The verified heads are reachable from no ref on the host, so a clone of `main` lacks them. E3 then reports `NOT CHECKABLE HERE` until the commits are restored from the preservation bundles, and `--require-objects` makes that a failure.

`--self-test` mutates the table once per check and requires each failure. Its E3 mutations run only where the objects are present.

## Not retained here

- **Job conclusions and served log facts.** These are host records read through the API on 2026-10-16/17. They are given in `errata.json` with job ids and the sha256 of the served text each fact was read from.
- **The served text itself.** It is a tail of at most 5000 lines, not the original log, and is not committed.

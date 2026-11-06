# introduction-repro-ext — the staged 28-module expected result, retained as historical evidence

**Status.** The 28-module result in this directory supports no manuscript claim and is not an accepted
result. An independent review, recorded in `../unit5-evidence/`, re-compares each of the 248 reports of
its 14 added modules, by module and fully qualified name, with the pinned historical log of job
121598983127, the archived fresh-build log of run 40457712855, the source at `17b830bc` and this file,
and finds no mismatch. It classifies the 14 added entries as independently audited historical evidence;
no fresh reproduction is claimed. That review's acceptance is pending on #941, which remains the
accountable Issue. Retaining the result here is not scientific acceptance: it promotes nothing and
strengthens no claim (AGENTS.md §A.42 item 6; §A.46 items 1, 3, 4 and 7).

Retained under the owner decision on #941 (comment 6658967061, Option (b), 2026-11-05), which
responds to the proposal in comment 6658728711 of the same Issue.

## What the file is

`results-121598983127-28.json` is byte-identical to git blob
`97a2377dbfc30987887dffea2b72e423feed079d`, the file
`papers/introduction_repro/results-121598983127.json` at commit
`e73f7be3c343ce12c5f64b9dc1485a5a7ba5498c` on branch `staging/introduction-repro-ext-20261027`.
`git hash-object` on it returns that id.

It is an `oi-evidence-result` (version 1, kind `bridge`), read from the log of job 121598983127
("Mathlib bridge", run 40330683786, `verify.yml`, at `17b830bcd0ecc36e10eff5b9eeca03bdd7198d86`).
It extends the 14-module expected result on `main`, `papers/introduction_repro/results-121598983127.json`
(blob `61cfd6ea2df4590cc2ff86f90fc8f50ab71201f7`), to 28 modules and 534 `#print axioms` reports:

- every field other than `expected.modules` is identical in the two files, and the 14 module
  entries they share are identical entry for entry;
- the 14 added modules, each under `OIBridge/` with a `.lean` suffix, are `CanonicalMeasure`,
  `CausalReadback`, `FiniteEntropy`, `FrozenSourcing`, `OIRealization`, `OperationalAssembly`,
  `PhaseSource`, `PhysicalC4StorageReadback`, `QuantumRepresentationT2`, `ReadWriteControl`,
  `RootedClassification`, `RootedClassificationAllTime`, `StructuralClosure` and
  `SubstratumInterface`.

The file is named `-28` here so that it is not confused with the 14-module file of the same job.

## Recipe

The file's own `reproduce.recipe` is the recipe. It checks out
`17b830bcd0ecc36e10eff5b9eeca03bdd7198d86`, builds `verification/lean-mathlib`, runs
`tools/release_gate.py`, and extracts and compares the result with the frozen evidence-retention
extractor and comparator read from `48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29`. Both commits are
reachable from `main`. The recipe names `<this results.json>` rather than a path, so it applies
unchanged to this copy. The comparison is expected to print `REPRODUCTION HOLDS`; that has not been
established from `main` (see Status).

## Provenance (§A.42 item 8)

| Reference | Off `main` | Classification |
| --- | --- | --- |
| `24e70304a6b94e0e3150e6b0eb5167fa312b52ae` (staging branch; introduced the blob) | yes | provenance: no claim here uses its content beyond the blob retained in this directory |
| `e73f7be3c343ce12c5f64b9dc1485a5a7ba5498c` (staging branch; the blob unchanged, README corrections) | yes | provenance, as above |
| #942 comment 6434184021: an author-posted report of an independent review of the staged result (ACCEPT WITH CHANGES) | yes | provenance only; no review report is on `main` |
| #942 comment 6435469998: an author-posted report of a fresh-build replay, run 40457712855, comparing against this blob | yes | provenance only; a CI run is not verification from `main` (§A.42 item 2; §A.46 item 7) |
| job 121598983127, run 40330683786 (the extracted log) | yes | provenance of the extraction; the log is not retained |
| `17b830bc…`, `48b18ac5…` (recipe commit and tools) | no | support on `main` for the recipe only |

## Relation to `.github/workflows/evidence-replay.yml`

The workflow's `EXPECTED_28` pin is `2714278a7dd9057a73610658478661065152ca97`, the commit that adds
this directory, reachable from `main`. The workflow checks that `results-121598983127-28.json` there is
blob `97a2377d…` and reads the expected result by that id, so the replay does not depend on the staging
branch. The pin preserves the evidence and verifies nothing (see Status). The staging branch is kept
unchanged, and none of its history is merged into `main`.

## Remediation route

The owner's standard for this result is CI evidence plus an independent re-comparison, with no new
full Lean build (#1031 comment 6678672357, section 3). The review in `../unit5-evidence/` is that
re-comparison; the result is independently audited historical evidence once the review is accepted on
#941. A fresh reproduction needs a fresh build, which is a separately authorized step.

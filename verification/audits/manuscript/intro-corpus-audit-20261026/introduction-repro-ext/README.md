# introduction-repro-ext — the staged 28-module expected result, retained unreviewed

**Status.** The 28-module result in this directory is **not independently verified on `main`**.
It supports no manuscript claim and is not an accepted result. Retaining it here is not scientific
acceptance: it promotes nothing and strengthens no claim (AGENTS.md §A.42 item 6; §A.46 items 1, 3,
4 and 7). The accountable Issue is #941.

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

The workflow's `EXPECTED_28` pin (`e73f7be3…`, blob `97a2377d…`) is unchanged. It still reads the
blob through that commit, which is reachable only from the staging branch. This record does not make
the pin durable; that dependency is a separate unresolved issue tracked on #941. The staging branch is
kept unchanged, and none of its history is merged into `main`.

## Remediation route

The result becomes verified only by meeting §A.46 item 1, for example by an independent review
recorded on `main` that re-derives the 14 added entries, or by a reproduction from `main` whose
per-comparison outcome is a structured signal (§A.44). Each step needs its own owner authorization.

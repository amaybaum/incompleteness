# KTOKEN-MAXCONE-1 (#829): evidence extraction for the two design runs

**Where things are.** The two design runs' expected results were extracted in CI and hold every acceptance check below.
They are committed at `evidence/run1-39043849411.json` and `evidence/run2.json`. The preregistration's pins are
still pending: filling them makes the reviewed checker's self-test fail (see "Pins and the checker"). `F` is not
designated.

## The extraction run

- Workflow: `KTOKEN-MAXCONE-1 evidence extraction (read-only)` on the parentless branch
  `tmp/ktoken-evidence-20261017` at `0d94937d4d8dbc6662b4464842bcdb1523ede18e` (tree `cd75be74`).
- Before the push, an independent review covered `ba3f0804`, `f0e1dbd5` and `0d94937d`; it passed at
  `0d94937d`.
- After the push, the remote commit, tree and all four file blobs matched the reviewed objects:

  | file | blob |
  |---|---|
  | `.github/workflows/ktoken-evidence.yml` | `d117e466` |
  | `extractor/assemble_evidence.py` | `30d96134` |
  | `extractor/download_job_logs.py` | `d32d6392` |
  | `extractor/fetch_records.py` | `976e95c4` |
- The single push started exactly one run, [39063510375](https://github.com/amaybaum/incompleteness/actions/runs/39063510375).
  It ran job 117486234075, which concluded `success` on 2026-10-17 at 19:41Z.
- The job's log, 4,037 lines, was read in full.
- Its self-tests passed: fetch 23/23, download 37/37 and assemble 67/67.

## Acceptance checks

| check | observed | holds |
|---|---|---|
| final line | `EXTRACT HOLDS`, exactly | yes |
| both results hold | `RESULT run1 … HOLDS (57 checks, 0 failed)`, `RESULT run2 … HOLDS (60 checks, 0 failed)` | yes |
| no failing check | 117 `CHECK` lines, all `ok` | yes |
| cross-checks | all four `CROSSCHECK` lines `equal`: jobs 117428550018 (41,715 lines), 117428550439 (173), 117466847042 (41,728), 117466847062 (223); each tail equals the text read in-session | yes |
| digests | each block, with timestamps stripped and a final newline added, recomputes to its printed SHA256 | yes |
| identities | run 1: commit `1ab0fd9d…`, run 39043849411, bridge job 117428550018, probe job 117428550439. Run 2: commit `6959ced4…`, run 39056982958, bridge job 117466847042, probe job 117466847062 | yes |
| sources | extractor `05c41bce` (main `b96662e6`), assembler `30d96134`, downloader `d32d6392`; both module sources identical across the runs (`OIBridge.lean` `93c89b36`, `OIBridge/KTokenMaxCone.lean` `14bb9fc0`) | yes |
| gate | 22 of 22 steps `PASS`, verdict `PASS`, in both runs | yes |
| reports | `OIBridge.lean` 19 of 19 and `OIBridge/KTokenMaxCone.lean` 68 of 68, complete, within `propext`, `Classical.choice` and `Quot.sound`; markers `sorryAx`, `declaration uses 'sorry'`, `Lean.ofReduceBool` and `error:` all 0 | yes |
| A3 | `A3-CHECK-NONVACUOUS: 13 cases as expected` in both runs | yes |
| probe | `checks 3196`, failures 0, 5 mutations rejected and 0 accepted, `VERDICT KTOKEN-K3-EXACT`, in both runs | yes |
| controls | run 1: not applicable (its tree has no `controls.py`); run 2: `controls: OK (0 failure(s))`, `38 self-checks ran, as frozen (38)` | yes |

The A3 block counts 12 `error:` lines. These are the deliberately broken mutation cases failing to compile, which A3
requires; the extractor reads them inside A3's case ranges and they are not failure markers of the build.

## The evidence files

| path | sha256 |
| --- | --- |
| `evidence/run1-39043849411.json` | `4e6303690387740559e4e37ca35037722f22c45a0b3da311365be06ca3be9b5c` |
| `evidence/run2.json` | `bc896c46a7ea528cc9010ac124a3c12866ec4b32669ddbd73dea016f47cd2a53` |

Each file is a §A.42 structured expected result. It names its commit, run, jobs, recipe and source digests, and it
contains no log text. The values the extractor checked against came from the run-2 draft preregistration and
`controls.py` `8c8eb522`, not from #829's PR head `625f853f`. For run 1, the probe count of 3196 is a consistency
check, not a prediction.

What this establishes: what these two design runs logged, at those two commits. It is design evidence for the proposed
execution tree, not a `check-run` attestation of `F` or `E`.

## Pins and the checker

Filling the two pins in the preregistration makes the reviewed `controls.py` (`8c8eb522`) fail its own self-test. Its
end-to-end fixture writes synthetic evidence files and fills only pins that are still `pending`, so with real digests
pinned, its unmutated case fails P. Both pins therefore stay pending, and `controls.py` is unchanged.

A proposed fix, `controls-fixture-fix.diff` in this folder, is not applied and needs review. It changes only the
fixture: when a pin is filled, it uses the real retained file, and if that file is absent, P fails. Applying it gives
`controls.py` the blob `904c1e700586d008b54078b2cf03f9b7a021a9b5`, so the preregistration's frozen-blob pin for
`controls.py` moves with it. Local self-test results on the run-2 tree, with that pin moved:

| mode | result |
|---|---|
| pins filled, real files present | `controls: OK (0 failure(s))`, 38 self-checks |
| pins pending, as reviewed | `controls: OK (0 failure(s))`, 38 self-checks |
| pins filled, `run2.json` altered | `controls: FAILED`, P |
| pins filled, `run1-39043849411.json` absent | `controls: FAILED`, P, no traceback |

## Still open before F

- Review of the fixture fix; then filling the pins and moving the `controls.py` pin.
- Retaining both heads, `1ab0fd9d` and `6959ced4`, under main's off-main object mechanism. This is being prepared in
  the evidence-retention change, which has not been pushed.
- Bringing #829's PR head up to the revised preregistration, and finalizing `D`.

Until then, `dev-equivalence/ktoken-maxcone` (`1ab0fd9d`) and `dev-equivalence/ktoken-maxcone-r2` (`6959ced4`) stay
in place.

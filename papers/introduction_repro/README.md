# introduction_repro — expected result of the Lean 4/Mathlib check for "Observational Incompleteness"

`results-121598983127.json` is the expected result behind the paper's statement that the declarations
of its Appendix A are machine-checked in Lean 4/Mathlib. It uses the `oi-evidence-result` schema
(version 1, kind `bridge`) of the evidence-retention archive, which is frozen at
`48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29` and read from `main`'s history (AGENTS.md §A.42). The
result is `derived`: it was read from a named job log by that archive's extractor, and the log's
digest is recorded.

## What it holds at

| item | value |
| --- | --- |
| commit | `17b830bcd0ecc36e10eff5b9eeca03bdd7198d86` (`main`, merge of #936) |
| Lean sources | `verification/lean` tree `277d2822cca09f9e1ad41459b9e9fe385dcbe9e1` and `verification/lean-mathlib` tree `8624ba39ada139201b5939084b74613250d24471`. Both are identical at `687e885b1cfd24d6f17eee439101afc8acf07015` (`git diff --stat 687e885b 17b830bc -- verification/lean verification/lean-mathlib` is empty), so Appendix A's line numbers hold at both commits |
| run | `40330683786`: workflow `verify` (`.github/workflows/verify.yml`), event `push`, attempt 1, conclusion `success` |
| job | `121598983127`, "Mathlib bridge", conclusion `success` (steps Build and Release gate `success`) |
| toolchain of the check | `verification/lean-mathlib/lean-toolchain` = `leanprover/lean4:v4.33.0`. The job printed `Lean (version 4.33.0, x86_64-unknown-linux-gnu, commit d8b18978322de05a8f3dba51ef03cf5461676c17, Release)` |
| Mathlib | `lakefile.toml` requires `mathlib` at `rev = "v4.33.0"` (a tag). No `lake-manifest.json` is committed, so lake resolved it in the job: `mathlib: checking out revision 'db584cd6d46c92f209a44c0f1c829460d327499d'` |
| Mathlib's dependencies, as resolved in the job | plausible `b7eb3304aeae834b12dda98993a37f6a41f6f0bb`, LeanSearchClient `5f4d51b81cbd3f6b32b156bfad9056621a040404`, importGraph `16f02aa7642864af59f1ff0e384a015994db9118`, proofwidgets `4be2e3d5087eeb272cf5a8853b8f9dd025ef5957`, aesop `3448c0bcc5ce01b2d1546e483ec3620e32df3d0e`, Qq `92c15be17b7caf78c2ad767ec40f89052d908d81`, batteries `4488d40d070b9700d4d5a6aa342f0d40c31b2a2d`, Cli `6130a47896ce867c6a4a55373441e59e565bad0f` |

The run's other Lean job, "Lean kernel check" (job `121598983232`, `success`), checks only the six
zero-import files in `verification/lean`. It installs `leanprover/lean4:stable`, which resolved to
`Lean (version 4.35.0, …, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Release)`. That is not
the toolchain that checked the Appendix A declarations.

## The commands that produced it

From `verify.yml` at the commit, job "Mathlib bridge", after a full-history checkout, elan installed
with `--default-toolchain none`, and a restore of `verification/lean-mathlib/.lake/build` from the
Actions cache:

```
# step "Build", in verification/lean-mathlib (timing lines omitted)
lean --version
lake exe cache get
lake --rehash build
# step "Release gate", at the repository root
python3 tools/release_gate.py
```

The gate's `lean-axioms` step runs `python3 tools/lean_axiom_check.py --require-lake`. That check runs
`lake build` again in `verification/lean-mathlib` and fails if a report mentions `sorryAx`, if an
axiom lies outside `propext`, `Classical.choice` and `Quot.sound`, or if a `#print axioms` command
produced no report.

## What it records

- **Build:** success (`Build completed successfully (3656 jobs).`).
- **Release gate:** `PASS  (note: --label bNNN not given, so the baseline check ran in relative mode only)`.
  All 22 steps pass: toolchain, staleness, baseline-label, voice, voice-scope, ci-gate-presence,
  artifact-placement, manifest-drift, claims, duplicate, mirror, citation, architecture,
  dependency-label, coverage, lean-axioms (`6082 named result(s) reported`), lean-manuscript,
  legacy-records, v3-self-test, v3-corpus, v3-receipts and citation-roles. Each summary is recorded
  as the gate printed it.
- **Failure markers** in the build and gate output: `sorryAx` 0, `Lean.ofReduceBool` 0,
  `declaration uses 'sorry'` 0, `error:` 0.
- **Modules:** the 14 modules that contain an Appendix A declaration, each `complete`: every
  `#print axioms` command in the module's source has exactly one report. There are 286 reports in
  all. 285 depend on `propext, Classical.choice, Quot.sound`; one, `OIBridge.PhysicalCharacterization.levelOne_eq`,
  which the paper does not cite, depends on `propext` alone.

### The 28 declarations of Appendix A

Each has exactly one report, and each report is `[propext, Classical.choice, Quot.sound]`, as
printed. "Decl." is the declaration's line, as Appendix A gives it. "Print" is the line of its
`#print axioms` command, which is where lake reports it.

| declaration (as reported) | decl. | print | axioms |
| --- | --- | --- | --- |
| `OIBridge.Equivalence.finite_horizon_equivalence` | Equivalence:462 | 480 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.Equivalence.S_imp_D` | Equivalence:422 | 479 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.Equivalence.D_imp_Qfb` | Equivalence:294 | 475 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.Equivalence.Qfb_imp_S` | Equivalence:245 | 474 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.EquivalenceChain.permMatrix_mem_unitaryGroup` | EquivalenceChain:179 | 392 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.HiddenMemory.pushforward_identity` | HiddenMemory:83 | 197 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.HiddenMemory.distinguishability_floor` | HiddenMemory:114 | 199 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.HiddenMemory.capacity_floor` | HiddenMemory:170 | 201 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.HiddenMemory.unavoidable_hidden_predictive_memory` | HiddenMemory:185 | 202 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.C3.c3_necessity` | C3Necessity:80 | 140 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.C3.card_hidden_ge_two_pow_Istar` | C3Necessity:117 | 143 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.EquivalenceChain.isPermMatrix_of_stochastic_inverse` | EquivalenceChain:110 | 391 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.RecurrenceHorizon.pIndivisible_of_rooted_identity_return_of_overlap` | RecurrenceHorizon:148 | 190 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.PhysicalC4Discharge.routed_forces_indivisible_somewhere` | PhysicalC4Discharge:122 | 668 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.CoherentLiftGauge.gl2_strong_gauge_moves_relative_candidate` | CoherentLiftGauge:537 | 758 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.CoherentLiftGauge.gl3_constant_gauge_preserves_relative` | CoherentLiftGauge:451 | 754 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.TrackBQfbBridge.bridge_traj` | TrackBQfbBridge:276 | 282 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.TrackBQfbBridge.rooted_eq_iff_slice_eq` | TrackBQfbBridge:180 | 192 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.TrackBQfbBridge.realData_traj_stochastic` | TrackBQfbBridge:286 | 292 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.GeneralCarrier.exactAll_iff_physical_general` | GeneralCarrier:100 | 221 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.PhysicalCharacterization.physical_of_exactAll` | PhysicalCharacterization:301 | 597 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.GeneralCarrier.exactAll_of_physical_general` | GeneralCarrier:93 | 220 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.OperationalValidity.krausSoundExt_of_validity_inert` | OperationalValidity:124 | 242 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.IsometryExtension.compositeCompleteness_unconditional` | IsometryExtension:179 | 294 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.IsometryExtension.finiteIsometryExtensionSF_discharged` | IsometryExtension:116 | 288 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.LevelOneSeam.exactAll_of_levelOne` | LevelOneSeam:196 | 407 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.RankGapTheory.five_way_minimality` | RankGapTheory:702 | 777 | `propext, Classical.choice, Quot.sound` |
| `OIBridge.GeneralCarrier.oi_alone_not_qm` | GeneralCarrier:160 | 227 | `propext, Classical.choice, Quot.sound` |

The "compositions :466–468" that Appendix A names under Theorem 1 are the proof term of
`finite_horizon_equivalence`, not separate declarations; they are covered by its report.

## Provenance

- **Source text.** The job log was read whole through the REST API (`actions/jobs/121598983127/logs`) on
  2026-10-26. It has 43064 lines (sha256 `bc2291bc57d952779f27282211b588321618bf503d39d192840c777074cd0c81`).
  The extractor read its lines 1–38918: job set-up through the Release gate step, ending at the
  gate's verdict line. That text has sha256 `1a83921fb967dad82785ce79b06013f184f4a82e377e39cad21ab4df453e09df`
  (`source.served_sha256`), counting lines by splitting on newline characters as the archive does.
  The cut leaves out the later steps of the job (KTOKEN-MAXCONE-1, PRESERVE-INDUCT-1 and KTRANS-SEP-2).
  They are not part of the recipe, and their deliberate mutation errors and second partial build
  would otherwise enter the marker counts and the reports. The job-log tool's served tail agrees with
  the API text: the same last lines, and `original_length` 43064.
- **Extractor.** `verification/audits/evidence-retention/extract_result.py` at `48b18ac5`
  (blob `e6f69713bfffd1f1f9aca3c27bf26a689c994167`).
- **The build in this job was a replay.** The job restored `.lake/build` from the Actions cache
  (an exact key hit), and lake printed `Replayed` for each of the 226 `OIBridge` modules: it did not
  re-elaborate them in this job. `--rehash` re-hashes the checked-out sources against the restored
  traces, so a replayed report belongs to the source at the commit. The reports are the messages
  that an earlier elaboration of the same sources logged. Reproduction by the recipe below starts
  from an empty `.lake/build`, so it elaborates all 226 `OIBridge` modules afresh; `lake exe cache get`
  still fetches Mathlib's prebuilt files.
- **Not recorded.** Timestamps, durations, cache keys and job counts are not part of the expected
  result. They appear only under `observed`, as provenance, and are not compared.
- **Secrets.** The log and this file were scanned with the archive's R5 patterns (tokens, keys,
  signed-URL parameters, IPv4 and e-mail addresses). There were no matches. The log shows only
  GitHub's masked values (`token: ***`, `AUTHORIZATION: basic ***`). No raw log is retained.

## Reproducing it

Run from the root of a full-history clone. It needs elan (which installs the toolchain named in
`verification/lean-mathlib/lean-toolchain`), python3, and network access for lake to fetch Mathlib and its
prebuilt cache. `<dir>` is a new directory, `<tools>` a new directory outside it, and `<log>` a file
outside both. These are the steps of the file's `reproduce.recipe`:

```
git worktree add --detach <dir> 17b830bcd0ecc36e10eff5b9eeca03bdd7198d86
mkdir <tools>
git show 48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29:verification/audits/evidence-retention/extract_result.py > <tools>/extract_result.py
git show 48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29:verification/audits/evidence-retention/compare_result.py > <tools>/compare_result.py
(cd <dir>/verification/lean-mathlib && lean --version && lake exe cache get && lake --rehash build) > <log> 2>&1
(cd <dir> && python3 tools/release_gate.py) >> <log> 2>&1
python3 -I <tools>/extract_result.py <log> > reproduced.json
python3 -I <tools>/compare_result.py papers/introduction_repro/results-121598983127.json reproduced.json --tree <dir>
```

The comparison fails closed. It requires a successful build; the gate's verdict and each of the 22
steps with its status and summary; for each of the 14 modules, one report for every `#print axioms`
line of its source at the commit and no other, each with exactly the recorded axioms; and no
failure marker.

## Checks run on this file

These were run on a scratch copy with the archive's tools from `48b18ac5`; no repository file was changed.

- `check_retention.py`'s R4 (`check_results`): no failure. Six mutations are each caught under their
  own message: no build, a report removed, a wrong count, a marker missing, a short head id and no recipe.
- R8 (`check_entry_files`), with `run.json` and `jobs.json` derived from the runs and jobs API
  answers: no failure.
- `compare_result.py --self-test results-121598983127.json`: 31 cases, all pass.
- `compare_result.compare`, run on the file against the extractor's reading of the same text and the
  module sources at `17b830bc`, finds no failure. This is a consistency check, not a reproduction.
  Five countercontrols are each caught: `sorryAx` in a report of `GeneralCarrier`, the
  `finite_horizon_equivalence` report dropped, a failing gate verdict, a changed `lean-axioms` count,
  and an extra `#print axioms` in a source.
- `extract_result.check` against the 14 sources: no failure, no gap.

## Location

This package sits beside the paper it serves, as `papers/main_repro/` does for `papers/Main.md` (AGENTS.md §A.42
item 1: the result to expect, in a small structured file beside the record). The file keeps the archive's name for an
expected result, `results-<job>.json`. It is not added to the frozen evidence-retention archive, which left the tree
at `5c4e5087` and is read only from history.

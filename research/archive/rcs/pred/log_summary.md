# Job log summary: "Mathlib bridge", job 113130207703

Repository `amaybaum/incompleteness`, workflow `verify`, run 37721579646 (attempt 1), branch `claude/relc-select-predicted`, head `da295a1be51e7d7e2013307b85b0c5f44a9c897a`.
The job API reports status `completed` and conclusion `success`.

Every count below was computed by `/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/rcs/scripts/summarize.py` over the saved files. `Lnnnn` is a line number within `raw.log`, which holds the returned window. It is not a line number in the full job log. In quoted blocks, the `Lnnnn  ` prefix is added and the rest of each line is verbatim, timestamp included. An ESC character is shown as `\x1b`.

**Files** (all in `/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/rcs/pred/`):

- `raw.log` holds the `logs_content` field of the `get_job_logs` response, decoded from its JSON envelope and written unchanged: 430780 bytes, 5000 lines, no trailing newline, sha256 `bdca13bd2cbc72d40897bf05934724b4897251a99c84e919a3ff0a11f3526074`.
- `raw_tool_response.json` is the tool's response envelope, byte for byte (sha256 `0d8fd983fa004b6580ddf3d6f8d49e46cee2485913c567464828d20f7367953f`). Its `["logs_content"]` decodes to exactly `raw.log`.
- `job_api.json` holds the output of `gh api repos/amaybaum/incompleteness/actions/jobs/113130207703`.

Job steps, from `job_api.json`:

| # | Step | Conclusion | Started | Completed |
|---|---|---|---|---|
| 1 | Set up job | success | 2026-10-08T03:12:05Z | 2026-10-08T03:12:05Z |
| 2 | Run actions/checkout@v4 | success | 2026-10-08T03:12:05Z | 2026-10-08T03:12:21Z |
| 3 | Install elan | success | 2026-10-08T03:12:21Z | 2026-10-08T03:12:22Z |
| 4 | Restore the OIBridge build cache | success | 2026-10-08T03:12:22Z | 2026-10-08T03:12:26Z |
| 5 | Build | success | 2026-10-08T03:12:26Z | 2026-10-08T03:14:57Z |
| 6 | Release gate | success | 2026-10-08T03:14:57Z | 2026-10-08T03:15:36Z |
| 11 | Post Restore the OIBridge build cache | success | 2026-10-08T03:15:36Z | 2026-10-08T03:15:40Z |
| 12 | Post Run actions/checkout@v4 | success | 2026-10-08T03:15:40Z | 2026-10-08T03:15:41Z |
| 13 | Complete job | success | 2026-10-08T03:15:41Z | 2026-10-08T03:15:41Z |

## 0. Coverage

| | |
|---|---|
| `original_length` reported by the tool | 37327 |
| Lines returned | 5000 (4999 newline characters, no trailing newline; 0 lines lack a leading timestamp) |
| Position in the full log | the last 5000 lines, i.e. lines 32328–37327 of 37327 (about 13.4% of the log). `original_length` must be a line count: the 430562 characters returned already exceed 37327, so it cannot be a character count. |
| First timestamp (L1) | `2026-10-08T03:14:34.5764044Z` |
| Last timestamp (L5000) | `2026-10-08T03:15:41.0694039Z` |

The window opens inside the Build step (2026-10-08T03:12:26Z to 2026-10-08T03:14:57Z per the job API), partway through the diagnostics of `OIBridge.DitaTorusLocus`. Lines L1 to L4752 hold 854 diagnostics, all from `OIBridge/DitaTorusLocus.lean`; that module's own build-progress line comes before the window. The window then runs through the end of the build, the whole Release gate step and post-job cleanup.

Build-progress `[k/n]` lines in the window: 9, from `[3634/3643]` to `[3642/3643]`:

```text
L4753  2026-10-08T03:14:34.6694849Z ℹ [3634/3643] Replayed OIBridge.TrackBQfbBridge
L4781  2026-10-08T03:14:34.6707580Z ℹ [3635/3643] Replayed OIBridge.ProductAdmission
L4788  2026-10-08T03:14:34.6710826Z ⚠ [3636/3643] Replayed OIBridge.ProductStrictLift
L4829  2026-10-08T03:14:34.6726025Z ℹ [3637/3643] Replayed OIBridge.ProductOffLocusUniqueness
L4835  2026-10-08T03:14:43.3770205Z ℹ [3638/3643] Built OIBridge.RelcSelectParity (9.6s)
L4838  2026-10-08T03:14:48.2870210Z ℹ [3639/3643] Built OIBridge.RelcSelectSqueeze (14s)
L4854  2026-10-08T03:14:48.5880574Z ℹ [3640/3643] Built OIBridge.RelcSelectC5 (14s)
L4867  2026-10-08T03:14:51.0871883Z ⚠ [3641/3643] Built OIBridge.RelcSelectBlock (7.7s)
L4924  2026-10-08T03:14:57.3965080Z ℹ [3642/3643] Built OIBridge (6.3s)
```

No `[3643/3643]` line appears. The build's closing line:

```text
L4944  2026-10-08T03:14:57.4109475Z Build completed successfully (3643 jobs).
```

| Module | Build-progress line | Its output (up to the next progress line) | Inside the window? |
|---|---|---|---|
| `OIBridge.RelcSelectParity` | L4835 ℹ `[3638/3643]` Built (9.6s) | L4836 to L4837 (2 lines) | yes: build line and complete output |
| `OIBridge.RelcSelectSqueeze` | L4838 ℹ `[3639/3643]` Built (14s) | L4839 to L4853 (15 lines) | yes: build line and complete output |
| `OIBridge.RelcSelectC5` | L4854 ℹ `[3640/3643]` Built (14s) | L4855 to L4866 (12 lines) | yes: build line and complete output |
| `OIBridge.RelcSelectBlock` | L4867 ⚠ `[3641/3643]` Built (7.7s) | L4868 to L4923 (56 lines) | yes: build line and complete output |

**All four modules are inside the window.** Each has its build-progress line in the window, and its output is complete, because the next progress line also falls in the window. Inside: `OIBridge.RelcSelectParity`, `OIBridge.RelcSelectSqueeze`, `OIBridge.RelcSelectC5`, `OIBridge.RelcSelectBlock`. Outside: none.

All 4 progress lines read `Built`, not `Replayed`, so Lean compiled these modules in this run rather than replaying cached output.

## (a) Lines mentioning `RelcSelect`

There are 45 such lines, from L4835 to L4923, quoted here in order:

```text
L4835  2026-10-08T03:14:43.3770205Z ℹ [3638/3643] Built OIBridge.RelcSelectParity (9.6s)
L4836  2026-10-08T03:14:43.3800648Z info: OIBridge/RelcSelectParity.lean:363:0: 'OIBridge.RelcSelect.finrank_plus_eq_finrank_minus_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
L4837  2026-10-08T03:14:43.3860085Z info: OIBridge/RelcSelectParity.lean:364:0: 'OIBridge.RelcSelect.not_even_of_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
L4838  2026-10-08T03:14:48.2870210Z ℹ [3639/3643] Built OIBridge.RelcSelectSqueeze (14s)
L4839  2026-10-08T03:14:48.2929883Z info: OIBridge/RelcSelectSqueeze.lean:489:0: 'OIBridge.RelcSelect.frame_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
L4840  2026-10-08T03:14:48.2999399Z info: OIBridge/RelcSelectSqueeze.lean:490:0: 'OIBridge.RelcSelect.relT_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
L4841  2026-10-08T03:14:48.3000379Z info: OIBridge/RelcSelectSqueeze.lean:491:0: 'OIBridge.RelcSelect.relC_symm_of_relT' depends on axioms: [propext, Classical.choice, Quot.sound]
L4842  2026-10-08T03:14:48.3001145Z info: OIBridge/RelcSelectSqueeze.lean:492:0: 'OIBridge.RelcSelect.gateRel_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
L4843  2026-10-08T03:14:48.3001862Z info: OIBridge/RelcSelectSqueeze.lean:493:0: 'OIBridge.RelcSelect.gSq_frame' depends on axioms: [propext, Classical.choice, Quot.sound]
L4844  2026-10-08T03:14:48.3002869Z info: OIBridge/RelcSelectSqueeze.lean:494:0: 'OIBridge.RelcSelect.gateRel_gSq' depends on axioms: [propext, Classical.choice, Quot.sound]
L4845  2026-10-08T03:14:48.3003592Z info: OIBridge/RelcSelectSqueeze.lean:495:0: 'OIBridge.RelcSelect.pairVal_gSq_prodState' depends on axioms: [propext, Classical.choice, Quot.sound]
L4846  2026-10-08T03:14:48.3004411Z info: OIBridge/RelcSelectSqueeze.lean:496:0: 'OIBridge.RelcSelect.gSq_core' depends on axioms: [propext, Classical.choice, Quot.sound]
L4847  2026-10-08T03:14:48.3005083Z info: OIBridge/RelcSelectSqueeze.lean:497:0: 'OIBridge.RelcSelect.gSq_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
L4848  2026-10-08T03:14:48.3005761Z info: OIBridge/RelcSelectSqueeze.lean:498:0: 'OIBridge.RelcSelect.gSq_symm_value' depends on axioms: [propext, Classical.choice, Quot.sound]
L4849  2026-10-08T03:14:48.3006435Z info: OIBridge/RelcSelectSqueeze.lean:499:0: 'OIBridge.RelcSelect.gSq_not_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
L4850  2026-10-08T03:14:48.3007136Z info: OIBridge/RelcSelectSqueeze.lean:500:0: 'OIBridge.RelcSelect.not_nativeGate_gSq' depends on axioms: [propext, Classical.choice, Quot.sound]
L4851  2026-10-08T03:14:48.3007845Z info: OIBridge/RelcSelectSqueeze.lean:501:0: 'OIBridge.RelcSelect.not_nativeGate_gSqInv' depends on axioms: [propext, Classical.choice, Quot.sound]
L4852  2026-10-08T03:14:48.3008533Z info: OIBridge/RelcSelectSqueeze.lean:502:0: 'OIBridge.RelcSelect.gSq_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
L4853  2026-10-08T03:14:48.3009584Z info: OIBridge/RelcSelectSqueeze.lean:503:0: 'OIBridge.RelcSelect.gSqInv_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
L4854  2026-10-08T03:14:48.5880574Z ℹ [3640/3643] Built OIBridge.RelcSelectC5 (14s)
L4855  2026-10-08T03:14:48.5895737Z info: OIBridge/RelcSelectC5.lean:409:0: 'OIBridge.RelcSelect.isNot_nC5' depends on axioms: [propext, Classical.choice, Quot.sound]
L4856  2026-10-08T03:14:48.5909993Z info: OIBridge/RelcSelectC5.lean:410:0: 'OIBridge.RelcSelect.gC5_frame' depends on axioms: [propext, Classical.choice, Quot.sound]
L4857  2026-10-08T03:14:48.5939882Z info: OIBridge/RelcSelectC5.lean:411:0: 'OIBridge.RelcSelect.gC5_relT' depends on axioms: [propext, Classical.choice, Quot.sound]
L4858  2026-10-08T03:14:48.5969787Z info: OIBridge/RelcSelectC5.lean:412:0: 'OIBridge.RelcSelect.gC5_not_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
L4859  2026-10-08T03:14:48.5979760Z info: OIBridge/RelcSelectC5.lean:413:0: 'OIBridge.RelcSelect.selC5_target' depends on axioms: [propext, Classical.choice, Quot.sound]
L4860  2026-10-08T03:14:48.5999849Z info: OIBridge/RelcSelectC5.lean:414:0: 'OIBridge.RelcSelect.selC5_core' depends on axioms: [propext, Classical.choice, Quot.sound]
L4861  2026-10-08T03:14:48.6030231Z info: OIBridge/RelcSelectC5.lean:415:0: 'OIBridge.RelcSelect.prodEffVal_gC5_prodState' depends on axioms: [propext, Classical.choice, Quot.sound]
L4862  2026-10-08T03:14:48.6059806Z info: OIBridge/RelcSelectC5.lean:416:0: 'OIBridge.RelcSelect.gC5_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
L4863  2026-10-08T03:14:48.6120816Z info: OIBridge/RelcSelectC5.lean:417:0: 'OIBridge.RelcSelect.gC5_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
L4864  2026-10-08T03:14:48.6149841Z info: OIBridge/RelcSelectC5.lean:418:0: 'OIBridge.RelcSelect.c5_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
L4865  2026-10-08T03:14:48.6151184Z info: OIBridge/RelcSelectC5.lean:419:0: 'OIBridge.RelcSelect.not_nativeGate_gC5' depends on axioms: [propext, Classical.choice, Quot.sound]
L4866  2026-10-08T03:14:48.6179869Z info: OIBridge/RelcSelectC5.lean:420:0: 'OIBridge.RelcSelect.relT_not_dimension_selecting' depends on axioms: [propext, Classical.choice, Quot.sound]
L4867  2026-10-08T03:14:51.0871883Z ⚠ [3641/3643] Built OIBridge.RelcSelectBlock (7.7s)
L4868  2026-10-08T03:14:51.0872373Z warning: OIBridge/RelcSelectBlock.lean:606:23: This simp argument is unused:
L4876  2026-10-08T03:14:51.0875117Z warning: OIBridge/RelcSelectBlock.lean:606:52: This simp argument is unused:
L4884  2026-10-08T03:14:51.0877340Z warning: OIBridge/RelcSelectBlock.lean:608:10: This simp argument is unused:
L4892  2026-10-08T03:14:51.0879946Z warning: OIBridge/RelcSelectBlock.lean:622:25: This simp argument is unused:
L4900  2026-10-08T03:14:51.0882966Z warning: OIBridge/RelcSelectBlock.lean:622:54: This simp argument is unused:
L4908  2026-10-08T03:14:51.0886069Z warning: OIBridge/RelcSelectBlock.lean:623:70: This simp argument is unused:
L4916  2026-10-08T03:14:51.0889669Z warning: OIBridge/RelcSelectBlock.lean:623:93: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
L4919  2026-10-08T03:14:51.0891395Z info: OIBridge/RelcSelectBlock.lean:765:0: 'OIBridge.RelcSelect.ctrlGate_of_nativeGate' depends on axioms: [propext, Classical.choice, Quot.sound]
L4920  2026-10-08T03:14:51.0892608Z info: OIBridge/RelcSelectBlock.lean:766:0: 'OIBridge.RelcSelect.actT_slice_ctrl' depends on axioms: [propext, Classical.choice, Quot.sound]
L4921  2026-10-08T03:14:51.0893959Z info: OIBridge/RelcSelectBlock.lean:767:0: 'OIBridge.RelcSelect.blockData_of_ctrlGate' depends on axioms: [propext, Classical.choice, Quot.sound]
L4922  2026-10-08T03:14:51.0895140Z info: OIBridge/RelcSelectBlock.lean:768:0: 'OIBridge.RelcSelect.dim_of_ctrlGate' depends on axioms: [propext, Classical.choice, Quot.sound]
L4923  2026-10-08T03:14:51.0896394Z info: OIBridge/RelcSelectBlock.lean:769:0: 'OIBridge.RelcSelect.three_of_ctrlGate' depends on axioms: [propext, Classical.choice, Quot.sound]
```

**Axiom reports for `OIBridge.RelcSelect.*` names in the window:** 34 report lines naming 34 distinct names. No name is reported twice.

| Source file (as printed) | Reports |
|---|---|
| `OIBridge/RelcSelectParity.lean` | 2 |
| `OIBridge/RelcSelectSqueeze.lean` | 15 |
| `OIBridge/RelcSelectC5.lean` | 12 |
| `OIBridge/RelcSelectBlock.lean` | 5 |
| **Total** | **34** |

- Reports reading exactly `depends on axioms: [propext, Classical.choice, Quot.sound]`: **34 of 34**. Reports that differ: **none**.
- Reports reading `does not depend on any axioms`: 0.
- A looser match, for any line containing `OIBridge.RelcSelect.` together with an axiom phrase, finds 34 lines. That is the same set, so the strict pattern missed nothing.

**Cross-check against the `#print axioms` lines in the four sources at `da295a1`** (read with `git show da295a1be51e7d7e2013307b85b0c5f44a9c897a:verification/lean-mathlib/OIBridge/RelcSelect<X>.lean`):

| Source | Declared prints (file lines) | With a report in the window | Without a report |
|---|---|---|---|
| `RelcSelectParity.lean` | 2 (lines 363 to 364) | 2 | none |
| `RelcSelectSqueeze.lean` | 15 (lines 489 to 503) | 15 | none |
| `RelcSelectC5.lean` | 12 (lines 409 to 420) | 12 | none |
| `RelcSelectBlock.lean` | 5 (lines 765 to 769) | 5 | none |
| **Total** | **34** | **34** | **none** |

- Every declared `#print axioms` has its report in the window: 34 of 34. Matching is by `file:line`, and the printed name agrees in every case, so each report sits on its own `#print` line.
- Declared prints with no report in the window: none.
- Reports in the window with no declared print: none.
- Matching by name alone gives the same result: 34 of 34 declared names are reported.

| Source file:line | Declared name | Report | Axioms |
|---|---|---|---|
| RelcSelectParity.lean:363 | `OIBridge.RelcSelect.finrank_plus_eq_finrank_minus_relC` | L4836 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectParity.lean:364 | `OIBridge.RelcSelect.not_even_of_relC` | L4837 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:489 | `OIBridge.RelcSelect.frame_symm` | L4839 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:490 | `OIBridge.RelcSelect.relT_symm` | L4840 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:491 | `OIBridge.RelcSelect.relC_symm_of_relT` | L4841 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:492 | `OIBridge.RelcSelect.gateRel_symm` | L4842 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:493 | `OIBridge.RelcSelect.gSq_frame` | L4843 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:494 | `OIBridge.RelcSelect.gateRel_gSq` | L4844 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:495 | `OIBridge.RelcSelect.pairVal_gSq_prodState` | L4845 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:496 | `OIBridge.RelcSelect.gSq_core` | L4846 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:497 | `OIBridge.RelcSelect.gSq_posFwd` | L4847 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:498 | `OIBridge.RelcSelect.gSq_symm_value` | L4848 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:499 | `OIBridge.RelcSelect.gSq_not_posInv` | L4849 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:500 | `OIBridge.RelcSelect.not_nativeGate_gSq` | L4850 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:501 | `OIBridge.RelcSelect.not_nativeGate_gSqInv` | L4851 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:502 | `OIBridge.RelcSelect.gSq_sep` | L4852 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectSqueeze.lean:503 | `OIBridge.RelcSelect.gSqInv_sep` | L4853 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:409 | `OIBridge.RelcSelect.isNot_nC5` | L4855 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:410 | `OIBridge.RelcSelect.gC5_frame` | L4856 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:411 | `OIBridge.RelcSelect.gC5_relT` | L4857 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:412 | `OIBridge.RelcSelect.gC5_not_relC` | L4858 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:413 | `OIBridge.RelcSelect.selC5_target` | L4859 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:414 | `OIBridge.RelcSelect.selC5_core` | L4860 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:415 | `OIBridge.RelcSelect.prodEffVal_gC5_prodState` | L4861 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:416 | `OIBridge.RelcSelect.gC5_posFwd` | L4862 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:417 | `OIBridge.RelcSelect.gC5_posInv` | L4863 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:418 | `OIBridge.RelcSelect.c5_sep` | L4864 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:419 | `OIBridge.RelcSelect.not_nativeGate_gC5` | L4865 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectC5.lean:420 | `OIBridge.RelcSelect.relT_not_dimension_selecting` | L4866 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectBlock.lean:765 | `OIBridge.RelcSelect.ctrlGate_of_nativeGate` | L4919 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectBlock.lean:766 | `OIBridge.RelcSelect.actT_slice_ctrl` | L4920 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectBlock.lean:767 | `OIBridge.RelcSelect.blockData_of_ctrlGate` | L4921 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectBlock.lean:768 | `OIBridge.RelcSelect.dim_of_ctrlGate` | L4922 | `[propext, Classical.choice, Quot.sound]` |
| RelcSelectBlock.lean:769 | `OIBridge.RelcSelect.three_of_ctrlGate` | L4923 | `[propext, Classical.choice, Quot.sound]` |

## (b) Warnings, errors and failed-build markers

| Module | Warning lines naming its file | Build-line glyph |
|---|---|---|
| `OIBridge.RelcSelectParity` | 0 | ℹ |
| `OIBridge.RelcSelectSqueeze` | 0 | ℹ |
| `OIBridge.RelcSelectC5` | 0 | ℹ |
| `OIBridge.RelcSelectBlock` | 7 | ⚠ |

Every module's output is fully inside the window, so none of these counts is "not determinable". The glyphs agree with the counts: `⚠` marks the one module with warnings, and `ℹ` marks the three without.

The 7 `RelcSelectBlock` warning lines, verbatim:

```text
L4868  2026-10-08T03:14:51.0872373Z warning: OIBridge/RelcSelectBlock.lean:606:23: This simp argument is unused:
L4876  2026-10-08T03:14:51.0875117Z warning: OIBridge/RelcSelectBlock.lean:606:52: This simp argument is unused:
L4884  2026-10-08T03:14:51.0877340Z warning: OIBridge/RelcSelectBlock.lean:608:10: This simp argument is unused:
L4892  2026-10-08T03:14:51.0879946Z warning: OIBridge/RelcSelectBlock.lean:622:25: This simp argument is unused:
L4900  2026-10-08T03:14:51.0882966Z warning: OIBridge/RelcSelectBlock.lean:622:54: This simp argument is unused:
L4908  2026-10-08T03:14:51.0886069Z warning: OIBridge/RelcSelectBlock.lean:623:70: This simp argument is unused:
L4916  2026-10-08T03:14:51.0889669Z warning: OIBridge/RelcSelectBlock.lean:623:93: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
```

By linter, as named on each warning's `Note:` line: `unusedSimpArgs` 6, `unnecessarySeqFocus` 1. These are lint warnings about unused simp arguments and an unnecessary `<;>`, not proof failures.

Errors and failures anywhere in the window:

| Marker | Lines |
|---|---|
| Lean `error:` diagnostic lines | 0 |
| `error:` anywhere in a line | 0 |
| `##[error]` annotations | 0 |
| Lake failure glyph ✖ / ✗ / ❌ | 0 |
| `fail` as a substring, any case (covers `Build failed`, `failed`, `failures`, `FAIL`) | 0 |
| Gate rows reading `FAIL` | 0 |

Only 1 line contains `error` in any case. It is a Node.js deprecation notice printed by the cache post-step:

```text
L4980  2026-10-08T03:15:38.4864471Z (node:24544) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
```

The window has 1 `##[warning]` annotation, the runner's Node.js 20 notice at L5000. It is not a Lean diagnostic.

For context, the Lean `warning:` lines in the window per file: `OIBridge/DitaTorusLocus.lean` 781, `OIBridge/RelcSelectBlock.lean` 7, `OIBridge/ProductStrictLift.lean` 2.

## (c) `sorryAx` and `declaration uses 'sorry'`

| Pattern | Lines in the window |
|---|---|
| `sorryAx` | 0 |
| `declaration uses 'sorry'` | 0 |
| `sorry` (any case) | 0 |

The prefix `sorr` (any case) occurs on 1 line, the gate's lean-axioms row at L4968. The gate cut it to 60 characters, ending in `no sorr`:

```text
L4968  2026-10-08T03:15:36.4131658Z   PASS  lean-axioms      lean_axiom_check: OK (5860 named result(s) reported, no sorr
```

For context, the window holds 190 axiom reports across all modules. Their axiom lists: `[propext, Classical.choice, Quot.sound]` x 190. None names `sorryAx`.
The four RelcSelect sources at `da295a1` contain no `sorry`, `sorryAx` or `admit` token and no `axiom` declaration; each count is 0 in all four files.

## (d) Release gate

The job API records step 6, `Release gate`, with conclusion `success`, from 2026-10-08T03:14:57Z to 2026-10-08T03:15:36Z.

The step header and the gate's complete output, L4947 to L4975, verbatim:

```text
L4947  2026-10-08T03:14:57.4541676Z ##[group]Run python3 tools/release_gate.py
L4948  2026-10-08T03:14:57.4541967Z \x1b[36;1mpython3 tools/release_gate.py\x1b[0m
L4949  2026-10-08T03:14:57.4637216Z shell: /usr/bin/bash -e {0}
L4950  2026-10-08T03:14:57.4637437Z ##[endgroup]
L4951  2026-10-08T03:15:36.4124154Z release gate
L4952  2026-10-08T03:15:36.4124427Z ====================================================================
L4953  2026-10-08T03:15:36.4124835Z   PASS  toolchain        toolchain_check: OK (build entry present, unicode-fix.tex co
L4954  2026-10-08T03:15:36.4125243Z   PASS  staleness        staleness_check: OK (13 matched, 0 unstamped)
L4955  2026-10-08T03:15:36.4125629Z   PASS  baseline-label   baseline_label_check: OK (no baseline archives named)
L4956  2026-10-08T03:15:36.4126030Z   PASS  voice            voice_check: OK (no manuscript-voice history narration; 40 m
L4957  2026-10-08T03:15:36.4126727Z   PASS  voice-scope      voice_scope_test: OK (6 scope case(s); the checker scans the
L4958  2026-10-08T03:15:36.4127205Z   PASS  ci-gate-presence ci_gate_presence_test: OK (CI runs the real release gate)
L4959  2026-10-08T03:15:36.4127642Z   PASS  artifact-placement artifact_placement_check: OK (no unaccounted root artifact; 
L4960  2026-10-08T03:15:36.4128079Z   PASS  manifest-drift   build_migration_manifest --check: OK (91 artifacts; both gen
L4961  2026-10-08T03:15:36.4128490Z   PASS  claims           claims_check: OK (no withdrawn result asserted unconditional
L4962  2026-10-08T03:15:36.4129075Z   PASS  duplicate        duplicate_check: OK (no paragraph repeated within a file)
L4963  2026-10-08T03:15:36.4129496Z   PASS  mirror           mirror_check: 0 chapter line(s) absent from FULL.md
L4964  2026-10-08T03:15:36.4129874Z   PASS  citation         citation_check: 112 citation(s), 0 broken, 0 duplicate bib n
L4965  2026-10-08T03:15:36.4130276Z   PASS  architecture     architecture_check: 259 invariant(s), 0 violation(s), 0 self
L4966  2026-10-08T03:15:36.4130713Z   PASS  dependency-label dependency_label_check: OK (no stale dependency label, 41 fi
L4967  2026-10-08T03:15:36.4131137Z   PASS  coverage         coverage_check: OK (129 canonical statements, 19 unattached 
L4968  2026-10-08T03:15:36.4131658Z   PASS  lean-axioms      lean_axiom_check: OK (5860 named result(s) reported, no sorr
L4969  2026-10-08T03:15:36.4132054Z   PASS  lean-manuscript  lean_manuscript_census: OK (every cited identifier and path 
L4970  2026-10-08T03:15:36.4132465Z   PASS  legacy-records   LEGACY  303 record(s) in 75 closed namespace(s), all intact
L4971  2026-10-08T03:15:36.4132803Z   PASS  v3-self-test     v3_verifier: self-test OK
L4972  2026-10-08T03:15:36.4133111Z   PASS  v3-corpus        CORPUS  140 vector(s), exact and as expected
L4973  2026-10-08T03:15:36.4133425Z   PASS  v3-receipts      RECEIPTS  41 receipt(s), all hold
L4974  2026-10-08T03:15:36.4133692Z ====================================================================
L4975  2026-10-08T03:15:36.4134072Z release gate: PASS  (note: --label bNNN not given, so the baseline check ran in relative mode only)
```

- The table has **21 rows: 21 PASS, 0 FAIL**.
- The step names and their order match the check list in `tools/release_gate.py` at `da295a1`: the `checks = [...]` list, with `baseline-label` inserted at index 2 by line 172.
- Each row's detail is the last non-empty output line of its check, cut to 60 characters by the gate itself (`tail[:60]`, `tools/release_gate.py:179`). Cut-off text such as `no sorr` is how the gate prints it, not damage to the saved log. 12 row details are exactly 60 characters long, and 0 are longer.

The rows you asked about, verbatim:

```text
L4968  2026-10-08T03:15:36.4131658Z   PASS  lean-axioms      lean_axiom_check: OK (5860 named result(s) reported, no sorr
L4969  2026-10-08T03:15:36.4132054Z   PASS  lean-manuscript  lean_manuscript_census: OK (every cited identifier and path 
L4970  2026-10-08T03:15:36.4132465Z   PASS  legacy-records   LEGACY  303 record(s) in 75 closed namespace(s), all intact
L4973  2026-10-08T03:15:36.4133425Z   PASS  v3-receipts      RECEIPTS  41 receipt(s), all hold
```

The final verdict line:

```text
L4975  2026-10-08T03:15:36.4134072Z release gate: PASS  (note: --label bNNN not given, so the baseline check ran in relative mode only)
```

| Count as printed | Value |
|---|---|
| lean-axioms: named results reported | **5860** (`lean_axiom_check: OK (5860 named result(s) reported, no sorr`) |
| v3-receipts: receipts | **41**, all hold |
| legacy-records: records / closed namespaces | **303** in **75**, all intact |
| v3-corpus: vectors | 140 |

The lean-manuscript row reads `lean_manuscript_census: OK (every cited identifier and path `. Its detail is cut at 60 characters and states no count.


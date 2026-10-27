# Evidence part E3: CI and verification receipts; open obligations

36 items in `part-E3.json`: 19 `ci-receipt` and 17 `open-obligation`.

## Counts

| | pass | partial | fail | total |
|---|---|---|---|---|
| reproduced | 4 | 0 | 0 | 4 |
| certificate-checked | 12 | 3 | 0 | 15 |
| traced-only | 10 | 7 | 0 | 17 |
| **total** | 26 | 10 | 0 | 36 |

The open-obligation items are traced-only by nature: each status was traced to the corpus's own status records (ROADMAP at
`eae01647`, `inventory/proofs.json`, the cited paper lines), and no open or conditional result was re-proved.

## What was verified

- **Lean pin and its CI (E3-01 to E3-05).**
  - `17b830bc` is on main.
  - Run 40330683786 and job 121598983127 concluded success at that exact `head_sha`, with the Build and Release gate steps
    green.
  - The job log was fetched whole. Its sha256 (`bc2291bc…`) and the sha256 of its cut at the gate verdict (`1a83921f…`,
    38918 lines) match the digests recorded in `papers/introduction_repro/`.
  - The frozen extractor and comparator (`48b18ac5`) re-derive the retained result: REPRODUCTION HOLDS. Two log mutations
    are caught: an injected `sorryAx` and a dropped report.
  - All 28 Appendix A declarations sit at the stated lines and carry one three-axiom report each. A two-mutation
    countercontrol is caught.
  - The job printed Lean 4.33.0 and resolved Mathlib to `db584cd6`, which is the `v4.33.0` tag today.
  - The Lean trees are identical at `687e885b`, `17b830bc`, `c967d6a9`, `b64919cd`, `eae01647`, `02e73e56` and `4a260ca9`.
- **Main CI (E3-06 to E3-09).**
  - Each of `b64919cd`, `eae01647`, `02e73e56` and `c967d6a9` has exactly one workflow run, a `verify` push run that
    succeeded: 25 jobs success and 1 skipped placeholder.
  - In each Mathlib bridge log the release gate passes 22/22, and the 14-module reports equal the retained result.
  - `c967d6a9` is not cited by the Introduction, the matrix or FINDINGS.
- **R4 (E3-13).** The archive's R4 check passes on the retained result, and three countercontrols are caught. Tree mode does
  not apply, because the archive left the tree at `5c4e5087`.
- **V3 receipts and legacy records (E3-15).** The gate's v3-receipts step ("52 hold") and legacy-records step ("303
  intact") pass at all five pinned heads. No Introduction claim cites a receipt directly.
- **Black-hole records (E3-17 to E3-19).**
  - The review commits resolve on main, and every retained review matches its recorded sha256.
  - `SHA256SUMS` verifies 14/14 for both packages.
  - Both `checks.py` replays reproduce `result.json` byte for byte (52 s and 29 s). This includes the Introduction's counts
    1376/40320, 60 and 32.
  - Changes after the last retained review are wording only, plus one verdict string in BH-02.

## Partial items

1. **E3-11, fresh elaboration.**
   - Every checked main job replayed all 226 `OIBridge` modules from one cache key, and built none.
   - The run that saved that key, run 40218014178 at `8dc36d55` (identical Lean trees), elaborated afresh only 5 of the 14
     Appendix A modules.
   - No log examined shows a fresh elaboration of the other 9 at these sources. The README discloses the replay.
2. **E3-12, #918 head `4a260ca9`.** Its only CI is pull_request run 40391463077, a synthetic merge, which is not an
   exact-head attestation. Its tree equals the head's, because the base `b64919cd` is an ancestor. `introduction_repro/`
   exists only on #918.
3. **E3-14, claims whose only kernel evidence is an expiring CI log.**
   - Matrix claims I-009, I-088, I-112, I-117, I-120, I-121, I-125, I-146, I-246, I-258, I-281 and I-292 cite declarations
     outside the 14 retained modules.
   - The same holds for the declarations FINDINGS adds in R-06, R-09, R-13 and O-5.
   - Every one has a report in the digest-checked log text that reads the three axioms, but none is in a retained
     expected result. The structured certificate is the Release gate step's conclusion (every report within the
     allow-list, a report for every declared `#print axioms`); "exactly the three axioms" is read from log text.
   - OD-15 records this for R-06, R-13 and O-5 only. It is not recorded for the matrix-only links or R-09.
   - The same log can yield an extended expected result without a rebuild, while the log is still available.
4. **E3-20, H-scramble.** L183 "whether H-scramble … hold" treats as open a hypothesis that is settled negatively in the
   aligned configuration setting (BHb C1/C6(a), replayed). This is a settled-vs-open flag, resolved by R-01.
5. **E3-27, F2 and conditions (iii)–(v).** L12, L120, L173 and L183 present as open what the corpus settles negatively for
   the stated architecture (ROADMAP:69, :1528–1531, INDEPENDENT; kernel PhaseSource, StructuralClosure and others). This is
   a settled-vs-open flag, resolved by R-06.
6. **E3-35, exact gluing.** The rooted case is settled positively in the kernel by `finiteRootedRealizable_iff_pper`,
   which is stated in no manuscript. L185 lists exact gluing as open without restriction. This is a settled-vs-open flag,
   resolved by R-09 (CON-28).
7. **E3-25, E3-29, E3-30 and E3-34.** These are imprecisions or omissions: (C2) mixing (R-26), H-∞ and K kinematics (R-10),
   and the steps proved only on paper (R-27). In each case the corpus status agrees with the Introduction's direction.

## Other observations

- The black-hole landing #917's merge message says "exact-head CI green" for `84aca6b0`. The only run at `84aca6b0` is a
  pull_request run. This is recorded only, and history is not rewritten. The black-hole claims do not rest on CI, and no
  workflow runs the black-hole checks.
- BH-02's last retained review is of `ce7937d2`. The landing audit of `606c98d8` is recorded only in PROVENANCE and in the
  commit messages.
- The Born-exponent origin has no ROADMAP row, although the Introduction and Main state it as open.
- H-scramble and H-decouple have no ROADMAP row either.
- H-slope limits no Introduction claim.

## Not checked

- `mutants.py` for either black-hole package.
- `tools/v3_verifier.py --receipts` (needs full history; this worktree is shallow).
- R8 of the retention check.
- Log-retention settings.

## Needs owner authorization

- **A fresh-build CI reproduction** of `papers/introduction_repro/results-121598983127.json` by its recipe, from an empty
  `.lake/build` at `17b830bc`, through the `reproduce evidence` workflow or equivalent. This closes E3-11.
- **Optionally, before job 121598983127's log expires:** re-derive an extended expected result from the same
  digest-checked log, covering the modules of E3-14. This is local and needs no CI. Landing it in
  `papers/introduction_repro/` is a §A.42 change on #918.

## Scripts

All under `evidence/scripts/`:

- `E3_joblog_check.py`: log digests, the cut, extraction and comparison.
- `E3_appendix_a_check.py`: Appendix A declarations, lines and axiom reports.
- `E3_r4_check.py`: R4 with countercontrols.
- `E3_kernel_coverage.py`: matrix kernel links, retained or only in the log.

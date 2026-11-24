# The reader-cache correction: record revision 2

Writer's record, 2026-11-24, made under correction 1 (owner `amaybaum`, decision 2 of 2026-11-24: "Correct the caching
notes concerning submodule test coverage and replace the unverified timing figures with independently measured
results."). Local only. This file does not edit `PERF-FIX.md` (sha256 69ab713b…, kept as written and listed in
`MANIFEST.sha256`); it supersedes the two parts of it named below. Everything else in `PERF-FIX.md` stands.

Source of the measured figures: the independent review of the correction,
`review-perf-fix/review.md` (sha256 6def2c2a7561baf089e3d2ae0d73f9caeaa0abecd0a3185fda0eb6900657ae42), section 6 and
nits N-1, N-3, N-4.

## 1. Supersedes: the K08 row of the mutation table (submodule coverage)

`PERF-FIX.md` says of the surviving mutant K08 that "in-memory submodule entries are covered by TR51 through
`Overlay`". That is false for the exclusion itself. The reviewer's mutant K08o (the same exclusion removed from
`Overlay.paths`) survives at c59b562c, and the exclusion removed at 67bae482 also survives in both readers (B08,
B08o).

Corrected statement: **neither reader's submodule filter in `paths` (`GitRepo.paths` and `Overlay.paths`) has an
isolating control, at 67bae482 or at c59b562c.** No on-disk fixture holds a gitlink, and no control fails when either
filter is removed. The correction did not change the filter. It moved the unchanged filter into the cached builder, so
the gap existed before the correction and was not introduced by it. No control is added for it: owner decision 2
authorizes only the correction of this note.

## 2. Supersedes: the runtime and memory table (the "before" figures)

The "before" column of `PERF-FIX.md` comes from two sources that cannot be confirmed:
- `logs/full/`: step 6, with memory sampled from /proc every 10 s, so a lower bound;
- `before-steps.txt`: steps 1-5, timed at 14:19 UTC. That is inside the window in which the staged configuration had
  been overwritten (review N-4), so the inputs of those timings cannot be confirmed from the record.

Both sources are withdrawn as evidence. The figures below are the reviewer's. They were measured with `wait4`
(`ru_maxrss`) on each step's process, on the same machine and with the same inputs for both commits. The two runs ran
concurrently on 4 cores.

| Step | 67bae482 wall | c59b562c wall | 67bae482 peak | c59b562c peak |
|---|---|---|---|---|
| 1 self-test | 0.1 s | 0.2 s | 25 MB | 25 MB |
| 2 purity | 0.7 s | 0.7 s | 39 MB | 39 MB |
| 3 synthetic | 0.6 s | 0.5 s | 28 MB | 29 MB |
| 4 conformance | 6.5 s | 6.7 s | 34 MB | 35 MB |
| 5 A1 conformance | 57.8 s | 56.5 s | 198 MB | 203 MB |
| 6 A1 controls | **4600.8 s** | **1180.9 s** | **1.20 GB** | **1.48 GB** |
| of which sweeps | 4151.5 s | 752.9 s | | |
| total, steps 1-6 | about 77.8 min | about 20.8 min | | |

**Memory.** The A1 step's peak rises from 1.20 GB to 1.48 GB, an increase of 0.28 GB (about 23%). Both figures are
exact `ru_maxrss` values, so "at most about 0.3 GB" and "≥ 1.20 GB (sampled)" in `PERF-FIX.md` are replaced by these.

**What is unchanged.** The writer's "after" figures (`logs/perf/after-steps.txt`: step 6 1175.0 s, peak 1.48 GB) were
measured exactly and agree with the reviewer's. The call counts and the profile figures in `PERF-FIX.md` are
unaffected, as are the corruption table and the equality result. The runtime still fits a hosted runner's 360-minute
job limit and 16 GB of memory.

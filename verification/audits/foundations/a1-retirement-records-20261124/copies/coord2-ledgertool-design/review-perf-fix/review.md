# Independent focused review: the reader-cache correction (661bcbed..c59b562c on 67bae482)

Reviewer: independent non-author reviewer, 2026-11-24. Review only. I did not modify the worktree
`coord2-impl-wt`, the writer's record `impl-v6.0e/` or either implementation commit. I made no commit, push, GitHub
write, CI run or dispatch. Every run used my own copies of the trees, built through a temporary index file under my
scratch directory. The runners read history from `coord2-impl-wt` read-only, and every revision was given as a full id,
never HEAD.

Objects reviewed:
- the correction commits 661bcbedcf601a3f0c1fd035d26cf08775ca3e8d, 71a17c735e24df43e768c6c6e3856de4415ef3e6,
  f5c1bd3f73b4d5d38fd4f24108a8f8334dbf2424 and **c59b562c168dc24706f51b791ec526dd897c909d** (tree
  a8090aac77a0c9d956b07a144b794bd497941a1c);
- the base they sit on, 67bae482b5842ede9e8430da841bd78563b0f97d.

Writer's record: `impl-v6.0e/PERF-FIX.md`, sha256 69ab713b1fc0298dfbe326b50b56166754eb7ce826711e174e81b19613519078 (matches).

## Verdict

**ACCEPT-WITH-NITS** for the exact correction commit c59b562c, as a correction on 67bae482. The verdict covers the
caching correction only.

There are no blocking findings. The result against each owner acceptance condition:

| Owner condition | Result |
|---|---|
| Identical verification outcomes | Met. 0 status changes and 0 controls missing. The only differences in `actual` are the 3 that follow from the change itself. |
| No weakened integrity guarantees | Met. 18 corruption and missing-object cases behave identically at the two commits. |
| Correct isolation between commits | Met. Each commit's cache entry is keyed by its full commit id. GV-CACHE-KEY tests this, and my mutants R09 and R10 are killed. |
| Immutable cached file lists | Met. They are read-only views over private dicts, and every value is a string or tuple. |
| Measurable performance improvement | Met. A1 controls take 4601 s before and 1181 s after (3.9x faster). |
| Independent focused review | This document. |

The main reviewer's REJECT of the base 67bae482 (B-1, the `uses:` line rule, in `review-impl-v6.0e/review.md`) is
outside this correction and still stands. This verdict does not clear it.

## Provenance of this review

- **First attempt halted.** My first attempt extracted the trees with `git archive`. The commits' `.gitattributes`
  marks `verification/audits` as `export-ignore`, so the extractions had no audit directory, and conformance EI6 and
  EI8–EI15 failed for that reason alone. When I tried to stop that run with a name-matching `pkill`, the permission
  system refused the command; it never ran. I then stopped my own task through the task tool and reported the halt.
- **Invalid outputs kept, not used.** The owner authorized resumption on 2026-11-24 (decision quoted by the
  coordinator). The invalid outputs remain in `rv-perf/` (`after/`, `before/`, `*-git/`, `out-after/`, `logs-after/`,
  `mutK-after/`, `mutB-base/`) and are labelled in `rv-perf/INVALID-DIAGNOSTIC.txt`, copied here as
  `evidence/INVALID-DIAGNOSTIC.txt`. **None of their results is used below.**
- **Valid trees.** I rebuilt both trees with
  `GIT_INDEX_FILE=<scratch> git read-tree <C>; git checkout-index -a --prefix=<dir>/`. Each has 3660 files, equal to
  `git ls-tree -r <C> | wc -l`, and `verification/audits/foundations/ledger-coverage-tool-20261123/` is present. The
  worktree's `git status` was clean afterwards.
- **Isolation.** Each commit had its own tree, its own `git init`'d copy (used for the synthetic fixture's `repo_path`
  and for the mutation harness), its own output and log directories, and its own private, hash-checked staged
  configuration. The run script refuses to start if the configuration's hash does not match.

| Commit | Staged configuration (private copy) |
|---|---|
| 67bae482 | 5af8f07e5bf5073e5126ab3a03792f34600ae6c0354f7b8453bd6d7d221f9c6d |
| c59b562c | b45be784875043fe6501fc7644aced019a57b46583495a7693f3d00d2b00a078 |

The same `--main 9deb69568d8231210c7f39cb65be943dea566371` was passed to both commits.

## 1. Scope of the diff (67bae482..c59b562c)

Exactly three files changed:
- `tools/ledger_coverage/engine/gitobj.py` (+26/−8): the cache;
- `tools/ledger_coverage/adapters/conformance_controls.py` (+151/−2): `cache_controls`, the four control ids added to
  `ALL_IDS`, and the `GV-CACHE` group;
- `records/side-change-classes-v1.json`: two pins re-pinned, for `gitobj.py` and `conformance_controls.py`.

Nothing else changed. There is no finding.

## 2. The code

These conclusions come from reading the code. Sections 4–5 test them.

**GitRepo**
- `entries(cid)` walks the verified trees into a local `out`. It stores `MappingProxyType(out)` under the full commit
  id only after the whole walk returns. A tree refused partway leaves nothing cached: GV-CACHE tests this, and mutant
  K04 is killed.
- `paths(cid)` builds its map from the cached entry map, under the same key. My mutant R11 stores an empty view
  before filling it; GV-CACHE kills it.

**What did not change**
- `_batch` (request by full id, `--no-replace-objects`, the reader environment, recomputing the id from type, length
  and content) is unchanged.
- `_commit` and `_tree` parsing are unchanged.
- Replace refs, grafts, commit-graph and lazy fetch are handled as before.

**Overlay**
- Caches are kept per in-memory commit id. That id is a SHA-1 over the subject, parents and changes, and nothing
  outside `add_commit`/`derive` alters an in-memory tree after it is created (I searched every caller). So a cached
  entry cannot go stale.
- Base commits are delegated to the base reader's own views.
- Before the fix, `Overlay.entries` returned the `_LazyTree`'s own mutable dict to callers. It now returns a read-only
  copy, which is an improvement.

**Immutability**
- The dict behind each view is held only by the view.
- Every value is a `str` or a `(str, str)` tuple, so nothing a caller can reach is mutable.
- No caller in `tools/` assigns into, pops from, serialises or deep-copies a returned map (I checked all 59 call
  sites).
- The only way round a `MappingProxyType` is interpreter introspection (`gc.get_referents`, ctypes), which is not a
  caller-API path.

**Could a cached map ever be wrong?** I found no path by which a cached map could be served for a different commit or
for a tree that failed verification, or by which a first read could skip verification.

## 3. Equality of verification outcomes (identical, verified inputs)

Each commit ran steps 1–6 of the writer's `repro.sh`, each step under a `wait4` measurement:

1. self-test
2. staged purity lint
3. synthetic fixture
4. conformance
5. A1 conformance
6. A1 controls with `--main`, sweeps included

Step 7, the release gate, was not run. It needs a checkout's HEAD and decides no control's outcome.

The comparison (`evidence/scripts/cmp.py`) covers every control's (id, status, actual). Timing keys are dropped and
run-directory paths and temp-directory suffixes are normalized.

| | 67bae482 | c59b562c |
|---|---|---|
| controls compared | 342 | 346 |
| PASS / NOT RUN / informational | 335 / 3 / 4 | 339 / 3 / 4 |
| A1 controls | 91 passed, RT-T failed (not run, environment-bound) | the same |

Comparison (`evidence/cmp-before-after.json`):
- **339 identical** in id, status and actual;
- **4 added**: GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE and GV-CACHE-KEY, all PASS;
- **0 status changes, 0 absent after**;
- **3 differ in `actual` only**, each by construction:
  - `synthetic/_Y8_engine`: the engine's hash, 45ac7f13… before and a7f5da06… after. `gitobj.py` is the only engine
    file that changed.
  - `a1-controls/RT-L2`, PASS in both. Its 57 leaf differences (`evidence/rtl2.json`) are 54 changes of the predicted
    landing commit id (b9770c76… → f244b26f…) and 3 `m` blobs of exactly the changed paths (`gitobj.py`,
    `conformance_controls.py`, the class record). Nothing is unexplained.
  - `purity/outcome`, PASS with 0 findings in both. Only `config.blob_sha256` and `stand_in_for_F` differ, because the
    two commits use different staged configurations.

The writer reported 340 identical and 2 differing because their comparison read only `(outcome, findings)` for the
purity row; see N-2. Both counts describe the same results.

**Reproduction checks.** My 67bae482 results equal the writer's `logs/full`, all 342 controls
(`evidence/cmp-writerbefore-vs-minebefore.json`). My c59b562c results equal the writer's `logs/perf/after-full`, all
346 controls (`evidence/cmp-writerafter-vs-mineafter.json`).

## 4. Corruption and the new controls

**Corruption probe.** `evidence/scripts/corrupt.py` loads each commit's `gitobj.py` and runs 18 cases on identical
small stores. Results are in `evidence/corruption.json`. **Every case gives the same outcome at both commits**
(`identical: true`):

| Case | Both commits |
|---|---|
| Blob corrupted before the first read, commit's paths not listed | refused |
| Blob corrupted before the first read, paths already listed | refused, on a second read too, and through `read_blob` |
| Overlay commit derived over a corrupted blob: path listing (it lists ids only) | served |
| Overlay commit derived over a corrupted blob: reading that blob | refused |
| Tree corrupted before the first read: `paths`, `paths` again, `entries`, `blob_id`, overlay `paths` twice | all refused; nothing cached |
| Corruption after a successful read, same reader | not re-detected: verified bytes and the same path map served |
| Corruption after a successful read, a new reader | refused |
| Missing blob, with or without paths listed | refused |

**Corruption timing.** Corruption present before the first verifying read is refused at both commits. Corruption that
occurs after a successful read is not re-detected by the same reader at either commit, because the reader's object
cache (`_objs`, `_trees`), which predates this correction, serves what it verified. `PERF-FIX.md` and the
GV-CACHE-AFTER-READ text say exactly this and claim no detection after a read. That is consistent with the tests.

**The new controls test what they claim:**
- **GV-CACHE:** blob refused cold, warm and on a second read; tree refused on every call; the tool run exits 65. It
  kills K04, K07 and my R11.
- **GV-CACHE-IMMUTABLE:** five mutation forms refused on all five views; a mutated copy leaves the cache unchanged;
  the same view is returned. It kills K01, K02 and K06.
- **GV-CACHE-KEY:** each of seven commits is compared with `git --no-replace-objects ls-tree -r` in both read orders;
  seven distinct maps; X and M differ; two in-memory commits are kept apart. It kills K03, R09 and (with others) K05
  and R10.
- **GV-CACHE-AFTER-READ:** states the not-re-detected behaviour and that a new reader refuses.

## 5. Mutation

Harness: the writer's `mutate_cache.py`, copied, with 1 worker. Runs used the valid `git init`'d trees, covering
self-test, synthetic and conformance. Base runs were all PASS apart from 2 NOT RUN, at both commits.

| Mutant | c59b562c | Note |
|---|---|---|
| K01–K07 (writer's) | killed | matches the writer's run |
| K08: `GitRepo.paths` submodule exclusion removed | **survived** | |
| K08o (mine): `Overlay.paths` submodule exclusion removed | **survived** | |
| R09 / R10 (mine): GitRepo / Overlay entry cache keyed by a constant | killed | |
| R11 (mine): path map stored before it is built | killed | |
| R12 (mine): extra private alias of the entry dict | survived | expected; the alias is not reachable by any caller |

**K08 is a test gap that existed before the correction, not a weakness it introduces.** At 67bae482, removing the
same exclusion also survives:
- B08 (`GitRepo.paths`) survives (`evidence/mutation/mut-base-b08*`);
- B08o (`Overlay.paths`) survives (`evidence/mutation/mut-base*`).

No on-disk fixture contains a gitlink (`Disk._tree` can write one, but no disk world holds a submodule entry). The
correction moved the unchanged filter into the cached builder. The behaviour is the same, and so is the lack of a
control for it.

## 6. Runtime and memory (same machine, same inputs, measured identically)

Wall time and `ru_maxrss` come from `wait4` on each step's process (`evidence/scripts/meas.py`). Raw figures are in
`evidence/steps-*.txt`.

The two full runs started together and ran concurrently on 4 cores, so the c59b562c run shared the machine with the
67bae482 run for its whole duration.

| Step | 67bae482 wall | c59b562c wall | 67bae482 peak | c59b562c peak |
|---|---|---|---|---|
| 1 self-test | 0.1 s | 0.2 s | 25 MB | 25 MB |
| 2 purity | 0.7 s | 0.7 s | 39 MB | 39 MB |
| 3 synthetic | 0.6 s | 0.5 s | 28 MB | 29 MB |
| 4 conformance | 6.5 s | 6.7 s (4 more controls) | 34 MB | 35 MB |
| 5 A1 conformance | 57.8 s | 56.5 s | 198 MB | 203 MB |
| 6 A1 controls | **4600.8 s** | **1180.9 s** | **1.20 GB** | **1.48 GB** |
| of which sweeps | 4151.5 s | 752.9 s | | |
| coverage / terms / v / exec / trees | 30.5 / 29.5 / 99.7 / 156.1 / 60.7 s | 19.6 / 29.8 / 98.6 / 151.5 / 56.8 s | | |
| total, steps 1–6 | ~77.8 min | ~20.8 min | | |

- **Runtime:** this confirms the writer's figures: 4647 s → 1175 s, sweeps 4182 s → 747 s.
- **Memory:** the peak rises by **0.28 GB (+23%)**. The writer's "before" peak was a sampled lower bound (≥ 1.20 GB);
  the exact figure is 1.20 GB. The increase is bounded by the commits a run reads and fits a 16 GB hosted runner. No
  eviction was added, as authorized.

## 7. Governance and record integrity

**Commits:**
- each of the four commits has a single parent and is a linear child of 67bae482;
- author and committer are `Claude <<commit-identity-email>>`, with an SSH signature;
- each message ends with the `Co-Authored-By` and `Claude-Session` lines;
- the base 67bae482 object is unchanged.

**Pins:**
- The class record at c59b562c has 53 pins. They equal `git ls-tree -r` of the landing paths less the record itself:
  every `git_blob` and `blob_sha256` matches and every mode is 100644.
- The b45be784 staged configuration pins 43 tool files, all matching c59b562c.

**Staged configuration restoration:**
- `impl-v6.0e/staging/…/retirement-config.json` is byte-exact 5af8f07e again.
- The first 57 lines of the current `impl-v6.0e/MANIFEST.sha256` hash to e65ee36d…, the manifest the 67bae482 review
  recorded. Every current entry verifies, so the new entries were only appended.
- The 67bae482 evidence (`logs/full`, head 67bae482, staged 5af8f07e) is intact, and my independent run reproduces it
  exactly (section 3).

## Findings

There are no blocking findings. None of the nits below changes the verdict.

- **N-1 (writer's record overstates coverage).** `PERF-FIX.md`'s K08 row says in-memory submodule entries are
  "covered by TR51 through `Overlay`". The mutants refute this for the exclusion itself: K08o survives at c59b562c and
  B08o survives at 67bae482. The statement should be corrected to say that neither reader's submodule exclusion in
  `paths` has an isolating control, at either commit. This gap existed before the correction (section 5). Adding a
  control for it would be a new verification requirement, so I record it here and do not require it.
- **N-2 (equality accounting).** The writer's comparison reduced the purity row to `(outcome, findings)`. Compared
  whole, it differs by construction (the configuration hash and the F stand-in). The writer's 340 identical / 2
  differing and my 339 / 3 describe the same results.
- **N-3 (memory baseline).** `PERF-FIX.md` gives the before peak as ≥ 1.20 GB, sampled. The exact `ru_maxrss` is
  1.20 GB, so the increase is +0.28 GB.
- **N-4 (record process).** The writer's generator overwrote the reviewed staged configuration in place between
  14:17:39 and 15:05; this is the main reviewer's O-1. The file is now restored byte-exactly and the base evidence was
  not affected. The writer's own `before-steps.txt` timings (14:19) fall inside that window, and their inputs cannot be
  confirmed from the record. They are superseded by section 6.
- **Informational.** A `MappingProxyType` can be bypassed only through interpreter introspection, not through the
  caller API. R12 survives by design.

## Files

- `review.md` (this file) and `MANIFEST.sha256`.
- `evidence/`:
  - comparisons: `cmp-before-after.json`, `cmp-writerbefore-vs-minebefore.json`, `cmp-writerafter-vs-mineafter.json`,
    `rtl2.json`;
  - corruption: `corruption.json`;
  - per-step measurements: `steps-*.txt`, `a1-summary-*.json`, `inputs-*.txt`;
  - `mutation/`: stdout and a summary of each campaign;
  - `scripts/`: the run, measurement, comparison, corruption and mutation scripts;
  - `INVALID-DIAGNOSTIC.txt`.
- Full run outputs remain in `workspace/rv-perf/v2/` (`out-*`, `logs-*`, `mut-*`).

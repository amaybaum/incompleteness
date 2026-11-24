# The reader-cache correction (bounded performance fix on the v6.0e implementation)

Writer's record, 2026-11-24. Local only: no push, pull request, GitHub write, CI or dispatch; additive single-parent
commits on `tools/ledger-coverage-20261123`; the shared store only read. The implementation commit
67bae482b5842ede9e8430da841bd78563b0f97d and its objects are unchanged (its independent review proceeds on it); the
correction lies in the four commits on top of it.

Authority (owner `amaybaum`, 2026-11-24, in session, relayed by the coordinating session; no comment id held by this
writer): "Let's fix the performance bug." and "Authorize only the described paths() caching correction as a bounded
exception to the implementation hold. …" (with the conditions quoted in the task), and the earlier guidance "caching
already verified immutable Git objects, while preserving the integrity guarantees"; "Correctness first".

## Commits

| Commit | Content |
|---|---|
| 661bcbedcf601a3f0c1fd035d26cf08775ca3e8d | `engine/gitobj.py`: per-commit entry and path maps cached as read-only views; controls GV-CACHE, GV-CACHE-IMMUTABLE |
| 71a17c735e24df43e768c6c6e3856de4415ef3e6 | class record re-pin |
| f5c1bd3f73b4d5d38fd4f24108a8f8334dbf2424 | controls GV-CACHE-KEY, GV-CACHE-AFTER-READ (owner conditions) |
| **c59b562c168dc24706f51b791ec526dd897c909d** | class record re-pin (final commit) |

Staged A1 configuration regenerated: sha256 **b45be784875043fe6501fc7644aced019a57b46583495a7693f3d00d2b00a078**
(the `tool` pins of the final commit), kept at
`staging-c59b562c/verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json`; class record 53
pins, equal to `git ls-files -s` of the landing paths. The generator writes to `staging/…`; the final "after" run read
the b45be784 file there, and the file at `staging/…` was then restored to the 67bae482 configuration (5af8f07e…, as
`MANIFEST.sha256` records it for the reviewed commit). The supplementary run at 71a17c73 (`logs/perf/after-full-71a17c73`)
used that commit's regenerated configuration (eb778ed5…), not kept; it is timing evidence only.

## The change (only `engine/gitobj.py` among the tool's engine files)

- `GitRepo.entries(cid)`: the `{path: (mode, id)}` map is built as before, by walking verified tree objects, and stored
  in `_entries[cid]` **only after the whole walk succeeds**, as a `types.MappingProxyType` view.
- `GitRepo.paths(cid)`: the `{path: blob id}` map (submodule entries excluded, as before) is built once per full commit
  id from that verified entry map and stored in `_paths[cid]` as a `MappingProxyType` view. Before, it was rebuilt on
  every call.
- `Overlay.entries`, `Overlay.paths` for in-memory commits: the same, keyed by the in-memory commit id; for base
  commits the base reader's views are returned.

Why the views are safe and fast: a `MappingProxyType` is a zero-copy read-only proxy (no per-call copy); it refuses
item assignment, deletion, `pop`, `update` and `clear`; the dict behind it is held only in the reader's private cache
and never returned; its values are immutable (strings, tuples). A caller that needs a mutable map makes its own copy,
which cannot reach the cache. No caller in the tool or the runners mutated these maps (checked by search before the
change; GV-CACHE-IMMUTABLE checks it at run time).

What did not change: every object is still requested by full id and its id recomputed on first read (`_batch`,
unchanged); replace refs, grafts and commit-graph are still never consulted (unchanged reader environment and parsing);
a missing or corrupted object still raises the same unresolvable-object error at the same read. The caches are filled
only from objects the reader has verified, and only after the read that verifies them; nothing is read from a cache
that was not verified first. "Caching removes redundant computation, not verification."

## Corruption cases (stated only as tested)

| Case | Before (67bae482) | After (cache) | Evidence |
|---|---|---|---|
| object corrupted before the first read, commit's paths not yet listed | refused | refused | `logs/perf/prepost-corruption.json`; GV-CACHE ("blob, paths not cached") |
| object corrupted before the first read, commit's paths already listed (cached) | refused | refused | same; GV-CACHE ("blob, paths already cached", and a second read) |
| tree corrupted before the first read | refused on every call | refused on every call; the refusal caches nothing | GV-CACHE ("tree, first/second paths call", entries); mutant K04 |
| tool run reading a corrupted blob | ERROR 65 | ERROR 65 (UNRESOLVABLE) | GV4, GV-CACHE |
| store corrupted **after** a successful read, same reader reads again | **not re-detected**: served the verified bytes from the object cache | **not re-detected**: same | `prepost-corruption.json`; GV-CACHE-AFTER-READ |
| store corrupted after a successful read, a new reader | refused | refused | same |

The reader has always kept every verified object for its lifetime (`_objs`); the path-map cache adds no new
exposure: it lists ids, and every object read through it is still verified on its first read (mutant K07). No
detection of corruption that occurs after a successful read within one reader's lifetime is claimed, before or after.

## Controls added (implementation controls)

| Id | What it shows | Status |
|---|---|---|
| GV-CACHE | a corrupted object refused with and without the commit's paths cached; a corrupted tree refused on every call, nothing cached by the refusal; the tool run ERROR | PASS |
| GV-CACHE-IMMUTABLE | every mutation of the GitRepo and Overlay views refused; a mutated copy leaves the cache unchanged; the same view returned | PASS |
| GV-CACHE-KEY | each of seven commits' cached maps equals that commit's `git ls-tree` (replacement disabled) in both read orders; seven distinct maps; X's and M's views differ; two in-memory commits each see only their own file | PASS |
| GV-CACHE-AFTER-READ | after a successful read, the same reader serves the verified bytes and the same path map; a new reader refuses | PASS |

## Equality of verification outcomes (full repro, all steps)

Before: the run of `logs/repro.sh` at 67bae482 (`logs/full/`). After: `logs/perf/repro-after.sh` at c59b562c
(`logs/perf/after-full/`). `logs/perf/compare.py` compares every control's (id, status, actual) across self-test,
synthetic, conformance, A1 conformance, A1 controls (sweeps included) and the staged purity lint, with timing fields
removed and run-directory paths normalized (`logs/perf/compare-final.json`):

- 342 controls before, 346 after; **340 identical in id, status and actual**; 4 added (the GV-CACHE controls, all PASS);
  0 status changes; 0 controls absent after.
- 2 differ in `actual` only, both by construction: `synthetic/_Y8_engine` (the engine's own blob hash, which the change
  of `gitobj.py` changes) and `a1-controls/RT-L2` (it predicts `main` plus the tool landing, whose blobs changed):
  `logs/perf/compare_rtl2.py` finds every RT-L2 difference to be the predicted commit id or the blob of one of the
  three changed landing paths (`gitobj.py`, `conformance_controls.py`, the class record), 0 unexplained
  (`compare-final-rtl2.json`). RT-L2 is PASS in both.
- Every integrity control is unchanged: GV1-GV7 (with GV6-disk), EI1-EI15, TR*, X10, X11 PASS before and after with
  identical actuals; the release gate's failing rows are the same environment-bound rows.

## Runtime and memory, before and after

Wall time and peak memory per step. After: `logs/perf/after-steps.txt` (`measure.py`: wall clock and `ru_maxrss` of
the step's processes). Before, steps 1-5: the 67bae482 tool from an extraction, measured the same way
(`before-steps.txt`); before, step 6: the 67bae482 run (`logs/full/`; memory sampled from /proc every 10 s, so a
lower bound).

| Step | Before wall | After wall | Before peak | After peak |
|---|---|---|---|---|
| 1 self-test | 0.1 s | 0.1 s | 25 MB | 26 MB |
| 2 staged purity lint | 0.7 s | 0.7 s | 39 MB | 38 MB |
| 3 synthetic | 0.5 s | 0.5 s | 29 MB | 29 MB |
| 4 conformance | 7.0 s | 7.3 s (4 more controls) | 34 MB | 35 MB |
| 5 A1 conformance | 58.3 s | 57.2 s | 198 MB | 202 MB |
| 6 A1 controls | **4647 s** | **1175 s** | **≥ 1.20 GB** (sampled) | **1.48 GB** (exact) |
| of which sweeps SW1/SW2 | 4182 s | 747 s | | |
| of which coverage, terms, v, exec, trees | 31, 31, 101, 162, 66 s | 20, 30, 99, 149, 58 s | | |
| 7 release gate | not timed | 59.6 s | | 51 MB |
| total | ~79 min | ~22 min | | |

Call counts (cProfile of the A1 coverage group, `logs/perf/coverage-profile.txt` before, `coverage-after.prof` after):
`GitRepo.paths` 46,940 calls, 10.733 s own time before and 0.014 s after (cumulative 0.064 s); `Overlay.paths` 45,465
calls, 0.054 s cumulative after; `blob_id` 46,281 calls, 0.088 s cumulative after. The group went from 35.8 s to
24.4 s; the rest is profile matching, unchanged.

Memory: the A1 step's peak rises by about 0.3 GB at most (1.48 GB exact after against ≥ 1.20 GB sampled before),
because one path map per commit is kept for the reader's lifetime, including the in-memory commits the sweeps derive.
It is bounded by the commits a run reads and well within a hosted runner's 16 GB; no eviction was added (no further
change is authorized). Total runtime fits the 360-minute default job limit with a wide margin.

## Mutation (`mut/runK/`; harness `mut/scripts/mutate_cache.py`, mutants `mutants_cache.py`)

8 mutants of the cache code, run against self-test, synthetic and conformance (32 s): **7 killed, 1 survived**.

| Mutant | Rule | Result |
|---|---|---|
| K01 | `GitRepo.paths` returns a read-only view | killed (GV-CACHE-IMMUTABLE and its group) |
| K02 | `GitRepo.entries` returns a read-only view | killed (same) |
| K03 | the path cache keyed by the commit id | killed (GV-CACHE-KEY, G7) |
| K04 | a refused tree caches nothing | killed (GV-CACHE) |
| K05 | the overlay path cache keyed by the commit id | killed (many controls) |
| K06 | the overlay entry map a read-only copy | killed (GV-CACHE-IMMUTABLE) |
| K07 | an object listed in a cached map still verified on first read | killed (GV-CACHE) |
| K08 | the path map excludes submodule entries | **survived**: no on-disk tree in the controls holds a gitlink; the exclusion is the reader's unchanged pre-fix behaviour, moved into the cached builder; in-memory submodule entries are covered by TR51 through `Overlay` |

## Not done

No other optimization or change. The focused independent review of the correction commits (661bcbed to c59b562c) is
pending.

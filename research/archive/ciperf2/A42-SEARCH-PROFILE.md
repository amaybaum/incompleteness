# A42 exclusion shards: performance profile of `cubes:0`, `dfs:4`, `paths`

Diagnosis only. Nothing in `/home/user/incompleteness` was edited. Everything ran on a detached scratch worktree at
`6d0abf6b` (`ciperf2/wt`) with `PYTHONDONTWRITEBYTECODE=1`, Python 3.11.15, numpy 2.4.6, python-sat 1.9.dev15
(the CI pins). The container has 4 vCPUs and 15 GB; at most two heavy processes ran at once.

## Summary

| part | CI (last dispatch) | local, no profiler | local, cProfile | where the time goes | verdict |
|---|---|---|---|---|---|
| `cubes:0` | 941 s | 1284 s | 1311 s | 97.6 % inside CaDiCaL `solve` (C++); cube 0 (m = 1) alone takes 671 s | **INTRINSIC** |
| `dfs:4` | 874 s | 985 s | 1086 s | Python and numpy per-call overhead in the DFS (722,178 nodes); two row sets account for 44 % | **INTRINSIC search with removable bookkeeping**: no single hotspot; prototype −43 % with identical counts |
| `paths` | 812 s | 668 s | (r2a 519 s + r2b2 1785 s) | r2b2 457 s: `Fraction.__hash__` in `prop_partition` of the landed A41 independent probe | **CLEAR HOTSPOT** (Fraction-keyed dict); prototype r2b2 457 → 164 s with byte-identical output |

The hotspots in `paths` are in the landed A41 probes (`dita_index_map_independent.py`, `dita_index_map_probe.py`).
A42 executes them whole and unmodified as its C0 control. A fix there is a change to A41's landed code, made the way
CI-PERF-1 changed the A41 hulls H2, and it also speeds up A41's own `probes_a41_*` jobs. A42's own `a42/` tools need no
change for the `paths` gain.

Runner variance: all three parts are single-threaded and CPU-bound (user ≈ wall), use little memory, do no I/O, and do a
deterministic amount of work. The 30–70 % swings are therefore runner throughput, not algorithmic variation (§4).

***

## 1. `cubes:0`: the no-zero-line SAT cubes [0::3]

**Code path.** `part_cubes(0)` imports `sat42.Enc` → `pairtypes` → `dfs42` → `lib42`. `lib42` executes the head of the
landed act-37 probe: the stabilizer, `stab_pairs`, Fraction arithmetic, a one-off cost of about 11–19 s. It then builds
the 26 cube representatives (orbit reduction under the 32-element row-0 stabilizer, which is cheap). For cubes
0, 3, …, 24 it builds a fresh `Enc` (`straight`, `mode0`, `lines_ge(m)`, `support_le(39)`, plus 16 unit clauses
for y0) and runs `Cadical153(bootstrap_with=…).solve()`. No subprocesses.

**Profile (cProfile, 1311 s wall).**

| function | calls | tottime | share |
|---|---|---|---|
| `pysolvers.cadical153_solve` | 9 | 1279.1 s | 97.6 % |
| `lib42` import (probe-37 head, Fraction `stab_pairs`) | 1 | 18.1 s cum | 1.4 % |
| `Enc.straight` (encoding, incl. `pair_structure` numpy masks) | 9 | 8.2 s cum | 0.6 % |
| CNF append / `add_clause` | 2.4 M | ≈ 5 s | 0.4 % |

A native backtrace (gdb) taken mid-run is in `CaDiCaL153::Internal::propagate()` under `cdcl_loop_with_inprocessing`.

**Per cube (instrumented, unprofiled, 1284 s wall).** Each formula has 90.5k–91.4k variables and 270–272k clauses.
Encoding takes about 0.4 s and loading about 0.1 s per cube.

| cube | m | solve | conflicts | propagations |
|---|---|---|---|---|
| 0 | 1 | 671.0 s | 2,152,405 | 3.54 e9 |
| 3 | 2 | 57.7 s | 314,101 | 4.03 e8 |
| 6 | 2 | 69.6 s | 365,484 | 4.72 e8 |
| 9 | 2 | 66.1 s | 386,024 | 4.41 e8 |
| 12 | 2 | 106.6 s | 546,836 | 7.20 e8 |
| 15 | 2 | 58.4 s | 318,547 | 4.04 e8 |
| 18 | 2 | 91.4 s | 488,517 | 6.38 e8 |
| 21 | 2 | 68.8 s | 386,082 | 4.72 e8 |
| 24 | 2 | 84.4 s | 452,562 | 5.82 e8 |

**Determinism.** Cubes 3 and 15 were re-solved. Restarts, conflicts, decisions and propagations were identical, and
solve times were 56.95 / 57.71 s and 59.77 / 58.39 s. CaDiCaL's search here is a fixed function of the clause list,
so timing variation is purely the machine.

**Verdict: INTRINSIC.** Python, exact arithmetic and encoding together account for under 3 %. The remaining levers all
change the computation the preregistration froze, so none of them is a CI-PERF change:

- a different solver or options;
- a different encoding, e.g. a cardinality encoding other than seqcounter or totalizer;
- splitting cube 0 further, which changes the asserted "26 cubes (m = 1: 2, m = 2: 24)".

The one structural observation is shard balance: cube 0 alone is 52 % of this shard. A re-split is a new freeze, not a
performance fix.

***

## 2. `dfs:4`: the ≤ 39 zero-row DFS on `Rle13_39[4::6]`

**Code path.** `ensure_msize()` runs `cvsize.py` as a subprocess (15 s) because `msize.npy` is not in the checkout,
then checks its sha256. `part_dfs(4)` then calls `dfsR2.RSearch2(R, 39, True).run()` for each of the 915 row sets.
`__init__` builds the row candidates with `dfsR.row_cands`. Per row and per structure (18) it computes
`X @ M.T` in int64, casts it to int8 byte keys and takes `np.unique` ids. `_rec` is the DFS:

1. Lemma NS test (`_dita_subtree`, 18 structures × free rows);
2. budget slack;
3. branch row = fewest candidates;
4. per child: `nf` = 18 small matmuls, then `compat` filtering of every other row's candidates through the exact
   `VT` vanishing tables.

There are no SAT calls and no Fractions in the hot path: the Fraction calls in the profile are the one-off `lib42`
import.

**Profile (cProfile, 1086 s wall; totals 722,178 nodes, 72,305 pruned, 0 leaves, as frozen).**

| function | calls | tottime | cumtime | what it is |
|---|---|---|---|---|
| `dfs42.compat` | 6,303,376 | 287.2 | 287.2 | 4 fancy-index lookups into 64 KB bool tables per call (the pruning work itself) |
| `RSearch2.__init__` | 915 | 188.4 | 260.8 | int64 `X @ M.T` (numpy `LONG_matmul`, no BLAS for ints) × 18 per row, plus `np.unique` (48 s) |
| `_rec` `nf` dictcomp (dfsR2.py:68) | 1,227,140 | 187.6 | 187.6 | 18 small int64 matmuls per child, evaluated **before** the compat filter and also at leaves |
| `_rec` (self) | 722,178 | 142.5 | 790.9 | DFS bookkeeping |
| `_dita_subtree` | 722,178 | 81.7 | 152.8 | 18 × rows `ids.min()/max()` + matmuls |
| ndarray `min`/`max`/`any` | 44 M | ≈ 50 | ≈ 75 | small-array call overhead |
| import (`lib42` head) + `cvsize.py` | | | ≈ 34 | one-off |

Per-row-set cost is very skewed. 0xfafa and 0xafaf (248k nodes each) take 44 % of the shard. With 0xbfaf and 0x5fdf
(24k nodes, about 3 ms/node, large candidate arrays) the top four take 61 %. 97 of the 915 row sets take 92 %.
Shard 4 also holds the largest frozen node count of the six (722k against 152k–472k), so it is the slowest DFS shard by
construction. Rebalancing would change the per-shard `DFS_COUNTS` the probe asserts, so it needs a new freeze.

**Classification.** Python and numpy call overhead on small arrays, around a search whose size is fixed (the asserted
node and prune counts). There is no exact-arithmetic or SAT component. `compat` (26 %) is the essential pruning work.
`nf` (17 %), `_dita_subtree` (14 %) and `__init__` (24 %) are bookkeeping that is computed redundantly.

**Prototype (scratch `dfs_proto.py`, class `RSearch2Fast`; the landed classes are untouched).** It keeps the same
search order, the same `compat`, the same int8 byte-key ids and the same Lemma NS predicate. Only the bookkeeping
changes:

- (a) Stack the 18 relaxed structure matrices into one (2726 × 256) matrix. Per row, keep only the equations that
  involve that row (235–1092 of 2726), and compute each candidate's contribution once in `__init__` with one matmul
  instead of 18.
- (b) Make `fixedsum` one concatenated int64 vector. The child update becomes `nf[NZ[i]] += T[i][n]`, computed
  lazily after the compat filter succeeds and never at leaves.
- (c) `_dita_subtree` becomes per free row: one `(min == max)` over an (ncand × 18) id table, AND-ed across rows, then
  a zero test per surviving segment. This is the same existence predicate as the landed loop.

Result on all 915 row sets of shard 4, old and new run in the same process on the same inputs:

| | time | nodes | pruned | leaves |
|---|---|---|---|---|
| landed `RSearch2` | 984.7 s | 722,178 | 72,305 | 0 |
| prototype | 560.5 s | 722,178 | 72,305 | 0 |

There were **0 per-row-set mismatches** in (nodes, pruned, leaves, sorted leaf matrices). The leaf comparison is
vacuous on this shard because it has 0 leaves. The gain is concentrated in the heavy pruning sets: 0xfafa went from 218
to 116 s. The compat-bound sets gain about 15 %.

**Countercontrols (the per-row-set count comparison is not vacuous, but it is sparse).** Two mutants were run over the
335 shard-4 row sets that prune, excluding the two heaviest:

- **M1** prunes on id-constancy alone. This is dfsR2's own `BROKEN` mode.
- **M2** drops the assigned rows' contribution (`fixedsum = 0`).

M1 changed the counts on 8 row sets and M2 on 7, e.g. 0x2f2f went from (9621, 1032) to M1 (117, 24) and M2 (1941, 264).
On the other ~327 row sets both mutants give the landed counts, including 0x7777, 0xbfbe and 0xd7d7. A rewrite of the
`fixedsum` bookkeeping is therefore exercised by only a few percent of row sets. Equivalence evidence must cover every
row set of every shard, not a sample.

**Cost of the prototype.** Peak RSS rises from 262 MB to about 1.1 GB because the contribution tables are int64. Every
contribution is bounded by 4 in absolute value (max per-row-block L1 norm of the stacked matrix), and every structure
sum by 8, so int8 storage is exact. A landed version should store int8 with that bound asserted as a checkpoint.

**Verdict: INTRINSIC search; no single algorithmic hotspot.** About 40 % of the shard is removable bookkeeping. That is
a ~1.75× gain on `dfs:4`, and less on compat-bound shards. It is a real but moderate data-structure win, not a CI-PERF-1
style dominant inefficiency.

***

## 3. `paths`: R2 path A (`r2a_landed.py`) and path B(ii) (`r2b2_census.py`)

**Code path.** `part_paths` runs two subprocesses.

- **`r2a_landed.py`** execs the landed A41 production probe `dita_index_map_probe.py` whole (C0 replay against act
  41's `measurements.json`). It then runs `arc()` on 10 exponent matrices (E40, EE, PA, P, Q, T, gauged E40, three
  pairwise sums). Each call runs `orientations` → `enumerate_candidates` → `A41Family` → `a41_arc_summary`.
- **`r2b2_census.py`** execs the landed independent probe `dita_index_map_independent.py` whole (C0), then
  `a41_census` at 6 exact points on E40's arc.

**Wall time (unprofiled, 668 s):** r2a 211 s (the landed production probe alone 116 s), r2b2 457 s.

### 3a. r2b2: CLEAR HOTSPOT

Profile (cProfile, 1785 s; Python-level `__hash__` makes cProfile overhead large here):

| function | calls | tottime | cumtime |
|---|---|---|---|
| `fractions.Fraction.__hash__` | **770,792,448** | 535.2 | **917.2 (51 %)** |
| `builtins.pow` (inside `Fraction.__hash__`: modular inverse of the denominator, every call) | 770,792,448 | 217.4 | 217.4 |
| `dict.setdefault` (in `prop_partition`) | 51.8 M | 137.5 | 1063.7 |
| `prop_partition` | 3,228,580 | 95.4 | 1228.7 (69 %) |
| `dita_orientations` | 654 | 8.7 | 1353.3 |
| `is_unitary_s` (Fraction Gaussian arithmetic) | 21,728 | 11.3 | 403.2 |

`ratio_table` stores each entry as `G.key()`, a pair of `Fraction`s. `prop_partition` then groups the 16 rows by
`tuple(r[s] for s in S)` for every column subset S (C(16, n) for n = 2, 4, 8, i.e. 14,810 subsets), 12 times per matrix.
Every dict insertion re-hashes up to 16 Fractions, and Python 3.11's `Fraction.__hash__` computes
`pow(denominator, -1, P)` on each call. This is the same kind of defect as CI-PERF-1: exact rational objects used where
only equality is needed.

**Rewrite sketch.** Intern the keys once per table, in `ratio_table` only:

```python
def ratio_table(H):
    ids = {}   # each distinct key -> a small int; injective within this table
    return [[[ids.setdefault((H[i][s] * H[i][s0].conj()).key(), len(ids)) for s in range(16)] for s0 in range(16)] for i in range(16)]
```

`prop_partition` only compares key tuples for equality within one table, and its output (sorted row-index tuples) does
not contain the keys. An injective relabelling therefore leaves every output unchanged. The fix is exact by
construction: no floats, no change to any arithmetic.

**Prototype evidence (scratch copies `verification/lean/_proto_independent.py` and `a42/_proto_r2b2.py` in the scratch
worktree):**

- r2b2 wall time fell from **457 s to 164 s**. The independent probe's C0 replay alone took 146 s.
- The patched landed probe prints `dita_index_map_independent: OK -- REPLAYED: 42 named test cases, 38 distinct
  matrices`, an elementwise replay against act 41's `measurements.json`.
- `r2b2.json` is byte-identical, old against new (`cmp`).
- Per-call control (`intern_control.py`): for all 38 distinct named matrices × 2 forms × 14,810 subsets (1,125,560
  calls), `prop_partition` on the interned table equals the landed output **in every call** (0 differences).
  `prop_partition` time over those calls fell from 112.2 s to 14.0 s.
- Countercontrol: a deliberately non-injective interning (id mod 7) differs in 47,731 of those calls, so the per-call
  comparison is not vacuous.

**Finding on the end-to-end replay.** The same mod-7 mutant **still prints `OK -- REPLAYED`** end to end. The
downstream exact rank-1 and unitarity checks absorb the spurious merges. The end-to-end replay is therefore *not* a
sufficient control for this rewrite. The per-call `prop_partition` comparison is the decisive one. (Mod 2 instead blows
up the partition search and does not finish in 10 minutes.)

**Residual after the fix.** In the profile, `is_unitary_s` is 403 of 716 s: Fraction Gaussian multiply-adds in
`a41_valid_alignments`, recomputed per alignment combo. A second, smaller exact-arithmetic target follows; it is not
prototyped:

- memoize the per-(refs, c) unitarity test, or
- carry each matrix as Gaussian integers over a common denominator, and compare `Σ` against `s·D²` in integers.

Its old/new evidence would be the same per-call design.

**Cross-propagation.** The identical `ratio_table`/`prop_partition` pair is in eight landed probes:
`dita_local_escape_probe`, `dita_index_map_hulls`, `dita_arc_exclusivity_probe` (whose head every A42 part imports
through `lib42`), `dita_hierarchy_probe`, `dita_index_map_probe`, `dita_torus_probe`, `dita_index_map_independent`
and `dita_torus_locus_probe`. Any of them that run `dita_orientations` heavily pays the same Fraction-hash cost.

### 3b. r2a: moderate hotspot (`enumerate_candidates`)

Profile (cProfile, 519 s):

| function | calls | tottime | cumtime |
|---|---|---|---|
| `enumerate_candidates` | 14 | 103.1 | 260.9 (10 of them from r2a's own `arc()`: 186 s) |
| its `tuple(sorted(set(de[p][j] for j in Sb)))` genexpr | 421 M steps | 49.5 | 49.5 |
| `pbf` (flat cache lookup per subset × pair) | 49.8 M | 38.0 | 50.6 |
| `a41_orbits` / `a41_img` (landed production probe, A41-3) | 9 / 6.5 M | | 153.2 |
| `prop_partition` (same Fraction-hash pattern) | 177,720 | 5.2 | 67.4 |

`enumerate_candidates` rebuilds, for each block subset Sb (1,820 + 120 + 12,870 per form) and each of the 120 row
pairs, the sorted set of that pair's value tuples. These are integer tuples with no Fractions.

**Sketch** (scratch `enum_proto.py`):

- Give each pair's distinct values ids in sorted order.
- Compute every subset's value set as a numpy bitwise-OR of column bits over all subsets at once.
- Resolve each (pair, mask) to its flat once.

The partition/cover recursion and every insertion order are kept.

Evidence: on 12 orientation inputs (the 10 r2a arcs plus H3 and W), the old and new `cands` match exactly (keys,
flats, insertion order) and so do `stats`, with 0 mismatches. Time fell from **109.9 s to 34.5 s**. In `paths` this
saves about 60 s of r2a. `a41_orbits` computes every image up to three times (orbit sweep, closure test, Burnside
count). Computing each image once is a further safe saving of tens of seconds; it is not prototyped.

**Estimated `paths` with both fixes: about 668 → 315 s locally (about −50 %).** Most of that is the r2b2 interning.

***

## 4. Runner variance (the 30–70 % swings)

- **All three parts are single-threaded and CPU-bound.** user/wall is 1263/1284 s (cubes), 1061/1086 s (dfs) and
  657/668 s (paths). Voluntary context switches are near 0, there are no major faults, and peak RSS is 71–262 MB.
  Memory capacity and I/O play no part.
- **The work is deterministic.** DFS node and prune counts are asserted per shard, and CaDiCaL conflicts are identical
  across reruns. Local reruns differed by 1–2 %.
- **The local-to-CI ratio differs by workload.** CI was 1.36× faster than this container on `cubes:0`, 1.13× faster
  on `dfs:4`, and 0.82× (slower) on `paths`. With identical work, that pattern points to each shard landing on a
  different host. SAT propagation (3.5 e9 propagations in cube 0, watch lists over 270k clauses plus learnt clauses)
  is sensitive to cache and memory latency. The Python shards are sensitive to clock and IPC.
- **Inference, not measured:** the CI logs print no CPU model. The swings are consistent with GitHub's `ubuntu-latest`
  runners being shared VMs on mixed host generations and neighbour load, and they are fully explained by single-thread
  throughput differences. No algorithmic source of variance exists in these three parts. To confirm, a CI-PERF-2
  should print `lscpu` (model, MHz, L2/L3) at the top of each shard.

***

## 5. What a CI-PERF-2 would need as evidence

Ordered by yield. Every rewrite must leave each asserted value untouched, and must show old/new equivalence on the same
inputs with a countercontrol that bites.

1. **Intern ratio keys in `ratio_table`** (landed A41 independent probe, and the production probe; optionally the other
   six carriers). This gives about −290 s on `paths` and speeds up `probes_a41_independent` as well.
   - **Per-call control:** for every matrix the probe processes (all distinct named matrices, both forms, and the six
     r2b2 points), `prop_partition` old against new on all 14,810 subsets gives 0 differences. Recorded here:
     1,125,560 calls, 0 differences.
   - **Countercontrol:** a non-injective interning must differ in that comparison (mod 7: 47,731 differences). The
     end-to-end replay alone does **not** detect it.
   - **End to end:** the patched probe prints `OK -- REPLAYED` and the identical `A41-MEASUREMENTS`/`A41-SHA256`
     lines. `r2a.json` and `r2b2.json` are byte-identical, and A42 `paths` passes all 9 checks.
   - **Scope note:** this edits a landed A41 file executed as A42's C0. The round must list both rounds' affected
     records and run the A41 jobs as well.
2. **`enumerate_candidates` value-set vectorization** (landed production probe). This saves about 60 s on `paths` plus
   the A41 production job.
   - **Control:** old/new `(cands items in insertion order, stats)` identical on every orientation input the corpus
     feeds it: the 12 used here, plus A41's own H3, W and act-38 inputs.
   - **Countercontrol:** e.g. ids assigned out of sorted order, which must change flat keys or order.
3. **`dfsR2` bookkeeping** (A42's own `a42/dfsR2.py`; about −40 % on `dfs:4`, less on the other DFS shards).
   - **Control:** per-row-set (nodes, pruned, leaves, sorted leaf matrices) identical on **all 5,494** row sets, i.e.
     all six shards. The probe's `DFS_COUNTS` and `nonDita == 0` checks still pass.
   - **Countercontrols:** M1 (`BROKEN`) and M2 (dropped `fixedsum`) must each change at least one row set. They change
     only 7–8 of 335 pruning sets on shard 4, which is why sampling is not enough.
   - **Precondition:** int8 table storage gated by the asserted bound (row-block L1 ≤ 4, structure L1 ≤ 8). Peak memory
     is measured as a checkpoint.
4. **`cubes`**: nothing. It is intrinsic, and every lever changes the frozen computation.
5. **Every round:** exact-head CI timings for all 15 A42 shards before and after, with `lscpu` printed, so that a gain
   is not confused with runner variance of 30–70 %.

***

## Files (scratch, `ciperf2/`)

- Profiles: `cubes0.prof`, `dfs4.prof`, `r2a.prof`, `r2b2.prof`, `r2b2_new.prof` (logs `*.log`, timings `*.time`);
  `top.py` renders them.
- `cubes_instr.py` / `cubes_instr.log`: per-cube encode/solve split and CaDiCaL stats.
- `dfs_proto.py`, `dfs4_proto.log`, `dfs4_proto_per.json`, `dfs_counter.py`, `dfs_counter2.py` / `.log`: DFS
  prototype, per-R equivalence and mutants.
- `intern_control.py` / `.log`, `r2b2_old.json`, `r2b2_new.json`, `r2b2_new.log`: interning per-call control and end
  to end. The patched copies live in the scratch worktree as `verification/lean/_proto_independent.py`,
  `_proto_bad_independent.py` and `a42/_proto_r2b2.py`.
- `enum_proto.py` / `.log`: `enumerate_candidates` old/new.
- `paths_np.log` / `.time`: the unprofiled `paths` baseline.

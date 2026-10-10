# CI-PERF-1 — exact-computation acceleration (design note; scratchpad only, not a control plane)

Base: landed KINF-2 main `88bb2641` once its main-push run 36872837599 is green. Nothing here is frozen; this note is
design evidence for a later preregistration.

## Scope

Two implementation rewrites, each result-equivalent to the landed code, plus a re-profile:

1. **A42 `part_n18`** (`verification/lean/dita_support_minimality_probe.py`, shards `n18:0–2`): census indexed by its
   canonical key; `identity_eqs` vectors memoized per (key, alignment); the exact predicate
   `rank(new) = ro ∧ rank(old + new) = ro` computed as "every new row reduces to zero against a fraction-free integer
   echelon basis of `old`, and rank(new) = ro" — the same predicate, a different exact procedure. **Python-int
   normalization is part of the contract**: every row is converted to Python `int` before elimination (`lib42.SMAT`
   rows are numpy `int64`, and int64 elimination silently drops rank when a true nonzero value is a multiple of 2⁶⁴).
   No modular prefilter: measured, it is sound but slower than the exact test it would skip (85.3 s vs 71.5 s on
   `n18:0`), so it is not part of the implementation.
2. **A41 H2** (`verification/lean/dita_index_map_hulls.py`, shard `A41 hulls`): replace the two rational-RREF
   canonicalizations with a faster *independent* exact canonical form (fraction-free integer RREF / Hermite normal form
   of the row space). **H3 is untouched** — its mod-prime buckets plus exact joint rank remain the second, independent
   equality test, and H2 = H3 counts must still agree.
3. **Re-profile** the full dispatch on the rewritten head; reshaping shards is out of scope (more shards may worsen
   runner contention).

Out of scope: receipt-backed reuse (CI-RECEIPTS-1, a separate governance round); any change to what a probe asserts;
pip caching; **the census** (`triples.census()`, ~67 s, repeated in each n18 shard) — deferred until the dispatch
re-profile shows whether it is on the critical path; the three shards run in parallel, so a shared census artifact would
add a dependency barrier while mainly saving CPU. If it becomes critical, `census()` itself is optimized before any
artifact mechanism is considered.

Critical sequence: old/new n18 equivalence (full match lists, all three shards) → freeze the rank rewrite → A41-H2
independent canonicalization → full exact-head re-profile → only then decide on census, DFS, cubes or A41 hulls.

## Hazards and their checkpoints

| hazard | mitigation | checkpoint |
| --- | --- | --- |
| H-1 the rewrite changes a verdict | the probe's asserted values stay byte-identical; old/new run on the same inputs, full match lists compared, not only counts | replay: old and new outputs identical (n18: per-subspace rank and full match list; A41: every printed count, the A41_JSON/SHA, 3,896 hulls) |
| H-2 the new exact test is not the old predicate | equivalence argued in writing (span(new) = span(old) ⇔ both rank conditions) and checked on every candidate, including non-matches | per-candidate verdict equality, old vs new, on all three n18 shards |
| H-3 integer overflow in the exact path | rows normalized to Python `int` before elimination | `int64_control.py`: rows `[[2³², 0], [2³², 2³²]]` as int64 — trusted Fraction rank 2, raw int64 echelon 1, normalized echelon 2 |
| H-4 H2 and H3 collapse into one algorithm | H2's new canonical form must not use H3's prime buckets or joint-rank equality; review of imports and code paths | H2 and H3 code paths disjoint; their counts agree |
| H-5 a control becomes vacuous | every existing control and countercontrol in both probes kept and still exercised | control lines present and PASS in old and new output |
| H-6 the gain is runner noise | design evidence is an unprofiled old/new pair run sequentially on one checkout with `perf_counter` splits (census/index, identity_eqs, rank); cProfile is diagnosis only; then a full dispatch re-profile against the KINF-2 runs (36857990743 / 36862525395 / 36868807299) | per-shard wall time table, old vs new |
| H-7 workflow or shard layout drift | no workflow change in this round | `verify.yml` unchanged |

## Success criteria

- every n18 and A41 assertion unchanged, verdict-for-verdict;
- H2 and H3 independent and agreeing;
- the n18 shards and `A41 hulls` substantially faster in the dispatch re-profile (target set from the local benchmark,
  not assumed);
- full exact-head dispatch replay green at F and E with nothing skipped.

## Local measurements (filled as they finish)

See `n18_bench.py` and `n18_<k>_<mode>.json` beside this note.

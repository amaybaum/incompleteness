# Track B act 42 — the least class support of a non-Diţă straight line in D1: RESULT

**Outcome:** `A42-D1-MINIMUM-40`

> Within D1, the least class support of a non-Diţă straight line is exactly 40. Here a straight line is an integer exponent matrix `E` with `SIG ∘ u^E` complex Hadamard for every unit `u`; its class is its orbit under the gauge, the stabilizer of `SIG` and sign; its class support is the least number of nonzero entries over the class; D1 is the set of classes having a least-support representative with entries in {−1, 0, 1}; and non-Diţă means lying identically in no Diţă structure of `SIG` under act 41's semantics. The value is attained by `E40 = −P + Q − T`, straight by two exact methods, of class support exactly 40 by exact enumeration, and non-Diţă by two independent paths. No class of D1 has class support at most 39 and is non-Diţă: in the zero-row case with at most thirteen nonzero rows by an exact exhaustive search whose every leaf lies in one of eighteen subspaces, each equal by exact rank to the relaxed identity subspace of one of act 41's 976 realizing triples; in the zero-row case with at least fourteen nonzero rows and in the case with no zero line by SAT verdicts (UNSAT) carried without proof logs. Act 38's witness has class support 44. The lemmas of the case split are stated and argued in the preregistration and are not kernel-checked, the general-integer exclusions of the pre-freeze analysis are not re-derived, and nothing is claimed outside D1 or about the class supports 41 to 43 and 45 to 47.

**THE CLAUSE, carried at this mention — the result.**

> Act 42 settles, by exact computation, a case split stated in its preregistration and SAT verdicts carried without proof logs, the least class support of a straight line through the certified rational stratum point that lies identically in no Diţă structure of the point, within the domain D1 of classes having a least-support representative with entries in {−1, 0, 1}; the value is 40. It says nothing about classes outside D1, determines none of the class supports 41 to 43 and 45 to 47, re-derives none of the general-integer exclusions of the pre-freeze analysis, revises no earlier verdict, adopts no line, family or support value as a physical symmetry, principle or law, and leaves `P0` open; nothing here names, endorses or excludes a selection principle.

## The objects

- `D` = `0e87c4a129d91276c10f0438d03c1bcca3a0a3b8` (act 45's landing).
- `F` = `42845052f7ecf62ceb2a9787b9b3eb9c0bb4411a`, designated by the owner; `D` plus the preregistration alone (blob
  `9bb9856b67488b1dab121b133cd53373611a81a2`); attested by the exact-head dispatch run 36662954968, thirteen jobs green.
- Stage 1 = `6062af102153e18de57ab0624c841d0d62f4bd6c`, the single child of `F`: `controls.py`
  (`397f8e70e6af80216efc6c8fce45e7454a3a53b0`), the twenty-two tools under `verification/lean/a42/` with their frozen
  blobs, the probe `verification/lean/dita_support_minimality_probe.py` (`f65ec4fd66f6a50d62cb231734889817aaf68187`) and the frozen workflow
  edit. `C1` was verified before it: the preregistration's blob at `F` is the frozen one.
- `E` — the commit carrying this note and the four frozen `ROADMAP.md` replacements, the single child of stage 1.

## The measurement

The dispatch run 36664005768 on exactly stage 1 (`workflow_dispatch`, attempt 1): all thirty jobs green. Every A42
part printed its frozen summary line, with no failing check:

```text
dita_support_minimality_probe witness: OK -- 11 checks (252s)
dita_support_minimality_probe wlog: OK -- 9 checks (6s)
dita_support_minimality_probe d01span: OK -- 6 checks (344s)
dita_support_minimality_probe paths: OK -- 9 checks (754s)
dita_support_minimality_probe r5: OK -- 2 checks (315s)
dita_support_minimality_probe n18:0: OK -- 7 checks (812s)
dita_support_minimality_probe n18:1: OK -- 7 checks (1256s)
dita_support_minimality_probe n18:2: OK -- 7 checks (1289s)
dita_support_minimality_probe dfs:0: OK -- 4 checks (498s)
dita_support_minimality_probe dfs:1: OK -- 4 checks (528s)
dita_support_minimality_probe dfs:2: OK -- 4 checks (753s)
dita_support_minimality_probe dfs:3: OK -- 4 checks (533s)
dita_support_minimality_probe dfs:4: OK -- 4 checks (917s)
dita_support_minimality_probe dfs:5: OK -- 4 checks (751s)
dita_support_minimality_probe sathr: OK -- 1 checks (354s)
dita_support_minimality_probe cubes:0: OK -- 10 checks (837s)
dita_support_minimality_probe cubes:1: OK -- 10 checks (530s)
dita_support_minimality_probe cubes:2: OK -- 9 checks (178s)
```

- **The six `dfs` shards:** each reported 0 leaves and 0 non-Diţă leaves. Their (nodes, pruned) counts are the frozen
  ones: (151 625, 18 685), (471 631, 46 227), (281 624, 24 040), (428 775, 44 974), (722 178, 72 305) and (277 373, 22 143).
- **The two SAT cases:** `sathr` and the 26 cubes are UNSAT. These verdicts are carried without proof logs.
- **The aggregate:** `Numerical probes` printed `a42_exclusion=success (event workflow_dispatch)`.
- **The release gate** in the `Mathlib bridge` job passed 21 of 21 steps:
  - `lean-axioms`: 5278 named results, no sorry;
  - `v3-receipts`: 18 receipts, all hold;
  - `legacy-records`: 303 records intact.

The pull-request run 36664007382 on the same commit is not evidence for the label; it tested a synthetic merge. It
skipped the exclusion matrix, and the aggregate's skip branch passed with the two every-event A42 shards green. This is
checkpoint `C5`.

The dispatch run at `E` confirms these lines; the label is read off that run under the preregistration's rule.

## Evidence levels

The conclusion rests on three kinds of evidence, never merged:
- exact computation, replayed in CI;
- SAT verdicts from CaDiCaL 1.5.3 through python-sat 1.9.dev15, carried without proof logs;
- the lemmas of the case split, stated and argued in prose in the preregistration, Lemma I among them, with their finite
  ingredients checked exactly by the probe (`wlog`, `lemmas42.py` L3).

There is no kernel layer.

## Departures

None. The implementation is the frozen one, blob for blob. The argv defect found in the first predicted-tree run
(36635398265) was repaired before `F` and is recorded in the preregistration's pre-freeze evidence.

## Scope, as frozen

- Nothing is claimed outside D1, and nothing that makes 40 the least class support over all integer exponent matrices.
- Nothing is claimed about the class supports 41 to 43 or 45 to 47.
- No SAT verdict is presented as certified.
- No general-integer exclusion of the pre-freeze analysis is claimed as re-proved.
- No earlier verdict is revised. Act 38's witness keeps its recorded support 48 in its `{0, 1}` form; its class
  support 44 is a separate statement.
- `P0` stays `OPEN`.

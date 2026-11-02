# Introduction r27: the r26 confirmations (`90705d41`), on base `90705d41`

The scientific confirmation `scientific/GATE1-papers-90705d41.md` is ACCEPT with no findings. The editorial
confirmation `editorial/GATE3-papers-90705d41.md` is ACCEPT WITH CHANGES, with one should-fix and three optional
findings. r27 applies the should-fix and two of the optional findings before the fourth paper-only comprehension test.

**Unchanged:**
- No theorem or corollary statement changed.
- The §2.4 Corollary is byte-identical.
- Every census fingerprint is unchanged. The ledger `line` fields of INTRODUCTION:T-3 (140 → 142),
  INTRODUCTION:C-recurrence-cycle-indivisibility (146 → 148) and INTRODUCTION:T-4 (220 → 222) moved with the
  paragraph split.
- No ID was retired, and main was not merged.

## Finding → change

| # | Finding | Line (r26) | Change |
|---|---|---|---|
| 1 | G3 #1 (should-fix): the fixed-rule point made twice in three sentences | L130 | "It compares starting conditions under one fixed rule." is deleted. The merged sentence the owner kept ("The comparison is about one fixed rule, the same hidden preparation tried from every visible start the world could have, not about the starts a sample happens to contain, …") carries the point, and the example follows the naming of P-divisibility directly |
| 2 | G3 #2 (optional): L138 is one 278-word paragraph | L138 → L138, L140 | Split before "The step from two observed histories with a common endpoint to an *overlap* …": the first paragraph gives the plain definition, the root and the shared prior; the second gives the overlap step, the never-occurring rows and the price. No word changed |
| 3 | G3 #3 (optional): "Precisely:" right after an example | L154 → L156 | Now opens "Stated precisely:"; the scope that follows is unchanged |

Not applied: G3 #4, the recurrence Corollary's break across pp. 8–9, which is cosmetic and needs no source change.

## Checks

- `sh ./build.sh Introduction`: 22 pages, no dropped glyphs.
- Release gate: every step passes except `lean-axioms`, which needs `lake` and runs in CI.
- `coverage_check`: OK (134 canonical statements); the ledger lines match the census.
- `edge_rigidity_probe.py`: ALL CHECKS PASS.

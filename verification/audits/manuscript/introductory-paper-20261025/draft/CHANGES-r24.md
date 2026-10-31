# Introduction r24: the optional findings of the two r23 confirmations (`e87b9e27`), on base `edfc863d`

Both r23 confirmations are ACCEPT: `scientific/GATE1-papers-e87b9e27.md` (O1, O2) and
`editorial/GATE3-papers-e87b9e27.md` (findings 1–4, all optional). r24 applies the four wording findings before the
third paper-only comprehension test, because two of them, raised by both reviewers, touch the recurrence explanation
that the test examines.

**Unchanged:**
- No theorem or corollary statement changed.
- The §2.4 Corollary is byte-identical.
- No line was added or removed, so the ledger is unchanged.
- No ID was retired, and main was not merged.

## Finding → change

| # | Finding | Line | Change |
|---|---|---|---|
| 1 | G3 #1: the order and the recurrence time defined twice in one sentence | L49 | Now reads: "its *order* $L$, the world's *recurrence time*, is the least number of steps after which every configuration has returned to itself, and one such return is a *recurrence*." |
| 2 | G1 O2 = G3 #2: "only" can be misread | L140 | "A *return horizon* is a time $n$ with $\Gamma_n=I$, at which the forecasts from the start return to certainty, whether or not the whole world has returned; $L$ is one, and there may be earlier ones." |
| 3 | G1 O1 = G3 #3: distant antecedent of "sees neither" | L146 | "An observer confined to accessible windows therefore sees neither the late dependence nor the failure of chaining." |
| 4 | G3 #3: a fourth name for the hidden quantity | L118 | "readout-relevant hidden memory, the part of the hidden predictive memory that supports the observed process's dependence on history" |

Not applied: G3 #4, the two single-line widows on pp. 13–14. The fix would need `\widowpenalty` in the shared header,
which this paper does not change.

## Checks

- `sh ./build.sh Introduction`: 21 pages, no dropped glyphs.
- Release gate: every step passes except `lean-axioms`, which needs `lake` and runs in CI.
- `coverage_check`: OK (134 canonical statements).
- `edge_rigidity_probe.py`: ALL CHECKS PASS.

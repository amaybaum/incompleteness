# Introduction r29: the r28 confirmations (`4feca97b`), on base `4feca97b`

The scientific confirmation `scientific/GATE1-papers-4feca97b.md` is ACCEPT with no findings. The editorial
confirmation `editorial/GATE3-papers-4feca97b.md` is ACCEPT WITH CHANGES, with three should-fix findings and one
optional finding. r29 applies findings 2 and 3, and declines finding 1 for the reason below.

**Unchanged:**
- No theorem or corollary statement changed.
- The §2.4 Corollary is byte-identical.
- No line was added or removed, so the ledger is unchanged and its lines match the census.
- No ID was retired, and main was not merged.

## Finding → change

| # | Finding | Line | Change |
|---|---|---|---|
| 2 | G2 says "the rule, not the sample" twice | L140 | The closing "; dropping those rows would then describe the sample rather than the rule" is removed. The sentence now ends "…belong to starts that never happen, as in the different-deck example [Main §2.3]." The reason stays in G2's opening sentence |
| 3 | G3 restates the result a fourth time, and "rather than of any record" overstates | L152 | Now reads: "The failure of chaining is a property of the world's rule, its dynamics with its hidden preparation, rather than of any accessible record: it constrains how such a world can be described, not what accessible data will show [Main §2.3, Scope]." Under a full-support visible prior the failure is equivalent to conditional memory at some order below the recurrence time, which the full-cycle record carries, so the property is independent only of every accessible record. The hypotheses the deleted middle clause repeated are stated at L134, L148 and L150 |

**Declined, finding 1 (G1 at L130).** The proposal folds G1 into the preceding contrast sentence as a clause. The
run-4 evaluation found that L130 gave the reason only as a contrast ("two different deals") and that the reader
restated the hypothesis without its reason; G1 is the positive statement of that reason. G1 stays as written.

## Checks

- `sh ./build.sh Introduction`: 22 pages, no dropped glyphs.
- Release gate: every step passes except `lean-axioms`, which needs `lake` and runs in CI.
- `edge_rigidity_probe.py`: ALL CHECKS PASS.

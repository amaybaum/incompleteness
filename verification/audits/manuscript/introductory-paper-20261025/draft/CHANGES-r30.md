# Introduction r30: the run-5 comprehension evaluation, on base `72014a79`

`review/accessibility/RUN5-EVALUATION.md` is NOT MET: Q5 (a) restated, (b) absent, (c) correct conclusion without a
reason. It names two specific causes and requires one change for each, and recommends one more. r30 applies those
three and one optional finding of the r29 editorial check (`editorial/GATE3-papers-d76fe9df.md`, ACCEPT).

**Unchanged:**
- No theorem or corollary statement changed.
- The §2.4 Corollary is byte-identical.
- No line was added or removed, so the ledger is unchanged and its lines match the census.
- The owner-accepted causal explanation in the card example (step-1 overlap with the step-2 return, not the step-3
  recurrence) and G1 are unchanged.
- No ID was retired, and main was not merged.

## Finding → change

| # | Finding | Line | Change |
|---|---|---|---|
| H1 | Part (b): readers hear "never occurs" as "impossible" | L132 | After "Why keep a start that never occurs?": "Such a start is not impossible: the world can be started there, and this dealer's preparation simply never does so." Anchor: Main §2.3, where these are roots of visible probability zero under the chosen visible prior, not states excluded by the dynamics |
| H2 | Part (c): the reader cannot place the order k relative to accessible windows | L156 | After "…so that $k$ lies beyond the accessible windows.": "Picture the orders $1,2,\dots,L-1$ as a long line: accessible windows cover only its short beginning, while the order $k$ of the Corollary can lie anywhere on it, so a memory that first appears late on the line is real in the dynamics but outside every window." Anchor: Main §2.3, Scope |
| R-Page | What survives when H-scramble fails | L300 | After "…not every configuration of black hole and radiation has the same energy.": "What survives is the conditional statement: the cycle-averaged Page value follows once H-scramble holds, which requires an initial superposition of configurations or a split not aligned with them, and which of these the substratum supplies is open [GR App. A.7]; the separation of conservation from recovery above does not depend on it." The H-scramble requirement is quoted from GR App. A.7 (GR.md, "…it requires an initial superposition of configurations or a bipartition not aligned with them, and which of these the substratum supplies is open") |
| G3-opt-1 | "accessible record" ends two consecutive sentences | L152 | "…its dynamics with its hidden preparation: it constrains how such a world can be described, not what accessible data will show [Main §2.3, Scope]." The preceding sentence already says that neither property appears in any accessible record |

Not applied: G3-opt-2 (a tighter G1). The owner asked to retain r29's explanation of the shared preparation.

## Checks

- `sh ./build.sh Introduction`: no dropped glyphs.
- Release gate: every step passes except `lean-axioms`, which needs `lake` and runs in CI.
- `edge_rigidity_probe.py`: ALL CHECKS PASS.

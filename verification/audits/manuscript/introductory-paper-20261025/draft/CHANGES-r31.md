# Introduction r31: the r30 checks (`cc986a5b`), on base `cc986a5b`

Both r30 checks are ACCEPT WITH CHANGES: `scientific/GATE1-papers-cc986a5b.md` (one required) and
`editorial/GATE3-papers-cc986a5b.md` (one must-fix, one should-fix, one optional). The required and must-fix
findings are the same defect, found independently. r31 applies all of them.

**Unchanged:**
- No theorem or corollary statement changed.
- The §2.4 Corollary is byte-identical.
- No line was added or removed, so the ledger is unchanged.
- No ID was retired, and main was not merged.

## Finding → change

| # | Finding | Line | Change |
|---|---|---|---|
| G1-R = G3 #1 | The Page-curve sentence rested the conclusion on H-scramble alone; GR's Theorem A.9 is conditional on H-scramble, H-decouple and the single energy shell | L300 | "What survives is that conditional statement, with all three conditions. H-scramble requires an initial superposition of configurations or a split not aligned with them, and which of these the substratum supplies is open [GR App. A.7]; the separation of conservation from recovery above does not depend on any of the three." "That conditional statement" is the paragraph's opening sentence, which names all three conditions |
| G3 #2 | "Preparation" used for the visible start, where §2.5 uses it for the hidden preparation; "A different deck and shuffle shows" lost its object | L132 | "Such a start is not impossible: the world can be started there; the dealer who always deals red simply never does. A different deck and shuffle shows why it still matters." |
| G3 #3 (optional) | Term consistency with §2.4 | L156 | "a conditional memory that first appears late on the line" |

## Checks

- `sh ./build.sh Introduction`: 22 pages, no dropped glyphs.
- Release gate: every step passes except `lean-axioms`, which needs `lake` and runs in CI.
- `edge_rigidity_probe.py`: ALL CHECKS PASS.

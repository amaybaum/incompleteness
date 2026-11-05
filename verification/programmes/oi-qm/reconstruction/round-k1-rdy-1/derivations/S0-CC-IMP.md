# S0 control CC-IMP: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 36–39, 60, 125–139, 165–183, 210); `PROOFS.md` §1 and §7 (Proposition LEDGER) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Gates under test | G2, G3 |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 210)

`μ_Q` = `δ_0` on `E`'s cells `⊗ π_0` elsewhere. Passes iff Z1-VOID[IMPORTED] and `D(μ_Q) = 3 log 2`.

## Derivation

**G2.** The declaration's rule part is "`δ_0` on `E`'s cells": it fixes the cells `x_1, y_1, y_2` to `0` and leaves the
other cells uniform.
- **(a), syntactic** (line 126).
  - The rule part names `E`.
  - It also fixes the cells of `E∖W` by name. In B-pl `W` is trivial, so `E∖W = E`.

  (a) flags.
- **(b), semantic.**
  - T1 fires: the rule part lists `E` as an input, and `E` is not among `V`, `φ`, `(d, N, q, a)` and the fixed
    constants.
  - T2 fires: the fixture states no image at `t_0`.
- **Outcome** (§5.4).
  - A G2(a) flag gives Z1-VOID[IMPORTED]; a G2(b) flag gives Z1-VOID[DYN].
  - **(reading)** (a) is decided first in G2's order (lines 126–135), so the subtype issued is that of (a): IMPORTED.
  - The (b) firings are recorded here. They do not change the subtype under this reading.

**G3.** `μ_Q` fixes three cells and is uniform on the other seven, so it is uniform on `2^7 = 128` states and
`H(μ_Q) = 7 log 2`. Then `D(μ_Q) = log 1024 − 7 log 2 = 10 log 2 − 7 log 2 = 3 log 2` (LEDGER (a)).

**Result.** Z1-VOID[IMPORTED], and `D(μ_Q) = 3 log 2`. The pass condition holds, under the reading marked above. If
both subtypes were to be carried, the token would also carry DYN. The IMPORTED subtype is attained either way.

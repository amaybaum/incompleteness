# S0 control CC-IMP″: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31, 125–135, 198–203, 212); `PROOFS.md` §4 (Proposition IND) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Gates under test | G2(a); T1; T2's no-image disjunct |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 212)

- Instance `N = 6`, `q = 2`, `a = 1`.
- `W` = sites {0, 1}, both slices.
- `E` := site 2, both slices.
- `O` = "`W ≡ 0` over `[t_u − 1, t_u]`", with `t_u = t_0`.
- No image is stated.

Passes iff G2(a) passes, T1 fires (literal coordinates) and T2 fires (no image stated; `O` fixes `x_2(t_0) = 0`).

## Derivation

The rule part is: `W` = sites {0, 1}, both slices; `O` = "`W ≡ 0` over `[t_u − 1, t_u]`"; `t_u = t_0`.

1. **G2(a) passes** (line 126).
   - The rule part names neither `E`, `R_E` nor readiness.
   - It names no cell of `E∖W`. `E∖W` = site 2's cells `{x_2, y_2}`, which appear only in the fixture's definition of
     `E`, not in the rule part.
   - It conditions on a configuration ("`W ≡ 0`"), not on an event it describes as a record, preparation or copy.
2. **T1 fires** (lines 129–131). The rule part gives `W` as a literal set of cells, sites 0 and 1, not as a function of
   `V`, `φ`, `(d, N, q, a)` or a scalar constant fixed in §6. A literal set of cells is never such a constant, so it
   counts as a further input.
3. **T2 fires** (lines 131–133). The declaration states no image at `t_0`, which is T2's no-image disjunct.
4. **What `O` fixes.** This is the parenthetical of the pass condition; it is not needed for T2's firing.
   - At `N = 6`, `(Ax)_i = x_{i−1} + x_{i+1}` with indices mod 6, and `φ^{−1}(x, y) = (Ax − y, x)` as at the base
     instance (line 31). So `y_i(t_0 − 1) = x_i` and `x_i(t_0 − 1) = x_{i−1} + x_{i+1} + y_i`.
   - At `t_0`, `W ≡ 0` gives `x_0 = x_1 = y_0 = y_1 = 0`.
   - At `t_0 − 1`:
     - `y_0(t_0 − 1) = x_0 = 0` and `y_1(t_0 − 1) = x_1 = 0` hold already;
     - `x_0(t_0 − 1) = x_5 + x_1 + y_0 = x_5`, so `x_5 = 0`;
     - `x_1(t_0 − 1) = x_0 + x_2 + y_1 = x_2`, so `x_2 = 0`.
   - So `O = {x_0 = x_1 = x_2 = x_5 = y_0 = y_1 = 0}`, and `O` fixes `x_2(t_0) = 0`.
5. **Provenance check, not a ground.**
   - On `O`, `E = (x_2, y_2)` has `x_2 = 0` and `y_2` unconstrained. So `π_0(E_{t_0} = 0 | O) = 1/2`, since IND applies
     to the free cells.
   - `π_0(E_{t_0} = 0) = 2^{−2} = 1/4` (IND).
   - This agrees with proposal r3's recorded hand check, which is provenance.

**Result.** G2(a) passes, T1 fires and T2 fires through its no-image disjunct; `O` fixes `x_2(t_0) = 0`. The pass
condition holds.

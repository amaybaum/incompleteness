# S0 control CC-T2: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31, 42–43, 129–133, 213–214) |
| Dependencies or shared intermediate results | none. The image of `O₁` is derived here afresh. It coincides with the one in `S0-CC-PASS.md`, which is this round's derivation by the same writer and is not relied on |
| Gate under test | G2(b) T2 |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 214)

CC-PASS's rule (`W = W_eq` by rule; `O₁` = "`W`'s configuration is identical at `t_u − 1` and `t_u`"; `t_u = t_0`;
`k = 1`), with stated image `{x_1 + y_1 = 0}`. Passes iff T2 fires through its "differs" disjunct and T1 does not fire.

## Derivation

**T1.** The rule part's inputs are `V` (through `W_eq`'s rule) and the §6 scalar constants `k = 1` and
`t_u = t_0`. There is no literal set of cells, so **T1 does not fire**.

**The image from the rule and `φ`.**
- From `φ^{−1}(x, y) = (Ax − y, x)` and `x(t) = y(t − 1)`, `W(t) = (y_1(t − 1), y_1(t))`.
- In the state at `t_0`: `y_1(t_0) = y_1`, `y_1(t_0 − 1) = x_1`, and `y_1(t_0 − 2) = x_0 + x_2 + y_1`.
- `W(t_0 − 1) = W(t_0)` iff `x_1 = y_1` and `x_0 + x_2 + y_1 = x_1`.
- So the image is `I = {x_1 + y_1 = 0, x_0 + x_2 = 0}`.

**T2.** The stated image is `J = {x_1 + y_1 = 0}`. The state with `x_0 = 1` and every other cell `0` lies in `J`
(`x_1 + y_1 = 0`), but not in `I` (`x_0 + x_2 = 1`). So `I ≠ J` as subsets of `S`, and **T2 fires through its "differs"
disjunct**. The no-image disjunct does not apply, since an image is stated.

**Result.** T2 fires through "differs", and T1 does not fire. The pass condition holds.

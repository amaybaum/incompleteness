# S0 control CC-BLIND: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31–62, 139–143, 165–183, 198–200, 215–216; A2's cell order); `PROOFS.md` §1 at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none. The backward formulas are restated here from line 31 and not taken from `S0-POS-X.md` |
| Gate under test | G4 |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 216)

POS-X with `W = W_ct ∪ {y_4, x_0}` at `t_u = t_0 − 1`, under `π_0`. Here `W_ct = {y_0, y_1, y_2, y_3, x_1, x_2}`
(lines 198–200). Passes iff `w = 0` is sharp with mass 1/256, `NB` fails, and the token is BLIND.

## Derivation

**Setting.** Mod 2, `φ^{−1}(x, y) = (Ax + y, x)` (line 31). In the state `(x, y)` at `t_0`:
- `y_i(t_0 − 1) = x_i`;
- `x_i(t_0 − 1) = x_{i−1} + x_{i+1} + y_i`.

`E = {x_1, y_1, y_2}` (`PROOFS.md` §1) and `Σ = {x_0, y_0}`. A value of `W` at `t_0 − 1`, in A2's cell order, is
`w = (w_x0, w_x1, w_x2, w_y0, w_y1, w_y2, w_y3, w_y4)`.

**The event `B_w`.** In the state at `t_0`:
- `x_0 = w_y0`, `x_1 = w_y1`, `x_2 = w_y2`, `x_3 = w_y3`, `x_4 = w_y4`;
- `x_4 + x_1 + y_0 = w_x0`, `x_0 + x_2 + y_1 = w_x1`, `x_1 + x_3 + y_2 = w_x2`.

So `B_w` fixes every `x_i`, and also:
- `y_0 = w_x0 + w_y4 + w_y1`;
- `y_1 = w_x1 + w_y0 + w_y2`;
- `y_2 = w_x2 + w_y1 + w_y3`.

It leaves `y_3, y_4` free. Hence `|B_w| = 4`, and `π_0(B_w) = 4/1024 = 1/256` for each of the 256 values `w`.

**G4, sharp `w`.** On `B_w`, `E_{t_0} = (w_y1, w_x1 + w_y0 + w_y2, w_x2 + w_y1 + w_y3)` is constant. So `r(w)` is 1 or
0. `w` is sharp iff `w_y1 = 0`, `w_x1 = w_y0 + w_y2` and `w_x2 = w_y3`. `w = 0` satisfies this, so it is sharp, with
mass 1/256.

**G4, ledger comparison.** The readiness is cross-time, so it is not bounded by `D(μ)` (line 62). No VOID[row] arises.

**G4, `NB` at each sharp `w`.**
- On `B_w`, the carrier is `s_Σ(t_0) = (x_0, y_0) = (w_y0, w_x0 + w_y4 + w_y1)`, fixed by `w`.
- So under `π_0(· | B_w)` only one carrier value has positive mass, and D8's existential (`σ ≠ σ′`, both of positive
  mass) has no witness.
- **`NB` fails at every sharp `w`**, at `w = 0` in particular.

**G4 outcome.** Sharp `w` exist and `NB` fails at each, so the token is **BLIND** (§5.4).

**Result.** `w = 0` is sharp with mass 1/256; `NB` fails; the token is BLIND. The pass condition holds. The base's
hand-check values (HC-1) are provenance (A6) and are not grounds.

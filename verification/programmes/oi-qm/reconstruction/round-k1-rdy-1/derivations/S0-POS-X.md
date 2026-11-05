# S0 control POS-X: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31–62, 69–70, 139–154, 165–183, 198–200, 215; A2's cell order); `PROOFS.md` §1 and §7 (Proposition LEDGER) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be`; `LEMMAS.md` §1 (Lemma P1) at the same commit |
| Dependencies or shared intermediate results | none |
| Gates under test | G3, G4, G7 |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base lines 198–200, 215)

`π_0`, cross time, with `W = W_ct := E`'s one-tick dependency set `{y_0, y_1, y_2, y_3, x_1, x_2}`, read at
`t_u = t_0 − 1`. Passes iff:
- G3 does not void;
- `w = 0` is sharp, with mass 1/64;
- `NB` holds (`V_{t_0+1} = y_0(t_0)` on the event);
- the row is W-certified;
- `Λ` equals {H-μ, finite-`S` posit, H-ret, H-2s (declared), H-cur (declared)} as a set;
- the token is CONDITIONAL[Λ].

## Setting

Mod 2, `φ(x, y) = (y, Ay + x)` and `φ^{−1}(x, y) = (Ax + y, x)`, with `(Ax)_i = x_{i−1} + x_{i+1}` on `ℤ/5`
(line 31). In the state `(x, y)` at `t_0`:
- **Backward one tick:** `y_i(t_0 − 1) = x_i` and `x_i(t_0 − 1) = x_{i−1} + x_{i+1} + y_i`.
- **Readout:** `V_{t_0} = y_1` and `V_{t_0+1} = y_0 + y_2 + x_1`. `E = {x_1, y_1, y_2}` (`PROOFS.md` §1), and
  `Σ = {x_0, y_0}`.

Write `w = (w_x1, w_x2, w_y0, w_y1, w_y2, w_y3)` for a value of `W_ct` at `t_0 − 1`, in A2's cell order. In the
state at `t_0`, the event `B_w = {W_ct(t_0 − 1) = w}` reads:
- `x_0 = w_y0`, `x_1 = w_y1`, `x_2 = w_y2`, `x_3 = w_y3`;
- `x_0 + x_2 + y_1 = w_x1`, `x_1 + x_3 + y_2 = w_x2`.

So `B_w` fixes `x_0, x_1, x_2, x_3`, and also `y_1 = w_x1 + w_y0 + w_y2` and `y_2 = w_x2 + w_y1 + w_y3`. It leaves
`x_4, y_0, y_3, y_4` free. Hence `|B_w| = 2^4 = 16`, and `π_0(B_w) = 16/1024 = 1/64` for every one of the 64 values `w`.

## Derivation

**`E` at `t_0` as a function of `w`.** On `B_w`:
- `x_1 = w_y1`;
- `y_1 = w_x1 + w_y0 + w_y2`;
- `y_2 = w_x2 + w_y1 + w_y3`.

So `1[E_{t_0} = 0] = f(w)`, where `f(w) = 1` iff `w_y1 = 0`, `w_x1 = w_y0 + w_y2` and `w_x2 = w_y3`.

**W-certification** (line 55). The fixed `f` above gives `1[E_{t_0} = 0] = f(W_ct(t_0 − 1))` at every configuration.
So the row is **W-certified**, and H-law is not added.

**G3.**
- `D(π_0) = 0`: `π_0` is uniform (LEDGER (a)).
- The readiness is cross-time, so it is not bounded by `D(μ)` (line 62). The ledger line names H-ret.
- G3 does not void.

**G4.**
- **Sharp `w`.** `r(w) = π_0(E_{t_0} = 0 | B_w) = f(w)`. The sharp `w` are the 8 values with `w_y1 = 0`,
  `w_x1 = w_y0 + w_y2` and `w_x2 = w_y3`, parametrised by `(w_y0, w_y2, w_y3)`. `w = 0` is among them, with mass 1/64.
- **Weak values.** Each of the 64 values `w` has mass 1/64. `r(w)` is 1 on the 8 sharp values and 0 on the other 56,
  beside `π_0`'s value on the same `w` (the same, since the measure is `π_0`) and `q^{−|E|} = 1/8`.
- **Ledger comparison.** The readiness is cross-time, so the equal-time voiding clause does not apply.
- **`NB` at each sharp `w`** (line 141), under `π_0(· | B_w)`.
  - On `B_w`, the carrier is `s_Σ(t_0) = (x_0, y_0) = (w_y0, y_0)`, with `y_0` free and uniform. So two carrier values
    have positive mass, `(w_y0, 0)` and `(w_y0, 1)`, each with conditional mass 1/2.
  - On a sharp `B_w`, `x_1 = y_1 = y_2 = 0`, so the readout is `(V_{t_0}, V_{t_0+1}) = (0, y_0)`. That is
    `V_{t_0+1} = y_0(t_0)` on the event.
  - Given carrier `(w_y0, b)`, the readout is the point mass at `(0, b)`. These laws differ for `b = 0` and `b = 1`.
  - So **`NB` holds at every sharp `w`**, at `w = 0` in particular.
- **G4 outcome.** A sharp `w` with `NB` exists, so G4 passes.

**`Λ`** (G5's rule, line 148–149, assembled for G7):
- the declaration's hypotheses for `π_0`: H-μ and the finite-`S` posit (lines 69–70);
- the access labels of §2: H-cur (declared) for `V`'s read of `y_1` (current slice), and H-2s (declared) for `W_ct`'s
  read, which includes the previous-slice cells `x_1, x_2`;
- H-ret, for cross-time carriage of `W`'s value from `t_0 − 1` to `t_0`;
- no H-law (W-certified);
- no H-sel (the fixture has no rule part; G2 is not under test).

So `Λ` = {H-μ, finite-`S` posit, H-ret, H-2s (declared), H-cur (declared)}, which equals the fixture's set.

**G7** (§5.4). The gates not under test (G1, G2, G5, G6) are taken as the fixture states them; controls run in
isolation (§9). With G3 and G4 as derived here and H-sel ∉ Λ, the token is **CONDITIONAL[Λ]**.

**Result.** G3 does not void; `w = 0` is sharp with mass 1/64; `NB` holds, with `V_{t_0+1} = y_0(t_0)` on the event;
the row is W-certified; `Λ` is the stated set; the token is CONDITIONAL[Λ]. The pass condition holds. The base's
hand-check values (HC-1) are provenance (A6) and are not grounds.

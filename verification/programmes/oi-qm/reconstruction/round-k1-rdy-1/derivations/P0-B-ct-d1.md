# P0, branch B-ct: written derivation (d1)

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this row exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31–62, 66–70, 120–154, 165–183, 274–284; A9); `PROOFS.md` §1 and §7 (Proposition LEDGER) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Row | candidate P0, member none, branch B-ct |
| Token | **ABSENT[π_0; B-ct; H-cur (declared), H-2s (declared), H-ret]** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Row specification

- **Declaration** (lines 69–70): `μ = π_0`. Hypotheses: H-μ, the finite-`S` posit. Rule part: none. Image
  statement: no restriction (`supp π_0 = S`).
- **Branch** (lines 44–47; O-1(b)): `t_u = t_0 − 1`, `W = W_eq = {x_1, y_1}`, `V`'s own site set by rule (input `V`),
  read at `t_u`. Its value is carried to `t_0` by retention outside the state (H-ret), and the read is conditional on
  H-ret and H-2s (declared). A value `w = (w_x1, w_y1)` is written in A2's cell order.
- **Overlap rule** (line 49): at cross time, `W`'s cells at `t_u` and `E`'s at `t_0` are distinct by tick.

## Gates

**G1, Declaration.** The §3 block is complete, and every symbol is mapped in §10, B-ct's `W` included (O-1(b)).
**G1 passes.**

**G2, Z1 audit.** The rule part is empty: (a) does not flag, and T1 does not fire. The stated image `S` equals the
image from the empty rule and `φ`, so T2 does not fire. `Im = S`, so the H-sel content is none. **G2 passes.**

**G3, Ledger.** `D(π_0) = 0` (LEDGER (a)). Cross-time readiness is not bounded by `D(μ)` (line 62). The ledger line
names H-ret, for carriage from `t_0 − 1` to `t_0` outside the state. **G3 passes.**

**G4, Readiness.**
- **`W` in terms of the state at `t_0`.** Mod 2, `φ^{−1}(x, y) = (Ax + y, x)` (line 31), so
  `x_1(t_0 − 1) = x_0 + x_2 + y_1` and `y_1(t_0 − 1) = x_1`. Hence
  `B_w = {W_{t_0 − 1} = w} = {x_0 + x_2 + y_1 = w_x1, x_1 = w_y1}`.
- **Masses.** These are two independent linear conditions (`x_1` occurs only in the second, `y_1` only in the first),
  so `|B_w| = 1024/4 = 256` and each of the four `w` has mass 1/4.
- **`r(w)`.** On `B_w`, `x_1 = w_y1` and `y_1 = w_x1 + x_0 + x_2`. The cells `x_0, x_2, x_3, x_4, y_0, y_2, y_3, y_4` are
  free and, under `π_0(· | B_w)`, uniform and independent. `E_{t_0} = (x_1, y_1, y_2) = 0` requires:
  - `w_y1 = 0`;
  - `x_0 + x_2 = w_x1`, which has conditional probability 1/2;
  - `y_2 = 0`, which has conditional probability 1/2, independently of the previous condition.

  So `r(w) = 1/4` for `w ∈ {00, 10}` (`w_y1 = 0`), and `r(w) = 0` for `w ∈ {01, 11}`.
- **Sharp readiness.** No `w` has `r(w) = 1`, so no `w` is sharp.
- **Weak values.** `r(00) = r(10) = 1/4` and `r(01) = r(11) = 0`, beside `π_0`'s values on the same `w` (identical) and
  `q^{−|E|} = 1/8`.
- **Ledger comparison:** cross time, so the equal-time voiding clause does not apply. No sharp `w` exists, so `NB` is
  decided at no `w`.
- **Outcome:** no sharp `w`, so **ABSENT[π_0; B-ct; H-cur (declared), H-2s (declared), H-ret]**. The access field
  carries §2's labels: H-cur (declared) for `V`'s read; H-2s (declared) for `W_eq`'s read, which includes the
  previous-slice cell `x_1`; and H-ret for cross-time carriage.

**G5, G6, G7.**
- **(reading)** The row takes the token of the first gate that issues one (line 183). G4 issues ABSENT, so G5, G6 and
  G7 are recorded as `not-reached`.
- In `gate-table.json`, `hypotheses` carries the declaration's hypotheses and §2's labels: H-μ, the finite-`S` posit,
  H-cur (declared), H-2s (declared) and H-ret. H-law and H-sel are G5's and are not evaluated.

**W-certified** (line 55). On `B_00`, `E_{t_0} = 0` iff `x_0 + x_2 = 0` and `y_2 = 0`, and neither is fixed by `w`. So
`1[E_{t_0} = 0]` is not a function of `W_{t_0 − 1}`, and the row is **not W-certified**.

**Operational-usefulness report:** not applicable. The row is not positive.

## Result

Token **ABSENT[π_0; B-ct; H-cur (declared), H-2s (declared), H-ret]**. Under O-1(b), the row stands as issued; no other
readout region is substituted (line 47).

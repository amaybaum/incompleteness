# P0, branch B-pl: written derivation (d1)

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this row exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31–62, 66–70, 120–154, 165–183, 274–284; A3, A9); `PROOFS.md` §1, §4 (Proposition IND) and §7 (Proposition LEDGER) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Row | candidate P0, member none, branch B-pl |
| Token | **ABSENT[π_0; B-pl; H-cur (declared)]** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Row specification

- **Declaration** (lines 69–70): `μ = π_0` (Main:56; fork leg H-μ). Hypotheses: H-μ, the finite-`S` posit (Main:62).
  Rule part: none. Image statement: no restriction (`supp π_0 = S`).
- **Branch** (line 42): `W` trivial, `t_u = t_0`. The only value of `W` is the empty string (A9).

## Gates

**G1, Declaration** (lines 122–124).
- The §3 block is complete: a measure, its hypotheses, a (null) rule part and an image statement.
- Every symbol is mapped in §10:
  - `d, N, q, a, V, Σ, T` (K-18(b));
  - `t_0`;
  - `μ` at `t_0`, `Σ` included;
  - `E` (K-9), `R_E = {0}` (K-13);
  - P0's `π_0` (Main:56).
- In B-pl, `NB(μ)` is recorded and decides nothing (O-3).
  - **Record:** `NB(π_0)` fails.
  - Reason: `V_{t_0} = y_1` and `V_{t_0+1} = y_0 + y_2 + x_1` (line 31; `PROOFS.md` §1). Given the carrier
    `s_Σ(t_0) = (x_0, y_0) = (a, b)`, the readout is `(y_1, b + y_2 + x_1)`.
  - Under `π_0` the cells `x_1, y_1, y_2` are uniform and independent of `Σ`'s cells (Proposition IND, disjoint cell
    sets). So the readout is uniform on `{0, 1}^2` for each of the four carrier values. The four conditional laws are
    equal, so no pair `σ ≠ σ′` gives different laws.
- `π_0` is not removed. **G1 passes.**

**G2, Z1 audit** (lines 125–138).
- **(a):** the rule part is empty. It names nothing and conditions on nothing, so there is no flag.
- **T1:** the rule part lists no input, so T1 does not fire.
- **T2:** an image is stated, "no restriction". With an empty rule, the image from the rule and `φ` is `S`, equal to
  the stated image, so T2 does not fire.
- **H-sel content:** `Im = S`, so `Im ∩ {W = w} = {W = w}`, and no function of `E`'s cells is fixed by one and not by
  the other. The content is none.
- **G2 passes.**

**G3, Ledger** (line 139).
- `D(π_0) = log|S| − H(π_0) = 0`: `π_0` is uniform (LEDGER (a)).
- The equal-time bound for the row is (c1): B-pl sharp readiness needs `|E| log q = 3 log 2 ≤ D(π_0) = 0`.
- **G3 passes** (G3 issues no token; any voiding is G4's).

**G4, Readiness** (lines 140–143).
- **Sharp readiness:** `π_0(E_{t_0} = 0) = q^{−|E|} = 2^{−3} = 1/8` (Proposition IND; `E = {x_1, y_1, y_2}`).
  `1/8 < 1`, so no `w` is sharp.
- **Weak value:** `r("") = 1/8`, beside `π_0`'s value `1/8` (the measure is `π_0`) and `q^{−|E|} = 1/8`.
- **Ledger comparison:** no sharp positive exists, so nothing is voided. `NB` is decided at no `w`.
- **Outcome:** no sharp `w`, so **ABSENT[π_0; B-pl; H-cur (declared)]** (§5.4). The access field carries §2's label
  for `V`'s read of the current-slice cell `y_1`; `W` is trivial and is not read.

**G5, G6, G7.**
- **(reading)** The row takes the token of the first gate that issues one (line 183). G4 issues ABSENT, so G5, G6 and
  G7 are recorded as `not-reached`.
- In `gate-table.json` the field `hypotheses` carries the declaration's hypotheses and §2's access labels: H-μ, the
  finite-`S` posit and H-cur (declared). H-law and H-sel belong to G5, which is not reached, and are not evaluated.

**W-certified** (line 55, recorded for the gate table). With `W` trivial, `f(W)` is a constant. `1[E_{t_0} = 0]` is
not constant on `S`, so no fixed `f` exists. **Not W-certified.**

**Operational-usefulness report:** not applicable. The row is not positive.

## Result

Token **ABSENT[π_0; B-pl; H-cur (declared)]**. This is one of the rows the base lists as fixed in advance (line 233,
"from `π_0`'s full support"); it records the rule's consequence and is not an independent test (line 238).

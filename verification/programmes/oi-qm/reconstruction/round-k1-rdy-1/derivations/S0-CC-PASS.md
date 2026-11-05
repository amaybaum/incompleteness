# S0 control CC-PASS: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31, 42–43, 129–135, 198–202, 213); `PROOFS.md` §1 and §3 (as a pattern) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be`; `LEMMAS.md` §0.2 D10 and §4 (L-O(ii)) at the same commit |
| Dependencies or shared intermediate results | none |
| Gate under test | G2(b) (must pass) |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 213)

- `W = W_eq` by rule.
- `O₁` = "`W`'s configuration is identical at `t_u − 1` and `t_u`", with `t_u = t_0`.
- Stated image `{x_1 + y_1 = 0, x_0 + x_2 = 0}`.
- `k = 1` (line 201).

Passes iff neither T1 nor T2 fires, with H-sel content `x_1 + y_1` recorded in B-pl and none in B-eq.

## Derivation

**T1** (lines 129–131). The rule part's inputs are:
- `V`, through `W = W_eq`, `V`'s site set by K-12(b)'s rule;
- the scalar constants fixed in §6: `k = 1` and `t_u = t_0`.

`O₁` is value-free on `W`'s cells. No literal set of cells and no other input appears, so **T1 does not fire.**

**T2** (lines 131–133). The image is derived from the rule and `φ` alone.
- `φ^{−1}(x, y) = (Ax − y, x)` gives `y(t − 1) = x(t)` and `x(t − 1) = Ax(t) − y(t)`. From `s(t) = φ(s(t − 1))`,
  `x(t) = y(t − 1)`, so `W(t) = (x_1(t), y_1(t)) = (y_1(t − 1), y_1(t))`.
- In the state at `t_0`:
  - `y_1(t_0) = y_1`;
  - `y_1(t_0 − 1) = x_1`;
  - `y_1(t_0 − 2) = x_1(t_0 − 1) = x_0 + x_2 + y_1` (mod 2).
- `W(t_0 − 1) = (y_1(t_0 − 2), y_1(t_0 − 1))` and `W(t_0) = (y_1(t_0 − 1), y_1(t_0))` are equal iff
  `y_1(t_0 − 2) = y_1(t_0 − 1)` and `y_1(t_0 − 1) = y_1(t_0)`, that is, iff `x_0 + x_2 + y_1 = x_1` and `x_1 = y_1`.
  - The second is `x_1 + y_1 = 0`.
  - Given it, the first is `x_0 + x_2 = 0`.
  - Conversely, the two equations give both equalities.
- So the image is `Im = {x_1 + y_1 = 0, x_0 + x_2 = 0}`. As a subset of `S`, it equals the stated image, so
  **T2 does not fire.**

**H-sel content** (lines 133–135). For each positive-mass `w`, it is the function of `E`'s cells that `Im ∩ {W = w}`
fixes and `{W = w}` does not under `π_0`. Here `E = {x_1, y_1, y_2}` (`PROOFS.md` §1).

- **B-pl** (`W` trivial; one `w`, with `{W = w} = S`).
  - On `S`, `E` takes all 8 values.
  - On `Im`, `x_1` and `y_2` are free, and `y_1 = x_1`. Taking `x_0 = x_2 = 0` shows that every `(a, a, b)` occurs. So
    `E` takes exactly the values `(a, a, b)`, a subgroup of index 2 in `𝔽_2^3`.
  - The function `Im` fixes and `S` does not is the class of `E` modulo that subgroup, the value of `x_1 + y_1`
    (L-O(ii); D10). It is nonconstant on `S`.
  - **H-sel content: `x_1 + y_1`.**
- **B-eq** (`W = W_eq = {x_1, y_1}` at `t_0`).
  - For `w = (w_1, w_2)` (the values of `x_1, y_1`), `Im ∩ {W = w}` is nonempty iff `w_1 = w_2`. So the positive-mass
    values under the conditioned measure are `w = 00` and `w = 11`.
  - For `w = (a, a)`, `{W = w}` fixes `x_1 = y_1 = a` and leaves `y_2` free. On `Im ∩ {W = w}` (with `x_0 = x_2`),
    `x_1 = y_1 = a` and `y_2` is still free.
  - `E` takes the same values `(a, a, 0), (a, a, 1)` on both events, so no function of `E`'s cells is fixed by one and
    not by the other.
  - **H-sel content: none.**

**Result.** Neither T1 nor T2 fires. The H-sel content is `x_1 + y_1` in B-pl and none in B-eq. The pass condition
holds.

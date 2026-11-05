# P0, branch B-eq: written derivation (d1)

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this row exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31–62, 66–70, 120–154, 165–183, 274–284; A3, A9); `PROOFS.md` §1, §4 (Proposition IND) and §7 (Proposition LEDGER) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Row | candidate P0, member none, branch B-eq |
| Token | **ABSENT[π_0; B-eq; H-cur (declared), H-2s (declared)]** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Row specification

- **Declaration** (lines 69–70): `μ = π_0`. Hypotheses: H-μ, the finite-`S` posit. Rule part: none. Image
  statement: no restriction (`supp π_0 = S`).
- **Branch** (line 43): `t_u = t_0`, `W = W_eq`, `V`'s site set, both slices, by K-12(b)'s rule (input `V`). At the
  instance, `W_eq = {x_1, y_1}` (`PROOFS.md` §1). A value `w` is written in A2's cell order, `x_1` then `y_1`.
- **Overlap rule** (lines 48–49): `W_eq ⊆ E = {x_1, y_1, y_2}`. The overlap cells `x_1, y_1` are counted in `W`, and
  their certification is tautological; `E∖W = {y_2}`.

## Gates

**G1, Declaration.**
- The §3 block is complete, and every symbol is mapped in §10. `W_eq` is mapped there as `V`'s site set, both slices
  (K-12(b)'s rule).
- `NB` is recorded at G1 only in B-pl (line 123).
- **G1 passes.**

**G2, Z1 audit.**
- The rule part is empty: (a) does not flag, and T1 does not fire.
- The stated image "no restriction" equals the image from the empty rule and `φ`, which is `S`. T2 does not fire.
- `Im = S`, so for each `w` the events `Im ∩ {W = w}` and `{W = w}` coincide. The H-sel content is none.
- **G2 passes.**

**G3, Ledger.**
- `D(π_0) = 0` (LEDGER (a)).
- The equal-time bound for the row is (c2): sharp readiness on `w` of mass `p` needs
  `p · |E∖W| log q = p · log 2 ≤ D(π_0) = 0`.
- **G3 passes.**

**G4, Readiness.**
- **Masses.** By Proposition IND, `W_{t_0}` is uniform under `π_0`, so each `w ∈ {00, 01, 10, 11}` has mass 1/4.
- **`r(w)`.** By Proposition IND (A3), `r(w) = π_0(E_{t_0} = 0 | W_{t_0} = w)` is `q^{−|E∖W|} = 1/2` if `w` is `0` on
  `W ∩ E = {x_1, y_1}`, and `0` otherwise. So:
  - `r(00) = 1/2`;
  - `r(01) = r(10) = r(11) = 0`.
- **Sharp readiness.** No `w` has `r(w) = 1`, so no `w` is sharp.
- **Weak values.** The values above are reported beside `π_0`'s values on the same `w` (identical, since the measure is
  `π_0`) and `q^{−|E|} = 1/8`.
- **Ledger comparison:** no sharp positive exists, so nothing is voided. `NB` is decided at no `w`.
- **Outcome:** no sharp `w`, so **ABSENT[π_0; B-eq; H-cur (declared), H-2s (declared)]**. The access field carries
  §2's labels: H-cur (declared) for `V`'s read of `y_1`, and H-2s (declared) for `W_eq`'s read, which includes the
  previous-slice cell `x_1` (§11 Q3).

**G5, G6, G7.**
- **(reading)** The row takes the token of the first gate that issues one (line 183). G4 issues ABSENT, so G5, G6 and
  G7 are recorded as `not-reached`.
- In `gate-table.json`, `hypotheses` carries the declaration's hypotheses and §2's access labels: H-μ, the
  finite-`S` posit, H-cur (declared) and H-2s (declared). H-law and H-sel are G5's and are not evaluated.

**W-certified** (line 55). On `{W_{t_0} = 00}`, `E_{t_0} = 0` iff `y_2 = 0`, and `y_2` is not fixed by `W`. So
`1[E_{t_0} = 0]` is not a function of `W_{t_0}`, and the row is **not W-certified**.

**Operational-usefulness report:** not applicable. The row is not positive.

## Result

Token **ABSENT[π_0; B-eq; H-cur (declared), H-2s (declared)]**. This is one of the rows the base lists as fixed in
advance (line 234, "from TA (c4)", which is Proposition IND by A3); it records the rule's consequence and is not an
independent test (line 238).

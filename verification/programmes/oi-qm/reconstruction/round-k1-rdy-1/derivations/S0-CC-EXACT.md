# S0 control CC-EXACT: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 39, 50–52, 139–141, 207, 210; A3); `PROOFS.md` §1 and §4 (Proposition IND) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Gate under test | G4 |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 207)

`μ = (1 − ε) μ_Q + ε π_0` with `ε = 1/20`, where `μ_Q` is `δ_0` on `E`'s cells `⊗ π_0` elsewhere (line 210), in
B-pl. Passes iff sharp readiness is absent and the weak value `153/160` is recorded.

## Derivation

1. **The two components at `t_0`.**
   - `μ_Q` puts `x_1 = y_1 = y_2 = 0` with probability 1, so `μ_Q(E_{t_0} = 0) = 1`.
   - By Proposition IND, `π_0(E_{t_0} = 0) = q^{−|E|} = 2^{−3} = 1/8`, with `E = {x_1, y_1, y_2}` (`PROOFS.md` §1).

   `μ` is the law at `t_0`, and `E_{t_0}` is read at `t_0`, so no evolution enters.
2. **The mixture.** `μ(E_{t_0} = 0) = (19/20) · 1 + (1/20) · (1/8) = 152/160 + 1/160 = 153/160`.
3. **G4, sharp readiness.** In B-pl, `W` is trivial and sharp readiness is `μ(E_{t_0} = 0) = 1` (line 50).
   `153/160 < 1`, so it is not sharp. No ledger comparison arises, and `NB` is decided at no `w`.
4. **G4, weak value.** `r = 153/160`, beside `π_0`'s value `1/8` and `q^{−|E|} = 1/8`.
5. **G4 outcome.** No sharp `w`, so ABSENT (§5.4).

**Result.** Sharp readiness is absent, and the weak value `153/160` is recorded. The pass condition holds.

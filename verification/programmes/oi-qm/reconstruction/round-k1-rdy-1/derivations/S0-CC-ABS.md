# S0 control CC-ABS: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31–62, 139–143, 196–206; A3); `PROOFS.md` §1 and §4 (Proposition IND) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Gate under test | G4 |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 206)

`π_0`, in B-eq form (`t_u = t_0`) with `W = {x_3, y_3}`, disjoint from `E` and `Σ`. Passes iff ABSENT.

## Derivation

1. **Region.** `E = {x_1, y_1, y_2}` (`PROOFS.md` §1). `W = {x_3, y_3}` shares no cell with `E` or with `Σ = {x_0, y_0}`.
2. **Conditional law.** By Proposition IND at tick `t_0` (A3), with `X = W` and `Y = E` disjoint, `W_{t_0}` and
   `E_{t_0}` are independent and each is uniform under `π_0`. So each of the four values `w ∈ {0, 1}^2` has
   `π_0(W_{t_0} = w) = 1/4 > 0`, and `r(w) = π_0(E_{t_0} = 0 | W_{t_0} = w) = q^{−|E|} = 2^{−3} = 1/8`.
3. **G4, sharp readiness.** A `w` is sharp iff `r(w) = 1`. Every `r(w) = 1/8 < 1`, so no `w` is sharp. No ledger
   comparison arises (it concerns an equal-time sharp positive), and `NB` is decided at no `w`.
4. **G4, weak values.** For each `w`: `r(w) = 1/8`, beside `π_0`'s value on the same `w` (`1/8`; the measure is `π_0`)
   and `q^{−|E|} = 1/8`.
5. **G4 outcome.** No sharp `w`, so ABSENT (§5.4). The access labels of §2 are H-cur (declared) for `V`'s read and
   H-2s (declared) for `W`'s read, which includes the previous-slice cell `x_3`.

**Result.** G4 issues ABSENT. The pass condition holds. The base's hand-check value `r(w) = 1/8` (HC-1) is
provenance (A6) and is not a ground; the derivation above decides the control.

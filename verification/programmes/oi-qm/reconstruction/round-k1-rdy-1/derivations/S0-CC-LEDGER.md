# S0 control CC-LEDGER: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 50, 60–62, 139–143, 209; A6, A7); `PROOFS.md` §1, §5 (Proposition EN) and §7 (Proposition LEDGER) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Gate under test | G3/G4 |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 209)

A row asserting B-pl sharp readiness under `μ_0 := π_0(· | ℰ = 0)`. Passes iff VOID[row], with `3 log 2 > log 2`.

## Derivation

1. **G3, `D(μ)` and its source.** By Proposition EN(c), `{ℰ = 0}` has 512 states, so `μ_0` is uniform on 512 states.
   Then `H(μ_0) = log 512` and `D(μ_0) = log 1024 − log 512 = log 2` (LEDGER (a)).
2. **G3, the bound written for the row.** The row is B-pl, at equal time. Under (c1), B-pl sharp readiness needs
   `|E| log q ≤ D(μ)`, with `|E| = 3` (`PROOFS.md` §1) and `q = 2`, that is `3 log 2 ≤ D(μ_0)`.
3. **G4, the ledger comparison** (lines 141–143). It precedes the `NB` decision. The row asserts an equal-time sharp
   positive (B-pl sharp readiness), and its bound requires `3 log 2 ≤ log 2`, which is false (`3 log 2 > log 2`).
   An equal-time sharp positive that breaks its G3 bound voids the row.
4. **G4 outcome.** VOID[row]. It takes precedence over any BLIND (line 143).

**Remark** (not a ground for the outcome). The control tests G3/G4's handling of an asserted readiness that breaks
the bound; it does not use the assertion's truth. By LEDGER (b), read contrapositively, `D(μ_0) = log 2 < 3 log 2`
implies `μ_0(E_{t_0} = 0) < 1`, so the injected assertion is false.

**Result.** VOID[row], with `3 log 2 > log 2`. The pass condition holds. The base's hand-check shell count (HC-1) is
provenance (A6); the count used is Proposition EN(c).

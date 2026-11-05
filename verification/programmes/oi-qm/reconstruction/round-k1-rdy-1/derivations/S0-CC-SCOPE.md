# S0 control CC-SCOPE: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 31–62, 97–100, 139–143, 208; A5); `LEMMAS.md` §1 (Lemma P1) and §2 (blindness lemma, scope §2.3) and `PROOFS.md` §1 and §7 (Proposition LEDGER) at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Gate under test | G4 |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 208)

`δ_0`, the point mass at the fixed point `0`. Passes iff BLIND in B-pl, B-eq and B-ct.

## Derivation

**Common facts.**
- `φ` is additive, so `φ(0) = 0` and `φ^{−1}(0) = 0` (`LEMMAS.md` D1). Under `δ_0` the state is `0` at every tick.
- `δ_0 = u_{{0}}` is φ-invariant (Lemma P1(a); `{0}` is a cycle).
- `D(δ_0) = log|S| − H(δ_0) = log 1024 − 0 = 10 log 2` (LEDGER (a)).
- Under `δ_0`, `s_Σ(t_0) = (x_0, y_0) = (0, 0)` with probability 1. Only one carrier value has positive mass.

**B-pl** (`W` trivial, `t_u = t_0`).
1. Sharp: `δ_0(E_{t_0} = 0) = 1`.
2. Ledger (equal time, (c1)): `|E| log q = 3 log 2 ≤ 10 log 2 = D(δ_0)`, so G4 does not void the row.
3. `NB(δ_0)` fails. `δ_0` is φ-invariant with `δ_0(E_{t_0} = 0) = 1` and `V ∩ Σ = ∅`, so the blindness lemma applies
   (`LEMMAS.md` §2.3). Directly: only one carrier value has positive mass, so D8's existential has no witness.
4. G4 outcome: a sharp `w` exists and `NB` fails at it, so BLIND.

**B-eq** (`W = W_eq = {x_1, y_1}` at `t_u = t_0`).
1. Only `w = 00` has positive mass, and `δ_0(E_{t_0} = 0 | W_{t_0} = 00) = 1`, so `w = 00` is sharp.
2. Ledger (equal time, (c2)): with `p = 1` and `|E ∖ W| = |{y_2}| = 1`, `p · |E∖W| log q = log 2 ≤ 10 log 2`, so the
   row is not voided.
3. `δ_0(· | W_{t_0} = 00) = δ_0`. `NB` fails, as in B-pl (A5: the conditioned law is `δ_0` itself, which meets the
   lemma's premises).
4. G4 outcome: BLIND.

**B-ct** (`W = W_eq` at `t_u = t_0 − 1`).
1. The state at `t_0 − 1` is `φ^{−1}(0) = 0`, so `W_{t_0 − 1} = 00` with probability 1. Hence
   `δ_0(E_{t_0} = 0 | W_{t_0 − 1} = 00) = 1`, and `w = 00` is sharp.
2. Ledger: cross-time readiness is not bounded by `D(μ)` (line 62). The ledger line names H-ret, and nothing is voided.
3. `δ_0(· | W_{t_0 − 1} = 00) = δ_0`, so `NB` fails as above.
4. G4 outcome: BLIND.

**Result.** BLIND in B-pl, B-eq and B-ct. The pass condition holds.

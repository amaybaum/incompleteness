# S0 control CC-IMP′: written derivation

| Record | Value |
|---|---|
| Author / producing session | `writer-k1rdy1-exec` (W1, executor) |
| Access | No other derivation of this control exists in this round |
| Permitted inputs used | `preregistration.md` and `amendments/` at `F` = `d9b3de012e393262adb20f91ad49627bad48de43` (base lines 36–43, 78–80, 125–128, 211); `PROOFS.md` §1 at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` |
| Dependencies or shared intermediate results | none |
| Gate under test | G2(a) |
| Outcome | **pass** |

This is a paper derivation written by hand. It is not a computational or kernel-checked result.

## Fixture (base line 211)

- **(a)** `O′` = P3's `O` ∧ "`y_2(t_0) = 0`".
- **(b)** `π_0(· | x_3 = 0, x_1 = y_1 = x_3)`, declared as "`W_eq` is a fan-out copy of ancilla `x_3` prepared in 0".

Passes iff both are flagged.

## Derivation

G2(a) (lines 126–128): the rule part names neither `E`, `R_E` nor readiness, names no cell of `E∖W` by coordinates,
and conditions on no event that it describes as a record, a preparation or a copy of a prepared cell.

- **(a)** P3's `W` is `W_eq = {x_1, y_1}` (lines 78–80), and `E = {x_1, y_1, y_2}` (`PROOFS.md` §1), so
  `E∖W = {y_2}`. The rule part's added conjunct "`y_2(t_0) = 0`" names the cell `y_2` of `E∖W` by coordinates.
  **Flagged.**
- **(b)** The declaration describes its conditioning event as "a fan-out copy of ancilla `x_3` prepared in 0", which
  is an event described as a copy of a prepared cell. **Flagged.** (The event constrains only `x_1`, `y_1` and `x_3`,
  none of them in `E∖W`. The flag arises from the description, as the clause requires.)

**Result.** Both declarations are flagged. The pass condition holds.

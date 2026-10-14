# Relative two-NOT transport for KINF-COPY-1 (#822) — design record

Base: main `M = 5bfdaba6`. Disposable design commits on the session branch, not for merge. No adopted file changes.

- `CopyCovariance.lean` is KINF-COPY-1's design module, byte-identical to Git blob `fb9c73fe` at `8c92343e`
  (`dev-equivalence/split-l3`; first built in run 38091534622, job 114328799399).
- `RelativeGateTransport.lean` states `NativeGate2Of Ω avail z NC NT T`: `NativeGate2` with `maxConeOf avail` in place of
  `maxCone Ω` in the two positivity clauses (with `NC = NT` it is K1-BRIDGE-1's `NativeGateOf`).
- `relgate_counter.py` is an exact probe that reads the kernel's `CompositeDimension.lean`; `relgate-counter-output.txt`
  is its saved output (11 checks, 0 failures, `VERDICT TRANSPORT-NEEDS-CONE-EQUALITY`).

Run 38606561330, job 115998853730, at exact commit `c9f16498`: the probe replays byte for byte; `CopyCovariance.lean`
compiles at `M` with its twelve reports and `RelativeGateTransport.lean` with thirteen, all 25 within
`[propext, Classical.choice, Quot.sound]`; the comparison rejects the output with `sorryAx` injected and with one report
removed; legacy records, receipts and placement pass.

**Proved (design, every clause a premise).**

- `nativeGate2_of_cone_subset`: relative → maximal, from `maxConeOf avail ⊆ maxCone Ω` alone.
- `nativeGate2Of_of_cone_superset`, `maxCone_subset_maxConeOf`: maximal → relative, from `maxCone Ω ⊆ maxConeOf avail`,
  which effect soundness gives.
- `nativeGate2Of_iff_of_cone_eq`: the equivalence under the cone equality, from those two theorems, one per direction.
- `nativeGate2Of_conj`, `nativeGateOf_of_conj`: KINF-COPY-1's conjugacy results for the relative form, the second
  landing in `NativeGateOf`.
- `dim_of_nativeGate2Of_conj` (`d = 1 ∨ d = 3`), `three_of_nativeGate2Of_conj_of_two_le`, `dim_of_nativeGate2Of_conj_neg`,
  `dim_of_nativeGate2Of_conj_dense`, `dim_of_nativeGate2Of_conj_of_orbit`: the selectors in the relative form, under
  K1-BRIDGE-1's hypotheses (`maxConeOf_avail_eq`) or KTRANS-DENSE-1's (`maxConeOf_avail_eq_of_dense`). The dimension
  enters only through DIM-1's `dim_of_nativeGate`, reached through KINF-COPY-1's selector.
- `hcov_of_copyNatural`: KINF-2's `CopyNatural` gives KINF-COPY-1's covariance hypothesis (this direction only).
- `swapped_relative_hyps`: at `d = 3`, with `sharpUnitFamily 3` and `fullAut 3`, every hypothesis of the relative
  selector holds with distinct NOTs. The same gate is also a one-NOT gate, so this shows satisfiability only.

**Countercontrols.** Kernel half: `cone_eq_fails_axis`. Conclusion level (exact probe): `T_S` = `cnot` followed by
`diag(2,1,1)` on both copies, with `avail = axisFamily`, is a relative native gate and takes the value `−1/2` on
`sharpEff e₃ ⊗ sharpEff(−e₁)` at `prodState z3 xplus`, so it is not a `NativeGate`; the inclusion is needed for the
conclusion, not only for its proof. No kernel form of this countercontrol exists.

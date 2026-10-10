**MERGE-HELD — native §A.39 round PARITY-NOT-1. Do not merge; landing only on explicit owner authorization.**

DIM-1's parity count from the gate relations alone, the NOT those relations force at `d = 3`, and forward positivity as a separate condition. From `D` = `e2649339` (certified by push run 37584359361), non-sealing. `GateRel N G` is exactly `NativeGate`'s `relT` and `relC`, read from `D`.

- **Q-REL** (`PARITY-FROM-RELATIONS-PROVED` / `…-NOT-ESTABLISHED`): DIM-1's `finrank_plus_eq_finrank_minus` and `not_even_of_nativeGate` hold with `(hG : NativeGate (eball d) z N G)` replaced by `(hR : GateRel N G)` and nothing else; §A reads neither the frame nor positivity.
- **Q-NOT** (`D3-NOT-PI-ROTATION-PROVED` / `…-NOT-ESTABLISHED`): with `IsNot (eball 3) z N` and `GateRel N G` alone, both eigenspaces have dimension two, `tangentPlus N = 1`, `N x = 2 (u · x) u − x` for a unit `u`, and `det N = 1`; `NativeGate` corollaries. Controls: `diag(1, 1, −1)` and `−id` are NOTs of `eball 3` for which no gate satisfies the relations (determinant `−1`); `cnot` with `nflip` satisfies them.
- **Q-SEP** (`POSITIVITY-SEPARATION-PROVED` / `…-NOT-ESTABLISHED`): `gJ3` (with `nflip`) and `gJ5` (with `n5 = diag(1, 1, −1, −1, −1)`) satisfy `NativeGate`'s frame and `GateRel`, and an explicit pure product pairs to `−1/10` with two sharp effects, so forward positivity fails — at `d = 3` and directly at `d = 5` (a failure through `ne_five_of_nativeGate` does not satisfy the rule).

Load-bearing controls: S2 pairs each parity theorem with its landed partner's effective statement at `D` under the single replacement; S3 rejects any frame or positivity reading in the `d = 3` theorems; S5 ties the frame and positivity statements to `NativeGate`'s fields at `D` and freezes both `−1/10` witnesses. The non-inference rule is frozen: no dimension selector, no complex structure, no `J²` interpretation, no NOT of a physical theory, no claim that `d = 5` is the only higher-dimensional case, no premise adoption.

Governed paths: the record directory `verification/programmes/oi-qm/reconstruction/round-parity-not-1/`, `verification/receipts/PARITY-NOT-1.json`, `verification/lean-mathlib/OIBridge/ParityNot.lean` (A), `verification/lean-mathlib/OIBridge.lean` (M), `verification/lean-manuscript-census.json` (M). No manuscript or ROADMAP edit.

**Design evidence:** run 37595568691 on `2b80bbe7` is green (32/32, 24 prints standard, `lean-axioms` 5814). Run 37594392508 failed in the bridge only and was repaired in proof only; no statement changed.

**Predicted execution tree:** `46a1e33b`; controls `3b2789ec` (self-test 68) pass 20/20; the verdict prints exactly the three positive tokens; run 37608886234 is green 32/32.

**Candidate `F`:** `3398a071`, `D` + preregistration alone (blob `b9b7c5f0`). Exact-head attestation follows in a comment. `F` is not designated.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1

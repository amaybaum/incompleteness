**MERGE-HELD — native §A.39 round ODD-CHAR-1. Do not merge; landing only on explicit owner authorization.**

This round asks which dimensions carry a NOT together with DIM-1's frame and the two gate relations, and whether forward positivity fails at every odd dimension above one. It starts from `D` = `3c92d16b`, certified by push run 37631392533, and is non-sealing.

The family: for `d = 2k + 1`, `nK k` is the diagonal NOT with sign `−1` on the homogeneous indices above `k`, `zK k` is the last axis, and `gRev k` is PARITY-NOT-1's sign-free permutation gate for `Fin.rev`.

- **Q-FAM** (`ODD-FAMILY-PROVED` / `…-NOT-ESTABLISHED`): for every `k`, `IsNot (eball (2k+1)) (zK k) (nK k)` holds, `gRev k` satisfies `NativeGate`'s frame field (read from `D`), and `GateRel (nK k) (gRev k)` holds. §A reads neither positivity clause.
- **Q-ODD** (`ODD-CHARACTERIZATION-PROVED` / `…-NOT-ESTABLISHED`): `(∃ z N G, IsNot (eball d) z N ∧ frame ∧ GateRel N G) ↔ Odd d`.
  - Forward: PARITY-NOT-1's `not_even_of_gateRel`.
  - Reverse: DIM-1's `cnot1` at `d = 1`, and `gRev k` at `d = 2k + 1` for `k ≥ 1`.
- **Q-POS** (`HIGHER-ODD-POSFWD-FAILURE-PROVED` / `…-NOT-ESTABLISHED`): for every `k ≥ 1`, the image of an explicit product state pairs to `−1/10` with two sharp effects. Hence the negation of `NativeGate`'s `posFwd` field holds on `eball (2k+1)`, with no landed dimension corollary used.

The earned reading is frozen verbatim: *The frame and both relations admit exactly the odd dimensions. For every odd dimension at least 3, an explicit member of this family fails forward positivity. Combined with DIM-1, the positivity assumptions are therefore collectively load-bearing for excluding the higher odd dimensions.*

The claim that `posFwd` or `posInv` is individually necessary is explicitly frozen out. Each gate of the family is its own inverse, so the family does not separate the two clauses. The round also does not cover:
- classifying the positive gates;
- the necessity of the frame, `relT` or `relC`;
- a complex structure, `J²`, or physical realizability;
- premise adoption.

**Governed paths:**
- the record directory `verification/programmes/oi-qm/reconstruction/round-odd-char-1/`;
- the receipt `verification/receipts/ODD-CHAR-1.json`;
- `verification/lean-mathlib/OIBridge/OddChar.lean` (A);
- `verification/lean-mathlib/OIBridge.lean` (M);
- `verification/lean-manuscript-census.json` (M).

No manuscript or ROADMAP edit.

**Design evidence:**
- Run 37643178804 on `dbdb4662` was green (32/32) with lint-only warnings.
- The proof-only hygiene run 37646141082 on `6977ee04` was green (32/32) with no module warnings, 12 standard prints and `lean-axioms` 5826. All 30 statements are identical between the two runs.

**Predicted execution tree** `26f4c58f`:
- controls blob `95781938` (self-test 62) passes 18/18;
- the verdict prints exactly the three positive tokens;
- run 37648623767 was green (32/32).

**Candidate `F`:** `d3d058d9`, which is `D` plus the preregistration alone (blob `1b6ecb93`). The exact-head attestation follows in a comment. `F` is not designated.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1

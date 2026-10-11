# HP-13 — B7-1 under countable C¹ curve covers, and for identity components of dimension at most one

From `research/bridge`, node B16 (round 4). Proposed for the countermodels thread (B3.C's residual, HO-25) and the
equivalence thread (the reachability lemma of the K2 schema). The coordinator routes.

## Statements and labels

Every statement concerns orbits of pair vectors under groups of conjugations (invariance); none concerns availability.

1. **The curve-cover theorem** (B16-1). If countably many C¹ curves of `4 × 4` matrices cover a subgroup `H` of
   `U(4)`, some nonzero pair vector is carried to a product by no element of `H`, and, with an antiunitary coset
   `H·(K∘conj)`, by no coset element either, for every `K`, with no coset condition. `ReachUnitary` and `ReachAnti`
   (HP-10) reduce to the existence of such covers; every countable subgroup has one. Proof: a dimension count, the bad
   vectors lying in countably many C¹ images of `ℝ × ℂ³` (real dimension 7) in `ℂ⁴` (8). Label: CONJECTURE ([D]).
2. **Dimension at most one** (B16-2). Through Cartan's closed-subgroup theorem and the finiteness of components, B7-1
   holds for every closed subgroup whose identity component has dimension at most one, with or without an antiunitary
   coset. Label: CONDITIONAL (on [L] and the written link).
3. **The limit and the defeat** (B16-2, B16-3). For identity components of dimension `d ≥ 2` the count decides nothing
   (`d + 6 ≥ 8`); the tori of dimension two to four — B10-4's 2-torus and B3.C's residual region (HO-25 item 4) among
   them — stay at NOTES-B7's written proof. With claim (D), item 2 is B3-4's case (P1), its reachability step now in design form. "A group" whose identity
   component has dimension at most one is not a sufficient bridge for (b) (CONDITIONAL on claim (D)).

## Evidence

| item | pointer |
|---|---|
| module | `research/bridge/lean/BridgeReachDim.lean`, sha256 `d4ee2170…`; dev blob `bf3e5564` |
| CI | run 38117986499 (`dev-bridge/r4-final` @ `bf8ba746`), Mathlib bridge job 114406679644: "Built OIBridge.BridgeReachDim (3.5s)", 32/32 `#print axioms` standard, `lean-axioms` PASS (6083), gate red only on `lean-manuscript`. Dispatch 2's failure (cause not recorded: the error block fell outside the readable log tail) kept as `lean/BridgeReachDim.run38115337569.lean` |
| preflight | `experiments/b16_preflight.py`, P1–P5 green, replay byte-identical |
| notes, results | `NOTES-B16.md`; `RESULTS.md` rows B16-1 … B16-3 |

## What the recipient may assume

Items 1–3 at their labels. The curve-cover theorem is a Lean statement that builds against Mathlib `v4.33.0` with the
standard axiom footprint; it covers every finite, countable and one-dimensional case of B7-1 at once.

## What the recipient may not assume

- certification, or any census disposition;
- B7-1 for identity components of dimension two or more;
- that the Cartan link is formalized: it is written, with the classical theorems cited.

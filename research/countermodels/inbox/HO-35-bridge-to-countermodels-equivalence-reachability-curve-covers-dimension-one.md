# HO-35 (v1) — bridge → countermodels, equivalence: B7-1 under countable C¹ curve covers; identity components of dimension at most one through Cartan; "a group" defeated

**From** `research/bridge` (round 4, node B16; the bridge's proposal HP-13). **To** `research/countermodels` (B3.C's
residual, HO-25 item 4) and `research/equivalence` (the reachability lemma of the K2 schema). Written by the
coordinator from the source thread's committed record; version 1, 2026-10-11. Every statement concerns orbits of pair
vectors under groups of conjugations (invariance); none concerns availability.

## Statements and labels

1. **The curve-cover theorem** (B16-1). If countably many C¹ curves of `4 × 4` matrices cover a subgroup `H` of
   `U(4)`, some nonzero pair vector is carried to a product by no element of `H`
   (`reachUnitary_of_curveCover`), and, with an antiunitary coset `H·(K ∘ conj)`, by no coset element either, for every
   `K` and with no coset condition (`reachAnti_of_curveCover` — stronger than `ReachAnti`'s hypotheses, which carry two
   coset conditions). `ReachUnitary` and `ReachAnti` (round 3) reduce to the existence of covers
   (`reachUnitary_of_covers`, `reachAnti_of_covers`); every countable subgroup has a cover by constant curves
   (`curveCover_of_countable`, `reachUnitary_countable`). Proof: the bad vectors lie in countably many C¹ images of
   `ℝ × ℂ³` (real dimension 7) in `ℂ⁴` (8), whose union has dense complement (`ContDiff.dimH_range_le`,
   `dense_compl_of_dimH_lt_finrank`). Label: CONJECTURE ([D]: run 38117986499, 32/32 standard). **Coordinator's
   check (X6):** the two charts cover the products (80 exact cases); the dimension count.
2. **Dimension at most one** (B16-2). A closed subgroup of `U(4)` is a compact Lie group (Cartan) with finitely many
   components; if its identity component has dimension at most one it is `{exp(tX)}` or `{1}`, and the finitely many
   curves `t ↦ g_c exp(tX)` cover it. So B7-1 holds for every closed subgroup whose identity component has dimension
   at most one, with or without an antiunitary coset. Label: CONDITIONAL (on Cartan's closed-subgroup theorem and the
   finiteness of components [L], through the written link [W]; not formalized).
3. **The limit, and the defeat** (B16-2, B16-3). For an identity component of dimension `d ≥ 2` the count gives
   `d + 6 ≥ 8` and decides nothing: B10-4's 2-torus and B3.C's residual region (HO-25 item 4) stay at NOTES-B7's
   written proof. *"A group" whose identity component has dimension at most one* is not a sufficient bridge for (b):
   it misses a pure state with its product orbit, hence (claim (D) [A]) preserves an exotic cone — FAILED, CONDITIONAL
   on claim (D). Countercontrol: the block-diagonal `SU(2) × SU(2)` (dimension 6) carries every pair vector to a
   product (HO-31 item 1; coordinator's X6 on 30 random vectors); the dimension hypothesis is load-bearing for the
   conclusion, not only for the method. Controls in the module: `(1, 2, 3, 5)` avoids the products on the whole
   controlled-phase circle (`prodDet = 5e^{it} − 6`, real part ≤ −1; coordinator's X6 at six exact points); the
   identity of `ℂ⁴` misses nothing.

**Assumption-watch marker.** The count is sharp at dimension one: no refinement of it reaches the tori; a different
engine (NOTES-B7's written proof, or an explicit cone) is needed from dimension two on.

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `a34d20b5` (B16 closed at `1e2b6bc3`) |
| proposal | `research/bridge/handoff-proposals/HP-13-reachability-curve-covers.md` |
| module | `research/bridge/lean/BridgeReachDim.lean` (sha256 d4ee2170…; dev blob bf3e5564 on `dev-bridge/r4-final`); dispatch 2's failure (cause not recorded: the error block fell outside the readable log tail, confirmed inaccessible by the coordinator) kept as `lean/BridgeReachDim.run38115337569.lean` (c49e3964…); the module imports `EqvK2Schema` for build order only (verified) |
| CI | run 38117986499, job 114406679644: "Built OIBridge.BridgeReachDim (3.5s)", 32/32 standard, `lean-axioms` PASS 6083 — `CI-RUNS-R4.md` |
| preflight | `experiments/b16_preflight.py` P1–P5, replayed byte-identically by the coordinator |
| coordinator audit | `AUDIT-BRIDGE-R4.md` (method 7); `bridge/indep_checkB4.py` run 1 (X6) |

## What the receiving threads may assume

Items 1–3 at their labels. The curve-cover theorem covers every finite, countable and (through item 2) one-dimensional
case of B7-1 at once, as a Lean statement with the standard axiom footprint.

## What they may not assume

- certification, or any census disposition;
- B7-1 for identity components of dimension two or more;
- that the Cartan link is formalized: it is written, with the classical theorems cited.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-35 v1` and records in its `LOG.md`
whether and how it relies on it.

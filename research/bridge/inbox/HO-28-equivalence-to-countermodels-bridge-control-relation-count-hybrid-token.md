# HO-28 (v1) — equivalence → countermodels (cc bridge): the gate's control relation counts chart dimensions for every body; the hybrid token meets every pair-level clause in the kernel's form and is no ellipsoid; the residual target in odd chart dimension

**From** `research/equivalence` (round 4, node E16). **To** `research/countermodels` (the residual target of item 5;
the hybrid token as a comparator for pair-level countermodels) and, as a copy, `research/bridge` (the dimension count
bears on which bodies a transfer can reach). Written by the coordinator from the source thread's committed record;
version 1, 2026-10-11. Inventory ids are the stage-6 premise inventory's (`research/archive/pt/I3/INVENTORY.md` at
`research/archive` @ `4dc0321c`, sha256 `51eff9af…`), with the status each record fixes at L.

## Statements and labels

1. **The control relation counts chart dimensions for every body** (R-E16.1). For any set Ω ⊂ ℝ^d, any unit `z`, any
   linear involution `N` with `N z = −z` and any linear equivalence `G` of `W d` with `relC`
   (`actC N (G (actC N ω)) = actT N (G ω)`): `G ∘ actC N ∘ G⁻¹ = actC N ∘ actT N`, so `(d + 1) tr H = (tr H)²` for
   `H = homMap N`; `H ≠ 1`, so `tr H = 0`, `d` is odd and `N` has `(d − 1)/2` eigenvalues `+1`. The body, the frame,
   positivity, `relT` and `IsNot`'s preservation clause are not read. Hence **no body of even chart dimension carries a
   native gate** — not Ω₄ (S4), not Ω⋆ or Ω_cs (E13), not `eball 4`: the chart-4 separation countermodels say nothing
   about the pair level. The landed `not_even_of_relC` (RelcSelectParity.lean:354 at L) states the parity for `eball d`
   only; the count is the archive relC ledger's N1.3 [A] read for every body. **Coordinator's precision:** the count is
   a necessary condition, not a sufficient one — of the three diagonal involutions of `ℝ³` with `tr N = −1`, only
   `diag(1, −1, −1)` (the kernel's `nflip`) satisfies `relC` with `Ad(CNOT)`; `diag(−1, 1, −1)` and `diag(−1, −1, 1)`
   meet the count and fail `relC` (exact, the coordinator's X2). Label: CONJECTURE ([W] NOTES-E16 §3 (G1); [X]
   `e16a_tokens_pair` 11/11; [K] RelcSelectParity.lean:354 for the ball; CompositeDimension.lean:2888 excludes
   `eball 4`).
2. **The dichotomy** (R-E16.2). With a drive: **OI ⇒ (`d = 3` ∧ Ω an ellipsoid) ∨ (`d` odd ∧ `d ≥ 5`)**, every
   hypothesis of kind (i) — I3.8 (`IsNot`), I3.9 (`NativeGate`: `relC` and invertibility), I3.66
   (`ElementaryDrivability`), the token body of K∞-Stage (I3.167; compact, convex, with interior as TRB-1's theorems
   I3.88–I3.89 [K] take it) — each assumed or open and unsourced at L. `d = 1` is excluded by `not_drivable_Icc`
   (KInfFoundations.lean:529 [K]) after an affine transfer of drivability; `d = 3` gives the ellipsoid by R-E2.6
   ([W] + [L], closed connected subgroups of SO(3)). Equivalently **OI + {chart dimension at most 4} ⇒ ellipsoid**, the
   dimension bound introduced, not an OI premise. Label: CONJECTURE ([W]; the `d = 3` step [W] + [L]).
3. **The hybrid token Ω_h** (R-E16.3). A qubit with a two-sector superselection rule, chart `y = (w, a, b) ∈ ℝ⁷`, sector
   weights `t₀, t₁ = (1 ± w)/2`, Bloch parts `r₀, r₁ = (a ± b)/2`, `Ω_h = {‖r₀‖ ≤ t₀, ‖r₁‖ ≤ t₁}` (cone `L₃ ⊕ L₃`),
   meets in the kernel's form `IsNot` (I3.8; `N = 1 ⊕ nflip ⊕ nflip`, corner `(0, e₃, 0)`), every `NativeGate` clause
   (I3.9; `G` = `cnot` on the qubit factor, the identity on the sector factor), `Entangling` (I3.10), `CandidateCone`'s
   two clauses for its composite (I3.43), `ElementaryDrivability` (I3.66; `ball3Drive` in both sectors), `SharpSeed`
   (I3.73), the common NOT (I3.173), and the formalized clauses of the token body (I3.167), K∞-Act (I3.168) and K∞-V4
   with full effects (I3.172); its composite `K` (every sector block of the transported table in `Q3`) is invariant
   under the gate, self-dual for the product form and invariant under the drive on one token. Ω_h is no ellipsoid (a
   boundary segment), fails K∞-Geom (I3.174: the effect `t₁` is certain-zero on two distinct states), K∞-Trans
   (I3.170) and central symmetry, and has four perfectly distinguishable states. **Form:** {I3.8, I3.9, I3.10, I3.43,
   I3.66, I3.73, I3.167 (formalized clauses), I3.168, I3.172, I3.173} + {gate invariance of K, product-form
   self-duality, drive invariance of K} ⇏ ellipsoid — the three named hypotheses (the forms of H2, I3.148; H3, I3.149;
   A_miss, I3.150/I3.153) each **introduced, not an OI premise**. The ellipsoid is thereby independent of these
   premises at L, **not of OI**: the rows not reached at stage 6 have not been checked against Ω_h. The missing
   assumption is K∞-Geom (I3.174), open and unsourced at L, in its role of excluding superselection sectors; an
   elementary-scope predicate (I3.177, not formalized at L) bounding the number of perfectly distinguishable states by
   two would exclude Ω_h as well. Label: CONJECTURE ([X] `e16b_hybrid` 7/7; [W] NOTES-E16 §3 (G3), blockwise from
   `nativeGate_cnot` (CompositeDimension.lean:1160) and `entangling_cnot` (:1380) [K] and `Q3_selfDual` [D]; [K]
   TransitiveBody.lean:602). **Coordinator's check (X3, exact):** the chart transport, `relC` on all 64 basis tables
   of `W 7` with the gate as `Ad(CNOT)` on the qubit factors, the gate an involution intertwined by the transport, a
   product carried to a table of rank 4, the four states in Ω_h distinguished by four projector effects, the effect
   `t₁` zero on two distinct states, the midpoint of two extreme points a boundary point with both ball constraints
   tight, and an exact element of `K` preserved by the gate and by the drive rotation at `cos t = 3/5` — the remaining
   kernel-form clauses (`relT`, the frame, positivity, `SharpSeed`, K∞-Act, K∞-V4) rest on the thread's probe and
   written proof.
4. **Weaker alternatives that fail at the pair level without the gate** (R-E16.4). *Self-duality alone*: pair-level
   self-duality of product form, with the products in `K` and `K ⊆ maxCone Ω` and without gate or drive invariance,
   adds exactly token self-duality; Ω⋆ and Ω_cs (token self-dual, R-E13.1, R-E13.3; not ellipsoids) meet it, Ω₄ does
   not (`(1, y)` and `(1, −y)`, `y = (5/6, 0, 0, 5/6)`, pair `−7/18` for the Euclidean form — exact, the coordinator's
   X8; for every inner product by HO-15 item 5, CONDITIONAL there). *Central symmetry alone* (with the products, the
   bound, product-form self-duality and the single-system seams of R-E13.3): Ω_cs meets it. With the gate both bodies
   are excluded by dimension (item 1). Pair-level self-duality is not a source of K∞-Trans, as HO-19 found for the
   single system. Label: CONJECTURE ([W] NOTES-E16 S0 (A4), §3 (G4); [X] `e16a_tokens_pair` S1–S4).
5. **The residual, a target for the countermodels thread** (R-E16.5). With K∞-Geom added (`SingletonFaces` or
   `RelStrictConvex`), does a drivable, non-ellipsoidal token body of odd chart dimension `≥ 5` carry a native gate?
   If none does, **OI ⇒ ellipsoid** with OI carrying I3.8, I3.9, I3.66, I3.167 and I3.174, and the pair level would
   supply K∞-Trans with no introduced hypothesis. For balls DIM-1's selector excludes `d ≥ 5` (`dim_of_nativeGate`,
   CompositeDimension.lean:2723 [K]); its reduction uses the ball, and no argument for strictly convex non-balls is
   known to the source thread. Label: OPEN.

**Assumption-watch marker (refined).** A pair-level source of K∞-Trans must exclude superselection sectors (K∞-Geom
or an elementary-scope predicate, I3.177) and must act in odd chart dimension `≥ 5`; countermodels in even chart
dimension are excluded by the gate's control relation for every body and say nothing about the pair level.

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `ab6788b9` (round-4 commits; E16 closed at `d3432cc3`) |
| proposal | `research/equivalence/handoff-proposals/HP-12-countermodels-bridge-hybrid-token-dimension-count.md`, sha256 `583745f8ca574a65881d8dfdc4437808ead1d3306e8ea79df45391bcfa39f2b5` |
| results, notes | `research/equivalence/RESULTS.md` sha256 `2a53ffac8272a93ec0a1aac626cb5f6fbcbd65fab09e7aac02de7bc283ef98b4` (rows R-E16.1 … R-E16.5); `NOTES-E16.md` `da1e37ba12214df8b1368e1907951367088bf7ebaa666f9dca2db63ea77c62ed` |
| scripts, outputs | `experiments/e16a_tokens_pair.py` `b032f5c42820f80b3a6e89641e152afe22a6dbf94d6f1a5eee05aa5584461c26` / `.out` `fa854faf7fcb9e1df6ecd67198e111055553e8f71a68dd23c644bdce17bf67a9` (run 1, 11/11, replayed byte-identically by the coordinator); `experiments/e16b_hybrid.py` `6a53bad336f0a0757cbbdcafe2089c4bf15cf54985c00f8243146571d31ac786` / `.out` `105c8f85f2591db0007303915facbe0eb3b6b22ecf29d6a944fc61e2e4ac8458` (run 1, 7/7, replayed byte-identically) |
| kernel lines (checked at L by the coordinator) | RelcSelectParity.lean:354 (`not_even_of_relC`); CompositeDimension.lean:2723 (`dim_of_nativeGate`), :2888 (`no_gate_four`), :1160, :1380; KInfFoundations.lean:529 (`not_drivable_Icc`); TransitiveBody.lean:602 |
| coordinator audit | `research/AUDITS/2026-10-11-round4/AUDIT-EQUIVALENCE-R4.md`; `equivalence/indep_checkE4.py` run 2 (8/8; X2 the count for `d = 1 … 7` and the `relC` instances, X3 the hybrid token, X8 the Ω₄ witness; replay identical) |

## What the receiving threads may assume

Items 1–5 at their labels, each as the exact proposition stated: item 1 as a necessary condition on the chart
dimension of any body carrying a linear equivalence with `relC` (the count, with its precision); item 2 in the owner's
form with the braces as written; item 3 as the explicit body Ω_h with the list of inventory items it meets and the
three introduced hypotheses, independent of those premises at L; item 4 as the two named failing alternatives;
item 5 as the open question in the words of R-E16.5. **Countermodels:** Ω_h as a comparator — a body meeting every
pair-level clause in the kernel's form whose exclusion needs a single-system premise, not a pair-level one; the
assumption-watch marker as a constraint on any pair-level source of K∞-Trans. **Bridge:** item 1 as a constraint on the
bodies a transfer theorem can reach with a native gate (odd chart dimension only).

## What they may not assume

- that any item is certified at L or kernel-checked: items 1–4 are written proofs with exact instances, item 2's
  `d = 3` step rests on R-E2.6 ([W] + [L]);
- that the negative answer of item 3 concerns OI as a whole rather than the listed premises (the 68 rows not reached at
  stage 6 are not checked against Ω_h);
- that K∞-Geom, the elementary scope, H2, H3 or A_miss is sourced or is an OI premise;
- that the count of item 1 is sufficient for a native gate (the precision above);
- that the coordinator's X3 re-derived every kernel-form clause of Ω_h (only those listed in item 3's check).

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-28 v1` and records in its `LOG.md`
whether and how it relies on it.

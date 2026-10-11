# NOTES-E16 — K∞-Trans from the pair level: do the pair-level hypotheses force the token body to be an ellipsoid?

Base L = `9f9f8257`. Node E16 of round 4. The coordinator's question: in the K2 schema with the token body a general
compact convex Ω (not `eball 3`), do H1–H3 and A_miss force Ω to be an ellipsoid; does pair-level self-duality with the
gate supply what the single-system seams cannot (HO-19: self-duality of the state cone is not a source of K∞-Trans; its
invariant form is)? The owner's decisive question (addendum, 03:29Z): can the pair-level results imply the transitivity
needed at higher levels without adding assumptions? Answer forms (rule 1): a positive answer is written
"OI + {…} ⇒ ellipsoid" with the braces filled; a negative answer names the exact body that meets the pair-level
hypotheses and is not an ellipsoid. Inventory ids are the stage-6 inventory's (`pt/I3/INVENTORY.md`, `51eff9af…`).

## S0 (written 2026-10-11T03:31Z, before any probe of this node)

**Productivity test (§A.31, fixed now).** A finding counts if it (a) answers the decisive question in one of the two
forms with exact evidence; or (b) isolates the exact residual question, every hypothesis classified; or (c) exposes a
hidden assumption in "the pair level supplies K∞-Trans" with a countermodel. A restatement that the question is open is
a non-gem.

**The pair-level hypotheses for a token body Ω ⊂ ℝ^d (chart dimension d), stated precisely.**
- Carrier: the kernel's `W d` (I3.1, assumed: local tomography encoded), products `prodState x y` for `x, y ∈ Ω` (I3.2),
  the maximal cone `maxCone Ω` (I3.3, defined for every Ω). Body: Ω compact, convex, with interior (TRB-1's hypotheses,
  I3.88–I3.89).
- **P1 (products and the K2 bound)**: every product of Ω's states lies in `K`, and `K ⊆ maxCone Ω` — `CandidateCone`'s
  two clauses (I3.43, assumed) with Ω in place of `eball 3`. Kind (i).
- **P2 (what replaces `cnot`)**: a native gate of Ω — `NativeGate Ω z N G` (I3.9, assumed, defined for every Ω) with
  `IsNot Ω z N` (I3.8, assumed), and `Entangling Ω G` (I3.10, assumed) where used — and invariance of `K` under `G`. The
  gate and the NOT are kind (i); the invariance `G K ⊆ K` (H2's form, I3.148) is introduced.
- **P3 (what replaces `dualW`)**: `K = K^{*(M ⊗ M)}` for an inner product `M` on `ℝ^{d+1}` (for the ball, `M = I` gives
  `dualW`). Introduced (H3's form, I3.149).
- **P4 (what replaces A_miss)**: Ω carries `ElementaryDrivability` (I3.66, assumed/open; kind (i)), and `K` is invariant
  under `actT` of every flow member and of `J` (a form of (b), I3.153; introduced).
- **What replaces `Q3`**: nothing; there is no target cone for a non-ball token. The question is whether some `K` exists,
  and whether Ω must be an ellipsoid.

**Analysis before computation (written; to be checked exactly).**
- *(A1) The gate's control relation counts dimensions for every body.* If `G` is invertible and
  `actC N ∘ G ∘ actC N = actT N ∘ G` (relC) with `N` a linear involution, `N ≠ 1`, then
  `G ∘ actC N ∘ G⁻¹ = actC N ∘ actT N`; as maps of `W d` these are `H ⊗ 1` and `H ⊗ H` with `H = homMap N`, so
  `(d + 1) tr H = (tr H)²`; `tr H = d + 1` forces `H = 1`, excluded by `N z = −z`, `z ≠ 0`; so `tr H = 0`: `d` is odd and `N`
  has `(d − 1)/2` eigenvalues `+1`. Neither the body nor self-adjointness of `N` is read. This is the archive's relC
  ledger N1.3 [A] (trace form, written there for the ball's NOT but reading only "N involution, Nz = −z, z ≠ 0"); the
  landed `not_even_of_relC` (RelcSelectParity.lean:354) is stated for `eball d` [K]. **Consequence: no body of chart
  dimension 4 carries a native gate — not Ω₄, Ω⋆, Ω_cs, and not `eball 4` (`no_gate_four`, I3.20 [K]).**
- *(A2) What P2 and the drive give with no introduced hypothesis.* By (A1) `d` is odd. `d = 1` is excluded: a compact
  convex body with interior in `ℝ¹` is an affine image of `[−1, 1]`, drivability transfers along affine equivalences, and
  `not_drivable_Icc` (KInfFoundations.lean:529, I3.68 [K]). `d = 3`: a drive forces the ellipsoid (NOTES-E2 R3 [W] + [L];
  its circularity remark lapses, since (A1) does not use the ball). Predicted form, every hypothesis of kind (i):
  **OI ⇒ (d = 3 ∧ Ω an ellipsoid) ∨ (d odd ∧ d ≥ 5)**, with OI carrying I3.8, I3.9 (relC and the gate's invertibility
  only), I3.66 and TRB-1's body hypotheses, each at its status at L (assumed, unsourced). Hence, with one introduced
  hypothesis: **OI + {chart dimension at most 4} ⇒ ellipsoid**.
- *(A3) The residual, odd `d ≥ 5`: a candidate exact body for the negative answer.* The quantum–classical hybrid token —
  a qubit with a two-sector superselection rule: state cone `L₃ ⊕ L₃` (two Bloch balls with weights), chart dimension 7.
  Prediction: it carries `IsNot` (the half-turn in both sectors), a native gate with every `NativeGate` clause and
  `Entangling` (`cnot` on the qubit factor, identity on the sector factor), a drive (`ball3Drive` in both sectors), and a
  composite `K = Q3 ⊗ (the classical cone of sector pairs)` that meets P1, P2's invariance, P3 (product form) and P4's
  invariance — and it is not an ellipsoid (its boundary contains a segment). It fails K∞-Geom (I3.174: singleton faces),
  which is the place where "elementary system" would have to exclude a superselection sector. This is the
  Barnum–Wilce situation the archive names for non-ball local systems (`kirc/UNIFORM-NOGO.md` [A]: locally tomographic
  composites with a qubit give QM with superselection [L, abstract-level]). If it holds, the decisive question has a
  negative answer for the pair-level hypotheses with the single-system seams except K∞-Geom, and the open residue is
  odd `d ≥ 5` with K∞-Geom added.
- *(A4) Product-form self-duality adds exactly token self-duality.* (⇒) P1 and P3 force `C(Ω) = C(Ω)^{*M}`: from
  `a ⊗ c, b ⊗ c ∈ K ⊆ K^{*}`, `M(a, b) ≥ 0` on the cone; from `K ⊆ maxCone`, `K^{*} ⊇ (M ⊗ M)⁻¹(f ⊗ g)` for effects
  `f, g`, so `M⁻¹ f ⊗ M⁻¹ g ∈ K ⊆ maxCone`, whence `M⁻¹ C* ⊆ C`. (⇐) If `C = C^{*M}`, the products form a self-positive
  cone for `M ⊗ M` and a maximal self-positive cone containing it (Zorn) is self-dual and lies in
  `K_min^{*} = maxCone Ω`. So by HO-19/E13 P3 is not a source of K∞-Trans: Ω⋆ and Ω_cs meet P1 + P3. Ω₄ fails P3 (its
  cone is self-dual for no inner product, HO-15 item 5; re-derived below). With P4's invariance the existence of a
  self-dual composite for Ω⋆, Ω_cs is not decided here (an equivariant Zorn argument can fail: in ℝ² no closed pointed
  cone is invariant under the rotation by 90°).

**Order of the probes (depth first, each with its rule fixed before its run).** Probe `e16a_tokens_pair` on the three
tokens (the coordinator's instruction: pair carrier, candidate cones, the gate, product-form self-duality); then, only if
its verdict renders, probe `e16b_hybrid` on the residual (A3); the written general argument last.

**Predictions for `experiments/e16a_tokens_pair.py`** (sign, strength, reason): every check PASS and every
countercontrol failing as stated. Gate: the tokens' NOT `diag(−1, −1, 1, 1)` has `tr H = 1`, so `tr(actC N) = 5` and
`tr(actC N ∘ actT N) = 1` on `W 4` (certain: arithmetic); no diagonal involution of `ℝ⁴` meets the identity (certain);
the table `d = 1 … 6` meets it exactly at `tr H = 0`, odd `d` (certain); the kernel's `cnot` (d = 3), `cnot1` (d = 1)
and `gRev 2` (d = 5) satisfy relC on every basis table (very high: landed theorems `cnot_relC`, `nativeGate_cnot1`,
`gateRel_gRev` [K]); `refl3`, `negId3` fail the identity (certain). Self-duality: `(5/6, 0, 0, 5/6) ∈ Ω₄` has squared
norm `25/18 > 1`, so `C(Ω₄)` is not self-positive for `I`, and the axis values force any `Aut`-invariant self-dualizing
form to be `aI` (very high); the ball `eball 4` passes the same test (control); for Ω⋆ and Ω_cs the table
`ω_Φ = M⁻¹` lies in `K_max` and pairs `tr R = −1` with the positive bilinear form `M R` (`R : X ↦ −X`), so
`K_min ≠ K_max` (very high).

**Prediction for the node.** (A1)–(A2) hold: the pair level with the gate excludes chart dimension 4 for every body
and, with the drive, forces the ellipsoid below chart dimension 5 with no introduced hypothesis; (A3) gives the negative
answer in chart dimension 7 unless the probe finds a clause the hybrid fails (moderate-high: positivity of the hybrid
gate rests on the block structure of its maximal cone, written before the probe); the decisive question with K∞-Geom
added stays OPEN.

## 1. Probe a — the three chart-4 tokens (measured)

`experiments/e16a_tokens_pair.py` run 1 (started 03:35:01Z, after commit `aca4fc91`; decision rule unchanged): 11/11,
`COUNTER XG1/XG2/XS1/XS2 fails as stated`, `VERDICT E16A-CHART4-PAIR-LEVEL-SEPARATED`; replay byte-identical (py
`b032f5c4…`, out `fa854faf…`). Measured: the tokens' NOT `diag(−1, −1, 1, 1)` (the flow of `rotFun4` at `π`, parsed) has
`tr H = 1`, so on `W 4` `tr(actC N) = 5` and `tr(actC N ∘ actT N) = 1`: no invertible gate satisfies relC; the same holds
for all fifteen non-identity diagonal involutions of `ℝ⁴`; for `d = 1 … 6` the count is met exactly at
`(d, m) = (1, 1), (3, 2), (5, 3)`; the kernel's `cnot` (with `nflip`), `cnot1` (with `neg1`) and `gRev 2` (with
`nK 2 = diag(1, 1, −1, −1, −1)`) satisfy relC, all with `tr H = 0`; `refl3`, `negId3` do not meet the count (8 against 4,
−8 against 4). Self-duality: `(1, y)` and `(1, −y)`, `y = (5/6, 0, 0, 5/6) ∈ Ω₄`, pair `−7/18` for the Euclidean form, the
ball's sample pairs are all `≥ 0`; for Ω⋆ (43 exact cone points pairwise `≥ 0` for its `M`) and Ω_cs, the table `M⁻¹`
lies in `K_max` and pairs `tr R = −1` with a form that is nonnegative on products: `K_min ≠ K_max`. Every S0 prediction for
the probe held. **The three instances agree with (A1) and (A4).**

## S0-b (written 2026-10-11T03:36Z, after probe a and before probe b) — the residual, odd chart dimension

**Why this branch.** (A1)–(A2) settle chart dimension below 5 with no introduced hypothesis; the decisive question is
then whether odd chart dimension `≥ 5` admits a non-ellipsoidal token meeting the pair-level hypotheses. A negative answer
needs an exact body (rule 1). The candidate of (A3) is tested exactly, every clause in the kernel's form.

**The body.** Ω_h ⊂ ℝ⁷, chart coordinates `y = (w, a, b)`, `a, b ∈ ℝ³`; sector weights `t₀ = (1 + w)/2`, `t₁ = (1 − w)/2`,
sector Bloch parts `r₀ = (a + b)/2`, `r₁ = (a − b)/2`; Ω_h = `{|r₀| ≤ t₀, |r₁| ≤ t₁}` — a qubit with a two-sector
superselection rule (its cone `L₃ ⊕ L₃`). Homogenized coordinates `(T, w, a, b)` are the image of `V_q ⊗ V_b` (qubit
table index ⊗ sector index) under the linear map `Φ`: `T = t₀ + t₁`, `w = t₀ − t₁`, `a = r₀ + r₁`, `b = r₀ − r₁`.
NOT `N = 1 ⊕ nflip ⊕ nflip` on `(w, a, b)`, corner `z = (0, e₃, 0)` (unit; `hom z = hom_q(z3) ⊗ (e₀ + e₁)/2`). Gate
`G = (Φ ⊗ Φ)(cnot ⊗ id)(Φ ⊗ Φ)⁻¹` on `W 7`. Drive: `ball3Drive`'s flow and `J` acting on `a` and `b` together. Composite
`K = {ω : every sector block of (Φ ⊗ Φ)⁻¹ ω is in Q3}`.

**Predictions for `experiments/e16b_hybrid.py`** (sign, strength, reason). Every check PASS: Ω_h's chart objects (`IsNot`;
the drive's fields at exact angles; a sharp seed; compact, convex, interior), `NativeGate`'s five clauses on all 64 basis
tables (frame, relT, relC) and on exact product inputs (`posFwd`, `posInv`: each sector block of the image is a PSD
table, so every product of effects — which decompose by sector — is nonnegative; checked also directly on sample extreme
effects), `G` an involution, `Entangling` (the image of the pure product `(sector 0, +x) ⊗ (sector 0, +z)` has block
`phiW`, a non-product table), `tr H = 0` (the count of (A1) at `d = 7`); the composite `K` contains the products, is
invariant under `G` and under the drive on one token, and is self-dual for the product form `M ⊗ M` with `M` Euclidean in
the `V_q ⊗ V_b` basis (blockwise `Q3 = dualW Q3`); and Ω_h is no ellipsoid (a boundary segment) and fails `SingletonFaces`
(the zero face of the sector weight `t₁` is the sector-0 ball). Strength: high for the algebra (every clause reduces to
the kernel's `d = 3` facts blockwise), moderate-high that the chart transport through `Φ` is coded right on the first
run (D1-type checks expose it). Countercontrols, each failing as stated: `SingletonFaces` for Ω_h; "Ω_h's boundary holds
no segment"; "the gate with `cnot` replaced by the identity is entangling".

**Decision rule** (in the probe's header, fixed now): `VERDICT E16B-HYBRID-MEETS-PAIR-LEVEL-NOT-ELLIPSOID` iff every
check and every countercontrol behaves as stated.

## 2. Probe b — the hybrid token (measured)

`experiments/e16b_hybrid.py` run 1 (started 03:43:23Z, after commit `f540b32c`; decision rule unchanged): 7/7,
`COUNTER XH1/XH2/XH3 fails as stated`, `VERDICT E16B-HYBRID-MEETS-PAIR-LEVEL-NOT-ELLIPSOID`; replay byte-identical (py
`6a53bad3…`, out `105c8f85…`). Measured: `IsNot Ω_h z N` with the parsed `nflip` in both sectors; the drive's fields at
two exact angles and `J_off_axis`; the frame, relT and relC on all 64 basis tables of `W 7` (a complete check of these
linear identities) and `G ∘ G = id`; `tr H = 0` at `d = 7`, as the count of (A1) requires; all 100 images
`G(prodState x y)` of exact state pairs have PSD sector blocks, and 6400 values of extreme product effects on them are
`≥ 0` (minimum 0); the image of the pure product `(sector 0, +x) ⊗ (sector 0, +z)` has a rank-4 block, so it is no
product; the composite `K` contains the 100 products and is mapped into itself by the gate, the flow and `J` on 35
elements; a boundary segment and a two-point zero face. Every S0-b prediction held.

## 3. The general case (written, after the instances agreed)

**(G1) The control relation counts dimensions for every body.** For any set Ω ⊂ ℝ^d, any `z ≠ 0` and linear involution
`N` with `N z = −z`, and any linear equivalence `G` of `W d` with relC: `(d + 1) tr H = (tr H)²` and `tr H ≠ d + 1`, so
`tr H = 0`, `d` odd and `N` has `(d − 1)/2` eigenvalues `+1` (traces of similar maps; `actC N = H ⊗ 1`,
`actC N ∘ actT N = H ⊗ H` as maps of `W d`). The body, the frame, positivity, relT and self-adjointness of `N` are not
read. This is the archive's count N1.3 [A] read for every body; probe a measured its instances and controls. In
particular no body of even chart dimension carries a native gate.

**(G2) With a drive, below chart dimension 5 the ellipsoid follows with no introduced hypothesis.** Let Ω be compact,
convex, with interior (TRB-1's hypotheses), carry `ElementaryDrivability`, a NOT and a gate with relC. By (G1) `d` is odd.
If `d = 1`, Ω is a segment, an affine image of `[−1, 1]`; drivability transfers along affine equivalences (conjugate the
flow and `J`), and `[−1, 1]` is not drivable (`not_drivable_Icc`, KInfFoundations.lean:529 [K]); so `d ≠ 1`. If `d = 3`,
the drive forces the ellipsoid (NOTES-E2 R3: the closure of the flow and its `J`-conjugate is SO(3) in an invariant inner
product, by the classification of closed connected subgroups of SO(3) [L]); the ellipsoid is boundary transitive under
its affine automorphisms. R3's caveat — that the K route could not use it before DIM-1, whose selector is stated on
`eball d` — lapses: (G1) does not use the ball. **Form: OI ⇒ (d = 3 ∧ Ω an ellipsoid) ∨ (d odd ∧ d ≥ 5)**, every
hypothesis of kind (i): I3.8 (`IsNot`: involution, flip, unit corner; assumed), I3.9 (`NativeGate`: relC and the gate's
invertibility only; assumed), I3.66 (`ElementaryDrivability`; assumed/open), and the token body itself — the completed
body of K∞-Stage (I3.167, open), compact, convex, with interior as TRB-1's theorems (I3.88–I3.89, proved [K]) take it —
all unsourced at L. (S0's (A2) cited the body hypotheses as "TRB-1's, I3.88–I3.89, assumed"; those two items are proved
theorems that carry the hypotheses, and the inventory item that supplies the body is K∞-Stage.) Equivalently
**OI + {chart dimension at most 4} ⇒ ellipsoid**, the dimension bound introduced, not an OI premise.
The three chart-4 countermodels to "the single-system seams give K∞-Trans" (Ω₄ of S4, Ω⋆ and Ω_cs of E13) are excluded by
the gate's control relation — for a reason that does not see their shape, since it excludes `eball 4` as well.

**(G3) In odd chart dimension the pair-level hypotheses do not give the ellipsoid: the exact body Ω_h.** Ω_h meets every
pair-level hypothesis in the kernel's form and is not an ellipsoid (probe b; the written steps: positivity for all
inputs, because every sector block of `G(prodState x y)` is `cnot` of a product of two Lorentz-cone vectors, which
`nativeGate_cnot` [K] puts in `maxCone (eball 3)`, and every product effect of Ω_h is a sum of nonnegative multiples of
qubit product effects on the blocks; extremality of the entangled image, because the normalized maximal cone of Ω_h is
the convex hull of four copies of the qubit's, one per sector pair, and `phiW` is extreme in the qubit's
(`entangling_cnot` [K]); self-duality of `K` for the product form `M ⊗ M`, `M` Euclidean in the `V_q ⊗ V_b` basis,
because the dual of a product of independent blocks is the product of the blocks' duals and `Q3 = dualW Q3`
(`Q3_selfDual` [D]); the drive's fields at every `t`, because they are `ball3Drive`'s in each sector). Its standing:

| item (inventory id) | Ω_h | evidence |
|---|---|---|
| the token body: K∞-Stage's completed body (I3.167), with `SCInf`, `BinaryVisible`, `FiniteRank` (I3.94–I3.96) | meets | [W]: compact, convex (two second-order-cone constraints), the origin interior; a single-stage presentation with the sector-blind `z`-test as its binary visible test |
| the elementary scope (I3.167's unformalized part; I3.177) | not formalized at L | Ω_h has four perfectly distinguishable states (sector ⊗ `z`-basis, effects `(t_i ± r_i·e₃)/2`), the qubit two |
| P1: products in `K`, `K ⊆ maxCone Ω_h` (I3.43's clauses, Ω_h's version) | meets | [X] H6, [W] blockwise |
| `IsNot` (I3.8) | meets | [X] H1 |
| `NativeGate` (I3.9): frame, relT, relC | meets | [X] H3, complete on a basis |
| `NativeGate` (I3.9): posFwd, posInv | meets | [X] H4 on instances; [W] from `nativeGate_cnot` [K] |
| `Entangling` (I3.10) | meets | [X] H5 (no product); [W] extremality from `entangling_cnot` [K] |
| `ElementaryDrivability`, K∞-Drive (I3.66, I3.169) | meets | [X] H2; [W] every `t` |
| `SharpSeed`, K∞-Seed (I3.73, I3.171) | meets | [X] H1 |
| one NOT on both copies, K∞-Copy (I3.173) | meets | by construction (`NativeGate`'s single `N`) |
| reversible operations, K∞-Act (I3.168); seed-orbit availability with full effects, K∞-V4 (I3.75, I3.172) | meets | [W]: the flow members and `J` are body-preserving affine equivalences; every transport of an effect along them is an effect |
| `SingletonFaces` / `RelStrictConvex`, K∞-Geom (I3.62, I3.63, I3.174) | **fails** | [X] H7 (a two-state zero face; a boundary segment) |
| `BoundaryTransitive`, K∞-Trans (I3.76, I3.170) | **fails** | [W]: Ω_h is no ellipsoid (H7), so by TRB-1 (TransitiveBody.lean:602 [K]) no body-preserving family is boundary transitive |
| central symmetry (`CentrallySymmetric`, KInfFoundations.lean:160) | fails | [W]: the only candidate centre is the origin (fixed by `O(3)` on both sectors and by the sector swap `(w, a, b) ↦ (−w, a, −b)`), and `−(1, e₃, e₃) ∉ Ω_h` |
| gate invariance of `K` (H2's form, I3.148) — introduced | meets | [X] H6; [W] |
| product-form self-duality of `K` (H3's form, I3.149) — introduced | meets | [W] from `Q3_selfDual` [D]; [X] instance |
| drive invariance of `K` (A_miss's form, I3.150/I3.153) — introduced | meets | [X] H6; [W] |

So the decisive question has a **negative answer**: the pair-level results do not imply the transitivity without adding
an assumption. **Form: OI + {gate invariance of K, product-form self-duality, drive invariance of K} ⇏ ellipsoid**, the
three named hypotheses introduced, not OI premises, and the OI items I3.8, I3.9, I3.10, I3.43, I3.66, I3.73, I3.173 all
met by Ω_h, with the token body (I3.167's formalized clauses), K∞-Act and K∞-V4. The assumption whose absence lets Ω_h
through is K∞-Geom (I3.174) — an inventory item, open and unsourced at L — in its role of excluding superselection
sectors (the archive's "Barnum–Wilce territory" for non-ball local systems); the elementary scope (I3.177), not
formalized at L, would exclude Ω_h as well if it bounds the number of perfectly distinguishable states by two. The
negative answer is stated for this class: the hypotheses in their kernel form, without K∞-Geom and without an
elementary-scope predicate.

**(G4) Product-form self-duality adds exactly token self-duality** (both directions written in S0 (A4); instances in
probe a): it excludes Ω₄ and admits Ω⋆ and Ω_cs. By HO-19 it is not a source of K∞-Trans. Without the gate, the ball's
own composite is not singled out either (`Q3` and `actT reflY (Q3)` both meet P1, P3 and the drive invariance; K2Guard).

**(G5) The residual, OPEN.** With K∞-Geom added (strict convexity or singleton faces), does a drivable, non-ellipsoidal
body of odd chart dimension `≥ 5` carry a native gate? If none does, **OI ⇒ ellipsoid** with OI carrying I3.8, I3.9,
I3.66, I3.167 (the body) and I3.174 — the pair level would then supply K∞-Trans with no introduced hypothesis.
For balls DIM-1's selector excludes `d ≥ 5` (`dim_of_nativeGate`, CompositeDimension.lean, I3.18 [K]); its block
reduction uses the ball, and no argument for strictly convex non-balls is known to this thread.

## 4. Outcome (§A.31)

- Productivity test met: (a) the decisive question is answered negatively with an exact body (Ω_h), and positively in
  the stated scope (chart dimension below 5) in the form "OI ⇒ X"; (b) the residual is isolated with every hypothesis
  classified (G5). **NEW**: the dichotomy (G2) — the gate's control relation and the drive give the ellipsoid below chart
  dimension 5 with no introduced hypothesis, and they exclude every chart-4 countermodel of the separation record;
  **NEW** in the kernel's vocabulary: Ω_h meets every pair-level clause and is no ellipsoid, so K∞-Geom is load-bearing for
  "pair level ⇒ K∞-Trans" (CONFIRMING [L] that superselection must be excluded by a separate premise).
  **CONFIRMING** [A]: the body-independence of the relC count (N1.3). **ELABORATING** HO-19: product-form pair
  self-duality reduces to token self-duality.
- Skepticism on the favourable branch (G2): it is relative to a gate the inventory records as assumed and unsourced
  (I3.9), to `IsNot`, and to the drive; R3 is a written argument with a literature input, not a kernel theorem; and it
  excludes `eball 4` as well, so it selects dimensions, not shapes. On the negative branch (G3): positivity, extremality
  and self-duality are proved in writing from kernel and design facts blockwise and checked exactly on instances; Ω_h is
  a superselection body with four perfectly distinguishable states, which an elementary-scope predicate (not formalized
  at L, I3.177) bounding that number by two would also exclude. Before the closing commit the standing table was
  checked against the inventory's single-system hypothesis-structures (I3.50, I3.57–I3.76, I3.92–I3.108) and K∞
  obligations (I3.166–I3.177): with full effects `MixingClosed`, SEC and K∞-1 hold (supporting hyperplanes of a compact
  convex body with interior), ORD∞ holds (a flow member of infinite order), and no assumed or open item other than
  K∞-Geom (`SingletonFaces`, I3.62) and K∞-Trans (I3.76) excludes Ω_h; central symmetry (I3.65) is a definition used by
  Lemma D, not an assumed premise.
- **Assumption-watch marker** (new): a pair-level source of K∞-Trans must exclude superselection sectors (K∞-Geom or an
  elementary-scope predicate) and must work in odd chart dimension at least 5; separation countermodels in even chart
  dimension (Ω₄, Ω⋆, Ω_cs) are excluded by the gate's control relation for every body and so say nothing about the pair
  level.

## 5. Scope of the negative answer (coordinator addendum 3, 04:31Z)

Stage 6 established `A_reached ⊭ (b)` for the 118 transferred pair-level rows; the 68 rows not reached have not been
shown irrelevant. The same limit applies here: Ω_h meets the inventory items listed in (G3)'s table at their status at
L, so the ellipsoid (and K∞-Trans) is independent of those premises together with the three introduced hypotheses — not
of OI. Whether a row not reached at stage 6, once transferred, would exclude Ω_h is not decided by this node. RESULTS
R-E16.3 and the LEDGER's round-4 K∞-Trans note carry the form with the listed items in place of "OI".

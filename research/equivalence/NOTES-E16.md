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

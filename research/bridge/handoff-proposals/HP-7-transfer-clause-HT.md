# HP-7 — the transfer clause at one rational angle: its weakest H-level premise H-T, and what H-T does not reach

From `research/bridge`, node B10 (round 3). Proposed for the origin thread (sourcing targets on one token) and the
equivalence thread (the K2 schema, HO-13). The coordinator routes.

## Statements and labels

1. **The NOT half excludes nothing** (B10-1). `nflip` on either token preserves K(Z_F): it permutes `Z_F`, is a signed
   permutation, and is `Ad(X)` under the dictionary. Against K(Z_F), the excluding content of (T) at
   `θ₀` (`cos θ₀ = 3/5`) is invariance under the single infinite-order frame-axis rotation `R_z(θ₀)`.
   Label: CONJECTURE (exact computation, not kernel-checked; no named premise) for K(Z_F). The part about B4's
   realization (129 certified register tables) is CONDITIONAL on branch (a), as B4-1.
2. **B4's realization fails exactly (A)** (B10-2). `R_z(θ₀)` on token B satisfies (W) and (P), and LT holds. A joint
   effect certified in K(Z_F), with its complement, gives `⟨y, actT R_z(θ₀) w0⟩ = −2/5`. Controls: `Q3` gives `9/20`;
   `R_z(π)` passes on all 129 tables. By B1.1 every hidden realization obeying (W) and (P) fails (A) the same way.
   Label: CONDITIONAL (on branch (a) and B4-1; realization-independence on B1.1, a design module [D]).
3. **H-T, the weakest premise** (B10-3). In the pair context, (A) holds with (W) and (P) on one token for:
   - one infinite-order frame-axis rotation, or a dense directed family of finite-order ones;
   - the NOT.

   This is the weakest premise in NOTES-B1's vocabulary that yields (T) at `θ₀`. Dropping (A) leaves nothing, and the
   readout-only form is (b_H) itself.
   Label: CONDITIONAL (H-T assumed, unsourced; the realization theorem's H-level constraints do not imply it, by B4).
   As a bridge FAILED: the disguise test fails. H-T is OI⁺-1's spectator clause at level H for one operation
   (GR.md:228).
4. **H-T is strictly weaker than H-OI_g** (B10-4). With H1–H3 and `cnot`, H-T leaves exotic cones. The generated closed
   group has identity component the abelian 2-torus `exp(i(a Z_B + b Z_A Z_B))`, all of whose eigenlines are products.
   H-T ∧ (A)_J is H-OI_g at `{R_z(θ₀), J}`: the split relocates the spectator clause and does not shrink it.
   Label: CONDITIONAL (on claim (D) [A] through B7-2; on the stage-4 record [A]; on HO-13 item 2).
5. **The continuous half is locally finite** (B10-5). `G_n = ⟨CNOT, 1⊗diag(1, e^{2πi/2ⁿ}), 1⊗X⟩` is finite, of order
   `4^{n+1}` modulo phase, and `G_n ⊆ G_{n+1}`. The closure of the union contains `R_z(t)` on token B for every `t`.
   `R_z(θ₀)` itself lies at no finite stage (`tr = 64/5` on `W 3`; it crosses stages by CompositionOrder.lean:378 [K]).
   Label: CONJECTURE ([X] for `n ≤ 4`, [W] for all `n`; no named premise). The H-level form is CONDITIONAL on (A) at
   each stage.
6. **Assumption-watch marker** (B10-6). Read configuration-wise at level H, the certified
   `substratumClass_contextStable` (StructuralClosure.lean:261) is L-REG: Bell-local, and it hosts no candidate pair
   cone, `Q3` included. The transfer route identifies the matrix carrier's Kronecker composite with a product
   configuration space.
   Label: CONDITIONAL (on that reading [W]); the matrix theorem CERTIFIED [K at L, StructuralClosure.lean:261].
7. **The realization theorem does not imply H-T** (B10-7). B4 meets the constraints of Main.md:544–558 and violates
   H-T. Its certified instance contains the 3-4-5 rotation as one fixed step map at finite horizon (opglue_probes.py:9).
   Label: CONDITIONAL (reading of Main.md:544–558 [W]); the matrix-level non-implication of membership CERTIFIED
   [K at L, OIRealization.lean:360].

## Evidence

| item | pointer |
|---|---|
| notes | `research/bridge/NOTES-B10.md` §1–§7 (commit 5596c0ca) |
| script | `experiments/b10_transfer.py`, 10/10 PASS, VERDICT B10-EXACT, replay byte-identical |
| results | `RESULTS.md` rows B10-1 … B10-7 |
| kernel lines (checked at L) | CompositionOrder.lean:348/:378; StructuralClosure.lean:261; OIRealization.lean:360; SpectatorBridge.lean:223/:233 |

## What the recipient may assume

Items 1–7 at their labels. For origin: on one token the sourcing target for (T) at `θ₀` is H-T, i.e. (A) for one
infinite-order frame-axis rotation and for the NOT. Since a stage-preserving datum has finite order, that rotation must
cross stages. For equivalence: (T) at one rational angle with `J` is HO-13's clause. Its H-level premise is
H-OI_g at `{R_z(θ₀), J}`, not anything weaker.

## What the recipient may not assume

- that H-T, (A), (b), or any token operation is sourced at L: none is;
- that H-T is a bridge from embedded observation: the disguise test fails;
- that local finiteness (item 5) yields (T) without (A) at every stage;
- that the (A)-failure is certified for every realization: realization-independence rests on B1.1, a design module
  built in CI, not certified;
- anything beyond two tokens.

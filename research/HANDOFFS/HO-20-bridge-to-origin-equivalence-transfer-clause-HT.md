# HO-20 (v1) — bridge → origin, equivalence: H-T, the weakest H-level premise for the transfer clause at one rational angle; what H-T does not reach; the L-REG marker

**From** `research/bridge` (round 3, node B10). **To** `research/origin` (the sourcing target on one token) and
`research/equivalence` (the H-level premise behind HO-13's clause). Written by the coordinator from the source thread's
committed record; version 1, 2026-10-11. Sharpens HO-12 items 1 and 4 (the clause (T) and the relocation) with the
weakest premise that yields (T) at `θ₀`, `cos θ₀ = 3/5`.

## Statements and labels

1. **The NOT half excludes nothing** (B10-1). `nflip` on either token preserves K(Z_F): it permutes `Z_F`, is a signed
   permutation of the sixteen coordinates, and is `Ad(X)` under the dictionary. Against K(Z_F) the excluding content of
   (T) at `θ₀` is invariance under the single infinite-order frame-axis rotation `R_z(θ₀)`. Label: CONJECTURE (exact
   computation, not kernel-checked; no named premise) for K(Z_F); the part about B4's realization (129 certified register
   tables) CONDITIONAL on branch (a), as B4-1.
2. **B4's realization fails exactly (A)** (B10-2). `R_z(θ₀)` on token B satisfies (W) and (P), and LT holds; a joint
   effect certified in K(Z_F), with its complement, gives `⟨y, actT R_z(θ₀) w0⟩ = −2/5` (controls: `Q3` gives `9/20`;
   `R_z(π)` passes on all 129 tables). By B1.1 every hidden realization obeying (W) and (P) fails (A) the same way.
   Label: CONDITIONAL (on branch (a) and B4-1; realization-independence on B1.1, a design module [D]).
3. **H-T, the weakest premise** (B10-3). In the pair context, (A) holds with (W) and (P) on one token for (i) one
   infinite-order frame-axis rotation, or a dense directed family of finite-order ones, and (ii) the NOT. This is the
   weakest premise in NOTES-B1's vocabulary that yields (T) at `θ₀`; dropping (A) leaves nothing, and the readout-only
   form is (b_H) itself. **As a bridge from embedded observation: FAILED** — the disguise test fails; H-T is OI⁺-1's
   spectator clause at level H for one operation (GR.md:228). Label: CONDITIONAL (H-T assumed, unsourced; the
   realization theorem's H-level constraints do not imply it, item 7).
4. **H-T is strictly weaker than H-OI_g** (B10-4). With H1–H3 and `cnot`, H-T leaves exotic cones: the generated closed
   group has identity component the abelian 2-torus `exp(i(a Z_B + b Z_A Z_B))`, all of whose eigenlines are products
   (Lie closure of `{1⊗Z}` under `Ad(CNOT)`, `Ad(1⊗X)` and commutators: dimension 2, `span{1⊗Z, Z⊗Z}`). H-T ∧ (A)_J is
   H-OI_g at `{R_z(θ₀), J}`: the split relocates the spectator clause and does not shrink it. Label: CONDITIONAL (on claim
   (D) [A] through B7-2; on the stage-4 record [A]; on HO-13 item 2). The cone side of "H-T leaves exotic cones" is
   carried, for the Clifford half, by HO-25 item 1 (an explicit cone through Theorem S′ [W] instead of claim (D)).
5. **The continuous half is locally finite** (B10-5). `G_n = ⟨CNOT, 1⊗diag(1, e^{2πi/2ⁿ}), 1⊗X⟩` is finite, of order
   `4^{n+1}` modulo phase (16, 64, 256, 1024 for `n ≤ 4`), with `G_n ⊆ G_{n+1}`; the closure of the union contains
   `R_z(t)` on token B for every `t`. `R_z(θ₀)` itself lies at no finite stage (`tr = 64/5` on `W 3`, `16/5` on
   `HVec 3`; `6/5` is no algebraic integer; it crosses stages by CompositionOrder.lean:378 [K]). Label: CONJECTURE ([X]
   for `n ≤ 4`, [W] for all `n`; no named premise); the H-level form CONDITIONAL on (A) at each stage.
6. **Assumption-watch marker, L-REG** (B10-6). Read configuration-wise at level H, the certified
   `substratumClass_contextStable` (StructuralClosure.lean:261) is L-REG: Bell-local, and it hosts no candidate pair
   cone, `Q3` included. The transfer route identifies the matrix carrier's Kronecker composite with a product
   configuration space. Label: CONDITIONAL (on that reading [W]); the matrix theorem CERTIFIED [K at L].
7. **The realization theorem does not imply H-T** (B10-7). B4 meets the constraints of Main.md:544–558 and violates
   H-T; its certified instance contains the 3-4-5 rotation as one fixed step map at finite horizon (its Bloch image a
   rotation about `y` with trace `11/25`). Label: CONDITIONAL (reading of Main.md:544–558 [W]); the matrix-level
   non-implication of membership CERTIFIED [K at L, OIRealization.lean:360 `finiteOI_not_implies_inert`].

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `7abe4da4` (round-3 commits `0ccc1bef` … `7abe4da4`) |
| proposal | `research/bridge/handoff-proposals/HP-7-transfer-clause-HT.md`, sha256 `3d8eec3007d213491026711dd23fe3a51bd2de3f13e576be402512e93563b819` |
| results, notes | `research/bridge/RESULTS.md` sha256 `07b89737cb13ac2efe04f58b8af834ac968c5c71433e16439af31204600055c0` (rows B10-1 … B10-7); `NOTES-B10.md` `98b877ef00318d0db7167d8aad8a316f9ad470a4fa6719617755d3bdb4376925` (§1–§7) |
| script, output | `experiments/b10_transfer.py` `6302846c6ce3603423b3626d612bd84c5b823fd8b59d8c4518b909e92f643fe2` / `.out` `0c96cc44b9e124830f6531c31a0ca82f7c1ebf81c1b210e7fb182cabecf3277a` (10/10, VERDICT B10-EXACT; replayed byte-identically) |
| kernel lines (checked at L by the coordinator) | CompositionOrder.lean:348/:378; StructuralClosure.lean:261; OIRealization.lean:360; SpectatorBridge.lean:223/:233 |
| coordinator audit | replays 5/5; `indep_checkB3.py` run 2 4/4 — X2 (`nflip` permutes `Z_F` and is a signed permutation; `R_z(π)` permutes `Z_F` and pairs nonnegatively with the coordinator's certified members of K(Z_F); `actT R_z(θ₀)` carries `Z_F` defects to tables pairing negatively with certified members, 48 negative pairings, e.g. `−4/5`; `6/5` not an algebraic integer; the traces `64/5`, `16/5`; the orders 16, 64, 256, 1024 with the inclusions; the Lie closures of dimension 2 abelian and, with `Ad(1 ⊗ U_J)`, dimension 6 commuting with `Z ⊗ 1`; the 3-4-5 rotation's trace `11/25`); B10 §3 (H-T as the weakest premise; the disguise-test failure as OI⁺-1's clause at level H), §4, §5, §6 read: sound; 25/25 citations at L — `research/AUDITS/2026-10-11-round3/AUDIT-BRIDGE-R3.md` |

## What the receiving threads may assume

Items 1–7 at their labels. **Origin:** on one token the sourcing target for (T) at `θ₀` is H-T — (A) with (W) and
(P) for one infinite-order frame-axis rotation and for the NOT; since a stage-preserving datum has finite order
(CompositionOrder.lean:378), that rotation must cross stages (HO-22 items 2–5 say what a stage-crossing substratum
must supply). **Equivalence:** (T) at one rational angle with `J` is HO-13's clause; its H-level premise is H-OI_g at
`{R_z(θ₀), J}`, not anything weaker (item 4); item 6 as a marker for any argument that reads the certified
`ContextStable` theorem configuration-wise.

## What they may not assume

- that H-T, (A), (b) or any token operation is sourced at L: none is;
- that H-T is a bridge from embedded observation: the disguise test fails (item 3);
- that local finiteness (item 5) yields (T) without (A) at every stage;
- that the (A)-failure is certified for every realization: realization-independence rests on B1.1, a design module
  built in CI, not certified;
- that the value `−2/5` was recomputed by the coordinator: it is B4's (audited in round 1); the non-invariance of K(Z_F)
  under `actT R_z(θ₀)` was confirmed with the coordinator's own certified witnesses;
- anything beyond two tokens.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-20 v1` and records in its `LOG.md`
whether and how it relies on it.

# HP-9 — HO-13's clause on substrata: the finite half is a stabilizer, the two halves share no finite stage, and what a stage-crossing substratum must supply

From `research/bridge`, node B12 (round 3). Proposed for the origin thread (sourcing of the token's infinite-order
datum), the equivalence thread (why HO-13's clause forces `Q3` and its finite part does not) and the countermodels
thread (two group nodes for the composite-cone classification). The coordinator routes.

## Statements and labels

1. **The finite half with the gate is a stabilizer** (B12-1). `G₁ = ⟨cnot, actT J, actT S, actT nflip⟩` is exactly the
   stabilizer of `Z ⊗ 1` in the two-qubit Clifford group: `|G₁| = 384 = 11520/30`. It equals HO-13 item 3's group
   `⟨cnot, actT S, actT J⟩`; `⟨cnot, actT J⟩` alone has order 48. `G₁` permutes the 60 two-qubit stabilizer states
   (readout rank 16), so the finite half is realized by readout-respecting permutations of a fixed finite substratum.
   Label: CONJECTURE (exhaustive exact computation, not kernel-checked; no named premise).
2. **The two halves share no finite stage** (B12-2). On one token, `J · R_z(2π/m)` has trace `−sin(2π/m)`. It has
   finite order only if `−1 − sin(2π/m)` is an algebraic integer, i.e. only for `m ∈ {1, 2, 4}` (norm argument). So:
   - every finite rotation group holding `J` contains `z`-rotations of order 1, 2 or 4 only. The group itself is not
     bounded by 24: an icosahedral group of order 60 holds `J` and `R_z(π)`;
   - B10-5's tower (`R_z(2π/2ⁿ)` at stage `n`) admits `J` at stages `n ≤ 2` only;
   - every token-local directed tower of finite rotation groups holding `J` misses `R_z(θ₀)` in its closure.

   Label: CONJECTURE (complete written proof, not kernel-checked; exact checks for `m ≤ 24` with a positive control and
   a countercontrol; no named premise) for the finite-group statements. The tower clause is CONDITIONAL on the
   classification of finite subgroups of SO(3) [L].
3. **What the clause generates with the gate** (B12-3). `cnot`, `actT J` and `actT R_z(θ₀)` generate a closed group
   whose identity component is the block-diagonal `SU(2) × SU(2) = {P₀⊗U₀ + P₁⊗U₁}` in the control's `Z` basis. Its
   Lie algebra is `span{1⊗X, 1⊗Y, 1⊗Z, Z⊗X, Z⊗Y, Z⊗Z}`, and everything commutes with `Z ⊗ 1`. Its product orbit is
   every pure state (exact instance: HO-13's `φ₀`); the finite part `G₁` carries `φ₀` to no product. No directed
   tower of finite pair substrata realizes the clause with the gate.
   Label: CONJECTURE (exact computation and complete written proof; no named premise) for the closure and its orbit.
   The tower exclusion is CONDITIONAL on Jordan's theorem [L], through B3.2.
4. **Stage-crossing substrata exist and supply nothing** (B12-4). A word-length filtration over the 60 stabilizer
   states, with `R = actT R_z(θ₀)` crossing stages, has finite stages (`|Λ₁| = 588`). Started from a dense subset of
   any closed invariant cone, it realizes that cone. Over B4's register tables it hosts K(Z_F), where (A) fails for
   `J` (`−1/2`) as for `R_z(θ₀)` (`−2/5`).
   Label: CONJECTURE ([X] for the stages computed, [W] for all). The B4 part CONDITIONAL on branch (a).
5. **B12-S, what a stage-crossing pair substratum must supply** (B12-5):
   - (S1) an infinite-order datum on the token, not available on a passive, repeatable, finite-rank tower (HO-9
     item 3); the known candidate is Origin's open premise (HO-9 items 4–5);
   - (S2) `J`, stage-preserving and finitely sourced;
   - (S3) `R_z(θ₀)` crossing every stage structure that carries `J` and `cnot`;
   - (S4) availability in context (A), with (W) and (P), for `J` and `R_z(θ₀)` in the pair context, in branch (a).
     This is H-OI_g at `{R_z(θ₀), J}`.

   Label: CONDITIONAL (on HO-9 items 3–5 and HO-13 item 2 at their labels; on [L] as above).

## Evidence

| item | pointer |
|---|---|
| notes | `research/bridge/NOTES-B12.md` §1–§6, S0 and S0′ (commit 69fbbc53) |
| scripts | `experiments/b12_stagecross.py` (8/8, VERDICT B12-EXACT) and `experiments/b12_followup.py` (3/3, VERDICT B12F-EXACT), both replay byte-identical |
| results | `RESULTS.md` rows B12-1 … B12-5 |
| kernel line (checked at L) | CompositionOrder.lean:378 (`not_stagePreserving_of_infiniteOrderOn`) |

## Use

- **Origin.** (S1) and (S4) are what the token's sourcing must deliver. By item 2, the continuous half's natural
  finite approximants and `J` share no finite stage beyond stage 2 of the natural tower (on the token, the octahedral
  group). More generally, no finite stage holding `J` holds a `z`-rotation of order other than 1, 2 or 4.
- **Equivalence.** Item 3 is the structural reason HO-13's clause forces `Q3` (through the stage-4 dichotomy [A]) and
  its finite part does not. Forcing does not need a group that acts irreducibly on the pair: the clause's group
  fixes `Z ⊗ 1`.
- **Countermodels.** Two group nodes:
  - the finite `Stab_C(Z ⊗ 1)`, order 384, which leaves exotic cones by claim (D) [A];
  - the non-abelian block-diagonal `SU(2) × SU(2)` fixing `Z ⊗ 1`, whose product orbit is all pure states.

## What the recipient may not assume

- that (A), the re-preparing law, or `R_z(θ₀)` on the token is sourced at L: none is;
- that the norm argument or any group computation is kernel-checked;
- the general-tower clauses beyond their [L] inputs;
- that (S4)'s identification with H-OI_g removes the need for (A): it relocates it;
- that the icosahedral group, or any finite group, carries a `z`-rotation of order other than 1, 2 or 4 together with
  `J`: item 2 excludes it;
- anything beyond two tokens.

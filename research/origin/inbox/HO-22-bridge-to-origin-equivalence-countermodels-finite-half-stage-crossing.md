# HO-22 (v1) — bridge → origin, equivalence, countermodels: the finite half is `Stab_C(Z ⊗ 1)`; the two halves share no finite stage; the clause with the gate closes to `SU(2) × SU(2)`; what a stage-crossing substratum must supply (B12-S)

**From** `research/bridge` (round 3, node B12). **To** `research/origin` (sourcing of the token's infinite-order
datum), `research/equivalence` (why HO-13's clause forces `Q3` and its finite part does not) and
`research/countermodels` (two group nodes for the composite-cone classification). Written by the coordinator from the
source thread's committed record; version 1, 2026-10-11.

## Statements and labels

1. **The finite half with the gate is a stabilizer** (B12-1). `G₁ = ⟨cnot, actT J, actT S, actT nflip⟩` is exactly the
   stabilizer of `Z ⊗ 1` in the two-qubit Clifford group: `|G₁| = 384 = 11520/30`. It equals HO-13 item 3's group
   `⟨cnot, actT S, actT J⟩`; `⟨cnot, actT J⟩` alone has order 48 (integer traces `{0, 2, 4, 8, 16}`, fixing `E(3,0)`).
   `G₁` permutes the 60 two-qubit stabilizer states (readout rank 16), so the finite half is realized by
   readout-respecting permutations of a fixed finite substratum. Label: CONJECTURE (exhaustive exact computation, not
   kernel-checked; no named premise).
2. **The two halves share no finite stage** (B12-2). On one token, `J · R_z(2π/m)` has trace `−sin(2π/m)` (in the
   kernel's orientation). It has finite order only if `−1 − sin(2π/m)` is an algebraic integer, i.e. only for
   `m ∈ {1, 2, 4}` (norm argument: the Galois conjugates of `cos(2πr)` lie in `[−1, 1]`, and an algebraic integer with all
   conjugates of modulus `< 1` is zero). So: every finite rotation group holding `J` contains `z`-rotations of order 1, 2
   or 4 only — the group itself is not bounded by 24: an icosahedral group of order 60 (`u = (φ − 1, φ, 1)/2`) holds `J`
   and `R_z(π)` and has exactly two `z`-axis rotations; B10-5's tower (`R_z(2π/2ⁿ)` at stage `n`) admits `J` at stages
   `n ≤ 2` only; every token-local directed tower of finite rotation groups holding `J` misses `R_z(θ₀)` in its closure.
   Label: CONJECTURE (complete written proof, not kernel-checked; exact checks for `m ≤ 24` with a positive control and a
   countercontrol; no named premise) for the finite-group statements; the tower clause CONDITIONAL on the classification
   of finite subgroups of SO(3) [L]. FAILED as a token-local tower route to `R_z(θ₀)`.
3. **What the clause generates with the gate** (B12-3). `cnot`, `actT J` and `actT R_z(θ₀)` generate a closed group
   whose identity component is the block-diagonal `SU(2) × SU(2) = {P₀⊗U₀ + P₁⊗U₁}` in the control's `Z` basis (the
   determinant-ratio homomorphism confines the group to `{det U₀/det U₁ = ±1}`). Its Lie algebra is
   `span{1⊗X, 1⊗Y, 1⊗Z, Z⊗X, Z⊗Y, Z⊗Z}`, and everything commutes with `Z ⊗ 1`. Its product orbit is every pure state
   (control-basis Schmidt form; exact instance HO-13's `φ₀ = (1, 2, 3i, −1+i)/4 = (P₀⊗U₀ + P₁⊗U₁)(a ⊗ |0⟩)`,
   `a = (√5, √11)/4`); the finite part `G₁` carries `φ₀` to no product. No directed tower of finite pair substrata
   realizes the clause with the gate. Label: CONJECTURE (exact computation and complete written proof; no named premise)
   for the closure and its orbit; the tower exclusion CONDITIONAL on Jordan's theorem [L], through B3.2.
4. **Stage-crossing substrata exist and supply nothing** (B12-4). A word-length filtration over the 60 stabilizer
   states, with `R = actT R_z(θ₀)` crossing stages, has finite stages (`|Λ₁| = 588`, `RΛ₀ ⊄ Λ₀`, `RΛ₁ ⊄ Λ₁`). Started
   from a dense subset of any closed invariant cone, it realizes that cone. Over B4's register tables it hosts K(Z_F),
   where (A) fails for `J` (`−1/2`) as for `R_z(θ₀)` (`−2/5`). Label: CONJECTURE ([X] for the stages computed, [W] for
   all); the B4 part CONDITIONAL on branch (a).
5. **B12-S, what a stage-crossing pair substratum must supply** (B12-5):
   - (S1) an infinite-order datum on the token, not available on a passive, repeatable, finite-rank tower (HO-9
     item 3); the known candidate is Origin's open premise (HO-9 items 4–5; refuted on the stated access by HO-17 item 1);
   - (S2) `J`, stage-preserving and finitely sourced;
   - (S3) `R_z(θ₀)` crossing every stage structure that carries `J` and `cnot`;
   - (S4) availability in context (A), with (W) and (P), for `J` and `R_z(θ₀)` in the pair context, in branch (a) —
     this is H-OI_g at `{R_z(θ₀), J}` (HO-20 item 4).

   Label: CONDITIONAL (on HO-9 items 3–5 and HO-13 item 2 at their labels; on [L] as above).

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `7abe4da4` (round-3 commits `0ccc1bef` … `7abe4da4`) |
| proposal | `research/bridge/handoff-proposals/HP-9-finite-half-stage-crossing.md`, sha256 `b6f5aee7f865ec606b3856e0ede3429265f8a1cf7975d5261a2160b3fabf1baf` |
| results, notes | `research/bridge/RESULTS.md` sha256 `07b89737cb13ac2efe04f58b8af834ac968c5c71433e16439af31204600055c0` (rows B12-1 … B12-5); `NOTES-B12.md` `1edc874b42c04aed39f8ce878bb22e195df440d72f1d8b1ecbc3e61157869675` (§1–§6, S0 and S0′) |
| scripts, outputs | `experiments/b12_stagecross.py` `866503e729f1aa30fdd6a912c1782ad7cf81479d4f9d74e3114d18228d346da1` / `.out` `84cdf2c8ccf467d91f0c80c7bab39319304023abe9680a3841175c284515afaf` (8/8, VERDICT B12-EXACT); `experiments/b12_followup.py` `bbacf99b62cab434fd79ef14fa125ef2c1c50060e957635b6423eedb5ca65793` / `.out` `6156fb088e860913bfe8a8309253cc8df9acbb5466517a75b802b726f9622f38` (3/3, VERDICT B12F-EXACT); both replayed byte-identically |
| kernel line (checked at L) | CompositionOrder.lean:378 (`not_stagePreserving_of_infiniteOrderOn`) |
| coordinator audit | `indep_checkB3.py` run 2 4/4 — X3 (as signed permutations of the table coordinates: `⟨cnot, actT J⟩` order 48 with the integer traces, fixing `E(3,0)`; `⟨cnot, actT J, actT S, actT nflip⟩` order 384 equal to `⟨cnot, actT S, actT J⟩`; `⟨cnot, actC J, actT J⟩` order 11520 equal to the Clifford group with `actC S`, `actT S`, its stabilizer of `E(3,0)` the 384 group and the orbit of `E(3,0)` of 30 elements; the 60 stabilizer rays spanning 16 dimensions; the minimal polynomial of `−1 − sin(2π/m)` monic over ℤ exactly for `m ∈ {1, 2, 4}` among `m ≤ 24`, with `2 cos(2π/m)` monic for every `m` as control and `cos(2π/m)` monic exactly for `m ∈ {1, 2, 4}` as countercontrol; `tr(J R_z(φ)) = −sin φ` symbolically; the orders 12, 24 and the icosahedral 60 in `Q(√5)` with exactly two `z`-axis rotations; `φ₀`'s block-diagonal form with explicit unitaries and its unreachability by the 384 group (reduced-state purity); `|Λ₁| = 588` with the stage-crossing of `R`) and X2 (the Lie closure of dimension 6 commuting with `Z ⊗ 1`); B12 §2 (permutation-character integrality), §3 (the norm argument), §4 (the determinant-ratio homomorphism; the Schmidt form), §5 (the filtration) read: sound — `research/AUDITS/2026-10-11-round3/AUDIT-BRIDGE-R3.md` |

## What the receiving threads may assume

Items 1–5 at their labels. **Origin:** (S1) and (S4) are what the token's sourcing must deliver; by item 2 the
continuous half's natural finite approximants and `J` share no finite stage beyond stage 2 of the natural tower (on
the token, the octahedral group), and no finite stage holding `J` holds a `z`-rotation of order other than 1, 2 or 4.
**Equivalence:** item 3 is the structural reason HO-13's clause forces `Q3` (through the stage-4 dichotomy [A]) and its
finite part does not; forcing does not need a group acting irreducibly on the pair — the clause's group fixes
`Z ⊗ 1`. **Countermodels:** two group nodes — the finite `Stab_C(Z ⊗ 1)` of order 384, for which HO-24 now supplies an
explicit exotic cone (so claim (D) is no longer needed there), and the non-abelian block-diagonal `SU(2) × SU(2)`
fixing `Z ⊗ 1`, whose product orbit is all pure states.

## What they may not assume

- that (A), the re-preparing law or `R_z(θ₀)` on the token is sourced at L: none is;
- that the norm argument or any group computation is kernel-checked;
- the general-tower clauses beyond their [L] inputs;
- that (S4)'s identification with H-OI_g removes the need for (A): it relocates it;
- that the icosahedral group, or any finite group, carries a `z`-rotation of order other than 1, 2 or 4 together with
  `J`: item 2 excludes it;
- anything beyond two tokens.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-22 v1` and records in its `LOG.md`
whether and how it relies on it.

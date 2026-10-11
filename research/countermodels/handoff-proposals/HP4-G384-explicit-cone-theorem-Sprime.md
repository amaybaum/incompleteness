# HP4 — countermodels → equivalence (and bridge), via the coordinator: an explicit exotic cone for HO-14's order-384 group; Theorem S′; every finite unitary group with `cnot` is EXOTIC-X

**From** `research/countermodels` (round 3, node C11; HO-14 v1 received 2026-10-10T23:59Z, commit `43a49d57`).
**Proposed recipients** `research/equivalence` (HO-14's request: an explicit cone invariant under
`G₃₈₄ = ⟨cnot, actT R_z(π/2), actT cyc3⟩`, the countermodel to "H1–H3 + the native octahedral repertoire on one token ⇒
`Q3`") and `research/bridge` (finite groups as carriers of the composite action). Proposal only; the coordinator routes.
Written 2026-10-11T01:11Z, item 5 revised after node C16 at 2026-10-11T01:40Z (`date -u`).

## Statements, each with its label

1. **The group.** `G₃₈₄` is a group of 384 signed permutations of the sixteen table coordinates (HO-14's order,
   recomputed); its Gaussian-rational lift (`CNOT`, `I⊗diag(1, i)`, `I⊗(I − i(X + Y + Z))/2`) maps onto it modulo
   `{±1, ±i}`; every element is `P₀⊗A + P₁⊗ωPA` (`A` a one-qubit Clifford, `ω ∈ {±1, ±i}`, `P` a Pauli); no antiunitary
   element. CONDITIONAL (`pauliW` [D] for the lift; exact [X]).
2. **No Bell-type defect survives (Theorem C11-B).** `Σ_{P∈{X,Y,Z}} |det Ψ(C_P g)|² = |a|²|b|² + |⟨a|b⟩|²` for
   `g = |0⟩a + |1⟩b`; hence every Bell-type defect is carried out of `maxCone` by `C_Y` or `C_Z` (both in `G₃₈₄`; already
   `⟨cnot, actT R_z(π/2)⟩` suffices): no `G₃₈₄`-invariant cone with H1–H3 contains a Bell-type defect, and `K(Z_F)` is not
   invariant. CONDITIONAL ([W] + [X]).
3. **Theorem S′ (a surgery theorem for rank-one defects).** For any compact set `Z` of defects `I − c_dP_d`,
   `c_d ∈ (1, 2]`, with pairwise pairings `≥ 0`, if for every pair with positive pairing the open cap
   `{|⟨h_j|v̂⟩|² > 1/c_j}` lies in the open co-cap `{|⟨h_k|v̂⟩|² > 1 − 1/c_k}` (equivalently
   `c_jc_k|⟨h_j|h_k⟩|² ≥ (√(c_j − 1) + √(c_k − 1))²`), then `K(Z) = (Q3 ∩ Z*) + cone Z` is closed and self-dual. It contains
   SD1's sufficiency (one defect) and Theorem S (orthogonal Bell sets). CONDITIONAL ([W]: a short written proof, NOTES-C11
   and NOTES-C13 C13-S; not yet audited).
4. **The explicit cone (EXOTIC-X).** `h* = (10, 2 − 2i, −1 − 3i, 3 − i)/√128`, `c* = 401/400`: the `G₃₈₄`-orbit of
   `d* = I − c*P_{h*}` has 192 defects, all pairwise squared overlaps in `[25/2048, 13/16]`, every defect admissible for H1
   (`c*λ_max ≤ 1`, exact rational test), and (CC) for all 18336 pairs; so `K(G₃₈₄·z*)`, `z* = E00/2 − (c*/8)T_{h*}`, is a
   `G₃₈₄`-invariant self-dual cone with H1–H3 and `≠ Q3`. CONDITIONAL (item 3 [W]; operator-norm bound [W]; `pauliW` [D]).
5. **HO-14's `φ₀` cannot seed an explicit surgery**: its orbit (384 rays, unreachable, min `|det Ψ|² = 5/256`) contains an
   orthogonal pair, so every rank-one orbit surgery on it fails for every `c` in its H1 window (`φ₀` is not Bell-type, so
   `c = 2` is excluded by H1; explicit `y ∈ K* \ K`, Lemma C13-O). It still seeds EXOTIC-E through claim (D) [A].
   CONDITIONAL ([W] + [X]).
6. **Every finite group of unitary conjugations containing `cnot` has an explicit exotic invariant cone** (a rank-one
   orbit surgery with `c` near 1 on a state that is unreachable and has no orthogonal pair in its orbit — an open dense set
   of states); with antiunitary elements the same unless some element is `h ↦ Uh̄` with `U` antisymmetric. This upgrades
   stage 4's "every finite group is EXOTIC-E" (Y1.5) to EXOTIC-X for these groups. CONDITIONAL (item 3 [W]; genericity
   [W]). Exact instance beyond `G₃₈₄`: the order-11520 native Clifford family (node C15; HP5 item 1).

## What the recipients may not assume
- that Theorem S′ is kernel-checked or audited (it is a written proof of this round); the cones are explicit given S′;
- anything CERTIFIED; the cones differ from `Q3` only near small caps (`c − 1 = 1/400` here, `10⁻⁵` for the Clifford group);
- T on these cones: it fails (finitely many non-PSD extreme rays, C3.3), so they say nothing about C3.1's open class.

## Evidence
`research/countermodels/NOTES-C11.md` (sha256 prefix `6aa60bc4…`); `experiments/c11_octahedral.py` (`485ffad7…`) /
`.out` (`9b4fed7b…`): run 1 12/12, `VERDICT C11-OCTAHEDRAL-EXACT`, replay identical; RESULTS rows C11.1–C11.7; S′ for
compact `Z`: NOTES-C13 C13-S (row C13.1); Lemma C13-O: row C13.2.

# HO-24 (v1) — countermodels → equivalence, bridge: an explicit exotic cone for HO-14's order-384 group; Theorem S′ (the cap/co-cap surgery theorem, read by the coordinator); every finite unitary group with `cnot` is EXOTIC-X

**From** `research/countermodels` (round 3, node C11, with C13's compact form and Lemma C13-O). **To**
`research/equivalence` (HO-14's request: an explicit cone invariant under
`G₃₈₄ = ⟨cnot, actT R_z(π/2), actT cyc3⟩`, the countermodel to "H1–H3 + the native octahedral repertoire on one token
⇒ `Q3`") and `research/bridge` (finite groups as carriers of the composite action; the cone step of B7-4 and B3.C for
finite groups). Written by the coordinator from the source thread's committed record; version 1, 2026-10-11. Answers
HO-14 v1.

## Statements and labels

1. **The group** (C11.1). `G₃₈₄` is a group of 384 signed permutations of the sixteen table coordinates (HO-14's order,
   recomputed); its Gaussian-rational lift (`CNOT`, `I⊗diag(1, i)`, `I⊗(I − i(X + Y + Z))/2`) maps onto it modulo
   `{±1, ±i}`; every element is `P₀⊗A + P₁⊗ωPA` (`A` a one-qubit Clifford, `ω ∈ {±1, ±i}`, `P` a Pauli); no antiunitary
   element. It is the group HO-22 item 1 identifies as `Stab_C(Z ⊗ 1)`. Label: CONDITIONAL (`pauliW` [D] for the lift;
   exact [X]).
2. **No Bell-type defect survives — Theorem C11-B** (C11.2). `Σ_{P∈{X,Y,Z}} |det Ψ(C_P g)|² = |a|²|b|² + |⟨a|b⟩|²` for
   `g = |0⟩a + |1⟩b`; hence every Bell-type defect is carried out of `maxCone` by `C_Y` or `C_Z` (both in `G₃₈₄`;
   already `⟨cnot, actT R_z(π/2)⟩` suffices): no `G₃₈₄`-invariant cone with H1–H3 contains a Bell-type defect, and
   K(Z_F) is not invariant. Label: CONDITIONAL ([W] + [X]).
3. **Theorem S′, the surgery theorem for rank-one defects** (C11.3, C13.1). For any compact set `Z` of defects
   `I − c_dP_d`, `c_d ∈ (1, 2]`, with pairwise pairings `≥ 0`, if for every pair with positive pairing the open cap
   `{|⟨h_j|v̂⟩|² > 1/c_j}` lies in the open co-cap `{|⟨h_k|v̂⟩|² > 1 − 1/c_k}` — equivalently, condition (CC):
   `c_jc_k|⟨h_j|h_k⟩|² ≥ (√(c_j − 1) + √(c_k − 1))²`; for a common `c`, `c²s ≥ 4(c − 1)` — then
   `K(Z) = (Q3 ∩ Z*) + cone Z` is closed and self-dual. It contains SD1's sufficiency (one defect) and Theorem S
   (orthogonal Bell sets). Label: CONDITIONAL ([W]; JordanClassification.lean:84 `psd_iff_trace_nonneg` [K]; SD1's
   block lemma [A]). **Read by the coordinator, step by step: sound** — (1) closedness from `Q ∩ (−cone Z) = {0}`
   (positive traces); (2) `K ⊆ K*` from the three kinds of pairings; (3) `K* = (Q + cone Z) ∩ Z*` through
   `(A ∩ B)* = cl(A* + B*)` and the closed sum; (4) the minimal-weight decomposition on the compact set, with the two
   cases (`t*_j > 0`: `d_j` positive definite on `ker q ⊆ u^⊥` by Bessel and `c_j ≤ 2`; `t*_j = 0`: `⟨y, d_j⟩ ≥ 0`
   forces a listed `d_k` with positive weight and positive pairing, and (CC) makes `d_k` positive definite on `ker q`),
   each contradicting minimality; the compact extension and the extremality for a common `c`. The label stays [W]: a
   written proof read by one reader, not kernel-checked.
4. **The explicit cone, EXOTIC-X** (C11.5). `h* = (10, 2 − 2i, −1 − 3i, 3 − i)/√128`, `c* = 401/400`: the `G₃₈₄`-orbit
   of `d* = I − c*P_{h*}` has 192 defects, all pairwise squared overlaps in `[25/2048, 13/16]`, every defect admissible
   for H1 (`c*λ_max ≤ 1`, exact rational test; minimum normalised `|det Ψ|²` `85/2048`), and (CC) for all 18336 pairs; so
   `K(G₃₈₄·z*)`, `z* = E00/2 − (c*/8)T_{h*}`, is a `G₃₈₄`-invariant self-dual cone with H1–H3 and `≠ Q3`. At
   `c′ = 301/300` (CC) fails on the minimal-overlap pair (pair-level sharpness). Label: CONDITIONAL (item 3 [W];
   operator-norm bound [W]; `pauliW` [D]).
5. **HO-14's `φ₀` cannot seed an explicit surgery** (C11.4). Its orbit (384 rays, unreachable, min `|det Ψ|²` `5/256`,
   `s_max = 233/256`) contains exactly one ray orthogonal to `φ₀`, so every rank-one orbit surgery on it fails for every
   `c` in its H1 window (`φ₀` is not Bell-type, so `c = 2` is excluded by H1; explicit `y ∈ K* \ K` by Lemma C13-O:
   `y = P_h + ((c − 1)/(4 − 2c))d_{h′}` for `h ⊥ h′`, `c ∈ (1, 2)`; at `c = 101/100`, `h_k†yh_k = −4/22275`). It still
   seeds EXOTIC-E through claim (D) [A]. Label: CONDITIONAL ([W] + [X]).
6. **Every finite group of unitary conjugations containing `cnot` has an explicit exotic invariant cone** (C11.6): a
   rank-one orbit surgery with `c` near 1 on a state that is unreachable and has no orthogonal pair in its orbit (an
   open dense set of states, two proper real-algebraic exceptional sets); with antiunitary elements the same unless some
   element is `h ↦ Uh̄` with `U` antisymmetric. This upgrades stage 4's "every finite group is EXOTIC-E" (Y1.5) to
   EXOTIC-X for these groups. Exact instance beyond `G₃₈₄`: the order-11520 Clifford family (HO-25 item 1). Label:
   CONDITIONAL (item 3 [W]; genericity [W]).

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `23713ce9` (round-3 commits `43a49d57` … `23713ce9`) |
| proposal | `research/countermodels/handoff-proposals/HP4-G384-explicit-cone-theorem-Sprime.md`, sha256 `952145dedaf42399fa202a8aa5726c7da957e159b78b3e68a261683dec716120` |
| results, notes | `research/countermodels/RESULTS.md` sha256 `00ebcfe1e87dce26f16e313091bc23fdb0a2265c324dcb9b0902c83e0a14489f` (rows C11.1 … C11.7; C13.1, C13.2); `NOTES-C11.md` `6aa60bc40e4bedf764e6591117aedbc2ce2c6e02d25c1e38037d481f3793846a`; `NOTES-C13.md` `19dcb7df749e5e749498d401d46e9c4169ffaa0fe1ee1044f6e89c156be76410` (C13-S, the compact form; Lemma C13-O) |
| script, output | `experiments/c11_octahedral.py` `485ffad755a366944b8ca19a7ad86f3c17b12306db9d3be73d0ffad3a9c0312b` / `.out` `9b4fed7b3769582f4e0e828edd53530ba1fcd4849e9888774ba6b4913a056fdf` (run 1 12/12, VERDICT C11-OCTAHEDRAL-EXACT; replayed byte-identically) |
| design module | none (no Lean work this round in the thread) |
| kernel line (checked at L) | JordanClassification.lean:84 `psd_iff_trace_nonneg` (the self-duality of the PSD cone) |
| coordinator audit | replays 6/6; `indep_checkC3.py` run 1 10/10 — X1 (C11-B's identity, symbolic), X2 (orders 48, 384, 11520; the stabilizer; the orbit of 30), X3 (192 rays, `85/2048`, overlaps in `[25/2048, 13/16]` over 18336 pairs, H1 and (CC) at `401/400`, (CC) failing at `301/300`), X4 (`φ₀`'s orbit of 384, `5/256`, `s_max`, the single orthogonal ray, the witness at `101/100`); Theorem S′, Lemma C13-O and C11-E's genericity read: sound; 4/4 citations at L — `research/AUDITS/2026-10-11-round3/AUDIT-COUNTERMODELS-R3.md` |

## What the receiving threads may assume

Items 1–6 at their labels. **Equivalence:** HO-14's request is answered — `K(G₃₈₄·z*)` is an explicit cone invariant
under `⟨cnot, actT R_z(π/2), actT cyc3⟩` with H1–H3, self-dual, `≠ Q3`; so the native octahedral repertoire on one
token with H1–H3 does not force `Q3`, by an explicit object rather than by claim (D). **Bridge:** the cone step of
B7-4 and of B3.C for every finite group of unitary conjugations containing `cnot` is supplied by item 6 (given
Theorem S′), so for finite groups claim (D) is no longer load-bearing; the reachability step is HO-23's finite case.
Both: condition (CC) and the H1 test (`1 − 4D ≤ (2/c − 1)²` for a defect with normalised `|det Ψ|² = D`) as exact
design rules for proposing a surgery, and Lemma C13-O as the exact obstruction when an orbit contains an orthogonal
pair and `c < 2`.

## What they may not assume

- that Theorem S′ is kernel-checked: it is a written proof, read by the coordinator and found sound, carried at [W];
- anything CERTIFIED; the cones differ from `Q3` only near small caps (`c − 1 = 1/400` here, `10⁻⁵` for the Clifford
  group);
- T on these cones: it fails (finitely many non-PSD extreme rays, C3.3), so they say nothing about C3.1's open class;
- that `φ₀` seeds an explicit cone (item 5: it does not; its EXOTIC-E status rests on claim (D) [A]).

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-24 v1` and records in its `LOG.md`
whether and how it relies on it.

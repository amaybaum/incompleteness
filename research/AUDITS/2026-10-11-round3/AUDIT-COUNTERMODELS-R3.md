# Coordinator audit — `research/countermodels`, round 3

Thread head `23713ce9` (2026-10-11; round-3 commits `43a49d57` … `23713ce9`). Base L = `9f9f8257`. Audited: the 36
round-3 rows of `RESULTS.md` (C11.1 … C11.7; C12.1 … C12.6; C13.1 … C13.9 with C13.9f; C14.1 … C14.4; C15.1 … C15.3;
C16.1 … C16.6), `NOTES-C11.md` … `NOTES-C16.md`, `experiments/c11_octahedral`, `c12_pairs_bellsets`, `c13_residual`,
`c14_facial`, `c15_clifford`, `c16_kappa_bellcorner`, the receipts in `inbox/`, the handoff proposals HP4, HP5, HP6,
`LOG.md`. No Lean work this round (no CI run to verify).

## Method

1. **Receipts.** HO-10 v1, HO-11 v1 and HO-14 v1 copied verbatim (sha256 `ef909f69…`, `cd6305f6…`, `af4c4b63…`, each
   equal to the overview file at `2a055180`, re-checked by the coordinator) and committed at `43a49d57` with the
   reliance recorded in `LOG.md`: HO-10 only as the label under which the residual region's existence is covered
   (C13.6); HO-11 item 3 as context, the `cyc3` witness recomputed; HO-14 as the object of C11, its order and the
   unreachability of `φ₀` recomputed before any use. The receipts commit was amended before its first push to carry
   the LOG entry (process note recorded). HO-12 was not received: the Clifford group of C15 is taken from its
   definition in the overview only, every property recomputed, and nothing from HO-12 is relied on. Protocol
   satisfied.
2. **Replay.** Six scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 6/6
   (`countermodels/replay3/REPLAY-LOG.txt`).
3. **Independent check.** `countermodels/indep_checkC3.py` (own code; own Gaussian-rational arithmetic for the orbits,
   sympy for the symbolic identities and the square-root comparisons; reads nothing from the thread; decision rule
   fixed before the first run): run 1 **10/10 CONFIRMED**, `INDEP-C3-FIXED`, replay identical.
   - X1 (C11.2): Theorem C11-B's identity `Σ_{P∈{X,Y,Z}} |det Ψ(C_P g)|² = |a|²|b|² + |⟨a|b⟩|²`, symbolically.
   - X2 (C11.1, C15.1; HO-14): as signed permutations of the table coordinates `⟨cnot, actT J⟩` has order 48,
     `⟨cnot, actT J, actT S⟩` order 384 (equal to the group with `nflip` adjoined), `⟨cnot, actC J, actT J⟩` order 11520
     (equal to the full Clifford group with the phases), the stabiliser of `E(3,0)` in it the 384 group, the orbit of
     `E(3,0)` 30 elements.
   - X3 (C11.5): the `G₃₈₄`-orbit of `h* = (10, 2 − 2i, −1 − 3i, 3 − i)` has 192 rays, minimum `|det Ψ|²` normalised
     `85/2048`, pairwise squared overlaps in `[25/2048, 13/16]` over 18336 pairs; at `c* = 401/400` H1 holds on every ray
     and (CC) on every pair; at `c′ = 301/300` (CC) fails on the minimal-overlap pair.
   - X4 (C11.4): the orbit of `φ₀` has 384 rays, minimum `|det Ψ|²` `5/256` (so `λ_max = (8 + √59)/16`), `s_max = 233/256`,
     exactly one orbit ray orthogonal to `φ₀`; at `c = 101/100` the witness `y = P_{φ₀} + λd_k` pairs `≥ 0` with every
     orbit defect, `0` with `d_{φ₀}`, and `h_k†yh_k = −4/22275 < 0`.
   - X5 (C12.1): for `h₁ = e₁`, `h₂ = (3/5, 4/5, 0, 0)` the (CC) threshold is `c ≤ 10/9`; at `c = 5/4` the explicit
     `y = P_v + λd₂` (`v = (12/13, −5/13, 0, 0)`, `λ = 16/507`) lies in `K*` and not in `K` (`x†yx = −3116988/603351125`
     for `x = Π_{v⊥}h₂`); at `c = 11/10` (CC) holds and the inside-cap construction gives a PSD `y`.
   - X6 (C14.2): on the circle surgery `√(9/10) e₁ + √(1/10) e^{iα} e₂` at `c = 1000/961`, 14240 exact aligned contact
     points of `d₀` span exactly **14** real dimensions, each satisfying `⟨Y, d₀⟩ = 0` and `Im Y₁₂ = 0`; 377 exact points
     of the full null quadric (free phases) span **15**.
   - X7 (C16.4, C13.9f): the κ orbit members `(6, 2, x, −x)`, `(6, −2, x, x)` have `|v|² = 42`, `|det Ψ|²` normalised
     `16/441`, within-circle `|⟨v|v′⟩| ≥ 38`, cross `32` (`s_min = 256/441`); H1 holds at `103/100` and fails at `26/25`;
     (CC) holds at `103/100` and the cross pair violates it at `5/4`; `d` has eigenvalue `−3/100`; the S2-group image
     `(R_z(π) ⊗ R_x(π))(I ⊗ Z)h = (2, −6, 1, 1)` is orthogonal to `h`.
   - X8 (C15.2): the Clifford orbit of `h_C = (−480 + 7i, 357 + 870i, 939 + 834i, 448 + 486i)` has 11520 rays;
     `s_min = 164178929/3916193820250` against `h_C`; minimum `|det Ψ|²` normalised `198406621629/9790484550625 ≈ 0.0203`;
     at `c = 100001/100000` H1 and (CC) hold; the orbit of `4φ₀` has 5760 rays and contains a ray orthogonal to `4φ₀`.
   - X9 (C13.5): the basis `b₁ = (2,3)⊗(2, −1+2i)`, `b₂ = CNOT b₁`, `b₃ = |0⟩⊗(1+2i, 2)`, `b₄ = (10, −5+10i, −6−12i, −6−12i)`
     is orthogonal with norms `117, 117, 9, 585`; `b₁, b₃` products, `b₂, b₄` entangled; `p = 85/98`;
     `(A², B²) = (9/52, 0), (4/117, 20/117), (5/117, 20/117)`; the three circles are product-free; H1 holds on all three
     at `251/250` and fails on the circle through `b₂` at `101/100`; `s_min = (36/49)²` and (CC) holds at `251/250`.
   - X10 (C16.1 instances): CNOT carries both computational Bell circles to products (symbolic `w`).
4. **Written proofs read.** **Theorem S′** (the load-bearing [W] of every explicit cone of this round — C11.5, C13.5,
   C13.7, C15.2, C16.4): step (1) closedness from `Q ∩ (−cone Z) = {0}` (positive traces); (2) `K ⊆ K*` from the three
   kinds of pairings; (3) `K* = (Q + cone Z) ∩ Z*` through `(A ∩ B)* = cl(A* + B*)` and the closed sum; (4) the
   minimal-weight decomposition on the compact set `F`, with the two cases — `t*_j > 0`, where `d_j` is positive
   definite on `ker q ⊆ u^⊥` by Bessel and `c_j ≤ 2`; `t*_j = 0`, where `⟨y, d_j⟩ ≥ 0` forces a listed `d_k` with positive
   weight and positive pairing, and (CC) `U_j ⊆ W_k` makes `d_k` positive definite on `ker q` — each contradicting
   minimality; the compact extension (finite combinations; an unlisted defect falls under the same two cases) and the
   extremality for a common `c`: **sound**. Lemma C13-O (the three pairings `c(1 − s_{hl}) + λc²s_{h′l} ≥ 0`, `0`,
   `λ(1 − c) < 0`; the decomposition forced to `t = 0`): sound. Theorem C12-P's converse (the geodesic point in the cap
   with `b < 1 − 1/c₂`; `Π_{v⊥}h₂`): sound; the Bell-corner remark matches C4.1. Lemma BW and Tools A–C (the
   perturbation `v_ε`; Tool A's `f′` construction; Tool B's `ab/(1 − a)`; Tool C's parallelogram and Bessel bound,
   strict because `g_k ∉ span(g_i, g_m)`): read, sound; Theorem C12-5 uses the [L] separation-dimension fact as stated.
   C13-M (the two product lines of `span(b₃, b₄)` not orthogonal; instance X9): sound. C13-Π (a fixed-point-free
   subgroup of `S₄` contains a double transposition; the Cauchy–Schwarz bound in case (ii)): sound. C14-1 (the gradient
   of `θ ↦ ⟨y, U_θzU_θ†⟩` at its minimum; `z` and the `k` traceless tangents independent): sound. Lemma C16-1 (the
   distinct frequencies of the trigonometric polynomial; the product of extreme coefficients) and Corollary C16-2 (the
   count of product eigenlines): sound. C11-E's genericity (two proper real-algebraic exceptional sets): sound.
5. **Kernel citations.** The coordinator's sweep (lines added since `e6d42cab`) finds 4 distinct `File.lean:NNN`
   strings; **4/4 resolve at L** (`cite_check_r3_countermodels.out`): JordanClassification.lean:84
   `psd_iff_trace_nonneg` (the self-duality of the PSD cone, as cited), CompositeDimension.lean:741 `sgn` (the gate's
   definition), OIRealization.lean:360 `finiteOI_not_implies_inert` and SpectatorBridge.lean:223
   `InertSpectatorCompositionality` (in the HO-11 copy).

## Findings by row

| row | thread label | audit |
|---|---|---|
| C11.1 | CONDITIONAL (`pauliW` [D] for the lift) | accepted; X2 (order 384; the Clifford group 11520; the stabiliser) |
| C11.2 | CONDITIONAL (C11-B [W]) | accepted; X1 (the identity, symbolic) |
| C11.3 | CONDITIONAL (Theorem S′ [W]; JordanClassification.lean:84 [K]; SD1's block lemma [A]) | accepted; **Theorem S′ read by the coordinator: sound** (method 4); the kernel line verified; HP4's "not yet audited" is answered by this reading, the label [W] unchanged |
| C11.4 | CONDITIONAL ([W] + [A]) | accepted; X4 (the orbit, the single orthogonal ray, the witness at `101/100`) |
| C11.5 | CONDITIONAL (S′ [W]; the operator-norm bound [W]; `pauliW` [D]) | accepted; X3 (192 rays, `85/2048`, `[25/2048, 13/16]`, H1 and (CC) at `401/400`, the pair-level sharpness at `301/300`) |
| C11.6 | CONDITIONAL (S′ [W]; genericity [W]) | accepted; proof read |
| C11.7 | CONDITIONAL (C3.3) | accepted |
| C12.1 | CONDITIONAL (S′ [W] for ⇐; the witness [W] for ⇒) | accepted; X5 on a coordinator-chosen instance; the converse read |
| C12.2 | CONDITIONAL ([W]; C8-L) | accepted; BW and Tools A–C read |
| C12.3 | CONDITIONAL (C12.2; C8 (b)) | accepted; the ten-pattern case analysis read (replayed, not re-derived) |
| C12.4 | CONDITIONAL (C12.2; [L]) | accepted; the dimension argument read |
| C12.5 | OPEN | accepted |
| C12.6 | CONJECTURE (residual classes); CONDITIONAL where C12.3–C12.4 apply | accepted (the thread's own record of the two-part label) |
| C13.1 | CONDITIONAL (S′ [W]; C13-S [W]) | accepted; the compact extension and extremality read |
| C13.2 | CONDITIONAL ([W]) | accepted; Lemma C13-O read; its scope `c ∈ (1, 2)` as the thread's C16 records |
| C13.3 | CONDITIONAL (C13-M [W]; [A]) | accepted; X9 (the basis, the products and entangled members) |
| C13.4 | CONDITIONAL (C13-Π [W]; C13.1–C13.2) | accepted; C13-Π read; the `c = 2` corner by C16.2 |
| C13.5 | CONDITIONAL (S′ for compact `Z` [W]; orbit and minimum formulas [W]) | accepted; X9 (`p`, the `(A², B²)` values, product-freeness, the H1 window `251/250` / `101/100`, `s_min`) |
| C13.6 | CONDITIONAL (C13.2, C13.4); existence on claim (D) [A] | accepted; the `c = 2` corner by C16.2 |
| C13.7 | CONDITIONAL (S′ [W]; C13.2) | accepted; the S2 circle cone's facial value exact in X6 |
| C13.8 | CONDITIONAL ([W]; C3.2) | accepted; superseded in precision by C14.1–C14.2 |
| C13.9 | OPEN | accepted; its parenthetical corrected by C16.3 and the FAILED row C13.9f |
| C13.9f | FAILED (refuted exactly) | accepted; X7 (`(6, 2, 1, −1)` has no orthogonal pair in κ's orbit and an orthogonal partner under the S2 group) |
| C14.1 | CONDITIONAL ([W]) | accepted; the tangency bound read |
| C14.2 | CONDITIONAL (C14.1; the span count [W]) | accepted; X6 reproduces the ranks 14 and 15 on the coordinator's own point sets |
| C14.3 | CONDITIONAL (C14.2; C3.2; [A] Y6) | accepted |
| C14.4 | OPEN | accepted |
| C15.1 | CONDITIONAL (`pauliW` [D]) | accepted; X2 (11520) |
| C15.2 | CONDITIONAL (S′ [W]) | accepted; X8 (11520 rays, `s_min` to the exact value, the entanglement bound, H1 and (CC) at `100001/100000`, the `4φ₀` countercontrol) |
| C15.3 | CONDITIONAL (C13.2, C13.4) | accepted; the `c = 2` corner by C16.2 |
| C16.1 | CONDITIONAL ([W]; C7.6) | accepted; Lemma C16-1 read; X10 |
| C16.2 | CONDITIONAL (C13.2; C16.1; C7.6; [A] Z) | accepted; the scope correction of four rows by an appended row, labels unchanged, as §A.30 asks |
| C16.3 | CONDITIONAL | accepted |
| C16.4 | CONDITIONAL (S′ for compact `Z` [W]) | accepted; X7 |
| C16.5 | CONDITIONAL (C14.2; C3.2; [A] Y6) | accepted |
| C16.6 | OPEN | accepted |

No label changes. The round's closing review (C16) found two scope defects in its own rows and recorded them by
appended rows (C16.2; the FAILED row C13.9f) rather than edits — the method the protocol asks for. The thread's
recorded deviations (two version checks without `-I -B`; the amended receipts commit before its first push; two extra
nodes; pre-run edits logged in every NOTES "Runs" section; the cosmetic Fraction-pair print in `c13_residual.out`; a
numerical penalty-optimizer test found insensitive and not used; the decimal gloss of `s_min` in C15.2) are each in the
LOG and change nothing audited here.

## Handoff items

- HP4 (the explicit cone for HO-14's group; Theorem S′; EXOTIC-X for every finite unitary group with `cnot`; `φ₀` is
  not a seed) → **HO-24** to the equivalence and bridge threads, answering HO-14's request; S′ carried as [W], read by
  the coordinator.
- HP5 (the two halves of A_miss from the cone side; B3.C's residual region; Lemma C13-O; the Bell corner) → **HO-25**
  to the bridge and equivalence threads.
- HP6 (the sharp pair theorem; C8-C at four members; T on the continuum cones; κ with G16 EXOTIC-X; the two
  assumption-watch markers in C16's refined form) → **HO-26** to the equivalence thread; the classification and the
  markers recorded in the overview.

# HO-25 (v1) — countermodels → bridge, equivalence: the two halves of A_miss from the cone side; B3.C's residual region; Lemma C13-O and its Bell corner; explicit cones with a continuum of non-PSD extreme rays

**From** `research/countermodels` (round 3, nodes C13, C15, C16). **To** `research/bridge` (B3.C, HO-10/HO-16; the
split of A_miss, B9-3 and HO-12 item 4) and `research/equivalence` (the K2 schema's halves). Written by the
coordinator from the source thread's committed record; version 1, 2026-10-11. The thread did not receive HO-12: the
two groups below were taken from their definitions in the overview only and every property recomputed.

## Statements and labels

1. **The finite half alone leaves an explicit exotic cone** (C15.1, C15.2). `⟨cnot, actC cyc3, actT cyc3⟩` has order
   11520 (recomputed; the two-qubit Clifford group, HO-12 item 3); for
   `h_C = (−480 + 7i, 357 + 870i, 939 + 834i, 448 + 486i)` (orbit of 11520 entangled rays, minimal squared overlap
   `s_min = 164178929/3916193820250`, minimum normalised `|det Ψ|²` `198406621629/9790484550625`, no orthogonal pair) and
   `c = 100001/100000`, `K(G·(I − cP_{h_C}))` is an explicit invariant self-dual cone with H1–H3, `≠ Q3`. The statement
   "SPEC_P(J) alone leaves exotic cones" then needs Theorem S′ [W] (HO-24 item 3) instead of claim (D) [A]. The orbit of
   `4φ₀` (5760 rays) contains a ray orthogonal to `4φ₀`, so `φ₀` seeds nothing here either. Label: CONDITIONAL
   (Theorem S′ [W]; `pauliW` [D] for the lift).
2. **The continuous half: the rank-one route is closed** (C13.3, C13.4). The group of (b) for the phase flow and the NOT
   on each token, with `cnot`, is `T³ ⋊ D₄` on the computational basis (`D₄` = translations of `𝔽₂²` and `cnot`'s
   transvection); the translation `X⊗I` permutes the eigenlines as a double transposition, so every orbit of states
   contains an orthogonal pair and no rank-one orbit surgery with a common `c < 2` is self-dual (item 3); at `c = 2` no
   orbit is admissible for H1 (`cnot` carries both computational Bell circles to products). Exotic cones there: by
   claim (D) only. Label: CONDITIONAL ([W] + [X]).
3. **Lemma C13-O, the orthogonal-pair obstruction** (C13.2). For any set `Z` of defects `I − cP_h` with one
   `c ∈ (1, 2)` containing `h ⊥ h′`, `y = P_h + ((c − 1)/(4 − 2c))d_{h′}` lies in `K(Z)* \ K(Z)` (the three pairings
   `c(1 − s_{hl}) + λc²s_{h′l} ≥ 0`, `0`, `λ(1 − c) < 0`; the decomposition forced to `t = 0`). Scope: `c ∈ (1, 2)`,
   as C16 records. Label: CONDITIONAL ([W]; exact instances).
4. **B3.C's residual region (C10.3) from the cone side** (C13.5, C13.6, C15.3, C16.2). (a) For
   `G = closure⟨H₀, cnot⟩` (`H₀` a simple-spectrum torus normalized by `cnot`) the residual region is empty: a `cnot`
   swap of a product and an entangled eigenline forces an entangled `cnot`-fixed eigenline (the two product lines of
   the complementary plane in `E₊` are not orthogonal, C13-M), and C10.2's single-defect cone is explicit. (b) With the
   maximal torus `T³` and eigenline group `Π`: if `Π` fixes an eigenline (necessarily a product), states dominated by it
   have orbits without orthogonal pairs and Theorem S′ (compact form) gives an explicit cone — exhibited for `Π = S₃`
   (`G_A`; orthogonal basis `b₁ = (2,3)⊗(2, −1+2i)`, `b₂ = CNOT b₁`, `b₃ = |0⟩⊗(1+2i, 2)`, `b₄ = (10, −5+10i, −6−12i,
   −6−12i)`; `h = (9 + 2i)b₃ + b₁`, `p = 85/98`, `c = 251/250`): a `G_A`-invariant self-dual cone with H1–H3 whose non-PSD
   extreme rays form three product-free circles; otherwise `Π` contains a double transposition (C13-Π: a fixed-point-free
   subgroup of `S₄` contains one) and the rank-one route is closed — for `c < 2` by Lemma C13-O (exact witness for
   `Π = ⟨(12), (34)⟩`); at `c = 2` an orbit admissible for H1 in the residual region is a single phase circle of two
   product eigenlines, whose surgery is unitarily equivalent to C7.6's and not self-dual (Corollary C16-2; for
   `Π = ⟨(12), (34)⟩` no orbit is admissible). Label: CONDITIONAL ([W] + [X]; S′ [W]; C7.6); existence in the closed
   case stays at HO-10's label (CONJECTURE + claim (D)).
5. **Stage 4's torus node S2 at level (i)** (C13.7; C16.2 for the `c = 2` corner): `actC R_z ∘ actT R_x` with `cnot`,
   without G16 — the circle surgery on `{3|0+⟩ + w|1−⟩}` at `c = 21/20` is an explicit exotic invariant cone (the
   explicit torus cone of C5.3/C5.4, at level (i)); with G16 the double transposition `Ad(I⊗Z)` closes the rank-one
   route (for `c < 2` by orthogonal pairs; at `c = 2` the only admissible orbit is `C1 ∪ C2`, whose surgery `K_T` is not
   self-dual, [A] Z). The κ node with G16 is different (HO-26 item 4). Label: CONDITIONAL (S′ [W]; [X]; [A] Z).
6. **T on these cones fails** (C14.2, C14.3): on circle surgeries every defect has facial invariant exactly 14
   (`15 − k` for a `k`-dimensional torus orbit; exact rank on the S2 cone — 14240 aligned contact points span 14 real
   dimensions, the full null quadric 15), against `c(P00) = 9`. Label: CONDITIONAL ([W] + [X]; [A] Y6).

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `23713ce9` (round-3 commits `43a49d57` … `23713ce9`) |
| proposal | `research/countermodels/handoff-proposals/HP5-composite-action-halves-B3C-residual.md`, sha256 `38290338200816ed9014fe73b1ed842291d1a27da793583637ce0c66e6cd49b1` |
| results, notes | `research/countermodels/RESULTS.md` sha256 `00ebcfe1e87dce26f16e313091bc23fdb0a2265c324dcb9b0902c83e0a14489f` (rows C13.1 … C13.9, C13.9f, C14.1 … C14.3, C15.1 … C15.3, C16.1 … C16.3); `NOTES-C13.md` `19dcb7df749e5e749498d401d46e9c4169ffaa0fe1ee1044f6e89c156be76410`; `NOTES-C14.md` `b23b55dbc0cff70ff866e64e192094940b944baeffed3ee1b50d071c4ef3a037`; `NOTES-C15.md` `9ca593607e764603cc81cec93324f3bc12f93c51cdd264d1b5d46cd516ff6d61`; `NOTES-C16.md` `2ba7a281c6b7ef9feef863fc25f4854e54ae85c6fea030b97944d2444800c5a9` |
| scripts, outputs | `experiments/c13_residual.py` `707b021914cd1b8e0faa0ccbea6fc7d75bf61a390506a421f461c76ec8253926` / `.out` `cabe7692746e71b751bbed82d404b7005669aa3b154fb61376e3288b92d1a159` (9/9, VERDICT C13-RESIDUAL-EXACT); `c14_facial.py` `81324629a6f2f244ae5679014c664e2f25f20071615027db83eaf9fddccac800` / `.out` `e1a268983964aec2cc79a057ba14bab2d6c49da676df92c6fccc48fcc5f9d039` (8/8, VERDICT C14-FACIAL-EXACT); `c15_clifford.py` `e9018867ac51e907d149c1e69a90df1fe4d288cc8aa6e15f30b9a47f2e06c9ee` / `.out` `6cd53515831c00eeaa3aea29402667e59fcec448776452e6c1a17ea7b550f4b7` (6/6, VERDICT C15-CLIFFORD-EXACT); `c16_kappa_bellcorner.py` `fea92cecc47ad1c2499d18e30fdb1be2260eb8cc93da2a728c0407ccd9a30e93` / `.out` `6d0a5dfe4e091e131cfefd51fdded7c9246645925c62bf1079549e7666289e6d` (15/15, VERDICT C16-KAPPA-BELLCORNER-EXACT); all replayed byte-identically |
| design module | none |
| coordinator audit | `indep_checkC3.py` run 1 10/10 — X2 (order 11520), X8 (the Clifford orbit of `h_C`: 11520 rays, `s_min` to the exact value, the entanglement bound, H1 and (CC) at `100001/100000`, the `4φ₀` countercontrol), X9 (the basis `b₁ … b₄` orthogonal with norms 117, 117, 9, 585; `b₁, b₃` products, `b₂, b₄` entangled; `p = 85/98`; the `(A², B²)` values; the three circles product-free; H1 at `251/250` holding and failing on the circle through `b₂` at `101/100`; `s_min = (36/49)²` and (CC) at `251/250`), X6 (the facial ranks 14 and 15 on the coordinator's own point sets), X10 (CNOT carries both computational Bell circles to products, symbolic); Lemma C13-O, C13-M, C13-Π, C14-1, Lemma C16-1 and Corollary C16-2 read: sound — `research/AUDITS/2026-10-11-round3/AUDIT-COUNTERMODELS-R3.md` |

## What the receiving threads may assume

Items 1–6 at their labels. **Bridge:** for the Clifford half of A_miss (HO-12 item 4's finite half) "SPEC_P(J) alone
leaves exotic cones" rests on an explicit cone through Theorem S′ [W], no longer on claim (D); for the continuous half
(`T³ ⋊ D₄`) the rank-one surgery route is closed and existence there is by claim (D) only; B3.C's residual region is
empty for `closure⟨H₀, cnot⟩`, explicit for `Π = S₃`, and obstructed on the rank-one route for `Π` with a double
transposition. **Equivalence:** the two halves of the K2 schema's A_miss each leave exotic cones on the cone side (the
finite half explicitly); the schema's "together they force `Q3`" is not re-examined here and stays at HO-13's and
HO-18's labels.

## What they may not assume

- that Theorem S′, Lemma C13-O, Lemma C16-1 or Corollary C16-2 is kernel-checked (S′ and C13-O were read by the
  coordinator and found sound; still [W]); that any statement here is CERTIFIED;
- anything about HO-12's records beyond the two groups' definitions;
- explicit cones for `Π` with a double transposition, for the S2 node with G16, or for `K_circ` (all OPEN);
- that the continuous half's exotic cones exist other than through claim (D) [A].

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-25 v1` and records in its `LOG.md`
whether and how it relies on it.

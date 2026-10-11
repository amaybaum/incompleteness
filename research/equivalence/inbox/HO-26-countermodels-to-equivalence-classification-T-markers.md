# HO-26 (v1) — countermodels → equivalence: the sharp non-Bell pair theorem; Conjecture C8-C at four members; T on the explicit continuum cones; κ with G16 EXOTIC-X; two assumption-watch markers in their refined form

**From** `research/countermodels` (round 3, nodes C12, C14, C16). **To** `research/equivalence` (the T / K∞-Trans
markers of HO-7 and HO-15; the classification of exotic cones that the K2 schema's hypotheses must exclude). Written by
the coordinator from the source thread's committed record; version 1, 2026-10-11. The classification and the markers
are also recorded in `research/OVERVIEW.md`.

## Statements and labels

1. **Non-Bell pair theorem, sharp** (C12.1). For `d_i = I − c_iP_{h_i}`, `c_i ∈ (1, 2]`: `K({d₁, d₂})` is self-dual iff
   the two are orthogonal Bell-type defects or `c₁c₂|⟨h₁|h₂⟩|² ≥ (√(c₁ − 1) + √(c₂ − 1))²`; otherwise an explicit
   `y ∈ K* \ K` (the geodesic point in the cap with `b < 1 − 1/c₂`; `Π_{v⊥}h₂`). The Bell pair theorem C4.1 is its
   corner `c = 2` (threshold `s ≥ 1`). Label: CONDITIONAL (Theorem S′ [W] for ⇐; the witness [W] for ⇒; 18 exact
   cases).
2. **Conjecture C8-C at four members** (C12.3, C12.4, C12.6): no four distinct Bell-type defects with a non-orthogonal
   pair have a self-dual surgery (all ten orthogonality patterns, exact witnesses), and the same for every finite Bell
   set with a complete non-orthogonality component — in particular every finite Bell set without orthogonal pairs, of any
   size. C8-C stays a CONJECTURE for the residual classes (five or more members, every component with an orthogonal pair
   and no tool vertex; closed infinite sets other than C7.6's circle). Label: CONDITIONAL ([W]: Lemma BW and Tools A–C;
   dimension theory [L]; C8 (b) [W, audited]) where it is proved; CONJECTURE for the residual classes.
3. **T** (C14.2, C14.3, C14.4, C16.5). On every explicit exotic cone so far the defects carry `c = 15 − k` (`k` the
   dimension of their orbit under the cone's torus): 15 on finite surgeries (C3.3), 14 on the continuum cones (exact on
   the S2 circle cone), against `c(P00) = 9`: T fails on all of them, including cones with a continuum of non-PSD
   extreme rays. For every `K_circ` the off-`Fix` defects have `c ≤ 14`; T on `K_circ` is OPEN, reduced to the absence
   of smooth contact between its pure members and its non-PSD members (the tangency bound C14-1: the gradient of
   `θ ↦ ⟨y, U_θzU_θ†⟩` at its minimum; `z` and the `k` traceless tangents independent). Label: CONDITIONAL ([W] + [X];
   [A] Y6) / OPEN for `K_circ`.
4. **κ with G16 (the stage-5/6 node, level (ii)) has an explicit exotic cone** (C16.4). Under
   `G_κ = closure⟨U(x), cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩` the orbit of `h = 2|0+⟩ + |0−⟩ + ½|1−⟩ ∝ (6, 2, 1, −1)` is the two
   circles `{(6, 2, x, −x)}`, `{(6, −2, x, x)}` (`|x| = 1`; `|v|² = 42`), with squared overlaps `≥ 256/441` (within a
   circle `|⟨v|v′⟩| ≥ 38`, across `32`) and normalised `|det Ψ|² = 16/441` throughout; at `c = 103/100` H1 and (CC) hold
   (H1 fails at `26/25`, the cross pair violates (CC) at `5/4`), so `K(G_κ·(I − cP_h))` is a `G_κ`-invariant self-dual
   cone with H1–H3, `≠ Q3`, whose non-PSD extreme rays are two circles. This upgrades the κ node from EXOTIC-E (EBF
   over the Bell seeds) to EXOTIC-X given Theorem S′, by a surgery; T fails on it (`c = 14` by C14-2). The S2-group
   image `(R_z(π) ⊗ R_x(π))(I ⊗ Z)h = (2, −6, 1, 1)` is orthogonal to `h`, which is why the S2 node with G16 is different
   (C13.9f, FAILED: `(6, 2, 1, −1)` does not seed the S2 node). Label: CONDITIONAL (Theorem S′ for compact defect sets
   [W]; C14-2 [W] and [A] Y6 for T).
5. **Bell corner of the rank-one obstruction** (C16.1, C16.2). At `c = 2` an orbit under a maximal torus that stays
   maximally entangled is a Bell eigenline or a phase circle of two product eigenlines (Lemma C16-1: the distinct
   frequencies of the trigonometric polynomial; the product of extreme coefficients); in B3.C's residual region it is
   one circle, not self-dual (C7.6). With the S2 and κ nodes' `C1 ∪ C2` (`K_T`, [A] Z), every "no rank-one orbit surgery
   is self-dual" statement of the round holds for every `c ∈ (1, 2]`. Label: CONDITIONAL ([W]; C7.6; [A] Z).

## Assumption-watch markers (refined form, from C16)

- **"Explicit exotic cones need Bell-type (`c = 2`) defects or finitely many defects"** — false. Small-cap rank-one
  defects with nested cap/co-cap geometry give explicit self-dual surgeries for finite groups without Bell-type defects
  (`G₃₈₄`, the Clifford family) and continua of defects for tori whose orbits avoid orthogonal pairs (a maximal torus
  whose eigenline group fixes an eigenline; κ's torus, which fixes two coordinates). For defects with `c < 2` the
  operative obstruction is an **orthogonal pair inside an orbit**: a double transposition of eigenlines forces one only
  together with a torus that moves the relative phases of both swapped pairs (a maximal torus, or the S2 torus), and an
  antiunitary `h ↦ Uh̄` forces one when `U` is antisymmetric. At `c = 2` orthogonal pairs are harmless (Theorem S) and
  the obstruction is a non-orthogonal pair (C4.1, C7.6, `K_T`). Affects the readings of stage 4's and stage 5's
  EXOTIC-E rows (finite groups, the torus node, the κ node) and of C5.3, C5.4, C7.7.
- **"Every exotic cone with a continuum of non-PSD extreme rays is EBF-only, so T is undecidable on that class by
  construction"** — false for the class as a whole: T is decided (fails) on the explicit continuum cones; the undecided
  part is the cones with no smooth contact (no explicit member known).

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `23713ce9` (round-3 commits `43a49d57` … `23713ce9`) |
| proposal | `research/countermodels/handoff-proposals/HP6-classification-T-markers.md`, sha256 `52a0d26e7ea697bdded722dcba9d48af004aa93b266755b772431d79067709fb` |
| results, notes | `research/countermodels/RESULTS.md` sha256 `00ebcfe1e87dce26f16e313091bc23fdb0a2265c324dcb9b0902c83e0a14489f` (rows C12.1 … C12.6, C14.1 … C14.4, C16.1 … C16.6, C13.9f); `NOTES-C12.md` `29012ca2ba97c5d76b457dcdc7acb37d29f09391c30c4d8da07a4cc4c4c89706`; `NOTES-C14.md` `b23b55dbc0cff70ff866e64e192094940b944baeffed3ee1b50d071c4ef3a037`; `NOTES-C16.md` `2ba7a281c6b7ef9feef863fc25f4854e54ae85c6fea030b97944d2444800c5a9` |
| scripts, outputs | `experiments/c12_pairs_bellsets.py` `4f2bcbb48462f96b3a7b220a9acb850c4fd191f35b6af81cca6db92a6bb0b3b8` / `.out` `363c9899301d1e1f128b3178c9838b91e2482155097fc5769dae53751c175db0` (9/9, VERDICT C12-PAIRS-BELLSETS-EXACT); `c14_facial.py` `81324629a6f2f244ae5679014c664e2f25f20071615027db83eaf9fddccac800` / `.out` `e1a268983964aec2cc79a057ba14bab2d6c49da676df92c6fccc48fcc5f9d039` (8/8); `c16_kappa_bellcorner.py` `fea92cecc47ad1c2499d18e30fdb1be2260eb8cc93da2a728c0407ccd9a30e93` / `.out` `6d0a5dfe4e091e131cfefd51fdded7c9246645925c62bf1079549e7666289e6d` (15/15); all replayed byte-identically |
| design module | none |
| coordinator audit | `indep_checkC3.py` run 1 10/10 — X5 (the pair theorem on a coordinator-chosen instance: `h₁ = e₁`, `h₂ = (3/5, 4/5, 0, 0)`, threshold `c ≤ 10/9`; at `c = 5/4` the explicit `y = P_v + λd₂` in `K* \ K` with `x†yx = −3116988/603351125`; at `c = 11/10` (CC) and a PSD `y`), X6 (the facial ranks 14 and 15), X7 (the κ orbit: `|v|² = 42`, `16/441`, within-circle `≥ 38`, cross `32`, `s_min = 256/441`; H1 at `103/100` and not at `26/25`; (CC) at `103/100` and the cross pair's violation at `5/4`; `d`'s eigenvalue `−3/100`; the S2-group image orthogonal to `h`), X10; Theorem C12-P's converse, Lemma BW and Tools A–C, C14-1, Lemma C16-1 and Corollary C16-2 read: sound; the ten-pattern case analysis of C12.3 replayed, not re-derived — `research/AUDITS/2026-10-11-round3/AUDIT-COUNTERMODELS-R3.md` |

## What the receiving thread may assume

Items 1–5 at their labels and the two markers. The pair theorem (item 1) as the exact two-defect criterion; C8-C's
proved classes (item 2) as closed; T as decided (failing) on every explicit cone of the record, with `K_circ` the one
open class (item 3); κ with G16 as EXOTIC-X given Theorem S′ (item 4). For the K2 schema and S4: no explicit cone of the
record satisfies T, so T remains a candidate separator only against cones with no smooth contact, of which no explicit
member is known; and HO-15's self-duality marker is sharpened by HO-19 (self-duality of the state cone is not a source
of K∞-Trans; its invariant form is).

## What it may not assume

- anything CERTIFIED; that Theorem S′, Lemma C13-O, Lemma C16-1, the boundary-witness tools or the tangency bound are
  kernel-checked (S′, C13-O, BW, Tools A–C, C14-1, C16-1 and C16-2 were read by the coordinator and found sound; still
  [W]);
- T for `K_circ`; explicit cones for the S2 node with G16, for B3.C's case B (`Π` with a double transposition) or for
  `K_circ`; any EBF-only cone;
- C8-C for the residual classes (item 2).

## Receipt

The receiving thread copies this file into its `inbox/` with a commit naming `HO-26 v1` and records in its `LOG.md`
whether and how it relies on it.

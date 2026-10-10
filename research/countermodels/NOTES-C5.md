# NOTES-C5 — explicit κ-invariant cones, and what survives at the torus

Node C5 of `README.md`. κ: the gate flow `U(x) = I + (x − 1)|1−⟩⟨1−|`, `|x| = 1`, `U(−1) = CNOT` (stage 5 C5 KAPPA); the
stage-5/6 κ node is "κ with G16" (level (ii); R6 Table A3-seeds row A4b). Circles `C1(w) = (|0+⟩ + w|1−⟩)/√2`,
`C2(w) = (|0−⟩ + w|1+⟩)/√2`. Torus node S2: `actC Rz(θ) ∘ actT Rx(φ)` (stage 4). Script:
`experiments/c5_kappa_torus.py` (run 1: 8/8, `VERDICT C5-KAPPA-TORUS-EXACT`; replay identical).

## Verdicts

| node | verdict | evidence |
|---|---|---|
| κ with `cnot` only (level (i)) | **EXOTIC-X: explicit cones** `K({z_{C2(w′)}})` and `K({z_{C2(w′)}, z_{C2(−w′)}})`, every `w′` | [X K1] + [W] W1 |
| κ with G16 (level (ii), the stage-5/6 node) | **no exotic cone with finitely many non-PSD extreme rays**, in particular no defect-surgery cone with finite `Z`, is κ-invariant; EXOTIC-E stands ([A] C5); explicit cone OPEN | [X K2] + [W] W2 |
| torus S2 (with or without G16) | the same no-go for finitely many non-PSD extreme rays; `K_T` refuted ([A] Z); EXOTIC-E stands; explicit cone OPEN | [X K3] + [W] W2 |

## W1 — the explicit κ-invariant cones (level (i))
`U(x)` is unitary, `U(−1) = CNOT`, and `U(x)C2(w′) = C2(w′)` for all `x, w′` (C2 ⊥ |1−⟩) [X K1, symbolic]. So `Ad U(x)`
preserves `Q3` and fixes each defect `z_{C2(±w′)}`, hence preserves `K(Z)` for `Z ⊆ {z_{C2(w′)}, z_{C2(−w′)}}`; `cnot` is the
member `x = −1`. These are the members with `A₁ = ∅` of NOTES-C4's level-(i) family: H1, the certificates, orthogonality and
self-duality hold (C4.2); `K ≠ Q3`. They are level (i) only: `Ad(I⊗Z) z_{C2(w′)} = z_{C1(w′)}`, and `T_{C1(w′)} ∈ K` pairs
`−1/2` with it. Record: `Ad U(−i)` moves `K_F2` and `K(Z_F)` (pairing `−1/2`; their `C1` defects are not κ-fixed), as stage 5
found for `K(Z_F)`.

## W2 — the no-go at level (ii) and at the torus
- `Ad(I⊗Z) U(x) Ad(I⊗Z) = U′(x) = I + (x − 1)|1+⟩⟨1+|` [X K2], so the closure of `⟨U(x), G16⟩` contains the 2-torus
  `T_κ = {U(x)U′(x′)}`. A κ-and-G16-invariant `K` is `T_κ`-invariant; `T_κ` (connected) acts on any finite invariant set of
  non-PSD extreme rays trivially (unitary conjugations map non-PSD extreme rays to non-PSD extreme rays and keep the
  `E00` entry), so each would be a `T_κ`-fixed table in `maxCone`.
- The `T_κ`-fixed tables are exactly `pauliW = A ⊕ a ⊕ b` on `(|0⟩⊗ℂ²) ⊕ |1−⟩ ⊕ |1+⟩` (dimension 6) [X K2]; every vector of
  these blocks is a product vector, so block positivity gives `A ⪰ 0`, `a, b ≥ 0`: a fixed table in `maxCone` is PSD.
  Contradiction. Hence every exotic κ-and-G16-invariant cone has infinitely many (a continuum of) non-PSD extreme rays;
  no finite defect surgery serves this node.
- Torus S2: at a generic point the fixed tables are those diagonal in the product basis `(|0+⟩, |1−⟩, |0−⟩, |1+⟩)` [X K3]
  (stage 4 Z found the same span `{E00, E30, E01, E31}`), and the same argument applies, at level (i) and (ii).
- Countercontrols: a `T_κ`-fixed non-PSD table pairs `−4` with the product `|1−⟩` (the PSD conclusion uses `maxCone`)
  [X CC1]; at the non-generic torus point `θ = φ = π` the fixed space has dimension 8 [X CC3].

## What survives for the torus (and for κ at level (ii))
EXOTIC-E (stage 4 Z, stage 5 C5: EBF over the Bell seeds on `C1 ∪ C2`); the full-circle Bell surgery `K_T` is refuted
([A] Z, exact pair `−24/625`), and by NOTES-C4 W1 every pair of non-orthogonal Bell defects obstructs a two-defect surgery;
finite surgeries are excluded (W2). Any explicit cone must carry a continuum of non-PSD extreme rays, and by NOTES-C3 it
lies in the class where T is undecided. Non-surgery constructions remain the open route.

## Gem classification (§A.31)
- NEW: an explicit κ-invariant exotic cone exists once G16 is not imposed (stage 5 left the κ cone UNRESOLVED; its node is
  level (ii), where the no-go W2 now explains why a finite surgery cannot serve).
- ELABORATING: the torus no-go extends to every exotic cone with finitely many non-PSD extreme rays, and to κ at level (ii).

# Coordinator's pre-audit record for thread Z (stage 4, countermodels), written 2026-10-10 15:52Z, before reading Z's results

Purpose: fix, before Z reports, what the coordinator has established exactly about the nodes Z is to decide, so that
the audit compares Z's claims against checks made without its code or conclusions. Script `preaudit_z.py`
(`bc5739f3…`), run 3: 9/9 CONFIRMED, `PREAUDIT-Z-FIXED`; replay byte-identical (stdout and stderr). Run 1 (kept as
`.run1.*`, 3/5 before a crash) failed on three errors of my own: a wrong hand formula for the torus pairing (P3a), a
wrong choice of "other defect" in P3c (the generic torus image of `z_(1,1)` is orthogonal to `z_(−1,1)` and
`z_(1,−1)` for every angle; the non-orthogonality is within the orbit), and a PSD check on a trigonometric matrix
sympy could not decide (P4; run 2 uses rational unitaries with cosines 3/5, 4/5). Run 2 (kept as `.run2.*`, 8/9)
failed only on an asserted pairing value in P5c (hand slip: `ipW(E0, SWAP E0)` is 2, not 1; the decisive empty
λ-interval was as asserted). Only the asserted value changed between runs 2 and 3. Z had not finished at the time of
writing (its `pt/Z/` holds z1–z5 outputs and NOTES up to N11; nothing inside was read).

## Facts fixed [X], with the written argument [W] they support
- **P1 (S1).** `SWAP` acts on tables as the transpose and permutes the Bell-type defects, `z_s ↦ z_(−s₁s₂, s₂)`.
  With P4, `K(Z_F)` is `SWAP`-invariant, so S1 is EXOTIC-X with the stage-3 cone (the protocol's expectation).
- **P2 (S2, E0).** `ipW(E0, actC Rz(θ) E0) = 1 + 2cos θ`, equal to −1 at θ = π. Members of an invariant self-dual
  cone pair nonnegatively, so no self-dual cone invariant under the commuting torus contains `E0`: `K(E0)` cannot
  serve as an S2 countermodel.
- **P3 (S2, Z_F).** `ipW(z_s, torus(θ, φ) z_s) = (1 + cos(θ + s₁s₂φ))/8 ≥ 0`: the P2 obstruction does not fire for
  the Bell-type defects. The half-turns `actC Rz(π) = Ad(Z⊗I)` and `actT Rx(π) = Ad(I⊗X)` permute `Z_F`. A
  rational-angle torus image of `z_(1,1)` lies outside `Z_F` and pairs 9/100 with `z_(1,1)` itself (and 4/25 with
  `z_(−1,−1)`), so the torus orbit of a Bell-type defect is a 2-torus of mutually non-orthogonal tables: stage 3's
  finite-orthogonal surgery does not apply to S2 as it stands. An explicit torus-invariant cone, if Z gives one,
  must come from a different construction, or Z must show none of this kind exists.
- **P4 (retention).** `Q3` is preserved by `SWAP` and by the torus (exact PSD checks on a rank-4 sample and its
  images).
- **P5c (countercontrol).** `SWAP E0 = E00 + E31 − E22 ≠ E0`, `ipW(E0, SWAP E0) = 2 ≥ 0`, yet `SWAP E0 − λE0` is PSD
  for no λ in [0, 2/3] (exact root isolation): `SWAP E0 ∉ K(E0)`. `K(E0)` is not `SWAP`-invariant; S1 needs the
  Bell-type cone.
- **P6 (finite extensions, local Paulis).** All six local Paulis permute `Z_F`; with P1 and the level-(ii) group,
  `K(Z_F)` is invariant under LPT (order 64) and LPT + SWAP (192): those finite nodes are EXOTIC-X with the stage-3
  cone.
- **P7 (finite extensions, control Clifford).** `Ad(H⊗I) z_(1,1)` is a Bell-type defect (spectrum
  {−1/8, 1/8, 1/8, 1/8}) outside `Z_F`, and the pure state `P_{Ψ⁺}` lies in `K(Z_F)` (PSD; pairings 1/2, 0, 1/2, 0
  with the four defects) while pairing −1/2 with the image. So `K(Z_F)` is not invariant under the control Hadamard:
  the node `G16` + control Clifford (and the full Clifford group) needs a countermodel other than the stage-3 cone.

## What this does not establish (for the audit to hold Z to)
- Nothing here exhibits an explicit cone for S2, S3, the drive, or the Clifford extensions; Y's audited results give
  existence (EXOTIC-E) for those with exact cap-defect seeds (AUDIT-Y). Z's explicit cones, if any, are to be checked
  for H1–H3 and the node's invariance exactly, by the stage-3 surgery characterization where it applies and by an
  independent self-duality check where it does not.
- The "finite extension" conjecture (no finite group containing `G16` excludes all Bell-type defects) is Z's to
  prove or refute; Y's dichotomy shows every finite group is EXOTIC-E by a cap defect, which is a different
  statement (cap defects are not Bell-type unless c = 2).
- Whether Z's axis finding (its NOTES N11 heading, not read) agrees with Y's Y3 classification is to be compared
  after both are audited, each on its own evidence.

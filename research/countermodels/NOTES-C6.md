# NOTES-C6 — the realization-facing structure of K(Z_F)

Node C6 of `README.md`. Output: the handoff proposal `handoff-proposals/HP1-KZF-realization-facing.md` for
`research/bridge`, compiling the properties of K(Z_F) established in C1–C5 and the archive, with one new exact script.

## Script
`experiments/c6_handoff_checks.py` (run 1: 7/7, `VERDICT C6-HANDOFF-CHECKS-EXACT`; replay identical; the identity test of
H1 uses unique remainders modulo the Groebner basis `{|n|² − 1, cos² + sin² − 1}`, adopted before the first run).
- H1: T6's flow law re-derived independently, symbolic in the axis and the angle, both tokens, all four defects:
  `ipW(R_n(t) z_s, R_n(π/2) p_s) = −sin t/8`, the witness pairing `0` or `(1 − n_i²)/8` with the defects.
- H2: `Σ_s z_s = E00`; `ipW(z_s, T_{ψ_s}) = −1/2`; `z_s + z_t` PSD of rank 2.
- H3: the normalized defects are pure-like (squared norm 4, spectrum `(−1/2, 1/2, 1/2, 1/2)`).
- H4: maximal steering of the defects (stage 5 C5 θ re-checked symbolically).
- H5: no local generator commutes with all four cap projectors (a second route, with C2's finite local stabilizer, to "no
  continuous local symmetry").
- Countercontrols: Q3 members pair nonnegatively under the same rotations; the law fails with the defect in place of the
  cap-centre witness.

## The handoff (summary)
Twelve properties KZ1–KZ12 (extreme rays, excluded caps, pure-like defects with sum rules, steering, the full automorphism
group, the finite local group, the failure of every local flow, the pair's own non-local drive, the facial invariant, the
Bell-diagonal slice, non-uniqueness given the symmetry group, the four-copy readings), each labelled. Proposal: a
realization theorem whose composition clause makes continuous local operations act on the pair cannot have `K(Z_F)` in its
range (KZ5–KZ7); that clause is (b) (T6 §5's disguise test); a realization of `K(Z_F)` would need reversible dynamics inside
the Bell-diagonal torus with only the 384-element local group.

## Gem classification (§A.31)
- POSITIVE: T6's flow law survives an independent symbolic re-derivation.
- ELABORATING: the realization-facing list; the assumption-watch marker of R6 §6 sharpened to a statement about this cone.

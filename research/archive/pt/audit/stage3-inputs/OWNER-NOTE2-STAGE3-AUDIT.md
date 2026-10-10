# Owner's second note for the stage-3 audit (received 2026-10-10, after the U/X launch; audit input only)

Placed under `pt/audit/` so the running threads do not see it; not supplied to the threads; the protocol
`PROTOCOL-STAGE3.md` (`1a649168…`) is unchanged. Used by the coordinator's audit checks (`qsd_owner_note2.py`, 4/4
CONFIRMED on run 2; run 1 kept, failed on my own choice of a test vector outside the negative region).

----- BEGIN VERBATIM (mathematical content) -----
### 1. The 36 axis products are a bound, not a complete positivity test

They suffice to prove the coefficient bounds and restrict a normalized search to the unit cube. However, they do not
by themselves establish positivity on every product state. For an EXOTIC certificate, H1 must hold for the full
continuous family of product states, not just the 36 axis products. Likewise, satisfying the cube bounds does not
establish membership in C*. This distinction matters especially if Thread X discovers a numerical candidate.

### 2. An exact negative witness need not be an eigenvector

For any Hermitian X that is not positive semidefinite, one can find a vector v with Gaussian-rational coordinates
such that v†Xv < 0. This follows because the negative quadratic form is continuous and Gaussian-rational vectors are
dense. Consequently, the normalized projector P_v = vv†/(v†v) provides an exact witness without requiring an exact
symbolic eigendecomposition. If X ∈ K, then self-duality excludes P_v from K. H1 and H2 further ensure that P_v is
neither a product state nor a CNOT image of one. This could simplify Thread X's eventual exact certificate.

### The decisive distinction

* Uniqueness: Do H1–H3 mathematically force K = Q3?
* Origin: If they do, can H3 itself be derived from embedded observation?

The frozen protocol already separates these questions appropriately. I see no reason to expand the current research
scope before U and X have been independently audited.
----- END VERBATIM -----

Coordinator's exact confirmations:
- G1–G3: for X = F = E00/2 − T_ψ/4 (ρ(F) = I/8 − |ψ⟩⟨ψ|/4, ψ = (1,1,1,−1)/2), the Gaussian-rational vector
  v = (1, 1 + i/10, 1, −1 + 1/7), not an eigenvector, has v†ρ(F)v = −36251/78400; P_v has a rational Pauli table;
  ipW(F, P_v) = −36251/73396 < 0; P_v and CNOT P_v are entangled (Schmidt rank 2), so the missed pure state lies
  outside K_gen. The witness argument uses only K ⊆ K*.
- G4 (point 1, instance): w = E00 + (9/10)(E11 + E12 + E21 − E22) passes all 36 axis-product checks and the cube
  bound, yet lies outside maxCone (value 1 − (9/10)√2 < 0 at x = e1, y = −(e1 + e2)/√2). So the finite tests are
  necessary conditions only; membership in maxCone, K_E or K needs a continuous certificate (spectral bound or SOS
  identity, as in AUDIT-S2 E3 and S2's s2_6).

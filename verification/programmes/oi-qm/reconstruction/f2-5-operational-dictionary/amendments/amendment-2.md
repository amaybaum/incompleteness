# F2-5 — amendment 2: a site-ordering control, after one development run and before any recorded run

## The development run

The development run used script sha256 `d1c51433…` and gave output sha256 `3c9eda38…`.
- Every control passed.
- OD-SUB, OD-REV, OD-PREP, OD-READ, OD-COMP and OD-HOLD were positive.
- OD-AD failed, so the run printed `OD-NOT-READ`.

A diagnosis of the failure, made outside the cells, found three things:
- The script's `N`-site Weyl operators index site 1 by the least significant digit, so
  `D((x₁, x₂), (ξ₁, ξ₂)) = D(x₂, ξ₂) ⊗ D(x₁, ξ₁)`.
- So `A(z₁, z₂) = A(z₂) ⊗ A(z₁)` for all 81 points, while OD-AD compares against `A(z₁) ⊗ A(z₂)`.
- Its partial trace over the second Kronecker factor returns `A(z₂)`.

The failure is therefore a mismatch between the site order of the `N`-site construction and that of the Kronecker
product. It is not a property of the dictionary. OD-COMP is unaffected: product and maximally entangled images, and
their classification, do not depend on which factor is which. The development run's tokens are not used.

## The correction

- **The site order.** The script indexes site 1 by the most significant digit, so that the `N`-site construction and
  `⊗` agree.
- **A new control.** **K-order** checks `D((x₁, x₂), (ξ₁, ξ₂)) = D(x₁, ξ₁) ⊗ D(x₂, ξ₂)` for all 81 pairs.
  - OD-AD (i) then tests the factorization of the parity term `Π`, which is not implied by the site order.
  - A token printed with K-order failing is void.

No cell, configuration or reading changes.

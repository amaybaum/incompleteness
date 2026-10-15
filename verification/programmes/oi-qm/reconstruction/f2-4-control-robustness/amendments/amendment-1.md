# F2-4 amendment 1: OD-2's link set is taken per direction

Append-only amendment to `../RULES.md`, made after a development run and before the recorded run.
Nothing else in the rules changes.

## The defect

OD-2 joins two-site lines by the links `{(v₁,v₂) ~ (w₁,w₂) : wᵢ ∈ R(vᵢ)}`, with `R` OD-1's one-site
relation. That relation is F2-2's `adjoint_relation`, which merges the relation of `h` with that of
`h†`. A product of merged relations is not the relation of `h ⊗ h` together with its adjoint.

- It contains cross links `(w₁, w₂)` with `w₁ ∈ R_h(v₁)` and `w₂ ∈ R_{h†}(v₂)`.
- Neither `Ad_{h⊗h}` nor `Ad_{(h⊗h)†}` produces those links.

The rule's claim that the set "is exact, by the tensor-product structure of `Ad_{h⊗h}`" therefore
fails as written. The merged product can only over-join, which makes it unsound for D1.

**How it was found.** A development run of the script gave `VERDICT VOID`.

- K-D1neg with `u ⊗ u` failed at every `q`. For the Clifford gate `u`, the relations are
  `R_u(v) = {Jv}` and `R_{u†}(v) = {J⁻¹v}`. The merged product pairs `Jv₁` with `J⁻¹v₂` and joins
  distinct orbits.
- K-indep (i) passed at `(3,2)`. For the free half-layers there, the merged product happens to
  coincide with the exact relation, so that comparison alone could not have detected the defect.

That run's OD-2 tokens are discarded. The floating-point design probe used the same merged product,
so its two-site component counts are superseded as design evidence.

## The corrected link set

For `g ∈ {h, h†}`, let `R_g` be the one-site relation of `g` alone: `w ∈ R_g(v)` iff
`g W(v) g†` has a nonzero `W(w)` component. Extend it by `R_g(0) = {0}`. The link set is

`⋃_{g ∈ {h, h†}} {(v₁, v₂) ~ (w₁, w₂) : w₁ ∈ R_g(v₁), w₂ ∈ R_g(v₂)}`.

This set is exact. The `W(w₁) ⊗ W(w₂)` component of `Ad_{g⊗g}(W(v₁) ⊗ W(v₂))` is the product of the
one-site components.

Consequences for the cells and controls:

- **The sound subset** is taken per `g`.
- **OD-1's D1** uses `R_h ∪ R_{h†}`. That is F2-2's `adjoint_relation`, so OD-1 is unaffected.
- **A new check, K-indep (v):** at `q = 3` and `q = 5`, `R_h ∪ R_{h†}` must equal F2-2's
  `adjoint_relation` for every free pattern.
- **K-indep (i)** compares the corrected set with F2-2's `adjoint_relation` of `h ⊗ h`.
- **K-D1neg at `N = 2`** uses the corrected set for `u ⊗ u`.

## Also recorded, with no rule changed

- K-AD-mut's modular values are lower bounds.
  - At `(3,2)` they are tied to exact values by K-indep (ii).
  - At `(3,3)`, the local mutation's value is matched by the written upper bound `N(q² − 1)`:
    every generator is then a sum of one-site terms.
  - The value without translations at `(3,3)` is a lower bound only. The result says so.

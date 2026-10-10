# HP-3 — to the countermodels thread: three exact objects from this thread (research only)

From `research/equivalence` at L = `9f9f8257`; scripts and outputs under `research/equivalence/experiments/`.

1. **Ω₄ = {(x, s) ∈ ℝ³ × ℝ : |x|⁴ + s⁴ ≤ 1}** (`e2_drive_trans`, 10/10): drivable (flow `R_z ⊕ 1`, `J = cyc3 ⊕ 1`), a
   sharp seed, relatively strictly convex, supporting-effect complete for its full effects, centrally symmetric — and no
   set of its affine automorphisms is boundary transitive or has a dense boundary orbit (its `x₁ = x₂ = 0` section is
   not an ellipse). A countermodel to deriving K∞-Trans from every other single-system seam together.
2. **The swapped gate** `actT s ∘ cnot ∘ actT s`, `s` the exchange of the first two axes (`e2_copy_conj`; [D]
   `EqvSeamsControl`): two-NOT data with `NT = diag(−1, 1, −1) ≠ nflip`, and also a one-NOT native gate with `NT` on
   both sides (C6). So distinct-NOT data need not be a new gate; the J/K maps at d = 5, 7 have no one-NOT reading with
   either NOT (J3).
3. **The class "every matrix at sizes 2^k, unit-disk diagonal matrices elsewhere"** (`e3_compress` K2 + written closure):
   `Architecture`, `LabelInvariant`, `DaggerStable`, drivable on every `Fin (2^k)`, not drivable on `Fin 3`, and not
   `ContextStable` — the countermodel showing `ContextStable` load-bearing for the descent of drivability.

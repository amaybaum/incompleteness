# Thread L — running notes (read-only; certified main 6d0abf6b)

- Worktree `wt/` detached at 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a. Read in full: KF (1212 lines), NGB (289 lines).
  Background read: threads/H/RESULT.md, threads/H/CHARTER.md. Threads I, J and K were not opened.
- Mathlib: there is no `.lake` and no `~/.elan`. The scratchpad `mathlib-ref/` has no provenance. So the pinned
  sources were fetched from `raw.githubusercontent.com/leanprover-community/mathlib4/v4.33.0`:
  `lakefile.toml` pins rev `v4.33.0`, and that tag's `lean-toolchain` is `leanprover/lean4:v4.33.0`, which is
  identical to the repo's. Seven files are in `mathlib-v4.33.0/`. A name counts as verified when it appears
  there, or in a landed OIBridge module, which CI builds against the same pin.
- First pass, the mathematics.
  - Sharp on ball3 means 1 at u and 0 at w. With r = c + a·v, use the values at ±u, ±w and at the rational test
    point p = 4a/(1+4|a|²). This gives c = 1/2, |a|² ≤ 1/4 and |2a − u|² ≤ 0. Hence u = 2a and |u| = 1. The
    argument needs no sqrt.
  - ⊆ needs only that each g and g⁻¹ preserve the ball. Group structure, linearity and centrality are not
    used.
  - ⊇ needs the G-orbit of the seed's certain point to cover the sphere (COVER). Transitivity gives it, and the
    seed point is automatically a boundary point (L3).
- V4′ does not enter the set equality at all. It only places the orbit in `avail`.
- Trap: on `Fin 3 → ℝ`, `Metric.sphere 0 1` is the cube surface (sup norm). The family must be indexed by
  Σ b_j² = 1, which is exactly the form of the `lorentz_of_effects` hypothesis.
- Trap: KF's Lemma B (`eq_closedBall_of_frontier_subset_sphere`) gives `Metric.closedBall`. For V = Fin 3 → ℝ
  that is the cube, not `ball3`, so a route from Lemma B to `ball3` must go through EuclideanSpace.
- Pressure test of the favourable verdict.
  - A black-box K∞-R stated as transitivity does not contain G ⊆ Aut(Ω). Countermodel: all affine maps, or
    fullAut3 ∪ {½·id}. So PreservesBody is a separate premise.
  - For KF's drive generators, PreservesBody is supplied by `flow_preserves`, the flow inverse, `J_preserves`
    and `J_symm_preserves` (`preservesBody_drive`).
- Written remark, not used: for any ElementaryDrivability of ball3, ⟨flow, J⟩ ⊇ SO(3) is transitive.
  - The flow is a rotation about n, and J_off_axis forces Jn ≠ ±n.
  - Two distinct rotation axes generate a connected subgroup whose Lie algebra is so(3), which is SO(3) by
    Yamabe's theorem.
  - This is not kernel-checked, and K∞-R stays a black box.
- l_checks.py run: `OK -- 41 checks, 0 failed`. The replay is identical (`l_checks.rerun.out`).

# Thread N — working notes (ellipsoid / K∞-R step)

Read-only against `L = f7f5c3b0c621cc3e4b57e3709d11d9d580c81149` (worktree `wave2/wt-N-ellipsoid`, HEAD verified equal
to L). Paths below are under `verification/lean-mathlib/OIBridge/`. KF = `KInfFoundations.lean`, OG =
`OrbitGeneration.lean`, ON = `OrbitNormalization.lean`. No other wave-2 thread directory was read; the IIP round's
worktree was not read either (its interface is used only as stated in the charter).

## Productivity test (fixed before starting)

A branch is a gem iff it yields a fact strictly stronger than the restatement of K-T4 ("a drive on a compact convex
body of affine dimension 3 gives an ellipsoid and a boundary-transitive drive group") AND either constrains a frozen
statement or exposes a hidden assumption in one. Below that bar: record only.

## Landed identifiers re-verified at L (file:line)

| identifier | where | used for |
| --- | --- | --- |
| `ElementaryDrivability` (fields `flow` 265, `flow_zero` 266, `flow_add` 267, `flow_continuous` 268, `flow_preserves` 269, `t₀` 270, `N_involutive` 271, `N_moves` 272, `J` 273, `J_preserves` 274, `J_symm_preserves` 275, `J_off_axis` 276) | KF:264 | the drive |
| `ball3`, `ball3Drive`, `ball3_drivable` | KF:311, 449, 490 | controls |
| `not_drivable_Icc`, `not_drivable_singleton` | KF:529, 564 | dim ≤ 1 (landed, specific bodies) |
| `eq_closedBall_of_frontier_subset_sphere` (Lemma B; sup-norm `closedBall` on `Fin 3 → ℝ`, not `ball3`) | KF:770 | not used (wrong norm for `ball3`) |
| `ballEffect`, `ball3_extend` | KF:1026, 1036 | — |
| `SharpSeed`, `PreservesBody`, `SeedOrbitAvailable`, `BoundaryTransitive` | OG:65, 69, 74, 79 | K∞-R target |
| `drive_flow_symm_apply`, `preservesBody_drive` | OG:150, 161 | `g '' Ω = Ω` for the generators |
| `sphere_of_isBoundaryState_ball3`, `isBoundaryState_ball3_of_sphere` | OG:246, 239 | boundary of `ball3` = unit sphere |
| `seedOrbit_ball3_eq`, `lorentz_of_available` | OG:348, 422 | downstream consumer |
| `not_boundaryTransitive_flow` | OG:620 | flow alone is not K∞-R |
| `words`, `preservesBody_words`, `preservesBody_driveWords` | ON:53, 79, 107 | the K∞-R group |
| `flow_zero_of_add` (B1), `isEmpty_drivability_of_finite_orbits` (B5) | ON:114, 124 | `flow_zero` redundant |
| `conjTr`, `boundaryTransitive_tr`, `hypotheses_tr` | ON:177, 257, 295 | normalization transport |
| `seedOrbit_eq_of_normalization`, `lorentz_of_normalization` (take `T : V ≃ᵃ[ℝ] (Fin 3 → ℝ)`, `T '' Ω = ball3`) | ON:307, 340 | what ELL-ellipsoid must feed |
| `chart`, `isBoundaryState_restrict`, `restrictEquiv`, `hypotheses_restrict` | ON:357, 407, 489, 529 | restriction (named hypotheses only, not the drive) |
| `rotX`, `euler_apply_pole`, `exists_euler_angles`, `exists_word_pole`, `boundaryTransitive_ball3Drive` | ON:581, 589, 614, 658, 667 | template for the exact-word proof |
| `isBoundaryState_closedBall_iff`, `ball4`, `isom4`, `boundaryTransitive_ball4`, `finrank_E4` | ON:686, 715, 718, 735, 744 | dim-4 countercontrol (transitivity only) |

`ElementaryDrivability` is used only in KF, OG, ON (grep at L). OG-1's preregistration (round directory
`programmes/oi-qm/reconstruction/round-og-1-orbit-generation/preregistration.md`, lines 61–82) froze out "the
ellipsoid theorem", "dimension-3 sourcing" and B6, and says B6 "needs an inner product invariant under a compact group
of affine automorphisms, which nothing landed supplies" — the IIP interface removes the word "compact".

Mathlib: the repo pins tag `v4.33.0` (`lakefile.toml`, `lean-toolchain` = `leanprover/lean4:v4.33.0`). I cloned that
tag (blobless, depth 1) to `N/mathlib-v4.33.0` (commit `db584cd6d46c92f209a44c0f1c829460d327499d`, identical to the
commit of the scratchpad `ml4` checkout) and grepped names; table in RESULT.md §8.

## Depth-first walk (branch nodes, each closed by a check)

**N1. Does IIP make every generator orthogonal about c?** Generators satisfy `g '' Ω = Ω`: `preservesBody_drive`
(OG:161) gives `g x ∈ Ω ∧ g.symm x ∈ Ω`, hence image equality (two-line lemma, not landed). IIP then gives `g c = c`
and `A S Aᵀ = S` ⇔ `Aᵀ S⁻¹ A = S⁻¹` (exact X1.1–X1.2). Verdict: yes, for `flow t` (all t) and `J`. Normalization by
`S = M Mᵀ` makes `M⁻¹ A M` orthogonal (X1.3); Mathlib's LDL (`LDL.lower_conj_diag`) supplies `M` (X1.4–X1.5).

**N2. Are flow members rotations (det 1)?** `flow t = flow(t/2)²` (flow_add), so `det A(t) = det(A(t/2))² > 0`
(X2.1). No continuity. Verdict: `A(ℝ) ⊆ SO(3)`.

**N3. Do the flow members share one axis?** Take any t with `A(t) ≠ I`. `Q := A(t/2)` is neither `I` nor a half-turn
(its square is `A(t) ≠ I`; X3.3). Every `A(s)` commutes with `Q` (flow_add twice); the commutant of a non-half-turn
rotation in SO(3) is the circle about its axis (X3.1), while half-turns can commute without sharing an axis (X3.2, the
Klein countercheck — which is why `t/2` is used). Verdict: `A(ℝ) ⊆ SO(2)_a`. No continuity, no `t₀`.

**N4. Where does a non-identity flow member come from?** `J_off_axis` at `s = 0`: `J ∘ flow t ∘ J⁻¹ ≠ id` on Ω, so
`flow t ≠ id` on Ω (else `J (flow t (J⁻¹ x)) = J (J⁻¹ x) = x` for `x ∈ Ω`, using `J_symm_preserves`). With Ω spanning
(interior), `A(t) ≠ I`. Verdict: `N_moves`, `t₀`, `N_involutive` are not needed anywhere in (1)–(4). **NEW.**
`N_involutive` only identifies `N = A(t₀)` as the half-turn about a.

**N5. Is the flow the whole circle?** With `flow_continuous`: `t ↦ ⟨A(t)e, e⟩` (e ⊥ a unit) is continuous, equals 1
at 0 and `cos θ₁ < 1` at some t₁; IVT gives every value in `[cos θ₁, 1]`; the image is a group, so it contains
`R_a(±φ)` for `0 ≤ φ ≤ θ₁`, and powers give the whole circle. Without continuity: the image is a nontrivial
divisible subgroup of the circle, hence infinite, hence dense — its closure is the whole circle. Verdict: continuity
is needed for "image = circle", not for "closure of image = circle". **NEW (sharpens K 2.N3).**

**N6. Does J_off_axis force non-parallel axes, compared on Ω?** If `Ba = ±a` then `B R_a(θ) B⁻¹ = R_a(±θ)` for
all four O(3) families fixing the line (X4), so `J flow(t) J⁻¹ = flow(±t)` on all of V, and J_off_axis fails.
Contrapositive: `Ba ∉ {±a}`. Uses only that `A(ℝ)` is a subgroup of `SO(2)_a`; no continuity. Conversely, `Ba ∉ ±a`
and `A(t) ≠ I` give J_off_axis (X5.1–X5.4). Verdict: J_off_axis as landed is exactly "non-parallel axes" in affine
dimension 3 under IIP. POSITIVE. Skeptic pass on this favorable branch: (i) all four axis-preserving O(3) types
checked symbolically (X4); (ii) a reflection J (det −1) is allowed and still works, but then the words contain det −1
maps (X5.5): the closure is O(3), so ELL-closure must say "⊇ SO(3)"; (iii) an off-axis clause compared on V instead
of Ω would be too weak: X13 has J = id on Ω, J ∘ flow ∘ J⁻¹ ≠ flow on V. The landed "on Ω" reading is the right one.

**N7. Two full circles, non-parallel axes: exact finite words?** Cap argument (written; RESULT §3): alternating
words of n factors from `SO(2)_a`, `SO(2)_b` cover SO(3) iff `(n−1)α ≥ π`, α ∈ (0, π/2] the angle between the axes.
Order `N(α) = ⌈π/α⌉ + 1`. Matches Lowenthal 1971 (search-result summary: `π/(k+1) ≤ ψ < π/k ⇒ order k+2`, `ψ = π/2 ⇒
3`; X7.L2–L6). Witnesses of sharpness: half-turn about `a×b` (odd n), about `a−b` (even n) (X7.4–X7.5, X7.14 for
symbolic α). Exact word instances: α = π/2 three factors (X7.1); α = π/3 four factors for the n = 3 witness
(X7.9–X7.11). Verdict: exact finite reachability holds for every α > 0, with no uniform bound as α → 0. **NEW
(for this corpus).**

**N8. Ellipsoid from invariance.** Ω closed and invariant under a set whose orbit closures contain the Q-spheres ⇒
Ω contains the Q-sphere through each of its points ⇒ (convexity) the Q-ball through each point ⇒ Ω = Q-ball of
radius `max Q` (compactness for the max; interior for R > 0). Countermodels: shell (X11, convexity), open-ball-plus-
countable-orbit (closedness, written, needs the Hamel drive), cylinder (X12, compactness; IIP fails there).

**N9. Dimension-4 controls.** B⁴ with `R(t)⊕I₂`, swap J: J_off_axis holds (X8.2), invariant `|x₁₂|²|x₃₄|²`
(X8.3) separates two unit vectors (X8.4): neither words nor their closure is transitive, although B⁴ satisfies IIP.
Bidisk with the same drive: boundary contains a segment (X8.5), not an ellipsoid. K's `SO(3)⊕1` (X8.6).

**N10. Dimension ≤ 2 (B6).** O(2) conjugation sends `R(θ)` to `R(±θ)` (X6.1–X6.2) and flow members are in SO(2)
(X6.3); so `J flow(t) J⁻¹ = flow(±t)`: J_off_axis fails on every compact convex body of affine dimension 2 satisfying
IIP. Dimension 1: flow members are squares in O(1), so trivial (X6.4), J_off_axis fails. No continuity, no N fields.
ELABORATING (B6 re-derived more cheaply than F/K). Note OG-1 froze B6 out as a dimension-exclusion step.

**N11. Restriction of the drive (infrastructure).** `hypotheses_restrict` (ON:529) restricts P1/V4′/K∞-R/G-AUT, not
an `ElementaryDrivability`. The restricted flow's continuity cannot be read off `chartRetract Lg p0` because `Lg`
(from `LinearMap.exists_leftInverse_of_injective`) need not be continuous on an infinite-dimensional V (e.g. the
ℓ^∞(E∞) of Thread M). It holds by factoring through the finite-dimensional range (`LinearEquiv.toContinuousLinearEquiv`)
or a continuous projection (`Submodule.ClosedComplemented.of_finiteDimensional`). ELABORATING (proof-engineering
assumption-watch for the formal round).

Fixed point: passes 1 (N1–N7: NEW ×3), 2 (N8–N11: no NEW), 3 (skeptic re-pass of N5/N6/N7 favorable readings: no
NEW), 4 (circularity re-pass: no NEW). Stopped.

## Exact checks

`n_checks.py` → `n_checks.out`: `OK -- 66 checks`; replay byte-identical (`n_checks.rerun.out`).
sha256 `7b8d0ab59b5a3247366f4022045301b028646b77cb3b0f7a3350a9d46c66cdf0` (script),
`3f996bc5470448e09e5ab913537cdae719725b24c7011745add0b3cc525e7f58` (output). sympy 1.14.0, rationals, exact radicals,
symbolic trig; no floats.

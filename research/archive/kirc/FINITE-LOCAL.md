# Finite local symmetry — read-only, from L42

Baseline `fdebc6e3`. This is the branch left open by `BALL-NOGO.md`: replace the full `SO(d)×SO(d)` by the local
transformations actually available, and ask whether a CNOT-on-corners map still forces d = 3.
- Exact checks: `disc_depth1.py` (11 PASS, 0 FAIL, log `disc_depth1.log`).
- Numerical evidence: `depth1.py`, `depth1inv.py`, `finite_local.log`.
- Nothing is committed.

## 1. Density reduction: any infinite-order local gate is as good as the full group (exact)

`Aut_e(C)` is compact, hence closed (Step 0 of `BALL-NOGO.md`). If it contains a set `Γ` of local gates, it contains
the closure of the group they generate, `cl⟨Γ⟩ × cl⟨Γ⟩`.

- **Disc.** The corpus's native mixing datum is one fixed real rotation, `rot α` (`StateMixingCoupling.rot`,
  `DiscreteCompletion.FixedGateSourced`). It rotates the rebit disc by `2α`.
  - For α/π irrational, the multiples of `2α` are dense mod `2π` (the kernel's `dense_angles`, `DiscreteCompletion`
    Section E), so `cl⟨rot α⟩ = SO(2)`, and the disc theorem applies unchanged.
  - For α/π rational the group is finite.
- **d ≥ 3.** Fixed Givens rotations in every coordinate plane, each at an angle `α` with α/π irrational, have closure
  containing every plane rotation group `SO(2)_{ij}`. These generate `SO(d)`. The ball theorem then applies unchanged.
- **Consequence.** The continuity premise of `BALL-NOGO.md` is not a premise about the gates. It is implied by any
  single local gate of infinite order: compactness of the reversible group closes the orbit.
  - What remains open is exactly a *finite* local group, meaning every gate of rational angle. The corpus records the
    rational-angle classification as open: `α ∈ (π/4)ℤ` is finite, `π/8` is predicted dense, and neither remaining
    direction is kernel-proved.
- **Scope.** This uses the discrete completion audit's datum, which is stated with ℂ matrices and phases available.
  Here only its real rotation is used, acting on the disc or ball.

## 2. The disc needs no local dynamics at all (exact)

**Theorem (d = 2).** No injective linear map `G` on `ℝ³⊗ℝ³` that acts as CNOT on the four classical corners maps
`L₃ ⊗min L₃` into `L₃ ⊗max L₃`.
- There is no local group, not even NOT.
- There is no involution.
- `G(C) = C` is not required, only `G(min) ⊆ max`.

Proof, with `Y_b = G(X⊗|b⟩)`, `b ∈ {0,1}`:
- **D1 — the derivative at the corners.** `s(θ) = (1, sin θ, cos θ)` is pure, and by the frame
  `G(s(θ)⊗|b⟩) = cos²(θ/2)|0,b⟩ + sin²(θ/2)|1,1−b⟩ + sin θ·Y_b`.
  - A product effect vanishing on `|0,b⟩` gives `sin²(θ/2)(…) + sin θ·h(Y_b) ≥ 0` for small `θ` of both signs, so
    `h(Y_b) = 0`. The same holds at `θ → π` for effects vanishing on `|1,1−b⟩`.
  - Taking `h = ⟨0|⊗g` and `⟨1|⊗g` for all `g` gives `(u*⊗I)Y_b = (z*⊗I)Y_b = 0`. On the disc
    `ker u* ∩ ker z* = span X`, so `Y_b = X⊗w_b`.
- **D2 — the equator.** At `θ = ±π/2` the value on `(1,a)⊗(1,c)` is `1 + σ a_z c_z ± a_x (g·w_b)`, where
  `σ = (−1)^b` [checked symbolically].
  - Choose `a = (sin φ, cos φ)` and `c = (±sin φ, −σ cos φ)`. Then `|w₀ ± w_x sin φ − σ w_z cos φ| ≤ |sin φ|`.
  - Letting `φ → 0, π` gives `w₀ = w_z = 0`. So `Y_b = λ_b X⊗X`.
- **D3 — rank.** `G` maps the 2-dimensional `span{X⊗|0⟩, X⊗|1⟩}` into `span{X⊗X}`, so it is singular. ∎

**Where d = 3 escapes, and why it must.** On the Bloch ball, `ker u* ∩ ker z* = span{X, Y}` is 2-dimensional [D1
control]. The complex CNOT has `Y_b = XX ∓ YY`, and the two are independent [control]. The escape is the second
transverse direction, the one real QM's projection loses.

**Controls.**
- The measure-and-flip map `s⊗t ↦ Σ_k ⟨k|s⟩ |k⟩⊗NOT^k t` meets the frame and `G(min) ⊆ max`. Its `Y_b = 0`, so it is
  singular, as D3 requires.
- A constructive witness routine finds an explicit violated (product state, product effect) pair for 40 of 40 random
  invertible maps in the weak family.

**Numerical evidence (consistent, superseded).**
- Depth 1 with no local group: the best slack is 0 without the involution, reached only at `det ≈ 0`.
- Depth 1 with the involution: about −0.82.
- Both directions, `G` and `G⁻¹`, no involution: about −0.71.
- `C₂ = {I, NOT}` at depth 3: about −2.0.

The optimizer is not a reliable feasibility oracle: in the both-directions run on the Bloch ball it missed the known
feasible complex CNOT, reaching −1.13. The exact theorem, not these numbers, carries the disc.

## 3. What this changes

- **For d = 2 the local-group question dissolves.** No local dynamics is needed to exclude the disc. What does the
  work is the disc's continuum of pure states near the corners and at the equator, which is kinematics. It also
  excludes more than `BALL-NOGO.md` did, since only `G(min) ⊆ max` and injectivity are used.
- **For d ≥ 4 with a finite local group: open.** D1 leaves `Y_b ∈ T⊗ℝⁿ` with `T` the (d−1)-dimensional transverse
  space. From d = 3 on there is the same room the complex CNOT uses, so this elementary argument cannot exclude
  d ≥ 4. Whether some d ≥ 4 composite with a finite local group carries a CNOT-on-corners map is the live question; the
  quaternionic 5-ball is the case of interest.
  - Candidate countermodels would place the complex CNOT on a 3-dimensional sub-ball and must then handle the extra
    transverse directions.
  - A decisive computation needs an exact method. The feasibility optimizer is not trustworthy here (see the control
    above).

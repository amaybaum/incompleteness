# Three-dimensional free-wave observable revival without microscopic return

**Research candidate.** This is exact algebra for an added compact torus extension of the unnormalized cubic wave update, with an added distributed finite readout. It does not establish that OI physically supplies this carrier, Haar preparation, public readout or selectable measurement interactions. It is not a Lean proof or a manuscript theorem. The finite-horizon equivalence and conditional finite-carrier recurrence results are unchanged.

## Pinned mathematical construction

Use a periodic 3×3×3 cubic lattice. Let A be its six-neighbor adjacency matrix and put

`F(u,p) = (Au−p,u)`

on `X = (R/Z)^54`, equipped with normalized product Haar measure. This is the same **unnormalized** integer update form as the microscopic wave rule, extended from finite modular site values to circles; it does not substitute the observer-level coefficient 1/3. Its inverse is `(w,u) ↦ (u,Au−w)`, an integer map. Thus F is a compact-group automorphism, its integer determinant is ±1, and it preserves normalized Haar measure.

The reference source is `papers/oi_lattice_code/trace_out_fractional/wave_eqn.c` at research input `3cb09a15be46d536b0056b032234b3c2e3660d48`: lines 5–16 state the rule and reversibility, lines 35–43 compute the six-neighbor update, and lines 55–80 implement the inverse. That source acts modulo Q; changing the site group to a circle is the added mathematical extension here.

Set `h=(2,−1,−1)` and the 27-entry row `v(x,y,z)=h_x h_y`, constant in z. On the three-cycle the neighbor operator sends h to −h and the constant vector to twice itself. Therefore

`vA = (−1−1+2)v = 0`.

The row v is nonzero and primitive (some coefficient is 1). For `w=(v,0)` the exact identities are

`wF=(0,−v)`, `wF²=−w`, `wF⁴=w`.

Define `Y_t = wF^t x mod 1`, and a **single fixed finite observation** `X_t=1[Y_t∈[1/2,1))`. Each cell has Haar mass 1/2. At step one the two integer rows w and wF are linearly independent (they live on different time slices). Their joint map onto the two-torus is surjective, so Haar pushes forward to independent uniform circle coordinates. Consequently `Γ₁=J₂`, the matrix with every entry 1/2. At step two `Y₂=−Y₀`; the half-circle bit is complemented except at the two boundary points, a Haar-null set. Therefore `Γ₂=swap`, and `Γ₄=I` for every state at the circle-coordinate level.

The total-variation distance of the two rooted bit distributions is zero at t=1 and one at t=2. This is the existing `CausalReadback.C4r` witness; `c4r_implies_pIndivisible` applies without any finite hidden-carrier assumption. More directly, J₂Λ has identical rows for every Λ, while swap has distinct rows, so no intermediate stochastic divisor exists.

This uses current-bit marginals under two rooted preparations. It does not claim that a full accumulated record forgets the initial root: a transcript retaining X₀ already distinguishes the roots perfectly. The complete transcript must be accounted for separately by a physical observer model.

## No global finite-order recurrence

On spatially uniform fields, A has eigenvalue 6, and F restricts to `[[6,−1],[1,0]]`, with eigenvalues `3±2√2`. One eigenvalue is strictly greater than one, so no positive power of the integer matrix F is the identity. An integer torus endomorphism is the identity only when its integer matrix is the identity. Thus the microscopic dynamics has infinite order even though this selected observable has a period-four coordinate and two-step distinguishability revival.

## Rooted preparation and locality boundaries

Because v has a coefficient 1, replacing that current-site coordinate with `v·u mod 1` and retaining all other current/previous coordinates is a unimodular torus coordinate change. Haar becomes a product with the first coordinate uniform. Writing that coordinate as `(a+r)/2`, with a the visible root bit and r uniform on [0,1), exhibits the same hidden prior for both roots. This is an abstract preparation factorization, not a physical setting/preparation operation.

The readout sums 27 current sites. Its public accessibility, physical computation/latency, back-action, source compatibility and reusable outgoing carrier are unproved. The fixed side-three example does not justify arbitrary lattice sizes or nonlinearly interacting/gauge-coupled dynamics. It supplies no Yang–Mills action or quantum-control menu.

## Independent controls and reproduction

Run `python3 -I -B cubic_wave_revival_probe.py` (or with `-O`). The probe checks the two-sided integer inverse, uniform eigenvalue-six mode, primitive nonzero v, `vA=0`, `wF²=−w`, `wF⁴=w`, and the rank-two criterion. It separately checks a single-site current readout: both its step-one and step-two forms contain previous-slice dependence, so under Haar its rooted map is J₂ at both times. The revival is not generic to every finite readout.

An independent finite-subgroup control enumerates the quotient coordinates `(v·u,v·p)` modulo N for N=4,8,16. The first-step matrix is exactly J₂. Finite grids give boundary points positive mass: at step two each rooted row is at TV distance `2/N` from swap, and the two rows are at distance `1−4/N`. In particular the N=4 grid has no step-one-to-step-two revival, while N=8,16 do. This is a boundary-sensitive countercontrol, not a substitution of finite counting for the Haar proof.

The mathematical gap in `ObservableMeasureReturn` is separate: its ENNReal ratio/identity theorem does not yet compose measurable finite-cell normalization into a real row-stochastic family and the existing P-indivisibility theorem. The exact proof above bypasses that general formalization gap on paper; it does not close it in Lean.

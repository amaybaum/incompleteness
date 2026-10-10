# Act 36 pre-freeze measurement — the residual deformation space at the certified rational stratum point

Measurement only, against immutable D36 = `8b33e25fcb7e5b464cbfc605f61f7d40e5825784`. All objects are those of the
frozen A35 probe (blob `99f98ca7…` at D36): the point is `F₄(z) ⊗ F₄(w)`, `z = (3+4i)/5`, `w = (5+12i)/13`, scaled to
unimodular entries; the deformation coordinates are the phase perturbations `θ ∈ R^256`, `F(θ) = (H∘e^{iθ})(H∘e^{iθ})* − 16·I`.
Every number below is exact (Python integers and fractions, Gaussian rationals); `numpy` appears only in floating-point
controls and in the modular-arithmetic count of §E3.

## A. First order

| object | dim | how |
| --- | --- | --- |
| rank DF | 176 | fraction-free / rref over Q; float control agrees |
| ker DF | 80 | exact integer basis |
| gauge (row + column phases) | 31 | |
| T = T_c + T_r, the two fixed-pairing Diţă hulls | 57 with gauge, 26 mod gauge | T_c 14, T_r 14, T_c ∩ T_r 2 (the Kronecker stratum's two circle directions) |
| Def = ker DF / gauge (the defect) | 49 | |
| R = ker DF / (gauge + T) | 23 | |
| coker DF | 64 | left null space of DF, exact |

## B. Second order — the form B : Sym²(Def) → coker DF

`B(v,v') = class of −½ D²F(v,v') = ½ Σ_k c_k (v_ik − v_jk)(v'_ik − v'_jk)` in coker; exact.
- Control: B(gauge, ker DF) = 0 in coker. ✓ (so B descends to Def)
- Control: D²F(T_c, T_c) = 0 and D²F(T_r, T_r) = 0 **exactly** (each hull integrates; the straight lines in θ lie in the hull). ✓
- Cross terms D²F(T_c, T_r): 320 of 441 pairs nonzero — T_c + T_r is not the tangent of one manifold.
- rank of B on Sym²(Def): 47 (float control agrees); on Sym²(R): 30; on T × R: 44.
- Generic u ∈ Def: rank of B(u,·) = 45.

## C. The stabilizer of the point in G_ext (exact)

Order **1024** = (16 × 16 product relabellings fixing each factor up to phases) × {conjugation with the column swap 1↔3 in each factor} × {transpose}; no factor exchange (z ≠ w). 112 conjugacy classes.
Representation on Def: commutant dimension 18, trivial-isotypic dimension 2 (the two circle directions of the stratum).
Representation on R: commutant dimension 5, no trivial part; isotypic sectors of dimensions **8, 8, 4, 2, 1** (by exact eigenspaces of the class sums).
Representation on coker DF of the transpose-free subgroup (order 512; the transpose exchanges the row- and column-orthogonality presentations of the constraints, whose cokernels are identified through the base point): trivial-isotypic dimension 1, commutant dimension 45 (104 conjugacy classes); the image of B, a 47-dimensional invariant subspace, has trivial-isotypic dimension 1 and commutant dimension 27. Control: the action preserves im DF (full basis, eight elements).

## D. Every Diţă orientation through the point

Exact search over all partitions of the 16 columns into four 4-blocks on which the rows fall into four proportionality classes of four (and the transpose for row hulls): five column-block structures and five row-block structures pass the proportionality test; four of each are exact Diţă factorizations with flat unitary factors (one fails the rank-one condition):
- the fixed pairing (blocks by `c`, classes by `b`): the A35 hulls T_c, T_r;
- the swapped pairing (blocks by `d`, classes by `a`): T_c^sw, T_r^sw, each 14-dim, each adding 3 to T; together 6;
- a mixed regrouping (blocks `{(c,d): c ≡ ε, d ≡ ε'}`-type, `(0,2,9,11)…`): 14-dim each, adding 6 to T;
- the **parity regrouping** (blocks `(0,2,8,10)…`, rows `(0,2,8,10)…`): its five factors are **real** 4×4 Hadamards (defect 3 each, three Fourier circles through each), so it carries 3⁵ = 243 hulls in the column form and 243 in the row form, each 14-dim; their tangents together span 24 mod gauge and add 10 to T.

**Hull count through the point: 492**, each of tangent dimension 14 mod gauge; control: every hull tangent lies in ker DF and D²F vanishes **exactly** on every hull (492 of 492).

**Span of all hull tangents mod gauge: 49 = dim Def.** Every first-order deformation at the certified point is a sum of tangents of Diţă hulls through the point. Relative to all orientations through the point the residual quotient is zero; the 23 residual directions of A35 are explained by orientations the fixed pairing does not include (swapped: 6, mixed: 6, parity: 10 — with overlaps; 23 in all).

## E. Census of R's stabilizer sectors by fate (relative to the fixed-pairing hulls T)

| sector | dim | B on Sym²(sector) | couples to T | second order |
| --- | --- | --- | --- | --- |
| 0 | 8 | not isotropic | yes | **quadratically obstructed**: exact certificate `B(v,v) ∉ span{B(v,T), B(T,T)}` at generic v |
| 1 | 8 | not isotropic | yes | **quadratically obstructed**: same certificate |
| 2 | 4 | isotropic (B(V,V)=0) | yes | **extendable**: explicit correction t ∈ T_r with B(v+t, v+t) = 0 (t_c = 0) |
| 3 | 2 | isotropic | yes | extendable, same |
| 4 | 1 | isotropic | yes | extendable, same |

**Absorption by the hulls through the point** (a class of R is absorbed by a hull h iff it lies in (T + T_h)/T):
- the images of the hulls in R span R (23 of 23); 200 distinct absorbed subspaces; image dimensions: fixed pairing 0, swapped 3, mixed 6, parity hulls 3 to 8 (mostly 5 to 7);
- sector 4 (dim 1) and sector 3 (dim 2) lie in **every one of the 486 parity hulls** (and in no other): they are hull directions;
- sector 2 (dim 4) lies in no single hull; its overlap with each orientation family's span is 2; it is second-order extendable (§E) — whether its extended directions lie in a hull is §F2;
- sector 0 (dim 8) lies in no hull; its largest single-hull overlap is 4, with the mixed orientation (the mixed family's span meets it in 4); generic directions are quadratically obstructed;
- sector 1 (dim 8) lies in no hull; its largest single-hull overlap is 5, with a parity hull (the parity family's span meets it in 5); generic directions are quadratically obstructed.
Each sector is an irreducible Q-representation of the stabilizer (commutant dimension 5 = five constituents of multiplicity one), so the absorbed parts of sectors 0, 1, 2 are proper, non-invariant subspaces whose stabilizer orbits cover the absorbed directions.

**Second-order cone against the hull union.** Q = {u ∈ Def : B(u,u) = 0} contains every hull tangent. At random rational points u of a 4×4 hull the tangent space T_u Q = {v : B(u,v) = 0} has dimension 17 to 21 against the hull's 14: no hull is a component of Q. The space of quadrics on Def vanishing on all 492 hull tangents has dimension **527** (computed over F_p, p = 2²⁵ − 39, incrementally over all 492 hulls; an upper bound for the count over Q), and the 47 B-quadrics lie inside it. So Q is much larger than the quadratic closure of the hull union at second order.

**Straight lines outside every 4×4 hull.** For generic directions of sectors 2, 3 and 4, the second-order extension w = v + t found by the linear solve is an **exact straight line**: F(εw) ≡ 0 for all real ε, verified exactly (every level-set sum of the c_k over k ↦ w_ik − w_jk vanishes, all 120 pairs), and w lies in none of the 492 hull tangents. A numerical Gauss–Newton continuation confirms |F(εw)| ≈ 4·10⁻¹⁵ with zero correction for ε up to 0.4, while the same procedure needs corrections of order 0.1–2.6 on hull, generic and obstructed controls. The direction W (sector 2, integer form, largest entry 10) is supported on the even row-blocks a ∈ {0,2} and even column-blocks c ∈ {0,2} and repeats one 4×4 pattern M there, with M a gauge plus the Fourier circle direction of the inner factor: it deforms the inner factor F₄(w) along its own family in the four blocks where the outer factor F₄(z) is constant, and leaves the other blocks fixed. Its affine family A_w (all directions constant on W's level sets) has dimension 5 mod gauge, meets no 4×4 fixed-pairing tangent, and meets the parity family's span in 3, the swapped in 2 (column) / 1 (row).

**An exact realizable point in no relabelled 4×4 Diţă hull.** P = SIG ∘ u^W with u = (60+i)/(60−i) (Gaussian-rational unit, angle 1.9°; largest entry phase 19.1°) is an exact unimodular Hadamard matrix (verified), of defect **33**, at which the full search over every partition of the 16 columns into 4-blocks (all relabellings of the column construction) and the same for rows returns one proportionality candidate per form and **zero exact 4×4 Diţă factorizations**; its fixed-pairing cross-ratio identity is violated at 176 of 576 sites. The same holds at P₁ = SIG ∘ u₅^W (u₅ = (3+4i)/5; defect 33) and P₂ = SIG ∘ u₅^{2W} (defect 37). These are the "stronger future counterexample" A35 named — an exact realizable point near the stratum with zero 4×4 membership signature under every relabelling — and they answer A35's open modulus **in the negative for the 4×4 construction**.

**Diţă factorizations of other sizes (exact search over all block structures).** With m column blocks of n columns and n row classes of m rows, m·n = 16:

| point | 2×8 (col / row) | 8×2 (col / row) | 4×4 (col / row) |
| --- | --- | --- | --- |
| SIG | 3 / 3 orientations, all exact | 3 / 3 orientations, 2 / 2 exact | 5 / 5 orientations, 4 / 4 exact |
| P (near, defect 33) | **1 / 1, exact** | 1 / 1, none exact | 1 / 1, none exact |
| P₁ (defect 33) | **1 / 1, exact** | 1 / 1, none exact | 1 / 1, none exact |

So the straight-line family through the certified point that leaves every 4×4 hull is Diţă's construction at factor size 2×8: a 2×2 outer factor, two 8×8 inner factors and a 2×8 twist. The direction W is exactly that: the inner factor F₄(w) deformed along its own circle in the four blocks where the 2×2 outer restriction of F₄(z) is constant. The Diţă hierarchy over the factorizations of 16 (2·8, 4·4, 8·2, and their nestings) is the object the open modulus should be posed for.

## F. Reading

**Census of the stabilizer-invariant sectors of R = ker DF / (gauge + T), T the two fixed-pairing 4×4 hulls (dims 8, 8, 4, 2, 1):**

| sector | dim | fate |
| --- | --- | --- |
| 0 | 8 | **quadratically obstructed** at generic directions (exact certificate: no t ∈ T makes B(v+t, v+t) = 0); a 4-dimensional non-invariant subspace is absorbed by the mixed-regrouping 4×4 hulls |
| 1 | 8 | **quadratically obstructed** at generic directions (same certificate); a 5-dimensional non-invariant subspace is absorbed by parity 4×4 hulls |
| 2 | 4 | **unobstructed to second order** with an explicit row-hull correction; in no single 4×4 hull; its extensions are exact straight lines lying in the **2×8 Diţă hulls** through the point |
| 3 | 2 | in every one of the 486 parity 4×4 hulls; also carries exact straight lines outside every 4×4 hull (2×8 hulls) |
| 4 | 1 | in every parity 4×4 hull; also carries exact straight lines outside every 4×4 hull (2×8 hulls) |

None of the sectors is "mixed-coupling only": the isotropic sectors 2, 3, 4 all couple to T (B(V,T) ≠ 0) and are extendable; the non-isotropic sectors 0, 1 are obstructed. No sector is unresolved at second order relative to T.

**Exact statements the measurement supports for the next freeze:**
1. (first order) The tangents at the certified rational point of the 4×4 Diţă hulls through it — fixed, swapped, mixed and parity orientations, 492 hulls of dimension 14 — span the 49-dimensional defect space; the A35 residual is explained by orientations the fixed pairing omits.
2. (second order, obstruction) For generic directions of the two 8-dimensional sectors, no curve of Hadamard matrices through the point has tangent in v + T: the fixed-pairing hulls cannot be corrected to reach them, by an exact cokernel certificate.
3. (second order, families) The 4-, 2- and 1-dimensional sectors extend; their extensions are exact straight lines, and the exact point P on one of them is realizable, off the stratum (176 cross-ratio violations), of defect 33, and lies in **no relabelled 4×4 Diţă hull of either form** — the counterexample A35 named — while lying in a 2×8 Diţă hull.
4. (structure) The open modulus is answered negatively for the 4×4 construction and re-posed for the Diţă hierarchy: whether every realizable class near the stratum lies in a Diţă hull of some factorization of 16.

**What was not found.** No clean quadratic coupling law: B has rank 47 on Sym²(Def), its image has commutant dimension 27 under the transpose-free stabilizer and is not a small number of sectors; the couplings between residual sectors and T are dense (every residual sector couples to T). The mode-coupling analogy gains no support from this point's tensor.

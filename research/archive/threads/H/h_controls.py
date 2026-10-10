"""Thread H exact controls: field-neutral Naimark transport e_x(s) = r(D(U(A(s, rho_R)))).

Exact arithmetic only (sympy Rational / sqrt(3) / I). Written arguments are printed as NOTE and are
not counted as checks. Run: PYTHONDONTWRITEBYTECODE=1 python3 h_controls.py
"""
import itertools
import sympy as sp
from sympy import Rational as Q, sqrt, I, Matrix, eye, zeros, simplify, symbols

CHECKS = 0
NOTES = 0


def check(name, cond):
    global CHECKS
    if isinstance(cond, sp.logic.boolalg.BooleanAtom):
        cond = bool(cond)
    if cond is not True:
        raise SystemExit(f"FAIL {name}: {cond}")
    CHECKS += 1
    print(f"  ok  {name}")


def note(text):
    global NOTES
    NOTES += 1
    print(f"  NOTE {text}")


# ----------------------------------------------------------------------------------------------
print("== BALL: what 'sharp normalization' means on the 3-ball (target of lorentz_of_effects NGB:105)")
a, b0, b1, b2, beta = symbols("a b0 b1 b2 beta", real=True)
x = Matrix([Q(2, 3), Q(1, 3), Q(2, 3)])          # a rational point of the unit sphere
check("BALL.x_on_sphere", (x.T * x)[0] == 1)
# an affine e(r) = a + b.r is an effect on the ball iff a - |b| >= 0 and a + |b| <= 1.
# certain at the unit x:  1 = a + b.x <= a + |b| <= 1 forces b.x = |b|, i.e. b = beta x (Cauchy-Schwarz).
e_cert = lambda r, bt: 1 - bt + bt * (x.T * r)[0]
check("BALL.certain_at_x", simplify(e_cert(x, beta) - 1) == 0)
check("BALL.value_at_antipode_is_1-2beta", simplify(e_cert(-x, beta) - (1 - 2 * beta)) == 0)
# effect condition min = 1 - 2 beta >= 0  => beta <= 1/2 ; sharp (e(-x) = 0, i.e. {x,-x} perfectly
# distinguishable by (e, 1-e), KF:154) <=> beta = 1/2 <=> e = (1 + x.r)/2
sol = sp.solve(sp.Eq(e_cert(-x, beta), 0), beta)
check("BALL.sharp_iff_beta_half", sol == [Q(1, 2)])
r = Matrix(symbols("r0 r1 r2", real=True))
check("BALL.sharp_is_directional", simplify(e_cert(r, Q(1, 2)) - (1 + (x.T * r)[0]) / 2) == 0)
note("SEC alone gives some beta in (0,1/2]; lorentz_of_effects consumes beta = 1/2 for every unit b. "
     "Field-neutrally, 'sharp' = the pair (e, u-e) perfectly distinguishes x from a second state "
     "(PerfectlyDistinguishable KF:154 with iota = Fin 2); on the ball the second state is forced to be -x.")

# ----------------------------------------------------------------------------------------------
print("== CL: classical composite Delta_2 (x) Delta_2 = Delta_4 (min = max); U = all permutations")
states = list(itertools.product(range(2), range(2)))          # (system s, register k)
effects = set()
for perm in itertools.permutations(states):
    P = dict(zip(states, perm))
    for k in range(2):
        # attach register seed k0 = 0, apply U = P, read register k, discard system
        c = tuple(1 if P[(s, 0)][1] == k else 0 for s in range(2))
        effects.add(c)
check("CL.only_01_response_vectors", effects == {(0, 0), (0, 1), (1, 0), (1, 1)})
check("CL.classical_sharp_effects_reached", (1, 0) in effects and (0, 1) in effects)
note("Classical control passes: the classical composite manufactures nothing beyond 0/1 response "
     "effects (Resp of the ontic carrier), and does reach the simplex's own sharp vertex readouts. Landed "
     "typing: RevReal Equivalence.lean:157 (V x Hid, step bijection, init), marg FiniteEntropy.lean:130, "
     "RevReal.law Equivalence.lean:180, hiddenExt PassiveQuotient.lean:498.")

# ----------------------------------------------------------------------------------------------
print("== HYB: ball (x) classical register = L3 (+) L3 (canonical: one factor a simplex)")
# cone L3 = {(t, v): |v| <= t}; composite cone = L3 (+) L3 in R^8; register readout = block weight t_k.
inL = lambda w: w[0] >= 0 and w[0] ** 2 - (w[1] ** 2 + w[2] ** 2 + w[3] ** 2) >= 0
inC = lambda W: inL(W[0:4]) and inL(W[4:8])
c3, s3 = Q(3, 5), Q(4, 5)
Mix = Matrix([[c3, -s3], [s3, c3]]).applyfunc(lambda z: z)
MixFull = sp.kronecker_product(Mix, eye(4))     # rotation between the two blocks
pure_r0 = Matrix([1, 0, 0, 1, 0, 0, 0, 0])      # pure state z in block 0
pure_r1 = Matrix([0, 0, 0, 0, 1, 0, 0, 1])
check("HYB.mixing_map_leaves_cone", inC(pure_r0) and inC(pure_r1) and not inC(MixFull * pure_r1))
# block-diagonal and block-swapping automorphisms: transported register readout is constant
def rot_rat(axis, c, s):
    R = eye(3)
    i, j = [k for k in range(3) if k != axis]
    R[i, i], R[i, j], R[j, i], R[j, j] = c, -s, s, c
    return R
g0 = sp.diag(1, rot_rat(2, Q(3, 5), Q(4, 5)))
g1 = sp.diag(1, rot_rat(0, Q(5, 13), Q(12, 13)))
blockdiag = sp.diag(g0, g1)
blockswap = sp.kronecker_product(Matrix([[0, 1], [1, 0]]), eye(4)) * blockdiag
sv = symbols("s1 s2 s3", real=True)
s_state = Matrix([1, *sv])
attach0 = lambda s: Matrix([*s, 0, 0, 0, 0])                     # A(s, delta_0)
readk = lambda W, k: W[4 * k]                                     # r_k o D: block weight
for nm, U in (("blockdiag", blockdiag), ("blockswap", blockswap)):
    vals = [simplify(readk(U * attach0(s_state), k)) for k in range(2)]
    check(f"HYB.transport_constant_{nm}", all(v.is_number for v in vals) and set(vals) <= {0, 1})
note("Written (cone-decomposition): extreme rays of L3 (+) L3 are those of the two blocks, two connected "
     "spheres; an automorphism permutes extreme rays homeomorphically, so maps each block onto a block. "
     "Hence every reversible U on ball (x) Delta_n is a block permutation of local automorphisms and "
     "r_k(D(U(A(s,delta_k0)))) is constant in s: transport through a classical register is vacuous on "
     "every body whose cone is indecomposable (ball, square, polygon, bidisk).")

# ----------------------------------------------------------------------------------------------
print("== SIC: ontic-level Naimark on a fixed finite realization (realization dependence)")
r3 = sqrt(3)
avec = [Matrix(v) / r3 for v in ([1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1])]
check("SIC.tetrahedron", all(simplify((v.T * v)[0] - 1) == 0 for v in avec)
      and simplify(sum(avec, zeros(3, 1))) == zeros(3, 1))
z = Matrix([0, 0, 1])
for t in (1, Q(1, 2)):
    p = lambda rr: [(1 + t * (ai.T * rr)[0]) / 4 for ai in avec]
    # coefficients of the sharp seed (1 + b.r)/2 as a response c.p(r): c_i = (1 + (3/t) b.a_i)/2
    for bname, bvec in (("z", z), ("a1", avec[0])):
        c = [simplify((1 + (3 / t) * (bvec.T * ai)[0]) / 2) for ai in avec]
        # verify identity c.p(r) = (1 + b.r)/2 symbolically
        ok = simplify(sum(ci * pi for ci, pi in zip(c, p(r))) - (1 + (bvec.T * r)[0]) / 2) == 0
        check(f"SIC(t={t}).seed_{bname}_coefficients_identity", ok)
        check(f"SIC(t={t}).seed_{bname}_not_a_response",
              any(bool((ci - 1).is_positive) or bool(ci.is_negative) for ci in c))
    if t == 1:
        cz = [simplify((1 + 3 * (z.T * ai)[0]) / 2) for ai in avec]
        check("SIC.matches_Main540_value", any(simplify(ci - (Q(1, 2) + r3 / 2)) == 0 for ci in cz)
              and all(not bool((ci - (Q(1, 2) + r3 / 2)).is_positive) for ci in cz))
        # zeros of p_i on the ball are exactly r = -a_i; best response certain there: c = 1 - delta_i
        for i, ai in enumerate(avec):
            pv = p(-ai)
            check(f"SIC.tight.p{i}_vanishes_at_-a{i}", simplify(pv[i]) == 0)
            e_val_opp = simplify(1 - p(ai)[i])        # value of 1 - p_i at the antipode +a_i
            check(f"SIC.tight.best_response_beta_quarter_{i}", e_val_opp == Q(1, 2))
        note("Tight SIC: only the 4 points -a_i are certain for a non-unit response; the best such effect "
             "1 - p_i has beta = 1/4 (value 1/2 at the antipode), never 1/2: no sharp effect at ontic level.")
    else:
        # loose: p_i >= (1 - 1/2)/4 = 1/8 on the whole ball (|a_i.r| <= 1)
        check("SIC.loose.min_p_is_1/8", (1 - t) / 4 == Q(1, 8))
        note("Loose SIC (t=1/2): every p_i >= 1/8 on the ball, so by response_eq_one_forces (KF:899) no "
             "non-unit response effect is certain anywhere; ontic Naimark supports no boundary state.")
note("Body-level transport (seed + Aut(ball)) gives the same family for both realizations; the ontic-level "
     "transport (classical composite) gives 4 unsharp supports (tight) or none (loose): realization-dependent.")

# ----------------------------------------------------------------------------------------------
print("== MM: composite rules for two Bloch balls (min / QM / max), exact over Q(i)")
s0 = eye(2)
sx = Matrix([[0, 1], [1, 0]])
sy = Matrix([[0, -I], [I, 0]])
sz = Matrix([[1, 0], [0, -1]])
paulis = [s0, sx, sy, sz]
kron = sp.kronecker_product


def pt2(M):   # partial transpose on qubit 2
    R = zeros(4, 4)
    for i1, j1, i2, j2 in itertools.product(range(2), repeat=4):
        R[2 * i1 + i2, 2 * j1 + j2] = M[2 * i1 + j2, 2 * j1 + i2]
    return R


def min_eig(M):
    return min(simplify(ev) for ev in M.eigenvals().keys())


ket = lambda *amps: Matrix(amps)
k0, k1 = ket(1, 0), ket(0, 1)
kp, km = (k0 + k1) / sqrt(2), (k0 - k1) / sqrt(2)
kyp, kym = (k0 + I * k1) / sqrt(2), (k0 - I * k1) / sqrt(2)
six = [k0, k1, kp, km, kyp, kym]
proj = lambda v: v * v.H
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
SWAP = Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
ZZ = sp.diag(sp.exp(-I * sp.pi / 4), sp.exp(I * sp.pi / 4), sp.exp(I * sp.pi / 4), sp.exp(-I * sp.pi / 4))

bell = proj((kron(k0, k0) + kron(k1, k1)) / sqrt(2))
check("MM.Bell_in_QM", min_eig(bell) >= 0)
check("MM.Bell_not_in_min(PPT)", min_eig(pt2(bell)) == Q(-1, 2))
W = SWAP / 2
check("MM.SWAP/2_trace_one", W.trace() == 1)
uu, vv = symbols("u1:4", real=True), symbols("v1:4", real=True)
# Pauli coordinates T_ij = tr(W s_i (x) s_j); product-effect value (1,u)T(1,v)/4 >= 0 for unit u, v
T = Matrix(4, 4, lambda i, j: (W * kron(paulis[i], paulis[j])).trace())
check("MM.SWAP/2_Pauli_coords_identity", T == eye(4))
note("SWAP/2 has Pauli coordinates T = I, so its product-effect values are (1 + u.v)/4 >= 0 for unit u, v "
     "(Cauchy-Schwarz): it lies in the max composite.")
check("MM.SWAP/2_not_in_QM", min_eig(W) == Q(-1, 2))


def prod_min(M):
    return min(simplify((kron(u, v).H * M * kron(u, v))[0]) for u in six for v in six)


# max elements: partial transposes of pure states are positive on products (<ab|rho^TB|ab> = <a b*|rho|a b*>)
W2 = pt2(proj((kron(kp, k0) + kron(km, k1)) / sqrt(2)))
check("MM.W2_trace_one_not_QM", W2.trace() == 1 and min_eig(W2) < 0)
for nm, U, Wm in (("CNOT", CNOT, W), ("ZZ(pi/4)", ZZ, W2)):
    plus_plus = proj(kron(kp, k0)) if nm == "CNOT" else proj(kron(kp, kp))
    img = simplify(U * plus_plus * U.H)
    check(f"MM.{nm}_product_to_entangled(leaves_min)", min_eig(pt2(img)) < 0)
    imgW = simplify(U * Wm * U.H)
    check(f"MM.{nm}_moves_max_element_outside_max", prod_min(imgW) < 0)
    check(f"MM.{nm}_maps_products_into_QM_subset_max", min_eig(img) >= 0)
check("MM.SWAP_preserves_min_max_QM(products->products)",
      all(simplify(SWAP * kron(u, v) - kron(v, u)) == zeros(4, 1) for u in six for v in six))
note("CNOT and the interacting ZZ member preserve neither the min nor the max composite of two Bloch balls; "
     "they preserve QM. NB-1's hypothesis (G, G^-1 send PRODUCT states into the max cone, NGB header) is "
     "weaker than preserving any composite and is met by CNOT. Literature (citation, theorem number "
     "unverified): de la Torre-Masanes-Short-Mueller PRL 109 090403 (2012): for locally tomographic d-ball "
     "composites a continuous interacting reversible dynamics forces d=3 and the QM composite.")

# transport of the register seed: product effect u (x) r_seed, r_seed = (1 + z.r)/2 = |0><0|
P0 = proj(k0)
sv1, sv2, sv3 = symbols("x1 x2 x3", real=True)
rho_s = (s0 + sv1 * sx + sv2 * sy + sv3 * sz) / 2
rhoR = P0
read = lambda M: simplify((kron(s0, P0) * M).trace())          # u_S (x) r on register = D then r
readS = lambda M: simplify((kron(P0, s0) * M).trace())
# SWAP transport (register first, system second is irrelevant): e(s) = r(s)
e_swap = read(SWAP * kron(rho_s, rhoR) * SWAP.H)
check("MM.SWAP_transport_relocates_seed", simplify(e_swap - (1 + sv3) / 2) == 0)
# Naimark with CNOT (system control, register target): e(s) = <0|rho_s|0> = (1 + x3)/2
e_cnot = read(CNOT * kron(rho_s, rhoR) * CNOT.H)
check("MM.CNOT_Naimark_equals_seed", simplify(e_cnot - (1 + sv3) / 2) == 0)
# with a local rotation g first: Hadamard sends z-readout to x-readout
H = Matrix([[1, 1], [1, -1]]) / sqrt(2)
e_cnot_H = read(CNOT * kron(H, s0) * kron(rho_s, rhoR) * kron(H, s0).H * CNOT.H)
check("MM.CNOT_after_local_g_equals_seed_o_g", simplify(e_cnot_H - (1 + sv1) / 2) == 0)
note("Entangling Naimark transport of the sharp register readout yields exactly the seed composed with the "
     "local reversible map: the same family as SWAP-relocation + local orbit. The composite rule is "
     "irrelevant to the SHARP family; only the seed and the local group matter.")

# ----------------------------------------------------------------------------------------------
print("== ORB: seed (1 + z.r)/2 transported by the ball's reversible maps (ball3Drive: rot about axis 2, cyc3)")
rz = rot_rat(2, Q(3, 5), Q(4, 5))
cyc = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])        # cyc3: (v2, v0, v1)
rx = cyc.T * rz * cyc
check("ORB.conjugate_is_rotation_about_other_axis", (rx * cyc.T * z - cyc.T * z) == zeros(3, 1)
      and rx != rz and simplify(rx.T * rx) == eye(3))
# rational target b and a rational rotation g with g z = b (product of two reflections)
bt = Matrix([Q(2, 3), Q(1, 3), Q(2, 3)])
refl = lambda n: eye(3) - 2 * n * n.T / (n.T * n)[0]
g = refl(bt + z) * refl(z)   # reflection through z, then through b + z: a rotation with g z = b
check("ORB.g_orthogonal_det1", simplify(g.T * g) == eye(3) and g.det() == 1)
check("ORB.g_maps_z_to_b", simplify(g * z - bt) == zeros(3, 1))
seed = lambda rr: (1 + (z.T * rr)[0]) / 2
transported = lambda rr: seed(g.T * rr)       # e o g^{-1}
check("ORB.transported_is_directional_b", simplify(transported(r) - (1 + (bt.T * r)[0]) / 2) == 0)
check("ORB.transported_sharp", transported(bt) == 1 and transported(-bt) == 0)
# the same target reached by a WORD in the drive's own members: flow = rotation about axis 2 (rotFun KF:351),
# J = cyc3 (KF:425); J flow(theta) J^-1 rotates about J z = axis 0; b = R_z(phi) R_x(theta) z (ZXZ Euler)
r5 = sqrt(5)
Rz = lambda c_, s_: rot_rat(2, c_, s_)
Jm = cyc
Rx_word = lambda c_, s_: Jm * Rz(c_, s_) * Jm.T
check("ORB.J_conjugate_axis_is_axis0", Jm * z == Matrix([1, 0, 0]))
gw = Rz(-1 / r5, 2 / r5) * Rx_word(Q(2, 3), r5 / 3)
check("ORB.word_orthogonal", simplify(gw.T * gw) == eye(3))
check("ORB.word_maps_z_to_b", simplify(gw * z - bt) == zeros(3, 1))
check("ORB.word_transport_directional", simplify(seed(gw.T * r) - (1 + (bt.T * r)[0]) / 2) == 0)
note("Written: rotations about axis 2 (flow) and their cyc3-conjugates generate SO(3) (Euler angles), "
     "transitive on the sphere, so the drive's generated group carries one sharp seed to every (1+b.r)/2. "
     "This is B9 (Thread F) with a singleton-face sharp seed; no composite is used.")

# ----------------------------------------------------------------------------------------------
print("== SQ: gbit / square [-1,1]^2 control")
sq_vertices = [Matrix([i, j]) for i in (-1, 1) for j in (-1, 1)]
bdir = Matrix([Q(3, 5), Q(4, 5)])
check("SQ.directional_family_not_effects", (1 + (bdir.T * Matrix([1, 1]))[0]) / 2 == Q(6, 5))
# automorphisms: integer matrices with entries in {-1,0,1} preserving the vertex set
auts = []
for ent in itertools.product((-1, 0, 1), repeat=4):
    M = Matrix(2, 2, ent)
    if M.det() != 0 and {tuple(M * v) for v in sq_vertices} == {tuple(v) for v in sq_vertices}:
        auts.append(M)
check("SQ.Aut_is_D4_order8", len(auts) == 8)
# exhaustive over AFFINE maps: an affine automorphism permutes the 4 vertices and is fixed by 3 of them
aff = 0
for perm in itertools.permutations(sq_vertices):
    A_ = Matrix.hstack(perm[1] - perm[0], perm[2] - perm[0]) * Matrix.hstack(sq_vertices[1] - sq_vertices[0],
                                                                            sq_vertices[2] - sq_vertices[0]).inv()
    t_ = perm[0] - A_ * sq_vertices[0]
    if A_ * sq_vertices[3] + t_ == perm[3]:
        aff += 1
check("SQ.affine_Aut_order8_by_vertex_permutations", aff == 8)
vseed = lambda rr: (2 + rr[0] + rr[1]) / 4            # sharp singleton-face vertex seed
check("SQ.vertex_seed_sharp_singleton", vseed(Matrix([1, 1])) == 1 and vseed(Matrix([-1, -1])) == 0
      and all(vseed(v) < 1 for v in sq_vertices if tuple(v) != (1, 1)))
mid = Matrix([1, 0])
check("SQ.vertex_seed_orbit_misses_edge_midpoint", max(vseed(M.T * mid) for M in auts) == Q(3, 4))
eseed = lambda rr: (1 + rr[0]) / 2                     # squareEdgeEffect KF:716
check("SQ.edge_seed_orbit_covers_boundary",
      all(max(eseed(M.T * pt) for M in auts) == 1
          for pt in [Matrix([1, Q(k, 7)]) for k in range(-7, 8)] + [Matrix([Q(k, 7), -1]) for k in range(-7, 8)]))
check("SQ.edge_seed_face_not_singleton", eseed(Matrix([1, 1])) == 1 and eseed(Matrix([1, -1])) == 1)
note("Square: Aut finite (D4) so no drive (F: B5) and every composite of squares (min: polytope with 16 "
     "product vertices; max: polyhedral) has finite Aut: no continuous U. A singleton-face sharp seed covers "
     "only the 4 vertices (edge midpoints get 3/4); an edge seed covers the boundary but with edge faces (SF "
     "fails, not_singletonFaces_square KF:726); the directional family is not even an effect family. "
     "The failing step is COVER: G x0 = extreme boundary fails (finite G; non-extreme boundary points). "
     "The ball passes it: all boundary points extreme, SO(3) from the drive transitive.")

# ----------------------------------------------------------------------------------------------
print("== FUNCT: without pullback-closure the native seed alone does not give SEC on the ball")
xb = Matrix([1, 0, 0])                                   # isBoundaryState_ball3 KF:1080
Integer1 = sp.Integer(1)
vals = [Integer1, seed(xb), 1 - seed(xb)]
check("FUNCT.seed_and_complement_half_at_(1,0,0)", vals[1] == Q(1, 2) and vals[2] == Q(1, 2))
note("{unit, seed, 1-seed} is closed under complement but not under pullback; at the boundary state "
     "(1,0,0) the only certain member is the unit, which is not proper: SEC fails (as not_kInf1_ball3_unit "
     "KF:1089). Closing under pullback by the drive's group restores every (1+b.r)/2 (ORB.word_*).")

print(f"OK -- {CHECKS} checks, {NOTES} written notes")

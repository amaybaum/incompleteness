"""Thread M -- exact checks for the full-equivalence dependency audit (read-only; certified main 6d0abf6b).

Exact arithmetic only: sympy Rational / Gaussian rationals (sympy.I), no floats.
Sections:
  N  normalization ellipsoid -> ball3 (trap 1): the affine map, transport of seed / drive / G-AUT / V4' family,
     coordinate-dependence of the Lorentz consumer, residual O(3) freedom, cross-copy alignment.
  D  dimension (trap 2): drive gives d >= 3 only; d = 4 ball with a drive does not deliver the NB-1 input
     (the loop), literal transitivity does; lorentz_of_effects instantiation is dimension-free.
  S  drive sourcing (trap 3 / G-AUT): the current substratum (monomial) group fails the off-axis clause.
  Q  reverse implication in the qubit model: every forward premise row, checked separately.
  X  scope: forward premises stated for an unscoped body FAIL in QM (qutrit, dilated visible readout).
Run:  PYTHONDONTWRITEBYTECODE=1 python3 m_checks.py
"""
import itertools
import sympy as sp
from sympy import Rational as R, Matrix, I, eye, zeros, sqrt

CHECKS = []
NOTES = []


def check(name, cond):
    cond = bool(cond)
    CHECKS.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


def note(s):
    NOTES.append(s)
    print("NOTE " + s)


def simp(M):
    return M.applyfunc(lambda z: sp.nsimplify(sp.expand(sp.simplify(z))))


def quat_rot(a, b, c, d):
    """Rational rotation matrix from an integer quaternion (exact, det 1)."""
    n = a * a + b * b + c * c + d * d
    M = Matrix([
        [a*a + b*b - c*c - d*d, 2*(b*c - a*d), 2*(b*d + a*c)],
        [2*(b*c + a*d), a*a - b*b + c*c - d*d, 2*(c*d - a*b)],
        [2*(b*d - a*c), 2*(c*d + a*b), a*a - b*b - c*c + d*d]])
    return M / n


def norm2(v):
    return sum(x * x for x in v)


# Pythagorean rational unit vectors in R^3
UNITS = [Matrix([R(3, 5), R(4, 5), 0]), Matrix([0, R(3, 5), R(-4, 5)]), Matrix([R(2, 3), R(1, 3), R(2, 3)]),
         Matrix([R(-2, 7), R(3, 7), R(6, 7)]), Matrix([0, 0, 1]), Matrix([1, 0, 0])]
for u in UNITS:
    assert norm2(u) == 1
ROTS = [quat_rot(1, 1, 0, 0), quat_rot(1, 2, 3, 4), quat_rot(2, 0, 1, 1), quat_rot(3, 1, -1, 2), eye(3)]
for Rm in ROTS:
    assert simp(Rm.T * Rm) == eye(3) and Rm.det() == 1
ez = Matrix([0, 0, 1])

print("== N: normalization ellipsoid -> ball3 ==")
A = Matrix([[2, 1, 0], [0, 1, 0], [1, 0, 3]])
c = Matrix([1, -1, 2])
Ai = A.inv()
check("N0 A invertible, not orthogonal (ellipsoid is not a ball)", A.det() != 0 and A.T * A != eye(3))


def in_E(x):
    return norm2(Ai * (x - c)) <= 1


def T(x):          # the normalizing affine map Omega_E -> ball3
    return Ai * (x - c)


def Tinv(y):
    return c + A * y


def g_E(Rm):       # a member of the conjugated drive group on Omega_E, as (linear, translation)
    L = A * Rm * Ai
    return L, c - L * c


def apply(g, x):
    return g[0] * x + g[1]


def ginv(g):
    Li = g[0].inv()
    return Li, -Li * g[1]


# effects as (const, linear covector) : x -> const + lin . x
def eff_apply(e, x):
    return e[0] + (e[1].T * x)[0]


def eff_comp(e, g):  # e o g  for affine g = (L, b)
    return (e[0] + (e[1].T * g[1])[0], g[0].T * e[1])


def ballEffect(b):
    return (R(1, 2), b / 2)


r_E = (R(1, 2) - (ez.T * Ai * c)[0] / 2, Ai.T * ez / 2)   # (1 + ez . A^{-1}(x - c))/2
Tg = (Ai, -Ai * c)
Tinvg = (A, c)
# N1: T maps the boundary of Omega_E onto the unit sphere, both directions, on samples
ok = all(norm2(T(Tinv(b))) == 1 and in_E(Tinv(b)) and T(Tinv(b)) == b for b in UNITS)
check("N1 T(c + A b) = b on unit b; T^{-1}(ball3) = Omega_E on samples", ok)
# N2: seed transported by T is ballEffect(e_z)
e2 = eff_comp(r_E, Tinvg)
check("N2 r_E o T^{-1} = ballEffect(e_z) (coefficients exact)", simp(e2[1]) == ez / 2 and sp.simplify(e2[0]) == R(1, 2))
# N3: T g T^{-1} = R for every member
ok = True
for Rm in ROTS:
    g = g_E(Rm)
    conj = (Ai * g[0] * A, Ai * (g[0] * c + g[1]) - Ai * c)
    ok &= simp(conj[0]) == Rm and simp(conj[1]) == zeros(3, 1)
check("N3 T g_R T^{-1} = R exactly (linear part R, translation 0)", ok)
# N4: transport commutes with normalization: (r_E o g^{-1}) o T^{-1} = ballEffect(R e_z)
ok = True
for Rm in ROTS:
    g = g_E(Rm)
    f = eff_comp(eff_comp(r_E, ginv(g)), Tinvg)
    ok &= simp(f[1]) == simp(Rm * ez / 2) and sp.simplify(f[0] - R(1, 2)) == 0
check("N4 (r_E o g_R^{-1}) o T^{-1} = ballEffect(R e_z) for all sampled R", ok)
# N5: G-AUT transports: g_R and g_R^{-1} map boundary samples of Omega_E onto boundary samples
ok = all(norm2(T(apply(g_E(Rm), Tinv(b)))) == 1 and norm2(T(apply(ginv(g_E(Rm)), Tinv(b)))) == 1
         for Rm in ROTS for b in UNITS)
check("N5 PreservesBody transports along T (g and g^{-1} keep |T x| = 1)", ok)
# N6: boundary-state extension is affine-covariant: T(x + e(x - y)) = Tx + e(Tx - Ty)
eps = R(1, 7)
ok = all(simp(T(Tinv(b) + eps * (Tinv(b) - c)) - (b + eps * (b - T(c)))) == zeros(3, 1) for b in UNITS)
check("N6 IsBoundaryState's extension x + e(x - y) commutes with the affine T", ok)
# N7: sharp values survive
check("N7 r_E = 1 at c + A e_z and 0 at c - A e_z", eff_apply(r_E, c + A * ez) == 1 and eff_apply(r_E, c - A * ez) == 0)
# N8: the Lorentz consumer is coordinate-bound: the centre c is a state; raw test |c|^2 <= 1 fails,
# transported test |Tc|^2 <= 1 holds.  Feeding raw coordinates is a wrong verdict, not a premise.
check("N8a raw consumer on the state c: |c|^2 = 6 > 1 = x0^2 (wrong verdict if not transported)", norm2(c) == 6)
check("N8b transported consumer on T c = 0 passes", norm2(T(c)) == 0)
xE = c + A * Matrix([1, 0, 0])
check("N8d countercontrol: the RAW directional effect (1 + e_x . x)/2 is not an effect on Omega_E (value 2 at c + A e_x)",
      in_E(xE) and eff_apply(ballEffect(Matrix([1, 0, 0])), xE) == 2)
# conePair(e, x0, v) for e = ballEffect(b) transported back: the pairing of a transported effect with a transported
# vector equals the pairing of the raw effect with the raw vector (the pairing is invariant, the coordinates are not)
ok = True
for Rm in ROTS:
    for b in UNITS:
        x = Tinv(b / 2)            # an interior state
        e_raw = eff_comp(eff_comp(r_E, ginv(g_E(Rm))), (eye(3), zeros(3, 1)))
        e_ball = eff_comp(e_raw, Tinvg)
        ok &= sp.simplify(eff_apply(e_raw, x) - eff_apply(e_ball, T(x))) == 0
check("N8c pairing invariance: e(x) = (e o T^{-1})(T x) for transported effects and states", ok)
# N9: residual freedom T -> O T (O orthogonal, O e_z = e_z) keeps the seed and the Lorentz verdict
O = Matrix([[R(3, 5), R(-4, 5), 0], [R(4, 5), R(3, 5), 0], [0, 0, 1]])
ok = simp(O.T * O) == eye(3) and O * ez == ez
ok &= all(norm2(O * T(Tinv(b / 3))) == norm2(T(Tinv(b / 3))) for b in UNITS)
check("N9 residual O(3)_z freedom of the normalization keeps the seed axis and every Lorentz verdict", ok)
# N10: cross-copy: normalizing two copies independently need not align their NOTs; aligning requires equal splits
NA = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])      # rotation by pi about x: split (p, q) = (1, 1)
Q = quat_rot(1, 0, 0, 1)                               # rotation by pi/2 about z, fixes e_z
NB = Q * NA * Q.T
check("N10a independent normalizations: N_B = Q N_A Q^{-1} != N_A (both flip e_z)", NB != NA and NB * ez == -ez)
check("N10b same split => conjugate by an O fixing e_z (alignment is a choice) ", simp(Q.T * NB * Q) == NA)
Nrefl = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])     # split (2, 0): reflection, flips e_z, not in SO(3)
check("N10c split (2,0) NOT flips e_z but is not conjugate to N_A in O(3) (traces 1 vs -1)",
      Nrefl * ez == -ez and Nrefl.trace() != NA.trace())
note("N10: a drive NOT N = flow(t0) lies in the identity component, so in SO(3); an involution there that moves the "
     "ball is a pi-rotation, split (1,1). The split mismatch of Thread B cannot arise for drive NOTs on one 3-ball; "
     "what normalization cannot supply is that copy B's NOT is the T_B-image of copy A's (copy covariance).")

print("== D: dimension ==")
# D1: lorentz_of_effects is dimension-free: instantiate its hypothesis family at p = 1, 2, 4, 5 with exact witnesses
for p in (1, 2, 4, 5):
    v = Matrix([R(1, 3)] * p)
    x0 = sqrt(norm2(v))
    # the minimizing unit b = -v/|v| gives x0 + b.v = 0 exactly: the test is tight in every dimension
    b = -v / x0
    check(f"D1 p={p}: Lorentz test tight at b = -v/|v| (dimension-free consumer)",
          sp.simplify(norm2(b) - 1) == 0 and sp.simplify(x0 + (b.T * v)[0]) == 0)
note("D1: lorentz_of_effects (NGB:105) takes p as a parameter (1 <= p); its p = 3 instantiation in L's draft is a "
     "consequence of BODY = ball3, never a source of dimension 3.")
# D2: in NB-1 the consumer runs at p = dim V+ inside blocks_vanish, which needs p >= 2; at d = 3 with a drive NOT
# (split (1,1)) p = 1, so the consumer carries no dimension content there.
note("D2 (written): at d = 3 a drive NOT has split (1,1), so p = dim V+ = 1 and blocks_vanish (hypothesis 2 <= p) "
     "is not invoked; inside NB-1 the consumer only carries content when p >= 2, i.e. to exclude d >= 5 or the "
     "(2,0) reflection-NOT at d = 3.")
# D3: the loop. B^4 with drive Rz(+)1 and J = cyc3(+)1: drive fields hold (rotation flow, pi-rotation NOT, off-axis J),
# but the seed orbit of (1 + e_1 . x)/2 never reaches b with b_4 != 0, so the NB-1 input (all unit b in R^4) fails.
def blockdiag(M3):
    M = eye(4)
    M[:3, :3] = M3
    return M


cyc = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
gens = [blockdiag(Rm) for Rm in ROTS] + [blockdiag(cyc)]
e1 = Matrix([1, 0, 0, 0])
orbit_dirs = set()
frontier = [e1]
seen = {tuple(e1)}
for _ in range(3):
    nxt = []
    for v in frontier:
        for Gm in gens:
            w = Gm * v
            if tuple(w) not in seen:
                seen.add(tuple(w))
                nxt.append(w)
    frontier = nxt
check("D3a B^4 drive group preserves x4: every orbit direction has b_4 = 0 (sampled words, exact)",
      all(t[3] == 0 for t in seen))
check("D3b so the directional effect (1 + e_4 . x)/2 is not a transport of the seed: NB-1's input fails at d = 4",
      (0, 0, 0, 1) not in seen)
note("D3: with only the drive, the ball/ellipsoid and the full directional family are available exactly in d = 3 "
     "(Thread K); NB-1 needs that family on a d-ball to conclude d in {1,3}. Using NB-1 to supply d = 3 to the step "
     "that needs d = 3 is the loop. A literal-transitivity premise TRANS(G_D) gives the ball in every d (D4) and "
     "breaks the loop; drive alone does not.")
# D4: literal transitivity in d = 4: with a group containing SO(4) the orbit covers; Householder-pair witness
def householder(u, w):  # rotation (product of two reflections) taking u to w, |u| = |w| = 1, u != -w
    n = u + w
    H1 = eye(len(u)) - 2 * (u * u.T)                       # reflection fixing u-perp... maps u -> -u
    H2 = eye(len(u)) - 2 * (n * n.T) / norm2(n)            # reflection along u + w: maps -u -> w
    return H2 * H1


w4 = Matrix([R(1, 2), R(1, 2), R(1, 2), R(1, 2)])
Rw = householder(e1, w4)
check("D4 an SO(4) element maps e_1 to (1,1,1,1)/2 exactly (transitivity is a separable premise in d = 4)",
      simp(Rw * e1) == w4 and simp(Rw.T * Rw) == eye(4) and Rw.det() == 1)
# D5: drive excludes d <= 2 (disk): an orthogonal J conjugates R(t) to R(+-t)
t = sp.symbols('t', real=True)
Rt = Matrix([[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]])
Jr = Matrix([[R(3, 5), R(4, 5)], [R(4, 5), R(-3, 5)]])   # a reflection
Jrot = Matrix([[R(3, 5), R(-4, 5)], [R(4, 5), R(3, 5)]])
check("D5 disk: reflection J R(t) J^{-1} = R(-t), rotation J R(t) J^{-1} = R(t) (off-axis fails, d = 2 not drivable)",
      simp(Jr * Rt * Jr.inv() - Rt.subs(t, -t)) == zeros(2, 2) and simp(Jrot * Rt * Jrot.inv() - Rt) == zeros(2, 2))

print("== S: drive sourcing (G-AUT is a field of the drive; the current substratum cannot supply the drive) ==")
X = Matrix([[0, 1], [1, 0]])
Y = Matrix([[0, -I], [I, 0]])
Z = Matrix([[1, 0], [0, -1]])
PAULI = [X, Y, Z]


def bloch_action(U):
    Ud = U.H
    return Matrix(3, 3, lambda j, k: sp.nsimplify(sp.simplify(((PAULI[j] * U * PAULI[k] * Ud).trace()) / 2)))


phases = [1, I, -1, -I]
monos = []
for p1, p2 in itertools.product(phases, phases):
    monos.append(Matrix([[p1, 0], [0, p2]]))
    monos.append(Matrix([[0, p1], [p2, 0]]))
ok = True
for M in monos:
    Rm = bloch_action(M)
    ok &= (Rm * ez == ez) or (Rm * ez == -ez)
check("S1 all 32 monomial unitaries (4th-root phases) send the Bloch axis e_z to +-e_z", ok)
# general monomial with symbolic phases
a_, b_ = sp.symbols('a b', real=True)
Dg = Matrix([[sp.exp(I * a_), 0], [0, sp.exp(I * b_)]])
Rd = bloch_action(Dg)
check("S2 a diagonal phase acts as a rotation about z (symbolic phases): e_z fixed", simp(Rd * ez) == ez)
check("S3 the swap acts as diag(1,-1,-1): e_z -> -e_z", bloch_action(X) == Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]]))
note("S1-S3: inside the substratum (monomial) group every flow is a z-rotation and every J keeps the z-axis, so "
     "J flow(t) J^{-1} = flow(+-t): the off-axis clause D9 fails (kernel counterpart substratum_residual SC:383, "
     "substratumTheory_not_layerFlowExecutable LiftAudit:200). G-AUT, a consequence of D4/D7/D8 of whatever drive is "
     "used, is therefore sourced only as far as that drive is sourced.")

print("== Q: reverse implication, qubit model (each premise row separately) ==")


def rho(r):
    return (eye(2) + r[0] * X + r[1] * Y + r[2] * Z) / 2


def is_psd2(M):
    M = simp(M)
    return M.is_hermitian and sp.simplify(M.trace()) >= 0 and sp.simplify(M.det()) >= 0


# Q0 Bloch ball = ball3 in Pauli coordinates (BODY holds literally in these coordinates)
samples_in = [Matrix([R(1, 3), R(1, 3), R(1, 3)]), Matrix([R(3, 5), R(4, 5), 0]), Matrix([0, 0, 0])]
samples_out = [Matrix([R(3, 5), R(4, 5), R(1, 10)]), Matrix([1, 1, 0])]
check("Q0 rho(r) PSD with trace 1 iff |r|^2 <= 1 (samples both sides; det = (1-|r|^2)/4)",
      all(is_psd2(rho(r)) for r in samples_in) and not any(is_psd2(rho(r)) for r in samples_out)
      and all(sp.simplify(rho(r).det() - (1 - norm2(r)) / 4) == 0 for r in samples_in + samples_out))
# Q1 P1 (sharp seed with 0 value): visible readout |0><0| = (I+Z)/2 -> (1 + z)/2, values 1 at e_z, 0 at -e_z
P0 = (eye(2) + Z) / 2
check("Q1 P1 in QM: tr(P0 rho(+e_z)) = 1, tr(P0 rho(-e_z)) = 0, P0 a projector",
      (P0 * rho(ez)).trace() == 1 and (P0 * rho(-ez)).trace() == 0 and P0 * P0 == P0)
# Q2 effects of the qubit = fullEffects(ball3): E = aI + c.sigma, 0<=E<=I iff |c| <= min(a, 1-a); tr(E rho) = a + c.r
rr = sp.symbols('r0 r1 r2', real=True)
cc = sp.symbols('c0 c1 c2', real=True)
aa = sp.symbols('a', real=True)
E = aa * eye(2) + cc[0] * X + cc[1] * Y + cc[2] * Z
check("Q2a tr(E rho(r)) = a + c.r identically", sp.simplify((E * rho(Matrix(rr))).trace() - (aa + sum(ci * ri for ci, ri in zip(cc, rr)))) == 0)
grid = [R(k, 4) for k in range(0, 5)]
cgrid = [Matrix([R(3, 10), R(4, 10), 0]), Matrix([0, 0, R(1, 4)]), Matrix([R(1, 3), R(2, 3), R(2, 3)])]
ok = True
seen_eff = set()
for a in grid:
    for cv in cgrid:
        Em = a * eye(2) + cv[0] * X + cv[1] * Y + cv[2] * Z
        eff = is_psd2(Em) and is_psd2(eye(2) - Em)
        # affine functional a + c.r in [0,1] on the unit ball  <=>  a - |c| >= 0 and a + |c| <= 1
        cn = sqrt(norm2(cv))
        aff = (a - cn >= 0) and (a + cn <= 1)
        ok &= (eff == bool(aff))
        seen_eff.add(eff)
check("Q2b-control both outcomes occur on the grid (non-vacuous)", seen_eff == {True, False})
check("Q2b on a rational grid: 0 <= E <= I  <=>  a +- |c| in [0,1]  (quantum effects = fullEffects(ball3))", ok)
# Q3 the drive in QM: flow U(theta) = cos I - i sin X with (cos, sin) = (3/5, 4/5): Bloch R_x(2 theta), rational
U = R(3, 5) * eye(2) - I * R(4, 5) * X
RU = bloch_action(U)
Rx2 = Matrix([[1, 0, 0], [0, R(-7, 25), R(-24, 25)], [0, R(24, 25), R(-7, 25)]])
check("Q3a U = e^{-i theta X} acts as R_x(2 theta) exactly (cos 2t = -7/25)", RU == Rx2 and simp(U * U.H) == eye(2))
S = Matrix([[1, 0], [0, I]])
RS = bloch_action(S)
check("Q3b quarter phase S acts as R_z(pi/2): x -> y", RS * Matrix([1, 0, 0]) == Matrix([0, 1, 0]))
# off-axis D9: S R_x S^{-1} = R_y; R_y(2t) e_z has x-component 24/25 while every R_x(s) e_z has x-component 0
Ry2 = RS * Rx2 * RS.T
check("Q3c D9 in QM: (S R_x S^-1) e_z has x-component 24/25 != 0 = x-component of every R_x(s) e_z",
      (Ry2 * ez)[0] == R(24, 25))
Nq = -I * X
check("Q3d D5/D6: N = e^{-i pi X/2} = -iX acts as diag(1,-1,-1): involutive, moves e_z, exchanges the seed pair",
      bloch_action(Nq) == Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]]) and simp((Nq.H * P0 * Nq)) == (eye(2) - Z) / 2)
# Q4 G-AUT in QM: U rho U^dagger stays a state, and so does U^dagger rho U
ok = all(is_psd2(U * rho(r) * U.H) and sp.simplify((U * rho(r) * U.H).trace()) == 1 and is_psd2(U.H * rho(r) * U)
         for r in samples_in)
check("Q4 G-AUT in QM: U and U^-1 conjugation keep rho(r) a state (body-side row)", ok)
# Q5 V4' in QM: transported seed U^dagger P0 U is a projector effect and equals (I + (R^T e_z).sigma)/2
# convention: (r o g^{-1})(x) where g = R_U acts on Bloch vectors; r o g^{-1} has b = R e_z
ok = True
for Uu in (U, S, U * S, S * U * S):
    Rg = bloch_action(Uu)
    Eg = simp(Uu * P0 * Uu.H)       # tr(Eg rho) = tr(P0 U^dag rho U) = r(g^{-1} x)
    b = Rg * ez
    ok &= simp(Eg * Eg - Eg) == zeros(2, 2) and simp(Eg - (eye(2) + b[0] * X + b[1] * Y + b[2] * Z) / 2) == zeros(2, 2)
check("Q5 V4' in QM: r o g^-1 = tr(U P0 U^dag .) is a projector = ballEffect(R_U e_z) (effect-side row)", ok)
note("Q5: availability side: in the generated quantum theory every finite Kraus instrument is available "
     "(ExactFiniteEndomorphicQuantumOps, LevelOneSeam:186, from genTheory_qm_of_quantumArchitecture SS:136 with "
     "fullClass_quantumArchitecture SS:151); the two-outcome instrument {U P0 U^dag, 1 - U P0 U^dag} is a Kraus "
     "instrument, so V4' holds for every drive whose maps are unitary conjugations. Written step: effect = outcome "
     "of an available instrument.")
# Q6 transitivity on the qubit body: explicit SU(2) words moving e_z to each sampled unit vector (Householder pair in SO(3))
ok = True
for b in UNITS:
    if b == -ez:
        continue
    Hm = householder(ez, b) if b != ez else eye(3)
    ok &= simp(Hm * ez) == b and Hm.det() == 1
check("Q6 K-inf-R on the qubit body: SO(3) (= Bloch image of SU(2)) carries e_z to every sampled unit vector", ok)
# Q7 SC-inf / finite rank / dim 3 in QM: stage tables tr(E rho) nested and consistent; affine rank of the completion is 4
effs = [eye(2), P0, (eye(2) + X) / 2, (eye(2) + Y) / 2, (eye(2) + Z) / 2,
        (eye(2) + R(3, 5) * X + R(4, 5) * Y) / 2, (eye(2) + R(2, 3) * X + R(1, 3) * Y + R(2, 3) * Z) / 2]
states = [rho(r) for r in samples_in] + [rho(ez), rho(-ez), rho(Matrix([1, 0, 0])), rho(Matrix([0, 1, 0])),
                                         rho(Matrix([R(-2, 7), R(3, 7), R(6, 7)]))]
table = Matrix(len(effs), len(states), lambda i, j: sp.simplify((effs[i] * states[j]).trace()))
sub = Matrix(4, 4, lambda i, j: table[i, j])
note("Q7a (written): in the matrix model a stage is a finite set of density matrices and effects with table "
     "tr(E rho); forward maps are inclusions, so SC-inf holds by construction (consistency instance, not evidence "
     "that the stages OI supplies are consistent).")
check("Q7b completion body has affine dimension 3 (rank of the state-vector matrix = 4 = dim + 1)", table.rank() == 4)
check("Q7c all table entries in [0,1] (stage validity)", all(0 <= table[i, j] <= 1 for i in range(len(effs)) for j in range(len(states))))
# Q8 NB-1 premises at d = 3 in QM: CNOT relations with the common NOT X (Rt, Rc) in the matrix model
CN = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
IX = sp.kronecker_product(eye(2), X)
XI = sp.kronecker_product(X, eye(2))
check("Q8a Rt: (I x X) CNOT (I x X) = CNOT", IX * CN * IX == CN)
check("Q8b Rc: (X x I) CNOT (X x I) = (I x X) CNOT", XI * CN * XI == IX * CN)
SW = Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
check("Q8c identical-copy covariance: SWAP (X x I) SWAP^-1 = I x X", SW * XI * SW.T == IX)

print("== X: scope -- unscoped forward premises fail in QM ==")
# qutrit body: two boundary states with different purity; no unitary/antiunitary maps one to the other
r1 = Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
r2 = Matrix([[R(1, 2), 0, 0], [0, R(1, 2), 0], [0, 0, 0]])
y = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
epsq = R(1, 100)
ext = r2 + epsq * (r2 - y)
check("X1a diag(1/2,1/2,0) is a boundary state of the qutrit body: x + e(x - y) has eigenvalue -e for every e > 0",
      ext[2, 2] == -epsq)
check("X1b purities 1 vs 1/2 (invariant under U.U^dag and transpose): literal K-inf-R FAILS on the unscoped qutrit body",
      (r1 * r1).trace() == 1 and (r2 * r2).trace() == R(1, 2))
# affine dimension of the qutrit body: 9 linearly independent density matrices -> affine dim 8
E3 = lambda i, j: Matrix(3, 3, lambda a, b: 1 if (a, b) == (i, j) else 0)
dens = [E3(i, i) for i in range(3)]
for i, j in ((0, 1), (0, 2), (1, 2)):
    v = (E3(i, i) + E3(j, j) + E3(i, j) + E3(j, i)) / 2
    w = (E3(i, i) + E3(j, j) - I * E3(i, j) + I * E3(j, i)) / 2
    dens += [v, w]
Mv = Matrix([[sp.re(d[a, b]) for a in range(3) for b in range(3)] + [sp.im(d[a, b]) for a in range(3) for b in range(3)]
             for d in dens])
check("X2 DIM3 FAILS on the unscoped qutrit body: 9 independent states (affine dimension 8)", Mv.rank() == 9)
Pq = E3(0, 0) + E3(1, 1)
check("X3 singleton-face principle FAILS unscoped: the proper sharp test diag(1,1,0) is certain on |0><0| and |1><1|",
      (Pq * E3(0, 0)).trace() == 1 and (Pq * E3(1, 1)).trace() == 1 and (Pq * E3(2, 2)).trace() == 0)
# dilated visible readout: P0 (x) I on C^2 (x) C^2 is sharp but certain on two distinct product states; body dim 15
P0d = sp.kronecker_product(P0, eye(2))
s1 = sp.kronecker_product(rho(ez), rho(ez))
s2 = sp.kronecker_product(rho(ez), rho(-ez))
check("X4a block readout P_0 (x) 1_anc (Main.md:240 form) is sharp yet certain on two distinct states",
      (P0d * s1).trace() == 1 and (P0d * s2).trace() == 1 and s1 != s2)
check("X4b the visible marginal of both is rho(e_z): the reduced (visible-factor) body is the 3-ball",
      Matrix(2, 2, lambda a, b: s1[2 * a, 2 * b] + s1[2 * a + 1, 2 * b + 1]) == rho(ez)
      and Matrix(2, 2, lambda a, b: s2[2 * a, 2 * b] + s2[2 * a + 1, 2 * b + 1]) == rho(ez))
note("X: every forward premise holds in QM for the elementary (capacity-two) body read on the visible factor; "
     "stated for an arbitrary system's body (qutrit) or for the dilated visible readout, K-inf-R, DIM3 and the "
     "singleton-face principle are false in QM. The scope ELEM is a load-bearing premise row, not a convention.")

fails = [n for n, c in CHECKS if not c]
print()
print(f"{'OK' if not fails else 'FAILED'} -- {len(CHECKS)} checks, {len(fails)} failed, {len(NOTES)} written notes")
for n in fails:
    print("  failed:", n)

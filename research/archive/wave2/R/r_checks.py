"""Thread R (wave 2) -- exact checks for sourcing DIM3 of the elementary (visible-factor) body.

Read-only research against certified main L = f7f5c3b0c621cc3e4b57e3709d11d9d580c81149.
Exact arithmetic only: sympy Rational, exact radicals, symbolic trigonometry; no floats.

Sections
  A  lower bound: d = 1 excluded for every body (no boundedness, no continuity); d = 2 exclusion (B6)
     needs BOUNDEDNESS -- the whole plane is drivable (countermodel); bounded planar bodies fail D9.
  B  countermodels for upper-bound principles: Sp(1) left multiplication on B^4 (drive, transitive,
     3-dim generator algebra, no stationary pure state); SO(3) spin-2 drive on B^5 (drive, irreducible,
     3-dim generator algebra, seed orbit spanning, not transitive); SO(3)+1 on B^4.
  E  energy observability (EO): dimension of the space of Lie-algebra intertwiners g -> R^d for every
     candidate group; injective intertwiner exists exactly for so(3) on R^3 among the transitive cases.
  H  hat-map equivariance: proper rotations intertwine, improper ones intertwine with a sign
     (EO must be read on the identity component / Lie algebra level).
  U  U(2) on R^4: a sharp-effect -> flow assignment exists that is equivariant but not odd; EO fails.
  I  information-capacity / one-bit principle and Hardy counting: no constraint on d in binary scope.
Run:  PYTHONDONTWRITEBYTECODE=1 python3 r_checks.py
"""
import itertools
import sympy as sp
from sympy import Rational as R, Matrix, I, eye, zeros, sqrt, cos, sin, pi, symbols

CHECKS = []
NOTES = []


def check(name, cond):
    cond = bool(cond)
    CHECKS.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


def note(s):
    NOTES.append(s)
    print("NOTE " + s)


def S(M):
    return M.applyfunc(lambda z: sp.simplify(sp.expand(sp.expand_trig(z))))


def iszero(M):
    return all(sp.simplify(z) == 0 for z in M)


t, s, a, b = symbols("t s a b", real=True)


def rot2(th):
    return Matrix([[cos(th), -sin(th)], [sin(th), cos(th)]])


# ---------------------------------------------------------------- A: lower bound
# A1: d = 1, any body (bounded or not): N = h o h with h affine on the line (D2: flow(t0) = flow(t0/2)^2).
x = symbols("x", real=True)
hx = a * x + b
Nx = sp.expand(hx.subs(x, hx))                      # N(x) = a^2 x + a b + b
NNx = sp.expand(Nx.subs(x, Nx))
sols = sp.solve(sp.Poly(NNx - x, x).coeffs(), [a, b], dict=True)
real_sols = [d for d in sols if all(v.is_real for v in d.values())]
check("A1 d=1: every real h with (h o h) involutive has h o h = id on the line",
      all(sp.simplify(Nx.subs(d) - x) == 0 for d in real_sols) and len(real_sols) > 0)
note("A1 uses only D2 (flow(t0) = flow(t0/2)^2), D4 restricted to aff(Omega) and D5/D6: no continuity, "
     "no boundedness. Kernel: not_drivable_Icc (KF:529) for Icc(-1,1) in R only; transport written.")

# A2: unbounded planar body Omega = R^2 is drivable: flow R(t), t0 = pi, J = shear.
Fl = rot2(t)
check("A2a flow group law R(s)R(t) = R(s+t)", iszero(S(rot2(s) * rot2(t) - rot2(s + t))))
Nm = rot2(pi)
check("A2b N = R(pi) = -I: involutive and moves (1,0)", Nm * Nm == eye(2) and Nm * Matrix([1, 0]) != Matrix([1, 0]))
Jm = Matrix([[1, 1], [0, 1]])
C = S(Jm * rot2(pi / 2) * Jm.inv())
check("A2c J R(pi/2) J^-1 = [[1,-2],[1,-1]]", C == Matrix([[1, -2], [1, -1]]))
check("A2d it is not orthogonal, hence equal to no R(s): C^T C != I", C.T * C != eye(2))
note("A2: Omega = R^2 (affine dimension 2, unbounded, no boundary state) carries an ElementaryDrivability "
     "(D1-D9; D3 continuous). B6 'planar => not drivable' therefore needs BOUNDEDNESS of Omega. For the "
     "completion body it is supplied by values in [0,1] (P1b), not by the drive.")

# A3: bounded planar: every J in O(2) conjugates R(t) to R(t) or R(-t).
al = symbols("alpha", real=True)
Jr = rot2(al)
Jf = Matrix([[cos(al), sin(al)], [sin(al), -cos(al)]])
check("A3a rotation J: J R(t) J^-1 = R(t)", iszero(S(Jr * rot2(t) * Jr.T - rot2(t))))
check("A3b reflection J: J R(t) J^-1 = R(-t)", iszero(S(Jf * rot2(t) * Jf.T - rot2(-t))))

# ---------------------------------------------------------------- quaternion helpers
def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


def Lmat(p):
    cols = []
    for e in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]:
        cols.append(list(qmul(p, e)))
    return Matrix(cols).T


def Rmat(p):
    cols = []
    for e in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]:
        cols.append(list(qmul(e, p)))
    return Matrix(cols).T


Li, Lj, Lk = Lmat((0, 1, 0, 0)), Lmat((0, 0, 1, 0)), Lmat((0, 0, 0, 1))

# ---------------------------------------------------------------- B: countermodels
# B1: Sp(1) acting on R^4 = H by left multiplication; the unit ball B^4.
check("B1a L_i^2 = -I, L_i skew", Li * Li == -eye(4) and Li.T == -Li)
flow4 = lambda th: cos(th) * eye(4) + sin(th) * Li
check("B1b flow(s) flow(t) = flow(s+t)", iszero(S(flow4(s) * flow4(t) - flow4(s + t))))
check("B1c flow orthogonal (preserves B^4)", iszero(S(flow4(t).T * flow4(t) - eye(4))))
N4 = S(flow4(pi))
check("B1d N = flow(pi) = -I: involutive, moves", N4 == -eye(4))
q = (R(3, 5), 0, R(4, 5), 0)
qbar = (R(3, 5), 0, -R(4, 5), 0)
J4 = Lmat(q)
check("B1e J = L_q orthogonal (q unit, rational)", J4.T * J4 == eye(4))
ip = qmul(qmul(q, (0, 1, 0, 0)), qbar)
check("B1f q i q^-1 = (0, -7/25, 0, -24/25): not +-i", ip == (0, R(-7, 25), 0, R(-24, 25)))
Cj = S(J4 * flow4(pi / 2) * J4.T)
check("B1g J flow(pi/2) J^-1 = L_{q i q^-1} (zero diagonal)", Cj == Lmat(ip))
# equality with flow(s) needs cos s = 0 (diagonal) and then L_{qiq^-1} = +-L_i, false
check("B1h D9: L_{qiq^-1} != +-L_i, so J flow(pi/2) J^-1 equals no flow member",
      Cj != Li and Cj != -Li)


def lie_closure(gens):
    basis = []

    def add(M):
        vecs = [list(B) for B in basis] + [list(M)]
        if Matrix(vecs).rank() > len(basis):
            basis.append(M)
            return True
        return False

    for g in gens:
        add(g)
    changed = True
    while changed:
        changed = False
        for A_, B_ in itertools.product(list(basis), list(basis)):
            if add(A_ * B_ - B_ * A_):
                changed = True
    return basis


alg = lie_closure([Li, Lmat(ip)])
check("B1i Lie algebra generated by the flow generator and its J-conjugate has dim 3 (= sp(1))", len(alg) == 3)
u = (R(1, 2), R(1, 2), R(1, 2), R(1, 2))
check("B1j transitivity witness: L_u e_1 = u for a unit u (left multiplication is transitive on S^3)",
      Lmat(u) * Matrix([1, 0, 0, 0]) == Matrix(u))
check("B1k no stationary pure state: L_i has no real eigenvector (char poly (l^2+1)^2)",
      sp.factor(Li.charpoly().as_expr()) == sp.factor((symbols('lambda') ** 2 + 1) ** 2))
note("B1: B^4 with the Sp(1) drive satisfies DRIVE (D1-D9), boundary transitivity of the drive group "
     "(Sp(1) = words of two non-commuting circles, Lowenthal-type, written), and a 3-dimensional "
     "generator algebra: 'TRANS + minimal generator algebra' does not give d = 3.")

# B2: SO(3) acting on Sym0(3) (spin-2, d = 5); unit Frobenius ball.
Eij = lambda i, j: Matrix(3, 3, lambda r, c: 1 if (r, c) == (i, j) else 0)
sym_basis = [Eij(0, 0) - Eij(1, 1), Eij(1, 1) - Eij(2, 2), Eij(0, 1) + Eij(1, 0), Eij(0, 2) + Eij(2, 0),
             Eij(1, 2) + Eij(2, 1)]
SB = Matrix([list(M) for M in sym_basis]).T          # 9 x 5


def sym_coords(M):
    sol = SB.solve_least_squares(Matrix(list(M)))
    assert SB * sol == Matrix(list(M))
    return sol


def rep_on(basis_mats, coords, act):
    cols = [coords(act(Bm)) for Bm in basis_mats]
    return Matrix.hstack(*cols)


so3 = [Eij(2, 1) - Eij(1, 2), Eij(0, 2) - Eij(2, 0), Eij(1, 0) - Eij(0, 1)]  # Lx, Ly, Lz
rho2 = [rep_on(sym_basis, sym_coords, lambda Sm, X=X: X * Sm - Sm * X) for X in so3]


def Rz3(th):
    return Matrix([[cos(th), -sin(th), 0], [sin(th), cos(th), 0], [0, 0, 1]])


def Rx3(th):
    return Matrix([[1, 0, 0], [0, cos(th), -sin(th)], [0, sin(th), cos(th)]])


cyc = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
Sg = Matrix(3, 3, lambda r, c: symbols(f"s{min(r,c)}{max(r,c)}", real=True))
flowS = lambda th, M: Rz3(th) * M * Rz3(th).T
check("B2a spin-2 flow group law", iszero(S(flowS(s, flowS(t, Sg)) - flowS(s + t, Sg))))
check("B2b flow preserves the Frobenius norm and tracelessness",
      sp.simplify((flowS(t, Sg) * flowS(t, Sg)).trace() - (Sg * Sg).trace()) == 0
      and sp.simplify(flowS(t, Sg).trace() - Sg.trace()) == 0)
E13 = Eij(0, 2) + Eij(2, 0)
check("B2c N = conj by Rz(pi): involutive and moves E13+E31",
      S(flowS(pi, flowS(pi, Sg))) == Sg and S(flowS(pi, E13)) == -E13)
Jconj = lambda M: cyc * M * cyc.T
check("B2d J = conj by cyc3 conjugates the flow to conj by Rx(t) (cyc Rz cyc^-1 = Rx)",
      iszero(S(cyc * Rz3(t) * cyc.T - Rx3(t))))
E12 = Eij(0, 1) + Eij(1, 0)
lhs = S(Rx3(pi / 2) * E12 * Rx3(pi / 2).T)
rhs = S(Rz3(s) * E12 * Rz3(s).T)
check("B2e D9: conj by Rx(pi/2) differs from every conj by Rz(s) on E12+E21 (third-row entries)",
      lhs[2, 0] != 0 and sp.simplify(rhs[2, 0]) == 0)
comm = Matrix.vstack(*[ (lambda X: Matrix(5, 5, lambda r, c: symbols(f"c{r}{c}")) * X
                         - X * Matrix(5, 5, lambda r, c: symbols(f"c{r}{c}")))(X).reshape(25, 1)
                       for X in rho2])
cvars = [symbols(f"c{r}{c}") for r in range(5) for c in range(5)]
A_, _ = sp.linear_eq_to_matrix(list(comm), cvars)
check("B2f spin-2 representation irreducible (commutant dimension 1)", len(cvars) - A_.rank() == 1)
alg2 = lie_closure(rho2[2:3] + [rep_on(sym_basis, sym_coords, lambda Sm: (cyc * so3[2] * cyc.T) * Sm
                                       - Sm * (cyc * so3[2] * cyc.T))])
check("B2g generator algebra of the spin-2 drive has dim 3", len(alg2) == 3)
P1 = (Eij(0, 0) - Eij(1, 1)) / sqrt(2)
P2 = (2 * Eij(0, 0) - Eij(1, 1) - Eij(2, 2)) / sqrt(6)
check("B2h two unit boundary points with different det (an orbit invariant): not transitive",
      sp.simplify((P1 * P1).trace()) == 1 and sp.simplify((P2 * P2).trace()) == 1
      and sp.simplify(P1.det()) == 0 and sp.simplify(P2.det()) != 0)
v0 = sym_coords(E12 + Eij(2, 2) - Eij(0, 0))
orbit_span = Matrix.hstack(v0, *[r * v0 for r in rho2],
                           *[r1 * r2 * v0 for r1 in rho2 for r2 in rho2])
check("B2i a seed direction whose drive-orbit spans all of R^5 (orbit-span = Lie-module span)",
      orbit_span.rank() == 5)
note("B2: B^5 with the SO(3) spin-2 drive satisfies DRIVE, irreducibility, a 3-dimensional generator "
     "algebra and seed-orbit spanning, with d = 5. It fails TRANS (det invariant) and EO (E-series).")

# B3: B^4 with SO(3)+1.
so3p1 = [Matrix.diag(X, Matrix([[0]])) for X in so3]
check("B3 SO(3)+1 fixes x4: e_4 annihilated by every generator (boundary not one orbit)",
      all(X * Matrix([0, 0, 0, 1]) == zeros(4, 1) for X in so3p1))

# ---------------------------------------------------------------- E: energy observability
def structure(basis):
    Bm = Matrix([list(M) for M in basis]).T

    def coords(M):
        sol = Bm.solve_least_squares(Matrix(list(M)))
        assert Bm * sol == Matrix(list(M))
        return sol

    return [Matrix.hstack(*[coords(X * Y - Y * X) for Y in basis]) for X in basis]


def intertwiners(basis, rho):
    """dim and generic rank of { L : g -> R^d linear | L ad(X) = rho(X) L for all basis X }."""
    m = len(basis)
    d = rho[0].shape[0]
    ads = structure(basis)
    Lv = Matrix(d, m, lambda r, c: symbols(f"L{r}_{c}"))
    eqs = []
    for adX, rX in zip(ads, rho):
        eqs += list(Lv * adX - rX * Lv)
    vars_ = list(Lv)
    A, _ = sp.linear_eq_to_matrix(eqs, vars_)
    ns = A.nullspace()
    rk = 0
    if ns:
        gen = sum((sp.Integer(k + 2) * v for k, v in enumerate(ns)), zeros(len(vars_), 1))
        rk = Matrix(d, m, list(gen)).rank()
    return len(ns), rk, m, d


def so_basis(n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            M = zeros(n)
            M[i, j], M[j, i] = -1, 1
            out.append(M)
    return out


def cplx_to_real(M):
    n = M.shape[0]
    Rm = zeros(2 * n)
    for r in range(n):
        for c in range(n):
            z = M[r, c]
            re, im = sp.re(z), sp.im(z)
            Rm[2 * r, 2 * c], Rm[2 * r, 2 * c + 1] = re, -im
            Rm[2 * r + 1, 2 * c], Rm[2 * r + 1, 2 * c + 1] = im, re
    return Rm


sx, sy, sz = Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])
u2 = [cplx_to_real(I * M) for M in [eye(2), sx, sy, sz]]

cases = [
    ("so(2) on R^2 (rebit disk)", so_basis(2), None, False),
    ("so(3) on R^3 (qubit ball)", so_basis(3), None, True),
    ("sp(1)_L on R^4 (B1)", [Li, Lj, Lk], None, False),
    ("u(2) on R^4 = C^2", u2, None, False),
    ("so(4) on R^4", so_basis(4), None, False),
    ("so(5) on R^5 (quaternionic bit, Spin(5) = Sp(2) acts through SO(5))", so_basis(5), None, False),
    ("so(7) on R^7", so_basis(7), None, False),
    ("so(2)+so(2) on R^4 (bidisk)", [Matrix.diag(X, zeros(2)) for X in so_basis(2)]
     + [Matrix.diag(zeros(2), X) for X in so_basis(2)], None, False),
    ("so(3) on Sym0(3) = R^5 (spin-2, B2)", so3, rho2, False),
]
for name, basis, rho, expect in cases:
    nul, rk, m, d = intertwiners(basis, rho if rho is not None else basis)
    inj = (nul > 0 and rk == m)
    check(f"E {name}: intertwiners g->R^d dim {nul}, injective exists = {inj}", inj == expect)

for name, basis, rho, expect in [
    ("so(3)+0 on R^4 (B3, also cone over B^3 / B^3 x [-1,1])", so3p1, None, True),
    ("so(3)+so(3) on R^6 (B^3 x B^3)", [Matrix.diag(X, zeros(3)) for X in so3]
     + [Matrix.diag(zeros(3), X) for X in so3], None, True),
]:
    nul, rk, m, d = intertwiners(basis, basis)
    check(f"E {name} [non-transitive]: injective intertwiner exists (EO holds, TRANS fails)",
          (nul > 0 and rk == m) == expect)

# su(3) on Herm0(3) = R^8 (qutrit): coordinates over a rational basis of traceless Hermitian matrices.
H3 = [Eij(0, 0) - Eij(1, 1), Eij(1, 1) - Eij(2, 2)]
for (i_, j_) in [(0, 1), (0, 2), (1, 2)]:
    H3 += [Eij(i_, j_) + Eij(j_, i_), I * (Eij(i_, j_) - Eij(j_, i_))]
HB = Matrix([[sp.re(z) for z in M] + [sp.im(z) for z in M] for M in H3]).T


def hcoords(M):
    v = Matrix([sp.re(z) for z in M] + [sp.im(z) for z in M])
    sol = HB.solve_least_squares(v)
    assert HB * sol == v
    return sol


rho8 = [Matrix.hstack(*[hcoords(sp.expand(I * (Ka * Kb - Kb * Ka))) for Kb in H3]) for Ka in H3]
# Lie algebra i*Herm0 with coordinates of K; bracket [iKa, iKb] = i (i[Ka,Kb]) -> ad matrices = rho8
nul8 = rho8  # identity intertwiner: ad(iKa) in K-coordinates equals rho8[a]
Lv = Matrix(8, 8, lambda r, c: symbols(f"M{r}_{c}"))
eqs8 = []
for rA in rho8:
    eqs8 += list(Lv * rA - rA * Lv)
A8, _ = sp.linear_eq_to_matrix(eqs8, list(Lv))
check("E su(3) on Herm0(3) = R^8 (qutrit): identity intertwiner, commutant dim 1 (EO holds unscoped in QM)",
      len(list(Lv)) - A8.rank() == 1)

note("E: dimension counts close the transitive cases not computed: G2 (dim 14) on R^7, Spin(7) (21) on R^8, "
     "Spin(9) (36) on R^16, SU(n) (n^2-1), Sp(n) (n(2n+1)) on R^(2n), R^(4n), n >= 2: dim g > d, so no "
     "injective linear map g -> R^d at all.")

# ---------------------------------------------------------------- H: hat map equivariance
def hat(v):
    return Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def quat_rot(a1, b1, c1, d1):
    n = a1 * a1 + b1 * b1 + c1 * c1 + d1 * d1
    return Matrix([
        [a1*a1 + b1*b1 - c1*c1 - d1*d1, 2*(b1*c1 - a1*d1), 2*(b1*d1 + a1*c1)],
        [2*(b1*c1 + a1*d1), a1*a1 - b1*b1 + c1*c1 - d1*d1, 2*(c1*d1 - a1*b1)],
        [2*(b1*d1 - a1*c1), 2*(c1*d1 + a1*b1), a1*a1 - b1*b1 - c1*c1 + d1*d1]]) / n


Rq = quat_rot(1, 2, 3, 4)
vv = Matrix([R(2), R(-1), R(5)])
check("H1 proper rational rotation: R hat(v) R^T = hat(R v)", Rq.det() == 1 and Rq * hat(vv) * Rq.T == hat(Rq * vv))
Rim = -Rq
check("H2 improper (-R): (-R) hat(v) (-R)^T = -hat((-R) v): equivariance holds only up to det",
      Rim.det() == -1 and Rim * hat(vv) * Rim.T == -hat(Rim * vv))
D9J = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]]) * cyc       # improper J off the flow axis
check("H3 an improper J (det -1) still satisfies D9 with the Rz flow (J e_z not +-e_z)",
      D9J.det() == -1 and D9J * Matrix([0, 0, 1]) not in (Matrix([0, 0, 1]), Matrix([0, 0, -1])))

# ---------------------------------------------------------------- U: U(2) sharp-effect assignment
def u_vec_to_c(v):
    return Matrix([v[0] + I * v[1], v[2] + I * v[3]])


def A_of(uv):
    uc = u_vec_to_c(uv)
    P = uc * uc.H
    return cplx_to_real(sp.expand(I * (eye(2) - P)))


uv = Matrix([R(3, 5), 0, R(4, 5), 0])
Au = A_of(uv)
check("U1 A_u = i(1 - |u><u|) annihilates u and is nonzero", Au * uv == zeros(4, 1) and Au != zeros(4))
check("U2 A_{-u} = A_u (the assignment is even, not odd)", A_of(-uv) == Au)
g = cplx_to_real(Matrix([[R(3, 5), -R(4, 5)], [R(4, 5), R(3, 5)]]) * Matrix([[I, 0], [0, 1]]))
check("U3 equivariance g A_u g^-1 = A_{g u} for a rational U(2) element", sp.simplify(g * Au * g.inv() - A_of(g * uv)) == zeros(4))
note("U: on B^4 under U(2) (transitive, dim 4 = d, stabilizer dim 1) an equivariant map from sharp "
     "directions to nontrivial flows fixing them exists; it is even (A_{-u} = A_u), so it is not the "
     "restriction of a linear EO map (E: u(2) -> R^4 has no intertwiner). Stabilizer-dimension or "
     "'dim G = d' counting alone does not give d = 3.")

# ---------------------------------------------------------------- I: one bit, Hardy counting
xs = symbols("x1:8", real=True)
for d in (2, 3, 4, 5, 7):
    info = sum(((1 + xs[i]) / 2 - (1 - xs[i]) / 2) ** 2 for i in range(d))
    check(f"I1 d={d}: Brukner-Zeilinger total information over d orthogonal axes = |x|^2 (one bit on pure states)",
          sp.simplify(info - sum(xs[i] ** 2 for i in range(d))) == 0)
for d in (2, 3, 4, 5, 7):
    Ks = [(d + 1) ** n for n in (1, 2, 3)]
    pow2 = (d + 1) & d == 0
    check(f"I2 d={d}: K(2^n) = (d+1)^n multiplicative for n=1..3 (LT counting holds); r = log2(d+1) "
          f"integer: {pow2}",
          all(Ks[n] == Ks[0] ** (n + 1) for n in range(3)))
note("I2: within binary scope LT counting K(2^n) = K(2)^n holds for every d; Hardy's integrality of r "
     "needs systems with N = 3 (subspace axiom); with it, d + 1 = 2^r leaves d in {3, 7, 15, ...} "
     "(r >= 2), and only the Simplicity axiom (minimal K) picks d = 3.")

nfail = sum(1 for _, c in CHECKS if not c)
print(("OK" if nfail == 0 else "FAILED") + f" -- {len(CHECKS)} checks, {nfail} failed, {len(NOTES)} written notes")

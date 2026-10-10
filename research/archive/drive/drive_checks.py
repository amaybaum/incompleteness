"""DRIVE-operation sourcing investigation: exact checks (read-only, off-repo).

Base D_DRIVE = 0f2687b7b87925b53c6e3d8c6d1a233f36624dea.  sympy exact arithmetic; transcendental
inequalities only through mpmath interval arithmetic (rigorous enclosures).  Run with
PYTHONDONTWRITEBYTECODE=1.  Sections:
  M  matrix regime (imported C^2, Bloch picture): AffineRespect of phases and of the Clifford gate
     against the stage effect span; tomographic completeness forced; the body forced to the ball.
  C  chart continuity from finitely many probability functions (field-neutral illustration).
  N  completion-valued versus stage-valued: the NOT of a 1-radian tower leaves every preparation.
  G  closure route: one infinite-order operation; powers approach the involution and the identity.
  X  countermodels, one per new premise.
"""
from fractions import Fraction as Fr
import sympy as sp
from mpmath import iv, mpf

iv.dps = 60
RESULTS = []


def check(name, cond):
    RESULTS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
PAULI = [X, Y, Z]
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
th, ph, s, t = sp.symbols('theta phi s t', real=True)


def Rz(a):
    return sp.Matrix([[1, 0], [0, sp.exp(sp.I * a)]])


def dag(U):
    return U.conjugate().T


def adj(U):
    """Bloch (adjoint) matrix of conjugation by U on the traceless Hermitian part."""
    return sp.Matrix(3, 3, lambda i, j: sp.simplify(
        sp.expand((PAULI[i] * U * PAULI[j] * dag(U)).trace() / 2)))


def ket(v):
    return sp.Matrix(v)


def rho(v):
    k = ket(v)
    k = k / sp.sqrt((dag(k) * k)[0])
    return sp.simplify(k * dag(k))


r2 = 1 / sp.sqrt(2)
PREPS = {
    '0': rho([1, 0]), '1': rho([0, 1]),
    '+': rho([1, 1]), '-': rho([1, -1]),
    '+i': rho([1, sp.I]), '-i': rho([1, -sp.I]),
}
NAMES = list(PREPS)


def readout(Wbasis, r):
    return [sp.simplify(sp.expand((E * r).trace())) for E in Wbasis]


def affine_relations(Wbasis):
    """Kernel of the stage map c -> (sum c, sum c * readout) over the six preparations."""
    rows = [[1] * len(NAMES)]
    cols = [readout(Wbasis, PREPS[n]) for n in NAMES]
    for k in range(len(Wbasis)):
        rows.append([cols[j][k] for j in range(len(NAMES))])
    return sp.Matrix(rows).nullspace()


def respects(Wbasis, U):
    """AffineRespect of the datum x -> readout(U rho_x U^dag) on the six-preparation stage."""
    rels = affine_relations(Wbasis)
    imgs = [readout(Wbasis, U * PREPS[n] * dag(U)) for n in NAMES]
    for c in rels:
        for k in range(len(Wbasis)):
            if sp.simplify(sp.expand(sum(c[j] * imgs[j][k] for j in range(len(NAMES))))) != 0:
                return False
    return True


W_diag = [I2, Z]                    # the substratum's visible (diagonal) effect span
W_full = [I2, X, Y, Z]              # a tomographically complete effect span

# ---------------------------------------------------------------- M: matrix regime
RH = adj(H)
RZ = adj(Rz(th))
check('M0 adjoint of H is the x<->z swap with y -> -y',
      RH == sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]]))
check('M0 adjoint of the phase diag(1,e^{i theta}) is the z-rotation by theta',
      sp.simplify(RZ - sp.Matrix([[sp.cos(th), -sp.sin(th), 0],
                                  [sp.sin(th), sp.cos(th), 0], [0, 0, 1]])) == sp.zeros(3))
check('M1 diagonal effects: the phase datum respects affine relations (symbolic theta)',
      respects(W_diag, Rz(th)))
check('M1 diagonal effects: the Clifford datum H does NOT respect affine relations',
      not respects(W_diag, H))
# the explicit broken relation: rho_+ - rho_{+i} reads zero on diagonal effects, its H-image does not
rel_zero = [sp.simplify(a - b) for a, b in zip(readout(W_diag, PREPS['+']), readout(W_diag, PREPS['+i']))]
img = [sp.simplify(a - b) for a, b in zip(readout(W_diag, H * PREPS['+'] * dag(H)),
                                          readout(W_diag, H * PREPS['+i'] * dag(H)))]
check('M1 witness: rho_+ ~ rho_{+i} on diagonal effects, H rho_+ H !~ H rho_{+i} H',
      rel_zero == [0, 0] and img == [0, 1])
check('M2 diagonal effects: VIS fails, every phase acts trivially on the read-out (symbolic theta)',
      all(sp.simplify(sp.Matrix(readout(W_diag, Rz(th) * PREPS[n] * dag(Rz(th))))
                      - sp.Matrix(readout(W_diag, PREPS[n]))) == sp.zeros(2, 1) for n in NAMES))
check('M3 full effects: phase and H both respect affine relations',
      respects(W_full, Rz(th)) and respects(W_full, H))

# invariant subspaces of the Bloch traceless part under R_z(pi/2) and R_H
RQ = adj(Rz(sp.pi / 2))
check('M4 R_z(pi/2) is the integer quarter-turn', RQ == sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))
lam = sp.symbols('lam')
cp = sp.factor((RQ - lam * sp.eye(3)).det())
check('M4 char poly of R_z(pi/2) = -(lam-1)(lam^2+1): the xy-plane is irreducible over R',
      sp.expand(cp + (lam - 1) * (lam ** 2 + 1)) == 0)
# hence the R_z(pi/2)-invariant subspaces are 0, z, xy, R^3; test each under R_H
ez = sp.Matrix([0, 0, 1]); exy = sp.Matrix([[1, 0], [0, 1], [0, 0]])


def invariant(B, R):
    if B.shape[1] == 0:
        return True
    return sp.Matrix.hstack(B, R * B).rank() == B.rank()


cands = {'0': sp.zeros(3, 0), 'z': ez, 'xy': exy, 'R3': sp.eye(3)}
inv_H = {k: invariant(B, RH) for k, B in cands.items()}
check('M4 the only subspaces invariant under both R_z(pi/2) and R_H are 0 and R^3',
      inv_H == {'0': True, 'z': False, 'xy': False, 'R3': True})
check('M5 H conjugates the phase flow to the x-rotation flow: R_H R_z(theta) R_H = R_x(theta)',
      sp.simplify(RH * RZ * RH - sp.Matrix([[1, 0, 0], [0, sp.cos(th), -sp.sin(th)],
                                            [0, sp.sin(th), sp.cos(th)]])) == sp.zeros(3))
RX = sp.Matrix([[1, 0, 0], [0, sp.cos(th), -sp.sin(th)], [0, sp.sin(th), sp.cos(th)]])
RZp = RZ.subs(th, ph)
orb = sp.simplify(RZp * RX * ez)
check('M5 R_z(phi) R_x(theta) e_z = (sin th sin ph, -sin th cos ph, cos th): the orbit is the sphere',
      sp.simplify(orb - sp.Matrix([sp.sin(th) * sp.sin(ph), -sp.sin(th) * sp.cos(ph), sp.cos(th)]))
      == sp.zeros(3, 1))
check('M6 inverse data: Rz(theta) Rz(-theta) = 1 and H H = 1',
      sp.simplify(Rz(th) * Rz(-th) - I2) == sp.zeros(2) and sp.simplify(H * H - I2) == sp.zeros(2))
gate = sp.simplify(H * Rz(sp.pi * t) * H)
unitX = (1 + sp.exp(sp.I * sp.pi * t)) / 2 * I2 + (1 - sp.exp(sp.I * sp.pi * t)) / 2 * X
check('M7 H diag(1,e^{i pi t}) H = unit(X) t (the gate flow of the exchange)',
      sp.simplify(gate - unitX) == sp.zeros(2))

# ---------------------------------------------------------------- C: chart continuity
# ball tower, field-neutral reading: preparation vectors b, effect u reads (1 + u.b)/2.
ex, ey = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0])
basis_preps = [ez, -ez, ex, ey]
labels = [ex, ey, ez]
R = RZ  # a flow member


def prob(u, b):
    return (1 + (u.T * b)[0]) / 2


P = [[prob(u, R * b) for b in basis_preps] for u in labels]           # 12 probability functions
c = [sp.Matrix([2 * P[j][k] - 1 for j in range(3)]) for k in range(4)]  # chart images of the basis
m = (c[0] + c[1]) / 2
A = sp.Matrix.hstack(c[2] - m, c[3] - m, c[0] - m)
check('C1 the chart matrix of the flow member is a fixed affine combination of 12 probabilities',
      sp.simplify(A - R) == sp.zeros(3) and sp.simplify(m) == sp.zeros(3, 1))
check('C2 datum-level group law: p(a, R(s+t) x) = p(a, R(s) R(t) x) for the 12 probabilities',
      all(sp.simplify(prob(u, RZ.subs(th, s + t) * b) - prob(u, RZ.subs(th, s) * (RZ.subs(th, t) * b))) == 0
          for u in labels for b in basis_preps))

# ---------------------------------------------------------------- N: completion-valued vs stage-valued
# 1-radian tower: stage n has the preparations at angles k (radians), |k| <= n, on the equator.
pi_iv = iv.pi
ok = True
for k in range(-50, 51):
    for j in range(-50, 51):
        for l in range(-20, 21):
            d = iv.mpf(j - k) - pi_iv * (2 * l + 1)   # zero iff angle k + pi = angle j mod 2 pi
            if d.a <= 0 <= d.b:
                ok = False
check('N1 the NOT (rotation by pi) maps no preparation of stages |k| <= 50 to a preparation', ok)
check('N2 the generator g = R_z(1) maps stage n into stage n+1 (Prep-valued, not stage-preserving)',
      sp.simplify(RZ.subs(th, 1) * RZ.subs(th, 3) - RZ.subs(th, 4)) == sp.zeros(3))

# ---------------------------------------------------------------- G: closure of one infinite-order operation
d1 = iv.mpf(355) - 113 * pi_iv
d2 = iv.mpf(710) - 226 * pi_iv
check('G1 g^355 = R_z(pi + delta), 0 < delta < 1e-4 (113 odd): powers approach the NOT',
      d1.a > 0 and d1.b < mpf('1e-4'))
check('G1 g^710 = R_z(delta), 0 < delta < 1e-4: powers approach the identity',
      d2.a > 0 and d2.b < mpf('1e-4'))
offok = True
for mm in range(1, 41):
    comm = sp.simplify(RX.subs(th, mm) * RZ.subs(th, mm) - RZ.subs(th, mm) * RX.subs(th, mm))
    e01 = comm[0, 1]   # sin(m)^2 * cos(m)-type entry; check it is nonzero rigorously
    val = iv.mpf(0)
    f = sp.lambdify([], e01, modules=[{'sin': iv.sin, 'cos': iv.cos}, 'mpmath'])
    v = f()
    if v.a <= 0 <= v.b:
        offok = False
check("G2 OFF-Gamma' on the control: J g^m J^-1 = R_x(m) does not commute with g^m = R_z(m), m = 1..40",
      offok)
R3 = RZ.subs(th, 2 * sp.pi / 3)
check('G3 finite order gives no flow: R_z(2pi/3)^3 = 1 and R_H^2 = 1',
      sp.simplify(R3 ** 3 - sp.eye(3)) == sp.zeros(3) and RH * RH == sp.eye(3))

# ---------------------------------------------------------------- X: countermodels
# X-CONT: a square-root tower of reversible operations that does not approach the identity.
alpha = [Fr(0), Fr(1)]     # angles in units of pi, mod 2
for n in range(1, 60):
    a = alpha[-1] / 2
    b = a + 1
    da = min(a % 2, 2 - a % 2)
    db = min(b % 2, 2 - b % 2)
    alpha.append(a if da >= db else b % 2)
sq = all(((2 * alpha[n + 1] - alpha[n]) % 2) == 0 for n in range(len(alpha) - 1))
far = all(Fr(1, 2) <= alpha[n] <= Fr(3, 2) for n in range(1, len(alpha)))
check('X-CONT branch tower: g_{n+1}^2 = g_n, g_0 = 1, g_1 = NOT, and every g_n (n>=1) stays at angle '
      'in [pi/2, 3pi/2]: no continuous extension', sq and far and alpha[0] == 0 and alpha[1] == 1)
reg = [Fr(0)] + [Fr(1, 2 ** (n - 1)) for n in range(1, 60)]
check('X-CONT control: the regular tower alpha_n = pi/2^(n-1) is a square-root tower tending to 1',
      all(((2 * reg[n + 1] - reg[n]) % 2) == 0 for n in range(len(reg) - 1)) and reg[-1] < Fr(1, 10 ** 15))
# X-LAW: continuous, affine-respecting, not a group: theta -> R_z(theta^2)
c4, c2 = iv.cos(iv.mpf(4)), iv.cos(iv.mpf(2))
check('X-LAW the family R_z(theta^2) is not additive: R_z(4) != R_z(1)R_z(1)... at s=t=1 (cos 4 != cos 2)',
      (c4 - c2).b < 0 or (c4 - c2).a > 0)
# X-OFF: in a disk every automorphism normalizes the rotation flow
R2 = lambda a: sp.Matrix([[sp.cos(a), -sp.sin(a)], [sp.sin(a), sp.cos(a)]])
F2 = lambda a: sp.Matrix([[sp.cos(a), sp.sin(a)], [sp.sin(a), -sp.cos(a)]])
check('X-OFF disk: J R(t) J^-1 = R(t) for rotations J, = R(-t) for reflections J',
      sp.simplify(R2(ph) * R2(t) * R2(-ph) - R2(t)) == sp.zeros(2)
      and sp.simplify(F2(ph) * R2(t) * F2(ph) - R2(-t)) == sp.zeros(2))
# X-FR: product of disks, block N rotating at frequency N: coordinatewise continuous, not uniformly
Nsym = sp.symbols('N', positive=True, integer=True)
e1 = sp.Matrix([1, 0])
disp = sp.simplify((R2(Nsym * sp.pi / Nsym) * e1 - e1).norm())
check('X-FR infinite rank: at t = pi/N block N is displaced by 2, so sup-norm continuity fails at 0',
      disp == 2)
# X-INV: a reset datum respects affine relations and is not reversible
reset = sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
check('X-INV reset to the centre: affine (linear part 0), maps the body in, not injective',
      reset.rank() == 0)
# X-VIS is M2; X-AR is M1 (and the landed midOp); X-INFORD is G3.

# ---------------------------------------------------------------- countercontrols (must report False)
cc = [
    ('CC1 claim H respects affine relations on diagonal effects', respects(W_diag, H)),
    ('CC2 claim z-axis invariant under R_H', invariant(ez, RH)),
    ('CC3 claim the branch tower tends to 1', alpha[-1] < Fr(1, 4)),
]
cc_ok = all(not v for _, v in cc)
for nme, v in cc:
    print(('expected-false OK ' if not v else 'COUNTERCONTROL BROKEN ') + nme)
npass = sum(1 for _, ok_ in RESULTS if ok_)
print(f"{'OK' if npass == len(RESULTS) and cc_ok else 'FAILED'} -- {npass}/{len(RESULTS)} checks, "
      f"{len(cc)} countercontrols {'expected-false' if cc_ok else 'BROKEN'}")

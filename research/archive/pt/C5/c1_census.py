#!/usr/bin/env python3
"""c1_census.py -- thread C5 (BRIDGE-COUNTER), stage 5, node C1: the minimal-subset census.

Question. For each subset S of the native single-token operations (the flow through the NOT, i.e. the rotations
about nflip's axis x; the NOT nflip itself; J = cyc3), idle-extended on one token (or both, where named), decide
for a closed cone K in W 3 with H1-H3 (products in K; cnot-invariance, at level (ii) the order-16 group
G16 = <cnot, Ad(Z(x)I), Ad(I(x)Z), T>; K = dualW K) and invariance under S, by the stage-4 criteria:
  UNIQUE    every pure state is reachable from the pure products under the closure of <cnot (or G16), S>;
            then K contains Q3 and K = Q3 (stage-4 Y1/Z claim D, [W]);
  EXOTIC-E  some pure state phi0 is unreachable, certified exactly by an overlap bound over the WHOLE reachable
            set; then the seed alpha*E00 - T_psi/4 with alpha >= f(psi) is invariant-subdual and EBF [W, audited
            AUDIT-X] gives an exotic invariant self-dual K (existence only; never called EXOTIC-X here).

DECISION RULE (fixed before the first run; rules, not expected numbers):
 R1 Transcription. cnot (Lean sgn/pc/pt, CompositeDimension.lean:741-786), actC/actT (CD:198-202), nflip (CD:797),
    cyc3 (KInfFoundations.lean:416-425), rot3 (KIF:411) and transposeW (FourCopyDefs.lean:49) are implemented from
    their Lean definitions and must equal the stated conjugations (Ad of explicit Gaussian-rational unitaries, or
    complex conjugation for T) on all 16 basis tables. Every unitary used must satisfy U U^dag = (scale) I exactly.
    Any mismatch: no VERDICT.
 R2 Lie closure. For a node, L = the smallest real subspace of su(4) (Pauli coordinates, Fractions) containing the
    node's flow generators and closed under commutators i[A,B] and under Ad(d) for every discrete generator d of
    the node (cnot, the node's NOT/J, and at level (ii) Ad(Z(x)I), Ad(I(x)Z), T). dim L and abelianness are exact.
 R3 UNIQUE iff L contains |p><p|(x)su(2) or su(2)(x)|p><p| for one of the six Pauli eigenstates p (the reachability
    criterion: the connected group then contains {|p><p|(x)V + |p'><p'|(x)I}, which carries a product to every
    pure state [W]); in addition the exact reachability witness for psi0 = phi0/4 and psi_a = (15,-1,7,7)/18 must
    verify (sympy, exact radicals) at level (i) for the UNIQUE nodes of the protocol's census.
 R4 EXOTIC-E iff (a) L is abelian, every basis element of L is local except at most one involutive non-local
    generator N (N^2 = I), (b) every discrete generator normalizes L exactly, and (c) the orbit of the ray of
    phi0 = (1, 2, 3i, -1+i) under the discrete group D (BFS on canonical rays, exact) gives
    d_low = min over the orbit of [ |det Psi|^2/n^2 if N absent; (det Q/tr Q)/n^2 with Q the 2x2 form of
    |det Psi(e^{-i b N} psi)|^2 in (cos 2b, sin 2b) if N present ] > 0, the form identity itself being checked at
    four rational points of the circle. Then A2 = 1 - 4 d_low bounds the squared marginal Bloch length over the
    whole reachable set; alpha = (1 + r)/2 with r rational, r^2 >= A2, r < 1, is the certified seed parameter.
 R5 A node certified both UNIQUE and EXOTIC-E is a FAIL (contradiction). A node with neither is UNDECIDED (printed,
    not a failure).
 R6 Countercontrols (each must fail as stated, else no VERDICT): (c1) the product |00> run through R4 gives
    A2 = 1 (no seed) on every EXOTIC-E node; (c2) on the torus nodes the reachable state CNOT|+0> (a Bell state)
    gives det Q = 0 or d_low = 0; (c3) every UNIQUE node's reachability witness reaches psi_a, a state certified
    unreachable for the S3 node (stage 4, Z z3), and phi0, the seed used for the EXOTIC-E nodes; (c4) the
    criterion R3 must fail on the flow-only node (the S3 instance); (c5) Q3 retention: every generator is an exact
    unitary or the antiunitary conjugation T, hence a Q3-automorphism [W].
 VERDICT line only if every R1 check, every certificate and every countercontrol is green.
"""
from fractions import Fraction as Fr
import itertools
import sys

# ---------------------------------------------------------------- exact Gaussian rationals and 4x4 matrices
class C:
    __slots__ = ('r', 'i')
    def __init__(s, r=0, i=0):
        s.r = Fr(r); s.i = Fr(i)
    def __add__(s, o): o = cc(o); return C(s.r + o.r, s.i + o.i)
    __radd__ = __add__
    def __sub__(s, o): o = cc(o); return C(s.r - o.r, s.i - o.i)
    def __rsub__(s, o): o = cc(o); return C(o.r - s.r, o.i - s.i)
    def __mul__(s, o): o = cc(o); return C(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    __rmul__ = __mul__
    def __neg__(s): return C(-s.r, -s.i)
    def conj(s): return C(s.r, -s.i)
    def __eq__(s, o): o = cc(o); return s.r == o.r and s.i == o.i
    def __hash__(s): return hash((s.r, s.i))
    def abs2(s): return s.r * s.r + s.i * s.i
    def __truediv__(s, o):
        o = cc(o); d = o.abs2(); n = s * o.conj(); return C(n.r / d, n.i / d)
    def iszero(s): return s.r == 0 and s.i == 0

def cc(x): return x if isinstance(x, C) else C(x, 0)
ZERO, ONE, IM = C(0), C(1), C(0, 1)

def mat(rows): return [[cc(x) for x in r] for r in rows]
def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), ZERO) for j in range(p)] for i in range(n)]
def dag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def conjm(A): return [[x.conj() for x in r] for r in A]
def kron(A, B):
    return [[A[i // len(B)][j // len(B[0])] * B[i % len(B)][j % len(B[0])]
             for j in range(len(A[0]) * len(B[0]))] for i in range(len(A) * len(B))]
def addm(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def subm(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scal(c, A): return [[cc(c) * x for x in r] for r in A]
def eye(n): return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
def tr(A): return sum((A[i][i] for i in range(len(A))), ZERO)
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def mv(A, v): return [sum((A[i][k] * v[k] for k in range(len(v))), ZERO) for i in range(len(A))]

I2 = mat([[1, 0], [0, 1]]); X = mat([[0, 1], [1, 0]]); Y = [[ZERO, C(0, -1)], [C(0, 1), ZERO]]
Z = mat([[1, 0], [0, -1]])
SIG = [I2, X, Y, Z]
P16 = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
UJ = scal(Fr(1, 2), [[C(1, -1), C(-1, -1)], [C(1, -1), C(1, 1)]])      # (I - i(X+Y+Z))/2
P0 = mat([[1, 0], [0, 0]]); P1 = mat([[0, 0], [0, 1]])
CNOT = addm(kron(P0, I2), kron(P1, X))                                    # control first, z3 -> |0>

def table(M):
    t = []
    for m in range(4):
        row = []
        for n in range(4):
            v = tr(mm(M, P16[m][n]))
            assert v.i == 0, 'non-Hermitian input to table'
            row.append(v.r)
        t.append(row)
    return t
def from_table(w):
    M = [[ZERO] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            if w[m][n] != 0:
                M = addm(M, scal(Fr(w[m][n]) / 4, P16[m][n]))
    return M
def basis_table(m, n): return [[Fr(1) if (a, b) == (m, n) else Fr(0) for b in range(4)] for a in range(4)]
def ad_table(U, scale=Fr(1)):
    return lambda w: [[x / scale for x in r] for r in table(mm(mm(U, from_table(w)), dag(U)))]
def T_table(w): return table(conjm(from_table(w)))
def unitary(U, scale=Fr(1)): return meq(mm(U, dag(U)), scal(scale, eye(len(U))))

# ---------------------------------------------------------------- the Lean definitions, transcribed
def sgn(m, n): return -1 if (m, n) in ((1, 3), (2, 2)) else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnotFun(w): return [[sgn(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]
def homMap(N3, v):            # N3: 3x3 rational matrix; v: HVec (4 entries), index 0 fixed
    tail = v[1:]
    return [v[0]] + [sum(N3[i][k] * tail[k] for k in range(3)) for i in range(3)]
def actT(N3, w): return [homMap(N3, w[m]) for m in range(4)]
def actC(N3, w):
    cols = [homMap(N3, [w[k][n] for k in range(4)]) for n in range(4)]
    return [[cols[n][m] for n in range(4)] for m in range(4)]
NFLIP = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
CYC3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]                                 # v -> (v2, v0, v1)
CYC3INV = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
def rot3(c, s): return [[c, -s, 0], [s, c, 0], [0, 0, 1]]
def m3(A, B): return [[sum(Fr(A[i][k]) * Fr(B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]
SGNY = [1, 1, -1, 1]
def transposeW(w): return [[SGNY[m] * SGNY[n] * w[m][n] for n in range(4)] for m in range(4)]

OUT = []
FAILS = []
def check(cid, ok, text):
    OUT.append(('PASS ' if ok else 'FAIL ') + cid + ' ' + text)
    if not ok:
        FAILS.append(cid)

def same_map(f, g):
    return all(f(basis_table(m, n)) == g(basis_table(m, n)) for m in range(4) for n in range(4))

# ---------------------------------------------------------------- R1: transcription checks
def run_transcription():
    U5z = addm(scal(2, I2), scal(C(0, -1), Z))          # 2I - iZ, |.|^2 = 5: Rz(t), cos t = 3/5, sin t = 4/5
    U5x = addm(scal(2, I2), scal(C(0, -1), X))          # 2I - iX: Rx(t), same t
    check('T0', all([unitary(CNOT), unitary(kron(UJ, I2)), unitary(kron(X, I2)), unitary(kron(Z, I2)),
                     unitary(U5z, Fr(5)), unitary(U5x, Fr(5))]),
          'CNOT, UJ(x)I, X(x)I, Z(x)I exact unitaries; 2I-iZ, 2I-iX unitary up to scale 5')
    check('T1', same_map(cnotFun, ad_table(CNOT)), 'Lean cnotFun (sgn/pc/pt) = Ad(CNOT), CNOT = P0(x)I + P1(x)X, all 16 basis tables')
    check('T2', same_map(lambda w: actC(NFLIP, w), ad_table(kron(X, I2))) and
                same_map(lambda w: actT(NFLIP, w), ad_table(kron(I2, X))),
          'actC nflip = Ad(X(x)I), actT nflip = Ad(I(x)X)')
    check('T3', same_map(lambda w: actC(CYC3, w), ad_table(kron(UJ, I2))) and
                same_map(lambda w: actT(CYC3, w), ad_table(kron(I2, UJ))),
          'actC cyc3 = Ad(UJ(x)I), actT cyc3 = Ad(I(x)UJ), UJ = (I - i(X+Y+Z))/2')
    R = rot3(Fr(3, 5), Fr(4, 5))
    check('T4', same_map(lambda w: actC(R, w), ad_table(kron(U5z, I2), Fr(5))) and
                same_map(lambda w: actT(R, w), ad_table(kron(I2, U5z), Fr(5))),
          'actC/actT rot3(t) = Ad(Rz(t)) at cos t = 3/5, sin t = 4/5 (ball3Drive flow, axis z)')
    RX = m3(m3(CYC3, R), CYC3INV)
    RPI = rot3(Fr(-1), Fr(0))
    check('T5', same_map(lambda w: actC(RX, w), ad_table(kron(U5x, I2), Fr(5))) and
                m3(m3(CYC3, RPI), CYC3INV) == [[Fr(x) for x in r] for r in NFLIP] and
                RPI == [[Fr(-1), 0, 0], [0, Fr(-1), 0], [0, 0, Fr(1)]],
          'cyc3 . rot3 t . cyc3^-1 = Ad(Rx(t)) (the flow through nflip); at t = pi it is nflip; rot3 pi = diag(-1,-1,1) is not nflip')
    check('T6', same_map(transposeW, T_table), 'transposeW = complex conjugation T on tables')
    check('T7', all(m3(CYC3, CYC3INV)[i][j] == (1 if i == j else 0) for i in range(3) for j in range(3)) and
                m3(m3(CYC3, CYC3), CYC3) == [[Fr(int(i == j)) for j in range(3)] for i in range(3)],
          'cyc3 has order 3 and CYC3INV is its inverse')

# ---------------------------------------------------------------- Lie algebra in Pauli coordinates
def coords(H):
    v = []
    for m in range(4):
        for n in range(4):
            if (m, n) == (0, 0):
                continue
            t = tr(mm(H, P16[m][n]))
            assert t.i == 0
            v.append(t.r / 4)
    return v
def reduce_vec(basis, v):
    v = list(v)
    for piv, b in basis:
        if v[piv] != 0:
            f = v[piv]
            v = [x - f * y for x, y in zip(v, b)]
    return v
def add_basis(basis, v):
    r = reduce_vec(basis, v)
    nz = [k for k, x in enumerate(r) if x != 0]
    if not nz:
        return False
    piv = nz[0]
    r = [x / r[piv] for x in r]
    nb = []
    for p, b in basis:
        if b[piv] != 0:
            f = b[piv]
            b = [x - f * y for x, y in zip(b, r)]
        nb.append((p, b))
    nb.append((piv, r))
    basis[:] = nb
    return True
def comm(A, B): return scal(IM, subm(mm(A, B), mm(B, A)))
def make_ad(d):
    if d == 'T':
        return conjm
    return lambda H: mm(mm(d, H), dag(d))
def lie_closure(gens, discrete):
    basis, mats, queue = [], [], list(gens)
    ads = [make_ad(d) for d in discrete]
    while queue:
        H = queue.pop()
        if not add_basis(basis, coords(H)):
            continue
        for K in mats:
            queue.append(comm(H, K))
        for f in ads:
            queue.append(f(H))
        mats.append(H)
    return basis, mats
def in_span(basis, H): return all(x == 0 for x in reduce_vec(basis, coords(H)))
def is_abelian(mats): return all(all(x == 0 for x in coords(comm(A, B))) for A in mats for B in mats)

def criterion(basis):
    for k in (1, 2, 3):
        for s in (1, -1):
            proj = scal(Fr(1, 2), addm(I2, scal(s, SIG[k])))
            if all(in_span(basis, kron(proj, SIG[j])) for j in (1, 2, 3)):
                return ('T', k, s)        # |p><p| (x) su(2): control branch p, target rotated
            if all(in_span(basis, kron(SIG[j], proj)) for j in (1, 2, 3)):
                return ('C', k, s)        # su(2) (x) |p><p|: target branch p, control rotated
    return None

# ---------------------------------------------------------------- R4: tori and finite groups, exact seeds
LOCAL = [kron(SIG[k], I2) for k in (1, 2, 3)] + [kron(I2, SIG[k]) for k in (1, 2, 3)]
NONLOCAL = [(a, b, kron(SIG[a], SIG[b])) for a in (1, 2, 3) for b in (1, 2, 3)]
def torus_structure(basis, mats):
    if not is_abelian(mats):
        return None
    loc = [H for H in LOCAL if in_span(basis, H)]
    non = [(a, b, H) for (a, b, H) in NONLOCAL if in_span(basis, H)]
    if len(non) > 1 or len(loc) + len(non) != len(basis):
        return None
    return (loc, non[0][2] if non else None, (non[0][0], non[0][1]) if non else None)
def canon(v):
    k = next(i for i, x in enumerate(v) if not x.iszero())
    piv = v[k]
    return tuple((x / piv) for x in v)
def act_ray(d, v):
    if d == 'T':
        return canon([x.conj() for x in v])
    return canon(mv(d, list(v)))
def orbit(v0, discrete, cap=300000):
    start = canon(v0)
    seen = {start}
    todo = [start]
    while todo:
        v = todo.pop()
        for d in discrete:
            w = act_ray(d, v)
            if w not in seen:
                seen.add(w)
                todo.append(w)
                if len(seen) > cap:
                    return None
    return seen
def det2(v): return v[0] * v[3] - v[1] * v[2]
def nrm(v): return sum((x.abs2() for x in v), Fr(0))
def det_bound(v, N):
    """exact lower bound on min_b |det Psi(e^{-ibN} v)|^2 / |v|^4, with the form identity checked."""
    n = nrm(v)
    D = det2(v)
    if N is None:
        return D.abs2() / (n * n), True
    vN = mv(N, list(v))
    DN = det2(vN)
    m = det2([a + b for a, b in zip(v, vN)]) - D - DN
    ok = (DN == D)
    for (c, s) in ((Fr(1), Fr(0)), (Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(-12, 13)), (Fr(-8, 17), Fr(15, 17))):
        w = [cc(c) * a + C(0, -s) * b for a, b in zip(v, vN)]          # (cos b - i sin b N) v
        lhs = det2(w)
        rhs = cc(c * c - s * s) * D + C(0, -c * s) * m
        ok = ok and (lhs == rhs)
    u, wv = D, C(0, Fr(-1, 2)) * m
    q11, q22 = u.abs2(), wv.abs2()
    q12 = (u * wv.conj()).r
    detQ, trQ = q11 * q22 - q12 * q12, q11 + q22
    if trQ == 0:
        return Fr(0), ok
    return (detQ / trQ) / (n * n), ok
def isqrt_up(q, den):
    num = q * den * den
    k = int(num.numerator // num.denominator)
    import math
    k = math.isqrt(k)
    while Fr(k * k) < num:
        k += 1
    return Fr(k, den)
def seed_alpha(dlow):
    A2 = 1 - 4 * dlow
    if A2 >= 1:
        return A2, None
    den = 10 ** 6
    while True:
        r = isqrt_up(A2, den)
        if r < 1:
            break
        den *= 10
    assert r * r >= A2
    return A2, (1 + r) / 2

# ---------------------------------------------------------------- R3: exact reachability witness (sympy, radicals)
def witness(side, k, s, psi_list):
    import sympy as sp
    r2 = sp.sqrt(2)
    EIG = {(1, 1): [1 / r2, 1 / r2], (1, -1): [1 / r2, -1 / r2], (2, 1): [1 / r2, sp.I / r2],
           (2, -1): [1 / r2, -sp.I / r2], (3, 1): [sp.Integer(1), sp.Integer(0)], (3, -1): [sp.Integer(0), sp.Integer(1)]}
    p, q = EIG[(k, s)], EIG[(k, -s)]
    psi = [sp.Rational(x.r) + sp.I * sp.Rational(x.i) for x in psi_list]
    n = sp.sqrt(sum(sp.Abs(x) ** 2 for x in psi))
    psi = [sp.nsimplify(x / n) for x in psi]
    if side == 'C':
        u = [sum(sp.conjugate(p[j]) * psi[2 * i + j] for j in range(2)) for i in range(2)]
        v = [sum(sp.conjugate(q[j]) * psi[2 * i + j] for j in range(2)) for i in range(2)]
    else:
        u = [sum(sp.conjugate(p[i]) * psi[2 * i + j] for i in range(2)) for j in range(2)]
        v = [sum(sp.conjugate(q[i]) * psi[2 * i + j] for i in range(2)) for j in range(2)]
    nu = sp.sqrt(sp.simplify(sum(sp.Abs(x) ** 2 for x in u)))
    nv = sp.sqrt(sp.simplify(sum(sp.Abs(x) ** 2 for x in v)))
    if nu == 0 or nv == 0:
        return True, 'product'
    def W(x, nx): return sp.Matrix([[x[0], -sp.conjugate(x[1])], [x[1], sp.conjugate(x[0])]]) / nx
    V = W(u, nu) * W(v, nv).H
    Pp = sp.Matrix(2, 1, p) * sp.Matrix(2, 1, p).H
    Pq = sp.Matrix(2, 1, q) * sp.Matrix(2, 1, q).H
    I2s = sp.eye(2)
    pv, qv = sp.Matrix(2, 1, p), sp.Matrix(2, 1, q)
    if side == 'C':
        g = sp.kronecker_product(V, Pp) + sp.kronecker_product(I2s, Pq)
        a = sp.Matrix(2, 1, v) / nv
        b = nu * pv + nv * qv
    else:
        g = sp.kronecker_product(Pp, V) + sp.kronecker_product(Pq, I2s)
        a = nu * pv + nv * qv
        b = sp.Matrix(2, 1, v) / nv
    img = g * sp.kronecker_product(a, b)
    ok = all(sp.simplify(sp.expand(img[i] - psi[i])) == 0 for i in range(4))
    ok = ok and sp.simplify(sp.expand((V * V.H - I2s).norm())) == 0 and sp.simplify(sp.expand(V.det() - 1)) == 0
    return ok, 'reached'

# ---------------------------------------------------------------- the census
XI, IXm = kron(X, I2), kron(I2, X)
ZI, IZ = kron(Z, I2), kron(I2, Z)
JC, JT = kron(UJ, I2), kron(I2, UJ)
LEVEL2 = [ZI, IZ, 'T']
PHI0 = [C(1), C(2), C(0, 3), C(-1, 1)]
PSIA = [C(15), C(-1), C(7), C(7)]
PROD00 = [C(1), C(0), C(0), C(0)]
BELL = [C(1), C(0), C(0), C(1)]
NODES = [  # (id, protocol subset, flow generators, extra discrete elements, census?)
    ('flow@C', '{flow} control', [XI], [], True),
    ('flow@T', '{flow} target', [IXm], [], True),
    ('flow@CT', '{flow on both tokens}', [XI, IXm], [], True),
    ('flowNOT@C', '{flow, NOT} control', [XI], [XI], True),
    ('flowNOT@T', '{flow, NOT} target', [IXm], [IXm], True),
    ('J@C', '{J} control', [], [JC], True),
    ('J@T', '{J} target', [], [JT], True),
    ('NOTJ@C', '{NOT, J} control', [], [XI, JC], True),
    ('NOTJ@T', '{NOT, J} target', [], [IXm, JT], True),
    ('flowJ@C', '{flow, J} control', [XI], [JC], True),
    ('flowJ@T', '{flow, J} target', [IXm], [JT], True),
    ('flow@C+J@T', 'record: flow control, J target', [XI], [JT], False),
    ('flow@T+J@C', 'record: flow target, J control', [IXm], [JC], False),
    ('flow@C+NOT@T', 'record: flow control, NOT target', [XI], [IXm], False),
    ('NOT@C', 'record: {NOT} control', [], [XI], False),
    ('NOT@T', 'record: {NOT} target', [], [IXm], False),
    ('NOT@CT', 'record: {NOT} both tokens', [], [XI, IXm], False),
    ('J@CT', 'record: {J} both tokens', [], [JC, JT], False),
    ('NOTJ@CT', 'record: {NOT, J} both tokens', [], [XI, IXm, JC, JT], False),
    ('zflow@C', 'record: ball3Drive flow (axis z) control', [ZI], [], False),
    ('zflow@T', 'record: ball3Drive flow (axis z) target', [IZ], [], False),
    ('zflow@CT', 'record: ball3Drive flow both tokens', [ZI, IZ], [], False),
    ('zflowJ@C', 'record: {ball3Drive flow, J} control', [ZI], [JC], False),
    ('zflowJ@T', 'record: {ball3Drive flow, J} target', [IZ], [JT], False),
]

def seed_for(basis, mats, discrete, v0):
    ts = torus_structure(basis, mats)
    if ts is None:
        return None
    loc, N, Nlab = ts
    orb = orbit(v0, discrete)
    if orb is None:
        return None
    dl, ok = None, True
    for v in orb:
        d, okv = det_bound(list(v), N)
        ok = ok and okv
        dl = d if dl is None else min(dl, d)
    A2, alpha = seed_alpha(dl)
    return dict(nloc=len(loc), N=Nlab, orbit=len(orb), dlow=dl, A2=A2, alpha=alpha, formok=ok)

def main():
    run_transcription()
    # G16 order as a signed-permutation group on tables (stage-3/4 definition), and Loc8
    def sp_of(f):
        cols = []
        for m in range(4):
            for n in range(4):
                img = f(basis_table(m, n))
                nz = [(a, b) for a in range(4) for b in range(4) if img[a][b] != 0]
                if len(nz) != 1 or abs(img[nz[0][0]][nz[0][1]]) != 1:
                    return None
                cols.append((nz[0][0] * 4 + nz[0][1], img[nz[0][0]][nz[0][1]]))
        perm = [None] * 16
        for src, (dst, sg) in enumerate(cols):
            perm[dst] = (src, sg)
        return tuple(perm)
    def compose(p, q):      # (p o q)
        return tuple((q[src][0], sg * q[src][1]) for (src, sg) in p)
    def gen_group(gens):
        idt = tuple((i, 1) for i in range(16))
        G, todo = {idt}, [idt]
        while todo:
            x = todo.pop()
            for g in gens:
                y = compose(g, x)
                if y not in G:
                    G.add(y); todo.append(y)
        return G
    g_cnot, g_zi, g_iz, g_t = sp_of(cnotFun), sp_of(ad_table(ZI)), sp_of(ad_table(IZ)), sp_of(transposeW)
    G16 = gen_group([g_cnot, g_zi, g_iz, g_t])
    Loc8 = gen_group([g_zi, g_iz, g_t])
    check('G1', len(G16) == 16 and len(Loc8) == 8 and
          G16 == Loc8 | {compose(g_cnot, l) for l in Loc8},
          '|G16| = 16, |Loc8| = 8, G16 = Loc8 u cnot.Loc8 (signed permutations of the 16 entries)')
    RES = {}
    for (nid, label, flows, extra, census) in NODES:
        res = {}
        for lev, disc in (('i', [CNOT] + extra), ('ii', [CNOT] + extra + LEVEL2)):
            basis, mats = lie_closure(flows, disc)
            crit = criterion(basis)
            res[lev] = dict(dim=len(basis), abelian=is_abelian(mats), crit=crit, basis=basis, mats=mats, disc=disc)
        RES[nid] = res
        ri, rii = res['i'], res['ii']
        verdict, seed, seedlev = None, None, None
        if ri['crit'] is not None:
            verdict = 'UNIQUE at (i) and (ii)'
        else:
            lev = 'ii' if rii['crit'] is None else 'i'
            seed = seed_for(res[lev]['basis'], res[lev]['mats'], res[lev]['disc'], PHI0)
            seedlev = lev
            if seed is not None and seed['alpha'] is not None and seed['formok']:
                verdict = ('EXOTIC-E at (i) and (ii)' if lev == 'ii' else 'UNIQUE at (ii); EXOTIC-E at (i)')
            else:
                verdict = 'UNDECIDED'
        res['verdict'], res['seed'], res['seedlev'] = verdict, seed, seedlev
        line = (nid + ' [' + label + ']: dim L(i)=' + str(ri['dim']) + (' abelian' if ri['abelian'] else ' non-abelian') +
                ', dim L(ii)=' + str(rii['dim']) + (' abelian' if rii['abelian'] else ' non-abelian') +
                ', criterion(i)=' + str(ri['crit']) + ', criterion(ii)=' + str(rii['crit']))
        if seed is not None:
            line += (', seed@(' + seedlev + '): local gens ' + str(seed['nloc']) + ', N=' + str(seed['N']) +
                     ', orbit ' + str(seed['orbit']) + ', d_low=' + str(seed['dlow']) + ', A2<=' + str(seed['A2']) +
                     ', alpha=' + str(seed['alpha']) + ', form identity ' + ('ok' if seed['formok'] else 'FAILED'))
        OUT.append('NODE ' + line + ' => ' + verdict)
    return RES

def controls(RES):
    # c5 / Q3 retention: every discrete generator is an exact unitary (T is the antiunitary conjugation)
    mats_all = [CNOT, XI, IXm, ZI, IZ, JC, JT]
    check('c5', all(unitary(M) for M in mats_all),
          'Q3 retention: CNOT, X(x)I, I(x)X, Z(x)I, I(x)Z, UJ(x)I, I(x)UJ exact unitaries (flows are exp(-itP), P a Pauli product)')
    # c4: the S3 instance must not pass the criterion
    check('c4', RES['flow@C']['ii']['crit'] is None and RES['flow@C']['i']['crit'] is None,
          'countercontrol: the reachability criterion fails on {flow} control (the stage-4 S3 instance)')
    for nid, res in RES.items():
        v = res['verdict']
        if v.startswith('EXOTIC-E') or v.startswith('UNIQUE at (ii); EXOTIC-E'):
            lev = res['seedlev']
            sp0 = seed_for(res[lev]['basis'], res[lev]['mats'], res[lev]['disc'], PROD00)
            check('c1-' + nid, sp0 is not None and sp0['alpha'] is None and sp0['A2'] == 1,
                  'countercontrol: the product |00> gives A2 = 1, no seed')
            sb = seed_for(res[lev]['basis'], res[lev]['mats'], res[lev]['disc'], BELL)
            check('c2-' + nid, sb is not None and sb['alpha'] is None and sb['dlow'] == 0,
                  'countercontrol: the reachable Bell state CNOT|+0> gives d_low = 0, no seed')
        if v.startswith('UNIQUE at (i)'):
            ri = res['i']
            s5 = seed_for(ri['basis'], ri['mats'], ri['disc'], PHI0)
            check('R5-' + nid, s5 is None or s5['alpha'] is None,
                  'no seed is certified on a UNIQUE node (L(i) non-abelian or no bound)')
            side, k, s = ri['crit']
            ok1, how1 = witness(side, k, s, PHI0)
            ok2, how2 = witness(side, k, s, PSIA)
            check('c3-' + nid, ok1 and ok2,
                  'reachability witness at level (i), side ' + side + ', p = eigenvector of sigma_' + str(k) +
                  ' with eigenvalue ' + str(s) + ': phi0 ' + how1 + ', psi_a ' + how2 + ' (exact radicals)')
    # the seed identities (stage-4 Z claim D), once, at psi = phi0/4 and the flow@C alpha
    alpha = RES['flow@C']['seed']['alpha']
    psi = [x / 4 for x in PHI0]
    Tpsi = table([[a * b.conj() for b in psi] for a in psi])
    E00 = basis_table(0, 0)
    e = [[alpha * E00[m][n] - Tpsi[m][n] / 4 for n in range(4)] for m in range(4)]
    def ipW(A, B): return sum(A[m][n] * B[m][n] for m in range(4) for n in range(4))
    def pure_table(v):
        nn = nrm(v)
        return [[x / nn for x in r] for r in table([[a * b.conj() for b in v] for a in v])]
    def ov(u, v):
        s = sum((a.conj() * b for a, b in zip(u, v)), ZERO)
        return s.abs2() / (nrm(u) * nrm(v))
    ok = mv(from_table(e), psi) == [cc((alpha - 1) / 4) * x for x in psi]
    tests = [PROD00, [C(1), C(1), C(0), C(0)], mv(CNOT, [C(1), C(0), C(1), C(0)]), [C(2), C(-1), C(1), C(3)]]
    for t in tests:
        ok = ok and ipW(e, pure_table(t)) == alpha - ov(psi, t)
    ok = ok and ipW(e, cnotFun(e)) == alpha * alpha - alpha / 2 + ov(psi, mv(CNOT, psi)) / 4
    ok = ok and ipW(e, pure_table(psi)) == alpha - 1 and alpha - 1 < 0
    check('S1', ok, 'seed identities at psi = phi0/4, alpha = ' + str(alpha) +
          ': pauliW(e)psi = (alpha-1)/4 psi; <e,T_phi> = alpha - |<psi|phi>|^2 (4 states); '
          '<e, cnot e> = alpha^2 - alpha/2 + |<psi|CNOT psi>|^2/4; <e, T_psi> = alpha - 1 < 0')

if __name__ == '__main__':
    RES = main()
    controls(RES)
    for l in OUT:
        print(l)
    print('SUMMARY census (protocol subsets):')
    for (nid, label, flows, extra, census) in NODES:
        r = RES[nid]
        sd = r['seed']
        extra_s = ('' if sd is None or sd['alpha'] is None else ' seed alpha=' + str(sd['alpha']) + ' at level (' + r['seedlev'] + ')')
        print('  ' + ('CENSUS ' if census else 'RECORD ') + nid + ': ' + r['verdict'] + extra_s)
    nfail = len(FAILS)
    print('CHECKS: ' + str(sum(1 for l in OUT if l.startswith('PASS'))) + ' PASS, ' + str(nfail) + ' FAIL')
    undec = [nid for (nid, _, _, _, c) in NODES if RES[nid]['verdict'] == 'UNDECIDED']
    if nfail == 0:
        print('VERDICT C1-CENSUS-EXACT (undecided nodes: ' + (', '.join(undec) if undec else 'none') + ')')
    else:
        print('NO VERDICT: failures ' + ', '.join(FAILS))

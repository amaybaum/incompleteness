# r2_cones.py -- R6 node R2: exact checks on the explicit stage-3 cones K(E0) (level (i)) and K(Z_F) (level (ii)).
# DECISION RULE (fixed before the first run, 18:13Z by date -u):
#  Transcribed from L (CompositeDimension.lean:97-202, :741-798; K2Guard.lean:40-110): hom, homMap, prodState, actT, actC,
#  sgn/pc/pt/cnot, z3, nflip, xplus, phiW, reflY, idW, chainW. From the design module [D] (FourCopyDefs.lean:25-49,
#  FourCopyPackage.lean:172-183): ipW, tabMul, tabT, transposeW, pauliW. pauliW is not a kernel object at L, so every
#  check that passes through it is evidence [X via D].
#  D0 dictionary: cnotFun = Ad(CNOT) control-first on all 16 basis tables; actC R(U) = Ad(U(x)I), actT R(U) = Ad(I(x)U)
#     for U in {X, Z, U_J, U_x90}; R(U_J) = cyc3 (x->y->z->x); actT reflY = target partial transpose; transposeW = global
#     transpose = actC reflY o actT reflY.
#  D1 (K-independent, [K] re-checked): cnot involutive, ipW-orthogonal, symmetric; relT, relC with nflip on 16 basis
#     tables; frame at the four corner products; IsNot nflip; cnot(prodState xplus z3) = phiW of rank 4 and pauliW(phiW)
#     a rank-one projector; posFwd/posInv identity ipW(prodState a b, cnot prodState x y) = 4 tr(rho_a(x)rho_b CNOT
#     rho_x(x)rho_y CNOT^dag) (symbolic). Countercontrol D1c: relT and relC FAIL for N = reflY.
#  For each cone K(Z) (Z = {E0}, Z = Z_F):
#  C1 H1: symbolic SOS identity of each defect over the whole ball; pauliW(prodState x y) = rho(x)(x)rho(y) (symbolic).
#  C2 H2: cnot Z = Z as a set; Z_F also permuted by Ad(Z(x)I), Ad(I(x)Z), transposeW; record: ipW(E0, Ad(Z(x)I)E0) = -1.
#  C3 H3 certificates (SD1/SD2, audited stage 3): each pauliW(z) has exactly one negative eigenvalue -a, all others >= a;
#     Z pairwise ipW-orthogonal. Countercontrols: e_{3/2} FAILS the eigenvalue condition; {E0, Ad(Z(x)I)E0} FAILS
#     orthogonality.
#  C4 K != Q3: z not PSD; T_g (g the negative eigenvector) has ipW(z, T_g) < 0, so T_g is not in K = K*.
#  C5 maxCone bound: C1's identity is homogeneous of degree (1,1), so ipW(z, a(x)b) >= 0 for Lorentz a, b [W from C1].
#  C6 slice: cnot and the G16 generators fix the (0,0) entry of every table.
#  C7 I3.44 consistency: a z in Z and a w in K with ipW(actT reflY z, w) < 0; control: actT reflY phiW = idW not PSD.
#  C8 one-token maps (the do-not-assume (b) family; a FAIL there is a hypothesis failure): for g in {actC rot3(pi),
#     actT nflip, actC nflip, actC cyc3, actT cyc3, actC Rx(pi/2), actC R_n(pi/2) n=(3,0,4)/5, actC R1 (order 3 about
#     (5,1,1))} and the two-token SWAP: a witness w in K (a defect of Z, or the pure table of a candidate vector with
#     ipW(z', w) >= 0 for all z' in Z) with ipW(g z, w) < 0. Candidates: eigenvectors of each pauliW(z), their images
#     under the map's unitary and its inverse. No witness in the list prints NOWITNESS (no claim, not a failure);
#     invariance is printed where g permutes Z. Control: Q3 maps into Q3 (the image of every candidate table is PSD).
#  C9 FCC famI, uniform assignment: min over X, Y in Z and E, F in the 72 tables prodState(+-e_i, +-e_j) and their cnot
#     images (all in K = dualW K) of ipW(X, tabMul(tabMul E Y)(tabT F)); FCC FAILS iff min < 0. Control: Q3 with
#     X, Y in {phiW, prodState(z3,z3), cnot prodState(xplus,xplus)}: min >= 0.
#  C10 SF pair transfer (I4.236): e_P with pauliW = P/4, P = |0><0|(x)I, and E00 - e_P lie in K; e_P = 1 on prodState(z3,
#     +-z3), 0 on prodState(-z3, z3): SingletonFaces fails on the slice of K and of Q3 alike (record).
#  VERDICT R2-CONES-EXACT printed only if every check passes and every countercontrol fails as stated.
#  RUN 4 (18:17:16Z): amendment timestamps corrected to `date -u`; code identical to run 3.
#  RUN 5 (18:17:36Z): the run-4 line above had an estimated time; corrected; code identical to run 3.
#  RUN-2 AMENDMENT (18:15:56Z, after run 1, kept as r2_cones.run1.*, failed C1 K(E0), C7 K(E0), C9 K(Z_F)):
#   C1: the identity is 2v/c0 = |x + (M/c0)y|^2 + y^T(I - M^T M/c0^2)y + (1-|x|^2) + (1-|y|^2) with I - M^T M/c0^2 PSD
#       (run 1 assumed M orthogonal; E0's bilinear part has rank 2) -- implementation of the stated rule;
#   C7/C8: the candidate pool adds the eigenvectors of the moved table g z and, for a defect, the slides
#       psi' - (k/8) c_t psi_t (k = 1..8, t the largest component of psi' in the defect basis) -- run 1's pool missed the
#       joint eigenvector inside a degenerate eigenspace;
#   C9: E and F range over the 72 tables and the defects of Z (all in K = dualW K); with X, Y over Z this covers famI and
#       famII alike for a uniform self-dual assignment. Run 1's pool of products only gave min 0 for K(Z_F).
#  RUN-3 AMENDMENT (18:16:53Z, after run 2, kept as r2_cones.run2.*, failed C9 K(Z_F) with min 0): C9 takes X over Z and
#   Y, E, F over the 72 tables and Z (run 2 kept Y in Z). The stage-3 thread X's x8 output (read at 18:16Z, before this amendment) locates the
#   K(Z_F) violation at Y = cnot prodState(e2, e2). Integer arithmetic on tables scaled by 4. Q3 control: X over
#   {phiW, prodState(z3,z3), cnot prodState(xplus,xplus)}, Y, E, F over the 72 tables.
import sympy as sp
from fractions import Fraction as Fr
from itertools import product

iu, Rt = sp.I, sp.Rational
s = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
SS = [[kron(s[m], s[n]) for n in range(4)] for m in range(4)]
def pW(w): return sp.expand(sum((w[m, n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4)
def table(A):
    t = sp.Matrix(4, 4, lambda m, n: sp.expand((A * SS[m][n]).trace()))
    assert all(sp.im(x) == 0 for x in t), 'non-real table'
    return t.applyfunc(sp.re)
def ip(a, b): return sp.expand(sum(a[m, n] * b[m, n] for m in range(4) for n in range(4)))
def E(m, n):
    t = sp.zeros(4, 4); t[m, n] = 1; return t
def hom(x): return sp.Matrix([1] + list(x))
def prod(x, y): return hom(x) * hom(y).T
def Hom(N): H = sp.eye(4); H[1:, 1:] = N; return H
def actC(N, w): return Hom(N) * w
def actT(N, w): return w * Hom(N).T
SGN = lambda m, n: -1 if (m, n) in [(1, 3), (2, 2)] else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnot(w): return sp.Matrix(4, 4, lambda m, n: SGN(m, n) * w[PC[m][n], PT[m][n]])
z3, xplus = [0, 0, 1], [1, 0, 0]
nflip, reflY = sp.diag(1, -1, -1), sp.diag(1, -1, 1)
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
P0, P1 = sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]])
CNOT = kron(P0, s[0]) + kron(P1, s[1])
def Rof(U): return sp.Matrix(3, 3, lambda i, j: sp.nsimplify(sp.expand((s[i + 1] * U * s[j + 1] * U.H).trace() / 2)))
def ptT(A): return sp.Matrix(4, 4, lambda i, j: A[2 * (i // 2) + j % 2, 2 * (j // 2) + i % 2])
def transposeW(w): return sp.Matrix(4, 4, lambda m, n: (-1 if m == 2 else 1) * (-1 if n == 2 else 1) * w[m, n])
def Tpure(v):
    v = sp.Matrix(v); return table(v * v.H / sp.expand((v.H * v)[0]))
RES = {}
def chk(cid, ok, note=''):
    RES[cid] = bool(ok); print('CHECK %-26s %s %s' % (cid, 'PASS' if ok else 'FAIL', note))

# ---- D0 dictionary
basis = [E(m, n) for m in range(4) for n in range(4)]
chk('D0a cnot=Ad(CNOT)', all(table(CNOT * pW(b) * CNOT.H) == cnot(b) for b in basis), '16/16 basis tables, control first')
UJ = (s[0] - iu * (s[1] + s[2] + s[3])) / 2
Ux90 = (s[0] - iu * s[1]) / sp.sqrt(2)
cyc3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
chk('D0b R(U_J)=cyc3', Rof(UJ) == cyc3, 'x->y->z->x')
chk('D0b R(X)=nflip', Rof(s[1]) == nflip, 'nflip = R_x(pi)')
ok = True
for U in [s[1], s[3], UJ, Ux90]:
    R = Rof(U)
    ok &= all(table(kron(U, s[0]) * pW(b) * kron(U, s[0]).H) == actC(R, b) for b in basis)
    ok &= all(table(kron(s[0], U) * pW(b) * kron(s[0], U).H) == actT(R, b) for b in basis)
chk('D0c actC/actT=Ad', ok, 'U in {X, Z, U_J, U_x90}, 16 basis tables each')
chk('D0d actT reflY=pT_B', all(table(ptT(pW(b))) == actT(reflY, b) for b in basis), 'target partial transpose')
chk('D0e transposeW=T', all(table(pW(b).T) == transposeW(b) == actC(reflY, actT(reflY, b)) for b in basis), 'global transpose')
# ---- D1 gate and NOT identities
Mc = sp.Matrix(16, 16, lambda i, j: cnot(basis[j])[i // 4, i % 4])
chk('D1a cnot invol/orth/sym', Mc * Mc == sp.eye(16) and Mc.T == Mc, 'signed permutation, symmetric')
relT = lambda N: all(actT(N, cnot(actT(N, b))) == cnot(b) for b in basis)
relC = lambda N: all(actC(N, cnot(actC(N, b))) == actT(N, cnot(b)) for b in basis)
chk('D1b relT,relC nflip', relT(nflip) and relC(nflip), '[K] cnot_relT :854, cnot_relC :860')
chk('D1c cc relT,relC reflY', (not relT(reflY)) and (not relC(reflY)), 'countercontrol: both relations fail for reflY')
corner = lambda a: [0, 0, 1] if a == 0 else [0, 0, -1]
chk('D1d frame', all(cnot(prod(corner(a), corner(b))) == prod(corner(a), corner((a + b) % 2)) for a in (0, 1) for b in (0, 1)))
chk('D1e IsNot nflip', nflip * nflip == sp.eye(3) and nflip.T * nflip == sp.eye(3) and nflip * sp.Matrix(z3) == -sp.Matrix(z3))
pphi = pW(phiW)
chk('D1f entangling', cnot(prod(xplus, z3)) == phiW and phiW.rank() == 4 and pphi * pphi == pphi and pphi.trace() == 1,
    'cnot(prodState xplus z3) = phiW, rank 4, pure')
xs, ys, as_, bs = sp.symbols('x1:4'), sp.symbols('y1:4'), sp.symbols('a1:4'), sp.symbols('b1:4')
rho = lambda v: (s[0] + v[0] * s[1] + v[1] * s[2] + v[2] * s[3]) / 2
lhs = ip(prod(as_, bs), cnot(prod(xs, ys)))
rhs = 4 * (kron(rho(as_), rho(bs)) * CNOT * kron(rho(xs), rho(ys)) * CNOT.H).trace()
chk('D1g posFwd identity', sp.expand(lhs - rhs) == 0, 'value = 4 tr(PSD.PSD) on the ball [X via D]; [K] nativeGate_cnot')
chk('D1h pW(prod)=rho(x)rho', sp.expand(pW(prod(xs, ys)) - kron(rho(xs), rho(ys))) == sp.zeros(4, 4), 'symbolic')

# ---- the cones
E0 = E(0, 0) + E(1, 3) - E(2, 2)
def zs(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
ZF = [zs(a, b) for a, b in SIGNS]
CONES = [('K(E0)', [E0]), ('K(Z_F)', ZF)]
RzPi = sp.diag(-1, -1, 1)            # rot3 pi, the half-turn of ball3Drive's flow (= R(Z))
def eig(z):
    ev = pW(z).eigenvals(); assert sum(ev.values()) == 4; return ev
def certificate(z):
    ev = eig(z); neg = [l for l in ev if l < 0]
    if len(neg) != 1 or ev[neg[0]] != 1: return False
    a = -neg[0]; return all(l >= a for l in ev if l != neg[0])
def inK(Z, w): return all(ip(z, w) >= 0 for z in Z)            # for PSD w: w in Q3 cap Z*
def setEq(A, B): return all(any(a == b for b in B) for a in A) and all(any(a == b for a in A) for b in B)
for name, Z in CONES:
    print('== cone', name)
    # C1 H1
    okc1 = True
    for z in Z:
        v = sp.expand(ip(z, prod(xs, ys)))
        M = sp.Matrix(3, 3, lambda i, j: sp.expand(v.coeff(xs[i]).coeff(ys[j])))
        c0 = v.subs({**{x: 0 for x in xs}, **{y: 0 for y in ys}})
        Qy = sp.eye(3) - M.T * M / c0 ** 2
        ok = c0 > 0 and min(Qy.eigenvals()) >= 0
        X, Yv = sp.Matrix(xs), sp.Matrix(ys)
        sos = ((X + (M / c0) * Yv).T * (X + (M / c0) * Yv))[0] + (Yv.T * Qy * Yv)[0] + (1 - (X.T * X)[0]) + (1 - (Yv.T * Yv)[0])
        okc1 &= bool(ok) and sp.expand(2 * v / c0 - sos) == 0
    chk('C1 H1 %s' % name, okc1, 'SOS identity over the whole ball, each defect')
    # C2 H2
    chk('C2 cnot Z=Z %s' % name, setEq([cnot(z) for z in Z], Z))
    if name == 'K(Z_F)':
        okii = setEq([actC(RzPi, z) for z in Z], Z) and setEq([actT(RzPi, z) for z in Z], Z) and setEq([transposeW(z) for z in Z], Z)
        chk('C2 level(ii) G16', okii, 'Ad(Z(x)I), Ad(I(x)Z), transposeW permute Z_F')
        chk('C2 SWAP (iota) Z_F', setEq([z.T for z in Z], Z), 'record: node S1')
    else:
        chk('C2 record E0 level(ii)', ip(E0, actC(RzPi, E0)) == -1, 'ipW(E0, Ad(Z(x)I)E0) = -1: K(E0) is level (i) only')
    # C3 H3 certificates
    orth = all(ip(Z[i], Z[j]) == 0 for i in range(len(Z)) for j in range(len(Z)) if i != j)
    chk('C3 H3 cert %s' % name, all(certificate(z) for z in Z) and orth and all(pW(z).trace() > 0 for z in Z),
        'one negative eigenvalue -a, others >= a; pairwise orthogonal')
    # C4 K != Q3
    okc4 = True
    for z in Z:
        lneg = [l for l in eig(z) if l < 0][0]
        g = (pW(z) - lneg * sp.eye(4)).nullspace()[0]
        okc4 &= ip(z, Tpure(g)) < 0
    chk('C4 K!=Q3 %s' % name, okc4, 'defect not PSD; its negative eigenvector T_g lies in Q3 and not in K')
    # C5 maxCone bound (homogeneity of C1)
    a0, b0 = sp.symbols('a0 b0', positive=True)
    okc5 = all(sp.expand(ip(z, sp.Matrix([a0] + list(as_)) * sp.Matrix([b0] + list(bs)).T)
                         - a0 * b0 * ip(z, prod([a / a0 for a in as_], [b / b0 for b in bs]))) == 0 for z in Z)
    chk('C5 maxCone %s' % name, okc5, 'pairing with Lorentz a(x)b = a0 b0 x (C1 value at a/a0, b/b0) >= 0')
    # C6 slice
    chk('C6 slice (0,0) %s' % name, all(cnot(b)[0, 0] == b[0, 0] and actC(RzPi, b)[0, 0] == b[0, 0]
                                        and actT(RzPi, b)[0, 0] == b[0, 0] and transposeW(b)[0, 0] == b[0, 0] for b in basis))
    # candidate witness vectors
    cands = []
    for z in Z:
        for l, mult, vecs in pW(z).eigenvects():
            cands += list(vecs)
    # C7 reflY consistency
    found = None
    for z in Z:
        rz = actT(reflY, z)
        extra = [v for l, mu, vs in pW(rz).eigenvects() for v in vs]
        for w in list(Z) + [Tpure(v) for v in cands + extra]:
            if inK(Z, w) and ip(rz, w) < 0: found = (ip(rz, w)); break
        if found is not None: break
    chk('C7 reflY moves %s' % name, found is not None, 'pairing %s; consistent with no_candidateCone_cnot_reflY [K]' % found)
    # C8 one-token maps
    n = sp.Matrix([3, 0, 4]) / 5
    Un = (s[0] - iu * (n[0] * s[1] + n[1] * s[2] + n[2] * s[3])) / sp.sqrt(2)
    UR1 = s[0] / 2 - iu * (5 * s[1] + s[2] + s[3]) / 6
    maps = [('actC rot3(pi)', 'C', s[3]), ('actT nflip', 'T', s[1]), ('actC nflip', 'C', s[1]), ('actC cyc3', 'C', UJ),
            ('actT cyc3', 'T', UJ), ('actC Rx(pi/2)', 'C', Ux90), ('actC R_n(pi/2)', 'C', Un), ('actC R1', 'C', UR1)]
    for mname, side, U in maps:
        R = Rof(U); act = (lambda w: actC(R, w)) if side == 'C' else (lambda w: actT(R, w))
        UU = kron(U, s[0]) if side == 'C' else kron(s[0], U)
        if setEq([act(z) for z in Z], Z):
            print('MAP %-16s %s: permutes Z (invariant)' % (mname, name)); continue
        wit = None
        pool = list(Z) + [Tpure(v) for v in cands] + [Tpure(UU * v) for v in cands] + [Tpure(UU.H * v) for v in cands]
        for z in Z:
            pool += [Tpure(v) for l, mu, vs in pW(act(z)).eigenvects() for v in vs]
        if name == 'K(Z_F)':
            psis = [(pW(z) - min(eig(z)) * sp.eye(4)).nullspace()[0] for z in Z]
            psis = [v / sp.sqrt(sp.expand((v.H * v)[0])) for v in psis]
            for v in psis:
                vp = UU * v; c = [sp.expand((u.H * vp)[0]) for u in psis]
                tb = max(range(4), key=lambda t: sp.Abs(c[t]) ** 2)
                pool += [Tpure(sp.expand(vp - Rt(k, 8) * c[tb] * psis[tb])) for k in range(1, 9)]
        for z in Z:
            for w in pool:
                if inK(Z, w) and ip(act(z), w) < 0: wit = ip(act(z), w); break
            if wit is not None: break
        q3ok = all(sp.Matrix(pW(act(Tpure(v)))).eigenvals() and min(pW(act(Tpure(v))).eigenvals()) >= 0 for v in cands[:4])
        print('MAP %-16s %s: %s; Q3 control %s' % (mname, name, ('WITNESS pairing %s' % wit) if wit is not None else 'NOWITNESS',
                                                   'invariant' if q3ok else 'NOT'))
        RES['C8 Q3 ctrl %s %s' % (mname, name)] = bool(q3ok)
    swz = [z.T for z in Z]
    if not setEq(swz, Z):
        wit = None
        for z in Z:
            for w in list(Z) + [Tpure(v) for v in cands] + [Tpure(sp.Matrix([5, -5, -1, -1]))]:
                if inK(Z, w) and ip(z.T, w) < 0: wit = ip(z.T, w); break
            if wit is not None: break
        print('MAP %-16s %s: %s' % ('SWAP', name, ('WITNESS pairing %s' % wit) if wit is not None else 'NOWITNESS'))

# ---- rotation data of C8 (exact)
n511 = sp.Matrix([5, 1, 1]); R1m = Rof(s[0] / 2 - iu * (5 * s[1] + s[2] + s[3]) / 6)
nn = sp.Matrix([3, 0, 4]) / 5; Rnm = Rof((s[0] - iu * (nn[0] * s[1] + nn[2] * s[3])) / sp.sqrt(2))
chk('C8 data R1', R1m ** 3 == sp.eye(3) and R1m != sp.eye(3) and R1m * n511 == n511 and R1m.det() == 1, 'order 3 about (5,1,1), rational')
chk('C8 data R_n', Rnm ** 4 == sp.eye(3) and Rnm ** 2 != sp.eye(3) and Rnm * nn == nn and Rnm.det() == 1, 'quarter turn about (3,0,4)/5')
# ---- C9 FCC famI for the uniform assignment (Fractions)
def F4(t): return [[Fr(int(sp.numer(t[m, n])), int(sp.denom(t[m, n]))) for n in range(4)] for m in range(4)]
def I4(t): return [[int(4 * t[m, n]) for n in range(4)] for m in range(4)]       # tables scaled by 4 (exact integers)
def famI_min(Xs, pool):
    # min over X in Xs and Y, E, F in pool of ipW(X, tabMul(tabMul E Y)(tabT F)) = tr(X^T E Y F^T), scaled by 4^4
    best = None
    A = [[[sum(X[k][i] * Et[k][j] for k in range(4)) for j in range(4)] for i in range(4)] for X in Xs for Et in pool]
    B = [[[sum(Y[i][k] * Ft[j][k] for k in range(4)) for j in range(4)] for i in range(4)] for Y in pool for Ft in pool]
    Bf = [[b[j][i] for i in range(4) for j in range(4)] for b in B]
    for a in A:
        af = [a[i][j] for i in range(4) for j in range(4)]
        for bf in Bf:
            v = af[0]*bf[0]+af[1]*bf[1]+af[2]*bf[2]+af[3]*bf[3]+af[4]*bf[4]+af[5]*bf[5]+af[6]*bf[6]+af[7]*bf[7] \
                +af[8]*bf[8]+af[9]*bf[9]+af[10]*bf[10]+af[11]*bf[11]+af[12]*bf[12]+af[13]*bf[13]+af[14]*bf[14]+af[15]*bf[15]
            if best is None or v < best: best = v
    return Fr(best, 256)
axes = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
tabs72 = [prod(a, b) for a in axes for b in axes]; tabs72 += [cnot(t) for t in tabs72]
T72 = [I4(t) for t in tabs72]
mins = {}
for name, Z in CONES:
    mins[name] = famI_min([I4(z) for z in Z], T72 + [I4(z) for z in Z])
    chk('C9 FCC fails %s' % name, mins[name] < 0, 'uniform assignment: min famI value %s' % mins[name])
q3X = [I4(phiW), I4(prod(z3, z3)), I4(cnot(prod(xplus, xplus)))]
mq = famI_min(q3X, T72)
chk('C9 control Q3 FCC>=0', mq >= 0, 'instance control: min %s over 3 x 72^3 values' % mq)
# ---- C10 SF pair transfer
P = kron(P0, s[0]); eP = table(P) / 4; eC = E(0, 0) - eP
for name, Z in CONES + [('Q3', [])]:
    psd = min(pW(eP).eigenvals()) >= 0 and min(pW(eC).eigenvals()) >= 0
    okk = psd and inK(Z, eP) and inK(Z, eC)
    vals = (ip(eP, prod(z3, z3)), ip(eP, prod(z3, [0, 0, -1])), ip(eP, prod([0, 0, -1], z3)))
    chk('C10 SF fails on %s' % name, okk and vals == (1, 1, 0), 'effect e_P, complement in K; values %s' % (vals,))
# ---- countercontrols and record controls
e32 = E(0, 0) + Rt(3, 2) * (E(1, 3) - E(2, 2))
chk('CC e_{3/2} fails cert', not certificate(e32), 'eigenvalues %s' % sorted(eig(e32)))
pairZ = [E0, actC(RzPi, E0)]
chk('CC nonorth pair fails', ip(pairZ[0], pairZ[1]) < 0, 'ipW = %s' % ip(pairZ[0], pairZ[1]))
sharp = lambda v: sp.Matrix([Rt(1, 2)] + [Rt(c, 2) for c in v])           # ehom of the sharp effect (1 + v.x)/2
cv = (sharp([-1, 0, 0]).T * chainW * sharp([0, 0, -1]))[0]
chk('CC twin fails H2', cnot(idW) == chainW and actT(reflY, phiW) == idW and cv == Rt(-1, 2),
    'idW = actT reflY phiW in twin; cnot idW = chainW; prodEffVal = %s ([K] chain_value :134)' % cv)
chk('CC Q3 not reflY-inv', min(pW(idW).eigenvals()) < 0, 'actT reflY phiW = idW is not PSD (I3.44 holds for Q3)')
chk('CC Q3 has no defect', certificate(E(0, 0)) is False and min(pW(E(0, 0)).eigenvals()) > 0, 'E00 is PSD (no negative eigenvalue)')
bad = [k for k, v in RES.items() if not v]
print('summary: %d checks, %d failed%s' % (len(RES), len(bad), (': ' + ', '.join(bad)) if bad else ''))
if not bad:
    print('VERDICT R2-CONES-EXACT: K(E0) and K(Z_F) satisfy H1, H2 (level (i); level (ii) for K(Z_F)), the H3 certificates, '
          'the maxCone bound and the slice conditions; both fail FCC uniformly (min %s, %s), are not actT-reflY-invariant, '
          'and leave themselves under the one-token maps with witnesses listed; controls green' % (mins['K(E0)'], mins['K(Z_F)']))
else:
    print('NO VERDICT')

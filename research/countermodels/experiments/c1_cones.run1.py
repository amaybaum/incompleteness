# c1_cones.py -- research/countermodels node C1: exact checks on the two stage-3 cones that stage 6 did not reassess:
#   K_F2  = K({F, cnot F}) = (Q3 ∩ {F, cnot F}*) + cone{F, cnot F},  F = z_(-1,-1)        (stage 3 U `K_F2`; X)
#   K(e_c) = (Q3 ∩ e_c*) + R+ e_c,  e_c = E00 + c (E13 - E22),  c in (1/2, 1]            (stage 3 X)
# DECISION RULE (fixed before the first run, 2026-10-10T20:09:41Z by date -u):
#  Conventions (charter; archived records): W 3 = 4x4 real tables, index 0 the unit, 1-3 the ball coordinates;
#  pauliW(w) = (1/4) sum_mn w_mn s_m (x) s_n -- a comparison/construction tool, never a premise; ipW = entrywise sum
#  (= 4 tr(pauliW pauliW)); z_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4; actC/actT = left/right action by hom(R) = 1 (+) R;
#  cnot = the kernel's signed permutation (sgn, pc, pt), transcribed and compared with the text of
#  verification/lean-mathlib/OIBridge/CompositeDimension.lean:741-755 (check D0z).
#  c is a sympy symbol; "for all c" means for all c in (1/2, 1], decided exactly (square-free part + Sturm root counting
#  for polynomials in c; for the linear witness functions, an exact interval cover of (1/2, 1]).
#  D (K-independent re-checks of the kernel transcriptions): D0z pc/pt/sgn equal the Lean source text; D0a cnot = Ad(CNOT)
#   control first on the 16 basis tables; D0b actC/actT R(U) = Ad(U(x)I)/Ad(I(x)U) for U in {X, Z, U_J, U_x90};
#   D0c transposeW = global transpose = actC reflY o actT reflY; D0d table transpose = Ad(SWAP); D1a cnot involutive and
#   symmetric (ipW-orthogonal); D1b relT, relC with nflip; D1c frame; D1d IsNot nflip; D1e cnot prodState(xplus, z3) =
#   phiW, pure and not a product; D1f posFwd identity ipW(prod a b, cnot prod x y) = 4 tr(rho rho CNOT rho rho CNOT^dag)
#   (symbolic); D1g pauliW(prodState x y) = rho(x) (x) rho(y) (symbolic).
#  Per cone (tags F2, EC):
#   C1 H1: SOS identity 2v/c0 = |x + (M/c0)y|^2 + y^T(I - M^T M/c0^2)y + (1-|x|^2) + (1-|y|^2) for each defect, with
#      I - M^T M/c0^2 PSD (EC: eigenvalues nonnegative for all c).
#   C2 H2 at level (i): cnot permutes Z. Record (level (ii) fails): a G16 generator g, z in Z and w in K with
#      ipW(g z, w) < 0 (EC: for all c).
#   C3 H3 certificates (the hypotheses of SD1/SD2 and Theorem S, audited at stage 3): each pauliW(z) has exactly one
#      negative eigenvalue -a, simple, and all others >= a (EC: for all c); Z pairwise ipW-orthogonal; tr pauliW(z) > 0.
#      F2 also: the at-most-one-violation identity sum_s <psi_s|Q|psi_s> = tr Q over the orthonormal cap basis
#      (symbolic Hermitian Q), and the cap vectors of F and cnot F are two of its members.
#   C4 K != Q3: pauliW(z) not PSD; the pure table T_g of its negative eigenvector has ipW(z, T_g) < 0 (EC: for all c).
#   C5 maxCone bound: ipW(z, a (x) b) = a0 b0 (C1 value at a/a0, b/b0) symbolically (with C1: z in maxCone).
#   C6 slice: cnot fixes the (0,0) entry of every basis table.
#   C7 I3.44 consistency: z in Z, w in K with ipW(actT reflY z, w) < 0 (EC: for all c).
#   C8 one-token maps (actC and actT of rot3(pi), nflip, cyc3, Rx(pi/2), Rz(pi/2), R_n(pi/2) with n = (3,0,4)/5, R1 =
#      order 3 about (5,1,1)) and SWAP: INVARIANT if the map permutes Z; else a witness w in K (a member of Z, or a pure
#      table T_v of a candidate vector, membership checked) with ipW(g z, w) < 0 for some z in Z; F2 exact; EC: ALLC if
#      the candidate pure tables cover (1/2, 1] exactly, else INST if a witness exists at each c in {5/8, 3/4, 1}, else
#      NOWITNESS (no claim). Required (rows I3.137, I3.142, I3.150-I3.153, I3.165), for each cone: a witness (ALLC or INST)
#      for (IE1) some map; (IE1Drive) one of rot3(pi), Rz(pi/2), cyc3 on some token; (b_S4) some control map AND some
#      target map; (b_n) actC R_n(pi/2); (b_R1) actC R1; (b_DJ) one of nflip, Rx(pi/2), cyc3, rot3(pi), Rz(pi/2) on the
#      control AND one on the target; (K2 clause) some map. Control: Q3 is invariant -- the image of every candidate
#      pure table under every local map is PSD (unitary conjugation, checked on the tables).
#   C9 FCC famI for the uniform assignment: min over X in Z, Y, E, F in (the 72 tables prodState(+-e_i, +-e_j) and their
#      cnot images, plus Z) of ipW(X, E Y F^T) < 0. F2 exact; EC exact at c = 1; at c in {5/8, 3/4} the minimum is
#      printed as a record only (a nonnegative minimum over a finite pool is no evidence). Control: Q3 instance pool
#      (X in {phiW, prodState(z3,z3), cnot prodState(xplus,xplus)}, Y, E, F over the 72 tables) min >= 0.
#   C10 SF pair transfer (I4.236): e_P (pauliW = |0><0| (x) I / 4) and E00 - e_P lie in K; e_P takes the values 1, 1, 0
#      on prodState(z3, z3), prodState(z3, -z3), prodState(-z3, z3) (EC: for all c).
#   T  (I3.161) c(x) = dim span{y in K : ipW(x, y) = 0}. F2: c(F) = 15 (>= by 15 independent members of K ∩ F^perp:
#      pure tables T_v with |<t|v>|^2 = |v|^2/2 and cnot F; <= 15 since F != 0); c(P00) = 9 (>= by 9 independent members
#      of Q3 ∩ Z* ∩ P00^perp; <= 9 because ipW(P00, z) > 0 for z in Z forces y in Q3 with <00|y|00> = 0, whose span is
#      Herm(|00>^perp), dimension 9, checked as the rank of the constraint). EC: the same at each c in {5/8, 3/4, 1}
#      (for all c by the written argument of NOTES-C1).
#   Q3 control column: products PSD (D1g), cnot preserves PSD (D0a), Q3 not reflY-invariant (idW not PSD), FCC instance
#   min >= 0, c(P00) = 9 and c(T_phi) = 9 for the Bell table phiW.
#  COUNTERCONTROLS (must fail as stated): CC1 e_{3/2} fails the C3 certificate; CC2 e_{1/2} is PSD (the closed end of the
#  family is Q3, not exotic); CC3 for {F, g F}, g = actC R_x with cos = 3/5, sin = 4/5, some pure state violates both
#  constraints (orthogonality is load-bearing for Theorem S (b)); CC4 for every map printed INVARIANT, no pool member gives
#  a negative pairing (the search does not invent witnesses); CC5 twin fails H2: actT reflY phiW = idW, cnot idW = chainW,
#  and the product of the sharp effects along -e1, -e3 on chainW is -1/2.
#  VERDICT C1-CONES-EXACT printed iff every check passes and every countercontrol fails as stated; otherwise NO VERDICT.
import math
import re
import sympy as sp
from fractions import Fraction as Fr
from itertools import product

iu, Rt = sp.I, sp.Rational
cs = sp.Symbol('c', real=True)
HALF, ONE = Rt(1, 2), Rt(1)
s = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
SS = [[kron(s[m], s[n]) for n in range(4)] for m in range(4)]
def pW(w): return sp.expand(sum((w[m, n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4)
SSP = [[[(i, j, SS[m][n][j, i]) for i in range(4) for j in range(4) if SS[m][n][j, i] != 0] for n in range(4)] for m in range(4)]
def table(A):            # entries tr(A s_m (x) s_n), from the four nonzero entries of each Pauli product
    t = sp.Matrix(4, 4, lambda m, n: sp.expand(sum(A[i, j] * v for i, j, v in SSP[m][n])))
    assert all(sp.expand(sp.im(x)) == 0 for x in t), 'non-real table'
    return t.applyfunc(lambda x: sp.expand(sp.re(x)))
def ip(a, b): return sp.expand(sum(a[m, n] * b[m, n] for m in range(4) for n in range(4)))
def E(m, n):
    t = sp.zeros(4, 4); t[m, n] = 1; return t
def hom(x): return sp.Matrix([1] + list(x))
def prod(x, y): return hom(x) * hom(y).T
def Hom(N):
    H = sp.eye(4); H[1:, 1:] = N; return H
def actC(N, w): return Hom(N) * w
def actT(N, w): return w * Hom(N).T
SGN = lambda m, n: -1 if (m, n) in [(1, 3), (2, 2)] else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnot(w): return sp.Matrix(4, 4, lambda m, n: SGN(m, n) * w[PC[m][n], PT[m][n]])
def transposeW(w): return sp.Matrix(4, 4, lambda m, n: (-1 if m == 2 else 1) * (-1 if n == 2 else 1) * w[m, n])
def swapW(w): return w.T
z3, xplus = [0, 0, 1], [1, 0, 0]
nflip, reflY = sp.diag(1, -1, -1), sp.diag(1, -1, 1)
phiW, idW = sp.diag(1, 1, -1, 1), sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
P0, P1 = sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]])
CNOT = kron(P0, s[0]) + kron(P1, s[1])
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
def Rof(V, kap):          # rotation of U = V/sqrt(kap): R_ij = tr(s_i U s_j U^dag)/2
    return sp.Matrix(3, 3, lambda i, j: sp.nsimplify(sp.expand((s[i + 1] * V * s[j + 1] * V.H).trace() / (2 * kap))))
def Tpure(v):
    v = sp.Matrix(v); return table(v * v.H / sp.expand((v.H * v)[0]))
def eigvals_ok(M):
    ev = M.eigenvals(); assert sum(ev.values()) == 4; return ev
RES = {}
def chk(cid, ok, note=''):
    RES[cid] = bool(ok); print('CHECK %-30s %s %s' % (cid, 'PASS' if ok else 'FAIL', note))

# ---- exact sign decisions in c on (1/2, 1]
def _open_roots(Q, lo, hi):
    n = Q.count_roots(lo, hi)
    return n - (1 if Q.eval(lo) == 0 else 0) - (1 if Q.eval(hi) == 0 else 0)
def nonneg_on(p, lo=HALF, hi=ONE):           # p(c) >= 0 for every c in [lo, hi]
    p = sp.expand(p)
    if not p.has(cs): return bool(p >= 0)
    P = sp.Poly(p, cs); R = sp.Poly(1, cs)
    for f, k in P.sqf_list()[1]:
        if k % 2 == 1: R = R * f
    if R.degree() > 0 and _open_roots(R, lo, hi) > 0: return False
    for k in range(1, 60):
        v = P.eval(lo + (hi - lo) * Rt(k, 60))
        if v != 0: return bool(v > 0)
    return False
def neg_on(p, lo=HALF, hi=ONE):              # p(c) < 0 for every c in (lo, hi]
    p = sp.expand(p)
    if not p.has(cs): return bool(p < 0)
    P = sp.Poly(p, cs); Q = P.sqf_part()
    return bool(P.eval(hi) < 0) and Q.count_roots(lo, hi) == (1 if P.eval(lo) == 0 else 0)
def lin(p):              # linear polynomial in c -> (a0, a1) as Fractions, exactly
    p = sp.expand(p); a1 = p.coeff(cs, 1); a0 = p.coeff(cs, 0)
    assert sp.expand(p - a0 - a1 * cs) == 0, 'non-linear witness function'
    return (Fr(int(sp.Rational(a0).p), int(sp.Rational(a0).q)), Fr(int(sp.Rational(a1).p), int(sp.Rational(a1).q)))
def cover(cands, lo=Fr(1, 2), hi=Fr(1)):
    # cands: list of ((m0, m1), (p0, p1)); witness valid at c iff m0 + m1 c >= 0 and p0 + p1 c < 0. Exact cover of (lo, hi]:
    # every endpoint in (lo, hi] and every midpoint between consecutive breakpoints is covered (validity sets are
    # intervals whose endpoints are among the breakpoints).
    pts = {lo, hi}
    for (m0, m1), (p0, p1) in cands:
        for a0, a1 in ((m0, m1), (p0, p1)):
            if a1 != 0 and lo < -a0 / a1 < hi: pts.add(-a0 / a1)
    pts = sorted(pts)
    tests = [x for x in pts if x > lo] + [(a + b) / 2 for a, b in zip(pts, pts[1:])]
    def ok_at(x): return any(m0 + m1 * x >= 0 and p0 + p1 * x < 0 for (m0, m1), (p0, p1) in cands)
    return all(ok_at(x) for x in tests)

# ---- D: K-independent re-checks
src = open('../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean', encoding='utf-8').read()
def lean_table(name):
    blk = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){4})' % name, src).group(1)
    tab = [[None] * 4 for _ in range(4)]
    for a, b, v in re.findall(r'(\d), (\d) => (\d)', blk): tab[int(a)][int(b)] = int(v)
    return tab
sgn_src = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = 1 ∧ ν = 3\) ∨ \(μ = 2 ∧ ν = 2\) then -1 else 1', src)
chk('D0z pc/pt/sgn = Lean text', lean_table('pc') == PC and lean_table('pt') == PT and sgn_src is not None,
    'CompositeDimension.lean:741-755 at L')
basis = [E(m, n) for m in range(4) for n in range(4)]
chk('D0a cnot=Ad(CNOT)', all(table(CNOT * pW(b) * CNOT.H) == cnot(b) for b in basis), '16/16 basis tables, control first')
VX, VZ = s[1], s[3]
VJ = s[0] - iu * (s[1] + s[2] + s[3])            # U_J = VJ/2: cyc3
Vx90 = s[0] - iu * s[1]                           # Rx(pi/2) = Vx90/sqrt 2
Vz90 = s[0] - iu * s[3]                           # Rz(pi/2)
Vn90 = 5 * s[0] - iu * (3 * s[1] + 4 * s[3])      # R_n(pi/2), n = (3,0,4)/5: /sqrt 50
VR1 = 3 * s[0] - iu * (5 * s[1] + s[2] + s[3])    # order 3 about (5,1,1): /6
cyc3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
okd = Rof(VJ, 4) == cyc3 and Rof(VX, 1) == nflip and Rof(VZ, 1) == sp.diag(-1, -1, 1)
for V, kap in [(VX, 1), (VZ, 1), (VJ, 4), (Vx90, 2)]:
    R = Rof(V, kap)
    okd &= all(table(kron(V, s[0]) * pW(b) * kron(V, s[0]).H / kap) == actC(R, b) for b in basis)
    okd &= all(table(kron(s[0], V) * pW(b) * kron(s[0], V).H / kap) == actT(R, b) for b in basis)
chk('D0b actC/actT=Ad', okd, 'U in {X, Z, U_J, U_x90}; R(U_J) = cyc3, R(X) = nflip, R(Z) = rot3(pi)')
chk('D0c transposeW=T', all(table(pW(b).T) == transposeW(b) == actC(reflY, actT(reflY, b)) for b in basis))
chk('D0d SWAP=table transpose', all(table(SWAP * pW(b) * SWAP) == swapW(b) for b in basis))
Mc = sp.Matrix(16, 16, lambda i, j: cnot(basis[j])[i // 4, i % 4])
chk('D1a cnot invol/sym', Mc * Mc == sp.eye(16) and Mc.T == Mc)
chk('D1b relT,relC nflip', all(actT(nflip, cnot(actT(nflip, b))) == cnot(b) and
                               actC(nflip, cnot(actC(nflip, b))) == actT(nflip, cnot(b)) for b in basis), '[K] :854, :860')
corner = lambda a: [0, 0, 1] if a == 0 else [0, 0, -1]
chk('D1c frame', all(cnot(prod(corner(a), corner(b))) == prod(corner(a), corner((a + b) % 2)) for a in (0, 1) for b in (0, 1)))
chk('D1d IsNot nflip', nflip * nflip == sp.eye(3) and nflip.T * nflip == sp.eye(3) and nflip * sp.Matrix(z3) == -sp.Matrix(z3))
pphi = pW(phiW)
chk('D1e entangling image', cnot(prod(xplus, z3)) == phiW and pphi * pphi == pphi and pphi.trace() == 1 and phiW.rank() == 4,
    'cnot(prodState xplus z3) = phiW: pure, rank-4 table (not a product)')
xs, ys, as_, bs = sp.symbols('x1:4'), sp.symbols('y1:4'), sp.symbols('a1:4'), sp.symbols('b1:4')
rho = lambda v: (s[0] + v[0] * s[1] + v[1] * s[2] + v[2] * s[3]) / 2
lhs = ip(prod(as_, bs), cnot(prod(xs, ys)))
rhs = 4 * (kron(rho(as_), rho(bs)) * CNOT * kron(rho(xs), rho(ys)) * CNOT.H).trace()
chk('D1f posFwd identity', sp.expand(lhs - rhs) == 0, '[K] nativeGate_cnot :1160; through the [D] dictionary')
chk('D1g pW(prod)=rho(x)rho(y)', sp.expand(pW(prod(xs, ys)) - kron(rho(xs), rho(ys))) == sp.zeros(4, 4), 'symbolic')

# ---- the cones
def zs(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
F = zs(-1, -1); cF = cnot(F)
chk('D2 cnot F = z_(1,1)', cF == zs(1, 1), 'K_F2 = K({z_(-1,-1), z_(1,1)})')
ec = E(0, 0) + cs * (E(1, 3) - E(2, 2))
CONES = [('F2', [F, cF]), ('EC', [ec])]
def setEq(A, B): return all(any(sp.expand(a - b) == sp.zeros(4, 4) for b in B) for a in A) and len(A) == len(B)
def negvec(z):           # eigenvector of the negative eigenvalue of pauliW(z) (c-independent for e_c)
    M = pW(z).subs(cs, 1) if z.has(cs) else pW(z)
    lneg = min(M.eigenvals())
    return (M - lneg * sp.eye(4)).nullspace()[0]
def eigvecs(z):
    M = pW(z).subs(cs, 1) if z.has(cs) else pW(z)
    return [v for l, mu, vs in M.eigenvects() for v in vs]
INSTC = [Rt(5, 8), Rt(3, 4), ONE]

for tag, Z in CONES:
    print('== cone', tag)
    # C1 H1
    okc1 = True
    for z in Z:
        v = sp.expand(ip(z, prod(xs, ys)))
        M = sp.Matrix(3, 3, lambda i, j: sp.expand(v.coeff(xs[i]).coeff(ys[j])))
        c0 = sp.expand(v.subs({**{x: 0 for x in xs}, **{y: 0 for y in ys}}))
        Qy = sp.eye(3) - M.T * M / c0 ** 2
        X, Yv = sp.Matrix(xs), sp.Matrix(ys)
        sos = ((X + (M / c0) * Yv).T * (X + (M / c0) * Yv))[0] + (Yv.T * Qy * Yv)[0] + (1 - (X.T * X)[0]) + (1 - (Yv.T * Yv)[0])
        okc1 &= nonneg_on(c0) and all(nonneg_on(l) for l in Qy.eigenvals()) and sp.expand(2 * v / c0 - sos) == 0
        okc1 &= neg_on(-c0)
    chk('%s-C1 H1' % tag, okc1, 'SOS identity over the whole ball, each defect%s' % (' (all c)' if tag == 'EC' else ''))
    # C2 H2 level (i)
    chk('%s-C2 cnot permutes Z' % tag, setEq([cnot(z) for z in Z], Z))
    # C3 H3 certificates
    okc3 = True
    for z in Z:
        P = pW(z); cp = sp.factor(P.charpoly(sp.Symbol('t')).as_expr())
        ev = sp.roots(sp.Poly(P.charpoly(sp.Symbol('t')).as_expr(), sp.Symbol('t')))
        assert sum(ev.values()) == 4
        negs = [l for l in ev if neg_on(l)]
        others = [l for l in ev if l not in negs]
        okc3 &= len(negs) == 1 and ev[negs[0]] == 1 and all(nonneg_on(l + negs[0]) for l in others)
        okc3 &= all(nonneg_on(l) for l in others) and neg_on(-P.trace())
        print('  spectrum %s: %s' % (tag, sorted([sp.factor(l) for l in ev], key=str)))
    orth = all(sp.expand(ip(Z[i], Z[j])) == 0 for i in range(len(Z)) for j in range(len(Z)) if i != j)
    chk('%s-C3 H3 certificate' % tag, okc3 and orth, 'one simple negative eigenvalue -a, others >= a; Z orthogonal; tr > 0')
    if tag == 'F2':
        psis = [negvec(zs(a, b)) for a, b in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
        psis = [v / sp.sqrt(sp.expand((v.H * v)[0])) for v in psis]
        Gm = sp.Matrix(4, 4, lambda i, j: sp.simplify((psis[i].H * psis[j])[0]))
        qs = sp.symbols('q0:16', real=True)
        Qh = sp.Matrix(4, 4, lambda i, j: qs[4 * i + j] if i == j else (qs[4 * min(i, j) + max(i, j)] + (1 if i < j else -1) * iu * qs[4 * max(i, j) + min(i, j)]))
        tot = sp.expand(sum((v.H * Qh * v)[0] for v in psis) - Qh.trace())
        capF, capcF = negvec(F), negvec(cF)
        inb = lambda w: any(sp.Matrix.hstack(sp.Matrix(w), u).rank(simplify=True) == 1 for u in psis)
        chk('F2-C3 one-violation identity', Gm == sp.eye(4) and tot == 0 and inb(capF) and inb(capcF),
            'orthonormal cap basis {psi_s}; sum_s <psi_s|Q|psi_s> = tr Q (symbolic); caps of F, cnot F in it')
    # C4 K != Q3
    okc4 = True
    for z in Z:
        okc4 &= neg_on(ip(z, Tpure(negvec(z))))
    chk('%s-C4 K != Q3' % tag, okc4, 'ipW(z, T_g) < 0 for the negative eigenvector g; T_g in Q3, not in K = K*')
    # C5 maxCone bound by homogeneity
    a0, b0 = sp.symbols('a0 b0', positive=True)
    okc5 = all(sp.expand(ip(z, sp.Matrix([a0] + list(as_)) * sp.Matrix([b0] + list(bs)).T)
                         - a0 * b0 * ip(z, prod([a / a0 for a in as_], [b / b0 for b in bs]))) == 0 for z in Z)
    chk('%s-C5 maxCone' % tag, okc5 and okc1, 'pairing with Lorentz a (x) b = a0 b0 (C1 value) >= 0')
    chk('%s-C6 slice' % tag, all(cnot(b)[0, 0] == b[0, 0] for b in basis), 'cnot fixes the (0,0) entry')

    # membership of a pure table (PSD) in K: pairs >= 0 with every defect (EC: returns the linear function)
    def member_fn(w): return [ip(z, w) for z in Z]
    def inK_exact(w): return all(nonneg_on(p) for p in member_fn(w))
    # candidate vectors
    base = []
    for z in Z: base += eigvecs(z)
    if tag == 'EC':
        f0s = [v for v in eigvecs(ec) if sp.expand((v.H * pW(ec).subs(cs, 1) * v)[0]) == sp.expand((v.H * v)[0]) / 4]
        if len(f0s) == 2:
            base += [f0s[0] + f0s[1], f0s[0] - f0s[1], f0s[0] + iu * f0s[1], f0s[0] - iu * f0s[1]]
    def pool_for(Vg, g_of_z):
        pool = [v for v in base] + [Vg * v for v in base] + [Vg.H * v for v in base]
        for gz in g_of_z: pool += eigvecs(gz)
        gneg = [negvec(gz) for gz in g_of_z]
        for u in [negvec(z) for z in Z]:
            for v in base:
                for k in range(1, 5):
                    for ph in (1, iu):
                        pool += [Vg * (u + Rt(k, 4) * ph * v)]
        for u in gneg:
            for v in [negvec(z) for z in Z] + base:
                for k in range(1, 9):
                    pool += [u - Rt(k, 8) * v]
        return pool
    def witness(g, Vg):       # returns ('INVARIANT', ...) / ('WITNESS', value) / ('ALLC'|'INST'|'NOWITNESS', ...)
        gZ = [g(z) for z in Z]
        if setEq(gZ, Z): return ('INVARIANT', None)
        pool = pool_for(Vg, gZ)
        tabs = []
        for v in pool:
            if sp.expand((sp.Matrix(v).H * sp.Matrix(v))[0]) == 0: continue
            tabs.append(Tpure(v))
        if tag == 'F2':
            for gz in gZ:
                for w in list(Z) + tabs:
                    val = ip(gz, w)
                    if val < 0 and (any(w == z for z in Z) or inK_exact(w)): return ('WITNESS', val)
            return ('NOWITNESS', None)
        # EC: linear witness functions
        cands = []
        for w in tabs:
            m = ip(ec, w); p = ip(gZ[0], w)
            cands.append((m, p))
        if cover([(lin(m), lin(p)) for m, p in cands]): return ('ALLC', None)
        inst = []
        for c0 in INSTC:
            found = None
            for m, p in cands + [(ip(ec, ec), ip(gZ[0], ec))]:
                if sp.expand(m.subs(cs, c0)) >= 0 and sp.expand(p.subs(cs, c0)) < 0: found = sp.expand(p.subs(cs, c0)); break
            inst.append(found)
        if all(x is not None for x in inst): return ('INST', inst)
        return ('NOWITNESS', inst)
    # C2 record: level (ii) fails
    RzPi = sp.diag(-1, -1, 1)
    gens = [('actC rot3(pi)', lambda w: actC(RzPi, w), kron(VZ, s[0])), ('actT rot3(pi)', lambda w: actT(RzPi, w), kron(s[0], VZ)),
            ('transposeW', transposeW, None)]
    lev2 = None
    for gname, g, Vg in gens:
        if Vg is None: continue
        r = witness(g, Vg)
        if r[0] in ('WITNESS', 'ALLC', 'INST'): lev2 = (gname, r); break
    chk('%s-C2 record level (ii) fails' % tag, lev2 is not None, 'G16 generator %s moves K: %s' % (lev2[0], lev2[1]) if lev2 else '')
    # C7 reflY
    r7 = witness(lambda w: actT(reflY, w), sp.eye(4))
    chk('%s-C7 actT reflY moves K' % tag, r7[0] in ('WITNESS', 'ALLC'), '%s %s; consistent with no_candidateCone_cnot_reflY [K]' % r7)
    # C8 one-token maps
    def Rot(V, kap): return Rof(V, kap)
    MAPS = []
    for nm, V, kap in [('rot3(pi)', VZ, 1), ('nflip', VX, 1), ('cyc3', VJ, 4), ('Rx(pi/2)', Vx90, 2), ('Rz(pi/2)', Vz90, 2),
                       ('R_n(pi/2)', Vn90, 50), ('R1', VR1, 36)]:
        R = Rot(V, kap)
        MAPS.append(('actC ' + nm, 'C', (lambda R: lambda w: actC(R, w))(R), kron(V, s[0])))
        MAPS.append(('actT ' + nm, 'T', (lambda R: lambda w: actT(R, w))(R), kron(s[0], V)))
    outc = {}
    for mname, side, g, Vg in MAPS:
        r = witness(g, Vg); outc[mname] = r
        print('MAP %-16s %s: %s %s' % (mname, tag, r[0], '' if r[1] is None else r[1]))
    rs = witness(swapW, SWAP); outc['SWAP'] = rs
    print('MAP %-16s %s: %s %s' % ('SWAP', tag, rs[0], '' if rs[1] is None else rs[1]))
    rt = witness(transposeW, sp.eye(4)); outc['transposeW'] = rt
    print('MAP %-16s %s: %s %s' % ('transposeW', tag, rt[0], '' if rt[1] is None else rt[1]))
    W_OK = lambda k: outc[k][0] in ('WITNESS', 'ALLC', 'INST')
    ctrl = [m for m, sd, _, _ in MAPS if sd == 'C']; targ = [m for m, sd, _, _ in MAPS if sd == 'T']
    req = {
        'IE1 (I3.137)': any(W_OK(m) for m in ctrl + targ),
        'IE1Drive (I3.142)': any(W_OK(p + q) for p in ('actC ', 'actT ') for q in ('rot3(pi)', 'Rz(pi/2)', 'cyc3')),
        'b_S4 control (I3.150)': any(W_OK(m) for m in ctrl), 'b_S4 target (I3.150)': any(W_OK(m) for m in targ),
        'b_n actC (I3.151)': W_OK('actC R_n(pi/2)'), 'b_R1 actC (I3.152)': W_OK('actC R1'),
        'b_DJ control (I3.153)': any(W_OK('actC ' + q) for q in ('nflip', 'Rx(pi/2)', 'cyc3', 'rot3(pi)', 'Rz(pi/2)')),
        'b_DJ target (I3.153)': any(W_OK('actT ' + q) for q in ('nflip', 'Rx(pi/2)', 'cyc3', 'rot3(pi)', 'Rz(pi/2)')),
        'K2 clause (I3.165)': any(W_OK(m) for m in ctrl + targ)}
    for k, v in req.items(): chk('%s-C8 %s' % (tag, k), v)
    # Q3 control: images of candidate pure tables under every local map are PSD
    okq = True
    cand_tabs = [Tpure(v) for v in base[:4]]
    for mname, side, g, Vg in MAPS:
        for w in cand_tabs:
            okq &= min(pW(g(w)).eigenvals()) >= 0
    chk('%s-C8 Q3 control' % tag, okq, 'every map keeps the candidate pure tables PSD (Q3 invariant)')
    # CC4: maps printed INVARIANT give no negative pairing over the pool
    okcc4 = True
    ninv = 0
    for mname, side, g, Vg in MAPS + [('SWAP', 'S', swapW, SWAP), ('transposeW', 'S', transposeW, sp.eye(4))]:
        if outc[mname][0] != 'INVARIANT': continue
        ninv += 1
        tabs = [Tpure(v) for v in pool_for(Vg, [g(z) for z in Z]) if sp.expand((sp.Matrix(v).H * sp.Matrix(v))[0]) != 0]
        for z in Z:
            for w in tabs:
                if tag == 'F2':
                    okcc4 &= not (ip(g(z), w) < 0 and inK_exact(w))
                else:
                    okcc4 &= not (nonneg_on(ip(ec, w)) and neg_on(ip(g(z), w)))
    RES['%s-CC4 invariant maps give no witness' % tag] = okcc4 and ninv >= 1
    print('COUNTERCONTROL %s-CC4 %d invariant maps: %s' % (tag, ninv, 'no negative pairing (as required)' if okcc4 else 'WITNESS FOUND (FAIL)'))
    # C10 SF pair transfer
    eP = table(kron(P0, s[0])) / 4; eC = E(0, 0) - eP
    psd = min(pW(eP).eigenvals()) >= 0 and min(pW(eC).eigenvals()) >= 0
    vals = (ip(eP, prod(z3, z3)), ip(eP, prod(z3, [0, 0, -1])), ip(eP, prod([0, 0, -1], z3)))
    chk('%s-C10 SF pair reading fails' % tag, psd and inK_exact(eP) and inK_exact(eC) and vals == (1, 1, 0), 'values %s' % (vals,))

# ---- C9 FCC (integers: tables scaled by 8)
def I8(t, c0=None):
    t = t.subs(cs, c0) if c0 is not None else t
    return [[int(8 * t[m, n]) for n in range(4)] for m in range(4)]
def famI_min(Xs, pool):
    best, arg = None, None
    A = [(xi, ei, [[sum(X[k][i] * Et[k][j] for k in range(4)) for j in range(4)] for i in range(4)])
         for xi, X in enumerate(Xs) for ei, Et in enumerate(pool)]
    B = [(yi, fi, [[sum(Y[i][k] * Ft[j][k] for k in range(4)) for j in range(4)] for i in range(4)])
         for yi, Y in enumerate(pool) for fi, Ft in enumerate(pool)]
    Bf = [(yi, fi, [b[j][i] for i in range(4) for j in range(4)]) for yi, fi, b in B]
    for xi, ei, a in A:
        af = [a[i][j] for i in range(4) for j in range(4)]
        for yi, fi, bf in Bf:
            v = sum(x * y for x, y in zip(af, bf))
            if best is None or v < best: best, arg = v, (xi, yi, ei, fi)
    return Fr(best, 8 ** 4), arg
axes = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
tabs72 = [prod(a, b) for a in axes for b in axes]; tabs72 += [cnot(t) for t in tabs72]
T72 = [I8(t) for t in tabs72]
mF2, aF2 = famI_min([I8(F), I8(cF)], T72 + [I8(F), I8(cF)])
chk('F2-C9 FCC fails', mF2 < 0, 'uniform K_F2: min famI %s at (X, Y, E, F) pool indices %s' % (mF2, aF2))
for c0 in INSTC:
    m, a = famI_min([I8(ec, c0)], T72 + [I8(ec, c0)])
    if c0 == 1: chk('EC-C9 FCC fails at c = 1', m < 0, 'uniform K(e_1) = K(E0): min famI %s at %s' % (m, a))
    else: print('RECORD EC-C9 c = %s: min famI over the pool %s at %s' % (c0, m, a))
mq, aq = famI_min([I8(phiW), I8(prod(z3, z3)), I8(cnot(prod(xplus, xplus)))], T72)
chk('Q3-C9 control FCC >= 0', mq >= 0, 'instance control: min %s' % mq)

# ---- T: the extreme-ray invariant c(x)
def rank_of(tabs): return sp.Matrix([[t[m, n] for m in range(4) for n in range(4)] for t in tabs]).rank()
GBOX = [0, 1, iu, 1 + iu, 1 - iu, 2]
def two_sq(N):           # a Gaussian integer alpha = x + i y with x^2 + y^2 = N (x >= y >= 0), or None (integer search)
    for x in range(math.isqrt(N), -1, -1):
        y = math.isqrt(N - x * x)
        if x * x + y * y == N and x >= y: return x + iu * y
    return None
def norm2(z): return int(sp.expand(z * sp.conjugate(z)))
def face_vectors(basis4, weights, limit=40):
    # vectors al*b0 + be*b1 + ga*b2 + de*b3 (orthonormal b's) with |al|^2 = w1|be|^2 + w2|ga|^2 + w3|de|^2 (integer weights)
    out = []
    for be, ga, de in product(GBOX, repeat=3):
        N = weights[0] * norm2(be) + weights[1] * norm2(ga) + weights[2] * norm2(de)
        if N == 0: continue
        al = two_sq(N)
        if al is None: continue
        out.append(al * basis4[0] + be * basis4[1] + ga * basis4[2] + de * basis4[3])
        if len(out) >= limit: break
    return out
def T_F2():
    psis = [negvec(zs(a, b)) for a, b in [(-1, -1), (1, 1), (1, -1), (-1, 1)]]   # t = cap of F first, then cap of cnot F
    psis = [v / sp.sqrt(sp.expand((v.H * v)[0])) for v in psis]
    assert all(sp.simplify((psis[i].H * psis[j])[0]) == (1 if i == j else 0) for i in range(4) for j in range(4))
    face = [cF]
    for v in face_vectors(psis, (1, 1, 1)):
        w = Tpure(v)
        assert ip(F, w) == 0 and ip(cF, w) >= 0 and ip(F, cF) == 0
        face.append(w)
    cF15 = rank_of(face)
    # P00 face: pure states in span(|01>, |10>, |11>) in Z*
    P00 = prod(z3, z3)
    f00 = []
    for a, b, cc in product([0, 1, iu, -1, 2], repeat=3):
        v = sp.Matrix([0, a, b, cc])
        if v == sp.zeros(4, 1): continue
        w = Tpure(v)
        if ip(F, w) >= 0 and ip(cF, w) >= 0: f00.append(w)
    r00 = rank_of(f00)
    pos = ip(P00, F) > 0 and ip(P00, cF) > 0
    # Herm(|00>^perp): q with q|00> = 0 is a 9-dimensional real space: rank of the linear map table -> (q|00>) has kernel 9
    qs_ = sp.symbols('h0:16', real=True)
    gen = sp.zeros(4, 4)
    for k in range(16): gen += qs_[k] * basis[k]
    Q = pW(gen); v00 = Q * sp.Matrix([1, 0, 0, 0])
    eqs = [sp.re(sp.expand(x)) for x in v00] + [sp.im(sp.expand(x)) for x in v00]
    Jm = sp.Matrix([[sp.diff(e, q) for q in qs_] for e in eqs])
    ker = 16 - Jm.rank()
    return cF15, r00, pos, ker, len(f00)
cF15, r00, pos, ker, n00 = T_F2()
chk('F2-T c(F) = 15', cF15 == 15, 'rank of 19 members of K_F2 ∩ F^perp (pure tables with |<t|v>|^2 = |v|^2/2, and cnot F)')
chk('F2-T c(P00) = 9', r00 == 9 and pos and ker == 9, 'rank %s of %s members of Q3 ∩ Z* ∩ P00^perp; ipW(P00, z) > 0; '
    'span bound dim Herm(|00>^perp) = %s' % (r00, n00, ker))
def T_EC(c0):
    e = ec.subs(cs, c0)
    vs = {}
    for v in eigvecs(e):
        d = sp.expand((v.H * pW(ec).subs(cs, 1) * v)[0] / (v.H * v)[0])   # pW(e_1) eigenvalue: (1 + d c)/4 with D-value d
        vs.setdefault(sp.nsimplify(4 * d - 1), []).append(v / sp.sqrt(sp.expand((v.H * v)[0])))
    fm, fp = vs[-2][0], vs[2][0]
    f0, f1 = sp.GramSchmidt([vs[0][0], vs[0][1]], True)
    B4 = [fm, fp, f0, f1]
    assert all(sp.simplify((B4[i].H * B4[j])[0]) == (1 if i == j else 0) for i in range(4) for j in range(4))
    # |al|^2 (2c0 - 1) = (2c0 + 1)|be|^2 + |ga|^2 + |de|^2, scaled to integer weights
    k = 1 / (2 * c0 - 1); wts = ((2 * c0 + 1) * k, k, k)
    assert all(sp.Rational(x).q == 1 for x in wts)
    face = []
    for v in face_vectors(B4, tuple(int(x) for x in wts)):
        w = Tpure(v)
        assert ip(e, w) == 0
        face.append(w)
    rf = rank_of(face) if face else 0
    f00 = []
    for a, b, cc in product([0, 1, iu, -1, 2], repeat=3):
        v = sp.Matrix([0, a, b, cc])
        if v == sp.zeros(4, 1): continue
        w = Tpure(v)
        if ip(e, w) >= 0: f00.append(w)
    return rf, len(face), rank_of(f00), ip(prod(z3, z3), e)
for c0 in INSTC:
    rf, nf, r00e, p00 = T_EC(c0)
    chk('EC-T c(e_c) = 15 at c = %s' % c0, rf == 15, 'rank of %s pure tables on the cap boundary 1 + c<D> = 0' % nf)
    chk('EC-T c(P00) = 9 at c = %s' % c0, r00e == 9 and p00 > 0 and ker == 9, 'ipW(P00, e_c) = %s > 0' % p00)
# Q3 control for T: c(P00) = 9 and c(phiW) = 9 in Q3
q00 = [Tpure(sp.Matrix([0, a, b, cc])) for a, b, cc in product([0, 1, iu, -1, 2], repeat=3) if (a, b, cc) != (0, 0, 0)]
phi = sp.Matrix([1, 0, 0, 1])
perp = [sp.Matrix([1, 0, 0, -1]), sp.Matrix([0, 1, 0, 0]), sp.Matrix([0, 0, 1, 0])]
qphi = [Tpure(a * perp[0] + b * perp[1] + cc * perp[2]) for a, b, cc in product([0, 1, iu, -1, 2], repeat=3) if (a, b, cc) != (0, 0, 0)]
chk('Q3-T c(P00) = c(phiW) = 9', rank_of(q00) == 9 and rank_of(qphi) == 9 and all(ip(phiW, w) == 0 for w in qphi),
    'Q3: pure states orthogonal to |00> and to the Bell vector span 9 dimensions each')

# ---- countercontrols
e32 = E(0, 0) + Rt(3, 2) * (E(1, 3) - E(2, 2))
ev32 = pW(e32).eigenvals(); n32 = [l for l in ev32 if l < 0]
cc1 = not (len(n32) == 1 and all(l >= -n32[0] for l in ev32 if l != n32[0]))
RES['CC1 e_{3/2} fails certificate'] = cc1
print('COUNTERCONTROL CC1 e_{3/2}: eigenvalues %s -> certificate %s' % (sorted(ev32), 'fails (as required)' if cc1 else 'HOLDS (FAIL)'))
e12 = ec.subs(cs, HALF)
cc2 = min(pW(e12).eigenvals()) >= 0
RES['CC2 e_{1/2} PSD'] = cc2
print('COUNTERCONTROL CC2 e_{1/2}: eigenvalues %s -> %s' % (sorted(pW(e12).eigenvals()), 'PSD: K(e_{1/2}) = Q3 (as required)' if cc2 else 'not PSD (FAIL)'))
Rxc = sp.Matrix([[1, 0, 0], [0, Rt(3, 5), -Rt(4, 5)], [0, Rt(4, 5), Rt(3, 5)]])
gF = actC(Rxc, F)
cap1, cap2 = negvec(F), negvec(gF)
both = None
for k in range(0, 9):
    for ph in (1, iu, -1, -iu):
        v = cap1 + Rt(k, 4) * ph * cap2
        w = Tpure(v)
        if ip(F, w) < 0 and ip(gF, w) < 0: both = (k, ph, ip(F, w), ip(gF, w)); break
    if both: break
RES['CC3 non-orthogonal pair: two violations'] = both is not None and ip(F, gF) != 0
print('COUNTERCONTROL CC3 {F, actC Rx F} (cos 3/5): ipW(F, gF) = %s; pure state with both pairings negative: %s' % (ip(F, gF), both))
cv = (sp.Matrix([HALF, -HALF, 0, 0]).T * chainW * sp.Matrix([HALF, 0, 0, -HALF]))[0]
cc5 = actT(reflY, phiW) == idW and cnot(idW) == chainW and cv == Rt(-1, 2) and min(pW(idW).eigenvals()) < 0
RES['CC5 twin fails H2; Q3 not reflY-invariant'] = cc5
print('COUNTERCONTROL CC5 twin: actT reflY phiW = idW, cnot idW = chainW, value %s; idW not PSD: %s' % (cv, cc5))

bad = [k for k, v in RES.items() if not v]
print('summary: %d checks, %d failed%s' % (len(RES), len(bad), (': ' + ', '.join(bad)) if bad else ''))
if not bad:
    print('VERDICT C1-CONES-EXACT: K_F2 and K(e_c) (every c in (1/2, 1]) satisfy H1, H2 at level (i), the H3 certificates, '
          'the maxCone bound and the slice; both are moved by a G16 generator (level (i) only), by actT reflY, and by the '
          'one-token maps listed with witnesses; uniform FCC fails (K_F2: %s; K(e_1): exact); c = 15 on the defects and 9 '
          'on P00; controls green' % mF2)
else:
    print('NO VERDICT')

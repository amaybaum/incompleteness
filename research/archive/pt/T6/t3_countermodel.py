# t3_countermodel.py -- T6 node C1: the explicit countermodel K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F (stage 3 X K4 / U K_F;
# R6 Table A2), rebuilt here from the kernel's definitions with my own code, and the exact witnesses that it violates
# (b) in its weakest sufficient forms.  Exact arithmetic only (fractions, sympy rationals with I and sqrt).
# DECISION RULE (fixed before the first run, 19:08:34Z by date -u):
#  Transcription from L (CompositeDimension.lean:93-202, :741-799; K2Guard.lean:46, :101-104; KInfFoundations.lean:
#  411-425, :449-487): hom, prodState, Hom(N) = 1 ⊕ N, actT N ω = ω·Hom(N)^T, actC N ω = Hom(N)·ω, sgn/pc/pt/cnot,
#  nflip = diag(1,-1,-1), reflY = diag(1,-1,1), z3, xplus, rot3 = R_z, cyc3 (x,y,z) -> (z,x,y).  Dictionary (not a
#  kernel object at L; a construction tool of the countermodel): M(ω) = Σ ω_μν σ_μ⊗σ_ν, Q3 = {ω : M(ω) ⪰ 0},
#  ipW(a,b) = Σ a_μν b_μν, tr(M(a)M(b)) = 4 ipW(a,b).  Z_F = {z_s}, z_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4.
#  D0 dictionary: (a) cnot = Ad(CNOT) (control first) on the 16 basis tables; (b) for U in {X, Y, Z, U_J, Ux90, Uy90,
#     Uz90, Ux(3/5)} the matrix R(U)_ij = tr(σ_i U σ_j U†)/2 is as named and actC R(U) = Ad(U⊗I), actT R(U) = Ad(I⊗U)
#     on the 16 basis tables; (c) actC reflY ∘ actT reflY = global transpose; (d) tr(M(a)M(b)) = 4 ipW(a,b) on the
#     256 basis pairs.
#  Z1 M(z_s) = I/2 - P_s with P_s = (I - s1 X⊗Z - s2 Y⊗Y + s1 s2 Z⊗X)/4; P_s² = P_s, tr P_s = 1, P_s P_t = 0 (s≠t),
#     Σ P_s = I; p_s := table(P_s).
#  Z2 ipW(z_s, z_t) = [s=t]/4; ipW(z_s, p_s) = -1/8; tr M(z_s) = 1.
#  Z3 H1: symbolic: ipW(prodState x y, z_s) = (1 + x·M_s y)/4 with M_s a signed permutation (M_s^T M_s = I) and
#     2(1 + x·M_s y) = |x + M_s y|² + (1-|x|²) + (1-|y|²); M(prodState x y) = (I + x·σ)⊗(I + y·σ).
#  Z4 H3 [W proof in TEST.md]; instance control of its correction lemma: 600 deterministic real rational PSD q
#     (q = A Aᵀ and q = k P_s + A Aᵀ, k in {8,16,24,32,40}, A from a fixed LCG with entries in -2..2); for each, (i) at most one t has
#     <q, z_t>_tr < 0; (ii) for that t, q' = q + λ M(z_t), λ = -<q,z_t>_tr, is PSD (all coefficients of the
#     characteristic polynomial alternate correctly) and <q', z_u>_tr >= 0 for all u.  Non-vacuous: at least 100
#     instances have a negative pairing.  Countercontrol CC-Z4: for the non-orthogonal family {z_s, actC Rx(3/5) z_s}
#     the pure state P_s has two negative pairings (property (i) fails).
#  Z5 H2 level (ii): Gbig = <cnot, actC D ∘ actT D' (D, D' signed diagonal, det D det D' = 1)> generated exactly as
#     16x16 signed permutations; order printed (record: 64, X RESULT:186); every element maps Z_F onto Z_F; every
#     generator is M ↦ V M V† or M ↦ V Mᵀ V† for a Pauli product V on the 16 basis tables (so Gbig ⊆ Aut(Q3));
#     every element fixes the (0,0) entry.  Record: SWAP maps Z_F onto Z_F.
#  Z6 K ≠ Q3: M(z_s) P_s = -(1/2) P_s.
#  Z7 I3.44 consistency (no_candidateCone_cnot_reflY, K2Guard.lean:143): some z_s, w in K with ipW(actT reflY z_s, w) < 0.
#  Z8 LT on W 3 (K-independent): the 16 tables ehom(e)⊗ehom(f), e, f in {unit, sharp effects along ±e_i}, have rank 16.
#  B  (b) witnesses, each token τ in {C, T}: for g in {R_x(π/2), R_y(π/2), R_z(π/2), R_x(t), R_z(t) with
#     (cos t, sin t) = (3/5, 4/5), cyc3, cyc3^-1}: an s and a certified y in K (y a defect, or y with M(y) a trace-one
#     projector and ipW(y, z_u) >= 0 for all u) with ipW(g_τ z_s, y) < 0; the most negative over the pool
#     {z_u} ∪ {h_τ' p_u : h in {R_a(±π/2), cyc3^±1}, τ', u} ∪ {36 axis products} is printed.  Symbolic flow law: for
#     each axis a, token τ, sign s: ipW(R_a(c, sn)_τ z_s, R_a(0, 1)_τ p_s) = -sn/8 identically in (c, sn).
#  Countercontrols for B: (i) for g in {nflip, rot3 π} on each token, g z_s ∈ Z_F for every s and the pool yields no
#     negative pairing; (ii) §A.21: for every tested g and every u, M(g_τ p_u) is a trace-one projector (Q3 kept).
#  VERDICT C1-KZF-EXACT printed iff every check passes and every countercontrol behaves as stated; else VERDICT NONE.
#  Pre-run edits (19:11Z, before the first run): the Z4 weights k fixed as {8,..,40}; tableOf computes tr(A S) from
#  the four nonzero entries of each Pauli product (same value, faster).
import sympy as sp
from fractions import Fraction as F
from itertools import product

# ---------- kernel transcription (tables: 4x4 lists of Fractions) ----------
def E(m, n): return [[F(1) if (i, j) == (m, n) else F(0) for j in range(4)] for i in range(4)]
def add(a, b): return [[a[i][j] + b[i][j] for j in range(4)] for i in range(4)]
def scal(c, a): return [[c * a[i][j] for j in range(4)] for i in range(4)]
def mm(a, b): return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a): return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
def hom(x): return [F(1)] + [F(v) for v in x]
def prodState(x, y): hx, hy = hom(x), hom(y); return [[hx[m] * hy[n] for n in range(4)] for m in range(4)]
def Hom(N):
    H = [[F(1) if i == j == 0 else F(0) for j in range(4)] for i in range(4)]
    for i in range(3):
        for j in range(3): H[i + 1][j + 1] = F(N[i][j])
    return H
def actT(N, w): return mm(w, tr(Hom(N)))
def actC(N, w): return mm(Hom(N), w)
SGN = lambda m, n: -1 if (m, n) in [(1, 3), (2, 2)] else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnot(w): return [[SGN(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]
def ipW(a, b): return sum(a[i][j] * b[i][j] for i in range(4) for j in range(4))
def D3(a, b, c): return [[F(a), 0, 0], [0, F(b), 0], [0, 0, F(c)]]
nflip, reflY, I3 = D3(1, -1, -1), D3(1, -1, 1), D3(1, 1, 1)
RzPi = D3(-1, -1, 1)
cyc3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]            # cyc3 v = (v2, v0, v1)
cyc3i = tr(cyc3)
def Rx(c, s): return [[1, 0, 0], [0, c, -s], [0, s, c]]
def Ry(c, s): return [[c, 0, s], [0, 1, 0], [-s, 0, c]]
def Rz(c, s): return [[c, -s, 0], [s, c, 0], [0, 0, 1]]
xplus, z3 = [1, 0, 0], [0, 0, 1]
key = lambda w: tuple(tuple(r) for r in w)
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def zs(s1, s2): return scal(F(1, 4), add(add(E(0, 0), scal(s1, E(1, 3))), add(scal(s2, E(2, 2)), scal(-s1 * s2, E(3, 1)))))
ZF = [zs(*s) for s in SIGNS]
ZFK = set(key(z) for z in ZF)
RES = {}
def chk(cid, ok, note=''):
    RES[cid] = bool(ok); print('CHECK %-30s %s %s' % (cid, 'PASS' if ok else 'FAIL', note))

# ---------- dictionary (sympy, exact) ----------
iu = sp.I
sg = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
SS = [[kron(sg[m], sg[n]) for n in range(4)] for m in range(4)]
def Mof(w): return sum((sp.Rational(w[m][n].numerator, w[m][n].denominator) * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4))
NZ = [[[(i, j, SS[m][n][j, i]) for i in range(4) for j in range(4) if SS[m][n][j, i] != 0] for n in range(4)] for m in range(4)]
def tableOf(A):
    out = []
    for m in range(4):
        row = []
        for n in range(4):
            v = sp.nsimplify(sp.expand(sum(A[i, j] * c for i, j, c in NZ[m][n]) / 4))
            assert sp.im(v) == 0, 'non-real table entry'
            v = sp.Rational(sp.re(v)); row.append(F(int(v.p), int(v.q)))
        out.append(row)
    return out
basis = [E(m, n) for m in range(4) for n in range(4)]
P0, P1 = sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]])
CNOT = kron(P0, sg[0]) + kron(P1, sg[1])
chk('D0a cnot=Ad(CNOT)', all(tableOf(CNOT * Mof(b) * CNOT.H) == cnot(b) for b in basis), '16/16 basis tables')
def Rof(U):
    R = sp.Matrix(3, 3, lambda i, j: sp.nsimplify(sp.expand((sg[i + 1] * U * sg[j + 1] * U.H).trace() / 2)))
    return [[F(int(sp.Rational(R[i, j]).p), int(sp.Rational(R[i, j]).q)) for j in range(3)] for i in range(3)]
r2, r5 = sp.sqrt(2), sp.sqrt(5)
UJ = (sg[0] - iu * (sg[1] + sg[2] + sg[3])) / 2
Ux90, Uy90, Uz90 = (sg[0] - iu * sg[1]) / r2, (sg[0] - iu * sg[2]) / r2, (sg[0] - iu * sg[3]) / r2
Ux35 = (2 * sg[0] - iu * sg[1]) / r5                        # cos(t/2) = 2/sqrt5, sin(t/2) = 1/sqrt5: cos t = 3/5
named = [('X', sg[1], nflip), ('Y', sg[2], D3(-1, 1, -1)), ('Z', sg[3], RzPi), ('U_J', UJ, cyc3),
         ('Ux90', Ux90, Rx(0, 1)), ('Uy90', Uy90, Ry(0, 1)), ('Uz90', Uz90, Rz(0, 1)),
         ('Ux(3/5)', Ux35, Rx(F(3, 5), F(4, 5)))]
okb = True
for nm, U, Rexp in named:
    R = Rof(U)
    okb &= (R == [[F(v) for v in r] for r in Rexp])
    UI, IU = kron(U, sg[0]), kron(sg[0], U)
    okb &= all(tableOf(UI * Mof(b) * UI.H) == actC(R, b) for b in basis)
    okb &= all(tableOf(IU * Mof(b) * IU.H) == actT(R, b) for b in basis)
chk('D0b R(U), actC/actT=Ad', okb, 'X, Y, Z, U_J (=cyc3), quarter-turns about x, y, z, Rx(cos 3/5)')
chk('D0c transpose', all(tableOf(Mof(b).T) == actC(reflY, actT(reflY, b)) for b in basis), 'actC reflY ∘ actT reflY = M ↦ Mᵀ')
chk('D0d trace pairing', all(sp.expand((Mof(a) * Mof(b)).trace()) == 4 * sp.Rational(ipW(a, b).numerator, ipW(a, b).denominator)
                             for a in basis for b in basis), '256 basis pairs')

# ---------- Z1, Z2, Z6 ----------
Id4 = sp.eye(4)
XZ, YY, ZX = SS[1][3], SS[2][2], SS[3][1]
Ps = {s: (Id4 - s[0] * XZ - s[1] * YY + s[0] * s[1] * ZX) / 4 for s in SIGNS}
ok1 = all(sp.expand(Mof(zs(*s)) - (Id4 / 2 - Ps[s])) == sp.zeros(4, 4) for s in SIGNS)
ok1 &= all(sp.expand(Ps[s] * Ps[s] - Ps[s]) == sp.zeros(4, 4) and Ps[s].trace() == 1 for s in SIGNS)
ok1 &= all(sp.expand(Ps[s] * Ps[t]) == sp.zeros(4, 4) for s in SIGNS for t in SIGNS if s != t)
ok1 &= sp.expand(sum((Ps[s] for s in SIGNS), sp.zeros(4, 4)) - Id4) == sp.zeros(4, 4)
chk('Z1 M(z_s)=I/2-P_s', ok1, 'P_s orthogonal rank-one projectors summing to I')
pS = {s: tableOf(Ps[s]) for s in SIGNS}
ok2 = all(ipW(zs(*s), zs(*t)) == (F(1, 4) if s == t else 0) for s in SIGNS for t in SIGNS)
ok2 &= all(ipW(zs(*s), pS[s]) == F(-1, 8) for s in SIGNS) and all(Mof(zs(*s)).trace() == 1 for s in SIGNS)
chk('Z2 pairings', ok2, 'ipW(z_s,z_t) = [s=t]/4; ipW(z_s,p_s) = -1/8; tr M(z_s) = 1')
chk('Z6 K != Q3', all(sp.expand(Mof(zs(*s)) * Ps[s] + Ps[s] / 2) == sp.zeros(4, 4) for s in SIGNS), 'M(z_s) P_s = -(1/2) P_s')

# ---------- Z3: H1 (symbolic) ----------
xs, ys = sp.symbols('x1:4'), sp.symbols('y1:4')
def symtab(w): return sp.Matrix(4, 4, lambda i, j: sp.Rational(w[i][j].numerator, w[i][j].denominator))
def symprod(x, y):
    hx, hy = [1] + list(x), [1] + list(y)
    return sp.Matrix(4, 4, lambda i, j: hx[i] * hy[j])
def sip(a, b): return sp.expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))
ok3 = True
for s in SIGNS:
    v4 = sp.expand(4 * sip(symprod(xs, ys), symtab(zs(*s))))
    Ms = sp.Matrix(3, 3, lambda i, j: v4.coeff(xs[i]).coeff(ys[j]))
    const = v4.subs({**{x: 0 for x in xs}, **{y: 0 for y in ys}})
    X, Y = sp.Matrix(xs), sp.Matrix(ys)
    ok3 &= const == 1 and sp.expand(v4 - 1 - (X.T * Ms * Y)[0]) == 0 and Ms.T * Ms == sp.eye(3)
    sos = ((X + Ms * Y).T * (X + Ms * Y))[0] + (1 - (X.T * X)[0]) + (1 - (Y.T * Y)[0])
    ok3 &= sp.expand(2 * v4 - sos) == 0
rho = lambda v: sg[0] + v[0] * sg[1] + v[1] * sg[2] + v[2] * sg[3]
Mp = sum((symprod(xs, ys)[m, n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4))
ok3 &= sp.expand(Mp - kron(rho(xs), rho(ys))) == sp.zeros(4, 4)
chk('Z3 H1 SOS', ok3, '4 ipW(prodState x y, z_s) = 1 + x·M_s y, M_s orthogonal; 2(1+x·M_s y) = |x+M_s y|²+(1-|x|²)+(1-|y|²)')

# ---------- Z4: instance control of the correction lemma (real symmetric rational PSD) ----------
def det(a):
    a = [r[:] for r in a]; n = len(a); d = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if a[r][c] != 0), None)
        if p is None: return F(0)
        if p != c: a[c], a[p] = a[p], a[c]; d = -d
        d *= a[c][c]
        for r in range(c + 1, n):
            f = a[r][c] / a[c][c]
            for k in range(c, n): a[r][k] -= f * a[c][k]
    return d
def psd(a):
    n = len(a)
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if mask >> i & 1]
        if det([[a[i][j] for j in idx] for i in idx]) < 0: return False
    return True
def toF(A): return [[F(int(sp.Rational(A[i, j]).p), int(sp.Rational(A[i, j]).q)) for j in range(4)] for i in range(4)]
MZ = {s: toF(Mof(zs(*s))) for s in SIGNS}
PF = {s: toF(Ps[s]) for s in SIGNS}
def trp(a, b): return sum(a[i][j] * b[j][i] for i in range(4) for j in range(4))
seed = [20261010]
def lcg():
    seed[0] = (1103515245 * seed[0] + 12345) % (1 << 31); return (seed[0] >> 16) % 5 - 2
inst, neg, okz4 = 0, 0, True
for k in range(600):
    A = [[F(lcg()) for _ in range(4)] for _ in range(4)]
    q = mm(A, tr(A))
    if k % 2 == 1:
        s0 = SIGNS[(k // 2) % 4]; q = add(q, scal(F(8 * (1 + (k // 8) % 5)), PF[s0]))
    pr = {s: trp(q, MZ[s]) for s in SIGNS}
    negs = [s for s in SIGNS if pr[s] < 0]
    inst += 1
    if len(negs) > 1: okz4 = False
    if negs:
        neg += 1; t = negs[0]; lam = -pr[t]
        q2 = add(q, scal(lam, MZ[t]))
        okz4 &= psd(q2) and all(trp(q2, MZ[u]) >= 0 for u in SIGNS) and trp(q2, MZ[t]) == 0
chk('Z4 correction lemma', okz4 and neg >= 100, '%d instances, %d with a negative pairing, all corrected into Q3 ∩ Z_F*' % (inst, neg))
Ux35I = kron(Ux35, sg[0])
P2 = {s: sp.expand(Ux35I * Ps[s] * Ux35I.H) for s in SIGNS}
Z2fam = {s: Id4 / 2 - P2[s] for s in SIGNS}
twoneg = all(sp.expand((Ps[s] * (Id4 / 2 - Ps[s])).trace()) < 0 and sp.expand((Ps[s] * Z2fam[s]).trace()) < 0 for s in SIGNS)
chk('CC-Z4 non-orthogonal family', twoneg, 'P_s pairs negatively with z_s and with actC Rx(3/5) z_s: property (i) fails, as it must')

# ---------- Z5: H2 at level (ii): Gbig ----------
IDX = [(m, n) for m in range(4) for n in range(4)]
def elem_of(fn):
    perm, sgn = [], []
    for (m, n) in IDX:
        img = fn(E(m, n))       # image of a basis table: a signed basis table
        nz = [(i, j) for i in range(4) for j in range(4) if img[i][j] != 0]
        assert len(nz) == 1 and abs(img[nz[0][0]][nz[0][1]]) == 1
        perm.append(IDX.index(nz[0])); sgn.append(int(img[nz[0][0]][nz[0][1]]))
    # element as (p, sigma): (g w)[p[k]] = sigma[k] * w[k]
    return (tuple(perm), tuple(sgn))
def apply_el(el, w):
    p, sgn = el; out = [[F(0)] * 4 for _ in range(4)]
    for k, (m, n) in enumerate(IDX):
        i, j = IDX[p[k]]; out[i][j] += sgn[k] * w[m][n]
    return out
def compose(a, b):      # a after b
    pa, sa = a; pb, sb = b
    return (tuple(pa[pb[k]] for k in range(16)), tuple(sb[k] * sa[pb[k]] for k in range(16)))
diags = [D3(*d) for d in product([1, -1], repeat=3)]
dsgn = lambda D: D[0][0] * D[1][1] * D[2][2]
locs = [elem_of(lambda w, D=D, Dp=Dp: actC(D, actT(Dp, w))) for D in diags for Dp in diags if dsgn(D) * dsgn(Dp) == 1]
gens = [elem_of(cnot)] + locs
idel = (tuple(range(16)), tuple([1] * 16))
grp, frontier = {idel}, [idel]
while frontier:
    nxt = []
    for a in frontier:
        for g in gens:
            c = compose(g, a)
            if c not in grp: grp.add(c); nxt.append(c)
    frontier = nxt
okG = all(set(key(apply_el(g, z)) for z in ZF) == ZFK for g in grp)
fix00 = all(apply_el(g, E(0, 0)) == E(0, 0) for g in grp)
paulis = [kron(sg[a], sg[b]) for a in range(4) for b in range(4)]
def autQ3(fn):
    for V in paulis:
        if all(tableOf(V * Mof(b) * V.H) == fn(b) for b in basis): return 'conj'
        if all(tableOf(V * Mof(b).T * V.H) == fn(b) for b in basis): return 'transpose'
    return None
modes = [autQ3(lambda w, D=D, Dp=Dp: actC(D, actT(Dp, w))) for D in diags for Dp in diags if dsgn(D) * dsgn(Dp) == 1]
chk('Z5 Gbig', len(grp) == 64 and okG and fix00 and all(m is not None for m in modes) and RES['D0a cnot=Ad(CNOT)'],
    'order %d; every element permutes Z_F and fixes (0,0); 32 local generators in Aut(Q3) (%d conj, %d transpose); cnot = Ad(CNOT)'
    % (len(grp), modes.count('conj'), modes.count('transpose')))
swapZ = set(key(tr(z)) for z in ZF) == ZFK
print('RECORD SWAP permutes Z_F: %s' % swapZ)

# ---------- the certified pool of elements of K(Z_F) ----------
def isproj(w):
    M = Mof(w); return sp.expand(M * M - M) == sp.zeros(4, 4) and M.trace() == 1
def inZstar(w): return all(ipW(w, z) >= 0 for z in ZF)
QUARTER = [('Rx+90', Rx(0, 1)), ('Rx-90', Rx(0, -1)), ('Ry+90', Ry(0, 1)), ('Ry-90', Ry(0, -1)),
           ('Rz+90', Rz(0, 1)), ('Rz-90', Rz(0, -1)), ('cyc3', cyc3), ('cyc3^-1', cyc3i)]
def act(tok, N, w): return actC(N, w) if tok == 'C' else actT(N, w)
pool, rejected, q3ctrl = [], 0, True
for i, s in enumerate(SIGNS): pool.append(('z%s' % (s,), ZF[i]))
for tok in 'CT':
    for nm, N in QUARTER:
        for s in SIGNS:
            y = act(tok, N, pS[s])
            pr = isproj(y)
            q3ctrl &= pr
            if pr and inZstar(y): pool.append(('%s_%s p%s' % (nm, tok, s), y))
            else: rejected += 1
AX = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
for a in AX:
    for b in AX: pool.append(('prod(%s,%s)' % (a, b), prodState(a, b)))
print('POOL: %d certified elements of K (4 defects, %d rotated pure states in Q3 ∩ Z_F*, 36 axis products); %d rotated pure states not in Z_F* (not used)'
      % (len(pool), len(pool) - 40, rejected))

# ---------- Z7: I3.44 consistency ----------
best = min((ipW(actT(reflY, z), y), zl, yl) for zl, z in zip(['z%s' % (s,) for s in SIGNS], ZF) for yl, y in pool)
chk('Z7 I3.44 consistency', best[0] < 0, 'actT reflY %s pairs %s with %s ∈ K: actT reflY does not preserve K(Z_F)' % (best[1], best[0], best[2]))

# ---------- Z8: local tomography on W 3 (K-independent) ----------
ev = [[F(1), F(0), F(0), F(0)]] + [[F(1, 2)] + [F(sg_ * (1 if j == i else 0), 2) for j in range(3)] for i in range(3) for sg_ in (1, -1)]
rows = [[a[m] * b[n] for m in range(4) for n in range(4)] for a in ev for b in ev]
def rank(rows):
    r = [x[:] for x in rows]; rk, col = 0, 0
    ncol = len(r[0])
    for col in range(ncol):
        p = next((i for i in range(rk, len(r)) if r[i][col] != 0), None)
        if p is None: continue
        r[rk], r[p] = r[p], r[rk]
        for i in range(len(r)):
            if i != rk and r[i][col] != 0:
                f = r[i][col] / r[rk][col]; r[i] = [r[i][k] - f * r[rk][k] for k in range(ncol)]
        rk += 1
    return rk
chk('Z8 LT on W 3', rank(rows) == 16, 'the 49 product-effect tables (unit and sharp effects along ±e_i) span W 3')

# ---------- B: (b) witnesses ----------
GTEST = [('R_x(pi/2)', Rx(0, 1)), ('R_y(pi/2)', Ry(0, 1)), ('R_z(pi/2)', Rz(0, 1)),
         ('R_x(cos 3/5)', Rx(F(3, 5), F(4, 5))), ('R_z(cos 3/5)', Rz(F(3, 5), F(4, 5))),
         ('cyc3', cyc3), ('cyc3^-1', cyc3i)]
okB = True
for tok in 'CT':
    for nm, N in GTEST:
        best = min((ipW(act(tok, N, ZF[i]), y), '%s' % (SIGNS[i],), yl) for i in range(4) for yl, y in pool)
        okB &= best[0] < 0
        print('WITNESS %s on %s: min ipW(g z_s, y) = %s at s = %s, y = %s' % (nm, tok, best[0], best[1], best[2]))
chk('B (b) witnesses', okB, 'every tested flow member and J, on each token, moves some z_s out of K(Z_F)')
cs, sn = sp.symbols('c sn')
SR = {'x': lambda c, s: sp.Matrix([[1, 0, 0], [0, c, -s], [0, s, c]]), 'y': lambda c, s: sp.Matrix([[c, 0, s], [0, 1, 0], [-s, 0, c]]),
      'z': lambda c, s: sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])}
def sHom(N): H = sp.eye(4); H[1:, 1:] = N; return H
def sact(tok, N, w): return sHom(N) * w if tok == 'C' else w * sHom(N).T
okL, okY = True, True
for ax in 'xyz':
    for tok in 'CT':
        for s in SIGNS:
            lhs = sip(sact(tok, SR[ax](cs, sn), symtab(zs(*s))), sact(tok, SR[ax](0, 1), symtab(pS[s])))
            okL &= sp.expand(lhs + sn / 8) == 0
            y = act(tok, {'x': Rx, 'y': Ry, 'z': Rz}[ax](0, 1), pS[s])
            okY &= isproj(y) and inZstar(y)
chk('B flow law', okL and okY, 'ipW(R_a(t)_τ z_s, R_a(π/2)_τ p_s) = -sin(t)/8 for a in {x,y,z}, τ in {C,T}, all s; the witness is in Q3 ∩ Z_F*')

# ---------- countercontrols for B ----------
okI = True
for tok in 'CT':
    for nm, N in [('nflip', nflip), ('rot3 pi', RzPi)]:
        imgs = set(key(act(tok, N, z)) for z in ZF)
        mn = min(ipW(act(tok, N, z), y) for z in ZF for yl, y in pool)
        okI &= imgs == ZFK and mn >= 0
        print('CONTROL %s on %s: permutes Z_F %s; min pairing over the pool %s' % (nm, tok, imgs == ZFK, mn))
chk('CC-B symmetries', okI, 'nflip and rot3 π on either token permute Z_F; no negative pairing (no false witness)')
chk('CC-B Q3 kept (A.21)', q3ctrl, 'every rotated Bell-type pure state is a trace-one projector: the modeled actions preserve Q3')

ALL = all(RES.values())
print('SUMMARY %d/%d checks pass' % (sum(RES.values()), len(RES)))
if ALL:
    print('VERDICT C1-KZF-EXACT: K(Z_F) satisfies H1 (SOS), H2 at level (ii) (Gbig of order 64), the H3 ingredients and '
          'the correction-lemma control, K ≠ Q3, the I3.44 consistency, LT on W 3; every coordinate flow member with '
          'sin t ≠ 0 and cyc3^±1, on either token, moves K(Z_F) out (exact witnesses; flow law -sin(t)/8)')
else:
    print('VERDICT NONE: failing %s' % ', '.join(k for k, v in RES.items() if not v))

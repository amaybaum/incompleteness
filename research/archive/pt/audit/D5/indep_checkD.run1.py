#!/usr/bin/env python3
"""Coordinator's independent check of thread D5 (stage 5, BRIDGE-DERIVE).  Exact (sympy / integers) unless a line
says FLOAT.  Written from D5's RESULT/NOTES claims, not from its code: different representations throughout
(Pauli-string commutators in u(4) instead of 16x16 table maps; the permutation group and the phase torus of the
monomial class enumerated instead of a determinant scan alone; the level identity checked on the permutation matrices
and the affine step separately; K(Z_F) defects built from the stage-3 formula and their states as eigenvectors).
Run: python3 -I -B indep_checkD.py  from pt/audit/D5/ (reads two Lean files at L read-only).
DECISION RULE (fixed before the first run): every line prints CONFIRMED or MISMATCH; countercontrols (ids ending
'c') are CONFIRMED exactly when the tested property fails on them; INDEP-D-FIXED iff every line is CONFIRMED.

Claims checked (D5 RESULT/NOTES node -> check id):
 A  transcription: Lean sgn/pc/pt (CompositeDimension.lean) = Ad(CNOT control-first) on tables (A1, A1c);
    nflip = Ad(X) rotation (A2); cycEquiv = rotation of U_J = (I - i(X+Y+Z))/2, x->y->z->x (A3);
    actC R(U) = Ad(U x I) with homMap fixing coordinate 0 (A4; the no-signalling identity of candidate epsilon).
 B  Lie closures in u(4) by Pauli-string commutators (B1 dim 6 with ad(s_k x P+-) inside; B1c drive alone 2;
    B2c target drive 1; B5 W1 drive+phase control 6; B5c W1c phase alone 1; B6c W3c both phases 3; B7 W4 target 6).
 C  monomial class: permutations {X x I, I x X, CNOT, SWAP} generate S4 on the basis labels (C1); phase torus full
    modulo the global phase (rank 3 of the exponent lattice, C2); hence the orbit of SEP has rank-1 magnitude
    patterns up to arrangement; phi0 = (1,2,3,4)/sqrt30: min |det| over the 24 arrangements = 1/15 (C3) and
    m = max sigma_max^2 = (15 + sqrt221)/30 exactly (C4); c = 513/512 in (1, min(2, 1/m)] exactly (C5);
    C3c: a product magnitude pattern has min |det| = 0; C6 FLOAT sanity: random monomial-orbit overlaps <= m.
 D  lambda countercontrol replicated: family-(i) value for uniform K(E0) at the gate-supplied pair = -1 (D1);
    the Q3 control (Bell table) >= 0 over all 1296 pairs (D2).
 E  K(E0) and the NOT: actC nflip E0 = E00 + E13 + E22 (E1); a pure state in Q3 ∩ {E0}* (hence in K(E0)) pairs
    negatively with the image (E2); E2c: the same state pairs >= 0 with E0.
 F  K(Z_F): the stage-3 defects z_s and D5's psi(s) rays coincide as sets (F0); the flow U(w) fixes every defect for
    |w| = 1 symbolic (F1); U(-1) moves a pure state of K(Z_F) to another ray inside K(Z_F) (F2); actC J z_s leaves
    K(Z_F): pure witness in K(Z_F) with negative pairing (F3); F3c: actC nflip permutes Z_F.
 G  level identity (d2): reindex e_n (1_n x permMat(levelPerm s 1)) = permMat(levelPerm s n) for |S| = 2,3,4 and
    n = 1..4 (G1); the affine step with a symbol (G2); G1c: wrong reindexing fails.
"""
import re, itertools, random
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, simplify, expand, symbols, kronecker_product as kron
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
BASE = '../../base/verification/lean-mathlib/OIBridge/'
I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]
KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def tab(M): return Matrix(4, 4, lambda m, n: sp.nsimplify(simplify(expand((KR[(m, n)] * M).trace()))))
def ipW(a, b): return expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def Ad(U, w): return tab(U * pauliW(w) * U.H)
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])     # control first: |1b> -> |1,b+1>
SWAP = Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
def rotOf(U): return Matrix(3, 3, lambda i, j: sp.nsimplify(simplify(expand((SG[i + 1] * U * SG[j + 1] * U.H).trace() / 2))))
def homMap(Rm):
    M = eye(4)
    for i in range(3):
        for j in range(3): M[i + 1, j + 1] = Rm[i, j]
    return M
def actC(Rm, w): return homMap(Rm) * w
def actT(Rm, w): return w * homMap(Rm).T

print("== A  transcription from the Lean source at L")
cd = open(BASE + 'CompositeDimension.lean', encoding='utf-8').read()
def lean_table(name):
    blk = cd.split('def %s : Fin 4 → Fin 4 → Fin 4' % name, 1)[1].split('/--', 1)[0]
    return {(int(a), int(b)): int(c) for a, b, c in re.findall(r'\|\s*(\d),\s*(\d)\s*=>\s*(\d)', blk)}
PC = lean_table('pc'); PT = lean_table('pt')
sg = re.search(r'def sgn .*?if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1', cd)
NEG = {(int(sg.group(1)), int(sg.group(2))), (int(sg.group(3)), int(sg.group(4)))}
def cnot_lean(w): return Matrix(4, 4, lambda m, n: (-1 if (m, n) in NEG else 1) * w[PC[(m, n)], PT[(m, n)]])
okA1 = len(PC) == 16 and len(PT) == 16 and all(cnot_lean(E(m, n)) == Ad(CNOT, E(m, n)) for m in range(4) for n in range(4))
rec('A1', okA1, 'Lean sgn/pc/pt = Ad(CNOT control-first) on all 16 basis tables', 'NEG=%s' % sorted(NEG))
CNOTt = Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])  # target-first
rec('A1c', any(cnot_lean(E(m, n)) != Ad(CNOTt, E(m, n)) for m in range(4) for n in range(4)), 'target-first CNOT disagrees somewhere')
nf = re.search(r'def nflip[^\n]*\n\s*toFun x := fun i => \(!\[(-?\d), (-?\d), (-?\d)\]', cd)
NF = Matrix.diag(*[int(nf.group(k)) for k in (1, 2, 3)])
rec('A2', NF == rotOf(SX) and NF == Matrix.diag(1, -1, -1), 'nflip = rotation of Ad(X) = R_x(pi) = diag(1,-1,-1)')
kf = open(BASE + 'KInfFoundations.lean', encoding='utf-8').read()
cy = re.search(r'def cycEquiv[^\n]*\n\s*toFun v := !\[v (\d), v (\d), v (\d)\]', kf)
idx = [int(cy.group(k)) for k in (1, 2, 3)]
CYC = Matrix(3, 3, lambda i, j: 1 if idx[i] == j else 0)      # (CYC v)_i = v_{idx[i]}
UJ = (I2 - I * (SX + SY + SZ)) / 2
ex, ey, ez = Matrix([1, 0, 0]), Matrix([0, 1, 0]), Matrix([0, 0, 1])
okA3 = simplify(UJ * UJ.H - I2) == zeros(2, 2) and rotOf(UJ) == CYC and CYC * ex == ey and CYC * ey == ez and CYC * ez == ex and CYC ** 3 == eye(3) and CYC.det() == 1
rec('A3', okA3, 'cycEquiv = rotation of U_J = (I - i(X+Y+Z))/2: x -> y -> z -> x, proper, order 3')
U1 = Matrix([[Q(3, 5), Q(4, 5) * I], [Q(4, 5) * I, Q(3, 5)]]); R1 = rotOf(U1)
okA4 = all(actC(R1, E(m, n)) == Ad(kron(U1, I2), E(m, n)) and actT(R1, E(m, n)) == Ad(kron(I2, U1), E(m, n)) for m in range(4) for n in range(4))
okA4 = okA4 and all((actC(R1, w))[0, n] == w[0, n] for w in [E(m, n) for m in range(4) for n in range(4)] for n in range(4))
rec('A4', okA4, 'actC R(U) = Ad(U x I), actT = Ad(I x U) on 16 tables; actC fixes row 0 (no-signalling identity)')

print("== B  Lie closures in u(4): Pauli-string commutators (real coefficients of i*P)")
# single-qubit product table: s_a s_b = c * s_c with c in {1, i, -1, -i}
def pmul1(a, b):
    if a == 0: return (1, b)
    if b == 0: return (1, a)
    if a == b: return (1, 0)
    c = ({1, 2, 3} - {a, b}).pop()
    # XY = iZ, YZ = iX, ZX = iY ; reversed order gives -i
    return (I if (a, b) in [(1, 2), (2, 3), (3, 1)] else -I, c)
def pmul(P, Qs):
    c1, r1 = pmul1(P[0], Qs[0]); c2, r2 = pmul1(P[1], Qs[1])
    return (expand(c1 * c2), (r1, r2))
STR = [(a, b) for a in range(4) for b in range(4)]
IX = {s: k for k, s in enumerate(STR)}
def comm(u, v):   # u, v: real 16-vectors (coefficients of i*P); returns the commutator's coefficients
    out = [0] * 16
    for p in STR:
        if u[IX[p]] == 0: continue
        for q in STR:
            if v[IX[q]] == 0: continue
            c, r = pmul(p, q); c2, r2 = pmul(q, p)
            # [iP, iQ] = -(PQ - QP) = -(c - c2) R  (R = r = r2) ; must be i * real  -> coefficient of i*R is -(c - c2)/i
            d = expand(-(c - c2) / I)
            if d != 0: out[IX[r]] += u[IX[p]] * v[IX[q]] * d
    return [sp.nsimplify(x) for x in out]
def closure_dim(gens):
    basis = [list(g) for g in gens]
    def rk(vs): return Matrix(vs).rank() if vs else 0
    r = rk(basis); changed = True
    while changed:
        changed = False
        for a in list(basis):
            for b in list(basis):
                c = comm(a, b)
                if any(x != 0 for x in c) and rk(basis + [c]) > r:
                    basis.append(c); r += 1; changed = True
    return r
def vec(*terms):   # terms: (coef, (a,b))
    v = [0] * 16
    for c, s in terms: v[IX[s]] += c
    return v
def conj_cnot(s):  # CNOT P CNOT^-1 decomposed in the Pauli basis (exact)
    M = CNOT * KR[s] * CNOT.H
    return [(sp.nsimplify(simplify((KR[t] * M).trace() / 4)), t) for t in STR if simplify((KR[t] * M).trace()) != 0]
def with_cnot(strings):
    gens = [vec((1, s)) for s in strings]
    gens += [vec(*conj_cnot(s)) for s in strings]
    return gens
X_, Y_, Z_ = 1, 2, 3
dB1 = closure_dim(with_cnot([(X_, 0), (Y_, 0)]))
# ad(s_k x P+-) : P+- = (I +- X)/2 -> s_k x I /2 +- s_k x X /2
targets = [vec((Q(1, 2), (k, 0)), (s * Q(1, 2), (k, X_))) for k in (1, 2, 3) for s in (1, -1)]
alg = with_cnot([(X_, 0), (Y_, 0)])
basis = [list(g) for g in alg]
# rebuild the closure basis explicitly for the containment test
def closure_basis(gens):
    basis = [list(g) for g in gens]
    def rk(vs): return Matrix(vs).rank() if vs else 0
    r = rk(basis); changed = True
    while changed:
        changed = False
        for a in list(basis):
            for b in list(basis):
                c = comm(a, b)
                if any(x != 0 for x in c) and rk(basis + [c]) > r:
                    basis.append(c); r += 1; changed = True
    return basis
CB = closure_basis(alg)
contain = Matrix(CB).rank() == Matrix(CB + targets).rank() == 6
rec('B1', dB1 == 6 and contain, 'drive_C (X x I) + J-conjugate (Y x I) + CNOT conjugates: dim 6, contains all ad(s_k x P+-)', 'dim=%d' % dB1)
rec('B1c', closure_dim(with_cnot([(X_, 0)])) == 2, 'drive on the control alone with CNOT: dim 2 (abelian {X x I, X x X})')
rec('B2c', closure_dim(with_cnot([(0, X_)])) == 1, 'drive on the target alone with CNOT: dim 1 (I x X commutes with CNOT)')
rec('B5', closure_dim(with_cnot([(X_, 0), (Z_, 0)])) == 6, 'W1: drive (x) + phase flow (z) on the control with CNOT: dim 6')
rec('B5c', closure_dim(with_cnot([(Z_, 0)])) == 1, 'W1c: phase flow alone on the control: dim 1')
rec('B6c', closure_dim(with_cnot([(Z_, 0), (0, Z_)])) == 3, 'W3c: phase flows on both tokens: dim 3 (abelian {ZI, IZ, ZZ})')
rec('B7', closure_dim(with_cnot([(0, X_), (0, Z_)])) == 6, 'W4: drive + phase flow on the target with CNOT: dim 6')
rec('B8', closure_dim(with_cnot([(X_, 0), (0, Y_)])) == 15, 'record (C5 census): flow on control + J-conjugate flow on target: dim 15 = su(4)')

print("== C  the monomial (substratum) class transcribed: orbit structure and the seed")
# permutations of the basis labels 0..3 = |00>,|01>,|10>,|11> induced by X x I, I x X, CNOT, SWAP
def perm_of(U): return tuple(next(j for j in range(4) if U[j, i] != 0) for i in range(4))
gens_perm = [perm_of(kron(SX, I2)), perm_of(kron(I2, SX)), perm_of(CNOT), perm_of(SWAP)]
def compose(p, q): return tuple(p[q[i]] for i in range(4))
grp = set(gens_perm); frontier = list(grp)
while frontier:
    nxt = []
    for p in frontier:
        for g in gens_perm:
            for r in (compose(p, g), compose(g, p)):
                if r not in grp: grp.add(r); nxt.append(r)
    frontier = nxt
rec('C1', len(grp) == 24, 'the native permutations {X x I, I x X, CNOT, SWAP} generate S4 on the four basis labels', 'order=%d' % len(grp))
# phase exponent vectors on the labels (00,01,10,11): diag(1,e^{i a}) x I -> (0,0,1,1); I x diag(1,e^{i b}) -> (0,1,0,1);
# CNOT-conjugate of the target phase -> (0,1,1,0)
def expo_of_diag(D): return [sp.nsimplify(sp.arg(D[i, i]) / sp.pi) for i in range(4)]
t = symbols('t', real=True)
Dc = kron(Matrix.diag(1, -1), I2); Dt = kron(I2, Matrix.diag(1, -1)); DtC = CNOT * Dt * CNOT.H
vecs = [Matrix([[0, 0, 1, 1]]), Matrix([[0, 1, 0, 1]]), Matrix([[0, 1, 1, 0]])]
okC2 = perm_of(Dc) == (0, 1, 2, 3) and perm_of(DtC) == (0, 1, 2, 3) and [int(DtC[i, i]) for i in range(4)] == [1, -1, -1, 1]
okC2 = okC2 and Matrix.vstack(*vecs).rank() == 3 and Matrix.vstack(*(vecs + [Matrix([[1, 1, 1, 1]])])).rank() == 4
rec('C2', okC2, 'phase torus: exponent vectors (0,0,1,1), (0,1,0,1), (0,1,1,0) have rank 3; with the global phase rank 4 (full torus mod global phase)')
mags = [1, 2, 3, 4]
dets = sorted(set(abs(p[0] * p[3] - p[1] * p[2]) for p in itertools.permutations(mags)))
rec('C3', dets[0] == 2, 'phi0 = (1,2,3,4)/sqrt30: min |ad - bc| over 24 arrangements = 2/30 = 1/15 > 0 (not rank 1: unreachable)', 'dets=%s /30' % dets)
rec('C3c', min(abs(p[0] * p[3] - p[1] * p[2]) for p in itertools.permutations([1, 2, 2, 4])) == 0, 'product magnitudes (1,2,2,4)/5: some arrangement has det 0')
# m = max over arrangements of sigma_max^2 of the 2x2 magnitude matrix (Frobenius norm 1): exact via eigenvalues of M^T M
best = None
for p in itertools.permutations(mags):
    M = Matrix([[p[0], p[1]], [p[2], p[3]]]) / sqrt(30)
    ev = max((M.T * M).eigenvals().keys(), key=lambda e: float(e))
    if best is None or float(ev) > float(best): best = ev
m_claim = (15 + sqrt(221)) / 30
rec('C4', simplify(best - m_claim) == 0, 'm = max sigma_max^2 over the 24 arrangements = (15 + sqrt221)/30 exactly', 'm=%s ~ %.6f' % (best, float(best)))
c = Q(513, 512)
# c*m <= 1  <=>  2/c - 1 >= sqrt221/15  (both sides positive)  <=> (2/c - 1)^2 >= 221/225
lhs = 2 / c - 1
okC5 = c > 1 and c <= 2 and lhs > 0 and lhs ** 2 >= Q(221, 225) and simplify(c * m_claim) < 1
rec('C5', okC5, 'c = 513/512: 1 < c <= 2 and c*m < 1 exactly (seed admissible on the whole monomial orbit of SEP)', '1/m ~ %.6f, c ~ %.6f' % (1 / float(best), float(c)))
# C6 FLOAT sanity: random product states, random monomial unitaries (phases + S4), overlap with phi0 never exceeds m
random.seed(5)
phi0 = [1 / 30 ** 0.5, 2 / 30 ** 0.5, 3 / 30 ** 0.5, 4 / 30 ** 0.5]
worst = 0.0
for _ in range(4000):
    a = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(2)]; b = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(2)]
    na = sum(abs(x) ** 2 for x in a) ** 0.5; nb = sum(abs(x) ** 2 for x in b) ** 0.5
    prod = [a[i] * b[j] / (na * nb) for i in range(2) for j in range(2)]
    p = random.choice(sorted(grp)); permuted = [prod[p.index(k)] for k in range(4)]
    # optimal phases: align each entry with phi0 (phases are free in the torus mod global)
    ov = sum(phi0[k] * abs(permuted[k]) for k in range(4)) ** 2
    worst = max(worst, ov)
rec('C6', worst <= float(best) + 1e-12, 'FLOAT sanity: 4000 random monomial-orbit product states have overlap^2 with phi0 <= m', 'max=%.6f, m=%.6f' % (worst, float(best)))

print("== D  lambda countercontrol replicated (family-(i) value on uniform cones)")
E0 = E(0, 0) + E(1, 3) - E(2, 2)
def prodState(x, y): return Matrix([1] + list(x)) * Matrix([1] + list(y)).T
units = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
CP = [Ad(CNOT, prodState(x, y)) for x in units for y in units]
def fam1(Xt, Yt, Et, Ft): return ipW(Xt, Et * Yt * Ft.T)
v = fam1(E0, E0, Ad(CNOT, prodState(units[1], units[2])), Ad(CNOT, prodState(units[0], units[1])))
rec('D1', v == -1 and min(fam1(E0, E0, Et, Ft) for Et in CP for Ft in CP) == -1, 'uniform K(E0): family-(i) value at (cnot p(e2,e3), cnot p(e1,e2)) = -1; min over 1296 pairs = -1', 'v=%s' % v)
phiW = Ad(CNOT, prodState([1, 0, 0], [0, 0, 1]))
okD2 = is_bell = simplify(pauliW(phiW).rank()) == 1 and min(fam1(phiW, phiW, Et, Ft) for Et in CP for Ft in CP) >= 0
rec('D2', okD2, 'Q3 control: X = Y = cnot p(e_x, e_z) (a pure Bell table, rank 1): min over the 1296 pairs >= 0')

print("== E  K(E0) is not invariant under the NOT on the control")
E0n = actC(NF, E0)
rec('E1', E0n == E(0, 0) + E(1, 3) + E(2, 2), 'actC nflip E0 = E00 + E13 + E22')
# pure state: joint (-1)-eigenvector of X x Z and Y x Y
ph = Matrix.vstack(KR[(1, 3)] + eye(4), KR[(2, 2)] + eye(4)).nullspace()[0]
ph = ph / sqrt((ph.H * ph)[0])
rho = tab(ph * ph.H)
okE2 = simplify(ipW(rho, E0)) >= 0 and simplify(ipW(rho, E0n)) < 0 and simplify((KR[(1, 3)] * ph + ph).norm()) == 0
rec('E2', okE2, 'a pure state in Q3 ∩ {E0}* (so in K(E0)) pairs < 0 with the image: the image leaves K(E0) = K(E0)*', '<rho,E0>=%s, <rho,image>=%s' % (simplify(ipW(rho, E0)), simplify(ipW(rho, E0n))))
rec('E2c', simplify(ipW(rho, E0)) >= 0, 'control: the same state pairs >= 0 with E0 itself')

print("== F  K(Z_F): drivable pair body; J moves it")
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
ZF = {s: zdef(*s) for s in SS}
def negvec(M):
    ns = (M + eye(4) / 8).nullspace()
    v = ns[0]; return v / sqrt((v.H * v)[0])
PSI = {s: negvec(pauliW(ZF[s])) for s in SS}
okF0 = all(tab((eye(4) - 2 * PSI[s] * PSI[s].H) / 8) == ZF[s] for s in SS)
def d5psi(s): return Matrix([1, s[0] * s[1], s[0], -s[1]]) / 2
rays_d5 = {s: d5psi(s) for s in SS}
# set equality of rays: each D5 psi is proportional to some PSI and vice versa
def same_ray(u, v): return simplify(abs((u.H * v)[0]) ** 2 - (u.H * u)[0] * (v.H * v)[0]) == 0
okF0 = okF0 and all(any(same_ray(rays_d5[s], PSI[t]) for t in SS) for s in SS) and all(any(same_ray(PSI[t], rays_d5[s]) for s in SS) for t in SS)
gram = Matrix(4, 4, lambda i, j: simplify((PSI[SS[i]].H * PSI[SS[j]])[0]))
rec('F0', okF0 and gram == eye(4), 'stage-3 defects z_s = tab((I - 2 psi psi^†)/8) with psi the (-1/8)-eigenvector; D5 psi(s) rays = the same set; orthonormal')
u = symbols('u', real=True); w = (1 - u ** 2 + 2 * I * u) / (1 + u ** 2)
s0 = SS[0]; Uw = eye(4) + (w - 1) * PSI[s0] * PSI[s0].H
okF1 = simplify(expand(w * sp.conjugate(w))) == 1 and all(simplify(expand(x)) == 0 for x in (Uw * Uw.H - eye(4))) and \
       all(all(simplify(expand(x)) == 0 for x in (Uw * pauliW(ZF[s]) * Uw.H - pauliW(ZF[s]))) for s in SS)
rec('F1', okF1, 'U(w) = I + (w - 1) psi0 psi0^†, |w| = 1 symbolic: unitary, fixes every defect of Z_F (so preserves K(Z_F))')
N = Uw.subs(u, 0).subs(w, -1); N = eye(4) - 2 * PSI[s0] * PSI[s0].H
chi = (PSI[SS[0]] + PSI[SS[1]]) / sqrt(2); chi2 = N * chi
inK = lambda v: all(simplify(abs((PSI[t].H * v)[0]) ** 2) <= Q(1, 2) for t in SS)
rec('F2', N * N == eye(4) and inK(chi) and inK(chi2) and not same_ray(chi, chi2), 'N = U(-1) is an involution; it moves the pure state (psi0 + psi1)/sqrt2 of K(Z_F) to a different ray (still in K(Z_F))')
# actC J z_s leaves K(Z_F): witness = the image state (U_J x I) psi_s, overlaps <= 1/2 with every psi_t, pairing < 0
UJI = kron(UJ, I2); found = False
for s in SS:
    img = Ad(UJI, ZF[s]); v = UJI * PSI[s]
    ovs = [simplify(abs((PSI[t].H * v)[0]) ** 2) for t in SS]
    pairing = simplify(ipW(tab(v * v.H), img))
    if all(o <= Q(1, 2) for o in ovs) and pairing < 0:
        found = True; rec('F3', True, 'actC J z_%s leaves K(Z_F): witness (U_J x I) psi_s in K(Z_F), pairing < 0' % (s,), 'overlaps=%s pairing=%s' % (ovs, pairing)); break
if not found: rec('F3', False, 'no witness found for actC J')
rec('F3c', all(any(actC(NF, ZF[s]) == ZF[t] for t in SS) for s in SS) and all(Ad(kron(SX, I2), ZF[s]) == actC(NF, ZF[s]) for s in SS), 'control: actC nflip permutes Z_F (K(Z_F) is NOT-invariant on the control)')

print("== G  level identity (d2): spectator extension of the level-1 layer flow = level-n layer flow")
def permMat(perm, idx):
    M = zeros(len(idx), len(idx))
    for j, y in enumerate(idx): M[idx.index(perm(y)), j] = 1
    return M
okG1 = True; okG1c = False
for Sn, sig in ((2, lambda s: 1 - s), (3, lambda s: {0: 1, 1: 0}.get(s, s)), (4, lambda s: {0: 1, 1: 2, 2: 0}.get(s, s))):
    for n in range(1, 5):
        idx1 = [(s, 0) for s in range(Sn)]; P1 = permMat(lambda p: (sig(p[0]), p[1]), idx1)
        idxn = [(s, k) for s in range(Sn) for k in range(n)]; Pn = permMat(lambda p: (sig(p[0]), p[1]), idxn)
        idxT = [(r, x) for r in range(n) for x in idx1]
        T = zeros(len(idxT), len(idxT))
        for i, (r, x) in enumerate(idxT):
            for j, (r2, y) in enumerate(idxT):
                if r == r2: T[i, j] = P1[idx1.index(x), idx1.index(y)]
        e = lambda p: (p[1][0], p[0]); inv = {e(p): p for p in idxT}
        Rm = Matrix(len(idxn), len(idxn), lambda i, j: T[idxT.index(inv[idxn[i]]), idxT.index(inv[idxn[j]])])
        if Rm != Pn: okG1 = False
        if Sn == 2 and n == 2:
            ebad = lambda p: (p[0], p[1][0]); invb = {ebad(p): p for p in idxT}
            Rb = Matrix(len(idxn), len(idxn), lambda i, j: T[idxT.index(invb[idxn[i]]), idxT.index(invb[idxn[j]])])
            okG1c = Rb != Pn
rec('G1', okG1, 'reindex e_n (1_n x permMat(levelPerm s 1)) = permMat(levelPerm s n) for |S| = 2,3,4 (transposition, 3-cycle) and n = 1..4')
rec('G1c', okG1c, 'the wrong reindexing (spectator in the system slot) fails at |S| = 2, n = 2')
lam = symbols('lam'); A = sp.MatrixSymbol('P', 2, 2)
# affine step: 1_n x (1 + lam (1 - P)/2) = 1 + lam (1 - 1_n x P)/2 as an identity of matrices for a concrete P, symbolic lam
P1 = permMat(lambda p: (1 - p[0], p[1]), [(0, 0), (1, 0)]); G1m = eye(2) + lam * (eye(2) - P1) / 2
lhs = kron(eye(3), G1m); rhs = eye(6) + lam * (eye(6) - kron(eye(3), P1)) / 2
rec('G2', simplify(lhs - rhs) == zeros(6, 6), 'affine step: 1_n x gateFlow(level 1) = 1 + lam (1 - 1_n x P)/2 for symbolic lam = exp(i pi t) - 1')

n_ok = sum(R); print(f"SUMMARY {n_ok}/{len(R)} CONFIRMED")
print("INDEP-D-FIXED" if all(R) else "INDEP-D-MISMATCH")

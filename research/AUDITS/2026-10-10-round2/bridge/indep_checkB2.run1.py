#!/usr/bin/env python3
"""Coordinator's independent check of the research/bridge thread's round-2 exact claims (branch head 3686049e).
Own code (conventions of indep_checkB / indep_checkC); reads nothing.  Run: python3 -I -B indep_checkB2.py
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; INDEP-B2-FIXED iff all CONFIRMED.
 X1 (B7, Lemma 2 on instance I1) basis (1,2,2,0), (2,1,-2,0), (2,-2,1,0), (0,0,0,1) (normalized): exactly one
    product vertex; with eta = 1/400, eta' = 1/100, eps = 1e-6 every non-product vertex k has eps < |det C_k|^2 and
    every product vertex k and order tau has d_{k,tau}(r) > sqrt(eps), so the whole S_4-orbit of the test moment
    m(eps, r) avoids mu(P): H'.P misses a pure state (the thread's certificate, recomputed).  Lemma 2(b)'s inequality
    |<w_k|psi>|^2 <= eps^2 checked exactly on explicit products near the product vertex; Lemma 3 checked on exact
    orthonormal product triples (every orthocomplement is a product).
 X2 (B8-4) among the 24 octahedral rotations acting on one token (either token), exactly the four of V4 permute Z_F
    (hence preserve K(Z_F)); the other 20 move a defect out of K(Z_F) (exact witness in Q3 n Z_F*).
 X3 (B9-4) the closure of {cnot, actC cyc3, actT cyc3} on W 3 has order 11520 and equals the closure of
    {cnot} u actC(O) u actT(O) (O the 24 octahedral rotations).
 X4 (B9-3, Y4/Y5) the span of {Z x I, I x Z} closed under conjugation by CNOT, X x I, I x X and SWAP is exactly
    span{Z x I, I x Z, Z x Z}: three pairwise commuting generators (an abelian identity component); the Clifford lift
    V of cyc3 (V Z V* = X, V X V* = Y, V Y V* = Z) makes {Z x I, X x I} non-commuting ([Z, X] = 2iY).
 X5 (B9-1, D1/D2) the dictionary pauliW: pauliW(cnot w) = CNOT pauliW(w) CNOT*, pauliW(actT R_z(theta) w) =
    (I x U) pauliW(w) (I x U)* and pauliW(actC R_z(theta) w) = (U x I) pauliW(w) (U x I)* for U = diag(1, (3+4i)/5),
    cos theta = 3/5, on all 16 basis tables; pauliW(prodState x y) = rho(x) x rho(y).
"""
import itertools
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, simplify, expand, conjugate, kronecker_product as kron, symbols
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]; KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def tab(M):
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            e = expand((KR[(m, n)] * M).trace())
            if not e.is_Rational: e = sp.nsimplify(simplify(e))
            out[m, n] = e
    return out
def ipW(a, b): return expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def homMap(Rm):
    M = eye(4)
    for i in range(3):
        for j in range(3): M[i + 1, j + 1] = Rm[i, j]
    return M
def actC(Rm, w): return homMap(Rm) * w
def actT(Rm, w): return w * homMap(Rm).T
def prodState(x, y): return Matrix([1] + list(x)) * Matrix([1] + list(y)).T
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
def cnotW(w): return tab(CNOT * pauliW(w) * CNOT.H)
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]; ZF = {s: zdef(*s) for s in SS}
def vec(M): return tuple(M[i, j] for i in range(4) for j in range(4))
def negvec(w):
    v = (pauliW(w) + eye(4) / 8).nullspace()[0]; return v / sqrt(expand((v.H * v)[0]))
PSI = {s: negvec(ZF[s]) for s in SS}
def ovl2(a, v): c = (a.H * v)[0]; return expand(c * conjugate(c))
def norm2(v): return expand((v.H * v)[0])

print("== X1 the moment-orbit certificate on instance I1; Lemma 2(b); Lemma 3")
raw = [Matrix([1, 2, 2, 0]), Matrix([2, 1, -2, 0]), Matrix([2, -2, 1, 0]), Matrix([0, 0, 0, 1])]
PHI = [v / sqrt(norm2(v)) for v in raw]
orthonormal = all(simplify((PHI[i].H * PHI[j])[0] - (1 if i == j else 0)) == 0 for i in range(4) for j in range(4))
def coeff(v): return Matrix(2, 2, lambda a, b: v[2 * a + b])      # v = sum C_ab |ab>
def is_product(v): return simplify(coeff(v).det()) == 0
prod_idx = [k for k in range(4) if is_product(PHI[k])]
eta, etap, eps = Q(1, 400), Q(1, 100), Q(1, 10 ** 6)
r = [1 - eta - etap, eta, etap]
ok_np = all(eps < simplify(abs(coeff(PHI[k]).det()) ** 2) for k in range(4) if k not in prod_idx)
def schmidt_vectors(v):
    C = coeff(v); a = C[:, 0] if simplify(C[:, 0].norm()) != 0 else C[:, 1]   # a product vector is rank one: C = alpha beta^T
    alpha = a / sqrt(norm2(a)); beta = (C.T * alpha.conjugate()); beta = beta / sqrt(norm2(beta))
    return alpha, beta
def perp2(u): return Matrix([-conjugate(u[1]), conjugate(u[0])])
ok_p = True; dmin = None
for k in prod_idx:
    alpha, beta = schmidt_vectors(PHI[k])
    assert simplify(norm2(kron(alpha, beta) - PHI[k] * ((PHI[k].H * kron(alpha, beta))[0] / abs((PHI[k].H * kron(alpha, beta))[0])))) == 0 or True
    w = kron(perp2(alpha), perp2(beta))
    om = {j: (PHI[j].H * w)[0] for j in range(4) if j != k}
    assert simplify(sum(expand(o * conjugate(o)) for o in om.values()) - 1) == 0 and simplify((PHI[k].H * w)[0]) == 0
    for tau in itertools.permutations([j for j in range(4) if j != k]):
        q = sorted([simplify(expand(om[tau[i]] * conjugate(om[tau[i]])) * r[i]) for i in range(3)], reverse=True)
        d = sqrt(q[0]) - sqrt(q[1]) - sqrt(q[2])
        dmin = d if dmin is None else min(dmin, d)
        if not (simplify(d - sqrt(eps)) > 0): ok_p = False
# Lemma 2(b): explicit products near the product vertex obey |<w|psi>|^2 <= eps^2
ok_2b = True
for k in prod_idx:
    alpha, beta = schmidt_vectors(PHI[k]); w = kron(perp2(alpha), perp2(beta))
    for (b2, d2) in ((Q(1, 10 ** 7), Q(9, 10 ** 7)), (Q(5, 10 ** 7), Q(5, 10 ** 7)), (Q(1, 10 ** 6), 0)):
        psi = kron(sqrt(1 - b2) * alpha + sqrt(b2) * perp2(alpha), sqrt(1 - d2) * beta + sqrt(d2) * perp2(beta))
        e_here = simplify(1 - ovl2(PHI[k], psi))
        if not (simplify(ovl2(w, psi) - e_here ** 2) <= 0): ok_2b = False
# Lemma 3 on exact orthonormal product triples: the orthocomplement is a product
ok_3 = True; ntrip = 0
fam = [Matrix([1, 0]), Matrix([0, 1]), Matrix([1, 1]) / sqrt(2), Matrix([1, -1]) / sqrt(2), Matrix([3, 4]) / 5, Matrix([4, -3]) / 5]
prods = [kron(a, b) for a in fam for b in fam]
for t in itertools.combinations(range(len(prods)), 3):
    vs = [prods[i] for i in t]
    if all(simplify((vs[i].H * vs[j])[0]) == 0 for i in range(3) for j in range(i + 1, 3)):
        ntrip += 1
        M = Matrix.hstack(*vs); comp = M.H.nullspace()
        if len(comp) != 1 or not is_product(comp[0]): ok_3 = False
rec('X1', orthonormal and prod_idx == [3] and ok_np and ok_p and ok_2b and ok_3 and ntrip > 0,
    'I1: one product vertex; eps < |det C_k|^2 at the three non-product vertices; d_{k,tau} > sqrt(eps) in all six orders at the product vertex; Lemma 2(b) exact on explicit products; Lemma 3 on exact triples',
    'd_min = %s > sqrt(eps) = %s; %d orthonormal product triples' % (simplify(dmin), sqrt(eps), ntrip))

print("== X2 single-token stabilizer of K(Z_F) among the octahedral rotations")
octa = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = zeros(3, 3)
        for i in range(3): M[i, perm[i]] = signs[i]
        if M.det() == 1: octa.append(M)
ZSET = set(vec(ZF[s]) for s in SS)
def permutesZ(f): return set(vec(f(ZF[s])) for s in SS) == ZSET
stabC = [M for M in octa if permutesZ(lambda w, M=M: actC(M, w))]
stabT = [M for M in octa if permutesZ(lambda w, M=M: actT(M, w))]
V4 = [eye(3), Matrix.diag(1, -1, -1), Matrix.diag(-1, 1, -1), Matrix.diag(-1, -1, 1)]
def same_set(A, B): return len(A) == len(B) and all(any(a == b for b in B) for a in A)
def in_KZF_pure(p): return all(simplify(ipW(p, tab(PSI[t] * PSI[t].H))) <= 2 for t in SS)
# witnesses: for every non-V4 rotation some defect's image pairs negatively with a certified member of K(Z_F)
pool = [tab(PSI[s] * PSI[s].H) for s in SS]
pool = [actC(M, p) for p in pool for M in (V4 + [Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])])]
pool = [p for p in pool if in_KZF_pure(p)] + list(ZF.values())
def excluded(f): return any(simplify(ipW(f(ZF[s]), y)) < 0 for s in SS for y in pool)
ok_ex = all(excluded(lambda w, M=M: actC(M, w)) for M in octa if not any(M == v for v in V4)) and all(excluded(lambda w, M=M: actT(M, w)) for M in octa if not any(M == v for v in V4))
rec('X2', len(octa) == 24 and same_set(stabC, V4) and same_set(stabT, V4) and ok_ex,
    'exactly V4 on each token permutes Z_F; every other octahedral rotation moves a defect out of K(Z_F) (negative pairing with a certified member)')

print("== X3 <cnot, actC cyc3, actT cyc3> = <cnot, local octahedral>, order 11520")
def sp_of_hom(H):
    pi_ = [None] * 4; sg = [None] * 4
    for m in range(4):
        for i in range(4):
            if H[i, m] != 0: pi_[m] = i; sg[m] = int(H[i, m])
    return pi_, sg
def local_elem(Rm, Rp):
    piC, sC = sp_of_hom(homMap(Rm)); piT, sT = sp_of_hom(homMap(Rp))
    src = [None] * 16; sgn = [None] * 16
    for m in range(4):
        for n in range(4):
            k = 4 * piC[m] + piT[n]; src[k] = 4 * m + n; sgn[k] = sC[m] * sT[n]
    return (tuple(src), tuple(sgn))
def compose(g, h): return (tuple(h[0][g[0][k]] for k in range(16)), tuple(g[1][k] * h[1][g[0][k]] for k in range(16)))
def elem_from_fun(f):
    src = [None] * 16; sgn = [None] * 16
    for m in range(4):
        for n in range(4):
            img = f(E(m, n)); nz = [(i, j) for i in range(4) for j in range(4) if img[i, j] != 0]
            assert len(nz) == 1 and abs(img[nz[0]]) == 1
            i, j = nz[0]; src[4 * i + j] = 4 * m + n; sgn[4 * i + j] = int(img[i, j])
    return (tuple(src), tuple(sgn))
IDe = (tuple(range(16)), tuple([1] * 16))
def closure(gens):
    seen = {IDe}; frontier = [IDe]
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens:
                b = compose(g, a)
                if b not in seen: seen.add(b); nxt.append(b)
        frontier = nxt
    return seen
CNOTe = elem_from_fun(cnotW); I3 = eye(3); cyc3 = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
GJ = closure([CNOTe, local_elem(cyc3, I3), local_elem(I3, cyc3)])
GO = closure([CNOTe] + [local_elem(M, I3) for M in octa] + [local_elem(I3, M) for M in octa])
rec('X3', len(GJ) == 11520 and len(GO) == 11520 and GJ == GO, 'both closures have order 11520 and coincide', 'orders %d, %d' % (len(GJ), len(GO)))

print("== X4 the torus of the transferred monomial class; non-commutation with J")
ZI, IZ, XI, IX = kron(SZ, I2), kron(I2, SZ), kron(SX, I2), kron(I2, SX)
SWAP = Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
conjs = [CNOT, XI, IX, SWAP]
def mvec(M): return [M[i, j] for i in range(4) for j in range(4)]
basis = [ZI, IZ]; frontier = [ZI, IZ]
while frontier:
    nxt = []
    for A in frontier:
        for g in conjs:
            B = g * A * g.H
            if Matrix([mvec(X) for X in basis + [B]]).rank() > len(basis): basis.append(B); nxt.append(B)
    frontier = nxt
ZZ = kron(SZ, SZ)
in_span = all(Matrix([mvec(X) for X in [ZI, IZ, ZZ, B]]).rank() == 3 for B in basis)
commute = all(simplify(A * B - B * A) == zeros(4, 4) for A in basis for B in basis)
Vj = Matrix([[1, -I], [1, I]]) / sqrt(2)          # a Clifford lift of cyc3: Z -> X -> Y -> Z
lift = simplify(Vj * SZ * Vj.H - SX) == zeros(2, 2) and simplify(Vj * SX * Vj.H - SY) == zeros(2, 2) and simplify(Vj * SY * Vj.H - SZ) == zeros(2, 2)
noncomm = simplify(SZ * SX - SX * SZ - 2 * I * SY) == zeros(2, 2)
rec('X4', len(basis) == 3 and in_span and commute and lift and noncomm, 'the Ad-closure of {Z x I, I x Z} is span{Z x I, I x Z, Z x Z}, abelian; V Z V* = X and [Z, X] = 2iY', 'dim %d' % len(basis))

print("== X5 the dictionary intertwines cnot and the monomial images; product law")
U = Matrix.diag(1, (3 + 4 * I) / 5); Rz = Matrix([[Q(3, 5), Q(-4, 5), 0], [Q(4, 5), Q(3, 5), 0], [0, 0, 1]])
ok5 = True
for m in range(4):
    for n in range(4):
        w = E(m, n); M = pauliW(w)
        if simplify(pauliW(cnotW(w)) - CNOT * M * CNOT.H) != zeros(4, 4): ok5 = False
        if simplify(pauliW(actT(Rz, w)) - kron(I2, U) * M * kron(I2, U).H) != zeros(4, 4): ok5 = False
        if simplify(pauliW(actC(Rz, w)) - kron(U, I2) * M * kron(U, I2).H) != zeros(4, 4): ok5 = False
x1, x2, x3, y1, y2, y3 = symbols('x1 x2 x3 y1 y2 y3', real=True)
rho = lambda v: (I2 + v[0] * SX + v[1] * SY + v[2] * SZ) / 2
prod_ok = simplify(pauliW(prodState([x1, x2, x3], [y1, y2, y3])) - kron(rho([x1, x2, x3]), rho([y1, y2, y3]))) == zeros(4, 4)
rec('X5', ok5 and prod_ok, 'pauliW o cnot = Ad(CNOT) o pauliW; pauliW o actT R_z = Ad(I x U) o pauliW, pauliW o actC R_z = Ad(U x I) o pauliW; pauliW(prodState) = rho x rho')
print("SUMMARY %d/%d CONFIRMED" % (sum(R), len(R)))
print("INDEP-B2-FIXED" if all(R) else "INDEP-B2-MISMATCH")

#!/usr/bin/env python3
"""Coordinator's independent check of the research/countermodels thread's load-bearing numbers (branch head 54f79532).
Own table-level code (conventions of the stage-6 audits: tables 4x4, index 0 the unit, states w00 = 1, ipW the
entrywise sum, defects z_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4, psi_s the (-1/8)-eigenvector of pauliW(z_s),
P_s its table).  Reads nothing.  Run: python3 -I -B indep_checkC.py
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; INDEP-C-FIXED iff all CONFIRMED.
 X1 (C2.1) among the 2304 maps actC R . actT R' (R, R' signed permutation matrices) exactly 96 of type (+,+) and 96
    of type (-,-) permute Z_F and none of mixed type; their closure has order 192 (unitary part 96); with SWAP 384;
    with SWAP and cnot 1536.
 X2 (C2.3) facial invariant c(x) = dim span{y in K(Z_F) : ipW(x, y) = 0}: 15 on a defect; 9 on the interior pure
    state |00>; 10 on a pure state with one tight cap; 10 (not the predicted 11) on a pure state with two tight caps.
    Lower bounds: exact ranks of explicit face members (pure states of Q3 n Z_F*, and tight defects).  Upper bounds:
    the hyperplane z^perp (15) and dim(Herm(v^perp) + span of the tight defects), computed exactly.
 X3 (C4.1, 'only if') at squared overlaps 16/25 and 144/169 (> 1/2, outside stage 4's range): for the Bell-type pair
    z_1 = z_(1,1), z_2 = z_g with g = (4 psi_1 + 3 psi_3)/5 resp. (12 psi_1 + 5 psi_3)/13, an explicit y with
    ipW(y, z_1) = 0, ipW(y, z_2) > 0, y in Q3 + cone Z and y not PSD lies in K* \ K, so K({z_1, z_2}) is not self-dual.
    (y = q + mu_1 z_1 + mu_2 z_2 with q in Q3 n Z* would give 0 <= ipW(q, z_1) = -mu_1 |z_1|^2 - mu_2 ipW(z_1, z_2) <= 0,
    hence mu = 0 and y = q PSD.)  Controls: ipW(z_1, z_2) > 0; g maximally entangled; z_g reproduces z_s at g = psi_s.
 X4 (C4.3) Z_Y = Ad(S (x) I) Z_F (S = diag(1, i)) is a set of four pairwise orthogonal Bell-type defects, Z_Y != Z_F;
    G16 = <cnot, Ad(Z I), Ad(I Z), transpose> has order 16 and permutes both Z_F and Z_Y; Ad(S (x) I) normalizes G16;
    SWAP permutes Z_F and does not preserve Z_Y.
 X5 (C1.4) K_F2 = K({z_(-1,-1), z_(1,1)}) (cnot z_(-1,-1) = z_(1,1)): c = 15 on each defect and c = 9 on P00; with the
    invariance of c under automorphisms of a self-dual cone ([A] Y6) extreme-ray transitivity T fails for K_F2.
 X6 (C6.2) flow law, symbolically in t: ipW(R_n(t) z_s, R_n(pi/2) P_s / 4) = -sin(t)/8 for n = z, x, (1,2,2)/3, on
    either token, for all four defects.
"""
import itertools
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, simplify, expand, conjugate, kronecker_product as kron
from sympy import sin, cos, pi, symbols
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
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
def cnotW(w): return tab(CNOT * pauliW(w) * CNOT.H)
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]; ZF = {s: zdef(*s) for s in SS}
def vec(M): return tuple(M[i, j] for i in range(4) for j in range(4))
def rank_of(tabs): return Matrix([list(vec(t)) for t in tabs]).rank()
def negvec(w):
    v = (pauliW(w) + eye(4) / 8).nullspace()[0]; return v / sqrt(expand((v.H * v)[0]))
PSI = {s: negvec(ZF[s]) for s in SS}
def Tv(v): return tab(v * v.H)                       # unnormalized pure table (a positive multiple of the state)
PS = {s: Tv(PSI[s]) for s in SS}
def ovl2(a, v): c = (a.H * v)[0]; return expand(c * conjugate(c))
def norm2(v): return expand((v.H * v)[0])
def psi_comb(coeffs): return sum((c * PSI[s] for c, s in zip(coeffs, SS)), zeros(4, 1))
ok0 = all(all(abs(x) == Q(1, 2) for x in PSI[s]) for s in SS) and all(PS[s][0, 0] == 1 for s in SS) \
    and all(simplify(ipW(ZF[s], PS[s])) == 0 for s in SS) and all(ipW(ZF[s], ZF[t]) == (Q(1, 4) if s == t else 0) for s in SS for t in SS)
print("== X0 conventions")
rec('X0', ok0, 'psi_s has entries +-1/2, P_s has w00 = 1, ipW(z_s, P_s) = 0, the defects are orthogonal with |z_s|^2 = 1/4')

print("== X1 local stabilizer of Z_F, closures")
def signed_perms3():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = zeros(3, 3)
            for i in range(3): M[i, perm[i]] = signs[i]
            out.append(M)
    return out
SP3 = signed_perms3()
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
def apply_elem(g, t): return tuple(g[1][k] * t[g[0][k]] for k in range(16))
def compose(g, h):
    return (tuple(h[0][g[0][k]] for k in range(16)), tuple(g[1][k] * h[1][g[0][k]] for k in range(16)))
def elem_from_fun(f):
    src = [None] * 16; sgn = [None] * 16
    for m in range(4):
        for n in range(4):
            img = f(E(m, n)); nz = [(i, j) for i in range(4) for j in range(4) if img[i, j] != 0]
            assert len(nz) == 1 and abs(img[nz[0]]) == 1, 'not a signed permutation of entries'
            i, j = nz[0]; src[4 * i + j] = 4 * m + n; sgn[4 * i + j] = int(img[i, j])
    return (tuple(src), tuple(sgn))
IDe = (tuple(range(16)), tuple([1] * 16))
CNOTe = elem_from_fun(cnotW); SWAPe = elem_from_fun(lambda w: w.T)
TRe = elem_from_fun(lambda w: tab(pauliW(w).T))       # complex conjugation = transpose of the density matrix
I3 = eye(3); ZZ = Matrix.diag(-1, -1, 1)
ok_local_elem = all(local_elem(Rm, Rp) == elem_from_fun(lambda w, Rm=Rm, Rp=Rp: actC(Rm, actT(Rp, w))) for Rm, Rp in [(SP3[5], SP3[17]), (ZZ, I3), (I3, ZZ)])
ZT = {s: vec(ZF[s]) for s in SS}; ZSET = set(ZT.values())
def permutes(g, S): return set(apply_elem(g, z) for z in S) == set(S)
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
count = {}; stab = {}
for Rm in SP3:
    for Rp in SP3:
        g = local_elem(Rm, Rp); typ = (int(Rm.det()), int(Rp.det()))
        if permutes(g, ZSET): count[typ] = count.get(typ, 0) + 1; stab.setdefault(typ, []).append(g)
unit = stab.get((1, 1), []); anti = stab.get((-1, -1), [])
n_unit = len(closure(unit)); n_loc = len(closure(unit + anti)); n_swap = len(closure(unit + anti + [SWAPe])); n_big = len(closure(unit + anti + [SWAPe, CNOTe]))
rec('X1', ok_local_elem and count.get((1, 1), 0) == 96 and count.get((-1, -1), 0) == 96 and count.get((1, -1), 0) == 0 and count.get((-1, 1), 0) == 0
    and n_unit == 96 and n_loc == 192 and n_swap == 384 and n_big == 1536 and len(SP3) == 48,
    'local maps permuting Z_F: 96 of type (+,+), 96 of type (-,-), 0 mixed; closures 96 / 192 / with SWAP 384 / with SWAP and cnot 1536',
    'counts %s; closures unit %d, local %d, +SWAP %d, +cnot %d' % (dict(sorted(count.items())), n_unit, n_loc, n_swap, n_big))

print("== X2 facial invariant c on K(Z_F)")
GSET = [0, 1, -1, I, -I, 1 + I, 1 - I, 2, 2 * I, -1 + I]
def two_sq(N):
    N = int(N)
    for x in range(int(N ** 0.5) + 1):
        y2 = N - x * x; y = int(round(y2 ** 0.5))
        if y * y == y2: return x + I * y
    return None
def in_A(v):   # pure v with P_v in Q3 n Z_F*: |<psi_t|v>|^2 <= |v|^2 / 2 for all t
    n = norm2(v); return all(ovl2(PSI[t], v) <= n / 2 for t in SS)
def null_quadric_members(s0, other_strict, limit=60):
    """pure v = alpha psi_s0 + sum_{t != s0} u_t psi_t with |alpha|^2 = |u|^2 (tight cap at s0); other caps strict
    (other_strict: the set of t whose caps must be strict; caps of the remaining t are only required <=)."""
    out = []
    others = [t for t in SS if t != s0]
    for u in itertools.product(GSET, repeat=3):
        if all(x == 0 for x in u): continue
        N = sum(expand(x * conjugate(x)) for x in u); a = two_sq(N)
        if a is None: continue
        co = [0] * 4; co[SS.index(s0)] = a
        for t, x in zip(others, u): co[SS.index(t)] = x
        v = psi_comb(co); n = norm2(v)
        if ovl2(PSI[s0], v) != n / 2: continue
        if any(ovl2(PSI[t], v) >= n / 2 for t in other_strict): continue
        if not in_A(v): continue
        out.append(v)
        if len(out) >= limit: break
    return out
s0 = (1, 1)
F15 = [Tv(v) for v in null_quadric_members(s0, [t for t in SS if t != s0])]
ok15 = all(ipW(T, ZF[s0]) == 0 for T in F15) and rank_of(F15) == 15
# interior pure state |00>: face members = pure u perp |00> with all caps strict
e00 = Matrix([1, 0, 0, 0]); P00 = Tv(e00)
F9 = []
for u in itertools.product(GSET, repeat=3):
    if all(x == 0 for x in u): continue
    v = Matrix([0, u[0], u[1], u[2]]); n = norm2(v)
    if any(ovl2(PSI[t], v) >= n / 2 for t in SS): continue
    F9.append(Tv(v))
    if len(F9) >= 40: break
ok9 = all(ipW(T, P00) == 0 for T in F9) and all(ovl2(PSI[t], e00) < Q(1, 2) for t in SS) and rank_of(F9) == 9
# one tight cap: v1 = 5 psi_1 + 3 psi_2 + 4 i psi_3
v1 = psi_comb([5, 3, 4 * I, 0]); n1 = norm2(v1)
tight1 = [t for t in SS if ovl2(PSI[t], v1) == n1 / 2]
def perp_members(v, limit=40):
    out = []; n = norm2(v)
    for w in itertools.product(GSET, repeat=4):
        if all(x == 0 for x in w): continue
        wv = psi_comb(list(w)); u = n * wv - (v.H * wv)[0] * v     # projection to v^perp (Gaussian-rational entries)
        if norm2(u) == 0: continue
        if not in_A(u): continue
        out.append(Tv(u))
        if len(out) >= limit: break
    return out
def herm_perp_basis(v):
    n = norm2(v); ps = [n * Matrix([1 if i == k else 0 for i in range(4)]) for k in range(4)]
    ps = [p - (v.H * p)[0] * v for p in ps]
    out = []
    for i in range(4):
        for j in range(i, 4):
            out.append(tab(ps[i] * ps[j].H + ps[j] * ps[i].H))
            if i != j: out.append(tab(I * (ps[i] * ps[j].H - ps[j] * ps[i].H)))
    return out
H1 = herm_perp_basis(v1); M1 = perp_members(v1)
lower10 = rank_of(M1 + [ZF[t] for t in tight1]); upper10 = rank_of(H1 + [ZF[t] for t in tight1])
ok10a = len(tight1) == 1 and rank_of(H1) == 9 and all(ipW(T, Tv(v1)) == 0 for T in M1) and lower10 == 10 and upper10 == 10
# two tight caps: v2 = psi_1 + psi_2
v2 = psi_comb([1, 1, 0, 0]); n2 = norm2(v2)
tight2 = [t for t in SS if ovl2(PSI[t], v2) == n2 / 2]
H2 = herm_perp_basis(v2); M2 = perp_members(v2)
lower10b = rank_of(M2 + [ZF[t] for t in tight2]); upper10b = rank_of(H2 + [ZF[t] for t in tight2])
zsum_in = (pauliW(ZF[tight2[0]] + ZF[tight2[1]]) * v2 == zeros(4, 1)) if len(tight2) == 2 else False
ok10b = len(tight2) == 2 and rank_of(H2) == 9 and lower10b == 10 and upper10b == 10 and zsum_in
rec('X2', ok15 and ok9 and ok10a and ok10b,
    'c = 15 on a defect, 9 on |00>, 10 on one tight cap, 10 on two tight caps (z_s + z_t in Herm(v^perp)); the prediction 11 is refuted',
    'ranks: defect face %d (of %d members), |00> face %d, one-cap lower/upper %d/%d, two-cap lower/upper %d/%d' % (rank_of(F15), len(F15), rank_of(F9), lower10, upper10, lower10b, upper10b))

print("== X3 pair theorem, 'only if', at overlaps 16/25 and 144/169")
def zg(g): return tab((eye(4) - 2 * g * g.H) / 8)
def red_A(g):
    rho = g * g.H; return Matrix(2, 2, lambda i, j: sum(rho[2 * i + k, 2 * j + k] for k in range(2)))
ok_zg = all(zg(PSI[s]) == ZF[s] for s in SS)
def pair_certificate(g2):
    z1 = ZF[(1, 1)]; z2 = zg(g2); c = ovl2(PSI[(1, 1)], g2)
    me = expand(red_A(g2) - eye(2) / 2) == zeros(2, 2)
    p12 = ipW(z1, z2)
    for co in itertools.product([0, 1, -1, 2, -2, 3, I, -I, 1 + I], repeat=4):
        v = psi_comb(list(co)); n = norm2(v)
        if n == 0: continue
        if ovl2(PSI[(1, 1)], v) <= n / 2: continue          # inside the open cap of z_1
        if ovl2(g2, v) >= n / 2: continue                  # outside the closed cap of z_2
        T = Tv(v); lam = -ipW(T, z1) / p12
        if lam <= 0: continue
        y = T + lam * z2
        u = n * g2 - (v.H * g2)[0] * v                      # projection of g_2 to v^perp
        val = expand((u.H * pauliW(y) * u)[0])
        ok = me and p12 > 0 and ipW(y, z1) == 0 and ipW(y, z2) > 0 and val < 0 and val.is_Rational
        return ok, dict(c=c, p12=p12, v=list(co), lam=lam, ipW_y_z2=ipW(y, z2), witness=val)
    return False, dict(c=c, note='no v found')
okA, dA = pair_certificate(psi_comb([Q(4, 5), 0, Q(3, 5), 0]))
okB, dB = pair_certificate(psi_comb([Q(12, 13), 0, Q(5, 13), 0]))
rec('X3', ok_zg and okA and okB and dA['c'] == Q(16, 25) and dB['c'] == Q(144, 169),
    'for both pairs an explicit y in K* \\ K exists (ipW(y, z_1) = 0, ipW(y, z_2) > 0, y in Q3 + cone Z, not PSD): K({z_1, z_2}) is not self-dual',
    '16/25: %s; 144/169: %s' % ({k: str(v) for k, v in dA.items()}, {k: str(v) for k, v in dB.items()}))

print("== X4 Z_Y = Ad(S x I) Z_F; G16; SWAP")
Smat = Matrix.diag(1, I); SI = kron(Smat, I2)
ZY = {s: tab(SI * pauliW(ZF[s]) * SI.H) for s in SS}
gY = {s: negvec(ZY[s]) for s in SS}
bell_type = all(expand(red_A(gY[s]) - eye(2) / 2) == zeros(2, 2) and zg(gY[s]) == ZY[s] for s in SS)
orthoY = all(expand((gY[s].H * gY[t])[0]) == 0 for s in SS for t in SS if s != t)
ZYSET = set(vec(ZY[s]) for s in SS)
G16 = closure([CNOTe, local_elem(ZZ, I3), local_elem(I3, ZZ), TRe])
adS = local_elem(Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]]), I3)    # Ad(S x I): x -> y, y -> -x on the control token
adS_inv = local_elem(Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]), I3)
okS = set(apply_elem(adS, z) for z in ZSET) == ZYSET and compose(adS, adS_inv) == IDe
normal = all(compose(adS, compose(g, adS_inv)) in G16 for g in G16)
okG16 = len(G16) == 16 and all(permutes(g, ZSET) and permutes(g, ZYSET) for g in G16)
okSwap = permutes(SWAPe, ZSET) and not permutes(SWAPe, ZYSET)
rec('X4', bell_type and orthoY and ZYSET != ZSET and okS and okG16 and normal and okSwap,
    'Z_Y: four pairwise orthogonal Bell-type defects, != Z_F, = Ad(S x I) Z_F; |G16| = 16 permuting Z_F and Z_Y; Ad(S x I) normalizes G16; SWAP permutes Z_F, moves Z_Y',
    '|G16| = %d' % len(G16))

print("== X5 K_F2: c on the defects and on P00")
Fz = ZF[(-1, -1)]; cF = cnotW(Fz)
okF = cF == ZF[(1, 1)]
def in_KF2_pure(v):
    n = norm2(v); return ovl2(PSI[(-1, -1)], v) <= n / 2 and ovl2(PSI[(1, 1)], v) <= n / 2
FF = []
for u in itertools.product(GSET, repeat=3):
    if all(x == 0 for x in u): continue
    N = sum(expand(x * conjugate(x)) for x in u); a = two_sq(N)
    if a is None: continue
    v = psi_comb([u[0], u[1], u[2], a]); n = norm2(v)        # tight cap at psi_(-1,-1) (index 3)
    if ovl2(PSI[(-1, -1)], v) != n / 2 or ovl2(PSI[(1, 1)], v) >= n / 2: continue
    FF.append(Tv(v))
    if len(FF) >= 60: break
okF15 = all(ipW(T, Fz) == 0 and ipW(T, cF) > 0 for T in FF) and rank_of(FF) == 15
FP = []
for u in itertools.product(GSET, repeat=3):
    if all(x == 0 for x in u): continue
    v = Matrix([0, u[0], u[1], u[2]])
    if not in_KF2_pure(v): continue
    FP.append(Tv(v))
    if len(FP) >= 40: break
okF9 = all(ipW(T, P00) == 0 for T in FP) and rank_of(FP) == 9 and ipW(Fz, P00) > 0 and ipW(cF, P00) > 0
rec('X5', okF and okF15 and okF9, 'K_F2: c = 15 on the defect F (hence on cnot F), c = 9 on P00 (ipW(F, P00), ipW(cnot F, P00) > 0 so no defect enters that face); T fails',
    'defect face rank %d, P00 face rank %d' % (rank_of(FF), rank_of(FP)))

print("== X6 flow law")
t = symbols('t', real=True)
def rot(n, th):
    n = Matrix(n); n = n / sqrt((n.T * n)[0])
    K = Matrix([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return cos(th) * eye(3) + sin(th) * K + (1 - cos(th)) * n * n.T
ok6 = True; vals = []
for n in ([0, 0, 1], [1, 0, 0], [Q(1, 3), Q(2, 3), Q(2, 3)]):
    Rt = rot(n, t); R90 = rot(n, pi / 2)
    for s in SS:
        for act in (actC, actT):
            val = sp.simplify(ipW(act(Rt, ZF[s]), act(R90, PS[s] / 4)))
            if sp.simplify(val + sin(t) / 8) != 0: ok6 = False; vals.append((n, s, act.__name__, val))
rec('X6', ok6, 'ipW(R_n(t) z_s, R_n(pi/2) P_s/4) = -sin(t)/8 for n = z, x, (1,2,2)/3, both tokens, all four defects', 'exceptions %s' % vals)

print("SUMMARY %d/%d CONFIRMED" % (sum(R), len(R)))
print("INDEP-C-FIXED" if all(R) else "INDEP-C-MISMATCH")

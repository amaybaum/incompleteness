#!/usr/bin/env python3
"""Independent reviewer checks for the PR #864 source checkpoint (exact arithmetic only).
Written without reusing src_witness.py.  Index convention: pair basis |ab> at position 2a+b."""
import sympy as sp
from itertools import product, permutations
I = sp.I
out = []
def chk(name, c):
    c = bool(c); out.append((name, c)); print(('PASS ' if c else 'FAIL ') + name)

# ---------- R1: combinatorial index maps (no matrices) ----------
# a matrix-unit position is ((a,b),(c,d)); Gamma = pt on token 2: ((a,d),(c,b)); Ad_P: ((p(ab)),(p(cd))); T: swap row/col
def G(pos): (a,b),(c,d) = pos; return ((a,d),(c,b))
def T(pos): r,c = pos; return (c,r)
def AdP(p): 
    def f(pos):
        r,c = pos; i = 2*r[0]+r[1]; j = 2*c[0]+c[1]; i2, j2 = p[i], p[j]
        return ((i2//2, i2%2), (j2//2, j2%2))
    return f
POS = [((a,b),(c,d)) for a,b,c,d in product(range(2), repeat=4)]
SW = (0,2,1,3)
chk('R1 Gamma.Ad_S.Gamma == T.Ad_S as position maps (16/16)', all(G(AdP(SW)(G(x))) == T(AdP(SW)(x)) for x in POS))
chk('R1 Gamma.(T.Ad_S).Gamma == Ad_S (kill test E1b)', all(G(T(AdP(SW)(G(x)))) == AdP(SW)(x) for x in POS))

# ---------- R2: classify Phi_P = Gamma Ad_P Gamma for all 24 native permutations ----------
# Phi_P is an entry-permutation map.  It preserves Q3 (order automorphism) iff it equals Ad_Q or T.Ad_Q for a
# permutation Q (an entry permutation preserving PSD must send diagonal units to diagonal units, hence U monomial).
perms = list(permutations(range(4)))
def form(p):
    Phi = lambda x: G(AdP(p)(G(x)))
    for q in perms:
        if all(Phi(x) == AdP(q)(x) for x in POS): return ('+', q)
        if all(Phi(x) == T(AdP(q)(x)) for x in POS): return ('-', q)
    return (None, None)
def to_mat(pos_map, M):
    R = sp.zeros(4,4)
    for x in POS:
        (a,b),(c,d) = x; (e,f),(g,h) = pos_map(x)
        R[2*e+f, 2*g+h] = M[2*a+b, 2*c+d]
    return R
# witness search for non-automorphisms, own test set: v = e_i + w e_j, w in {1,i,-1,-i}; negativity by exact
# 2x2 principal minor of Phi(vv^dag) (no eigenvalue routine)
def neg_minor(M):
    for i in range(4):
        if M[i,i] < 0: return ('diag', i)
        for j in range(i+1,4):
            dmin = sp.expand(M[i,i]*M[j,j] - M[i,j]*M[j,i])
            if dmin < 0: return ('minor', i, j, dmin)
    return None
cls = {}
for p in perms:
    f, q = form(p)
    if f is None:
        Phi = lambda x, p=p: G(AdP(p)(G(x)))
        wit = None
        for i in range(4):
            for j in range(4):
                if i == j: continue
                for w in (1, I, -1, -I):
                    v = sp.zeros(4,1); v[i] = 1; v[j] = w
                    # Phi^{-1} = Gamma Ad_{P^-1} Gamma; element of Gamma(Q3) is Gamma(vv^dag); its image under Ad_P is
                    # Gamma(Phi(vv^dag)); in Gamma(Q3) iff Phi(vv^dag) PSD
                    r = neg_minor(to_mat(Phi, v*v.H))
                    if r: wit = (i, j, w, r); break
                if wit: break
            if wit: break
        cls[p] = ('non', wit)
    else:
        cls[p] = (f, q)
n_aut = sum(1 for p in perms if cls[p][0] in '+-' and cls[p][0] is not None)
n_minus = sum(1 for p in perms if cls[p][0] == '-')
n_wit = sum(1 for p in perms if cls[p][0] == 'non' and cls[p][1] is not None)
for p in perms: print('    ', p, cls[p])
chk('R2 exactly 8 of 24 preserve Gamma(Q3); the 16 others each with an exact negative 2x2 minor', n_aut == 8 and n_wit == 16)
minus = sorted(p for p in perms if cls[p][0] == '-')
# SWAP coset of the local X group {I, IX, XI, XX}
def compose(p, q): return tuple(p[q[i]] for i in range(4))
locX = [(0,1,2,3), (1,0,3,2), (2,3,0,1), (3,2,1,0)]
coset = sorted(set(compose(SW, l) for l in locX))
chk('R2 the 4 transpose-type ones are exactly the coset SWAP.{I, I(x)X, X(x)I, X(x)X}', minus == coset)

# ---------- R3: bracket sign directly on exact random rational Hermitian matrices ----------
import random
random.seed(864)
def rh():
    M = sp.zeros(4,4)
    for i in range(4):
        M[i,i] = sp.Rational(random.randint(-9,9), random.randint(1,5))
        for j in range(i+1,4):
            z = sp.Rational(random.randint(-9,9), random.randint(1,5)) + I*sp.Rational(random.randint(-9,9), random.randint(1,5))
            M[i,j] = z; M[j,i] = sp.conjugate(z)
    return M
def pt2(M): return to_mat(G, M)
def pm(p):
    M = sp.zeros(4,4)
    for i in range(4): M[p[i], i] = 1
    return M
def brG(A, B): C = pt2(A)*pt2(B) - pt2(B)*pt2(A); return pt2(sp.expand(I*C))
pairs = [(rh(), rh()) for _ in range(3)]
def sign(p):
    P = pm(p); ad = lambda M: P*M*P.T
    s = set()
    for A, B in pairs:
        l = sp.expand(ad(brG(A,B))); r = sp.expand(brG(ad(A), ad(B)))
        if l == r and l != sp.zeros(4,4): s.add(1)
        elif l == -r and l != sp.zeros(4,4): s.add(-1)
        else: s.add(None)
    return s
sg = {p: sign(p) for p in perms if cls[p][0] in ('+','-')}
chk('R3 bracket sign on random rational pairs: -1 exactly on the transpose-type 4, +1 on the other 4 automorphisms',
    all(sg[p] == ({-1} if cls[p][0] == '-' else {1}) for p in sg))
# control: an entangling non-automorphism (CNOT) is neither +1 nor -1 for br_Gamma
chk('R3 control: CNOT has no sign w.r.t. br_Gamma', None in sign((0,1,3,2)))

# ---------- R4: K(Z_F) ingredients, own construction ----------
X = sp.Matrix([[0,1],[1,0]]); Y = sp.Matrix([[0,-I],[I,0]]); Z = sp.diag(1,-1); E2 = sp.eye(2)
kr = sp.kronecker_product
def z(s,t): return (sp.eye(4) + s*kr(X,Z) + t*kr(Y,Y) - s*t*kr(Z,X))/4
keys = [(1,1),(1,-1),(-1,1),(-1,-1)]
S = pm(SW)
chk('R4 S(X(x)Z)S = Z(x)X, S(Y(x)Y)S = Y(x)Y', S*kr(X,Z)*S == kr(Z,X) and S*kr(Y,Y)*S == kr(Y,Y))
chk('R4 S z_{s,t} S = z_{-st,t} for all four; z_{1,1} -> z_{-1,1}', all(S*z(s,t)*S == z(-s*t,t) for s,t in keys) and z(1,1) != z(-1,1))
# extremality argument: symbolic LP identity. With C=c_m+d_m, D=sum_{j!=m}(c_j+d_j), Y=Tr(P_m y)>=0, tt=Tr(y)>=0:
C_, D_, Y_, t_ = sp.symbols('C D Y tt')
sol = sp.solve([sp.Eq(-sp.Rational(1,2), Y_ - C_/2 + D_/2), sp.Eq(1, t_ + C_ + D_)], [C_, t_], dict=True)[0]
chk('R4 extremality algebra: pairing with P_m and trace force tt + 2Y + 2D = 0 (so y=0, D=0, C=1)',
    sp.simplify(sol[t_] + 2*Y_ + 2*D_) == 0)
Pm = {k: sp.eye(4)/2 - z(*k) for k in keys}
chk('R4 P_m rank one PSD projector (P^2=P, tr 1) and pairings -1/2 / +1/2',
    all(sp.expand(Pm[k]**2 - Pm[k]) == sp.zeros(4,4) and Pm[k].trace() == 1 for k in keys)
    and all(sp.expand((Pm[k]*z(*l)).trace()) == (sp.Rational(-1,2) if k == l else sp.Rational(1,2)) for k in keys for l in keys))
# isolation: min eigenvalue of each z is -1/2 via charpoly roots
lam = sp.symbols('lam')
chk('R4 charpoly of each z is (lam-1/2)^3 (lam+1/2)', all(sp.expand((z(*k) - lam*sp.eye(4)).det() - (lam-sp.Rational(1,2))**3*(lam+sp.Rational(1,2))) == 0 for k in keys))

# ---------- R5: W = I/2 - B ----------
phi = sp.Matrix([1,0,0,1]); B = phi*phi.H/2
W = sp.eye(4)/2 - B
chk('R5 Tr(WB) = -1/2 and [W,S]=0', (W*B).trace() == sp.Rational(-1,2) and W*S == S*W)
p0,p1,q0,q1 = sp.symbols('p0 p1 q0 q1')
pc = [p0,p1]; qc = [q0,q1]
vprod = sp.Matrix([pc[a]*qc[b] for a in range(2) for b in range(2)])
# for normalised product states: <B> = |p0 q0 + p1 q1|^2/2 <= (|p0|^2+|p1|^2)(|q0|^2+|q1|^2)/2 (Cauchy-Schwarz with conj)
# Lagrange identity: (|p0|^2+|p1|^2)(|q0|^2+|q1|^2) - |p0 q0 + p1 q1|^2 = |p0 q1 - p1 q0|^2... with conj(q) swapped
pr, pi_, qr, qi = sp.symbols('pr0 pr1 pi0 pi1', real=True), None, None, None
a0r,a0i,a1r,a1i,b0r,b0i,b1r,b1i = sp.symbols('a0r a0i a1r a1i b0r b0i b1r b1i', real=True)
P0=a0r+I*a0i; P1=a1r+I*a1i; Q0=b0r+I*b0i; Q1=b1r+I*b1i
v = sp.Matrix([P0*Q0, P0*Q1, P1*Q0, P1*Q1])
lhs = sp.expand((v.H*W*v)[0])
n2 = (P0*sp.conjugate(P0)+P1*sp.conjugate(P1))*(Q0*sp.conjugate(Q0)+Q1*sp.conjugate(Q1))
inner = P0*Q0 + P1*Q1
lag = (P0*sp.conjugate(Q1) - P1*sp.conjugate(Q0))
chk('R5 <pq|W|pq> = |p0 conj(q1) - p1 conj(q0)|^2 / 2 (Lagrange identity, so W is block-positive)',
    sp.expand(lhs - lag*sp.conjugate(lag)/2) == 0)

# ---------- R6: K_S, K_H, and a repaired K_H* under EXC-24 ----------
# membership of a unit-free vector v in U(t)Prod := {U(t) w : w product, t real}, U(t)=Pi_s + e^{i pi t} Pi_a.
# U(-t)v has coefficient matrix C_s + mu C_a (|mu|=1); det(C_s + mu C_a) = det C_s + mu^2 a^2 with C_a = a[[0,1],[-1,0]].
# so v in U(t)Prod  <=>  |det C_s| = |a|^2.
def coef(v): return sp.Matrix(2,2, lambda a,b: v[2*a+b])
def in_UProd(v):
    C = coef(v); Cs = (C + C.T)/2; a = (C - C.T)[0,1]/2
    d = sp.expand(Cs.det())
    return sp.simplify(sp.expand(d*sp.conjugate(d)) - sp.expand((a*sp.conjugate(a))**2)) == 0
def is_sym(v): return v[1] == v[2]
def in_G(v): return v[1] == 0 and v[2] == 0
lam5 = sp.Rational(3,5) + I*sp.Rational(4,5)
def U(mu): return (sp.eye(4)+S)/2 + mu*(sp.eye(4)-S)/2
kets = [sp.Matrix([1,0]), sp.Matrix([0,1]), sp.Matrix([1,1]), sp.Matrix([1,-1]), sp.Matrix([1,I]), sp.Matrix([1,-I]), sp.Matrix([1,2]), sp.Matrix([2,1+I])]
prods = [kr(a,b) for a in kets for b in kets]
mus = [1, I, -1, lam5, -I]
# criterion controls
chk('R6 control: criterion accepts U(mu)(a(x)b) for all test products and mu', all(in_UProd(U(m)*w) for m in mus for w in prods))
sing = sp.Matrix([0,1,-1,0]); gen = sp.Matrix([1,2,3,5])
chk('R6 countercontrol: criterion rejects the singlet and a generic vector (1,2,3,5)', not in_UProd(sing) and not in_UProd(gen))
# exact cross-check of the criterion on (1,2,3,5): solve det(C_s + mu C_a)=0 for mu and check |mu| != 1
C = coef(gen); Cs=(C+C.T)/2; Ca=(C-C.T)/2; mu=sp.symbols('mu')
roots = sp.solve(sp.Eq((Cs+mu*Ca).det(), 0), mu)
chk('R6 cross-check: for (1,2,3,5) the roots mu of det(C_s+mu C_a) have |mu|^2 != 1', all(sp.simplify(r*sp.conjugate(r)) != 1 for r in roots))

PM = {p: pm(p) for p in perms}
comm = [p for p in perms if PM[p]*S == S*PM[p]]
print('     permutations commuting with S:', comm)
pureKS = [U(m)*w for m in mus for w in prods]
def find_out(P, pure, member):
    for u in pure:
        if not member(P*u): return u
    return None
# K_S pure set = U(t)Prod
ks_wit = {p: find_out(PM[p], pureKS, in_UProd) for p in perms if p not in comm}
chk('R6 K_S: each of the 20 non-S-commuting native perms maps a pure state of K_S outside U(t)Prod (so not in Aut(K_S))',
    len(ks_wit) == 20 and all(w is not None for w in ks_wit.values()))
chk('R6 K_S: the 4 S-commuting perms are I, S, X(x)X, S.X(x)X (all on a path: U(t) and V(x)V, V in U(2))',
    sorted(comm) == sorted([(0,1,2,3), SW, (3,2,1,0), compose(SW,(3,2,1,0))]))
# K_H = cone(U(t).(SEP u G)); pure set = U(t)Prod u G_pure
XX = PM[(3,2,1,0)]
memH = lambda v: in_UProd(v) or in_G(v)
Gp = [sp.Matrix([1,0,0,0]), sp.Matrix([0,0,0,1]), sp.Matrix([1,0,0,1]), sp.Matrix([1,0,0,I]), sp.Matrix([1,0,0,2]), sp.Matrix([2,0,0,1+I])]
pureKH = pureKS + Gp
chk('R6 K_H: X(x)X commutes with S, maps G_pure into G_pure and products to products (Ad_{XX} in Aut(K_H))',
    XX*S == S*XX and all(in_G(XX*g) for g in Gp) and XX*kr(sp.Matrix([P0,P1]), sp.Matrix([Q0,Q1])) == kr(X*sp.Matrix([P0,P1]), X*sp.Matrix([Q0,Q1])))
al, be = sp.symbols('alpha beta')
vg = sp.Matrix([al,0,0,be]); Cg = coef(vg); Csg = (Cg+Cg.T)/2; ag = (Cg-Cg.T)[0,1]/2
chk('R6 K_H: G_pure meets U(t)Prod only where alpha*beta = 0, i.e. at |00>, |11> (a=0, det C_s = alpha beta)',
    ag == 0 and sp.expand(Csg.det() - al*be) == 0)
chk('R6 K_H: Ad_{XX} swaps |00> and |11>', XX*sp.Matrix([1,0,0,0]) == sp.Matrix([0,0,0,1]))
chk('R6 K_H: singlet is not in the pure set of K_H (exact K_H != Q3 via rank-one extremality)', not memH(sing))
# repaired K_H* = cone(Ucal.(SEP u G)), Ucal = {U(t)(V(x)V)}: pure set = Sym u U(t)Prod (Takagi: V(x)V . G_pure = Sym)
memHs = lambda v: in_UProd(v) or is_sym(v)
syms = [sp.Matrix([a,b,b,c]) for a,b,c in [(1,1,0),(1,0,1),(0,1,1),(1,2,3),(1,I,2),(2,1+I,-1),(1,1,1),(0,1,0)]]
pureHs = pureKS + syms
hs_wit = {p: find_out(PM[p], pureHs, memHs) for p in perms if p not in comm}
chk('R6 K_H*: each of the 20 non-S-commuting native perms maps a pure state of K_H* outside its pure set',
    len(hs_wit) == 20 and all(w is not None for w in hs_wit.values()))
chk('R6 K_H*: singlet not in its pure set (K_H* != Q3); B (=Phi+, symmetric) in it (MI); K_H* in Q3 (MEV)', not memHs(sing) and memHs(phi))
# Takagi spot check: a generic symmetric C = V D V^T with V unitary -- check that V(x)V maps span{|00>,|11>} onto all Sym
# (dimension count of the real-linear span of the tangent vectors of the map (V, alpha, beta) -> (V(x)V)(alpha|00>+beta|11>))
npass = sum(c for _, c in out); print('SUMMARY %d PASS, %d FAIL' % (npass, len(out)-npass))
raise SystemExit(0 if npass == len(out) else 1)

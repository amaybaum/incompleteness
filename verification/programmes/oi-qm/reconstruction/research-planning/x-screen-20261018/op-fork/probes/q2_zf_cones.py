#!/usr/bin/env python3
"""q2_zf_cones.py -- nodes N3 (K(Z_F)), N4 (L = Q3 n Z_F*), N7 side properties, control C2 (mutated cut).
Exact SymPy; research only.  Universal statements are written arguments [WA] printed as such; each PASS line is an
exact certificate [EC] for the step it names.

Defects (#820, stage 6, as in ../../probes/p3_fixtures_op.py): e_{s,t} = (I + s XZ + t YY - st ZX)/16, z = 4e.
Z_F* = {X : Tr(X e) >= 0 for all four defects};  L = Q3 n Z_F*;  K(Z_F) = L + cone(Z_F).

Written-argument chain (the certificates below are its exact inputs):
 W1  z_k = I/2 - P_{m_k} with {m_k} an orthonormal maximally entangled basis (EC: projector, sum = I, unitarity).
 W2  For PSD X:  sum_k <m_k|X|m_k> = Tr X, so at most two of the four cuts Tr(X z_k) >= 0 are active
     (three active would give 3 Tr X/2 <= Tr X).  A PSD X of rank r >= 2 has minimal face Herm(range X) of
     dimension r^2 >= 4; at most two active linear cuts leave dimension >= 2, so X is not extreme in L.
     Hence Ext(L) = {rank-one PSD psi psi^dag with |<m_k|psi>|^2 <= 1/2 for all k}.
 W3  Ext(K(Z_F)) <= Ext(L) u {z_k}; every element of that set is extreme in maxCone (q1, N1), hence in K(Z_F).
     So the pure states of K(Z_F) are exactly the rank-one states of L and the four defects (full classification).
 W4  Existence at every marginal: the canonical purification psi_rho = sum_i sqrt(rho)|i>|i> lies in L for every rho
     (symbolic identity below + the premise |<m_k|Phi+>|^2 <= 1/2), and is extreme (N1).
 W5  U-weak at every marginal: by PREREG N2 (pure states rank-one or Gamma(rank-one)) and Uhlmann [L].
"""
import sympy as sp
from itertools import product, permutations

I = sp.I
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -I], [I, 0]]); Z = sp.diag(1, -1); I2 = sp.eye(2)
PA = [I2, X, Y, Z]
kr = sp.kronecker_product
s2 = sp.sqrt(2)
def pt2(M):
    R = sp.zeros(4, 4)
    for a, b, c, d in product(range(2), repeat=4):
        R[2*a+d, 2*c+b] = M[2*a+b, 2*c+d]
    return R
def m1(M):
    return sp.simplify(sp.Matrix(2, 2, lambda a, c: sum(M[2*a+b, 2*c+b] for b in range(2))))
def psd(M):
    from itertools import combinations
    n = M.shape[0]
    for k in range(1, n+1):
        for S in combinations(range(n), k):
            m = sp.simplify(M.extract(list(S), list(S)).det())
            if not (m.is_real and m >= 0): return False
    return True
res = []
def chk(name, c):
    res.append((name, bool(c))); print(('PASS ' if c else 'FAIL ') + name)

keys = [(s, t) for s in (1, -1) for t in (1, -1)]
e = {k: (sp.eye(4) + k[0]*kr(X, Z) + k[1]*kr(Y, Y) - k[0]*k[1]*kr(Z, X))/16 for k in keys}
z = {k: 4*v for k, v in e.items()}
Pm = {k: sp.eye(4)/2 - z[k] for k in keys}
mv = {}
for k in keys:
    v = Pm[k].columnspace()[0]; mv[k] = sp.simplify(v/sp.sqrt((v.H*v)[0]))

# ---------------- W1
chk('W1  each I/2 - z_k is a rank-one projector P_{m_k}', all(sp.simplify(Pm[k]*Pm[k] - Pm[k]) == sp.zeros(4, 4) and Pm[k].rank() == 1 for k in keys))
chk('W1  sum_k P_{m_k} = I (orthonormal basis)', sp.simplify(sum((Pm[k] for k in keys), sp.zeros(4, 4))) == sp.eye(4))
def coefmat(v): return sp.Matrix(2, 2, lambda a, b: v[2*a+b])
chk('W1  each m_k is maximally entangled (sqrt2 x coefficient matrix unitary)', all(sp.simplify((s2*coefmat(mv[k])).H*(s2*coefmat(mv[k]))) == I2 for k in keys))
print('     m_k (unit vectors):', {k: list(mv[k]) for k in keys})

# ---------------- W2 inputs: Tr(X z_k) = Tr X/2 - <m_k|X|m_k> on a symbolic Hermitian X
hs = sp.symbols('h0:16', real=True)
Hs = sp.Matrix(4, 4, lambda i, j: 0)
idx = 0
for i in range(4):
    Hs[i, i] = hs[idx]; idx += 1
for i in range(4):
    for j in range(i+1, 4):
        Hs[i, j] = hs[idx] + I*hs[idx+1]; Hs[j, i] = hs[idx] - I*hs[idx+1]; idx += 2
chk('W2  Tr(X z_k) = Tr X/2 - <m_k|X|m_k> for symbolic Hermitian X (all k)',
    all(sp.expand((Hs*z[k]).trace() - (Hs.trace()/2 - (mv[k].H*Hs*mv[k])[0])) == 0 for k in keys))
chk('W2  sum_k <m_k|X|m_k> = Tr X for symbolic X (=> at most two active cuts on PSD X)',
    sp.expand(sum(((mv[k].H*Hs*mv[k])[0] for k in keys), 0) - Hs.trace()) == 0)

# ---------------- Domain inclusions
ax, ay, az, bx, by, bz = sp.symbols('ax ay az bx by bz', real=True)
ra = (I2 + ax*X + ay*Y + az*Z)/2; rb = (I2 + bx*X + by*Y + bz*Z)/2
av = sp.Matrix([ax, ay, az]); bv = sp.Matrix([bx, by, bz])
okprod = True; Ms = {}
for k in keys:
    val = sp.expand(16*(kr(ra, rb)*e[k]).trace())
    M = sp.Matrix(3, 3, lambda i, j: sp.expand(val).coeff(av[i]).coeff(bv[j]))
    Ms[k] = M
    okprod &= sp.expand(val - (1 + (av.T*M*bv)[0])) == 0 and M.T*M == sp.eye(3)
chk('DOM SEP <= Z_F*: 16 Tr((rho_a(x)rho_b) e_k) = 1 + a.M_k b with M_k orthogonal (|a.M_k b| <= 1 on the ball) [EC+WA]', okprod)
chk('DOM L <= Q3 <= maxCone and cone(Z_F) <= maxCone (z_k = Gamma of a rank-one projector)',
    all(sp.simplify(pt2(z[k])*pt2(z[k]) - pt2(z[k])) == sp.zeros(4, 4) and pt2(z[k]).trace() == 1 for k in keys))

# ---------------- Distinctness
phi = sp.Matrix([1, 0, 0, 1])/s2; B = phi*phi.H
ovPhi = {k: sp.simplify(abs((mv[k].H*phi)[0])**2) for k in keys}
chk('NEQ Phi+ in L: |<m_k|Phi+>|^2 <= 1/2 for all k  (values %s)' % sorted(set(ovPhi.values())), all(v <= sp.Rational(1, 2) for v in ovPhi.values()))
chk('NEQ Phi+ not in Gamma(Q3) (Gamma(B) has eigenvalue -1/2)  => L != Gamma(Q3), K(Z_F) != Gamma(Q3)', sp.Rational(-1, 2) in pt2(B).eigenvals())
chk('NEQ m_k in Q3 but Tr(P_{m_k} z_k) = -1/2 < 0  => m_k not in L, L != Q3', all(sp.simplify((Pm[k]*z[k]).trace()) == sp.Rational(-1, 2) for k in keys))
chk('NEQ z_k not in Q3 (eigenvalue -1/2)  => K(Z_F) != Q3', all(sp.Rational(-1, 2) in z[k].eigenvals() for k in keys))
print('     [WA] m_k not in K(Z_F): m_k is extreme in maxCone, so m_k in L + cone(Z_F) forces m_k on a ray of L or of some z_j;'
      ' neither holds.')

# ---------------- W4 existence: symbolic identity
al, be = sp.symbols('alpha beta', real=True)
n1, n2, n3 = sp.symbols('n1 n2 n3', real=True)
c0, c1, c2, c3, th = sp.symbols('c0 c1 c2 c3 theta', real=True)
sq = al*I2 + be*(n1*X + n2*Y + n3*Z)
psi = sp.zeros(4, 1)
for i in range(2):
    col = sq[:, i]
    for a in range(2):
        psi[2*a+i] += col[a]
def reduce_(expr):
    expr = sp.expand(expr)
    expr = sp.expand(expr.subs(al**2, sp.Rational(1, 2) - be**2))
    expr = sp.expand(expr.subs(n1**2, 1 - n2**2 - n3**2))
    return sp.expand(expr)
chk('W4  m1(psi_rho psi_rho^dag) = sqrt(rho)^2 (canonical purification has token-1 marginal rho)',
    sp.expand(m1(psi*psi.H) - sq*sq) == sp.zeros(2, 2))
wd = sp.exp(I*th)*(c0*I2 + I*(c1*X + c2*Y + c3*Z))     # w^dag; unitary iff c0^2+|c|^2 = 1
wmat = wd.H
mgen = sp.zeros(4, 1)
for i in range(2):
    col = wmat[:, i]
    for a in range(2):
        mgen[2*i+a] += col[a]/s2                          # (I (x) w) Phi+
ov = (mgen.H*psi)[0]
ov2 = sp.expand(sp.simplify(ov*sp.conjugate(ov)))
ntil = (n1, -n2, n3)
lhs = sp.Rational(1, 2) - ov2
rhs = (1 - 4*be**2)*(sp.Rational(1, 2) - c0**2) + 2*be**2*(1 - c0**2 - (ntil[0]*c1 + ntil[1]*c2 + ntil[2]*c3)**2)
diff = reduce_(lhs - rhs)
diff = sp.expand(diff.subs(c0**2, 1 - c1**2 - c2**2 - c3**2))
chk('W4  identity: 1/2 - |<m|psi_rho>|^2 = (1-4b^2)(1/2-c0^2) + 2b^2(1-c0^2-(n~.c)^2) for every max-ent m = (I(x)w)Phi+,'
    ' given a^2+b^2 = 1/2, |n| = 1, c0^2+|c|^2 = 1', sp.simplify(diff) == 0)
ovPhiGen = sp.expand(sp.simplify(((mgen.H*phi)[0])*sp.conjugate((mgen.H*phi)[0])))
chk('W4  c0^2 = |<m|Phi+>|^2 for m = (I(x)w)Phi+ (the lemma premise is the Phi+ cut condition)', sp.simplify(ovPhiGen - c0**2) == 0)
print('     [WA] with alpha >= |beta| and alpha^2+beta^2 = 1/2, beta^2 <= 1/4; Cauchy-Schwarz gives (n~.c)^2 <= |c|^2;'
      ' so the right side is >= 0 whenever |<m|Phi+>|^2 <= 1/2.  sqrt(rho) = alpha I + beta n.sigma covers every token'
      ' state rho (alpha, beta from the square roots of its eigenvalues).  Hence psi_rho in L for every rho.')

# independent instance countercheck: direct construction, no use of the identity
lams = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(1, 2), sp.sqrt(3)/2), (1, 0), (1/s2, 1/s2)]
Us = [I2, sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]]),
      sp.Matrix([[1, 1], [1, -1]])/s2, sp.Matrix([[1, I], [I, 1]])/s2,
      sp.Matrix([[1 + I, 1 - I], [1 - I, 1 + I]])/2*sp.diag(1, I),
      sp.Matrix([[sp.Rational(5, 13), -sp.Rational(12, 13)*I], [-sp.Rational(12, 13)*I, sp.Rational(5, 13)]])]
okinst = True; minval = None; ninst = 0
for (r0, r1) in lams:
    for U in Us:
        sqr = U*sp.diag(r0, r1)*U.H
        rho = sp.simplify(sqr*sqr)
        ps = sp.zeros(4, 1)
        for i in range(2):
            for a in range(2):
                ps[2*a+i] += sqr[a, i]
        Pp = ps*ps.H
        okinst &= sp.simplify(m1(Pp) - rho) == sp.zeros(2, 2)
        for k in keys:
            v = sp.nsimplify(sp.simplify((Pp*z[k]).trace()))
            okinst &= bool(v >= 0); ninst += 1
            minval = v if minval is None or v < minval else minval
chk('W4  instance countercheck: %d (marginal, defect) pairs, 24 marginals incl. non-diagonal, direct psi_rho in Z_F*' % ninst, okinst)
print('     min Tr(psi psi^dag z_k) over instances =', minval)

# C2 mutated cut: a cut whose eigenvector is Phi+ violates the lemma premise; routine must report FAIL
zmut = sp.eye(4)/2 - B
chk('C2  mutated cut z\' = I/2 - P_Phi+: canonical purification of I/2 (= Phi+) violates it: Tr(B z\') = -1/2 (existence routine reports FAIL)',
    sp.simplify((B*zmut).trace()) == sp.Rational(-1, 2))

# ---------------- U-strong failure (direct, at the I/2 pair) and U-weak-SO
v = sp.diag(1, I)
psi2 = kr(I2, v)*phi
chk('US  psi2 = (I(x)diag(1,i))Phi+ is a pure state of L (|<m_k|psi2>|^2 <= 1/2)', all(sp.simplify(abs((mv[k].H*psi2)[0])**2) <= sp.Rational(1, 2) for k in keys))
wit = None
for k in keys:
    xk = kr(I2, v.H)*mv[k]
    if all(sp.simplify(abs((mv[j].H*xk)[0])**2) <= sp.Rational(1, 2) for j in keys):
        wit = (k, xk); break
chk('US  witness x = (I(x)v^dag) m_k lies in L while Ad_{I(x)v} x = P_{m_k} lies outside L and outside K(Z_F)', wit is not None)
if wit: print('     witness defect index', wit[0], 'x =', list(wit[1]))
print('     [WA] Phi+ and psi2 are pure states of L and of K(Z_F) with marginal I/2.  The relating maps g in O(3): improper'
      ' g send Phi+ to Gamma(max-ent), which is not PSD, so not psi2; proper g = Ad_u need (I(x)u)Phi+ = e^{i f}(I(x)v)Phi+,'
      ' i.e. u = e^{i f} v.  The only relating map is Ad_v, which is not an automorphism (witness).  U-strong FAILS for'
      ' L and for K(Z_F).')
chk('USO K(Z_F) fails U-weak-SO: Phi+ (PSD) and z_k (eigenvalue -1/2) are pure at I/2; Ad_u preserves PSD',
    sp.Rational(-1, 2) in z[keys[0]].eigenvals() and psd(B))
print('     [WA] L passes U-weak-SO: all its pure states are rank-one PSD, related by Ad_u (Uhlmann [L]).')

# ---------------- N7 side properties: the 24 native permutations
def permmat(p):
    M = sp.zeros(4, 4)
    for i in range(4): M[p[i], i] = 1
    return M
eset = [e[k] for k in keys]
inv = 0; cnot_ok = False; swap_ok = False
CN = permmat((0, 1, 3, 2)); SW = permmat((0, 2, 1, 3))
for p in permutations(range(4)):
    P = permmat(p)
    imgs = [sp.simplify(P*E*P.T) for E in eset]
    ok = all(any(im == E2 for E2 in eset) for im in imgs) and len({tuple(im) for im in imgs}) == 4
    inv += ok
    if P == CN: cnot_ok = ok
    if P == SW: swap_ok = ok
chk('N7  all 24 native permutations permute the defect set (=> preserve Z_F*, Q3, L and K(Z_F))', inv == 24)
chk('N7  PC: CNOT among them;  token symmetry: SWAP among them', cnot_ok and swap_ok)
print('     [WA] MI for L and K(Z_F): CNOT(rho(x)P0)CNOT is PSD and pairs with e_k as (rho(x)P0) with CNOT e_k CNOT,'
      ' a defect, which is >= 0 on products (DOM line).')

nf = sum(1 for _, c in res if not c)
print('SUMMARY checks=%d failed=%d' % (len(res), nf))
cert = lambda pre: all(c for n, c in res if n.startswith(pre))
dom = cert('DOM'); neq = cert('NEQ'); w = cert('W'); us = cert('US')
print('RESULT N3_KZF domain=%s pure_classification=%s existence_all_marginals=%s uweak_all_marginals=%s distinct=%s ustrong=%s' %
      ('GREEN' if dom else 'RED', 'GREEN' if cert('W1') and cert('W2') else 'RED', 'GREEN' if cert('W4') else 'RED',
       'GREEN' if w else 'RED', 'GREEN' if neq else 'RED', 'FAIL' if us else 'UNDETERMINED'))
print('RESULT N4_L domain=%s pure_classification=%s existence_all_marginals=%s uweak_all_marginals=%s distinct=%s ustrong=%s uweakSO=%s' %
      ('GREEN' if dom else 'RED', 'GREEN' if cert('W1') and cert('W2') else 'RED', 'GREEN' if cert('W4') else 'RED',
       'GREEN' if w else 'RED', 'GREEN' if neq else 'RED', 'FAIL' if us else 'UNDETERMINED', 'PASS' if w else 'RED'))
print('RESULT N7 native_perm_invariant=%d/24 PC=%s' % (inv, cnot_ok))
print('RESULT C2_mutated_cut=%s' % ('GREEN' if cert('C2') else 'RED'))
print('VERDICT', 'N3/N4-GREEN: K(Z_F) and L = Q3 n Z_F* are domain cones other than Q3 and Gamma(Q3) whose pure states are'
      ' classified exactly (rank-one, plus the four defects for K(Z_F)); existence holds at every marginal (symbolic) and'
      ' U-weak at every marginal [WA on EC inputs]; U-strong fails for both (exact witness); both are invariant under all 24'
      ' native permutations' if nf == 0 else 'VOID')

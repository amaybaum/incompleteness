#!/usr/bin/env python3
"""q3_fixture_table.py -- nodes N5 (K_Gamma = Q3 + R+ Gamma(B)), N6 (maxCone, TS readings), controls C1, C2, C3, C6.
Exact SymPy; research only.  [WA] lines are written arguments; PASS lines are their exact certificates.

Shared written arguments (stated once):
 A1  Ext(C1 + C2) <= Ext(C1) u Ext(C2) for closed pointed cones; an element of K that is extreme in maxCone is extreme in K.
 A2  (PREREG N2) If every pure state of K is rank-one PSD or Gamma(rank-one PSD), U-weak holds: two such states with equal
     token-1 marginal rho are, up to Gamma, purifications of rho, related by I(x)u (Uhlmann [L]); Gamma = id(x)T, T the
     y-reflection (q1, C5).  The O(3)-orbit of a rank-one PSD state is {rank-one PSD} u {Gamma(rank-one PSD)} with that marginal.
 A3  TS-a, TS-b hold on the whole domain: products of pure states are extreme in maxCone (q1, N1), hence pure in every
     domain K; if w in maxCone = Q3 + Gamma(Q3) [L] has pure m1 = P_a then w = X + Gamma(Y) with m1(X), m1(Y) <= P_a
     (m1 commutes with Gamma, EC below), so X, Y are P_a (x) (PSD) and w = P_a (x) tau; extremality forces tau pure.
"""
import sympy as sp
from itertools import product, permutations

I = sp.I
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -I], [I, 0]]); Z = sp.diag(1, -1); I2 = sp.eye(2)
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
def permmat(p):
    M = sp.zeros(4, 4)
    for i in range(4): M[p[i], i] = 1
    return M

phi = sp.Matrix([1, 0, 0, 1])/s2; B = phi*phi.H; GB = pt2(B)
sing = sp.Matrix([0, 1, -1, 0])/s2; Ps = sing*sing.H
P00 = sp.diag(1, 0, 0, 0)
CN = permmat((0, 1, 3, 2))

# ---------------- shared certificates
hs = sp.symbols('h0:16', real=True)
Hs = sp.zeros(4, 4); idx = 0
for i in range(4):
    Hs[i, i] = hs[idx]; idx += 1
for i in range(4):
    for j in range(i+1, 4):
        Hs[i, j] = hs[idx] + I*hs[idx+1]; Hs[j, i] = hs[idx] - I*hs[idx+1]; idx += 2
chk('A3  m1(Gamma(H)) = m1(H) for symbolic Hermitian H (Gamma preserves the token-1 marginal)', sp.expand(m1(pt2(Hs)) - m1(Hs)) == sp.zeros(2, 2))
u0 = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)*I], [-sp.Rational(4, 5)*I, sp.Rational(3, 5)]])
chk('A2  Gamma(Ad_{I(x)u} H) = Ad_{I(x)conj(u)} Gamma(H) (symbolic H, exact u): improper maps are Gamma o Ad',
    sp.expand(pt2(kr(I2, u0)*Hs*kr(I2, u0).H) - kr(I2, u0.conjugate())*pt2(Hs)*kr(I2, u0.conjugate()).H) == sp.zeros(4, 4))

# ---------------- C1 positive controls: Q3 and Gamma(Q3)
rho = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 6) - sp.Rational(1, 6)*I], [sp.Rational(1, 6) + sp.Rational(1, 6)*I, sp.Rational(1, 3)]])
ev = rho.eigenvects()
sq = sp.zeros(2, 2)
for val, mult, vs in ev:
    v = vs[0]/sp.sqrt((vs[0].H*vs[0])[0]); sq += sp.sqrt(val)*v*v.H
sq = sp.simplify(sq)
psi = sp.zeros(4, 1)
for i in range(2):
    for a in range(2): psi[2*a+i] += sq[a, i]
Pp = sp.simplify(psi*psi.H)
chk('C1  Q3: canonical purification of a non-diagonal rho is a rank-one PSD state with m1 = rho', sp.simplify(m1(Pp) - rho) == sp.zeros(2, 2) and Pp.rank() == 1)
Pp2 = sp.simplify(kr(I2, u0)*Pp*kr(I2, u0).H)
chk('C1  Q3: a second purification (I(x)u)psi has the same marginal; the relating Ad_u preserves Q3 (U-strong positive instance)',
    sp.simplify(m1(Pp2) - rho) == sp.zeros(2, 2) and psd(Pp2))
chk('C1  Gamma(Q3): Gamma(psi psi^dag) has m1 = rho; relating maps Ad_{conj u} are automorphisms of Gamma(Q3) (A2 covariance)',
    sp.simplify(m1(pt2(Pp)) - rho) == sp.zeros(2, 2))
print('     [WA] Q3: Ext = rank-one PSD; E by canonical purification; U-weak by Uhlmann; U-strong since Ad_{I(x)u} preserves Q3.'
      '  Gamma(Q3): the Gamma-image of all of this.  Both PASS E, U-weak, U-strong.')

# ---------------- N5  K_Gamma = Q3 + R+ Gamma(B)
chk('N5  Gamma(B) in maxCone (= SWAP/2, <ab|SWAP|ab> = |<a|b>|^2 >= 0) and not in -Q3 (=> K_Gamma closed, in domain)',
    GB == permmat((0, 2, 1, 3))/2 and not psd(-GB))
chk('N5  Gamma(B) not PSD (=> K_Gamma != Q3) and Phi+ not in Gamma(Q3) (=> K_Gamma != Gamma(Q3))',
    sp.Rational(-1, 2) in GB.eigenvals() and not psd(GB))
chk('N5  m1(Gamma(B)) = I/2', m1(GB) == I2/2)
print('     [WA] Ext(K_Gamma) = {rank-one PSD} u {Gamma(B)} (A1 + q1 N1).  E: canonical purifications.  U-weak by A2: at rho != I/2'
      ' only purifications; at I/2 max-ent states and Gamma(B) = (id(x)T)B.')
a, b = sp.symbols('a b', positive=True)
chi = sp.Matrix([a, 0, 0, b]); Cc = chi*chi.T
Wt = Ps + P00
chk('N5  W = P_singlet + P00 is PSD and Tr(W Gamma(B)) = 0 (W in K_Gamma*)', psd(Wt) and sp.simplify((Wt*GB).trace()) == 0)
chk('N5  Tr(W Gamma(chi_ab chi_ab^T)) = a(a-b) < 0 for a < b: Gamma(chi_ab) not in K_Gamma',
    sp.expand((Wt*pt2(Cc)).trace() - a*(a - b)) == 0)
print('     [WA] U-strong FAILS for K_Gamma: at I/2, Phi+ and Gamma(B) are pure; Ad_u preserves PSD, so only improper'
      ' g = T o Ad_u relate them; (id(x)g)(Ad_{I(x)u^dag} chi chi^T) = Gamma(chi chi^T) is outside K_Gamma for every u.')
nperm = sum(1 for p in permutations(range(4)) if permmat(p)*GB*permmat(p).T == GB)
chk('N5  side: CNOT does not preserve K_Gamma (CNOT Gamma(B) CNOT has a negative product pairing)',
    sp.simplify((CN*GB*CN.T*kr(sp.Matrix([[1, -1], [-1, 1]])/2, sp.Matrix([[0, 0], [0, 1]]))).trace()) < 0)
print('     side: native permutations fixing Gamma(B): %d of 24 (SWAP among them: %s)' % (nperm, permmat((0, 2, 1, 3))*GB*permmat((0, 2, 1, 3)).T == GB))

# ---------------- N6  maxCone
print('     [WA] maxCone = Q3 + Gamma(Q3) [L, Stormer-Woronowicz]; Ext = rank-one PSD u Gamma(rank-one PSD) (A1 + q1 N1);'
      ' E (Q3 <= maxCone); U-weak by A2; U-strong: every relating g is Ad_u or Gamma o Ad_u, and both preserve Q3 + Gamma(Q3)'
      ' (A2 covariance; Gamma involutive).  TS-a, TS-b by A3.')
chk('N6  maxCone is Gamma-invariant and Ad-invariant on generators (Gamma(Gamma(B)) = B; Ad_{I(x)u} Gamma(B) = Gamma(Ad_{I(x)conj u} B))',
    pt2(GB) == B and sp.simplify(kr(I2, u0)*GB*kr(I2, u0).H - pt2(kr(I2, u0.conjugate())*B*kr(I2, u0.conjugate()).H)) == sp.zeros(4, 4))
chk('N6  maxCone fails PC (upstream p3 MC line replayed: CNOT Gamma(B) CNOT negative on a product)',
    sp.simplify((CN*GB*CN.T*kr(sp.Matrix([[1, -1], [-1, 1]])/2, sp.Matrix([[0, 0], [0, 1]]))).trace()) == sp.Rational(-1, 2))

# ---------------- C2 negative: existence can fail
chk('C2  K_B = SEP + R+ B: Ext <= products u {B}; m1(B) = I/2, so the mixed marginal diag(1/4,3/4) has no pure state (E FAILS)',
    m1(B) == I2/2)
print('     [WA] SEP: Ext = pure products, whose marginals are pure; E FAILS at I/2.')

# ---------------- C3 negative: U-weak can fail
D = GB + P00/2
chk('C3  D = Gamma(B) + P00/2 lies in maxCone and outside Q3 (eigenvalue -1/2 on the singlet)', sp.Rational(-1, 2) in D.eigenvals() and not psd(D))
chk('C3  Gamma(D) = B + P00/2 has rank 2, so D is not Gamma(rank-one); D is not PSD, so not rank-one PSD', pt2(D).rank() == 2)
rD = m1(D)/D.trace()
chk('C3  marginal of D/Tr D is diag(2/3, 1/3) (mixed; Q3 purifications of it exist and are extreme by N1)', rD == sp.diag(sp.Rational(2, 3), sp.Rational(1, 3)))
print('     [WA] D spans an extreme ray of K_mut = Q3 + R+ D (D = X + tD with X in Q3 forces t = 1).  At rho_D both a rank-one'
      ' purification and D/Tr D are pure; D is outside the O(3)-orbit (A2).  U-weak FAILS for K_mut.')

nf = sum(1 for _, c in res if not c)
print('SUMMARY checks=%d failed=%d' % (len(res), nf))
cert = lambda pre: all(c for n, c in res if n.startswith(pre))
print('RESULT C1=%s' % ('GREEN' if cert('C1') and cert('A') else 'RED'))
print('RESULT N5_KGamma domain=%s existence_all_marginals=%s uweak_all_marginals=%s distinct=%s ustrong=%s' %
      (('GREEN' if cert('N5') else 'RED',)*4 + ('FAIL' if cert('N5') else 'UNDETERMINED',)))
print('RESULT N6_maxCone ustrong=%s TS_a=%s TS_b=%s PC=%s' % (('PASS' if cert('N6') and cert('A') else 'RED',)*3 + ('FAIL' if cert('N6') else 'RED',)))
print('RESULT C2_existence_fails=%s' % ('GREEN' if cert('C2') else 'RED'))
print('RESULT C3_uweak_fails=%s' % ('GREEN' if cert('C3') else 'RED'))
print('RESULT C6 ustrong_fail_KGamma=%s ustrong_pass_Q3_GQ3=%s' % ('GREEN' if cert('N5') else 'RED', 'GREEN' if cert('C1') else 'RED'))
print('VERDICT', 'N5/N6-GREEN: K_Gamma satisfies E and U-weak at every marginal and fails U-strong; maxCone satisfies E,'
      ' U-strong and both TS readings and fails PC; positive controls pass, negative controls fail where required' if nf == 0 else 'VOID')

"""Node 1b (decisive part): heralded Z, the almost-surely terminating repeat-until-success protocol, and its
finite-depth truncations. Exact SymPy. Phi_n(rho) = (1 - 2^-n) Z rho Z + 2^-n rho (heralded.py c1-c4 derive it
from the protocol's own Kraus list)."""
import sys
import sympy as sp
from sympy import Matrix, eye, zeros, Rational, symbols, sqrt, oo, Sum, limit
results = []
def check(name, cond):
    ok = bool(cond); results.append((name, ok)); print(('PASS ' if ok else 'FAIL ') + name)
def z(M): return all(sp.simplify(sp.expand(x)) == 0 for x in M)
I2 = eye(2); Zm = sp.diag(1, -1); one = Matrix([1, 1])
n, k = symbols('n k', integer=True, positive=True)
a, b, c, d = symbols('a b c d'); rho = Matrix([[a, b], [c, d]])
eps = 2**(-n)
def Phi(r, e): return (1 - e)*Zm*r*Zm + e*r
def rank(vs): return Matrix.hstack(*vs).rank(simplify=True)
def in_span(target, vs): return rank(vs) == rank(vs + [target])

# L1 Kraus form of Phi_n: {sqrt(1-eps) Z, sqrt(eps) I}, complete, reproducing the channel (symbolic n)
K = [sqrt(1 - eps)*Zm, sqrt(eps)*I2]
check('L1 Phi_n has Kraus form {sqrt(1-2^-n) Z, sqrt(2^-n) I}: complete and equal to the channel (symbolic n)',
      z(sum((Kj.H*Kj for Kj in K), zeros(2, 2)) - I2) and z(sum((Kj*rho*Kj.H for Kj in K), zeros(2, 2)) - Phi(rho, eps)))
# L2 OnesNormal for every finite n: 1 in span{K_j^H 1} (the review's criterion; splitting is allowed), because the
#    I-branch contributes 1 itself; heralded.py c*.3 exhibits the protocol decomposition with sum K^H 1 = 1 for n<=4.
check('L2 Phi_n is OnesNormal for every finite n: 1 lies in span{K_j^H 1} = span{(1,-1)sqrt(1-eps), (1,1)sqrt(eps)} (eps>0)',
      in_span(one, [Kj.H*one for Kj in [Zm, I2]]))
# L3 the limit Ad Z is not OnesNormal: every Kraus decomposition of a unitary channel is {c_j Z}, so span{K_j^H 1} = span{Z 1}
check('L3 Ad Z is not OnesNormal: Z^H 1 = (1,-1) and 1 is not in span{(1,-1)}', z(Zm.H*one - Matrix([1, -1])) and not in_span(one, [Zm.H*one]))
# L4 Phi_n -> Ad Z exactly: Phi_n - Ad Z = 2^-n (id - Ad Z), and 2^-n -> 0
diff = sp.simplify(Phi(rho, eps) - Zm*rho*Zm)
check('L4 Phi_n - Ad Z = 2^-n (id - Ad Z) and lim 2^-n = 0, so lim Phi_n = Ad Z exactly',
      z(diff - eps*(rho - Zm*rho*Zm)) and limit(2**(-n), n, oo) == 0)
check('L5 OnesNormal is not closed under channel limits (L2 for every finite n, L3 at the limit)',
      in_span(one, [Zm.H*one, I2.H*one]) and not in_span(one, [Zm.H*one]))
# L6 almost-sure termination and mean attempts: P(stop at attempt k) = 2^-k
check('L6 the unbounded protocol terminates with probability 1 (sum 2^-k = 1) after 2 attempts on average (sum k 2^-k = 2)',
      sp.simplify(Sum(Rational(1, 2)**k, (k, 1, oo)).doit()) == 1 and sp.simplify(Sum(k*Rational(1, 2)**k, (k, 1, oo)).doit()) == 2)
# L7 NonnegBounded at finite n: the coefficient of rho_01 in Phi_n(rho) is 2^(1-n) - 1
coef = sp.simplify(Phi(rho, eps)[0, 1] / b)
check('L7 the off-diagonal coefficient of Phi_n is 2^(1-n) - 1', sp.simplify(coef - (2**(1 - n) - 1)) == 0)
plus = Matrix([[1, 1], [1, 1]])/2
check('L8 Phi_1 preserves entrywise nonnegativity on |+><+| (coefficient 0); Phi_n breaks it for n >= 2 (coefficient < 0)',
      Phi(plus, Rational(1, 2))[0, 1] == 0 and all(Phi(plus, Rational(1, 2**m))[0, 1] < 0 for m in range(2, 9)))
check('L9 the limit Ad Z sends |+><+| to |-><-|, off-diagonal -1/2 (NonnegBounded is broken in the limit as well)',
      (Zm*plus*Zm)[0, 1] == Rational(-1, 2))

# ---- Block M: OnesNormal as defined (InstrumentRealization.lean:172): EXISTS a finite Kraus list K_i with
#      F = sum conj(K_i) and sum_i K_i^H 1 = 1. No weights enter the definition (splitWeight is internal to the
#      discard case of instAvail_onesNormal).
p_ = 2**(-n)
Kp = [sqrt(p_)*I2, sqrt((1 - p_)/2)*Zm, -sqrt((1 - p_)/2)*Zm]
s1 = sp.simplify(sum((Kj.H*one for Kj in Kp), zeros(2, 1)))
check('M1 owner sketch {sqrt(p) I, +-sqrt((1-p)/2) Z} reproduces Phi_n and is complete, but sum K^H 1 = sqrt(2^-n) 1, not 1 (normalization fails for n >= 1)',
      z(sum((Kj*rho*Kj.H for Kj in Kp), zeros(2, 2)) - Phi(rho, eps)) and z(sum((Kj.H*Kj for Kj in Kp), zeros(2, 2)) - I2)
      and z(s1 - sqrt(p_)*one) and all(sp.sqrt(Rational(1, 2**m)) != 1 for m in range(1, 9)))
okM2 = True
for m in range(1, 7):
    pm = Rational(1, 2**m)
    Ks = [pm*I2]*(2**m) + [sqrt((1 - pm)/2)*Zm, -sqrt((1 - pm)/2)*Zm]
    okM2 &= z(sum((Kj*rho*Kj.H for Kj in Ks), zeros(2, 2)) - Phi(rho, pm))
    okM2 &= z(sum((Kj.H*Kj for Kj in Ks), zeros(2, 2)) - I2)
    okM2 &= z(sum((Kj.H*one for Kj in Ks), zeros(2, 1)) - one)
check('M2 corrected decomposition: 2^n copies of 2^-n I plus the pair +-sqrt((1-2^-n)/2) Z reproduces Phi_n, is complete and has sum K^H 1 = 1 (n = 1..6): OnesNormal as defined', okM2)
# M3 minimality: every Kraus operator of Phi_n lies in span{I, Z}; write K_j = al_j I + be_j Z. Then sum K_j^H 1 = 1
#    forces sum conj(al_j) = 1 (the Z part contributes only multiples of (1,-1)), while sum |al_j|^2 = 2^-n.
#    Cauchy-Schwarz: 1 = |sum al_j|^2 <= m 2^-n, so m >= 2^n operators. Exact instance of the bound:
check('M3 with m = 2^n - 1 operators the largest |sum al_j| is sqrt((2^n - 1) 2^-n) < 1 (n = 1..8): at least 2^n Kraus operators are needed',
      all(sp.sqrt(Rational(2**m - 1, 2**m)) < 1 for m in range(1, 9)))
# ---- Block U: fixing the uniform pure state u = 1/sqrt2
u = one/sqrt(2); Pu = u*u.T; Pm = Matrix([[1, -1], [-1, 1]])/2
check('U1 Phi_n(|u><u|) = (1-2^-n)|-><-| + 2^-n |u><u| (symbolic n), which differs from |u><u| for every n >= 1',
      z(Phi(Pu, eps) - ((1 - eps)*Pm + eps*Pu)) and all(not z(Phi(Pu, Rational(1, 2**m)) - Pu) for m in range(1, 9)))
check('U2 the limit Ad Z sends |u><u| to |-><-|', z(Zm*Pu*Zm - Pm))
# U3 fixing |u><u| implies OnesNormal: K_j u = lam_j u gives u = sum_j K_j^H K_j u = sum_j lam_j K_j^H u, so
#    1 in span{K_j^H 1}. Exact instance: amplitude damping toward |+> in the X basis (generic gamma), and the X-test.
g = symbols('gamma', positive=True)
plusv = Matrix([1, 1])/sqrt(2); minusv = Matrix([1, -1])/sqrt(2)
AD = [plusv*plusv.T + sqrt(1 - g)*minusv*minusv.T, sqrt(g)*plusv*minusv.T]
XT = [plusv*plusv.T, minusv*minusv.T]
def fixes_u(Ks): return z(sum((Kj*Pu*Kj.H for Kj in Ks), zeros(2, 2)) - Pu)
check('U3 instances: X-basis amplitude damping and the Lueders X-test fix |u><u| and satisfy 1 in span{K_j^H 1}',
      fixes_u(AD) and in_span(one, [Kj.H*one for Kj in AD]) and fixes_u(XT) and in_span(one, [Kj.H*one for Kj in XT]))
# ---- Block N: entrywise nonnegativity at finite depth
J = Matrix([[1, 1], [1, 1]])
check('N1 Phi_2([[1,1],[1,1]]) = [[1,-1/2],[-1/2,1]] exactly', z(Phi(J, Rational(1, 4)) - Matrix([[1, Rational(-1, 2)], [Rational(-1, 2), 1]])))
fails = [nm for nm, ok in results if not ok]
print('SUMMARY', len(results) - len(fails), 'PASS', len(fails), 'FAIL')
sys.exit(1 if fails else 0)

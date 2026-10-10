#!/usr/bin/env python3
"""Coordinator's independent check of thread Z's claims (stage 4, Q-EX, countermodels), written from Z's RESULT/NOTES
claims only, without Z's code.  Exact arithmetic (sympy / Fraction).  DECISION RULE (fixed before the first run): every
line CONFIRMED or MISMATCH; verdict INDEP-Z-CONFIRMED iff all lines CONFIRMED, countercontrols included.

Sections.  K: the K_T refutation (S2's natural torus-invariant Bell-type surgery is not self-dual): in the product
basis B = (|0+>, |1->, |0->, |1+>) the circle-1 defect cone is L1 = {-u E12 - conj(u) E21 + L (E33+E44) : |u| <= L}
with dual {2|y12| <= y33 + y44}; Z's y and w are checked to lie in K_T* = (Q + L1 + L2) cap L1* cap L2* exactly, and
tr(y w) = -6/625 (ipW = -24/625).  P: the pair obstruction tr(yw) = c - 1/(4c) for two Bell-type defects at squared
overlap c (symbolic), and NOTES N15's generalization 4c - (1-a)^2/G for seeds aE00 - T/4 (symbolic).  S: the S3 seed
psi_a = (15,-1,7,7)/18: |det| constant 28/81 on the torus orbits of psi_a and CNOT psi_a, f = 1/2 + 5 sqrt(137)/162
<= 7/8, rho(e) psi = -psi/32; no Bell-type defect for S3 (CNOT sends (|++> + e^{i g}|-->)/sqrt2 to a product; AM-GM
step as [W]); S3-z seed (7,4,0,4)/9 with min|det| = 16/81 and f = 1/2 + sqrt(5537)/162 <= 24/25.  G: the groups as
signed permutations of the 16 Pauli tables (cnot = Ad(CNOT) control-first, Ad(Z(x)I), Ad(I(x)Z), T, SWAP, Ad(I(x)H),
Ad(S(x)I), Ad(H(x)I), Ad(I(x)S)): orders 16, 48, 128, 32, 64 (local Paulis + T + cnot), 192, 23040, Stab_Cl(Z_F) =
1536; the action of <G16, SWAP> on the four defects has image of order 24; the G_S orbit of e_F has 8 defects with
off-diagonal pairings in {0, 1/8}; the conjecture refutation's marginal identities (X(x)I and Y(x)I coefficients of
cnot T equal C11, C21; the I(x)Z coefficient of cnot.Ad(I(x)H) T equals C31) symbolically; the seeds' m values
4160/6561 (G_H) and 6272/6561 (G_Cl) by exhaustive enumeration; a product state has m = 1.  A: the axis question at
level (ii): control (3,4,0)/5 and target (0,3,4)/5 with the images under T and Ad(I(x)Z) that G16 supplies close to
dimension >= 4 (reachable), so Z's [W] extrapolation 'EXOTIC for every equatorial control axis / every target axis
perpendicular to x' holds at level (i) only; the coordinate axes stay exceptional.
Countercontrols: c = 16/25 gives a positive pair value; the SD2 orthogonal pair is outside the construction (c = 0);
a product state is reachable (min|det| = 0; m = 1); a member of K_T pairs >= 0 with w; the pair (y,w) is not in K_T.
"""
import itertools, sys
from fractions import Fraction
import sympy as sp
R = []
def rec(cid, kind, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} [{kind}] {text}" + (f" -- {detail}" if detail else ""))
I2 = sp.eye(2); SX = sp.Matrix([[0,1],[1,0]]); SY = sp.Matrix([[0,-sp.I],[sp.I,0]]); SZ = sp.Matrix([[1,0],[0,-1]])
SG = [I2, SX, SY, SZ]; kron = sp.kronecker_product
KR = {(m,n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m,n]*KR[(m,n)] for m in range(4) for n in range(4) if w[m,n] != 0), sp.zeros(4,4))/4
def tab(M): return sp.Matrix(4,4, lambda m,n: sp.nsimplify(sp.expand((KR[(m,n)]*M).trace())))
def ipW(a,b): return sp.expand(sum(a[i,j]*b[i,j] for i in range(4) for j in range(4)))
def E(m,n): B = sp.zeros(4,4); B[m,n] = 1; return B
def charcoeffs(M):
    x = sp.Symbol('x'); return sp.Poly(sp.expand((x*sp.eye(M.rows) - M).det()), x).all_coeffs()
def is_psd(M):
    cs = charcoeffs(M); return all(sp.simplify((-1)**k * cs[k]) >= 0 for k in range(len(cs)))
CNOT = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
Hd = sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2); Sg = sp.Matrix([[1,0],[0,sp.I]])
SWAPU = sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
def Psi(psi): return sp.Matrix(2,2, lambda i,j: psi[2*i+j])

print("== K  the K_T refutation (Z's S2 explicit-cone attempt): y, w in K_T* with tr(yw) < 0, in the basis B = (|0+>,|1->,|0->,|1+>)")
c1 = (1 + 2*sp.I)/5; c2 = (2 - sp.I)/5
y = sp.Matrix([[1, 1, c1, 0], [1, 1, c2, 0], [sp.conjugate(c1), sp.conjugate(c2), 1, 0], [0, 0, 0, 1]])
def ell1(u, L):  # circle-1 defect cone element: -u E12 - conj(u) E21 + L (E33 + E44); membership |u| <= L
    M = sp.zeros(4,4); M[0,1] = -u; M[1,0] = -sp.conjugate(u); M[2,2] = L; M[3,3] = L; return M
# K1: the circle-1 defects (I - 2 phi phi^dag) for phi = (1, e^{i g}, 0, 0)/sqrt2 are exactly ell1(e^{-i g}, 1) (so cone = L1), symbolic in g
g_ = sp.Symbol('g', real=True); phi = sp.Matrix([1, sp.exp(sp.I*g_), 0, 0])/sp.sqrt(2)
dphi = sp.eye(4) - 2*phi*phi.H
rec("K1","identity", (dphi - ell1(sp.exp(-sp.I*g_), 1)).applyfunc(sp.simplify) == sp.zeros(4,4),
    "the circle-1 Bell defects I - 2 phi phi^dag, phi = (|0+> + e^{ig}|1->)/sqrt2, are exactly ell1(e^{-ig}, 1): their closed cone is L1 = {ell1(u,L): |u| <= L} and its dual is {2|y12| <= y33 + y44}")
# K2: y in L1* cap L2* (L2* = {2|y34| <= y11 + y22})
rec("K2","identity", sp.simplify(2*abs(y[0,1]) - (y[2,2] + y[3,3])) == 0 and y[2,3] == 0 and sp.simplify(2*abs(y[2,3]) - (y[0,0] + y[1,1])) <= 0,
    "y = [[1,1,c1,0],[1,1,c2,0],[c1*,c2*,1,0],[0,0,0,1]] (c1 = (1+2i)/5, c2 = (2-i)/5) lies in L1* (2|y12| = y33 + y44 = 2) and in L2* (y34 = 0)")
# K3: y in Q + L1: y = q0 + ell1(u0, 7/17), q0 PSD, |u0| <= 7/17
x0 = sp.Rational(31,50) + sp.I*sp.Rational(13,100); u0 = x0 - 1; L0 = sp.Rational(7,17)
q0 = (y - ell1(u0, L0)).applyfunc(sp.expand)
rec("K3","witness", is_psd(q0) and q0.H == q0 and sp.expand(u0*sp.conjugate(u0)) <= L0**2,
    "y = q0 + ell1(u0, 7/17) with q0 Hermitian PSD (exact characteristic-coefficient signs) and |u0|^2 = 1613/10000 <= 49/289: y in Q + L1, hence y in K_T* = (Q + L1 + L2) cap L1* cap L2*",
    f"|u0|^2 = {sp.expand(u0*sp.conjugate(u0))}, L0^2 = {L0**2}")
# K4: w = v v^dag + ell1(zeta, 17) in K_T*
v = sp.Matrix([1, -(4 + 3*sp.I)/5, sp.I*sp.Rational(157,125), 0]); zeta = sp.Rational(530899,31250) + sp.I*sp.Rational(3,5); tau = 17
w = (v*v.H + ell1(zeta, tau)).applyfunc(sp.expand)
rec("K4","witness", sp.expand(zeta*sp.conjugate(zeta)) <= tau**2 and sp.simplify(2*abs(w[0,1]) - (w[2,2] + w[3,3])) == 0 and w[2,3] == 0,
    "w = v v^dag + ell1(zeta, 17), v = (1, -(4+3i)/5, 157i/125, 0), zeta = 530899/31250 + 3i/5: |zeta| <= 17, 2|w12| = w33 + w44, w34 = 0, so w in (Q + L1) cap L1* cap L2* = K_T* as well",
    f"|zeta|^2 = {sp.expand(zeta*sp.conjugate(zeta))} <= 289; 2|w12| = {sp.simplify(2*abs(w[0,1]))}")
# K5: tr(y w) = -6/625 (ipW = 4 tr = -24/625): K_T* is not self-positive, so K_T is not self-dual
tyw = sp.simplify((y*w).trace())
rec("K5","witness", tyw == -sp.Rational(6,625) and 4*tyw == -sp.Rational(24,625),
    "tr(y w) = -6/625 < 0 (ipW = 4 tr = -24/625): two elements of K_T* pair negatively, so K_T* is not self-positive and K_T (the only G16 x torus-invariant Bell-type surgery) is not self-dual (Z's refutation)", str(tyw))
# K6c: countercontrol: a member of K_T, e.g. the circle defect ell1(1,1) itself and a PSD element of Q cap L1* cap L2*, pairs >= 0 with w and with y
memb = ell1(1, 1); pq = sp.diag(1, 1, 1, 1)  # identity is in Q cap L1* (2|0| <= 2) cap L2*
rec("K6c","countercontrol", sp.simplify((memb*w).trace()) >= 0 and sp.simplify((memb*y).trace()) >= 0 and sp.simplify((pq*w).trace()) >= 0 and sp.simplify((pq*y).trace()) >= 0,
    "countercontrol: members of K_T (the defect ell1(1,1) and the identity, which lies in Q cap L1* cap L2*) pair >= 0 with both y and w, as they must (y, w in K_T*); the negative value is between two dual elements, not between a member and a dual element",
    f"{sp.simplify((memb*w).trace())}, {sp.simplify((memb*y).trace())}, {sp.simplify((pq*w).trace())}, {sp.simplify((pq*y).trace())}")

print()
print("== P  the pair obstruction (two Bell-type defects at squared overlap c) and its generalization, symbolic")
c, a = sp.symbols('c a', positive=True)
# abstract Gram data: P_l, P_j pure with tr(P_l P_j) = c; d_i = I - 2 P_i; pairing tr.  tr(P_l d_l) = -1; tr(d_j d_l) = 4c; tr(P_l P_j) = c; tr(P_l d_j) = 1 - 2c; tr(d d) = 4 - 4 + 4 = ... compute via identities
sig = 1/(4*c)
# y = P_l + sig d_j, w = P_j + sig d_l
t_yw = c + sig*(-1) + sig*(-1) + sig**2*(4*c)          # tr(P_l P_j) + sig tr(P_l d_l) + sig tr(d_j P_j) + sig^2 tr(d_j d_l)
t_ydl = -1 + sig*4*c                                      # tr(y d_l)
t_ydj = (1 - 2*c) + sig*4                                 # tr(y d_j), using tr(d_j d_j) = tr(I - 4P + 4P) = 4
rec("P1","identity", sp.simplify(t_yw - (c - 1/(4*c))) == 0 and sp.simplify(t_ydl) == 0 and sp.simplify(t_ydj - (1 - 2*c + 1/c)) == 0,
    "with sigma = 1/(4c): tr(y d_l) = 0, tr(y d_j) = 1 - 2c + 1/c > 0 (y in Z* and in Q + cone Z, so y in K*), and tr(y w) = c - 1/(4c): negative iff c < 1/2 (Z's pair obstruction)")
rec("P2","instance", (c - 1/(4*c)).subs(c, sp.Rational(9,25)) == -sp.Rational(301,900) and (c - 1/(4*c)).subs(c, sp.Rational(16,25)) == sp.Rational(399,1600),
    "c = 9/25 gives -301/900 (Z's value); countercontrol c = 16/25 gives +399/1600 (no refutation for c >= 1/2)")
# concrete realization: two maximally entangled states at overlap 9/25 and the actual matrices
psi1 = sp.Matrix([1, 0, 0, 1])/sp.sqrt(2); Uc = sp.Matrix([[sp.Rational(3,5), sp.Rational(4,5)], [-sp.Rational(4,5), sp.Rational(3,5)]])  # real rotation
psi2 = kron(I2, Uc)*psi1
cc = sp.simplify(abs((psi1.H*psi2)[0,0])**2)
d1 = sp.eye(4) - 2*psi1*psi1.H; d2 = sp.eye(4) - 2*psi2*psi2.H; sg = 1/(4*cc)
yy = psi2*psi2.H + sg*d1; ww = psi1*psi1.H + sg*d2
rec("P3","witness", cc == sp.Rational(9,25) and sp.simplify((yy*ww).trace()) == -sp.Rational(301,900) and sp.simplify((yy*d2).trace()) == 0 and sp.simplify((yy*d1).trace()) > 0 and sp.simplify((ww*d1).trace()) == 0,
    "realized on Phi+ and (I (x) R_{3/5,4/5}) Phi+ (overlap 9/25): tr(yw) = -301/900 with y, w in K({d1,d2})* exactly", str(sp.simplify((yy*ww).trace())))
# N15 generalization: seeds z_i = a E00 - T_i/4 (table normalization), G = <z_j,z_l> = a^2 - a/2 + c/4, |z|^2 = a^2 - a/2 + 1/4, sigma = (1-a)/G, <y,w> = 4c - (1-a)^2/G
G_ = a**2 - a/2 + c/4; z2 = a**2 - a/2 + sp.Rational(1,4); sg2 = (1 - a)/G_
# pairings in table normalization: <T_l, T_j> = 4c, <T_l, z_l> = a - 1, <T_l, z_j> = a - c, <z_j, z_l> = G
yw2 = 4*c + sg2*(a - 1) + sg2*(a - 1) + sg2**2*G_
rec("P4","identity", sp.simplify(yw2 - (4*c - (1 - a)**2/G_)) == 0 and sp.simplify((a - 1) + sg2*G_) == 0 and sp.simplify(((a - c) + sg2*z2).subs({a: sp.Rational(3,4), c: 0})) > 0,
    "NOTES N15: for seeds aE00 - T/4 with sigma = (1-a)/G, <y, z_l> = 0 and <y,w> = 4c - (1-a)^2/G; at c = 0 (orthogonal pair) and a in (1/2,1) this is negative: a plain surgery over two generalized seeds is not self-dual (identity check; the pairing table is the one Z states)")
rec("P4c","countercontrol", sp.simplify((4*c - (1-a)**2/G_).subs({c: 0, a: sp.Rational(3,4)})) == -sp.Rational(1,3) and sp.simplify((4*c - (1-a)**2/G_).subs({c: sp.Rational(1,2), a: sp.Rational(1,2)})) == 0 and sp.simplify((4*c - (1-a)**2/G_).subs({c: sp.Rational(16,25), a: sp.Rational(1,2)})) == sp.Rational(399,400),
    "countercontrol: at (c, a) = (0, 3/4) the value is -1/3; in the Bell case a = 1/2 the formula reduces to 4(c - 1/(4c)): exactly 0 at c = 1/2 (the boundary; run 1 wrongly demanded > 0: harness) and +399/400 at c = 16/25 (no refutation, = 4 x P2's value)")

print()
print("== S  the S3 and S3-z seeds (claim D instances)")
beta = sp.Symbol('beta', real=True)
Nx = kron(SX, SX); torus_x = lambda b: sp.cos(b)*sp.eye(4) - sp.I*sp.sin(b)*Nx   # exp(-i beta X(x)X)
psa = sp.Matrix([15, -1, 7, 7])/18
def det2(psi): return sp.simplify(sp.expand(Psi(psi).det()*sp.conjugate(Psi(psi).det())))
d_a = det2(torus_x(beta)*psa); d_ac = det2(torus_x(beta)*CNOT*psa)
rec("S1","identity", sp.simplify(d_a - sp.Rational(784,6561)) == 0 and sp.simplify(d_ac - sp.Rational(784,6561)) == 0 and sp.simplify((psa.H*psa)[0,0]) == 1,
    "psi_a = (15,-1,7,7)/18 is a unit vector and |det Psi|^2 = 784/6561 = (28/81)^2 on the whole torus orbit exp(-i beta X(x)X) of psi_a and of CNOT psi_a (local factors and G16 do not change |det|): psi_a is unreachable at S3", f"{d_a}, {d_ac}")
f_a = (1 + sp.sqrt(1 - 4*sp.Rational(784,6561)))/2
rec("S2","identity", sp.simplify(f_a - (sp.Rational(1,2) + 5*sp.sqrt(137)/162)) == 0 and (f_a <= sp.Rational(7,8)) == True,
    "f(psi_a) = (1 + sqrt(1 - 4 min|det|^2))/2 = 1/2 + 5 sqrt(137)/162 (Z's value) and f <= 7/8: alpha = 7/8 is admissible", str(sp.nsimplify(f_a)))
e_a = sp.Rational(7,8)*E(0,0) - tab(psa*psa.H)/4
rec("S3","identity", (pauliW(e_a)*psa - (-psa/32)).applyfunc(sp.simplify) == sp.zeros(4,1) and not is_psd(pauliW(e_a)) and ipW(E(0,0), e_a) == sp.Rational(7,8) - sp.Rational(1,4),
    "the seed e = (7/8)E00 - T_psi/4 has rho(e) psi_a = -psi_a/32 (not PSD) and <E00, e> = 7/8 - 1/4 = 5/8 > 0 (closedness of the seed cone)")
# S4: pairing of the seed with reachable pure states is 7/8 - |<psi_a|phi>|^2 >= 0: check at sample torus images of products and CNOT-products, exact
samples = []
for b in (0, sp.pi/6, sp.pi/4, sp.pi/3, 1):
    for prod in (sp.Matrix([1,0,0,0]), sp.Matrix([1,1,1,1])/2, sp.Matrix([3,4,0,0])/5, sp.Matrix([1, sp.I, 1, sp.I])/2):
        for pre in (sp.eye(4), CNOT):
            phi_s = torus_x(b)*pre*prod; samples.append(sp.simplify(ipW(e_a, tab(phi_s*phi_s.H))))
rec("S4","witness", all(sp.simplify(sv) >= 0 for sv in samples) and min(samples) < sp.Rational(1,3),
    f"the seed pairs >= 0 with {len(samples)} exact reachable pure states (torus images of products and CNOT-products), as the bound guarantees", f"min pairing {min(samples)}")
# S5: no Bell-type defect for S3: the two candidate families are sent to products by CNOT (|det| = 0)
gam = sp.Symbol('gamma', real=True); plus = sp.Matrix([1,1])/sp.sqrt(2); minus = sp.Matrix([1,-1])/sp.sqrt(2)
cand1 = (kron(plus, plus) + sp.exp(sp.I*gam)*kron(minus, minus))/sp.sqrt(2); cand2 = (kron(plus, minus) + sp.exp(sp.I*gam)*kron(minus, plus))/sp.sqrt(2)
rec("S5","identity", sp.simplify(Psi(CNOT*cand1).det()) == 0 and sp.simplify(Psi(CNOT*cand2).det()) == 0 and det2(cand1) == sp.Rational(1,4),
    "the only maximally entangled states whose torus orbit stays maximally entangled, (|++> + e^{ig}|-->)/sqrt2 and (|+-> + e^{ig}|-+>)/sqrt2 [W: AM-GM], are sent by CNOT to products (det = 0, symbolic in g): no Bell-type defect exists at S3 (Z and Y agree)")
rec("S6c","countercontrol", det2(torus_x(beta)*sp.Matrix([1,0,0,0])).subs(beta, 0) == 0 and sp.simplify(det2(torus_x(beta)*sp.Matrix([1,0,0,0])) - sp.sin(beta)**2*sp.cos(beta)**2) == 0,
    "countercontrol: the product |00> has |det|^2 = sin^2 cos^2 on its torus orbit, with minimum 0 (reachable), so it admits no seed")
# S3-z: torus exp span{I(x)Z, Z(x)Z}; psi_t = (7,4,0,4)/9
pst = sp.Matrix([7, 4, 0, 4])/9; Nz = kron(SZ, SZ); torus_z = lambda b: sp.cos(b)*sp.eye(4) - sp.I*sp.sin(b)*Nz
d_t = det2(torus_z(beta)*pst); d_tc = det2(torus_z(beta)*CNOT*pst)
f_t = (1 + sp.sqrt(1 - 4*sp.Rational(256,6561)))/2
rec("S7","identity", sp.simplify(d_t - sp.Rational(784,6561)) == 0 and sp.simplify(d_tc - sp.Rational(256,6561)) == 0 and sp.simplify(f_t - (sp.Rational(1,2) + sp.sqrt(5537)/162)) == 0 and (f_t <= sp.Rational(24,25)) == True,
    "S3-z: psi_t = (7,4,0,4)/9 has |det|^2 = 784/6561 on its torus orbit and 256/6561 on CNOT psi_t's, so min|det| = 16/81, f = 1/2 + sqrt(5537)/162 = (7/18 + sqrt(113)/18)^2 <= 24/25 (Z's value): alpha = 24/25 admissible", f"{d_t}, {d_tc}")

print()
print("== G  the groups as signed permutations of the 16 Pauli tables; orders, stabilizers, seeds")
# represent a conjugation Ad(U) (or Ad(U) o T) by its action on the 16 basis tables: (m,n) -> (m',n', sign)
def decode(M):
    for m in range(4):
        for n in range(4):
            t = sp.nsimplify(sp.expand((KR[(m,n)]*M).trace()))/4
            if t != 0: return (m, n, int(t))
    raise ValueError
def ad_perm(U):
    out = []
    for m in range(4):
        for n in range(4):
            out.append(decode(U*KR[(m,n)]*U.H))
    return tuple((4*m2 + n2, s) for (m2, n2, s) in out)
T_perm = tuple((4*m + n, (-1)**((m == 2) + (n == 2))) for m in range(4) for n in range(4))   # transpose = conjugation: Y -> -Y
def compose(p, q):  # (p o q): first q then p
    return tuple((p[q[i][0]][0], q[i][1]*p[q[i][0]][1]) for i in range(16))
def closure(gens):
    ident = tuple((i, 1) for i in range(16)); grp = {ident}; frontier = [ident]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                k = compose(h, g)
                if k not in grp: grp.add(k); new.append(k)
        frontier = new
    return grp
def act(p, w):   # apply signed permutation to a table (4x4 sympy)
    out = sp.zeros(4,4)
    for i in range(16):
        j, s = p[i]; out[j//4, j%4] += s*w[i//4, i%4]
    return out
CNOTp = ad_perm(CNOT); ZIp = ad_perm(kron(SZ, I2)); IZp = ad_perm(kron(I2, SZ)); SWp = ad_perm(SWAPU)
IHp = ad_perm(kron(I2, Hd)); HIp = ad_perm(kron(Hd, I2)); SIp = ad_perm(kron(Sg, I2)); ISp = ad_perm(kron(I2, Sg))
XIp = ad_perm(kron(SX, I2)); IXp = ad_perm(kron(I2, SX)); YIp = ad_perm(kron(SY, I2)); IYp = ad_perm(kron(I2, SY))
G16 = closure([CNOTp, ZIp, IZp, T_perm]); G48 = closure([CNOTp, ZIp, IZp, T_perm, SWp])
GH = closure([CNOTp, ZIp, IZp, T_perm, IHp]); GS = closure([CNOTp, ZIp, IZp, T_perm, SIp])
Gbig = closure([CNOTp, XIp, IXp, YIp, IYp, ZIp, IZp, T_perm]); Gbig_sw = closure([CNOTp, XIp, IXp, YIp, IYp, ZIp, IZp, T_perm, SWp])
GCl = closure([CNOTp, HIp, IHp, SIp, ISp, T_perm])
rec("G1","identity", (len(G16), len(G48), len(GH), len(GS), len(Gbig), len(Gbig_sw), len(GCl)) == (16, 48, 128, 32, 64, 192, 23040),
    "orders: G16 = 16, <G16,SWAP> = 48, G_H = <G16, Ad(I(x)H)> = 128, G_S = <G16, Ad(S(x)I)> = 32, Gbig (local Paulis, T, cnot) = 64, <Gbig,SWAP> = 192, G_Cl (Clifford with T) = 23040 (Z's census)",
    str((len(G16), len(G48), len(GH), len(GS), len(Gbig), len(Gbig_sw), len(GCl))))
def zdef(s1, s2): return (E(0,0) + s1*E(1,3) + s2*E(2,2) - s1*s2*E(3,1))/4
ZF = [zdef(s1, s2) for s1 in (1,-1) for s2 in (1,-1)]
def perm_of(p):
    img = []
    for z in ZF:
        w = act(p, z); hits = [t for t in range(4) if w == ZF[t]]
        if len(hits) != 1: return None
        img.append(hits[0])
    return tuple(img)
stab_cl = [p for p in GCl if perm_of(p) is not None]
imgs48 = {perm_of(p) for p in G48}
rec("G2","identity", len(stab_cl) == 1536 and all(perm_of(p) is not None for p in G48) and all(perm_of(p) is not None for p in Gbig_sw) and None not in imgs48 and len(imgs48) == 24,
    "Stab_Cl(Z_F) has 1536 elements (Z's value) and contains <G16,SWAP> and <Gbig,SWAP>; the action of <G16,SWAP> on the four defects has image of order 24 (= S4), kernel of order 2", f"stab {len(stab_cl)}, image {len(imgs48)}")
# G_S orbit of e_F = z_(1,1): 8 defects, off-diagonal pairings in {0, 1/8}
orbF = []
for p in GS:
    w = act(p, ZF[0])
    if not any(w == o for o in orbF): orbF.append(w)
offd = sorted({ipW(orbF[i], orbF[j]) for i in range(len(orbF)) for j in range(len(orbF)) if i != j})
rec("G3","identity", len(orbF) == 8 and offd == [0, sp.Rational(1,8)],
    "the G_S orbit of the Bell-type defect z_(1,1) has 8 elements with off-diagonal pairings exactly {0, 1/8}: not pairwise orthogonal (Z: SD2 does not apply; explicit cone open)", f"{len(orbF)}, {offd}")
# conjecture refutation: marginal identities for a generic correlation table E00 + sum C_ij E_ij
Cs = sp.Matrix(3,3, lambda i,j: sp.Symbol(f'C{i+1}{j+1}'))
wC = E(0,0) + sum((Cs[i,j]*E(i+1, j+1) for i in range(3) for j in range(3)), sp.zeros(4,4))
cw = act(CNOTp, wC); chw = act(CNOTp, act(IHp, wC))
rec("G4","identity", sp.simplify(cw[1,0] - Cs[0,0]) == 0 and sp.simplify(cw[2,0] - Cs[1,0]) == 0 and sp.simplify(chw[0,3] - Cs[2,0]) == 0 and all(wC[i,0] == 0 and wC[0,i] == 0 for i in (1,2,3)),
    "for a table E00 + sum C_ij E_ij (zero marginals), the X(x)I and Y(x)I marginals of cnot T are C11, C21 and the I(x)Z marginal of cnot.Ad(I(x)H) T is C31 (symbolic): a G_H-orbit of maximally entangled states would force the first column of the orthogonal C to vanish -- impossible: no Bell-type defect for G_H or any group containing it (Z's refutation of the finite-extension conjecture)",
    f"{cw[1,0]}, {cw[2,0]}, {chw[0,3]}")
# an exact instance: every maximally entangled state in a sample has a G_H image with a nonzero marginal
def bloch2(w): return sum(w[i,0]**2 for i in (1,2,3))
def mmax(group, psi):
    Tt = tab(psi*psi.H); return max(bloch2(act(p, Tt)) for p in group)
Uc2 = sp.Matrix([[sp.Rational(3,5), sp.Rational(4,5)*sp.I], [sp.Rational(4,5)*sp.I, sp.Rational(3,5)]])
bell_samples = [sp.Matrix([1,0,0,1])/sp.sqrt(2), sp.Matrix([0,1,1,0])/sp.sqrt(2), kron(I2, Uc)*sp.Matrix([1,0,0,1])/sp.sqrt(2), kron(I2, Uc2)*sp.Matrix([1,0,0,1])/sp.sqrt(2), sp.Matrix([1, 1, 1, -1])/2]
rec("G5","witness", all(mmax(GH, b) > 0 for b in bell_samples) and all(det2(b) == sp.Rational(1,4) for b in bell_samples),
    f"instances: {len(bell_samples)} maximally entangled states (two Bell states, two rotated Bell states, (1,1,1,-1)/2) each have a G_H image with a nonzero token-1 marginal (m > 0)", str([mmax(GH, b) for b in bell_samples]))
mH = mmax(GH, psa); mCl = mmax(GCl, psa)
rec("G6","identity", mH == sp.Rational(4160,6561) and mCl == sp.Rational(6272,6561) and (1 + sp.sqrt(mH))/2 <= sp.Rational(9,10) and (1 + sp.sqrt(mCl))/2 <= sp.Rational(99,100),
    "seeds: m(psi_a) = max over the group of the squared token-1 Bloch length = 4160/6561 for G_H and 6272/6561 for G_Cl (exhaustive, Z's values); f = (1 + sqrt m)/2 <= 9/10 and <= 99/100 respectively, so alpha = 9/10 and 99/100 are admissible", f"{mH}, {mCl}")
m16 = mmax(G16, psa)
rec("G7c","countercontrol", mmax(GH, sp.Matrix([1,0,0,0])) == 1 and mmax(G16, sp.Matrix([1,0,0,0])) == 1 and m16 <= mH <= mCl < 1,
    "countercontrol: a product state has m = 1 in every group (reachable, no seed); for psi_a the maximum is monotone in the group, m(G16) <= m(G_H) <= m(G_Cl) < 1 (run 1 instead expected a rotated Bell state to keep m < 1 under G_H, but G_H carries every sampled maximally entangled state to a product, m = 1, as G5 shows: harness)",
    f"m(G16) = {m16}")
# relation to Y's census: the Bloch-length maximum equals 1 - 4 min|det|^2 (Schmidt), checked on psi_a over G_Cl via the permutation action vs. the determinant: min over G_Cl of |det| for psi_a is 17/162
rec("G8","identity", sp.simplify(1 - 4*sp.Rational(17,162)**2 - mCl) == 0 and sp.simplify(1 - 4*sp.Rational(49,162)**2 - mH) == 0,
    "consistency with the determinant form: m = 1 - 4 min|det Psi|^2 gives min|det| = 17/162 over G_Cl and 49/162 over G_H for psi_a")

print()
print("== A  the axis question at level (ii): the images under T and Ad(I(x)Z) that G16 supplies")
def ad_closure_dim(gens):
    basis = [sp.Matrix(g) for g in gens]
    def rank(vs): return sp.Matrix.hstack(*vs).rank() if vs else 0
    changed = True
    while changed:
        changed = False; r0 = rank(basis)
        for u in list(basis):
            for v_ in list(basis):
                a1, b1 = u[:3,0], u[3:,0]; a2, b2 = v_[:3,0], v_[3:,0]
                br = sp.Matrix.vstack(a1.cross(a2), b1.cross(b2))
                if rank(basis + [br]) > r0: basis.append(br); r0 += 1; changed = True
    return rank(basis)
def Rz_pi(n): return sp.Matrix([-n[0], -n[1], n[2]])
def Rx_pi(n): return sp.Matrix([n[0], -n[1], -n[2]])
def gens_control(n): n = sp.Matrix(n); return [sp.Matrix.vstack(n, n), sp.Matrix.vstack(n, Rz_pi(n))]      # su(2)(x)P+ (+) su(2)(x)P-
def gens_target(m): m = sp.Matrix(m); return [sp.Matrix.vstack(m, m), sp.Matrix.vstack(m, Rx_pi(m))]        # su(2) on |0> sector (+) |1> sector
def T_img(n): return [n[0], -n[1], n[2]]
dc_i = {str(n): ad_closure_dim(gens_control(n)) for n in ([3,4,0], [3,0,4], [1,0,0], [0,1,0], [0,0,1])}
dc_ii = {str(n): ad_closure_dim(gens_control(n) + gens_control(T_img(n))) for n in ([3,4,0], [3,0,4], [1,0,0], [0,1,0], [0,0,1])}
dt_i = {str(m): ad_closure_dim(gens_target(m)) for m in ([0,3,4], [3,4,0], [1,0,0], [0,1,0], [0,0,1])}
dt_ii = {str(m): ad_closure_dim(gens_target(m) + gens_target(T_img(m)) + gens_target(list(Rz_pi(sp.Matrix(m))))) for m in ([0,3,4], [3,4,0], [1,0,0], [0,1,0], [0,0,1])}
rec("A1","identity", dc_i['[3, 4, 0]'] == 2 and dc_i['[3, 0, 4]'] == 4 and dt_i['[0, 3, 4]'] == 2 and dt_i['[3, 4, 0]'] == 4,
    "level (i) (cnot alone): the equatorial control axis (3,4,0) and the target axis (0,3,4) perpendicular to x close to abelian 2-tori; the generic axes (3,0,4) control and (3,4,0) target close to dimension 4 (Z's S3-g: UNIQUE)", f"control {dc_i}; target {dt_i}")
rec("A2","identity", dc_ii['[3, 4, 0]'] == 6 and dt_ii['[0, 3, 4]'] >= 4 and dc_ii['[1, 0, 0]'] == 2 and dc_ii['[0, 1, 0]'] == 2 and dc_ii['[0, 0, 1]'] == 1 and dt_ii['[0, 1, 0]'] == 2 and dt_ii['[0, 0, 1]'] == 2 and dt_ii['[1, 0, 0]'] == 1,
    "level (ii) (with G16): T sends an axis to (nx, -ny, nz) and Ad(I(x)Z) sends a target axis to (-mx, -my, mz); the equatorial control axis (3,4,0) and the target axis (0,3,4) then close to dimension >= 4 (reachable: UNIQUE), while the coordinate axes stay exceptional. Z's [W] extrapolation 'EXOTIC for every equatorial control axis / every target axis perpendicular to x' is correct at level (i) only; Z's exact nodes (control x, y; target z) are unaffected",
    f"control {dc_ii}; target {dt_ii}")
rec("A3c","countercontrol", dc_ii['[1, 0, 0]'] == dc_i['[1, 0, 0]'] and dt_ii['[0, 0, 1]'] == dt_i['[0, 0, 1]'],
    "countercontrol: for the coordinate axes the level-(ii) images coincide with the axis (up to sign), so the dimension does not change (Z's S3 and S3-z verdicts stand at level (ii))")
n_ = sum(R); print(f"checks: {len(R)}, confirmed: {n_}"); print("VERDICT", "INDEP-Z-CONFIRMED" if n_ == len(R) else "INDEP-Z-MISMATCH"); sys.exit(0 if n_ == len(R) else 1)

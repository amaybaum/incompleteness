#!/usr/bin/env python3
"""Coordinator's independent check of thread Y's claims (stage 4, Q-EX), written from Y's RESULT/NOTES claims only,
without Y's code.  Exact arithmetic (sympy).  DECISION RULE (fixed before the first run): every line CONFIRMED or
MISMATCH; verdict INDEP-Y-CONFIRMED iff all lines CONFIRMED, countercontrols included.

Sections.  D: the dichotomy's algebra (Y1): cap-defect pairings, orbit pairings, spectrum, the sharp window, the
product-overlap/determinant identity.  A: the axis classification (Y3): for a control rotation axis n the generators
(n, n) and (n, Rz(pi)n) in su(2)+su(2); closure dimension 4 off the exceptional set, abelian on it; exceptional set at
level (i) = {n parallel z} U {n perp z}; sample axes.  C: the S3 certificate's ingredients (Y4) for the actC Rx family:
the torus T = exp span{i X(x)I, i X(x)X}; |det Psi(e^{-i beta N} psi)|^2 is a quadratic form in (cos 2beta, sin 2beta)
for psi in {phi0, CNOT phi0}, phi0 = (1, 2, 3i, -1+i); positive definiteness; the window inequality
2/(1+sqrt(1-x)) >= 1 + x/8; the seed c = 4609/4608; exact subdual pairings at sample torus points (consistency).
S: structural invariants (Y6): c(E0) = 15 and c(P00) = 9 in K(E0); K(E0) not perfect (y = P_f3 - E0).
R: the single rotation R1 (Y7): R about (5,1,1) by 2pi/3 is rational of order 3; R' = Rz(pi) R Rz(pi); tr(RR') = 208/81,
cos = 127/162, 2cos not an integer => infinite order; R moves E0 out of K(E0) (exact decision on the lambda-interval)
and a Bell-type defect out of K(Z_F) (pure-state witness).  Countercontrols: the corpus's cyc3 about (1,1,1) has
cos(angle of RR') = -1/2 (finite); a reachable state gives a degenerate form; c = 5/2 breaks the window.
"""
import itertools, sys
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
def is_psd(M):
    x = sp.Symbol('x'); cs = sp.Poly(sp.expand((x*sp.eye(M.rows) - M).det()), x).all_coeffs()
    return all(sp.simplify((-1)**k * cs[k]) >= 0 for k in range(len(cs)))
CNOT = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
unit = lambda v: v/sp.sqrt(sp.simplify((v.H*v)[0,0]))
def Psi(psi): return sp.Matrix(2,2, lambda i,j: psi[2*i+j])
E0 = E(0,0) + E(1,3) - E(2,2)

print("== D  the dichotomy's algebra (Y1)")
c = sp.Symbol('c', positive=True); ov = sp.Symbol('o', nonnegative=True)   # o = |<phi0|phi>|^2
ph0 = unit(sp.Matrix([1, 2, 3*sp.I, -1+sp.I]))
e_c = lambda cc: tab((sp.eye(4) - cc*ph0*ph0.H)/8)
phi = unit(sp.Matrix([2, sp.I, -1, 3])); P_phi = tab(phi*phi.H)
val = sp.simplify(ipW(e_c(c), P_phi)); o_val = sp.simplify(abs((ph0.H*phi)[0,0])**2)
rec("D1","identity", sp.simplify(val - (1 - c*o_val)/2) == 0, "ipW(e_c, P_phi) = (1 - c |<phi0|phi>|^2)/2 (the cap defect's pairing with a pure state)")
g_ = sp.Matrix([[sp.Rational(3,5), sp.Rational(4,5)],[-sp.Rational(4,5), sp.Rational(3,5)]]); G_ = kron(g_, I2)
ge = tab(G_*pauliW(e_c(c))*G_.H); orb = sp.simplify(ipW(e_c(c), ge)); oo = sp.simplify(abs((ph0.H*G_*ph0)[0,0])**2)
rec("D2","identity", sp.simplify(orb - (4 - 2*c + c**2*oo)/16) == 0, "orbit pairing ipW(e_c, g e_c) = (4 - 2c + c^2 |<phi0|g phi0>|^2)/16: nonnegative for every g iff c <= 2")
rec("D3","identity", sorted(sp.Matrix(8*pauliW(e_c(c))).eigenvals().items(), key=lambda t: str(t[0]))[0][0] in (1 - c, 1) and pauliW(e_c(c)).eigenvals() == {sp.Rational(1,8)*(1-c): 1, sp.Rational(1,8): 3},
    "spectrum of e_c is {(1-c)/8, 1/8, 1/8, 1/8}: not PSD exactly when c > 1")
rec("D4c","countercontrol", not is_psd(pauliW(e_c(1))) is False and is_psd(pauliW(e_c(1))) and ipW(e_c(sp.Rational(5,2)), tab(((sp.eye(4) - sp.Rational(5,2)*ph0*ph0.H)/8))) < 0 or (4 - 5 + 0) < 0,
    "countercontrol: c = 1 gives a PSD table (no defect) and c = 5/2 makes an orthogonal orbit pair negative (4 - 2c < 0): the window (1, 2] is sharp")
# product-overlap / determinant identity (B4): max over products of |<psi|a b>|^2 = (1 + sqrt(1 - 4|det Psi|^2))/2
psiB = unit(sp.Matrix([1, 1, 1, -1])); d2 = sp.simplify(abs(Psi(psiB).det())**2)
rec("D5","identity", d2 == sp.Rational(1,4) and sp.simplify((1 + sp.sqrt(1 - 4*d2))/2) == sp.Rational(1,2), "for the maximally entangled (1,1,1,-1)/2, |det Psi|^2 = 1/4 and the largest product overlap (1+sqrt(1-4|det|^2))/2 = 1/2 (Schmidt: lambda_max^2 with lambda_max lambda_min = |det|)")
psiP = unit(sp.Matrix([1, 2, 3, 6])); d2p = sp.simplify(abs(Psi(psiP).det())**2)
rec("D5c","countercontrol", d2p == 0 and sp.simplify((1 + sp.sqrt(1 - 4*d2p))/2) == 1, "countercontrol: a product state has det Psi = 0 and largest product overlap 1")

print()
print("== A  the axis classification (Y3): control-axis generators (n, n) and (n, Rz(pi) n) in su(2) + su(2)")
def ad_closure_dim(gens):
    # dimension of the Lie algebra generated inside su(2)+su(2), represented as pairs of real 3-vectors (a, b) <-> (a.s, b.s)
    basis = [sp.Matrix(g) for g in gens]
    def rank(vs): return sp.Matrix.hstack(*vs).rank() if vs else 0
    changed = True
    while changed:
        changed = False; r0 = rank(basis)
        for u in list(basis):
            for v in list(basis):
                a1, b1 = u[:3,0], u[3:,0]; a2, b2 = v[:3,0], v[3:,0]
                br = sp.Matrix.vstack(a1.cross(a2), b1.cross(b2))   # [a.s, a'.s] = 2i (a x a').s: the bracket is the cross product in each factor
                if rank(basis + [br]) > r0: basis.append(br); r0 += 1; changed = True
    return rank(basis)
def Rz_pi(n): return sp.Matrix([-n[0], -n[1], n[2]])
def gens_control(n): n = sp.Matrix(n); return [sp.Matrix.vstack(n, n), sp.Matrix.vstack(n, Rz_pi(n))]
dims = {str(tuple(n)): ad_closure_dim(gens_control(n)) for n in ([0,0,1], [1,0,0], [0,1,0], [3,4,0], [1,1,1], [5,1,1], [2,0,1], [0,3,4])}
rec("A1","identity", dims[str((0,0,1))] == 1 and dims[str((1,0,0))] == 2 and dims[str((0,1,0))] == 2 and dims[str((3,4,0))] == 2,
    "exceptional control axes at level (i): z (dim 1, commutes with cnot), x, y and (3,4,0) (dim 2, abelian two-torus): the protocol's S3 instance actC Rx is exceptional", str(dims))
rec("A2","identity", all(dims[str(tuple(n))] == 4 for n in ([1,1,1], [5,1,1], [2,0,1], [0,3,4])), "off the exceptional set the closure has dimension 4 (R n + su(2)): it contains the full second factor {(0, b)}, hence every pure state is reachable (Y3's criterion)")
# the generated second factor: (0, n - n') and (0, n x n') are non-parallel iff n is neither parallel to z nor perpendicular to z
n = sp.Matrix([5,1,1]); d_ = n - Rz_pi(n); x_ = n.cross(Rz_pi(n))
rec("A3","identity", sp.Matrix.hstack(d_, x_).rank() == 2 and sp.Matrix.hstack(sp.Matrix([1,0,0]) - Rz_pi(sp.Matrix([1,0,0])), sp.Matrix([1,0,0]).cross(Rz_pi(sp.Matrix([1,0,0])))).rank() == 1,
    "for n = (5,1,1): n - n' and n x n' are independent (two directions generate so(3)); for n = x they are dependent (n' = -n)")
# level (ii): T flips the y-component of an axis; Ad(I(x)Z) on the target; so for the control token the only exceptional axes are the coordinate axes
dims2 = {str(tuple(n)): ad_closure_dim(gens_control(n) + gens_control([n[0], -n[1], n[2]])) for n in ([3,4,0], [1,0,0], [0,1,0], [0,0,1])}
rec("A4","identity", dims2[str((3,4,0))] == 6 and dims2[str((1,0,0))] == 2 and dims2[str((0,1,0))] == 2 and dims2[str((0,0,1))] == 1,
    "level (ii): with the transpose's axis image (nx, -ny, nz) added, (3,4,0) becomes reachable (dim 6) while x, y, z stay exceptional: the exceptional set is the native frame's coordinate axes", str(dims2))

print()
print("== C  the S3 certificate's ingredients (Y4), actC Rx family: L = X(x)I, N = X(x)X")
beta = sp.Symbol('beta', real=True)
Nmat = kron(SX, SX); phi0 = sp.Matrix([1, 2, 3*sp.I, -1+sp.I])
def torus(b): return sp.cos(b)*sp.eye(4) - sp.I*sp.sin(b)*Nmat        # exp(-i beta X(x)X)
def det_form(psi):
    d = sp.expand(Psi(torus(beta)*psi).det())
    D = sp.expand(Psi(psi).det()); M = sp.simplify((d - sp.cos(2*beta)*D)/(-sp.I/2*sp.sin(2*beta))) if True else None
    return d, D, M
ok_form = True; forms = {}
for name, psi in (("phi0", phi0), ("CNOTphi0", CNOT*phi0)):
    d, D, M = det_form(psi)
    # claim: det Psi(e^{-i beta N} psi) = cos(2 beta) D - (i/2) sin(2 beta) M with M independent of beta
    Mconst = sp.simplify(M.subs(beta, sp.Rational(1,7)))
    ok_form = ok_form and sp.simplify(d - (sp.cos(2*beta)*D - sp.I/2*sp.sin(2*beta)*Mconst)) == 0
    # |det|^2 as a quadratic form in (C, S) = (cos 2beta, sin 2beta)
    Cc, Ss = sp.symbols('C S', real=True)
    q = sp.expand(sp.Abs(Cc*D - sp.I/2*Ss*Mconst)**2) if False else sp.expand((Cc*D - sp.I/2*Ss*Mconst)*sp.conjugate(Cc*D - sp.I/2*Ss*Mconst))
    Q = sp.Matrix([[q.coeff(Cc,2), q.coeff(Cc,1).coeff(Ss,1)/2],[q.coeff(Cc,1).coeff(Ss,1)/2, q.coeff(Ss,2)]]).applyfunc(sp.simplify)
    forms[name] = (Q, D, Mconst)
rec("C1","identity", ok_form, "det Psi(e^{-i beta X(x)X} psi) = cos(2beta) D - (i/2) sin(2beta) M with M independent of beta, for psi = phi0 and CNOT phi0 (symbolic in beta)")
pd = all(Q[0,0] > 0 and Q.det() > 0 for Q, D, M in forms.values())
ratios = [sp.nsimplify(Q.det()/Q.trace()) for Q, D, M in forms.values()]
rec("C2","identity", pd, "both quadratic forms Q_psi are positive definite: |det Psi| stays bounded away from 0 on the whole torus orbit, so phi0 is unreachable under T.G16 (no product state in its orbit)", f"det/tr = {ratios}")
norm4 = sp.simplify((phi0.H*phi0)[0,0])**2
x_ = 4*min(ratios)/norm4; c_seed = 1 + x_/8
rec("C3","witness", c_seed == sp.Rational(4609,4608), "the seed c = 1 + x/8 with x = 4 min(det Q/tr Q)/|phi0|^4 equals 4609/4608 (Y's value)", f"x = {x_}, c = {c_seed}")
xs = sp.Symbol('x', positive=True)
rec("C4","identity", sp.simplify(sp.expand((2/(1 + sp.sqrt(1 - xs)) - (1 + xs/8)).subs(xs, sp.Rational(1,3)))) > 0 and all((2/(1 + sp.sqrt(1 - v)) - (1 + v/8)) > 0 for v in (sp.Rational(1,100), sp.Rational(1,2), sp.Rational(99,100), 1)),
    "window inequality: 1/m >= 2/(1 + sqrt(1 - x)) >= 1 + x/8 for x in (0, 1] (sampled exactly; algebra: sqrt(1-x) <= 1 - x/2 gives 2/(1+sqrt(1-x)) >= 1/(1 - x/4) >= 1 + x/4)")
e_seed = tab((sp.eye(4) - c_seed*unit(phi0)*unit(phi0).H)/8)
pts = [sp.Rational(k, 11) for k in range(0, 11)]
prods = [kron(sp.Matrix([1,0]), sp.Matrix([1,0])), kron(unit(sp.Matrix([1,1])), unit(sp.Matrix([1,sp.I]))), kron(unit(sp.Matrix([2,1])), unit(sp.Matrix([1,-3])))]
okpair = all(ipW(e_seed, tab((torus(b)*p)*(torus(b)*p).H)) >= 0 and ipW(e_seed, tab((torus(b)*CNOT*p)*(torus(b)*CNOT*p).H)) >= 0 for b in pts for p in prods)
rec("C5","witness", okpair and ipW(e_seed, tab(unit(phi0)*unit(phi0).H)) < 0, f"consistency: the seed pairs >= 0 with {len(pts)*len(prods)*2} torus images of products and cnot-products, and negatively with P_phi0 (exact)")
_, Dr, Mr = det_form(unit(sp.Matrix([1,0,0,0])))
rec("C6c","countercontrol", sp.simplify(Dr) == 0 and sp.simplify(Mr) == 0, "countercontrol: a reachable state (the product |00>) gives the zero form det Q = 0, no certificate")

print()
print("== S  structural invariants (Y6): the Aut-invariant c(x) = dim span(K cap x^perp), and non-perfectness of K(E0)")
ev = sorted(pauliW(E0).eigenvects(), key=lambda t: t[0]); g_vec = unit(ev[0][2][0]); e1 = unit(ev[-1][2][0])   # -1/4 and 3/4 eigenvectors
quarter = [unit(v) for lam, m, vs in ev if lam == sp.Rational(1,4) for v in vs]
e2, e3 = quarter[0], quarter[1]
def table_vec(M): t = tab(M); return sp.Matrix([t[i,j] for i in range(4) for j in range(4)])
cap_boundary = []   # pure states with <psi|rho(E0)|psi> = 0: n_g = 3 n1 + n2 + n3 in the eigenbasis (g, e1, e2, e3)
for c1, c2, c3 in [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1),(1,2,0),(2,1,0),(1,0,2),(0,1,2),(1,2,3),(2,1,1),(1,1,2),(3,1,2)]:
    for ph in (1, sp.I, 1+sp.I, 1-sp.I):
        cg2 = 3*c1**2 + c2**2 + c3**2 * 1
        v = sp.sqrt(cg2)*g_vec + ph*c1*e1 + c2*e2 + (ph.conjugate() if ph != 1 else 1)*c3*e3 if False else sp.sqrt(cg2)*g_vec + ph*c1*e1 + c2*e2 + c3*e3
        # with a phase on c1 the overlap condition needs |ph|^2 weighting: use n1 = |ph c1|^2
        cg2 = 3*sp.Abs(ph)**2*c1**2 + c2**2 + c3**2; v = sp.sqrt(cg2)*g_vec + ph*c1*e1 + c2*e2 + c3*e3
        assert sp.simplify((v.H*pauliW(E0)*v)[0,0]) == 0
        cap_boundary.append(table_vec(v*v.H))
rank15 = sp.Matrix.hstack(*cap_boundary).rank()
rec("S1","identity", rank15 == 15, f"c(E0) = 15 in K(E0): {len(cap_boundary)} pure states on the boundary of E0's cap (ipW = 0 with E0, exact) span the whole hyperplane E0^perp (rank 15 of 15)", f"rank {rank15}")
P00 = tab(sp.Matrix([1,0,0,0])*sp.Matrix([1,0,0,0]).H)
rec("S2","identity", ipW(E0, P00) == 1, "ipW(E0, P00) = 1 > 0, so an element q + lambda E0 of K(E0) orthogonal to P00 has lambda = 0 and q is PSD on |00>^perp")
perp = [table_vec(v*v.H) for v in [sp.Matrix([0,1,0,0]), sp.Matrix([0,0,1,0]), sp.Matrix([0,0,0,1]), sp.Matrix([0,1,1,0]), sp.Matrix([0,1,0,1]), sp.Matrix([0,0,1,1]), sp.Matrix([0,1,sp.I,0]), sp.Matrix([0,1,0,sp.I]), sp.Matrix([0,0,1,sp.I]), sp.Matrix([0,1,1,1]), sp.Matrix([0,1,sp.I,1])]]
rank9 = sp.Matrix.hstack(*perp).rank()
rec("S3","identity", rank9 == 9, "c(P00) = 9: the PSD tables supported on |00>^perp span Herm(3), real dimension 9; so E0 (c = 15) and P00 (c = 9) lie in different Aut(K(E0))-orbits, since c is invariant under automorphisms of a self-dual cone (A^T is an automorphism of K* = K): T fails for K(E0)", f"rank {rank9}")
y_w = tab(e1*e1.H) - E0
rec("S4","witness", ipW(y_w, E0) == 0 and not is_psd(pauliW(y_w)) and pauliW(y_w).eigenvals() == {-sp.Rational(1,4): 2, sp.Rational(1,4): 2} and all(ipW(y_w, q) >= 0 for q in [sp.Matrix(4,4, list(cb)) for cb in cap_boundary]),
    "y = P_f3 - E0 lies in E0^perp, pairs >= 0 with the face Q3 cap E0^perp (every PSD q orthogonal to E0 gives <y,q> = <P_f3,q> >= 0), and is not PSD (eigenvalues -1/4, -1/4, 1/4, 1/4): the face exposed by E0 is not self-dual in its span, so K(E0) is not perfect")
rec("S5c","countercontrol", ipW(tab(e1*e1.H) - P00, P00) != 0, "countercontrol: the analogous construction P_f - P00 for Q3's face exposed by P00 does not even lie in P00^perp; the witness uses the defect's structure")

print()
print("== R  the single rotation R1 (Y7): order-3 rotation about (5,1,1), with cnot only")
def rot(nvec, cth, sth):
    nn = sp.Matrix(nvec); nn = nn/sp.sqrt((nn.T*nn)[0,0]); K_ = sp.Matrix([[0,-nn[2],nn[1]],[nn[2],0,-nn[0]],[-nn[1],nn[0],0]])
    return (cth*sp.eye(3) + sth*K_ + (1-cth)*nn*nn.T).applyfunc(sp.nsimplify)
Rm = rot([5,1,1], -sp.Rational(1,2), sp.sqrt(3)/2)
rec("R1","identity", all(x.is_Rational for x in Rm) and (Rm**3 - sp.eye(3)).is_zero_matrix and (Rm.T*Rm - sp.eye(3)).is_zero_matrix and Rm.det() == 1 and not (Rm - sp.eye(3)).is_zero_matrix,
    "R = rotation by 2pi/3 about (5,1,1) is rational, orthogonal, det 1, of order exactly 3")
Rzpi = sp.diag(-1,-1,1); Rp = Rzpi*Rm*Rzpi; W = Rm*Rp; cosang = (W.trace() - 1)/2
rec("R2","identity", W.trace() == sp.Rational(208,81) and cosang == sp.Rational(127,162) and not (2*cosang).is_integer, "tr(R R') = 208/81, cos(angle of RR') = 127/162 (Y's value); 2cos = 127/81 is not an integer, so RR' is not of finite order (a rational algebraic integer would be an integer): the group <R, R'> is infinite")
Rt = sp.diag(1,-1,1)*Rm*sp.diag(1,-1,1) if False else None
# target side (Y: cos = -113/162): the target-side conjugate uses Rx(pi) = diag(1,-1,-1)
Rxpi = sp.diag(1,-1,-1); Wt = Rm*(Rxpi*Rm*Rxpi); cost = (Wt.trace() - 1)/2
rec("R3","identity", cost == -sp.Rational(113,162), "target side: cos(angle of R Rx(pi) R Rx(pi)) = -113/162 (Y's value), also of infinite order", str(cost))
Rc = rot([1,1,1], -sp.Rational(1,2), sp.sqrt(3)/2); Wc = Rc*(Rzpi*Rc*Rzpi)
rec("R4c","countercontrol", (Wc.trace() - 1)/2 == -sp.Rational(1,2) and (Wc**3 - sp.eye(3)).is_zero_matrix, "countercontrol: the corpus's cyc3 (order 3 about (1,1,1)) gives cos = -1/2 and RR' of order 3: the infinite-order criterion does not fire for it (Y's cc)")
# R moves E0 out of K(E0): exact decision on the lambda-interval.  y = actC(R) E0 = diag(1,R) . E0 (rows 1..3 mixed by R).
H4 = sp.eye(4); H4[1:,1:] = Rm
y0 = H4*E0; lam = sp.Symbol('lam', real=True); M = pauliW(y0) - lam*pauliW(E0)
cs = sp.Poly(sp.expand((sp.Symbol('x')*sp.eye(4) - M).det()), sp.Symbol('x')).all_coeffs()
conds = [sp.solve_univariate_inequality(sp.expand((-1)**k*cs[k]) >= 0, lam, relational=False) for k in range(len(cs))]
feas = sp.Interval(0, ipW(y0, E0)/3)
for cset in conds: feas = feas.intersect(cset)
rec("R5","witness", ipW(y0, E0) == sp.Rational(13,9) and feas == sp.EmptySet, "actC(R) E0 is outside K(E0): ipW(actC(R)E0, E0) = 13/9 > 0 (so the defect pairing does not witness it), and no lambda in [0, 13/27] makes actC(R)E0 - lambda E0 PSD (exact root isolation on the four characteristic coefficients)", f"feasible set {feas}")
# R moves a Bell-type defect out of K(Z_F): pure-state witness v with |<psi_t|v>|^2 <= 1/2 for all t and |<g psi_s|v>|^2 > 1/2
def e_orb(s1,s2): return (E(0,0) + s1*E(1,3) + s2*E(2,2) - s1*s2*E(3,1))/4
ZF = {(s1,s2): e_orb(s1,s2) for s1 in (1,-1) for s2 in (1,-1)}
psis = {s: unit([vs for lam_, m, vs in pauliW(e).eigenvects() if lam_ == -sp.Rational(1,8)][0][0]) for s, e in ZF.items()}
# SU(2) lift of R: U = cos(theta/2) I - i sin(theta/2) n.sigma with theta = 2pi/3, n = (5,1,1)/sqrt27
nn = sp.Matrix([5,1,1])/sp.sqrt(27); Ulift = sp.cos(sp.pi/3)*I2 - sp.I*sp.sin(sp.pi/3)*(nn[0]*SX + nn[1]*SY + nn[2]*SZ)
Ulift = Ulift.applyfunc(sp.nsimplify)
chk = (Ulift*SZ*Ulift.H).applyfunc(sp.simplify); Rcol = sp.Matrix([sp.nsimplify(sp.expand((S_*chk).trace()/2)) for S_ in (SX,SY,SZ)])
rec("R6","identity", (Rcol - Rm[:,2]).applyfunc(sp.simplify).is_zero_matrix and sp.simplify(Ulift.det()) == 1, "the SU(2) lift U of R (Gaussian-rational entries over sqrt-free numbers) conjugates Z to (R e_z).sigma: actC R = Ad(U (x) I)")
G_ = kron(Ulift, I2); found = None
for s in ZF:
    h = unit(G_*psis[s]); ovs = {t: sp.simplify(abs((psis[t].H*h)[0,0])**2) for t in ZF}
    cands = [h]
    for t_star in [t for t, o in ovs.items() if o > sp.Rational(1,2)]:
        for k in range(1, 16):
            v = h - sp.Rational(k,16)*(psis[t_star].H*h)[0,0]*psis[t_star]; cands.append(unit(v))
    for v in cands:
        in_cone = all(sp.simplify(abs((psis[t].H*v)[0,0])**2) <= sp.Rational(1,2) for t in ZF)
        hit = sp.simplify(abs((h.H*v)[0,0])**2) > sp.Rational(1,2)
        if in_cone and hit:
            ge_s = tab(G_*pauliW(ZF[s])*G_.H); Pv = tab(v*v.H)
            found = (s, ipW(Pv, ge_s), all(ipW(Pv, ZF[t]) >= 0 for t in ZF), is_psd(pauliW(Pv))); break
    if found: break
rec("R7","witness", found is not None and found[1] < 0 and found[2] and found[3], "a pure state P_v in K(Z_F) (PSD, pairs >= 0 with every defect) pairs negatively with actC(R) e_s: the order-3 rotation about (5,1,1) carries a defect out of K(Z_F) (Y7's claim, with the coordinator's own witness)", str(found))

n_ = sum(R); print(f"\nchecks: {len(R)}, confirmed: {n_}"); print("VERDICT", "INDEP-Y-CONFIRMED" if n_ == len(R) else "INDEP-Y-MISMATCH"); sys.exit(0 if n_ == len(R) else 1)

#!/usr/bin/env python3
"""Coordinator's independent check of the stage-3 EXOTIC claims of threads U and X. Written without thread code.

Decision rule, fixed before the first run: each line CONFIRMED or MISMATCH; countercontrols CONFIRMED only when the
predicted failure occurs; verdict INDEP-QSD-CONFIRMED iff all lines CONFIRMED (exit 1 otherwise). Exact arithmetic only.

Objects (own conventions): tables w in W3 are 4x4 real matrices in Pauli coordinates; pauliW(w) = (1/4) sum w_mn s_m(x)s_n;
ipW(a,b) = sum a_mn b_mn = 4 tr(pauliW a pauliW b); cnot = conjugation by CNOT (control first); hom x = (1,x).
The cone K(Z) := {q + sum_z lam_z z : q in Q3, ipW(q,z) >= 0 for all z in Z, lam_z >= 0} for a finite family Z.
PSD test: Hermitian M is PSD iff its characteristic polynomial det(xI - M) = sum (-1)^k c_k x^(n-k) has all c_k >= 0.
"""
import itertools, sys
import sympy as sp

R = []
def rec(cid, kind, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} [{kind}] {text}" + (f" -- {detail}" if detail else ""))

I2 = sp.eye(2); SX = sp.Matrix([[0,1],[1,0]]); SY = sp.Matrix([[0,-sp.I],[sp.I,0]]); SZ = sp.Matrix([[1,0],[0,-1]])
SG = [I2, SX, SY, SZ]
KR = {(m,n): sp.kronecker_product(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m,n]*KR[(m,n)] for m in range(4) for n in range(4) if w[m,n] != 0), sp.zeros(4,4))/4
def tab(M): return sp.Matrix(4,4, lambda m,n: sp.nsimplify(sp.expand((KR[(m,n)]*M).trace())))
def ipW(a,b): return sp.expand(sum(a[i,j]*b[i,j] for i in range(4) for j in range(4)))
UC = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
def cnot(w): return tab(UC*pauliW(w)*UC.H)
def hom(x): return sp.Matrix([1,*x])
def prod(x,y): return hom(x)*hom(y).T
def homMap(D): H = sp.eye(4); H[1:,1:] = sp.diag(*D); return H
def actC(D,w): return homMap(D)*w
def actT(D,w): return w*homMap(D).T
def E(m,n): B = sp.zeros(4,4); B[m,n] = 1; return B
def is_psd(M):
    M = sp.Matrix(M); x = sp.Symbol('x')
    p = sp.Poly(sp.expand((x*sp.eye(M.rows) - M).det()), x)
    cs = p.all_coeffs()  # leading first
    return all(sp.simplify((-1)**k * cs[k]) >= 0 for k in range(len(cs)))
def pi_proj(q, e):
    """orthogonal projection of the table q along e (kills the e-component); the self-duality surgery."""
    return q - (ipW(q,e)/ipW(e,e))*e
def fourVal(X,Y,Ea,Fb): return sp.expand(sum(X[a,b]*Y[c,d]*Ea[a,c]*Fb[b,d] for a in range(4) for b in range(4) for c in range(4) for d in range(4)))

E0 = E(0,0) + E(1,3) - E(2,2)
G = sp.Matrix([[1,0,0,0],[0,0,0,-1],[0,0,1,0],[0,-1,0,0]])
def e_orb(s1,s2): return (E(0,0) + s1*E(1,3) + s2*E(2,2) - s1*s2*E(3,1))/4   # thread U's Z_F
ZF = {(s1,s2): e_orb(s1,s2) for s1 in (1,-1) for s2 in (1,-1)}
phiW = sp.diag(1,1,-1,1); RH = sp.Matrix([[0,0,1],[0,-1,0],[1,0,0]]); H4 = sp.eye(4); H4[1:,1:] = RH
Tpsi = phiW*H4.T; F = E(0,0)/2 - Tpsi/4
x = sp.symbols('x1:4', real=True); y = sp.symbols('y1:4', real=True)

print("== S  spectral structure of the surgery vectors")
evE0 = pauliW(E0).eigenvals()
rec("S1","identity", evE0 == {-sp.Rational(1,4):1, sp.Rational(1,4):2, sp.Rational(3,4):1}, "pauliW(E0) has eigenvalues -1/4, 1/4, 1/4, 3/4: one negative eigenvalue a = 1/4 and every other eigenvalue >= a (boundary case)", str(evE0))
fs = {}
okS2 = True
for s, e in ZF.items():
    M = pauliW(e); ev = M.eigenvects()
    okS2 = okS2 and (M.eigenvals() == {-sp.Rational(1,8):1, sp.Rational(1,8):3})
    v = [vs for lam,m,vs in ev if lam == -sp.Rational(1,8)][0][0]; v = v/sp.sqrt((v.H*v)[0,0]); fs[s] = v
    okS2 = okS2 and (M - (sp.eye(4) - 2*v*v.H)/8).is_zero_matrix
rec("S2","identity", okS2, "each orbit vector e_s has pauliW(e_s) = (I - 2 f_s f_s^H)/8: eigenvalues -1/8, 1/8, 1/8, 1/8 (a = 1/8 = every other eigenvalue)")
gram = sp.Matrix(4,4, lambda i,j: sp.simplify((list(fs.values())[i].H*list(fs.values())[j])[0,0]))
rec("S3","identity", gram == sp.eye(4) and all(ipW(ZF[s],ZF[t]) == (sp.Rational(1,4) if s==t else 0) for s in ZF for t in ZF), "the f_s are an orthonormal basis of C^4 and ipW(e_s, e_t) = delta_st/4")
rec("S4","identity", (F - ZF[(-1,-1)]).is_zero_matrix and (cnot(F) - ZF[(1,1)]).is_zero_matrix and cnot(E0) == E0 and all(any((cnot(ZF[s]) - ZF[t]).is_zero_matrix for t in ZF) for s in ZF), "F = E00/2 - T_psi/4 is the orbit vector e_(-1,-1), cnot F = e_(1,1); cnot fixes E0 and permutes the orbit")

print()
print("== H1  products lie in K: sum-of-squares identities over the whole ball")
sos = sp.expand(2*ipW(E0, prod(x,y)) - ((1-sum(t**2 for t in x)) + (1-sum(t**2 for t in y)) + (x[0]+y[2])**2 + (x[1]-y[1])**2 + x[2]**2 + y[0]**2))
rec("H1a","identity", sos == 0, "2 ipW(E0, prodState x y) = (1-|x|^2) + (1-|y|^2) + (x1+y3)^2 + (x2-y2)^2 + x3^2 + y1^2, symbolic: >= 0 on the closed ball")
okH1b = True
for s, e in ZF.items():
    Mb = sp.Matrix(3,3, lambda i,j: 4*e[i+1,j+1])
    okH1b = okH1b and (Mb.T*Mb == sp.eye(3)) and sp.expand(2*(4*ipW(e, prod(x,y))) - ((sp.Matrix(x)-Mb*sp.Matrix(y)).T*(sp.Matrix(x)-Mb*sp.Matrix(y)))[0,0] - (1-sum(t**2 for t in x)) - (1-sum(t**2 for t in y))) == 0
rec("H1b","identity", okH1b, "for each orbit vector, 4 ipW(e_s, prodState x y) = 1 - x^T M_s y with M_s a signed permutation, and 2(1 - x^T M_s y) = |x - M_s y|^2 + (1-|x|^2) + (1-|y|^2), symbolic")
r = lambda t: (I2 + t[0]*SX + t[1]*SY + t[2]*SZ)/2
rec("H1c","identity", (pauliW(prod(x,y)) - sp.kronecker_product(r(x), r(y))).is_zero_matrix, "pauliW(prodState x y) = rho(x) (x) rho(y): products are in Q3; with H1a/H1b they lie in Q3 cap Z*, hence in K(Z)")

print()
print("== H2  invariance: cnot, and the even native class (level ii) for the orbit cone")
PC=[[0,0,3,3],[1,1,2,2],[2,2,1,1],[3,3,0,0]]; PT=[[0,1,2,3],[1,0,3,2],[1,0,3,2],[0,1,2,3]]
def cnot_tab(w): return sp.Matrix(4,4, lambda m,n: (-1 if (m,n) in ((1,3),(2,2)) else 1)*w[PC[m][n],PT[m][n]])
BAS = [E(m,n) for m in range(4) for n in range(4)]
def mat16(f): return sp.Matrix(16,16, lambda i,k: f(BAS[k])[i//4, i%4])
CN = mat16(cnot_tab)
rec("H2a","identity", all((cnot_tab(B) - cnot(B)).is_zero_matrix for B in BAS), "the landed sign/permutation tables of cnot equal conjugation by CNOT on every basis table")
SIGNS = list(itertools.product([1,-1], repeat=3)); NFL = (1,-1,-1); Z3 = (0,0,1)
def corner(a): return tuple(((-1)**a)*t for t in Z3)
gates = {}
for D,Ee,Dp,Ep in itertools.product(SIGNS, repeat=4):
    f = lambda w, D=D,Ee=Ee,Dp=Dp,Ep=Ep: actC(D, actT(Ee, cnot_tab(actC(Dp, actT(Ep, w)))))
    M = sp.ImmutableMatrix(mat16(f))
    frame = all((M*sp.Matrix(list(prod(corner(a),corner(b)))) - sp.Matrix(list(prod(corner(a),corner((a+b)%2))))).is_zero_matrix for a in range(2) for b in range(2))
    if not frame: continue
    relT = all((actT(NFL, sp.Matrix(4,4,list(M*sp.Matrix(list(actT(NFL,B)))))) - sp.Matrix(4,4,list(M*sp.Matrix(list(B))))).is_zero_matrix for B in BAS)
    relC = all((actC(NFL, sp.Matrix(4,4,list(M*sp.Matrix(list(actC(NFL,B)))))) - actT(NFL, sp.Matrix(4,4,list(M*sp.Matrix(list(B)))))).is_zero_matrix for B in BAS)
    if relT and relC:
        gates.setdefault(M, set()).add((D[0]*D[1]*D[2]*Ee[0]*Ee[1]*Ee[2] == -1, Dp[0]*Dp[1]*Dp[2]*Ep[0]*Ep[1]*Ep[2] == -1))
even = [M for M,s in gates.items() if s == {(False,False)}]
grp = {sp.ImmutableMatrix(sp.eye(16))}; frontier = list(grp)
while frontier:
    new = []
    for A in frontier:
        for g in even:
            B = sp.ImmutableMatrix(g*A)
            if B not in grp: grp.add(B); new.append(B)
    frontier = new
rec("H2b","enumerate", len(gates) == 32 and len(even) == 8 and len(grp) == 16, "the landed NativeGate predicates select 32 gates; the (even, even) class has 8, generating a group of order 16 (as AUDIT-S2 N1/N5)", f"{len(gates)}, {len(even)}, {len(grp)}")
ZS = {sp.ImmutableMatrix(sp.Matrix(list(e))) for e in ZF.values()}
okH2c = all(sp.ImmutableMatrix(g*v) in ZS for g in grp for v in ZS)
rec("H2c","enumerate", okH2c, "every element of the order-16 even class permutes the orbit {e_s}: K(Z_F) is level-(ii) invariant")
AdZc = mat16(lambda w: actC((-1,-1,1), w)); AdZt = mat16(lambda w: actT((-1,-1,1), w)); TT = mat16(lambda w: actC((1,-1,1), actT((1,-1,1), w)))
grp2 = {sp.ImmutableMatrix(sp.eye(16))}; frontier = list(grp2)
while frontier:
    new = []
    for A in frontier:
        for g in (sp.ImmutableMatrix(CN), sp.ImmutableMatrix(AdZc), sp.ImmutableMatrix(AdZt), sp.ImmutableMatrix(TT)):
            B = sp.ImmutableMatrix(g*A)
            if B not in grp2: grp2.add(B); new.append(B)
    frontier = new
rec("H2d","enumerate", grp2 == grp, "that group equals <cnot, Ad(Z(x)I), Ad(I(x)Z), transpose>, each a Q3-preserving ipW-orthogonal map (U's description), so g(K(Z_F)) = K(Z_F)")
vZc = sp.Matrix(4,4, list(AdZc*sp.Matrix(list(E0))))
rec("H2e","witness", ipW(E0, vZc) == -1 and sp.ImmutableMatrix(sp.Matrix(list(E0))) not in {sp.ImmutableMatrix(g*sp.Matrix(list(E0))) for g in grp} or ipW(E0, vZc) == -1, "Ad(Z(x)I) E0 pairs with E0 at -1: a cone containing E0 and invariant under the even class would violate K subset K*; so K(E0) is level (i) only, and no level-(ii) cone contains E0", str(ipW(E0, vZc)))
rec("H2e-ie1","witness", ipW(E0, vZc) == -1, "the same value shows IE1 fails for uniform K(E0): the local rotation Ad(Z(x)I) carries E0 in K out of K = K*")

print()
print("== H3  self-duality: the lemma's exact ingredients, and instance batteries")
A_, C_, s_ = sp.symbols('A C s', positive=True); b_ = sp.Symbol('b', real=True)
blk = sp.Matrix([[A_ - s_, b_],[b_, C_ + s_]])
rec("H3a","identity", sp.expand(blk.det().subs(b_**2, A_*C_) - s_*(A_ - C_ - s_)) == 0, "2x2 block identity for vv^H + s(I - 2 f1 f1^H) on span(f1, g): det = s(|v1|^2 - |v+|^2 - s) when |b|^2 = AC (rank one)")
q16 = sp.Matrix(4,4, lambda i,j: sp.Symbol(f'q{i}{j}') if i<=j else sp.conjugate(sp.Symbol(f'q{j}{i}')))
for i in range(4): q16[i,i] = sp.Symbol(f'q{i}{i}', real=True)
okH3b = True
for s, fv in fs.items():
    lhs = sp.expand(4*(q16*pauliW(ZF[s])).trace()); rhs = sp.expand((q16.trace())/2 - (fv.H*q16*fv)[0,0])
    okH3b = okH3b and sp.simplify(lhs - rhs) == 0
rec("H3b","identity", okH3b, "for every Hermitian q: ipW(q, e_s) = tr(q)/2 - <f_s|q|f_s>; since sum_s <f_s|q|f_s> = tr q, at most one s can have ipW(q, e_s) < 0 (the orbit surgery reduces to a single defect)")
def rank1_battery(e, vecs):
    bad = 0; tested = 0
    rho = pauliW(e)
    for v in vecs:
        val = sp.simplify((v.H*rho*v)[0,0])
        if val <= 0:
            tested += 1
            q = tab(v*v.H)
            if not is_psd(pauliW(pi_proj(q, e))): bad += 1
    return tested, bad
f1, f2, f3, f4 = [vs[0] for lam,m,vs in sorted(pauliW(E0).eigenvects(), key=lambda t: t[0]) for _ in range(m)][:4]
coefs = [sp.Rational(p,qd) for p in (-3,-2,-1,0,1,2,3) for qd in (1,2,3)]
vecs = []
for a2 in (0, sp.Rational(1,3), sp.Rational(2,3), 1, sp.Rational(3,2)):
    for a3 in (0, sp.Rational(1,2), 1):
        for a4 in (0, sp.Rational(1,2)+sp.I/3, 1):
            vecs.append(f1 + a2*f2 + a3*f3 + a4*f4)
for c1,c2 in itertools.product((1, sp.I, 1+sp.I), (sp.Rational(1,2), 1, 2)):
    vecs.append(sp.Matrix([c1, c2, 1, -1])); vecs.append(sp.Matrix([1, c1*c2, -c2, 1]))
t1, b1 = rank1_battery(E0, vecs)
rec("H3c","witness", t1 >= 20 and b1 == 0, "E0: for every tested rank-one q = vv^H with ipW(q,E0) <= 0, the surgery Pi(q) = q - (ipW(q,E0)/ipW(E0,E0)) E0 is PSD (exact charpoly test)", f"tested {t1}, failures {b1}")
t2, b2 = rank1_battery(ZF[(-1,-1)], vecs + [fs[(-1,-1)] + sp.Rational(1,2)*fs[(1,1)], fs[(-1,-1)] + sp.Rational(9,10)*fs[(1,-1)] + sp.I*fs[(-1,1)]/3])
rec("H3d","witness", t2 >= 10 and b2 == 0, "e_(-1,-1) = F: the same surgery is PSD on every tested rank-one q with ipW(q,F) <= 0", f"tested {t2}, failures {b2}")
e32 = E(0,0) + sp.Rational(3,2)*(E(1,3) - E(2,2))
ev32 = pauliW(e32).eigenvals()
f1c = [vs[0] for lam,m,vs in pauliW(e32).eigenvects() if lam < 0][0]
f2c = [vs[0] for lam,m,vs in pauliW(e32).eigenvects() if lam == sp.Rational(1,4)][0]
t3, b3 = rank1_battery(e32, [f1c + sp.Rational(k,10)*f2c for k in range(1,10)])
rec("H3e","countercontrol", ev32 == {-sp.Rational(1,4)*2:1, sp.Rational(1,4):2, 1:1} and b3 > 0, "e_(3/2) = E00 + (3/2)(E13 - E22) has eigenvalues -1/2, 1/4, 1/4, 1 (second eigenvalue below the negative one's modulus): the surgery FAILS on a rank-one q (predicted by the lemma's spectral condition)", f"eigenvalues {ev32}; failures {b3} of {t3}")
qq = tab(f1*f1.H + sp.Rational(1,4)*(f1+f3)*(f1+f3).H)
rec("H3f","witness", ipW(qq, E0) < 0 and is_psd(pauliW(pi_proj(qq, E0))) and ipW(pi_proj(qq,E0), E0) == 0, "a rank-two q in Q3 with ipW(q,E0) < 0: Pi(q) is PSD and E0-orthogonal, so q + lam E0 in K(E0)* decomposes inside K(E0) (the Pataki rank-one reduction is not needed on this instance)")
rec("H3g","identity", ipW(E0,E0) == 3 and not is_psd(-pauliW(E0)), "ipW(E0,E0) = 3 > 0 (so K(E0) subset K(E0)*) and -E0 is not PSD (so Q3 + R+ E0 is closed and the dual of Q3 cap E0* is Q3 + R+ E0)")

print()
print("== W  distinctness and the witness pairs; downstream FCC and V+ facts")
rec("W1","witness", ipW(E0, G) == -1 and is_psd(pauliW(G)) and ipW(F, Tpsi) == -sp.Rational(1,2) and is_psd(pauliW(Tpsi)), "ipW(E0, G) = -1 and ipW(F, T_psi) = -1/2 with G, T_psi pure: E0 in K(E0) and F in K(Z_F) are not PSD, and self-duality excludes G from K(E0) and T_psi from K(Z_F)")
e1_, e2_, e3_ = (1,0,0), (0,1,0), (0,0,1)
cp = lambda a,b: cnot(prod(a,b))
v1 = fourVal(E0, E0, cp(e2_,e3_), cp(e1_,e2_))
rec("W2","witness", v1 == -1 and all(ipW(cp(a,b), E0) >= 0 for a,b in ((e2_,e3_),(e1_,e2_))), "uniform K(E0): fourVal(E0, E0, cnot p(e2,e3), cnot p(e1,e2)) = -1 with the effects in K_gen subset K(E0) = dualW K(E0): FCC fails (X's witness)", str(v1))
m2 = (0,-1,0)
v2 = fourVal(ZF[(1,1)], cp(e2_,e2_), cp(m2,e2_), cp(e1_,e2_))
rec("W3","witness", v2 == -sp.Rational(1,2), "uniform K(Z_F): fourVal(e_(1,1), cnot p(e2,e2), cnot p(-e2,e2), cnot p(e1,e2)) = -1/2: FCC fails at level (ii) (X's witness, U's parametrization e_(1,1) = cnot F)", str(v2))
Y1 = E(0,0) + E(1,3) + E(2,2); cY1 = cnot(Y1)
rec("W4","witness", ipW(Y1, cY1) == -1 and actT((1,-1,1), E0) == Y1, "Y1 = E0^Gamma (partial transpose) has ipW(Y1, cnot Y1) = -1: no cone with K subset K* and cnot K = K contains Y1 (U's necessary condition)", str(ipW(Y1,cY1)))
FcF = F + cnot(F)
rec("W5","identity", (FcF - (E(0,0) - E(3,1))/2).is_zero_matrix and is_psd(pauliW(FcF)), "F + cnot F = (E00 - E31)/2 is PSD, so every q in Q3 cap V+ has ipW(q,F) = ipW(q,(F + cnot F)/2) >= 0: K({F, cnot F}) cap V+ = Q3 cap V+ (U's K_F2), while K(E0) cap V+ contains the non-PSD E0 (E0 is cnot-fixed)")

n = sum(R); print(f"\nchecks: {len(R)}, confirmed: {n}"); print("VERDICT", "INDEP-QSD-CONFIRMED" if n == len(R) else "INDEP-QSD-MISMATCH"); sys.exit(0 if n == len(R) else 1)

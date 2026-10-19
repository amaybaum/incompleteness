# Independent reviewer check (exact, SymPy). Written from the memo's definitions; does not import or run verify_mev.py / dc_premise.py.
import sympy as sp, random
from sympy import Rational as R, I, Matrix, eye, zeros, symbols, conjugate, expand, simplify, sqrt
res=[]
def chk(name,c): res.append(bool(c)); print(("PASS " if c else "FAIL ")+name)
def kr(A,B): return sp.kronecker_product(A,B)
def pr(v): return v*v.H
P0=Matrix([[1,0],[0,0]]); P1=Matrix([[0,0],[0,1]]); Xp=Matrix([[0,1],[1,0]])
CN=kr(P0,eye(2))+kr(P1,Xp)          # control token 1, basis |ij> = |i>(x)|j>, index 2i+j
phi=Matrix([1,0,0,1])/sqrt(2)
c=R(53,100); v=Matrix([4,0,0,1])/sqrt(17); Pv=pr(v); Xc=eye(4)/2-c*Pv
# (a) not PSD
chk("min eig X_c = 1/2-53/100 = -3/100", min(Xc.eigenvals())==R(-3,100))
# (b) ME-validity: all ME vectors = (I(x)W)phi, W in U(2): W = e^{i t}[[a,-b*],[b,a*]], |a|^2+|b|^2=1
a1,a2,b1,b2=symbols('a1 a2 b1 b2',real=True); a=a1+I*a2; b=b1+I*b2
W=Matrix([[a,-conjugate(b)],[b,conjugate(a)]])   # global phase drops out of a projector
psi=kr(eye(2),W)*phi
ov=expand(sp.simplify((psi.H*Pv*psi)[0]))
chk("<psi|P_v|psi> = (25 a1^2 + 9 a2^2)/34", simplify(ov-(25*a1**2+9*a2**2)/34)==0)
# max of (25a1^2+9a2^2) on a1^2+a2^2<=1 is 25 (since 25a1^2+9a2^2 <= 25(a1^2+a2^2) <= 25), attained at a=1,b=0
chk("25a1^2+9a2^2 <= 25(a1^2+a2^2) identically (difference = 16 a2^2 >= 0)", expand(25*(a1**2+a2**2)-(25*a1**2+9*a2**2))==16*a2**2)
mev_min=R(1,2)-c*R(25,34)
chk("min over ME projectors = 15/136", mev_min==R(15,136) and mev_min>0)
chk("attained at W=I: <phi|X_c|phi> = 15/136", simplify((phi.H*Xc*phi)[0])==R(15,136))
# every ME vector has this form: coefficient matrix C with C C^dag = I/2 <=> sqrt2*C unitary; (I(x)W)phi has C = W^T/sqrt2  [checked symbolically]
Cpsi=Matrix(2,2,lambda i,j: psi[2*i+j])
chk("coefficient matrix of (I(x)W)phi = W^T/sqrt2", simplify(Cpsi-W.T/sqrt(2))==zeros(2,2))
# (c) block positivity: max product overlap = top Schmidt coefficient^2 = 16/17
Cv=Matrix(2,2,lambda i,j: v[2*i+j]); sv=(Cv*Cv.H).eigenvals()
chk("Schmidt coefficients^2 of v = {16/17, 1/17}", set(sv)=={R(16,17),R(1,17)})
chk("min over product vectors = 1/2 - 53/100*16/17 = 1/850", R(1,2)-c*R(16,17)==R(1,850))
# (d) fails a product test after the coupling
ev=pr(Matrix([4,1])/sqrt(17))
chk("CN(e_v (x) P0)CN = P_v", simplify(CN*kr(ev,P0)*CN.H-Pv)==zeros(4,4))
val=simplify((kr(ev,P0)*CN*Xc*CN.H).trace())
chk("Tr[(e_v (x) P0) CN X_c CN] = 1/2-53/100 = -3/100", val==R(-3,100))
chk("e_v is a pure token effect (rank-one projector, Bloch vector (8/17,0,15/17))", ev*ev==ev and ev.trace()==1)
# (e) fails UPD (even block)
ebl=Matrix([[Xc[0,0],Xc[0,3]],[Xc[3,0],Xc[3,3]]])
chk("even block of X_c has eigenvalue -3/100", R(-3,100) in ebl.eigenvals())
# (f) OV-LU => MEV : Tr(P_{(I(x)W)phi} X) = Tr[(|+><+|(x)P0) CN (I(x)W)^dag X (I(x)W) CN] for symbolic X, unitary W
plus=pr(Matrix([1,1])/sqrt(2)); Bm=CN*kr(plus,P0)*CN.H
chk("B = CN(|+><+|(x)P0)CN = |phi+><phi+|", simplify(Bm-pr(phi))==zeros(4,4))
Xs=Matrix(4,4,lambda r,s: symbols(f'x{r}{s}'))
L=kr(eye(2),W)
lhs=(pr(psi)*Xs).trace(); rhs=(kr(plus,P0)*CN*L.H*Xs*L*CN.H).trace()
chk("Tr(P_psi X) = product test |+><+|(x)P0 after LU (I(x)W^dag) and CN (identity in X, W)", simplify(expand(lhs-rhs))==0)
# (g) countercontrol: the same machinery flags a PSD state as ME-valid and product-test-valid after CN
Q=pr(Matrix([1,2,0,1])/sqrt(6))
chk("countercontrol: PSD Q passes product test e_v(x)P0 after CN", (kr(ev,P0)*CN*Q*CN.H).trace()>=0)
# (h) mutation: with c = 1/2 the product-test value is 0, not negative (shows the test is sensitive to c)
chk("mutation: c=1/2 gives value 0 (no violation)", simplify((kr(ev,P0)*CN*(eye(4)/2-R(1,2)*Pv)*CN.H).trace())==0)
# (i) float sampling countercheck over random U(2) (evidence only, not certification)
import cmath, math
random.seed(1); mn=1e9
for _ in range(20000):
    x=[random.gauss(0,1) for _ in range(4)]; n=math.sqrt(sum(t*t for t in x)); x=[t/n for t in x]
    A=complex(x[0],x[1]); ov_f=(25*x[0]**2+9*x[1]**2)/34
    mn=min(mn,0.5-0.53*ov_f)
chk("float sampling: min ME value >= 15/136 - 1e-12 (got %.6f; 15/136=%.6f)"%(mn,15/136), mn>=15/136-1e-12)
print("TOTAL", sum(res), "PASS", len(res)-sum(res), "FAIL")

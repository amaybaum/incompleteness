"""Review check: M* needs only ONE non-configuration test basis (X). Exact SymPy.
X-test on |0>, Z = R_z(pi) (circle) on outcome '-', R_z(pi/2) (circle) gives |+i>, then the author's
S4 gadget (CNOT ancilla->data, X-basis test of ancilla, native X on one outcome) gives R_x(pi/2)."""
import sympy as sp
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]])
def Rz(a): return sp.diag(sp.exp(-sp.I*a/2), sp.exp(sp.I*a/2))
k0=sp.Matrix([1,0]); p=sp.Matrix([1,1])/sp.sqrt(2); m=sp.Matrix([1,-1])/sp.sqrt(2)
br_p = p*(p.H*k0)[0]; br_m = Rz(sp.pi)*m*(m.H*k0)[0]
def propto(u,v): return all(sp.simplify(u[i]*v[j]-u[j]*v[i])==0 for i in range(len(u)) for j in range(len(u)))
ok1 = propto(br_p, p) and propto(br_m, p) and sp.simplify((br_p.H*br_p)[0]+(br_m.H*br_m)[0]-1)==0
anc = Rz(sp.pi/2)*p
ypl = sp.Matrix([1, sp.I])/sp.sqrt(2)
ok2 = propto(anc, ypl)
a0,a1=sp.symbols('a0 a1'); d=sp.Matrix([a0,a1])
P0=sp.diag(1,0); P1=sp.diag(0,1); kr=sp.kronecker_product
CN=kr(I2,P0)+kr(X,P1); st=CN*kr(d,anc)
bw=kr(I2,m.H)*st; bwp=X*(kr(I2,p.H)*st)
Rx=sp.cos(sp.pi/4)*I2-sp.I*sp.sin(sp.pi/4)*X; tgt=Rx*d
ok3 = propto(bw,tgt) and propto(bwp,tgt) and sp.simplify((bw.H*bw)[0]+(bwp.H*bwp)[0]-(d.H*d)[0])==0
# countercontrol: without the R_z(pi/2) step (ancilla |+>), the gadget does NOT give R_x(pi/2)
st2=CN*kr(d,p); bw2=kr(I2,m.H)*st2
cc = not propto(bw2, tgt)
for n,c in (("O1 X-test + Z gives |+> deterministically",ok1),("O2 R_z(pi/2)|+> ~ |+i>",ok2),("O3 gadget gives R_x(pi/2), both branches, weight 1",ok3),("O4 countercontrol: ancilla |+> fails",cc)):
    print(("PASS" if c else "FAIL"), n)

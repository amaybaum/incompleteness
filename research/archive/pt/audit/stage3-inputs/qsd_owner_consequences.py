#!/usr/bin/env python3
"""Coordinator's exact check of the owner's three stage-3 consequences of H1-H3 (prepared for the U/X audits;
written without thread code). Decision rule fixed before the first run: every line CONFIRMED, else MISMATCH (exit 1)."""
import itertools, sys
import sympy as sp
R = []
def rec(cid, kind, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} [{kind}] {text}" + (f" -- {detail}" if detail else ""))
PC=[[0,0,3,3],[1,1,2,2],[2,2,1,1],[3,3,0,0]]; PT=[[0,1,2,3],[1,0,3,2],[1,0,3,2],[0,1,2,3]]
def cnot(w): return sp.Matrix(4,4, lambda m,n: (-1 if (m,n) in ((1,3),(2,2)) else 1)*w[PC[m][n],PT[m][n]])
S0=sp.eye(2); SX=sp.Matrix([[0,1],[1,0]]); SY=sp.Matrix([[0,-sp.I],[sp.I,0]]); SZ=sp.Matrix([[1,0],[0,-1]]); SG=[S0,SX,SY,SZ]
def pauliW(w): return sum((w[m,n]*sp.kronecker_product(SG[m],SG[n]) for m in range(4) for n in range(4)), sp.zeros(4,4))/4
def ipW(a,b): return sp.expand(sum(a[i,j]*b[i,j] for i in range(4) for j in range(4)))
hom=lambda x: sp.Matrix([1,*x]); prod=lambda x,y: hom(x)*hom(y).T
AX=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
E00=sp.zeros(4,4); E00[0,0]=1
# --- consequence 3: normalization and compact base, with a FINITE average ---
P36=[prod(a,b) for a in AX for b in AX]
avg=sum(P36, sp.zeros(4,4))/36
M=sp.Matrix([[p[i,j] for i in range(4) for j in range(4)] for p in P36])
rec("N1","identity", avg==E00 and M.rank()==16, "the 36 axis products average to E00 and span R^16: for X nonneg on products, <X,E00> = mean <X,p_i> >= 0, and = 0 forces all 36 pairings 0, hence X = 0; so every nonzero X in maxCone (a fortiori in K) has X_00 = Tr X/... > 0")
w=sp.Matrix(4,4, sp.symbols('w0:16')); w=w.subs(w[0,0],1)
okB=True
for i in range(1,4):
    for j in range(1,4):
        vals=[sp.expand(ipW(w, prod(tuple(s*int(k==i-1) for k in range(3)), tuple(t*int(k==j-1) for k in range(3))))) for s in (1,-1) for t in (1,-1)]
        # (s,t)=(1,1)+(-1,-1) gives 2+2w_ij ; (1,-1)+(-1,1) gives 2-2w_ij
        okB = bool(okB) and bool(sp.expand(vals[0]+vals[3]-(2+2*w[i,j]))==0) and bool(sp.expand(vals[1]+vals[2]-(2-2*w[i,j]))==0)
    okB = bool(okB) and bool(sp.expand(ipW(w, prod(tuple(int(k==i-1) for k in range(3)),(0,0,0)))+ipW(w, prod(tuple(-int(k==i-1) for k in range(3)),(0,0,0)))-2)==0)
rec("N2","identity", okB, "for w in maxCone with w_00 = 1, pairs of axis products give 2 +- 2 w_ij >= 0 and 1 +- w_i0 >= 0: every entry has |w_mn| <= 1, so the section {w_00 = 1} of maxCone, hence of any K in the corridor, is compact")
# --- consequence 1: the witness pair (X, P_psi) for X = E0 ---
E0=sp.zeros(4,4); E0[0,0]=1; E0[1,3]=1; E0[2,2]=-1
rho=pauliW(E0); ev=rho.eigenvects()
neg=[(lam,vs) for lam,mult,vs in ev if lam<0]
lam,vs=neg[0]; psi=vs[0]/sp.sqrt((vs[0].H*vs[0])[0,0])
Ppsi=psi*psi.H
G=sp.Matrix([[1,0,0,0],[0,0,0,-1],[0,0,1,0],[0,-1,0,0]])
val=sp.simplify(4*(rho*Ppsi).trace())
gpsi=sp.Matrix([1,-1,-1,-1])/2
rec("W1","witness", lam==-sp.Rational(1,4) and val==-1 and sp.simplify((psi.H*gpsi)[0,0]*sp.conjugate((psi.H*gpsi)[0,0]))==1,
    "E0's negative eigenvalue is -1/4 with eigenprojector P_psi = G (|<psi|G>|^2 = 1): ipW(E0, P_psi) = -1 < 0, so if E0 were in a self-dual K then the pure state G would not be", str(val))
# the missed pure state is outside K_gen: G is not a cnot image of a product (rank test) and not a product
rank_ok = all(cnot(prod(a,b))!=G for a in AX for b in AX)
rec("W2","witness", G.rank()==4 and cnot(G).rank()==4, "G and cnot G have table rank 4, so G is neither a product (rank 1) nor a cnot image of a product (rank 1 after cnot): the missed pure state lies outside K_gen, as the corridor requires")
# --- consequence 2: the V+ reduction ---
v=sp.Matrix(4,4, sp.symbols('v0:16')); k=sp.Matrix(4,4, sp.symbols('k0:16'))
Pp=lambda t: (t+cnot(t))/2
vplus=Pp(v)
rec("V1","identity", sp.expand(ipW(vplus,k)-ipW(vplus,Pp(k)))==0 and cnot(vplus)==vplus and sp.expand(ipW(Pp(v),k)-ipW(v,Pp(k)))==0,
    "P+ = (I + cnot)/2 is a self-adjoint projection onto V+: for v in V+, <v,k> = <v,P+ k> symbolically; so v in K* iff v in (K cap V+)^{*V+}, and K cap V+ is self-dual within V+")
cols=[]
for i in range(16):
    B=sp.zeros(4,4); B[i//4,i%4]=1; C=cnot(B); cols.append([C[a//4,a%4] for a in range(16)])
CM=sp.Matrix(cols).T
rec("V2","identity", len((CM-sp.eye(16)).nullspace())==10 and len((CM+sp.eye(16)).nullspace())==6, "dim V+ = 10, dim V- = 6")
n=sum(R); print(f"\nchecks: {len(R)}, confirmed: {n}"); print("VERDICT", "QSD-OWNER-CONSEQUENCES-CONFIRMED" if n==len(R) else "MISMATCH"); sys.exit(0 if n==len(R) else 1)

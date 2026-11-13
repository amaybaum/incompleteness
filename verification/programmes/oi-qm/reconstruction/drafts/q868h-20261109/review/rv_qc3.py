"""Reviewer check for QC-3 (Q-868-H unit 1). Generic matrices only; encodes no OI rule, encoding,
coupling or preparation. Partial transpose implemented independently via reshape/permute.
Self-contained; imports no earlier probe. sympy, exact."""
import sys, itertools
import sympy as sp
from sympy.tensor.array import Array, permutedims
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Y=sp.Matrix([[0,-sp.I],[sp.I,0]]); Z=sp.Matrix([[1,0],[0,-1]])
P={"0":I2,"x":X,"y":Y,"z":Z}; K=lambda a,b: sp.kronecker_product(a,b)
res=[]
def chk(n,ok,d=""):
    res.append(bool(ok)); print(("PASS " if ok else "FAIL ")+n+(" :: "+d if d else ""))
def ptA(M):
    A=Array([[M[i,j] for j in range(4)] for i in range(4)]).reshape(2,2,2,2)   # (iA,iB,jA,jB)
    B=permutedims(A,(2,1,0,3))                                                   # swap iA<->jA
    return sp.Matrix(B.reshape(4,4).tolist())
chk("T3a transposes: X^T=X, Z^T=Z, Y^T=-Y, I^T=I", X.T==X and Z.T==Z and Y.T==-Y)
syms={(a,b):sp.Symbol("t_"+a+b) for a in "0xyz" for b in "0xyz"}
R=sum((syms[(a,b)]*K(P[a],P[b]) for a in "0xyz" for b in "0xyz"),sp.zeros(4,4))/4
Rflip=sum(((-1 if a=="y" else 1)*syms[(a,b)]*K(P[a],P[b]) for a in "0xyz" for b in "0xyz"),sp.zeros(4,4))/4
chk("T3b on a fully generic 16-entry symbolic table, PT on wing A = negation of every T_{y,b}", sp.expand(ptA(R)-Rflip)==sp.zeros(4,4))
Rflip2=sum(((-1 if b=="y" else 1)*syms[(a,b)]*K(P[a],P[b]) for a in "0xyz" for b in "0xyz"),sp.zeros(4,4))/4
chk("T3c control: PT on wing A is not the negation of the Y column (wing B)", sp.expand(ptA(R)-Rflip2)!=sp.zeros(4,4))
phi=sp.Matrix([1,0,0,1])/sp.sqrt(2); rho=phi*phi.T
SWAP=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
chk("T3d PT_A(|Phi+><Phi+|) = SWAP/2", sp.simplify(ptA(rho)-SWAP/2)==sp.zeros(4,4))
chk("T3e SWAP/2 has minimum eigenvalue -1/2", min((SWAP/2).eigenvals())==sp.Rational(-1,2))
chk("T3f control: PT_A of the product |00><00| is PSD (positive map on product inputs)",
    min(ptA(sp.Matrix([1,0,0,0])*sp.Matrix([1,0,0,0]).T).eigenvals())>=0)
nf=res.count(False); print(f"\n{len(res)} checks, {nf} failures"); sys.exit(1 if nf else 0)

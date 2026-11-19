"""Reviewer check: a witness for 'hH2 fails for the native table cone' (Q-868-H unit 1). Generic Pauli
tables only; which tables are natively reachable is decided by hand in the review. Encodes no OI rule,
encoding, coupling or preparation. Self-contained; imports no earlier probe. sympy, exact."""
import sys, itertools
import sympy as sp
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Y=sp.Matrix([[0,-sp.I],[sp.I,0]]); Z=sp.Matrix([[1,0],[0,-1]])
P={"0":I2,"x":X,"y":Y,"z":Z}; K=lambda a,b: sp.kronecker_product(a,b)
res=[]
def chk(n,ok,d=""):
    res.append(bool(ok)); print(("PASS " if ok else "FAIL ")+n+(" :: "+d if d else ""))
CN=sp.zeros(4,4)
for c,t in itertools.product(range(2),repeat=2): CN[2*c+((t+c)%2),2*c+t]=1
SWAP=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
W=SWAP/2
Wc=CN*W*CN   # table cnot = conjugation by CNOT on the operator rho_T
tab={(a,b):sp.simplify((Wc*K(P[a],P[b])).trace()) for a in "0xyz" for b in "0xyz"}
nz={k:v for k,v in tab.items() if v!=0}
chk("H2a cnot(SWAP/2) has table (I + X(x)I + I(x)Z - X(x)Z)/4", nz=={("0","0"):1,("x","0"):1,("0","z"):1,("x","z"):-1}, str(nz))
eff=lambda A,s: (I2+s*A)/2
vals={(a,s,b,u):sp.simplify((Wc*K(eff(P[a],s),eff(P[b],u))).trace()) for a in "xyz" for b in "xyz" for s in (1,-1) for u in (1,-1)}
neg={k:v for k,v in vals.items() if v<0}
chk("H2b cnot(SWAP/2) is negative on a Pauli product: value -1/2 on (-x) (x) (-z)", vals[("x",-1,"z",-1)]==sp.Rational(-1,2), str(neg))
chk("H2c control: SWAP/2 itself is nonnegative on all 36 Pauli products",
    all(sp.simplify((W*K(eff(P[a],s),eff(P[b],u))).trace())>=0 for a in "xyz" for b in "xyz" for s in (1,-1) for u in (1,-1)))
nf=res.count(False); print(f"\n{len(res)} checks, {nf} failures"); sys.exit(1 if nf else 0)

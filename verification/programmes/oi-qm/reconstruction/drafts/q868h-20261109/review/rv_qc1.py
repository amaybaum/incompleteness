"""Reviewer check for QC-1 (Q-868-H unit 1). Generic Pauli facts only; encodes no OI rule,
encoding, coupling or preparation. Self-contained; imports no earlier probe. sympy, exact."""
import sys, itertools
import sympy as sp
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Y=sp.Matrix([[0,-sp.I],[sp.I,0]]); Z=sp.Matrix([[1,0],[0,-1]])
K=lambda a,b: sp.kronecker_product(a,b)
res=[]
def chk(n,ok,d=""):
    res.append(bool(ok)); print(("PASS " if ok else "FAIL ")+n+(" :: "+d if d else ""))
t=sp.Symbol("t",real=True)
# table (I + XX + ZZ + t YY)/4, t in [-1,1]: eigenvalues
M=(sp.eye(4)+K(X,X)+K(Z,Z)+t*K(Y,Y))/4
ev=M.eigenvals()
evs=sorted([sp.simplify(e) for e in ev], key=lambda e: str(e))
target={(1+t)/4:2,(3-t)/4:1,(-1-t)/4:1}
chk("Q1a eigenvalues of (I+XX+ZZ+tYY)/4 are (1+t)/4 (x2), (3-t)/4, (-1-t)/4",
    {sp.expand(k):v for k,v in ev.items()}=={sp.expand(k):v for k,v in target.items()}, str(ev))
chk("Q1b at t=0 (node-10 zero completion) minimum eigenvalue is exactly -1/4",
    min(sp.simplify(e.subs(t,0)) for e in ev)==sp.Rational(-1,4))
chk("Q1c on t in [-1,1] the table is PSD iff t = -1 (all eigenvalues >= 0 at t=-1; (-1-t)/4 < 0 for t > -1)",
    all(sp.expand(k).subs(t,-1)>=0 for k in ev) and sp.solve_univariate_inequality((-1-t)/4<0,t,relational=False)==sp.Interval.open(-1,sp.oo))
# operator identity forcing YY = -1 when XX = ZZ = +1 in any quantum state
chk("Q1d (X(x)X)(Z(x)Z) = -(Y(x)Y)", K(X,X)*K(Z,Z)==-K(Y,Y))
chk("Q1e control: (X(x)X)(Z(x)Z) != +(Y(x)Y)", K(X,X)*K(Z,Z)!=K(Y,Y))
# generic: any two commuting distinct correlators s1 A1(x)B1, s2 A2(x)B2 with zero marginals and nothing else -> min eig -1/4
P={"x":X,"y":Y,"z":Z}; ok=True; cnt=0
for (a1,b1),(a2,b2) in itertools.combinations(list(itertools.product("xyz",repeat=2)),2):
    O1=K(P[a1],P[b1]); O2=K(P[a2],P[b2])
    if O1*O2!=O2*O1: continue
    for s1,s2 in itertools.product([1,-1],repeat=2):
        m=min(sp.nsimplify(sp.re(e)) for e in ((sp.eye(4)+s1*O1+s2*O2)/4).eigenvals())
        ok&=(m==sp.Rational(-1,4)); cnt+=1
chk("Q1f every table with zero marginals and exactly two commuting Pauli-product correlators has min eigenvalue -1/4",ok,f"{cnt} tables")
nf=res.count(False); print(f"\n{len(res)} checks, {nf} failures"); sys.exit(1 if nf else 0)

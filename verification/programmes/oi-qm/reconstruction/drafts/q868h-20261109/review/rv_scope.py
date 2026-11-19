"""Reviewer scope checks (Q-868-H unit 1): Bell content of Pauli-only settings, and herald-level
membership for the QC =/=> (C) witness. Generic qubit facts only; encodes no OI rule, encoding,
coupling or preparation. Self-contained; imports no earlier probe. sympy, exact."""
import sys, itertools
import sympy as sp
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Y=sp.Matrix([[0,-sp.I],[sp.I,0]]); Z=sp.Matrix([[1,0],[0,-1]])
P={"x":X,"y":Y,"z":Z}; K=lambda a,b: sp.kronecker_product(a,b)
res=[]
def chk(n,ok,d=""):
    res.append(bool(ok)); print(("PASS " if ok else "FAIL ")+n+(" :: "+d if d else ""))
s2=1/sp.sqrt(2)
bell=[sp.Matrix([1,0,0,1])*s2, sp.Matrix([1,0,0,-1])*s2, sp.Matrix([0,1,1,0])*s2, sp.Matrix([0,1,-1,0])*s2]
def E(v,A,B): return sp.simplify((v.H*K(A,B)*v)[0])
def chsh_max(v,As,Bs):
    best=0
    for a0,a1 in itertools.permutations(As,2):
        for b0,b1 in itertools.permutations(Bs,2):
            for sg in itertools.product([1,-1],repeat=4):
                val=sg[0]*E(v,a0,b0)+sg[1]*E(v,a0,b1)+sg[2]*E(v,a1,b0)+sg[3]*E(v,a1,b1)
                if sg[0]*sg[1]*sg[2]*sg[3]==-1: best=max(best,sp.Abs(val))
    return best
paulis=[X,Y,Z]
m=max(chsh_max(v,paulis,paulis) for v in bell)
chk("B5a the four Bell states (stabilizer) with Pauli-only settings: max |CHSH| = 2", m==2, str(m))
O=K(X,X)+K(X,Z)+K(Z,X)-K(Z,Z)
chk("B5b but the Pauli-settings CHSH operator XX+XZ+ZX-ZZ has eigenvalue 2*sqrt2 (a non-stabilizer state violates with Pauli settings)",
    max(O.eigenvals())==2*sp.sqrt(2))
Bp=(X+Z)*s2; Bm=(X-Z)*s2
chk("B5c control: Phi+ with B at (X+-Z)/sqrt2 reaches 2*sqrt2",
    sp.simplify(E(bell[0],X,Bp)+E(bell[0],X,Bm)+E(bell[0],Z,Bp)-E(bell[0],Z,Bm))==2*sp.sqrt(2))
# herald level: comparator for Phi+, A reads X then Z (Lueders), B conditional Bloch vector
phi=bell[0]; rho=phi*phi.H
def proj(Pm,b): return (sp.eye(2)+(-1)**b*Pm)/2
ok=True; heralds=[]
for b1,b2 in itertools.product(range(2),repeat=2):
    M=K(proj(Z,b2)*proj(X,b1),I2)
    r=M*rho*M.H; pr=sp.simplify(r.trace())
    rB=sp.zeros(2,2)
    for i in range(2):
        for j in range(2):
            rB[i,j]=sum(r[2*k+i,2*k+j] for k in range(2))
    rB=sp.simplify(rB/pr)
    bv=tuple(sp.simplify((rB*P[a]).trace()) for a in "xyz"); heralds.append(bv)
    ok&=(bv in [(1,0,0),(-1,0,0)])
chk("B5d comparator: Phi+, A reads X then Z: B's conditional Bloch vector is +-e_x (inside the octahedron)", ok, str(heralds))
rhoB=(I2+X+Z)/2
chk("B5e Bloch (1,0,1) is no qubit state: (I+X+Z)/2 has eigenvalue (1-sqrt2)/2 < 0",
    min(rhoB.eigenvals())==(1-sp.sqrt(2))/2)
# abstract property-level witness for QC =/=> (C): a quantum product state whose B marginal is a
# ball point outside the octahedron (comparator object, not a native preparation)
th=sp.pi/8; psi=sp.Matrix([sp.cos(th),sp.sin(th)])
bvec=[sp.simplify((psi.H*P[a]*psi)[0]) for a in "xyz"]
chk("B5f |0>(x)(cos(pi/8)|0>+sin(pi/8)|1>) is PSD with B Bloch (1/sqrt2,0,1/sqrt2): unit norm, L1 norm sqrt2 > 1",
    sp.simplify(bvec[0]-s2)==0 and bvec[1]==0 and sp.simplify(bvec[2]-s2)==0 and sp.simplify(sum(abs(c) for c in bvec)-sp.sqrt(2))==0)
nf=res.count(False); print(f"\n{len(res)} checks, {nf} failures"); sys.exit(1 if nf else 0)

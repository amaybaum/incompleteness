import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, kronecker_product as kron, simplify, expand, sqrt
I2 = eye(2); SX = Matrix([[0,1],[1,0]]); SY = Matrix([[0,-I],[I,0]]); SZ = Matrix([[1,0],[0,-1]]); SG=[I2,SX,SY,SZ]
KR = {(m,n): kron(SG[m],SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m,n]*KR[(m,n)] for m in range(4) for n in range(4) if w[m,n]!=0), zeros(4,4))/4
def tab(M): return Matrix(4,4, lambda m,n: sp.nsimplify(simplify(expand((KR[(m,n)]*M).trace()))))
def Ad(U,w): return tab(U*pauliW(w)*U.H)
CNOT = Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
idW = eye(4); chainW = Ad(CNOT, idW); print("chainW =", chainW.tolist())
def sharp(n): return Matrix([Q(1,2), n[0]/2, n[1]/2, n[2]/2])
print("val_chain =", (sharp([-1,0,0]).T*chainW*sharp([0,0,-1]))[0])
import itertools
grid = [sp.Matrix(n) for n in itertools.product([-1,0,1], repeat=3) if sum(abs(k) for k in n)==1] + [Matrix([Q(3,5),0,Q(4,5)]), Matrix([0,Q(3,5),Q(-4,5)])]
print("min idW pairing", min((sharp(n).T*idW*sharp(m))[0] for n in grid for m in grid))
# group orders and orbits
UJ = (I2 - I*(SX+SY+SZ))/2; UJI = kron(UJ,I2); IUJ = kron(I2,UJ)
def canon(M):
    M = M.applyfunc(lambda z: sp.nsimplify(simplify(z)))
    for i in range(4):
        for j in range(4):
            if M[i,j]!=0: return sp.ImmutableMatrix((M/M[i,j]).applyfunc(lambda z: sp.nsimplify(simplify(z))))
def gorder(gens):
    gens=[canon(g) for g in gens]; grp=set(gens); fr=list(grp)
    while fr:
        nx=[]
        for g in fr:
            for h in gens:
                for r in (canon(Matrix(g)*Matrix(h)), canon(Matrix(h)*Matrix(g))):
                    if r not in grp: grp.add(r); nx.append(r)
        fr=nx
    return len(grp)
print("proj order <UJI,CNOT> =", gorder([UJI, CNOT]))
print("proj order <IUJ,CNOT> =", gorder([IUJ, CNOT]))
phi0 = Matrix([1,2,3*I,-1+I])
def vorbit(gens, v0):
    v0 = sp.ImmutableMatrix(v0.applyfunc(lambda z: sp.nsimplify(simplify(z)))); orb={v0}; fr=[v0]
    while fr:
        nx=[]
        for v in fr:
            for g in gens:
                w = sp.ImmutableMatrix((g*Matrix(v)).applyfunc(lambda z: sp.nsimplify(simplify(expand(z)))))
                if w not in orb: orb.add(w); nx.append(w)
        fr=nx
    return orb
oC = vorbit([UJI, CNOT], phi0); oT = vorbit([IUJ, CNOT], phi0)
print("vector orbits:", len(oC), len(oT))
def det2(v): return v[0]*v[3]-v[1]*v[2]
def dl(orb): return min(simplify(expand(det2(v)*sp.conjugate(det2(v)))/((v.H*v)[0])**2) for v in orb)
print("d_low over vector orbits (|det|^2/n^4):", dl(oC), dl(oT))

# exploratory float: dimension of W = span of F_BP(x+y), and the B6 inequality, for random pairs
import numpy as np
rng = np.random.default_rng(1)
def ket(v): v=np.array(v,complex); return v/np.linalg.norm(v)
def rnd(): return ket(rng.normal(size=2)+1j*rng.normal(size=2))
def perp(v): return np.array([-np.conj(v[1]), np.conj(v[0])])
herm_basis=[]
for i in range(4):
    for j in range(4):
        M=np.zeros((4,4),complex)
        if i==j: M[i,i]=1
        elif i<j: M[i,j]=M[j,i]=1
        else: M[i,j]=1j; M[j,i]=-1j
        herm_basis.append(M)
for trial in range(5):
    a,b,a2,b2=rnd(),rnd(),rnd(),rnd()
    p1=np.kron(perp(a),perp(b2)); p2=np.kron(perp(a2),perp(b))
    rows=[]
    for p,(g,d) in [(p1,(perp(a),perp(b2))),(p2,(perp(a2),perp(b)))]:
        gp,dp=perp(g),perp(d)
        for q in [np.kron(g,d), np.kron(gp,d), np.kron(g,dp)]:
            # condition <q|w|p> = 0 (complex -> 2 real, or 1 if q=p)
            row=[np.vdot(q, M@p) for M in herm_basis]
            rows.append(np.real(row)); rows.append(np.imag(row))
    A=np.array(rows)
    r=np.linalg.matrix_rank(A,1e-9)
    print("trial",trial,"conditions rank",r,"dim W",16-r)

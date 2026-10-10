"""K2.3 (read-only, exact), narrow scope: tripartite composites obtained from standard quantum theory by local O(3)
relabellings (L_A (x) L_B (x) L_C) Q_ABC.  Pairwise branch of a pair = Q or PT(Q) for its two-party marginal cone
(L_X (x) L_Y) Q_XY (the marginal: L_C fixes u, so tracing C commutes with the relabelling)."""
import itertools, sympy as sp
kr=sp.kronecker_product
P=[sp.eye(2),sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.Matrix([[1,0],[0,-1]])]
B2=[kr(P[i],P[j]) for i in range(4) for j in range(4)]
def choi(G):
    """Choi matrix of the 2-qubit map whose Pauli-transfer (Bloch) matrix is G"""
    S=lambda Mx: sum((G[i,j]*B2[i]*((B2[j].H*Mx).trace()/4) for i in range(16) for j in range(16) if G[i,j]!=0), sp.zeros(4))
    C=sp.zeros(16)
    for k in range(4):
        for l in range(4):
            E=sp.zeros(4); E[k,l]=1; C+=kr(E,S(E))
    return C
def unitary(G):
    C=choi(G); return C.rank()==1 and C==C.H and all(sp.re(C[i,i])>=0 for i in range(16))
R=sp.diag(1,1,-1,1); T=kr(R,R); PB=kr(sp.eye(4),R); PA=kr(R,sp.eye(4))
def wigner(G): return unitary(G) or unitary(T*G)          # a unitary or antiunitary symmetry of Q
def branch(LA,LB):
    G=kr(LA,LB)
    q=wigner(G); pt=wigner(PB*G)
    assert q!=pt
    return 0 if q else 1                                  # 0: the pair's cone is Q; 1: it is PT(Q)
D=[sp.diag(1,a,b,c) for a,b,c in itertools.product((1,-1),repeat=3)]
# (1) the pairwise branch depends only on the determinants, and is det L_A * det L_B
tab={(i,j):branch(D[i],D[j]) for i in range(8) for j in range(8)}
print('(1) branch = [det L_A != det L_B] for all 64 pairs of sign relabellings:',
      all(tab[i,j]==int(D[i].det()!=D[j].det()) for i in range(8) for j in range(8)))
# (2) Q != PT(Q): the Bell state's partial transpose has eigenvalue -1/2
bell=sp.Matrix([1,0,0,1])/sp.sqrt(2); rho=bell*bell.T
pt=sp.Matrix(4,4,lambda r,c: rho[(r//2)*2+(c%2),(c//2)*2+(r%2)])
print('(2) eigenvalues of PT(Bell):',sorted(pt.eigenvals().items(),key=lambda kv: kv[0]))
# (3) PT_A(Q) = PT_B(Q): PT_A = T . PT_B and T is a Wigner symmetry of Q
print('(3) PT_A = T . PT_B in Bloch coordinates:',PA==T*PB,'; T antiunitary symmetry of Q:',unitary(T*T) and not unitary(T))
# (4) three copies: every triple of relabellings gives an even triangle parity; every even assignment occurs
seen=set()
for i,j,k in itertools.product(range(8),repeat=3):
    e=(tab[i,j],tab[j,k],tab[k,i]); seen.add(e)
    assert (e[0]+e[1]+e[2])%2==0
print('(4) all 512 triples have even triangle parity; realised assignments:',sorted(seen))
print('    odd assignments (e.g. all three pairs mirrored) realised:',sorted(set(itertools.product((0,1),repeat=3))-seen and set(itertools.product((0,1),repeat=3))&seen ^ set(itertools.product((0,1),repeat=3)) ) and 'none')

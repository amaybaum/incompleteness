"""SC-25 exact counterexample: invariance group of a cubic-lattice step kernel inside O(3,1).
Coordinates (t,x,y,z), metric eta = diag(1,-1,-1,-1), n = (1,0,0,0).
Kernel T: one update step moves a site to a nearest neighbour, increments S = {n +- e_i}, each 1/6.
An invariance of T is a Lambda in O(3,1) with Lambda S = S (it then preserves the uniform weights).
S spans R^4, so Lambda is fixed by its action on S: enumerate all images of a basis, exactly."""
from fractions import Fraction as F
from itertools import permutations

ETA = [[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]]
n = (1,0,0,0)
def vec(t,x,y,z): return tuple(F(c) for c in (t,x,y,z))
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def T_(A): return [list(r) for r in zip(*A)]
def apply(L,v): return tuple(sum(L[i][j]*v[j] for j in range(4)) for i in range(4))
def inv(M):
    m=len(M); A=[list(map(F,r))+[F(int(i==j)) for j in range(m)] for i,r in enumerate(M)]
    for c in range(m):
        p=next(r for r in range(c,m) if A[r][c]!=0); A[c],A[p]=A[p],A[c]
        pv=A[c][c]; A[c]=[x/pv for x in A[c]]
        for r in range(m):
            if r!=c and A[r][c]!=0:
                f=A[r][c]; A[r]=[a-f*b for a,b in zip(A[r],A[c])]
    return [r[m:] for r in A]

def group_of(S):
    S=list(S); Sset=set(S)
    # pick 4 independent vectors from S
    basis=[]
    for v in S:
        cand=basis+[v]
        M=[list(c) for c in cand]
        # rank test via elimination
        A=[list(r) for r in M]; rk=0
        for c in range(4):
            p=next((r for r in range(rk,len(A)) if A[r][c]!=0),None)
            if p is None: continue
            A[rk],A[p]=A[p],A[rk]
            for r in range(len(A)):
                if r!=rk and A[r][c]!=0:
                    f=A[r][c]/A[rk][c]; A[r]=[a-f*b for a,b in zip(A[r],A[rk])]
            rk+=1
        if rk==len(cand): basis=cand
        if len(basis)==4: break
    B=T_([list(b) for b in basis]); Binv=inv(B)
    G=[]
    for img in permutations(S,4):
        L=matmul(T_([list(v) for v in img]),Binv)
        if matmul(matmul(T_(L),ETA),L)!=ETA: continue
        if set(apply(L,v) for v in S)!=Sset: continue
        G.append(L)
    return G

E=[vec(0,1,0,0),vec(0,0,1,0),vec(0,0,0,1)]
units=[e for e in E]+[tuple(-c for c in e) for e in E]
S_fwd=[tuple(a+b for a,b in zip(vec(*n),u)) for u in units]          # time-oriented kernel
S_pm=S_fwd+[tuple(-c for c in v) for v in S_fwd]                       # time-reversal-symmetric data

ok=True
def check(name,cond):
    global ok; ok&=cond; print(('PASS ' if cond else 'FAIL ')+name)

G=group_of(S_fwd)
check('|G_T| = 48 for the time-oriented cubic kernel', len(G)==48)
check('every element fixes n (G_T subset Stab(n))', all(apply(L,vec(*n))==vec(*n) for L in G))
def spatial(L): return [r[1:] for r in L[1:]]
def signed_perm(R): return all(sum(1 for x in r if x!=0)==1 and all(x in (0,1,-1) for x in r) for r in R) and all(sum(1 for r in R if r[j]!=0)==1 for j in range(3))
check('spatial blocks are exactly the 48 signed permutations (O_h)', all(signed_perm(spatial(L)) for L in G) and len({str(spatial(L)) for L in G})==48)
check('-1 (parity) in G_T', any(spatial(L)==[[-1,0,0],[0,-1,0],[0,0,-1]] for L in G))
# fixed subspace of G_T: since parity in G_T acts as -1 on n-perp, fixed vectors lie in R n; n itself fixed.
check('fixed subspace of G_T is exactly R n (n still selected)', any(spatial(L)==[[-1,0,0],[0,-1,0],[0,0,-1]] and L[0]==[1,0,0,0] for L in G))
# a rotation fixing n that is not an invariance: z-rotation by pi/2 IS in O_h; z-rotation by pi/4 is not.
# exact surrogate: the rotation x->( x - y )/sqrt2 is irrational; use the rational rotation (3/5,4/5) about z.
R=[[1,0,0,0],[0,F(3,5),F(-4,5),0],[0,F(4,5),F(3,5),0],[0,0,0,1]]
check('control: rational rotation (3/5,4/5) about z lies in Stab(n) ∩ O(3,1)', matmul(matmul(T_(R),ETA),R)==ETA and apply(R,vec(*n))==vec(*n))
check('control: that rotation is NOT an invariance (Stab(n) ⊄ G_T)', set(apply(R,v) for v in S_fwd)!=set(S_fwd))
# boost countercontrol: rational boost with rapidity cosh=5/4, sinh=3/4 along x
Bst=[[F(5,4),F(3,4),0,0],[F(3,4),F(5,4),0,0],[0,0,1,0],[0,0,0,1]]
check('countercontrol: boost is in O(3,1), moves n, and is not an invariance', matmul(matmul(T_(Bst),ETA),Bst)==ETA and apply(Bst,vec(*n))!=vec(*n) and set(apply(Bst,v) for v in S_fwd)!=set(S_fwd))
Gpm=group_of(S_pm)
check('time-symmetric data: |G| = 96 = |O_h x O(1)|', len(Gpm)==96)
check('time-symmetric data: Lambda n = ±n for all, and -n occurs (G ⊄ Stab(n), G ⊆ Stab(R n))', all(apply(L,vec(*n)) in (vec(*n),vec(-1,0,0,0)) for L in Gpm) and any(apply(L,vec(*n))==vec(-1,0,0,0) for L in Gpm))
print('ALL CONTROLS GREEN' if ok else 'A CHECK FAILED'); raise SystemExit(0 if ok else 1)

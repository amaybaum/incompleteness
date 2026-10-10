"""Side probe (read-only, exact): does 'the native NOT is continuously interpolable' (det N = +1 on the ball) remove
the two-NOT loophole of NB-1 at d = 7?  Candidate: the J/K construction with N_A = (3,3) on the control and N_B = (1,5)
on the target.  Exact integer/Fraction arithmetic; positivity by the C3 reduction (written) plus a numerical check."""
from fractions import Fraction as Fr
import itertools, numpy as np
def zeros(n,m=None): return [[0]*(m or n) for _ in range(n)]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B)) if A[i][k]) for j in range(len(B[0]))] for i in range(len(A))]
def kron(a,b): return [x*y for x in a for y in b]
def kronM(A,B):
    n,m=len(A),len(B); return [[A[i//m][j//m]*B[i%m][j%m] for j in range(n*m)] for i in range(n*m)]
def diag(v): return [[v[i] if i==j else 0 for j in range(len(v))] for i in range(len(v))]
def det(M):
    return int(round(np.linalg.det(np.array(M,dtype=float))))
def build(d, NA_d, NB_d, Jmap, Kmap):
    """d-ball, basis u=0, T=1..d-1, z=d. NA_d/NB_d: eigenvalues on coordinates 1..d (z last, must be -1).
    Target E+ = {u} + NB's +1 transverse axes (here one axis x=1); A = identity (exchange u<->x);
    V- block: G(c (x) e_j) = Jc (x) K e_j."""
    n=d+1; e=eye(n); G=zeros(n*n)
    NB=[1]+NB_d
    plus=[i for i in range(n) if NB[i]==1]; assert plus==[0,1]
    for j in range(n):
        Pp=[e[j][i]*(1 if NB[i]==1 else 0) for i in range(n)]; Pm=[e[j][i]*(1 if NB[i]==-1 else 0) for i in range(n)]
        cu=[a+b for a,b in zip(kron(e[0],Pp),kron(e[d],Pm))]; cz=[a+b for a,b in zip(kron(e[d],Pp),kron(e[0],Pm))]
        for r in range(n*n): G[r][0*n+j]=cu[r]; G[r][d*n+j]=cz[r]
    S={0:1,1:0}
    for c in range(1,d):
        for j in (0,1): G[c*n+S[j]][c*n+j]=1
        for j in range(2,n):
            s1,cc=Jmap[c]; s2,l=Kmap[j]; G[cc*n+l][c*n+j]=s1*s2
    return G
def rels(G,n,NA,NB):
    I=eye(n); rt=matmul(matmul(kronM(I,NB),G),kronM(I,NB))==G
    rc=matmul(matmul(kronM(NA,I),G),kronM(NA,I))==matmul(kronM(I,NB),G); return rt,rc
def frame(G,n):
    k=[[1]+[0]*(n-2)+[1],[1]+[0]*(n-2)+[-1]]
    def mv(v): return [sum(G[i][j]*v[j] for j in range(len(v))) for i in range(len(G))]
    return all(mv(kron(k[a],k[b]))==kron(k[a],k[a^b]) for a in (0,1) for b in (0,1))
def as_mat(mp,n):
    M=zeros(n)
    for a,(s,b) in mp.items(): M[b][a]=s
    return M
d=7; n=8
# control: T = 1..6; N_A = +1 on 1,2,3 ; -1 on 4,5,6 and z=7.   J pairs i <-> i+3 : maps the +1 space to the -1 space
NA_d=[1,1,1,-1,-1,-1,-1]
J={1:(1,4),4:(-1,1),2:(1,5),5:(-1,2),3:(1,6),6:(-1,3)}
# target: N_B = +1 on x=1 only; -1 on 2..6 and z=7.  V- = {2,...,7}; K a complex structure on it
NB_d=[1,-1,-1,-1,-1,-1,-1]
K={2:(1,3),3:(-1,2),4:(1,5),5:(-1,4),6:(1,7),7:(-1,6)}
G=build(d,NA_d,NB_d,J,K)
NA=diag([1]+NA_d); NB=diag([1]+NB_d)
Jm=as_mat(J,n); Km=as_mat(K,n)
Jt=[[Jm[i][j] for j in range(1,7)] for i in range(1,7)]; Kt=[[Km[i][j] for j in range(2,8)] for i in range(2,8)]
neg=lambda M:[[-x for x in r] for r in M]; tr=lambda M:[list(r) for r in zip(*M)]
cs=matmul(Jt,Jt)==neg(eye(6)) and tr(Jt)==neg(Jt) and matmul(Kt,Kt)==neg(eye(6)) and tr(Kt)==neg(Kt)
anti=matmul(matmul(NA,Jm),NA)==neg(Jm)
rt,rc=rels(G,n,NA,NB)
print('d=7 two-NOT J/K map: frame %s; G^2 = I %s; J, K orthogonal complex structures %s; N_A J N_A = -J %s' % (frame(G,n), matmul(G,G)==eye(n*n), cs, anti))
print('  Rt with N_B: %s; Rc with (N_A, N_B): %s' % (rt,rc))
print('  det N_A = %d (p_A,q_A)=(3,3); det N_B = %d (p_B,q_B)=(1,5): both continuously interpolable iff both +1' % (det([r[1:] for r in NA[1:]]), det([r[1:] for r in NB[1:]])))
rt2,rc2=rels(G,n,NB,NB)
print('  control: with ONE common N = N_B on both factors the control relation fails: %s' % (not rc2))
# the exact reduction formula (multi-affine grid), as C5
def reduction_ok():
    e=eye(n); pts=[None]+list(range(1,n))
    def vec(i):
        v=[0]*n; v[0]=1
        if i is not None: v[i]+=1
        return v
    Vm=list(range(2,8))
    for si in pts:
        s=vec(si); Gs=[[sum(G[r][c*n+j]*s[c] for c in range(n)) for r in range(n*n)] for j in range(n)]
        for ti in pts:
            t=vec(ti); W=[sum(Gs[j][r]*t[j] for j in range(n)) for r in range(n*n)]
            for ai in pts:
                f=vec(ai)
                for bi in pts:
                    g=vec(bi); val=sum(f[i]*g[j]*W[i*n+j] for i in range(n) for j in range(n))
                    sT=[s[i] if 1<=i<d else 0 for i in range(n)]; aT=[f[i] if 1<=i<d else 0 for i in range(n)]
                    Js=[sum(Jm[i][j]*sT[j] for j in range(n)) for i in range(n)]
                    tm=[t[i] if i in Vm else 0 for i in range(n)]; bm=[g[i] if i in Vm else 0 for i in range(n)]
                    Kt_=[sum(Km[i][j]*tm[j] for j in range(n)) for i in range(n)]
                    rhs=(1+s[d]*f[d])*(1+g[1]*t[1])+(s[d]+f[d])*sum(x*y for x,y in zip(bm,tm)) \
                        +sum(x*y for x,y in zip(aT,sT))*(t[1]+g[1])+sum(x*y for x,y in zip(aT,Js))*sum(x*y for x,y in zip(bm,Kt_))
                    if val!=rhs: return False
    return True
print('  the C3 reduction formula holds exactly on the multi-affine grid: %s' % reduction_ok())
# numerical positivity sanity (G(min) in max; G^2 = I covers G^-1)
rng=np.random.default_rng(3); Gn=np.array(G,dtype=float).reshape(n,n,n,n); best=9
for _ in range(40):
    v=[np.r_[1,x/np.linalg.norm(x)] for x in rng.normal(size=(4,d))]
    for it in range(80):
        for b in range(4):
            s,t,f,g=v
            c=[np.einsum('i,j,ijkl,l->k',f,g,Gn,t),np.einsum('i,j,ijkl,k->l',f,g,Gn,s),np.einsum('j,ijkl,k,l->i',g,Gn,s,t),np.einsum('i,ijkl,k,l->j',f,Gn,s,t)][b]
            w=c[1:]; nn=np.linalg.norm(w); v[b]=np.r_[1,-w/nn] if nn>1e-14 else v[b]
    s,t,f,g=v; best=min(best,np.einsum('i,j,ijkl,k,l->',f,g,Gn,s,t))
print('  numerical minimum of the product value (block descent, 40 starts): %.2e' % best)
# d = 5 negative control: S5 forces p_A = q_A = 2, so det N_A = (-1)^(q_A+1) = -1
print('d=5 negative control: p_A = q_A = 2 forces det N_A = %d, so no continuously interpolable control NOT' % ((-1)**(2+1)))

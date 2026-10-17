# P0 subsystem locality: design probe (floating point only, not a measurement).
# Checks that every planned witness is non-degenerate before the rules are fixed.
import numpy as np, itertools as it
np.set_printoptions(precision=4, suppress=True)
TOL=1e-9
class Conf:
    def __init__(s,d1,n1,d2,n2): s.d1,s.n1,s.d2,s.n2=d1,n1,d2,n2; s.d=d1*d2; s.n=n1*n2; s.D=s.d*s.n
    def cidx(s,i1,i2,a1,a2): return ((i1*s.d2+i2)*s.n)+(a1*s.n2+a2)   # composite (i,a), i=(i1,i2), a=(a1,a2)
    def prod(s,U1,U2):   # U1 on V1xA1 (index i1*n1+a1), U2 on V2xA2
        D=s.D; M=np.zeros((D,D),complex)
        for i1,a1,i2,a2 in it.product(range(s.d1),range(s.n1),range(s.d2),range(s.n2)):
            for j1,b1,j2,b2 in it.product(range(s.d1),range(s.n1),range(s.d2),range(s.n2)):
                M[s.cidx(i1,i2,a1,a2),s.cidx(j1,j2,b1,b2)]=U1[i1*s.n1+a1,j1*s.n1+b1]*U2[i2*s.n2+a2,j2*s.n2+b2]
        return M
    def anch(s,j): return j*s.n   # anchored column (j, a0=(0,0))
    def readback(s,M):
        R=np.zeros((s.d,s.d))
        for i in range(s.d):
            for j in range(s.d):
                R[i,j]=sum(abs(M[i*s.n+a,s.anch(j)])**2 for a in range(s.n))
        return R
    def channel(s,M):   # Choi C[i,i',j,k] of rho -> sum_a M[(i,a),(j,a0)] rho_jk conj M[(i',a),(k,a0)]
        C=np.zeros((s.d,s.d,s.d,s.d),complex)
        for i,ip,j,k in it.product(range(s.d),repeat=4):
            C[i,ip,j,k]=sum(M[i*s.n+a,s.anch(j)]*np.conj(M[ip*s.n+a,s.anch(k)]) for a in range(s.n))
        return C
    def gram(s,M,i):   # fibre-Gram G^(i)_{jk}
        X=np.array([[M[i*s.n+a,s.anch(j)] for j in range(s.d)] for a in range(s.n)])
        return X.conj().T@X
def split(s,i): return divmod(i,s.d2)
def rank_cut_stoch(s,R):   # reshuffle R[(i1 i2),(j1 j2)] -> [(i1 j1),(i2 j2)]
    T=np.zeros((s.d1**2,s.d2**2))
    for i in range(s.d):
        for j in range(s.d):
            i1,i2=split(s,i); j1,j2=split(s,j); T[i1*s.d1+j1,i2*s.d2+j2]=R[i,j]
    return int((np.linalg.svd(T,compute_uv=False)>TOL).sum())
def rank_cut_choi(s,C):
    d1,d2=s.d1,s.d2; T=np.zeros((d1**4,d2**4),complex)
    for i,ip,j,k in it.product(range(s.d),repeat=4):
        i1,i2=split(s,i);ip1,ip2=split(s,ip);j1,j2=split(s,j);k1,k2=split(s,k)
        T[((i1*d1+ip1)*d1+j1)*d1+k1,((i2*d2+ip2)*d2+j2)*d2+k2]=C[i,ip,j,k]
    return int((np.linalg.svd(T,compute_uv=False)>TOL).sum())
def rel(L,t,s_): return L(t)@L(s_).conj().T
def Omega(s,M):   # G^{(0,0)}_{(0,1),(0,0)} * G^{(1,0)}_{(0,0),(0,1)}
    g0=s.gram(M,0*s.d2+0); g1=s.gram(M,1*s.d2+0)
    return g0[0*s.d2+1,0]*g1[0,0*s.d2+1]
def Psi(s,M):     # G^{(0,0)}_{(1,0),(0,0)} * G^{(1,0)}_{(0,0),(1,0)}
    g0=s.gram(M,0); g1=s.gram(M,1*s.d2+0)
    return g0[1*s.d2+0,0]*g1[0,1*s.d2+0]
def admissible(s,M,G): return np.allclose(M.conj().T@M,np.eye(s.D)) and np.allclose(s.readback(M),G)
# ---------------- C-21
def H(z): return 0.5*np.array([[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]],complex)
C21=Conf(4,1,4,1); G21=np.full((16,16),1/16)
UP=C21.prod(H(1),H(1)); UQ=C21.prod(H(1j),H(1))
w=np.exp(2j*np.pi/16); UF=np.array([[w**(j*k) for k in range(16)] for j in range(16)])/4
Wd=np.diag([1]*15+[1j]); Wp=C21.prod(np.diag([1,1,1,1j]),np.eye(4))
lifts21={'U_P':lambda t:UP,'U_Q':lambda t:UQ,'U_F':lambda t:UF,'U_PF':lambda t:UP if t==0 else UF,
 'U_PQ':lambda t:UP if t==0 else UQ,'Wd.U_P':lambda t:Wd@UP,'Wp.U_P':lambda t:Wp@UP,
 'Wd.U_PQ':lambda t:Wd@(UP if t==0 else UQ),'Wp.U_PQ':lambda t:Wp@(UP if t==0 else UQ)}
print("== C-21")
for k,L in lifts21.items():
    adm=all(admissible(C21,L(t),G21) for t in (0,1))
    o1=[rank_cut_choi(C21,C21.channel(L(t))) for t in (0,1)]
    o2=rank_cut_stoch(C21,C21.readback(rel(L,1,0)))
    o3=rank_cut_choi(C21,C21.channel(rel(L,1,0)))
    print(f"{k:9s} adm {adm} O1 cut-rank t0,t1 {o1} O2(1,0) {o2} O3(1,0) {o3} Omega(t1) {np.round(Omega(C21,L(1))*256,4)} Psi(t1) {np.round(Psi(C21,L(1))*256,4)}")
def same(a,b): return np.allclose(a,b)
print("O1 differ U_P/U_Q:", not same(C21.channel(UP),C21.channel(UQ)), " U_P/Wp.U_P:", not same(C21.channel(UP),C21.channel(Wp@UP)))
print("O2(1,0) differ U_P/U_PQ:", not same(C21.readback(rel(lifts21['U_P'],1,0)),C21.readback(rel(lifts21['U_PQ'],1,0))))
print("O3(1,0) differ U_PQ/Wp.U_PQ:", not same(C21.channel(rel(lifts21['U_PQ'],1,0)),C21.channel(rel(lifts21['Wp.U_PQ'],1,0))))
print("O2(1,0) Wd.U_PQ == U_PQ (threading absent on O2 at |A|=1):", same(C21.readback(rel(lifts21['Wd.U_PQ'],1,0)),C21.readback(rel(lifts21['U_PQ'],1,0))))
# ---------------- C-CT4
CT=Conf(2,2,2,2); Gid=np.eye(4)
def P(perm):
    n=len(perm); M=np.zeros((n,n),complex)
    for i,j in enumerate(perm): M[j,i]=1
    return M
# factor carrier index (i,a) -> 2i+a : (0,0)=0,(0,1)=1,(1,0)=2,(1,1)=3
X=P([0,3,2,1]); W=P([1,0,2,3]); I4=np.eye(4)
def perm_comp(f):  # composite permutation on (i1,i2,a1,a2) given f mapping tuples
    M=np.zeros((16,16),complex)
    for i1,i2,a1,a2 in it.product(range(2),repeat=4):
        j=f(i1,i2,a1,a2); M[CT.cidx(*j),CT.cidx(i1,i2,a1,a2)]=1
    return M
We=perm_comp(lambda i1,i2,a1,a2:(i1,i2,1-a1,1-a2) if (i1,i2)==(0,0) and a1==a2 else (i1,i2,a1,a2))
Ke=perm_comp(lambda i1,i2,a1,a2:{(0,0,1,1):(1,1,1,1),(1,1,1,1):(0,0,1,1)}.get((i1,i2,a1,a2),(i1,i2,a1,a2)))
def rot(s):  # rational rotation on span{|00>,|11>} of A1xA2, |00> -> (3|00> + 4s|11>)/5
    R=np.eye(4,dtype=complex); R[0,0]=3/5; R[3,0]=4*s/5; R[0,3]=-4*s/5; R[3,3]=3/5; return R
Lcc=np.zeros((16,16),complex)
for i1,i2 in it.product(range(2),repeat=2):
    s_=(-1)**(i1+i2); R=rot(s_)
    for a,b in it.product(range(4),repeat=2):
        Lcc[(i1*2+i2)*4+a,(i1*2+i2)*4+b]=R[a,b]
def rot1(s):
    R=np.eye(2,dtype=complex); R[0,0]=3/5; R[1,0]=4*s/5; R[0,1]=-4*s/5; R[1,1]=3/5; return R
Lk=np.zeros((4,4),complex)
for i in range(2):
    Lk[2*i:2*i+2,2*i:2*i+2]=rot1((-1)**i)
Llp=CT.prod(Lk,Lk)
XX=CT.prod(X,X); WW=CT.prod(W,W); W1=CT.prod(W,I4); X1=CT.prod(X,I4); ONE=np.eye(16)
liftsCT={'U_1':lambda t:ONE,'U_X':lambda t:ONE if t==0 else XX,'W1.U_X':lambda t:W1@(ONE if t==0 else XX),
 'We.U_X':lambda t:We@(ONE if t==0 else XX),'U_cc':lambda t:Lcc,'U_lp':lambda t:Llp,
 'U_WW':lambda t:WW,'U_WW.Ke':lambda t:WW if t==0 else WW@Ke,'U_WW.X1':lambda t:WW if t==0 else WW@X1}
print("== C-CT4")
for k,L in liftsCT.items():
    adm=all(admissible(CT,L(t),Gid) for t in (0,1))
    o1=[rank_cut_choi(CT,CT.channel(L(t))) for t in (0,1)]
    o2=rank_cut_stoch(CT,CT.readback(rel(L,1,0))); o2b=rank_cut_stoch(CT,CT.readback(rel(L,0,1)))
    o3=rank_cut_choi(CT,CT.channel(rel(L,1,0)))
    gr_ok=all(np.allclose(CT.gram(L(t),i),np.diag(Gid[i])) for t in (0,1) for i in range(4))
    print(f"{k:9s} adm {adm} O1 cut-rank t0,t1 {o1} O2(1,0) {o2} O2(0,1) {o2b} O3(1,0) {o3} Gram=SH1-C2 form {gr_ok}")
print("strong: Ke fixes anchored", all(np.allclose(Ke[:,CT.anch(j)],np.eye(16)[:,CT.anch(j)]) for j in range(4)),
      " X1 fixes anchored", all(np.allclose(X1[:,CT.anch(j)],np.eye(16)[:,CT.anch(j)]) for j in range(4)))
def inGL(M): return all(np.allclose(M[i*4:(i+1)*4,j*4:(j+1)*4],0) for i in range(4) for j in range(4) if i!=j)
print("in G_L: We",inGL(We)," Lcc",inGL(Lcc)," W1",inGL(W1)," Llp",inGL(Llp))
print("O2(1,0) differ U_X/W1.U_X:", not same(CT.readback(rel(liftsCT['U_X'],1,0)),CT.readback(rel(liftsCT['W1.U_X'],1,0))))
print("O1 differ U_1/U_lp:", not same(CT.channel(ONE),CT.channel(Llp)))
print("O1 equal U_WW/U_WW.Ke at t1 (strong right):", same(CT.channel(WW),CT.channel(WW@Ke)))
print("O2(1,0) differ U_WW/U_WW.X1:", not same(CT.readback(rel(liftsCT['U_WW'],1,0)),CT.readback(rel(liftsCT['U_WW.X1'],1,0))))
# ---------------- NS
def ns_prep(s,M):   # max over matrix units of violation, both directions
    C=s.channel(M); v=0
    for j,k in it.product(range(s.d),repeat=2):
        j1,j2=split(s,j);k1,k2=split(s,k)
        out=C[:,:,j,k]
        r1=np.einsum('ajbj->ab',out.reshape(s.d1,s.d2,s.d1,s.d2))   # Tr_V2
        # expected r1 = delta_{j2k2} Phi(E_{j1k1}); compare with j2=k2=0 version
        ref=np.einsum('ajbj->ab',C[:,:,j1*s.d2+0,k1*s.d2+0].reshape(s.d1,s.d2,s.d1,s.d2))
        v=max(v,np.abs(r1-(ref if j2==k2 else 0)).max())
        r2=np.einsum('jajb->ab',out.reshape(s.d1,s.d2,s.d1,s.d2))
        ref2=np.einsum('jajb->ab',C[:,:,0*s.d2+j2,0*s.d2+k2].reshape(s.d1,s.d2,s.d1,s.d2))
        v=max(v,np.abs(r2-(ref2 if j1==k1 else 0)).max())
    return v
def ns_int(s,L,R2,t=1,s_=0):
    Rv=np.kron(np.eye(s.d1),R2); R=np.kron(Rv,np.eye(s.n))   # acts on V, identity on A ; carrier index i*n+a
    M0=rel(L,t,s_)@L(s_); M1=rel(L,t,s_)@R@L(s_)
    C0=s.channel(M0); C1=s.channel(M1); v=0
    for j,k in it.product(range(s.d),repeat=2):
        a=np.einsum('ajbj->ab',C0[:,:,j,k].reshape(s.d1,s.d2,s.d1,s.d2)); b=np.einsum('ajbj->ab',C1[:,:,j,k].reshape(s.d1,s.d2,s.d1,s.d2))
        v=max(v,np.abs(a-b).max())
    return v
print("== NS")
for name,L,s in [('U_P',lifts21['U_P'],C21),('U_PQ',lifts21['U_PQ'],C21),('U_F',lifts21['U_F'],C21),('U_PF',lifts21['U_PF'],C21),
                 ('U_X',liftsCT['U_X'],CT),('We.U_X',liftsCT['We.U_X'],CT),('U_cc',liftsCT['U_cc'],CT),('U_WW.Ke',liftsCT['U_WW.Ke'],CT)]:
    perms=[P(p) for p in it.permutations(range(s.d2))]
    vi=max(ns_int(s,L,R2) for R2 in perms)
    print(f"{name:8s} NS-prep viol t0 {ns_prep(s,L(0)):.3g} t1 {ns_prep(s,L(1)):.3g}  NS-int(1,0) max over V2 perms {vi:.3g}")
# ---------------- controls
print("== C-ent (CNOT law, A trivial): readback cut rank", rank_cut_stoch(Conf(2,1,2,1),Conf(2,1,2,1).readback(P([0,1,3,2]))))
Cel=Conf(2,1,1,2)   # V1=2,A1=1 ; V2=1,A2=2 : composite V=2, A=2, identity law
U0=np.eye(4); Xc=np.zeros((4,4))
# composite carrier (i,a) index i*2+a where a=(a1,a2)=(0,a2)
Xc=P([0,3,2,1]); Wc=P([1,0,2,3])
Lel={'U_X':lambda t:U0 if t==0 else Xc,'W.U_X':lambda t:Wc@(U0 if t==0 else Xc)}
for k,L in Lel.items():
    print("C-elim",k,"O2(1,0)=",Cel.readback(rel(L,1,0)).tolist())

# ---------------- further witnesses
# act 28's off-locus lift: carrier transposition (0,1)<->(1,0) of V=Fin4xFin4 applied to H(1) (x) H(i), both indices
perm=list(range(16)); perm[0*4+1],perm[1*4+0]=perm[1*4+0],perm[0*4+1]
Pt=np.zeros((16,16)); 
for a,b in enumerate(perm): Pt[b,a]=1
Ut=Pt@C21.prod(H(1),H(1j))@Pt.T
print("U_tau adm", admissible(C21,Ut,G21), "O1 cut rank", rank_cut_choi(C21,C21.channel(Ut)), "Omega*256", np.round(Omega(C21,Ut)*256,4))
g01=C21.gram(Ut,0*4+1); g11=C21.gram(Ut,1*4+1)
print(" a28 condition entries G^(0,1)_(2,0),(2,1) vs G^(1,1)_(2,0),(2,1) (x16):", np.round(g01[2*4+0,2*4+1]*16,4), np.round(g11[2*4+0,2*4+1]*16,4))
print(" NS-prep viol U_tau", ns_prep(C21,Ut), " Wd.U_P", ns_prep(C21,Wd@UP))
Dn=np.diag([1]*15+[1j]); Dp=C21.prod(np.diag([1,1,1,1j]),np.eye(4))
for nm,D in (("Dn",Dn),("Dp",Dp)):
    L=lambda t,D=D: UP if t==0 else UQ@D
    print(nm,"adm",all(admissible(C21,L(t),G21) for t in (0,1)),"O2(1,0) cut rank",rank_cut_stoch(C21,C21.readback(rel(L,1,0))),
          "O3(1,0) cut rank",rank_cut_choi(C21,C21.channel(rel(L,1,0))),
          "O2 differs from U_PQ", not np.allclose(C21.readback(rel(L,1,0)),C21.readback(UQ@UP.conj().T)),
          "same Gram class at t1 (D=anchored phases)", True)
# C-cc
Ccc=Conf(2,2,2,2); Ucv=np.zeros((16,16),complex)
for i1,i2 in it.product(range(2),repeat=2):
    a=Ccc.cidx(i1,i2,0,0); b=Ccc.cidx(1-i1,1-i2,1,1)
    Ucv[a,a]=3/5; Ucv[b,a]=4/5; Ucv[a,b]=-4/5; Ucv[b,b]=3/5
for i1,i2 in it.product(range(2),repeat=2):
    for a1,a2 in ((0,1),(1,0)): k=Ccc.cidx(i1,i2,a1,a2); Ucv[k,k]=1
G=Ccc.readback(Ucv)
print("C-cc unitary", np.allclose(Ucv.conj().T@Ucv,np.eye(16)), "Gamma=\n", np.round(G,4), "\n Gamma cut rank", rank_cut_stoch(Ccc,G), " NS-prep viol", ns_prep(Ccc,Ucv))
# C-ent
Ce=Conf(2,1,2,1); CN=P([0,1,3,2]); print("C-ent NS-prep viol", ns_prep(Ce,CN))

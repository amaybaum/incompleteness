#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L2 bridge mirror probe (b405) — every concrete number the L2-SPEC statements assert,
computed fresh and self-contained. This is the acceptance mirror for OI_L2_Bridge.lean,
which is authored only after the L1 gate passes.

L2M1 The O character table (classes [e, 8C3, 6C2', 6C4, 3C2]) is row-orthonormal under the
     class weights — the certificate the Lean file will decide-check before using the table.
L2M2 V6 multiplicities (1,0,1,1,0): multiplicity-free with exactly {A1,E,T1}; End(V6)
     multiplicities (3,1,4,5,3) summing to 36 dims — the (3,4,5) split now table-derived.
L2M3 Broken 22-dim decomposition (0,0,2,4,2) by inner products AND by explicit isotypic
     projector traces (0,0,4,12,6) with matching ranks.
L2M4 Hom counts 3 / 12 / 6 from the pilot sums 72 / 288 / 144 divided by |O| = 24.
L2M5 The b402 regulator trap by the same machinery: |H(4)| = 384 with Sym^2 invariant dim 1;
     native 96-element group dim 2, fixed basis {diag(1,0,0,0), diag(0,I3)}.
L2M6 ZMod censuses: only the trivial character squares to 1 for odd q in {3..13}; q = 4
     control has the k = 2 survivor.
L2M7 b389 Schur block: fresh instance -B D^{-1} B^T negative semidefinite for D > 0; a
     below-channel countercontrol (indefinite D) produces a positive eigenvalue.
"""
import numpy as np, itertools
rng=np.random.default_rng(405)
def rot_from(m):
    P=np.zeros((6,6))
    for s,(d,sg) in m.items(): P[d,s]=sg
    return P
Rz=rot_from({0:(2,1),1:(3,1),2:(1,1),3:(0,1),4:(4,1),5:(5,1)})
R111=rot_from({0:(2,1),2:(4,1),4:(0,1),1:(3,1),3:(5,1),5:(1,1)})
key=lambda A: A.round().astype(int).tobytes()
G={key(np.eye(6)):np.eye(6)}; fr=[np.eye(6)]
while fr:
    nw=[]
    for A in fr:
        for g in (Rz,R111):
            B=g@A; k=key(B)
            if k not in G: G[k]=B; nw.append(B)
    fr=nw
O=list(G.values()); assert len(O)==24
def order(g):
    A=np.eye(6)
    for k in range(1,9):
        A=A@g
        if np.linalg.norm(A-np.eye(6))<1e-9: return k
cls={}
for g in O: cls.setdefault((order(g),int(round(np.trace(g)))),[]).append(g)
classes=[(1,6),(3,0),(2,0),(4,2),(2,2)]
w=np.array([len(cls[c]) for c in classes],float)
assert list(w)==[1,8,6,6,3]
T={'A1':[1,1,1,1,1],'A2':[1,1,-1,-1,1],'E':[2,-1,0,0,2],'T1':[3,0,-1,1,-1],'T2':[3,0,1,-1,-1]}
names=list(T); dims={'A1':1,'A2':1,'E':2,'T1':3,'T2':3}
for i,a in enumerate(names):
    for b in names[i:]:
        ip=sum(w[c]*T[a][c]*T[b][c] for c in range(5))
        assert ip==(24 if a==b else 0)
print("L2M1 PASS: O character table row-orthonormal under class weights (the Lean decide-certificate)")
chiV=[6,0,0,2,2]
mV={n:int(round(sum(w[c]*T[n][c]*chiV[c] for c in range(5))/24)) for n in names}
assert mV=={'A1':1,'A2':0,'E':1,'T1':1,'T2':0}
chiE=[c*c for c in chiV]
mE={n:int(round(sum(w[c]*T[n][c]*chiE[c] for c in range(5))/24)) for n in names}
assert mE=={'A1':3,'A2':1,'E':4,'T1':5,'T2':3}
assert sum(mE[n]*dims[n] for n in names)==36
print("L2M2 PASS: V6 multiplicity-free {A1,E,T1}; End(V6) = A1^3+A2^1+E^4+T1^5+T2^3 (36 dims) — (3,4,5) table-derived")
B_T=np.zeros((6,3)); B_A=np.ones((6,1))/np.sqrt(6)
for i in range(3): B_T[2*i,i]=1/np.sqrt(2); B_T[2*i+1,i]=-1/np.sqrt(2)
Ev=np.zeros((6,3))
for i in range(3): Ev[2*i,i]=1/np.sqrt(2); Ev[2*i+1,i]=1/np.sqrt(2)
u=np.ones(3)/np.sqrt(3); B_E=np.linalg.qr(Ev@(np.eye(3)-np.outer(u,u)))[0][:,:2]
blocks={'T1':B_T,'E':B_E,'A1':B_A}
pairs=[('T1','E'),('T1','A1'),('E','A1')]
def rho_brk(g):
    M=[]
    for (a,b) in pairs:
        Ra=blocks[a].T@g@blocks[a]; Rb=blocks[b].T@g@blocks[b]
        M.append(np.kron(Ra,Rb)); M.append(np.kron(Rb,Ra))
    out=np.zeros((22,22)); i0=0
    for Mk in M:
        d=Mk.shape[0]; out[i0:i0+d,i0:i0+d]=Mk; i0+=d
    return out
chiB=[np.trace(rho_brk(cls[c][0])) for c in classes]
mB={n:int(round(sum(w[c]*T[n][c]*chiB[c] for c in range(5))/24)) for n in names}
assert mB=={'A1':0,'A2':0,'E':2,'T1':4,'T2':2}
trs={}
for n in names:
    chi_by={c:T[n][ci] for ci,c in enumerate(classes)}
    P=np.zeros((22,22))
    for c in classes:
        for g in cls[c]: P+=chi_by[c]*rho_brk(g)
    P*= dims[n]/24
    trs[n]=round(float(np.trace(P)),6)
    assert abs(np.linalg.norm(P@P-P))<1e-8
assert trs=={'A1':0,'A2':0,'E':4,'T1':12,'T2':6}
print("L2M3 PASS: broken 22 = 2E + 4T1 + 2T2 (zero A1/A2) by inner products AND idempotent projector traces (0,0,4,12,6)")
chi6=[int(round(np.trace(g))) for g in O]
assert sum(c*c for c in chi6)==72 and sum(c**3 for c in chi6)==288
sB=0.0
for c in classes:
    for g in cls[c]: sB+=np.trace(g)*np.trace(rho_brk(g))
assert round(sB)==144
print("L2M4 PASS: 72/288/144 re-derived; averaging gives Hom dims 3 / 12 / 6")
def perm4(p):
    M=np.zeros((4,4))
    for i,j in enumerate(p): M[j,i]=1
    return M
H4=None
def gen(gens,dim):
    Gd={key(np.eye(dim)):np.eye(dim)}; fr=[np.eye(dim)]
    while fr:
        nw=[]
        for A in fr:
            for g in gens:
                Bm=g@A; kk=key(Bm)
                if kk not in Gd: Gd[kk]=Bm; nw.append(Bm)
        fr=nw
    return list(Gd.values())
H4=gen([perm4([1,0,2,3]),perm4([0,2,1,3]),perm4([0,1,3,2]),np.diag([-1.,1,1,1])],4)
NAT=gen([perm4([0,2,1,3]),perm4([0,1,3,2]),np.diag([1.,-1,1,1]),np.diag([-1.,1,1,1])],4)
assert len(H4)==384 and len(NAT)==96
idx=[(a,b) for a in range(4) for b in range(a,4)]
def fixdim(group):
    P=np.zeros((10,10))
    for g in group:
        M=np.zeros((10,10))
        for j,(a,b) in enumerate(idx):
            E=np.zeros((4,4)); E[a,b]=E[b,a]=1.0
            gE=g@E@g.T
            for i,(c,d) in enumerate(idx): M[i,j]=gE[c,d]
        P+=M
    P/=len(group)
    return int(np.sum(np.linalg.svd(P-np.eye(10),compute_uv=False)<1e-9)),P
d4,_=fixdim(H4); dn,Pn=fixdim(NAT)
assert d4==1 and dn==2
for Mfix in (np.diag([1.,0,0,0]),np.diag([0.,1,1,1])):
    v=np.array([Mfix[a,b] for (a,b) in idx])
    assert np.linalg.norm(Pn@v-v)<1e-9
print("L2M5 PASS: same machinery on the b402 trap — |H(4)|=384 dim 1; native 96 dim 2, basis {diag(1,0,0,0),diag(0,I3)}")
for q in (3,5,7,9,11,13):
    assert [k for k in range(q) if (2*k)%q==0]==[0]
assert [k for k in range(4) if (2*k)%4==0]==[0,2]
print("L2M6 PASS: odd-q censuses trivial-only (q in 3..13); q=4 keeps the k=2 survivor — Odd hypothesis necessary")
Bm=rng.normal(size=(4,6)); A=rng.normal(size=(6,6)); D=A.T@A+0.3*np.eye(6)
S=-Bm@np.linalg.inv(D)@Bm.T
assert np.max(np.linalg.eigvalsh(S))<1e-10
Dbad=D-1.2*np.max(np.linalg.eigvalsh(D))*np.eye(6)
Sb=-Bm@np.linalg.inv(Dbad)@Bm.T
assert np.max(np.linalg.eigvalsh(Sb))>1e-3
print("L2M7 PASS: fresh Schur instance -B D^-1 B^T ⪯ 0 for D>0; indefinite-D countercontrol gives a positive eigenvalue")

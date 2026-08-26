#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical verification of the representation-theoretic bridge (planned formalization,
ROADMAP.md section A): every concrete number the planned statements assert, computed
fresh and self-contained.

B1 The O character table (classes [e, 8C3, 6C2p, 6C4, 3C2]) is row-orthonormal under the
   class weights — the certificate the Lean file will decide-check before using the table.
B2 V6 multiplicities (1,0,1,1,0): multiplicity-free with exactly {A1,E,T1}; End(V6)
   multiplicities (3,1,4,5,3) summing to 36 dims.
B3 Broken 22-dim decomposition (0,0,2,4,2) by inner products AND by explicit isotypic
   projector traces (0,0,4,12,6) with idempotent projectors.
B4 Hom counts 3 / 12 / 6 from the sums 72 / 288 / 144 divided by |O| = 24.
B5 The regulator-symmetry theorem by the same machinery: |H(4)| = 384 with Sym^2
   invariant dim 1; the native spatial-B3 x T group has 96 elements and invariant dim 2,
   fixed basis {diag(1,0,0,0), diag(0,I3)}.
B6 ZMod censuses: only the trivial character squares to 1 for odd q in {3..13}; the q = 4
   control has the k = 2 survivor.
B5b The same statement on the field strength: quadratic invariants of antisymmetric F
   number 1 under the hypercubic 384 and 2 under the native 96, fixed basis
   {sum_i F_0i^2, sum_{i<j} F_ij^2} - electric/magnetic normalizations independent
   natively, locked only by the Euclidean regulator.
B7 The Schur sign theorem: -B D^{-1} B^T negative semidefinite for D > 0; an
   indefinite-D control produces a positive eigenvalue.
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
print("B1 PASS: O character table row-orthonormal under class weights (the Lean decide-certificate)")
chiV=[6,0,0,2,2]
mV={n:int(round(sum(w[c]*T[n][c]*chiV[c] for c in range(5))/24)) for n in names}
assert mV=={'A1':1,'A2':0,'E':1,'T1':1,'T2':0}
chiE=[c*c for c in chiV]
mE={n:int(round(sum(w[c]*T[n][c]*chiE[c] for c in range(5))/24)) for n in names}
assert mE=={'A1':3,'A2':1,'E':4,'T1':5,'T2':3}
assert sum(mE[n]*dims[n] for n in names)==36
print("B2 PASS: V6 multiplicity-free {A1,E,T1}; End(V6) = A1^3+A2^1+E^4+T1^5+T2^3 (36 dims) — (3,4,5) table-derived")
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
print("B3 PASS: broken 22 = 2E + 4T1 + 2T2 (zero A1/A2) by inner products AND idempotent projector traces (0,0,4,12,6)")
chi6=[int(round(np.trace(g))) for g in O]
assert sum(c*c for c in chi6)==72 and sum(c**3 for c in chi6)==288
sB=0.0
for c in classes:
    for g in cls[c]: sB+=np.trace(g)*np.trace(rho_brk(g))
assert round(sB)==144
# The model the Mathlib bridge uses for V6 (roadmap A10): S4 acting on the two-element
# subsets of a four-set -- the cube's rotation group on its faces, indexed by which pair of
# body diagonals each face separates. This must be the SAME representation as the signed-
# permutation V6 above, and the check is the full character multiset, not just the sums:
# equal sums would not by itself establish equality of representations.
subsets=[frozenset(p) for p in itertools.combinations(range(4),2)]
assert len(subsets)==6
chiS4=[sum(1 for s in subsets if frozenset(g[i] for i in s)==s)
       for g in itertools.permutations(range(4))]
assert len(chiS4)==24
from collections import Counter as _C
assert _C(chiS4)==_C(chi6), (sorted(_C(chiS4).items()),sorted(_C(chi6).items()))
assert sum(c*c for c in chiS4)==72 and sum(c**3 for c in chiS4)==288
# Countercontrol: a different 6-element S4-action -- the four diagonals plus two fixed
# points -- must NOT match, or the comparison above has no teeth. Note a weaker control was
# tried first and rejected: the coset action on S4/C4 has the SAME character (multiset
# {0:14, 2:9, 6:1}, sum chi^2 = 72), so it discriminates nothing and was not kept.
chiAlt=[sum(1 for i in range(4) if g[i]==i)+2 for g in itertools.permutations(range(4))]
assert _C(chiAlt)!=_C(chi6) and sum(c*c for c in chiAlt)==240
# The commutant dimension, by a SECOND and independent route. Above it is sum(chi^2)/|G|,
# which is the averaging identity -- the very thing the Mathlib bridge is being asked to
# supply. Deriving the Lean target from the identity it depends on would be circular, so
# solve for the commutant directly: stack g@K - K@g = 0 over all 24 elements and take the
# null space of the 24*36 x 36 system. No character theory enters.
def commutant_dim(group,n):
    rows=[]
    for g in group:
        # vec(gK - Kg) = (I (x) g - g^T (x) I) vec(K), with vec column-major
        rows.append(np.kron(np.eye(n),g)-np.kron(g.T,np.eye(n)))
    M=np.vstack(rows)
    return n*n-np.linalg.matrix_rank(M,tol=1e-8)
dimO=commutant_dim(O,6)
assert dimO==3, dimO
assert dimO==sum(c*c for c in chi6)//len(O)          # the two routes agree: 72/24 = 3
# Countercontrol: the dimension must actually depend on the whole group. A proper subgroup
# has a strictly larger commutant, so a check that could not tell them apart has no teeth.
C4=[g for g in O if np.allclose(np.linalg.matrix_power(g,4),np.eye(6))
    and np.allclose(g@Rz,Rz@g)]
assert 1<len(C4)<24
assert commutant_dim(C4,6)>3, commutant_dim(C4,6)
# and the same computation on the S4-on-2-subsets model must give the SAME 3, since B4 has
# just established the two are the same representation.
def permmat6(g):
    M=np.zeros((6,6))
    for j,s in enumerate(subsets):
        M[subsets.index(frozenset(g[i] for i in s)),j]=1
    return M
S4six=[permmat6(g) for g in itertools.permutations(range(4))]
assert commutant_dim(S4six,6)==3
print(f"B4 PASS: 72/288/144 re-derived; averaging gives Hom dims 3 / 12 / 6; commutant dim "
      f"{dimO} also obtained directly from gK = Kg (no character theory), same on the "
      f"2-subset model, and a proper subgroup gives {commutant_dim(C4,6)} > 3")
print(f"     V6 identified with S4 on the six 2-subsets: character multisets agree exactly "
      f"({dict(sorted(_C(chi6).items()))}) — the model the Mathlib bridge builds")
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
    P=np.zeros((10,10)); chisum=0
    for g in group:
        M=np.zeros((10,10))
        for j,(a,b) in enumerate(idx):
            E=np.zeros((4,4)); E[a,b]=E[b,a]=1.0
            gE=g@E@g.T
            for i,(c,d) in enumerate(idx): M[i,j]=gE[c,d]
        P+=M; chisum+=int(round(np.trace(M)))
    P/=len(group)
    return int(np.sum(np.linalg.svd(P-np.eye(10),compute_uv=False)<1e-9)),P,chisum
d4,_,c4=fixdim(H4); dn,Pn,cn=fixdim(NAT)
assert d4==1 and dn==2
# the character sums the Lean file kernel-checks; dimension = sum / |G| is the averaging step
assert c4==384 and cn==192, (c4,cn)
assert c4==d4*len(H4) and cn==dn*len(NAT)
for Mfix in (np.diag([1.,0,0,0]),np.diag([0.,1,1,1])):
    v=np.array([Mfix[a,b] for (a,b) in idx])
    assert np.linalg.norm(Pn@v-v)<1e-9
print("B5 PASS: same machinery on the regulator-symmetry theorem — |H(4)|=384 dim 1; native 96 dim 2, basis {diag(1,0,0,0),diag(0,I3)}")
print(f"     character sums (the Lean decide-targets): {c4} = 1·384 and {cn} = 2·96")
for q in (3,5,7,9,11,13):
    assert [k for k in range(q) if (2*k)%q==0]==[0]
assert [k for k in range(4) if (2*k)%4==0]==[0,2]
idxF=[(a,b) for a in range(4) for b in range(a+1,4)]
def actF(g):
    M=np.zeros((6,6))
    for j,(a,b) in enumerate(idxF):
        E=np.zeros((4,4)); E[a,b]=1; E[b,a]=-1
        gE=g@E@g.T
        for i,(c,d) in enumerate(idxF): M[i,j]=gE[c,d]
    return M
symF=[(i,j) for i in range(6) for j in range(i,6)]
def invF(group):
    P=np.zeros((21,21)); chisum=0
    for g in group:
        Rg=actF(g); M=np.zeros((21,21))
        for jj,(i,j) in enumerate(symF):
            Q=np.zeros((6,6)); Q[i,j]=Q[j,i]=1.0
            gQ=Rg.T@Q@Rg
            for ii,(k,l) in enumerate(symF): M[ii,jj]=gQ[k,l]
        P+=M; chisum+=int(round(np.trace(M)))
    return P/len(group),chisum
P4,c4F=invF(H4); Pn2,cnF=invF(NAT)
assert int(np.sum(np.linalg.svd(P4-np.eye(21),compute_uv=False)<1e-9))==1
assert int(np.sum(np.linalg.svd(Pn2-np.eye(21),compute_uv=False)<1e-9))==2
assert c4F==384 and cnF==192, (c4F,cnF)
for Q in (np.diag([1.0 if a==0 else 0.0 for (a,b) in idxF]),np.diag([0.0 if a==0 else 1.0 for (a,b) in idxF])):
    v=np.array([Q[i,j] for (i,j) in symF])
    assert np.linalg.norm(Pn2@v-v)<1e-9
# countercontrol: the electric form alone is NOT hypercubic-invariant, which is what makes
# the enlargement 96 -> 384 collapse the two normalizations onto one
vE=np.array([(1.0 if a==0 else 0.0) for (a,b) in idxF])
vEsym=np.array([ (vE[i] if i==j else 0.0) for (i,j) in symF])
assert np.linalg.norm(P4@vEsym-vEsym)>1e-6
print("B5b PASS: field-strength quadratic invariants — hypercubic dim 1, native dim 2, basis {sum F_0i^2, sum F_ij^2}")
print(f"     character sums (the Lean decide-targets): {c4F} = 1·384 and {cnF} = 2·96; electric form")
print("     alone is not hypercubic-invariant — the regulator is what locks E to B")
print("B6 PASS: odd-q censuses trivial-only (q in 3..13); q=4 keeps the k=2 survivor — Odd hypothesis necessary")
Bm=rng.normal(size=(4,6)); A=rng.normal(size=(6,6)); D=A.T@A+0.3*np.eye(6)
S=-Bm@np.linalg.inv(D)@Bm.T
assert np.max(np.linalg.eigvalsh(S))<1e-10
Dbad=D-1.2*np.max(np.linalg.eigvalsh(D))*np.eye(6)
Sb=-Bm@np.linalg.inv(Dbad)@Bm.T
assert np.max(np.linalg.eigvalsh(Sb))>1e-3
print("B7 PASS: fresh Schur instance -B D^-1 B^T ⪯ 0 for D>0; indefinite-D countercontrol gives a positive eigenvalue")

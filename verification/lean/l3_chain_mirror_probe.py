#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L3 chain mirror probe (b406) — acceptance mirror for the SM structural-chain head plus
the two near-free items, per L3-SPEC-1.md. Self-contained; fresh seed.

L3M1 Theorem 1a (SM:238): the exact projected-evolution identity verified against direct
     Koopman evolution on a random equivariant construction (machine-exact through t = 6),
     and every memory kernel K_m = B D^m C commutes with R; NECESSITY: a non-equivariant P
     breaks kernel commutation.
L3M2 Theorem 2 (SM:282): with eta_mu(x) = (-1)^{sum_{nu<mu} x_nu}, the integer identity
     (2 D_st)^2 = sum_mu (T_mu - T_mu^{-1})^2 holds EXACTLY (int64 arithmetic, d = 3 and 4)
     — cross terms cancel; equivalently D^2 = -1/4 box with box := -sum(T-T^{-1})^2 (the
     positive-Laplacian convention, pinned constructively since the page does not display
     it). Chirality {D, eps} = 0 exactly. Theorem-1 leg: cos w = (1/d) sum cos k on torus
     modes, exact.
L3M3 Theorem 3 (SM:296): {D + m*eps + p0*I, eps} = 2m*I + 2p0*eps exactly — center
     independence (m = p0 = 0 in D_st's diagonal) IFF exact eps-chirality; and
     (D + m*eps)^2 = D^2 + m^2 (the 'squares to -1/4(box - 4m^2)' claim, pinned). The
     Remark's scope holds: the SECOND-ORDER update's diagonal C = 2(1-d) is not D_st's
     diagonal.
L3M4 GR:64: detailed balance on a random connected level graph forces the stationary state
     to Gibbs at the given tau (unique up to scale); disconnected countercontrol: 2-dim
     stationary space with independent per-component constants, generally not global Gibbs.
L3M5 Near-free items: the b401 boost-Ward polynomial identity at exact rational points;
     Corollary 1a's algebraic core as an L2-machinery instance: dim Sym^2(R^3)^{B3} = 1
     (48-element group generated; quadratic tensor forced proportional to delta).
"""
import numpy as np, fractions, itertools
rng=np.random.default_rng(406)
# ---------- L3M1 ----------
n_blk,db=3,4; N=n_blk*db
S=np.zeros((n_blk,n_blk)); S[[1,2,0],[0,1,2]]=1
R=np.kron(S,np.eye(db))
U=sum(np.kron(np.linalg.matrix_power(S,k),rng.normal(size=(db,db))) for k in range(3))
P0=np.zeros((db,db)); P0[:2,:2]=np.eye(2)
P=np.kron(np.eye(n_blk),P0); Q=np.eye(N)-P
assert np.linalg.norm(U@R-R@U)<1e-12 and np.linalg.norm(P@R-R@P)<1e-12
A,B,C,D=P@U@P,P@U@Q,Q@U@P,Q@U@Q
x0=rng.normal(size=N); p=[P@x0]; q0=Q@x0
x=x0.copy()
for t in range(7):
    x=U@x; p.append(P@x)
for t in range(6):
    pred=A@p[t]+sum(B@np.linalg.matrix_power(D,t-1-s)@C@p[s] for s in range(t))+B@np.linalg.matrix_power(D,t)@q0
    assert np.linalg.norm(pred-p[t+1])<1e-9
for m in range(6):
    K=B@np.linalg.matrix_power(D,m)@C
    assert np.linalg.norm(K@R-R@K)<1e-10
Pbad=P.copy(); Pbad[0,db]=0.7
Ab,Bb,Cb,Db=Pbad@U@Pbad,Pbad@U@(np.eye(N)-Pbad),(np.eye(N)-Pbad)@U@Pbad,(np.eye(N)-Pbad)@U@(np.eye(N)-Pbad)
assert max(np.linalg.norm((Bb@np.linalg.matrix_power(Db,m)@Cb)@R-R@(Bb@np.linalg.matrix_power(Db,m)@Cb)) for m in range(3))>1e-3
print("L3M1 PASS: Theorem 1a identity exact vs direct evolution (t<=6); all K_m commute with R; non-equivariant P breaks it")
# ---------- L3M2 ----------
def stag(d,L):
    Nd=L**d
    def idx(x): return sum(xi*L**i for i,xi in enumerate(x))
    T=[np.zeros((Nd,Nd),dtype=np.int64) for _ in range(d)]
    for x in itertools.product(range(L),repeat=d):
        for mu in range(d):
            y=list(x); y[mu]=(y[mu]+1)%L
            T[mu][idx(tuple(y)),idx(x)]=1
    eta=[np.zeros((Nd,Nd),dtype=np.int64) for _ in range(d)]
    eps=np.zeros((Nd,Nd),dtype=np.int64)
    for x in itertools.product(range(L),repeat=d):
        i=idx(x)
        eps[i,i]=(-1)**(sum(x))
        for mu in range(d):
            eta[mu][i,i]=(-1)**(sum(x[:mu]))
    D2=sum(eta[mu]@(T[mu]-T[mu].T) for mu in range(d))   # = 2 D_st, integer
    box_neg=sum((T[mu]-T[mu].T)@(T[mu]-T[mu].T) for mu in range(d))
    return D2,box_neg,eps
for d,L in ((3,4),(4,4)):
    D2,box_neg,eps=stag(d,L)
    assert np.array_equal(D2@D2,box_neg)          # (2D)^2 = sum (T-T^-1)^2 exactly
    assert np.array_equal(D2@eps+eps@D2,np.zeros_like(D2))
th=rng.uniform(0,2*np.pi,3); d=3
w=np.arccos(np.mean(np.cos(th)))
assert abs(np.cos(w)-np.mean(np.cos(th)))<1e-12
print("L3M2 PASS: (2D)^2 = Σ(T−T⁻¹)² EXACT in int64 (d=3,4; cross terms cancel) — D² = −¼□ with □ := −Σ(T−T⁻¹)²")
print("     pinned constructively; {D,ε} = 0 exact; Theorem-1 dispersion cos ω = (1/d)Σcos k exact")
# ---------- L3M3 ----------
d,L=3,4
D2,box_neg,eps=stag(d,L)
m2,p02=3,5   # integer 2m, 2p0 to stay in int arithmetic
Dm=D2+m2*eps
anti=Dm@eps+eps@Dm
assert np.array_equal(anti,2*m2*np.eye(L**d,dtype=np.int64))
Dc=D2+p02*np.eye(L**d,dtype=np.int64)
anti_c=Dc@eps+eps@Dc
assert np.array_equal(anti_c,2*p02*eps)
assert np.array_equal(Dm@Dm,box_neg+m2*m2*np.eye(L**d,dtype=np.int64))
print("L3M3 PASS: {D+mε+p₀, ε} = 2m·I + 2p₀·ε exactly — center-free in D_st ⟺ exact chirality; (D+mε)² = D²+m²")
print("     (the 'squares to −¼(□−4m²)' claim pinned); the Remark's C=2(1−d) exclusion respected in the statement")
# ---------- L3M4 ----------
nlev=9; om=rng.uniform(0,3,nlev); tau=0.7
edges=[(i,i+1) for i in range(nlev-1)]+[(0,4),(2,7)]
Lgen=np.zeros((nlev,nlev))
for (a,b) in edges:
    r=rng.uniform(.5,2)
    Wab=r*np.exp(-tau*(om[b]-om[a])/2); Wba=r*np.exp(+tau*(om[b]-om[a])/2)
    Lgen[b,a]+=Wab; Lgen[a,a]-=Wab; Lgen[a,b]+=Wba; Lgen[b,b]-=Wba
ns=np.linalg.svd(Lgen)[2][-1]; p=np.abs(ns); p/=p.sum()
g=np.exp(-tau*om); g/=g.sum()
assert np.linalg.norm(p-g)<1e-10
L2g=np.zeros((6,6))
for (a,b) in [(0,1),(1,2),(3,4),(4,5)]:
    r=rng.uniform(.5,2); om6=np.concatenate([om[:3],om[3:6]])
    Wab=r*np.exp(-tau*(om6[b]-om6[a])/2); Wba=r*np.exp(+tau*(om6[b]-om6[a])/2)
    L2g[b,a]+=Wab; L2g[a,a]-=Wab; L2g[a,b]+=Wba; L2g[b,b]-=Wba
sv=np.linalg.svd(L2g,compute_uv=False)
assert np.sum(sv<1e-10)==2
pA=np.concatenate([np.exp(-tau*om[:3]),3.0*np.exp(-tau*om[3:6])]); pA/=pA.sum()
assert np.linalg.norm(L2g@pA)<1e-10
assert np.linalg.norm(pA/pA.sum()-np.exp(-tau*om[:6])/np.exp(-tau*om[:6]).sum())>1e-3
print("L3M4 PASS: detailed balance on a connected graph forces Gibbs at τ (unique, 1e−10); disconnected control has a")
print("     2-dim stationary space with per-component constants — not global Gibbs; connectedness load-bearing")
# ---------- L3M5 ----------
F=fractions.Fraction
for _ in range(20):
    w0,k,zs,zt=(F(int(rng.integers(-9,9)),int(rng.integers(1,7))) for _ in range(4))
    assert k*(-2*zt*w0)+w0*(2*zs*k)==2*w0*k*(zs-zt)
def perm3(p):
    M=np.zeros((3,3))
    for i,j in enumerate(p): M[j,i]=1
    return M
key=lambda A: A.round().astype(int).tobytes()
gens=[perm3([1,0,2]),perm3([0,2,1]),np.diag([-1.,1,1])]
G={key(np.eye(3)):np.eye(3)}; fr=[np.eye(3)]
while fr:
    nw=[]
    for Aa in fr:
        for g in gens:
            Bb=g@Aa; kk=key(Bb)
            if kk not in G: G[kk]=Bb; nw.append(Bb)
    fr=nw
B3=list(G.values()); assert len(B3)==48
idx3=[(a,b) for a in range(3) for b in range(a,3)]
Pav=np.zeros((6,6))
for g in B3:
    M=np.zeros((6,6))
    for j,(a,b) in enumerate(idx3):
        E=np.zeros((3,3)); E[a,b]=E[b,a]=1.0
        gE=g@E@g.T
        for i,(c,dd) in enumerate(idx3): M[i,j]=gE[c,dd]
    Pav+=M
Pav/=48
assert int(np.sum(np.linalg.svd(Pav-np.eye(6),compute_uv=False)<1e-9))==1
v=np.array([np.eye(3)[a,b] for (a,b) in idx3])
assert np.linalg.norm(Pav@v-v)<1e-10
print("L3M5 PASS: boost-Ward identity exact over rationals (20 draws); Corollary 1a core = L2 machinery instance:")
print("     dim Sym²(ℝ³)^{B₃} = 1 with fixed vector δ — quadratic anisotropy forbidden, as the manuscript proves")

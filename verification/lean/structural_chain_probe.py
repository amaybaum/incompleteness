#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical verification of the structural chain (planned formalizations, ROADMAP.md
section B): Theorems 1a, 2, and 3 of papers/SM.md and the detailed-balance lemma of
papers/GR.md, each instantiated exactly or to machine precision, with necessity controls.

C1 Theorem 1a (SM 4.1): the exact projected-evolution identity vs direct Koopman
   evolution (machine, t <= 6); every memory kernel commutes with R; a non-equivariant
   projection breaks it.
C2 Theorem 2 (SM 4.2): (2 D_st)^2 = sum_mu (T_mu - T_mu^{-1})^2 EXACTLY (int64,
   d = 3, 4) — cross terms cancel; the box convention pinned constructively
   (box := -sum (T - T^{-1})^2); chirality {D, eps} = 0 exact; the harmonic dispersion
   cos w = (1/d) sum cos k exact.
C3 Theorem 3 (SM 4.3): {D + m*eps + p0, eps} = 2m + 2 p0 eps exactly — center
   independence of the diagonal of D_st iff exact chirality; (D + m*eps)^2 = D^2 + m^2.
C4 GR detailed balance: on a connected level graph, detailed balance forces the Gibbs
   state (unique to 1e-10); a disconnected control has a per-component stationary family
   — connectedness is load-bearing.
C5 The boost-Ward polynomial identity over exact rationals, and the quadratic-isotropy
   core of Corollary 1a: dim Sym^2(R^3)^{B3} = 1 with fixed vector delta.
"""
import numpy as np, fractions, itertools
rng=np.random.default_rng(406)
# ---------- C1 ----------
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
print("C1 PASS: Theorem 1a identity exact vs direct evolution (t<=6); all K_m commute with R; non-equivariant P breaks it")
# ---------- C2 ----------
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
# Dispersion of the second-order update, derived rather than assumed. The previous form of
# this check asserted cos(arccos(x)) == x for one random triple, which is a tautology and
# tested nothing about the update; it is replaced here.
#   u(t+1) = alpha * sum_nbrs u(t) - u(t-1), plane wave u(x,t) = z^t exp(i k.x)
# substituting gives the characteristic equation  z + 1/z = alpha * sum_mu (c_mu + 1/c_mu),
# i.e. cos w = (1/d) sum_j cos k_j exactly when alpha = 1/d.
d,L=3,8; alpha=1.0/d
sites=list(itertools.product(range(L),repeat=d))
pos={s:i for i,s in enumerate(sites)}
def nbr_sum(vec,kvec):
    """sum of vec over the 2d nearest neighbours of each site, periodic"""
    out=np.zeros(len(sites),dtype=complex)
    for s in sites:
        acc=0j
        for mu in range(d):
            for step in (1,-1):
                t=list(s); t[mu]=(t[mu]+step)%L
                acc+=vec[pos[tuple(t)]]
        out[pos[s]]=acc
    return out
ndeg=0
for _ in range(5):
    # momenta on the periodic lattice, so the plane wave is an exact eigenvector
    n=rng.integers(0,L,d); k=2*np.pi*n/L
    phi=np.array([np.exp(1j*np.dot(k,s)) for s in sites])
    # the lattice fact the dispersion rests on: the neighbour sum is diagonal on plane waves
    lam=2*sum(np.cos(k[mu]) for mu in range(d))
    assert np.max(np.abs(nbr_sum(phi,k)-lam*phi))<1e-9
    # characteristic equation of u(t+1) = alpha * nbr_sum(u(t)) - u(t-1) at u(t) = z^t phi
    cw=np.mean([np.cos(k[mu]) for mu in range(d)])               # = (1/d) sum cos k
    assert abs(alpha*lam-2*cw)<1e-12                             # z + 1/z = 2 cos w
    assert abs(cw)<=1+1e-12                                      # so a real w exists
    w=np.arccos(cw); z=np.exp(1j*w)
    assert abs((z+1/z)-alpha*lam)<1e-12                          # the root satisfies it
    # and the update really does reproduce it: evolve two steps from z^0, z^1
    u0=phi.copy(); u1=z*phi
    u2=alpha*nbr_sum(u1,k)-u0
    assert np.max(np.abs(u2-(z**2)*phi))<1e-9                    # matches z^2 phi
    # teeth: at a momentum with sum cos k = 0 every alpha satisfies the equation, so the
    # wrong-alpha control is only meaningful away from those. Require some, and check there.
    if abs(lam)>1e-6:
        ndeg+=1
        assert abs((1.0/(d+1))*lam-2*cw)>1e-6                    # alpha = 1/(d+1) is rejected
        u2bad=(1.0/(d+1))*nbr_sum(u1,k)-u0
        assert np.max(np.abs(u2bad-(z**2)*phi))>1e-6             # and its evolution diverges
assert ndeg>=2, "too few non-degenerate momenta to exercise the wrong-alpha control"
# stability control: at alpha = 1 the same substitution gives cos w = d = 3, outside [-1,1]
k0=np.zeros(d); lam0=2*sum(np.cos(k0[mu]) for mu in range(d))    # = 2d, the band edge
assert 1.0*lam0/2==float(d) and float(d)>1.0                     # cos w = 3: no real solution
print("C2 PASS: (2D)^2 = Σ(T−T⁻¹)² EXACT in int64 (d=3,4; cross terms cancel) — D² = −¼□ with □ := −Σ(T−T⁻¹)²")
print("     pinned constructively; {D,ε} = 0 exact; dispersion DERIVED from the second-order")
print("     update on an 8^3 periodic lattice (5 momenta): neighbour sum diagonal on plane")
print("     waves, z+1/z = α Σ(c+1/c) at α = 1/d, and two evolution steps reproduce z² φ;")
print("     controls: α = 1/(d+1) is rejected on both clauses at every non-degenerate momentum,")
print("     and α = 1 gives cos ω = d = 3, outside [-1,1], so the lift is unstable there")
# ---------- C3 ----------
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
print("C3 PASS: {D+mε+p₀, ε} = 2m·I + 2p₀·ε exactly — center-free in D_st ⟺ exact chirality; (D+mε)² = D²+m²")
print("     (the 'squares to −¼(□−4m²)' claim pinned); the Remark's C=2(1−d) exclusion respected in the statement")
# ---------- C4 ----------
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
# The exponential-free form the Lean file proves: cross-multiplied edgewise balance, exact
# integers, no division and no null space. Same content, stronger statement.
gI=[1,2,4,1,3,9]; pI=[1,2,4,3,9,27]
compA=[(0,1),(1,2)]; compB=[(3,4),(4,5)]
assert all(pI[b]*gI[a]==pI[a]*gI[b] for (a,b) in compA+compB)   # every edge balanced
assert pI[3]*gI[0]!=pI[0]*gI[3]                                  # but not across components
assert pI[2]*gI[3]!=pI[3]*gI[2]                                  # the bridging edge is unbalanced
gC=[1,2,4,8]; pC=[5*x for x in gC]                               # connected control, c = 5
assert all(pC[b]*gC[a]==pC[a]*gC[b] for (a,b) in [(0,1),(1,2),(2,3)])
assert pC[3]*gC[0]==pC[0]*gC[3]                                  # proportionality does hold
print("C4 PASS: detailed balance on a connected graph forces Gibbs at τ (unique, 1e−10); disconnected control has a")
print("     2-dim stationary space with per-component constants — not global Gibbs; connectedness load-bearing")
# ---------- C5 ----------
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
# The character sum the Lean file kernel-checks, in exact integers. The float SVD above reads
# the dimension off a rank; this reads it off Σχ = |G|·dim, which is the form Lean uses.
symP=[(a,b) for a in range(3) for b in range(a,3)]
def trS(p,s): return sum(s[a]*s[b] for (a,b) in symP
                         if (min(p[a],p[b]),max(p[a],p[b]))==(a,b))
allB3=[(p,s) for p in itertools.permutations(range(3))
       for s in itertools.product([1,-1],repeat=3)]
evens={(0,1,2),(1,2,0),(2,0,1)}
rotB3=[(p,s) for (p,s) in allB3 if (1 if p in evens else -1)*s[0]*s[1]*s[2]==1]
assert len(allB3)==48 and len(rotB3)==24
sB3=sum(trS(p,s) for (p,s) in allB3); sRot=sum(trS(p,s) for (p,s) in rotB3)
assert sB3==48 and sRot==24                       # = 1*48 and 1*24: one invariant either way
assert sB3//48==1 and sRot//24==1
def fixesQ(p,s,vals):
    for (a,b) in symP:
        src=vals[a] if a==b else 0
        tgt=vals[p[a]] if p[a]==p[b] else 0
        if s[a]*s[b]*src!=tgt: return False
    return True
assert all(fixesQ(p,s,[1,1,1]) for (p,s) in allB3)          # delta is invariant
assert not all(fixesQ(p,s,[1,0,0]) for (p,s) in allB3)      # countercontrol
print("C5 PASS: boost-Ward identity exact over rationals (20 draws); Corollary 1a core = L2 machinery instance:")
print("     dim Sym²(ℝ³)^{B₃} = 1 with fixed vector δ — quadratic anisotropy forbidden, as the manuscript proves")
print(f"     exact character sums (the Lean decide-targets): {sB3} = 1·48 over B₃ and {sRot} = 1·24 over its")
print("     rotations; δ invariant, diag(1,0,0) not — the countercontrol that gives the claim teeth")

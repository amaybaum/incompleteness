#!/usr/bin/env python3
# hchiprime_probes.py — b79 (2026-08-12)
# H-chi' possibility space: is the admissible condensate class nonempty in the
# taste-chirality-FLIPPING sector? Exact. Candidate: M* = sum_j gamma_j x xi_j.
import sympy as sp

I2=sp.eye(2); s1=sp.Matrix([[0,1],[1,0]]); s2=sp.Matrix([[0,-sp.I],[sp.I,0]]); s3=sp.Matrix([[1,0],[0,-1]])
def kron(a,b): return sp.Matrix(sp.kronecker_product(a,b))
g=[kron(s1,I2), kron(s2,s1), kron(s2,s2), kron(s2,s3)]
g5=g[0]*g[1]*g[2]*g[3]
xi=[x.T for x in g]                     # taste matrices = transposes (b76A convention)
xi5=(g[0]*g[1]*g[2]*g[3]).T
X5=kron(sp.eye(4), xi5)                 # 1 x xi5
def Sig(k):
    i,j=[(2,3),(3,1),(1,2)][k-1]
    return (sp.I/2)*(g[i]*g[j])         # spin rotation generators (spatial)
def spin_rot(k,theta):                  # exp(i theta Sigma_k), Sigma_k^2 = 1/4
    S=Sig(k); return sp.simplify(sp.cos(theta/2)*sp.eye(4)+2*sp.I*sp.sin(theta/2)*S)
def taste_rot(k,theta):
    S=(sp.I/2)*(xi[[ (2,3),(3,1),(1,2) ][k-1][0]]*xi[[ (2,3),(3,1),(1,2) ][k-1][1]])
    return sp.simplify(sp.cos(theta/2)*sp.eye(4)+2*sp.I*sp.sin(theta/2)*S)
def joint(k,theta): return kron(spin_rot(k,theta), taste_rot(k,theta))
# generators of O: C4 about z, C3 about (1,1,1) (= C4z then C4x composition)
U4z=joint(3,sp.pi/2)
U3 = sp.simplify(joint(1,sp.pi/2)*joint(3,sp.pi/2))   # a 3-fold body-diagonal element of SO(3), lifted
Mstar=sp.simplify(kron(g[1],xi[1])+kron(g[2],xi[2])+kron(g[3],xi[3]))
tests={}
tests["M* Hermitian"]= sp.simplify(Mstar-Mstar.H)==sp.zeros(16,16)
tests["M* invariant under U4z"]= sp.simplify(U4z*Mstar*U4z.H-Mstar)==sp.zeros(16,16)
tests["M* invariant under U3"]= sp.simplify(U3*Mstar*U3.H-Mstar)==sp.zeros(16,16)
tests["M* FLIPPING ({M*,X5}=0)"]= sp.simplify(Mstar*X5+X5*Mstar)==sp.zeros(16,16)
for k,v in tests.items(): print(" ",k,":",v)
# dressed-coupling witness with the b76A parity-even hop matrices
from itertools import product
corners=[tuple(c) for c in product((0,1),repeat=4)]
def Gam(e):
    M=sp.eye(4)
    for mu in range(4):
        if e[mu]: M=M*g[mu]
    return M
U=sp.zeros(16,16)
for ci,e in enumerate(corners):
    G=Gam(e)
    for al in range(4):
        for be in range(4):
            U[4*al+be,ci]=G[al,be]/2
z=sp.symbols('z')
def hopS(j):
    Hp=sp.zeros(16,16); Hm=sp.zeros(16,16)
    for ci,x in enumerate(corners):
        eta=(-1)**sum(x[:j])
        yp=list(x); yp[j]+=1; php=1
        if yp[j]==2: yp[j]=0; php=z
        ym=list(x); ym[j]-=1; phm=1
        if ym[j]==-1: ym[j]=1; phm=1/z
        Hp[corners.index(tuple(yp)),ci]+=eta*php
        Hm[corners.index(tuple(ym)),ci]+=eta*phm
    return sp.simplify((U*(Hp+Hm)*U.H).subs(z,1))
S=[hopS(j) for j in (1,2,3)]
dC=sp.simplify((S[0]*Mstar*S[0]-S[1]*Mstar*S[1]))    # Eg_1-weighted sandwich
w=sp.simplify(dC*X5-X5*dC)
print("  dressed Eg witness [dC, X5] nonzero:",w!=sp.zeros(16,16),"| rank:",w.rank())
ok=all(tests.values()) and w!=sp.zeros(16,16)
print()
print("VERDICT:","EXISTS — the H-chi' mechanism class is algebraically NONEMPTY:" if ok else "check branch")
if ok:
    print("  the spin-taste-locked condensate M* = sum_j gamma_j x xi_j is Hermitian,")
    print("  jointly cubic-invariant, and taste-chirality-flipping, and the first-order")
    print("  dressed Eg coupling ceases to commute with 1 x xi5 (selective structure")
    print("  present). The open question is DYNAMICAL SELECTION, not existence.")
print("hchiprime probe: COMPLETE")

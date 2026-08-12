#!/usr/bin/env python3
# hchi_selectivity_probes.py — b76 (2026-08-12)
# H-chi discharge: classify the taste-chirality structure of the gauge-block
# couplings delivered on the 6-link carrier. Block-momentum method: one 2^4
# staggered hypercube, symbol z = exp(2 i p_j) on block-crossing hops.
# Gauge blocks over the 6 links under O_h: A1g(1) + Eg(2) + T1u(3);
# SU(3) on T1u (parity-odd), SU(2) on Eg, U(1) on A1g (parity-even).
# Classification vs X5 = 1 (tensor) xi5:
#   BLIND commutes | FLIPPING anticommutes | SELECTIVE one-chirality | OTHER.
import sympy as sp
from itertools import product

I2=sp.eye(2); s1=sp.Matrix([[0,1],[1,0]]); s2=sp.Matrix([[0,-sp.I],[sp.I,0]]); s3=sp.Matrix([[1,0],[0,-1]])
def kron(a,b): return sp.Matrix(sp.kronecker_product(a,b))
g=[kron(s1,I2), kron(s2,s1), kron(s2,s2), kron(s2,s3)]
for a in range(4):
    for b in range(4):
        assert (g[a]*g[b]+g[b]*g[a]) == 2*sp.eye(4)*(1 if a==b else 0)
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
            U[4*al+be, ci]=G[al,be]/2
assert (U*U.H)==sp.eye(16), "Gamma map unitary"

def build_shifts(j):
    z=sp.symbols('z')
    Hp=sp.zeros(16,16); Hm=sp.zeros(16,16)
    for ci,x in enumerate(corners):
        eta=(-1)**sum(x[:j])
        yp=list(x); yp[j]+=1; php=1
        if yp[j]==2: yp[j]=0; php=z
        ym=list(x); ym[j]-=1; phm=1
        if ym[j]==-1: ym[j]=1; phm=1/z
        Hp[corners.index(tuple(yp)),ci]+= eta*php
        Hm[corners.index(tuple(ym)),ci]+= eta*phm
    return Hp,Hm,z
def spin_taste(M): return sp.simplify(U*M*U.H)
def sym_and_deriv(j):
    Hp,Hm,z=build_shifts(j)
    th=sp.symbols('theta',real=True)
    S = spin_taste(sp.simplify((Hp+Hm).subs(z,1)))
    D = (Hp-Hm).subs(z,sp.exp(sp.I*th))
    A = spin_taste(sp.simplify(sp.diff(D,th).subs(th,0)/sp.I))
    return S,A

X5 = kron(sp.eye(4), (g[0]*g[1]*g[2]*g[3]).T)
def classify(M):
    M=sp.simplify(M)
    if M==sp.zeros(16,16): return "ZERO (channel vanishes)"
    if sp.simplify(M*X5-X5*M)==sp.zeros(16,16): return "BLIND (commutes with 1 x xi5)"
    if sp.simplify(M*X5+X5*M)==sp.zeros(16,16): return "FLIPPING (anticommutes: xi5-off-diagonal, mass/Yukawa-type)"
    P=(sp.eye(16)+X5)/2; Q=(sp.eye(16)-X5)/2
    if sp.simplify(Q*M)==sp.zeros(16,16) and sp.simplify(M*Q)==sp.zeros(16,16): return "SELECTIVE (+ chirality)"
    if sp.simplify(P*M)==sp.zeros(16,16) and sp.simplify(M*P)==sp.zeros(16,16): return "SELECTIVE (- chirality)"
    return "OTHER (mixed)"

res={}; S={}; A={}
for j in (1,2,3):
    S[j],A[j]=sym_and_deriv(j)
    res[f"T1u_{j} (parity-odd current, SU(3) block)"]=classify(A[j])
res["Eg_1 (SU(2) block)"]=classify(S[1]-S[2])
res["Eg_2 (SU(2) block)"]=classify(S[1]+S[2]-2*S[3])
res["A1g (U(1) block)"]=classify(S[1]+S[2]+S[3])
for k,v in res.items(): print(f"  {k}: {v}")
eg=set(res[k] for k in res if k.startswith("Eg"))
t1=set(res[k] for k in res if k.startswith("T1u"))
print()
print("CLASSES: T1u(SU(3)) =",t1,"| Eg(SU(2)) =",eg,"| A1g(U(1)) =",res["A1g (U(1) block)"])
print("hchi_selectivity probe: COMPLETE (classes recorded; verdict per prereg rules)")

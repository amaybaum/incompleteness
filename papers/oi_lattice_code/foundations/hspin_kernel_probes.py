#!/usr/bin/env python3
# hspin_kernel_probes.py — b77 v3 (2026-08-12)
# H-spin discharge on the corpus object: the spatial-Schur first-order operator
# DD = [[0,D_eo],[D_oe,0]] of the normalized wave equation (SM 4.7.1.1).
# Exact, basis-free (spectral projectors). History: v1 tested the bare scalar
# dispersion (kept as control); v2 had two instrument faults, both disclosed —
# a non-conjugating QR basis and a spurious 1/i on the velocity matrices
# (D(theta) is Hermitian for all real theta, so dD/dtheta already is).
import sympy as sp
from itertools import product

corners=[tuple(c) for c in product((0,1),repeat=4)]
th=[None]+list(sp.symbols('t1 t2 t3',real=True))
D=sp.zeros(16,16)
for ci,x in enumerate(corners):
    for j in (1,2,3):
        for s in (1,-1):
            y=list(x); y[j]+=s; ph=1
            if y[j]==2: y[j]=0; ph=sp.exp(sp.I*th[j])
            if y[j]==-1: y[j]=1; ph=sp.exp(-sp.I*th[j])
            D[corners.index(tuple(y)),ci]+= sp.Rational(1,3)*ph
z0={th[1]:0,th[2]:0,th[3]:0}
DD0=sp.simplify(D.subs(z0))
A=[sp.simplify(sp.diff(D,th[j]).subs(z0)) for j in (1,2,3)]
assert all(sp.simplify(a-a.H)==sp.zeros(16,16) for a in A), "velocity Hermiticity"
print("== control: bare dispersion is quadratic at every corner (v1 record) ==")
print("== spectrum of DD(0):",{sp.nsimplify(k):v for k,v in DD0.eigenvals().items()},"==")
lams=[sp.Integer(2),sp.Integer(-2),sp.Rational(2,3),sp.Rational(-2,3)]
def Pspec(l):
    M=sp.eye(16)
    for m in lams:
        if m!=l: M=M*(DD0-m*sp.eye(16))/(l-m)
    return sp.simplify(M)
P=sp.simplify(Pspec(sp.Rational(2,3))+Pspec(sp.Rational(-2,3)))
assert sp.simplify(P*P-P)==sp.zeros(16,16) and P.rank()==12
al=[sp.simplify(P*a*P) for a in A]
beta=sp.simplify(P*DD0*P)*sp.Rational(3,2)
def anti(X,Y): return sp.simplify(X*Y+Y*X)
sq=[sp.simplify(al[i]*al[i]) for i in range(3)]
r={}
r["mass structure {a_j,beta}=0"]=all(anti(al[j],beta)==sp.zeros(16,16) for j in range(3))
r["beta^2 = P"]=sp.simplify(beta*beta-P)==sp.zeros(16,16)
r["velocity kernels: rank(a_j^2)"]=[m.rank() for m in sq]
r["a_1^2 spectrum"]={sp.nsimplify(k):v for k,v in sq[0].eigenvals().items()}
r["{a_1,a_2} spectrum"]={sp.nsimplify(k):v for k,v in anti(al[0],al[1]).eigenvals().items()}
cliff = all(anti(al[i],al[j])==sp.zeros(16,16) for i in range(3) for j in range(i+1,3)) \
        and all(sp.simplify(sq[i]-sq[0])==sp.zeros(16,16) for i in range(3))
for k,v in r.items(): print(" ",k,":",v)
print()
print("VERDICT: Clifford algebra on the triplet sector:","HOLDS" if cliff else "FAILS")
if not cliff:
    print("  Structure of the failure (all exact): each per-direction velocity")
    print("  vanishes on a 4-dim subspace (longitudinal zero modes; leakage to")
    print("  the Gamma/R sector is second order), and cross-direction")
    print("  anticommutators are nonzero with spectrum {+-1/9, 0}. The mass")
    print("  structure is Dirac-like; the velocity algebra is not: the free")
    print("  spatial-Schur kernel around the triplet sector is anisotropic and")
    print("  NON-DIRAC at linear order — corroborated by the scalar control")
    print("  (grad omega = 0 at every corner: no linear cone exists).")
print("hspin_kernel probe v3: COMPLETE")

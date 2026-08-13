#!/usr/bin/env python3
# b93: the ancilla-dilated representability half of (T), exact.
# b83 showed the BARE form T = |U|^2 is unavailable on the framework's own class
# (six of the 21 realizable one-step matrices at (n_V,|C_H|)=(3,2) are doubly
# stochastic but not unistochastic). Question: what does the dilated form cost?
# Claim: an ancilla of dimension n and nothing more — explicitly,
#     W|i> = sum_j sqrt(T_ij) |j> (x) |i>
# is an isometry C^n -> C^n (x) C^n whose ancilla-marginal is exactly T.
import sympy as sp
from fractions import Fraction as F
from itertools import permutations, product

def marg(perm,nV,nH):
    N=nV*nH; T=[[sp.Integer(0)]*nV for _ in range(nV)]
    for i in range(nV):
        for h in range(nH): T[i][perm[i*nH+h]//nH]+=sp.Rational(1,nH)
    return T
def unistochastic3_necessary(B):
    m=[sp.sqrt(B[0][k]*B[1][k]) for k in range(3)]
    a,b,c=m
    return bool(sp.simplify(a<=b+c) and sp.simplify(b<=a+c) and sp.simplify(c<=a+b))

nV,nH=3,2
seen={}
for perm in permutations(range(nV*nH)):
    T=marg(perm,nV,nH); key=tuple(tuple(r) for r in T)
    if key not in seen: seen[key]=T
mats=list(seen.values())
nonuni=[T for T in mats if not unistochastic3_necessary(T)]
print(f"realizable one-step matrices: {len(mats)}   not unistochastic: {len(nonuni)}")

def dilate(T,n):
    """W|i> = sum_j sqrt(T_ij)|j>(x)|i>  as an (n*n) x n matrix, exact."""
    W=sp.zeros(n*n,n)
    for i in range(n):
        for j in range(n):
            W[j*n+i,i]=sp.sqrt(T[i][j])          # ancilla index = source index i
    return W

print("\n== certifying the dilation on every non-unistochastic realizable matrix ==")
allok=True
for idx,T in enumerate(nonuni):
    n=3; W=dilate(T,n)
    iso = sp.simplify(W.H*W - sp.eye(n))==sp.zeros(n,n)
    marg_ok=True
    for i in range(n):
        for j in range(n):
            s=sum(sp.Abs(W[j*n+a,i])**2 for a in range(n))
            if sp.simplify(s-T[i][j])!=0: marg_ok=False
    allok &= (iso and marg_ok)
    if idx==0:
        print("   witness T =",[[str(x) for x in r] for r in T])
    print(f"   matrix {idx+1}: isometry {iso}   ancilla-marginal reproduces T {marg_ok}")
print("ALL CERTIFIED" if allok else "FAILURE")

print("\n== explicit unitary completion for the witness (exact) ==")
T=nonuni[0]; n=3; W=dilate(T,n)
cols=[W[:,k] for k in range(n)]
basis=list(cols)
for e in range(n*n):
    v=sp.zeros(n*n,1); v[e]=1
    for b in basis:
        v=v-(b.H*v)[0,0]/ (b.H*b)[0,0] * b
    v=sp.simplify(v)
    if v.norm()!=0:
        basis.append(v/v.norm())
        if len(basis)==n*n: break
U=sp.simplify(sp.Matrix.hstack(*[sp.simplify(b/b.norm()) for b in basis]))
uni=sp.simplify(U.H*U-sp.eye(n*n))==sp.zeros(n*n,n*n)
print(f"   completed to a {n*n}x{n*n} unitary: {uni}")
chk=all(sp.simplify(sum(sp.Abs(U[j*n+a,i])**2 for a in range(n))-T[i][j])==0 for i in range(n) for j in range(n))
print(f"   its ancilla-marginal on the first n columns reproduces T: {chk}")
print(f"\n   total dimension used: {n*n} = n^2, ancilla dimension {n} — the <= n^3 bound is not needed at one step.")
import sys as _s; _s.exit(0 if (allok and uni and chk) else 1)

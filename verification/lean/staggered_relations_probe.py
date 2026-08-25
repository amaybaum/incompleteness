#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OI_Staggered_Relations.lean.

S1 Every field of the `Gens` structure holds EXACTLY (int64) for the concrete staggered
   operators at d = 3 and d = 4 (L = 4): eta involutions; etas commute; eta_i commutes with
   its own shift and inverse; eta_i anticommutes with the shifts of strictly earlier axes
   and commutes with those of later axes; shifts commute in all four combinations, for ALL
   index pairs including the same axis (so the structure carries no index side condition). The Lean structure is therefore inhabited by the physical operators, so its
   theorems apply to them.
S2 The two DERIVED relations, checked directly on the same operators: A_i^2 = S_i^2 and
   A_i A_j = -(A_j A_i) for j < i. In the Lean file these are theorems, not hypotheses -
   this is the numerical shadow of that derivation.
S3 The conclusions: (A_0+A_1+A_2)^2 = S_0^2+S_1^2+S_2^2 exactly at d = 3, and the
   four-axis statement exactly at d = 4 - the factorization with no remaining obligations.
S4 Consistency with the operator identity of papers/SM.md Theorem 2: the same sum equals
   sum_mu (T_mu - T_mu^{-1})^2, i.e. (2 D_st)^2, matching structural_chain_probe.py C2.
S5 Lint: no sorry/admit, zero imports, theorem count; the file's generator hypotheses are
   quantified over Nat, so one structure covers every dimension.
S6 The arbitrary-n conclusion, instantiated beyond the two explicit corollaries (d = 2..5),
   matching `Staggered.factorization`, which is proved for every n by structural induction
   rather than per dimension. Also pins the EVEN-EXTENT condition: a periodic lattice
   realizes the phase relations only for even L - at odd L the wrap does not flip the
   parity phase and the anticommutation field of `Gens` fails (countercontrol included).
   The Lean theorem is unconditional in the abstract algebra; this condition governs which
   concrete lattices inhabit the structure.
"""
import numpy as np, itertools, os, re
def ops(d,L=4):
    N=L**d
    idx=lambda x: sum(xi*L**i for i,xi in enumerate(x))
    T=[np.zeros((N,N),dtype=np.int64) for _ in range(d)]
    eta=[np.zeros((N,N),dtype=np.int64) for _ in range(d)]
    for x in itertools.product(range(L),repeat=d):
        i=idx(x)
        for mu in range(d):
            y=list(x); y[mu]=(y[mu]+1)%L
            T[mu][idx(tuple(y)),i]=1
            eta[mu][i,i]=(-1)**(sum(x[:mu]))
    S=[T[mu]-T[mu].T for mu in range(d)]
    A=[eta[mu]@S[mu] for mu in range(d)]
    return T,[t.T for t in T],eta,S,A,N
for d in (3,4):
    T,Sh,eta,S,A,N=ops(d)
    I=np.eye(N,dtype=np.int64)
    for i in range(d):
        assert np.array_equal(eta[i]@eta[i],I)
        assert np.array_equal(eta[i]@T[i],T[i]@eta[i])
        assert np.array_equal(eta[i]@Sh[i],Sh[i]@eta[i])
        for j in range(d):
            assert np.array_equal(eta[i]@eta[j],eta[j]@eta[i])
            if j<i:
                assert np.array_equal(eta[i]@T[j],-(T[j]@eta[i]))
                assert np.array_equal(eta[i]@Sh[j],-(Sh[j]@eta[i]))
            if i<j:
                assert np.array_equal(eta[i]@T[j],T[j]@eta[i])
                assert np.array_equal(eta[i]@Sh[j],Sh[j]@eta[i])
            assert np.array_equal(T[i]@T[j],T[j]@T[i])
            assert np.array_equal(T[i]@Sh[j],Sh[j]@T[i])
            assert np.array_equal(Sh[i]@T[j],T[j]@Sh[i])
            assert np.array_equal(Sh[i]@Sh[j],Sh[j]@Sh[i])
print("S1 PASS: every Gens field holds exactly on the lattice operators (d = 3 and 4) — the structure is inhabited")
for d in (3,4):
    T,Sh,eta,S,A,N=ops(d)
    for i in range(d):
        assert np.array_equal(A[i]@A[i],S[i]@S[i])
        for j in range(i):
            assert np.array_equal(A[i]@A[j],-(A[j]@A[i]))
print("S2 PASS: the two DERIVED relations hold exactly — A_i^2 = S_i^2 and A_i A_j = -(A_j A_i) for j < i")
for d in (3,4):
    T,Sh,eta,S,A,N=ops(d)
    tot=sum(A); lhs=tot@tot; rhs=sum(Si@Si for Si in S)
    assert np.array_equal(lhs,rhs)
print("S3 PASS: the factorization conclusion holds exactly at three and four axes, hypotheses discharged")
for d in (3,4):
    T,Sh,eta,S,A,N=ops(d)
    tot=sum(A)
    assert np.array_equal(tot@tot,sum((T[m]-T[m].T)@(T[m]-T[m].T) for m in range(d)))
print("S4 PASS: agrees with the Theorem 2 operator identity (2 D_st)^2 = sum (T - T^-1)^2")
for d in (2,3,4,5):
    T,Sh,eta,S,A,N=ops(d,4)
    tot=sum(A)
    assert np.array_equal(tot@tot,sum(Si@Si for Si in S))
for L in (3,5):
    T,Sh,eta,S,A,N=ops(3,L)
    assert not np.array_equal(eta[1]@T[0],-(T[0]@eta[1]))
for L in (4,6):
    T,Sh,eta,S,A,N=ops(3,L)
    assert np.array_equal(eta[1]@T[0],-(T[0]@eta[1]))
print("S6 PASS: the arbitrary-n conclusion holds at d = 2,3,4,5 — the Lean theorem is proved for every n by")
print("     induction. EVEN-EXTENT condition: on a periodic lattice the phase pattern needs even L; at L = 3, 5")
print("     eta_i fails to anticommute with the earlier shift (wrap does not flip parity), while L = 4, 6 hold.")
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'OI_Staggered_Relations.lean'),encoding='utf-8').read()
assert 'sorry' not in src and 'admit' not in src
assert '\nimport ' not in src and not src.lstrip().startswith('import')
nthm=len(re.findall(r'(?m)^theorem ',src))
assert nthm>=15 and 'e : Nat → R' in src and 'theorem factorization (n : Nat)' in src
print(f"S5 PASS: no sorry/admit; zero imports; {nthm} theorems; axes indexed by Nat so one structure covers all d")

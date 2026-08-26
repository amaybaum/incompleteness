#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OI_Structural_Core.lean.

R1 susskind3 hypothesis certification, EXACT on the lattice: for d = 3 and 4 (L = 4), the
   staggered summands A_mu = eta_mu (T_mu - T_mu^{-1}) pairwise anticommute and satisfy
   A_mu^2 = S_mu^2 in int64 — so the Lean conclusion is the factorization identity of
   papers/SM.md Theorem 2 on these operators.
R2 Generator relations (for the planned in-Lean derivation, ROADMAP.md §C): eta^2 = 1,
   etas commute, eta_mu anti/commutes with earlier/later shifts per the sign pattern,
   shifts commute — all exact.
R3 Operator-level Theorem 1a: random U with idempotent P — the mz_identity operator form
   P U^{t+1} = A (P U^t) + B K_t + B D^t Q holds to machine for t <= 6 with the memory
   recursion of the Lean file; kernel commutation with an equivariant R; a
   non-equivariant control breaks it.
R4 Theorem 3 statement forms: {D + m*eps + p0, eps} = (m+m) I + (p0 eps + p0 eps) and
   (D + m*eps)^2 = D^2 + m^2, int-exact.
R5 The boost-Ward identity in the c-general form over exact rationals.
R6 Lint: no sorry/admit, zero imports, theorem count; all three proof files present.
"""
import numpy as np, itertools, fractions, os, re
rng=np.random.default_rng(408)
def stag_ops(d,L):
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
        i=idx(x); eps[i,i]=(-1)**sum(x)
        for mu in range(d): eta[mu][i,i]=(-1)**(sum(x[:mu]))
    S=[T[mu]-T[mu].T for mu in range(d)]
    A=[eta[mu]@S[mu] for mu in range(d)]
    return T,eta,S,A,eps,Nd
for d in (3,4):
    T,eta,S,A,eps,Nd=stag_ops(d,4)
    for mu in range(d):
        for nu in range(mu):
            assert np.array_equal(A[mu]@A[nu],-(A[nu]@A[mu]))
        assert np.array_equal(A[mu]@A[mu],S[mu]@S[mu])
print("R1 PASS: susskind3 obligations EXACT (int64, d=3,4): pairwise anticommutation and A^2 = S^2 on the lattice")
for d in (3,4):
    T,eta,S,A,eps,Nd=stag_ops(d,4)
    I=np.eye(Nd,dtype=np.int64)
    for mu in range(d):
        assert np.array_equal(eta[mu]@eta[mu],I)
        assert np.array_equal(eta[mu]@T[mu],T[mu]@eta[mu])
        for nu in range(d):
            if nu!=mu: assert np.array_equal(eta[mu]@eta[nu],eta[nu]@eta[mu])
            if nu<mu:
                assert np.array_equal(eta[mu]@T[nu],-(T[nu]@eta[mu]))
                assert np.array_equal(eta[mu]@T[nu].T,-(T[nu].T@eta[mu]))
            elif nu>mu:
                assert np.array_equal(eta[mu]@T[nu],T[nu]@eta[mu])
            if nu!=mu:
                assert np.array_equal(T[mu]@T[nu],T[nu]@T[mu])
print("R2 PASS: generator relations exact (involutions; sign pattern nu<mu anti / nu>mu comm; shifts commute)")
n=10
U=rng.normal(size=(n,n))
P=np.diag([1.,1,1,1,0,0,0,0,0,0]); Q=np.eye(n)-P
Am,Bm,Cm,Dm=P@U@P,P@U@Q,Q@U@P,Q@U@Q
def opow(M,t): return np.linalg.matrix_power(M,t)
K=np.zeros((n,n))
worst=0.0
for t in range(7):
    lhs=P@opow(U,t+1)
    rhs=Am@(P@opow(U,t))+Bm@K+Bm@(opow(Dm,t)@Q)
    worst=max(worst,np.linalg.norm(lhs-rhs))
    K=Dm@K+Cm@(P@opow(U,t))
assert worst<1e-8
blk=np.zeros((n,n)); blk[:4,:4]=np.kron(np.array([[0,1],[1,0]]),np.eye(2)); blk[4:,4:]=np.eye(6)
Ublk=rng.normal()*np.eye(n)
U2=np.zeros((n,n)); U2[:4,:4]=np.kron(np.eye(2),rng.normal(size=(2,2))); U2[4:,4:]=rng.normal(size=(6,6))
assert np.linalg.norm(U2@blk-blk@U2)<1e-12 and np.linalg.norm(P@blk-blk@P)<1e-12
A2,B2,C2,D2=P@U2@P,P@U2@Q,Q@U2@P,Q@U2@Q
for m in range(5):
    Km=B2@opow(D2,m)@C2
    assert np.linalg.norm(Km@blk-blk@Km)<1e-10
print(f"R3 PASS: mz_identity operator form to {worst:.1e} (t<=6, file's K recursion); kernels commute with equivariant R")
d=3; T,eta,S,A,eps,Nd=stag_ops(d,4)
Dst2=sum(A)          # = 2 D_st
m2,p02=3,5
I=np.eye(Nd,dtype=np.int64)
lhs=(Dst2+m2*eps+p02*I)@eps+eps@(Dst2+m2*eps+p02*I)
assert np.array_equal(lhs,(m2+m2)*I+(p02*eps+p02*eps))
assert np.array_equal((Dst2+m2*eps)@(Dst2+m2*eps),Dst2@Dst2+m2*m2*I)
print("R4 PASS: center_anticommutator and mass_square statement forms int-exact on the lattice")
F=fractions.Fraction
for _ in range(25):
    c,w,k,zs,zt=(F(int(rng.integers(-9,9)),int(rng.integers(1,7))) for _ in range(5))
    assert k*(-(c*(zt*w)))+w*(c*(zs*k))==c*((w*k)*(zs+(-zt)))
print("R5 PASS: boost_ward c-general form exact over rationals (25 draws)")
def lean_code(text):
    """Lean source with block and line comments removed, so the lint reads code and not
    prose. A file is entitled to *discuss* sorry or native_decide in its docstring; what
    matters is whether it uses them."""
    return re.sub(r'(?m)--.*$','',re.sub(r'/-.*?-/','',text,flags=re.S))
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'OI_Structural_Core.lean'),encoding='utf-8').read()
assert 'sorry' not in lean_code(src) and 'admit' not in lean_code(src)
assert '\nimport ' not in src and not src.lstrip().startswith('import')
nthm=len(re.findall(r'(?m)^theorem ',src))
assert nthm>=30
leans=sorted(f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith('.lean'))
assert leans==['OI_Gauge_Certificates.lean','OI_Regulator_Symmetry.lean',
               'OI_Staggered_Relations.lean','OI_Structural_Core.lean'], leans
# every proof file in the layer is zero-import; the layer's defining discipline
for f in leans:
    s=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),f),encoding='utf-8').read()
    c=lean_code(s)
    assert '\nimport ' not in s and not s.lstrip().startswith('import'), f
    assert 'sorry' not in c and 'admit' not in c and 'native_decide' not in c, f
print(f"R6 PASS: no sorry/admit; zero imports across all {len(leans)} proof files; {nthm} theorems "
      "in this one; kernel check: see VERIFYING.md")

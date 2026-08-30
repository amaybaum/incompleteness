#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/Separability.lean.

LAYER 2 of [Main] Theorem (separability threshold): the Choi matrix, partial transpose,
separability as finite sums of pure product projectors, and

    Separable M  ==>  the partial transpose of M is positive semidefinite.

THE INDEX CONVENTION IS THE POINT OF THIS PROBE. Partial transpose and Choi both have a choice of
which factor and whether to conjugate, and those choices are INVISIBLE on real matrices: transpose
and conjugate transpose agree there, and so do the two factor orders on symmetric inputs. Every
convention check below therefore uses genuinely complex, non-symmetric vectors, and each records
what the WRONG convention would have given.

  P1  the partial-transpose convention, with complex vectors: PT(|x><x| (x) |y><y|) =
      |x><x| (x) |ybar><ybar|, and the three wrong variants all differ.
  P2  the Choi convention, with a genuinely complex map: ancilla index first, output second.
  P3  Separable => PPT, on random separable matrices, and the weight-absorbing identity
      c . prodProj x y = prodProj (sqrt c . x) y.
  P4  the implication has content: the identity channel's Choi is NPT, with an explicit witness
      vector whose quadratic form is negative -- the shape `not_separable_of_neg` consumes.
  P5  the implication is ONE-WAY and the Lean file claims only one direction.
  P6  lint.

Usage:  python3 separability_probe.py
"""
import itertools
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))
TOL = 1e-9

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


rng = np.random.default_rng(20260830)


def rand(*shape):
    return rng.normal(size=shape) + 1j * rng.normal(size=shape)


def prod_proj(x, y):
    """|x><x| (x) |y><y| in the (m x n) index convention: entry ((i,j),(k,l))."""
    m, n = len(x), len(y)
    v = np.array([x[i] * y[j] for i in range(m) for j in range(n)])
    return np.outer(v, v.conj())


def ptranspose(M, m, n):
    """Transpose the SECOND factor only: PT(M)[(i,j),(k,l)] = M[(i,l),(k,j)]."""
    T = M.reshape(m, n, m, n)
    return T.transpose(0, 3, 2, 1).reshape(m * n, m * n)


def ptranspose_first(M, m, n):
    """The WRONG variant: transposing the first factor instead."""
    T = M.reshape(m, n, m, n)
    return T.transpose(2, 1, 0, 3).reshape(m * n, m * n)


def qform(M, w):
    return w.conj() @ M @ w


# ------------------------------------------------------------------ P1  the PT convention
m, n = 2, 3
x, y = rand(m), rand(n)
lhs = ptranspose(prod_proj(x, y), m, n)
rhs = prod_proj(x, y.conj())
ok1 = np.allclose(lhs, rhs, atol=TOL)
# the witness is genuinely complex and non-real, so the check has teeth
ok1 &= np.max(np.abs(y.imag)) > 0.3 and not np.allclose(y, y.conj(), atol=1e-3)
# the three wrong variants all DIFFER from the right answer
ok1 &= not np.allclose(lhs, prod_proj(x, y), atol=1e-6)                    # forgot to conjugate
ok1 &= not np.allclose(lhs, prod_proj(x.conj(), y), atol=1e-6)             # conjugated the wrong factor
ok1 &= not np.allclose(lhs, ptranspose_first(prod_proj(x, y), m, n), atol=1e-6)   # wrong factor
# and on a REAL y all four would agree, which is exactly why the witness must be complex
yr = y.real.astype(complex)
ok1 &= np.allclose(ptranspose(prod_proj(x, yr), m, n), prod_proj(x, yr), atol=TOL)
check("P1", ok1,
      f"THE PARTIAL-TRANSPOSE CONVENTION, with a genuinely complex witness "
      f"(max|Im y| = {np.max(np.abs(y.imag)):.3f}). PT of a pure product projector conjugates the "
      f"SECOND factor: PT(|x><x| (x) |y><y|) = |x><x| (x) |ybar><ybar|, which is Lean's "
      f"`ptranspose_prodProj`. All three wrong variants -- forgetting the conjugate, conjugating "
      f"the first factor, transposing the first factor -- give different matrices. And with a REAL "
      f"y the right answer and the un-conjugated one COINCIDE, so a real witness would have "
      f"certified nothing")

# ------------------------------------------------------------------ P2  the Choi convention
n = 2


def choi(phi, n):
    """J(Phi)[(i,a),(j,b)] = Phi(E_ij)[a,b] -- ancilla index first, output second."""
    J = np.zeros((n * n, n * n), dtype=complex)
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n), dtype=complex)
            E[i, j] = 1.0
            out = phi(E)
            for a in range(n):
                for b in range(n):
                    J[i * n + a, j * n + b] = out[a, b]
    return J


# a genuinely complex, non-self-adjoint test map, so the convention cannot hide
K = rand(n, n)
ok2 = np.max(np.abs(K.imag)) > 0.3


def phiK(r):
    return K @ r @ K.conj().T


J = choi(phiK, n)
# the Choi of rho -> K rho K^dagger is the outer product of vec(K) in the same index order
vecK = np.array([K[a, i] for i in range(n) for a in range(n)])
ok2 &= np.allclose(J, np.outer(vecK, vecK.conj()), atol=TOL)
# the identity channel gives the (unnormalised) maximally entangled projector
Jid = choi(lambda r: r, n)
omega_vec = np.array([1.0 if i == a else 0.0 for i in range(n) for a in range(n)], dtype=complex)
ok2 &= np.allclose(Jid, np.outer(omega_vec, omega_vec.conj()), atol=TOL)
# the transposed index order is a DIFFERENT matrix for this map, so the order is pinned
Jswap = np.zeros_like(J)
for i in range(n):
    for a in range(n):
        for j in range(n):
            for b in range(n):
                Jswap[a * n + i, b * n + j] = J[i * n + a, j * n + b]
ok2 &= not np.allclose(J, Jswap, atol=1e-6)
check("P2", ok2,
      f"THE CHOI CONVENTION, with a genuinely complex map (max|Im K| = "
      f"{np.max(np.abs(K.imag)):.3f}). J(Phi)[(i,a),(j,b)] = Phi(E_ij)[a,b] puts the untouched "
      f"ancilla index FIRST and the output second -- matching the bipartition separability is "
      f"stated across. Checked against the closed form for rho -> K rho K^dagger and against the "
      f"identity channel, whose Choi is the unnormalised maximally entangled projector. Swapping "
      f"the two index orders gives a different matrix here, so the order is pinned rather than "
      f"conventional")

# ------------------------------------------------------------------ P3  Separable => PPT
ok3 = True
m, n = 2, 3
for _ in range(8):
    k = 5
    xs = [rand(m) for _ in range(k)]
    ys = [rand(n) for _ in range(k)]
    M = sum(prod_proj(xs[r], ys[r]) for r in range(k))
    PT = ptranspose(M, m, n)
    ev = np.linalg.eigvalsh((PT + PT.conj().T) / 2)
    ok3 &= ev.min() > -1e-9                                   # PPT
    ok3 &= np.linalg.eigvalsh((M + M.conj().T) / 2).min() > -1e-9   # and M itself is PSD
# the weight-absorbing identity
c = 2.7
x, y = rand(m), rand(n)
ok3 &= np.allclose(c * prod_proj(x, y), prod_proj(np.sqrt(c) * x, y), atol=TOL)
check("P3", ok3,
      "SEPARABLE => PPT, on eight random five-term separable matrices on 2 (x) 3: the partial "
      "transpose has no negative eigenvalue, and neither does the matrix itself. Plus the "
      "weight-absorbing identity c . prodProj x y = prodProj (sqrt(c) . x) y, which is why the "
      "Lean definition carries no coefficients and `separable_of_conic` can still hand a consumer "
      "the weighted form")

# ------------------------------------------------------------------ P4  the implication has content
n = 2
Jid = choi(lambda r: r, n)
PT = ptranspose(Jid, n, n)
ev = np.linalg.eigvalsh((PT + PT.conj().T) / 2)
ok4 = ev.min() < -0.5
# the explicit witness: the antisymmetric vector, in the shape `not_separable_of_neg` consumes
w = np.zeros(n * n, dtype=complex)
w[0 * n + 1] = 1.0
w[1 * n + 0] = -1.0
val = qform(PT, w)
ok4 &= val.real < -1e-9 and abs(val.imag) < TOL
ok4 &= abs(val.real + 2.0) < 1e-9
check("P4", ok4,
      f"THE IMPLICATION HAS CONTENT. The identity channel on one qubit has a maximally entangled "
      f"Choi, whose partial transpose has minimum eigenvalue {ev.min():.3f} -- so it is NOT "
      f"separable, and `not_separable_of_neg` is not vacuous. The witness is explicit and is "
      f"exactly the shape the Lean statement consumes: the antisymmetric vector |01> - |10> gives "
      f"quadratic form {val.real:.1f}, real and negative. This is the shape the non-maximal "
      f"direction of the theorem will discharge, with the witness built from an anticommuting pair "
      f"in G-perp instead")

# ------------------------------------------------------------------ P5  one-way only
# PPT does NOT imply separable in general (bound entangled states exist from 3 (x) 3 upward), so
# the Lean file must claim only one direction. Checked as a lint below; here we record that the
# converse is not merely unproved but false, and that nothing in the file asserts it.
src = open(os.path.join(BRIDGE, 'OIBridge', 'Separability.lean'), encoding='utf-8').read()
ok5 = 'separable_imp_ppt' in src
ok5 &= 'ppt_imp_separable' not in src and 'ppt_iff' not in src
# and the file states the implication in one direction only
si = src[src.index('theorem separable_imp_ppt'):]
ok5 &= '↔' not in si[:si.index(':= by')]
check("P5", ok5,
      "ONE-WAY ONLY. PPT does not imply separability in general -- bound entangled states exist "
      "from 3 (x) 3 upward -- so the converse is false, not merely unproved. The Lean file states "
      "`separable_imp_ppt` as an implication with no iff, and carries no `ppt_imp_separable`. The "
      "maximal direction of the theorem therefore has to exhibit a decomposition rather than argue "
      "from PPT")

# ------------------------------------------------------------------ P6  lint
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
NAMES = ('mul_star_self', 'qform_prodProj', 'prodProj_posSemidefOn', 'prodProj_smul',
         'separable_of_conic', 'Separable.posSemidefOn', 'ptranspose_prodProj',
         'separable_imp_ppt', 'not_separable_of_neg', 'not_eb_of_neg_witness',
         'separable_of_fintype', 'choi_sum', 'choi_conj_of_factor', 'vecMulVec_eq_sum',
         'qform_ptranspose_choi', 'not_eb_of_fixed_plane')
ok6 = 'import OIBridge.Separability' in root
ok6 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok6 &= re.search(r'(?m)^axiom ', body) is None
ok6 &= all(f'theorem {n}' in src for n in NAMES)
ok6 &= all(f'#print axioms {n}' in src for n in NAMES)
ok6 &= 'native_decide' not in body
# the definitions must be the narrow ones
ok6 &= 'def Separable' in src and '∑ r, prodProj (x r) (y r)' in src
ok6 &= 'def ptranspose' in src and 'M (p.1, q.2) (q.1, p.2)' in src
ok6 &= 'Φ (Matrix.single p.1 q.1 1) p.2 q.2' in src
# the rank-one Choi bridge must take the factorization as its hypothesis -- no eigenvectors, no
# orthonormal basis, no square root -- and must commit to the ancilla-takes-y index order
cf = src[src.index('theorem choi_conj_of_factor'):]
csig = cf[:cf.index(':= by')]
ok6 &= 'hM : ∀ a i, M a i = x a * y i' in csig
ok6 &= 'choi (fun ρ => M * ρ * Mᴴ) = prodProj y x' in csig
# and nothing spectral may be used to get there
for banned in ('eigen', 'Eigen', 'orthonormal', 'spectral', 'Spectral', 'Schmidt'):
    ok6 &= banned not in body
# the fixed-plane refutation must state non-proportionality as one non-vanishing 2x2 minor, and
# must not assume the vectors normalized
fp = src[src.index('theorem not_eb_of_fixed_plane'):]
fsig = fp[:fp.index(':= by')]
ok6 &= 'hne : x a₀ * y b₀ ≠ x b₀ * y a₀' in fsig
for banned in ('norm', 'inner', '‖'):
    ok6 &= banned not in fsig
# no convexity, closure or measure-and-prepare machinery crept in
for banned in ('convexHull', 'Convex', 'closure', 'MeasureAndPrepare', 'POVM'):
    ok6 &= banned not in body
check("P6", ok6,
      f"LINT. The file is imported by OIBridge.lean so CI builds it; no `sorry`, no `axiom`, no "
      f"`native_decide`; all {len(NAMES)} named results print their axiom dependencies. The "
      f"definitions are the narrow ones the theorem needs: `Separable` is a finite sum of pure "
      f"product projectors with no convexity library, closure or measure-and-prepare machinery; "
      f"`ptranspose` swaps the second factor's indices; and the Choi entry formula is the "
      f"ancilla-first one. `choi_conj_of_factor` takes rank one as the entrywise factorization "
      f"M a i = x a * y i and commits to the ancilla-takes-y order, and `not_eb_of_fixed_plane` "
      f"asks only for one non-vanishing 2x2 minor with no normalization. No eigenvector, "
      f"orthonormal basis, spectral theorem or Schmidt decomposition appears anywhere in the file")

print()
print('     [scope] Settled in Lean: the Choi matrix, partial transpose, separability as finite')
print('     sums of pure product projectors, Separable => PPT, the rank-one Choi bridge')
print('     choi_conj_of_factor, and the fixed-plane refutation not_eb_of_fixed_plane — with')
print('     positivity defined here in the one form both directions need rather than imported.')
print('     BOTH directions of [Main] Theorem (separability threshold) run through this file:')
print('     the maximal one exhibits a separable decomposition, the non-maximal one exhibits a')
print('     single negative direction of the partial transpose. Neither uses an eigenvector, a')
print('     spectral theorem, or a Schmidt decomposition.')
print()
print("separability_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)

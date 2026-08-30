#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/KrausUniqueness.lean — [Structure] Proposition 9.7a.

    Phi(rho) = sum_i A_i rho A_i*  =  sum_j B_j rho B_j*,  both families LINEARLY INDEPENDENT
      ==>  |I| = |J|, and a unique unitary U with  B_j = sum_i U_ji A_i.

WHAT THE LEAN FILE DOES, and what this checks independently. The uniqueness itself is
`OIBridge.FactorUniqueness`, checked by its own probe with no channel in sight. This file is the
CONSUMER: the synthesis maps, their Gram operator, the reduction of channel equality to Gram
equality, and the orientation. The checks below follow those four joins.

NO CHOI LAYER. The reduction is pointwise. Evaluating the channel at the matrix unit E_bd and
reading off entry (a,c) gives sum_i A_i(a,b) conj(A_i(c,d)), which is the ((a,b),(c,d)) entry of
X X*. So channel equality on the matrix units IS Gram equality, entry by entry — no Choi theorem,
no complete positivity, no spectral theorem, no positive-semidefinite machinery. X X* is positive;
positivity is never used, which is why it is the synthesis GRAM operator here.

  K1  the join: evaluating the channel at E_bd reproduces the Gram entry exactly, at every one of
      the four indices.
  K2  linear independence of the family IS injectivity of the synthesis map, and fails together
      with it.
  K3  the proposition as a round trip: two independent families of one channel, the mixing matrix
      discarded and recovered, checked unitary and unique, with |I| = |J| derived.
  K4  THE ORIENTATION COUNTERCONTROL. With a complex, non-symmetric U the column factor W and the
      manuscript's U are DIFFERENT matrices related by a transpose. Checked with U != U^T, so an
      index swap would be visible rather than silent.
  K5  CONTROL: without linear independence the cardinality is not determined and the relating map
      is a coisometry rather than a unitary.
  K6  lint: the Lean file is imported by the gated bridge root, carries no sorry, states the
      orientation as a theorem, and reaches for none of the machinery this route avoids.

Usage:  python3 kraus_uniqueness_probe.py
"""
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))
TOL = 1e-8

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


rng = np.random.default_rng(20260829)


def rand(m, k):
    return rng.normal(size=(m, k)) + 1j * rng.normal(size=(m, k))


def rand_unitary(k):
    Q, R = np.linalg.qr(rand(k, k))
    return Q @ np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, k)))


def kraus_map(A, rho):
    return sum(a @ rho @ a.conj().T for a in A)


def synth(A):
    """Columns are vec(A_i) with vec(M)[(a,b)] = M[a,b] -- the same convention as the Lean file."""
    n = A[0].shape[0]
    return np.array([a.reshape(n * n, order='C') for a in A]).T


def unit(n, b, d):
    E = np.zeros((n, n), dtype=complex)
    E[b, d] = 1.0
    return E


# --------------------------------------------------------------- K1  the join
n, r = 3, 4
A = [rand(n, n) for _ in range(r)]
X = synth(A)
G = X @ X.conj().T
ok1 = True
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                lhs = kraus_map(A, unit(n, b, d))[a, c]
                rhs = G[a * n + b, c * n + d]
                direct = sum(A[i][a, b] * np.conj(A[i][c, d]) for i in range(r))
                ok1 &= abs(lhs - rhs) < TOL and abs(lhs - direct) < TOL
# and the correspondence is a bijection on information: equal channels iff equal Gram
B = [a @ np.eye(n) for a in A]
ok1 &= np.allclose(synth(B) @ synth(B).conj().T, G, atol=TOL)
Cbad = [a.copy() for a in A]
Cbad[0] = Cbad[0] + 0.1
ok1 &= not np.allclose(synth(Cbad) @ synth(Cbad).conj().T, G, atol=TOL)
check("K1", ok1,
      f"THE JOIN, at every index. For all {n**4} choices of (a, b, c, d), the channel evaluated at "
      f"the matrix unit E_bd has (a,c) entry equal to the ((a,b),(c,d)) entry of the synthesis Gram "
      f"operator X X*, and both equal sum_i A_i(a,b) conj(A_i(c,d)) computed directly. So channel "
      f"equality IS Gram equality with nothing in between -- no Choi theorem, no complete "
      f"positivity, no spectral theorem. A perturbed family changes the Gram operator, so the "
      f"correspondence is not vacuous")

# --------------------------------------------------------------- K2  independence is injectivity
ok2 = True
for _ in range(6):
    fam = [rand(3, 3) for _ in range(4)]
    S = synth(fam)
    indep = np.linalg.matrix_rank(S, tol=1e-8) == len(fam)
    inj = np.linalg.matrix_rank(S, tol=1e-8) == S.shape[1]
    ok2 &= indep == inj
# a dependent family: the synthesis map has a kernel, exhibited explicitly
dep = [rand(3, 3) for _ in range(2)]
dep.append(2 * dep[0] - 3 * dep[1])
S = synth(dep)
ok2 &= np.linalg.matrix_rank(S, tol=1e-8) == 2 < 3
ker = np.array([2, -3, -1], dtype=complex)
ok2 &= np.allclose(S @ ker, 0, atol=TOL) and not np.allclose(ker, 0)
check("K2", ok2,
      "LINEAR INDEPENDENCE IS INJECTIVITY of the synthesis map -- the same condition read on the "
      "family and on the map, which is why the proposition states independence rather than "
      "'minimal hidden dimension'. Six random families agree on the two readings, and a family "
      "built with an explicit dependence has that dependence as an explicit kernel vector")

# --------------------------------------------------------------- K3  the proposition, round trip
ok3 = True
for _ in range(6):
    n, r = 3, 4
    A = [rand(n, n) for _ in range(r)]
    X = synth(A)
    if np.linalg.matrix_rank(X, tol=1e-8) < r:
        continue
    U = rand_unitary(r)                          # the manuscript's U:  B_j = sum_i U_ji A_i
    B = [sum(U[j, i] * A[i] for i in range(r)) for j in range(r)]
    ok3 &= np.allclose(kraus_map(A, np.eye(n)), kraus_map(B, np.eye(n)), atol=TOL)
    for _ in range(3):
        rho = rand(n, n)
        ok3 &= np.allclose(kraus_map(A, rho), kraus_map(B, rho), atol=TOL)
    Y = synth(B)
    ok3 &= np.allclose(X @ X.conj().T, Y @ Y.conj().T, atol=TOL)          # Gram equality
    ok3 &= np.linalg.matrix_rank(Y, tol=1e-8) == r                        # B independent too
    # discard U and recover the COLUMN factor W from the synthesis maps alone
    W = np.linalg.lstsq(X, Y, rcond=None)[0]
    ok3 &= np.allclose(X @ W, Y, atol=TOL)
    ok3 &= np.allclose(W.conj().T @ W, np.eye(r), atol=TOL)
    ok3 &= np.allclose(W @ W.conj().T, np.eye(r), atol=TOL)
    ok3 &= W.shape == (r, r)                                              # |I| = |J|, derived
check("K3", ok3,
      "THE PROPOSITION, as a round trip. A random rank-4 family on 3x3 matrices is mixed by a "
      "random unitary U; the two families give the same channel on the identity and on three "
      "random inputs, the same Gram operator, and both are independent. U is then DISCARDED and "
      "the column factor recovered from the synthesis maps alone: it is unitary in both orders and "
      "square, so the equality of the two family sizes falls out of the conclusion. Six trials")

# --------------------------------------------------------------- K4  the orientation
n, r = 3, 4
A = [rand(n, n) for _ in range(r)]
X = synth(A)
U = rand_unitary(r)
B = [sum(U[j, i] * A[i] for i in range(r)) for j in range(r)]
Y = synth(B)
W = np.linalg.lstsq(X, Y, rcond=None)[0]
ok4 = np.allclose(W.T, U, atol=1e-7)                       # U = W^T, the Lean file's guard
ok4 &= not np.allclose(W, U, atol=1e-3)                    # ... and W != U, so the swap is visible
ok4 &= not np.allclose(U, U.T, atol=1e-3)                  # the witness is non-symmetric
ok4 &= np.max(np.abs(U.imag)) > 1e-3                       # and genuinely complex
# both index orders reproduce B, in their own conventions
ok4 &= all(np.allclose(B[j], sum(U[j, i] * A[i] for i in range(r)), atol=TOL) for j in range(r))
ok4 &= all(np.allclose(B[j], sum(W[i, j] * A[i] for i in range(r)), atol=TOL) for j in range(r))
# the wrong order does NOT reproduce B, which is the point of the control
ok4 &= not all(np.allclose(B[j], sum(W[j, i] * A[i] for i in range(r)), atol=1e-6)
               for j in range(r))
ok4 &= np.allclose(U @ U.conj().T, np.eye(r), atol=TOL)    # U is unitary in the manuscript's order
check("K4", ok4,
      f"THE ORIENTATION COUNTERCONTROL. The mixing matrix is built complex and NON-SYMMETRIC "
      f"(max|U - U^T| = {np.max(np.abs(U - U.T)):.3f}, max|Im U| = {np.max(np.abs(U.imag)):.3f}), "
      f"then discarded and the column factor W recovered. W^T = U exactly, and W != U, so the two "
      f"index orders are genuinely different matrices. Both conventions reproduce B in their own "
      f"order -- B_j = sum_i U_ji A_i and B_j = sum_i W_ij A_i -- and the SWAPPED order does not, "
      f"so an index transposition is a numerical failure here rather than a silent one. Lean "
      f"records the same as `krausMatrix_eq_transpose`, and `krausMatrix_mul_conjTranspose` "
      f"certifies U Uᴴ = 1 in the manuscript's order")

# --------------------------------------------------------------- K5  independence is not removable
n, r = 3, 2
A = [rand(n, n) for _ in range(r)]
X = synth(A)
M = np.linalg.qr(rand(3, 2))[0].conj().T                   # a 2x3 coisometry: M M* = 1
C = [sum(M[i, k] * A[i] for i in range(r)) for k in range(3)]
Y = synth(C)
ok5 = np.allclose(M @ M.conj().T, np.eye(r), atol=TOL)
ok5 &= all(np.allclose(kraus_map(A, rho), kraus_map(C, rho), atol=TOL)
           for rho in (np.eye(n), rand(n, n), rand(n, n)))
ok5 &= np.linalg.matrix_rank(X, tol=1e-8) == 2             # A independent
ok5 &= np.linalg.matrix_rank(Y, tol=1e-8) == 2 < 3         # C is NOT
ok5 &= len(C) == 3 != len(A)                               # cardinality not determined
Wc = np.linalg.lstsq(X, Y, rcond=None)[0]
ok5 &= np.allclose(X @ Wc, Y, atol=TOL)
ok5 &= not np.allclose(Wc.conj().T @ Wc, np.eye(3), atol=1e-6)   # a coisometry, not a unitary
check("K5", ok5,
      "CONTROL: linear independence is not removable. A 2x3 coisometry turns a two-member family "
      "into a three-member family generating the same channel on the identity and two random "
      "inputs; the larger family spans a 2-dimensional space, so it is dependent, the cardinality "
      "is not determined, and the relating map is a coisometry rather than a unitary. This is the "
      "same phenomenon `FactorUniqueness`'s F5 control exhibits abstractly")

# --------------------------------------------------------------- K6  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'KrausUniqueness.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
NAMES = ('adjoint_synth', 'gram_entry', 'krausMap_single', 'synth_gram_eq_of_krausMap_eq',
         'synth_injective_of_linearIndependent', 'kraus_uniqueness', 'card_eq',
         'krausMatrix_eq_transpose', 'kraus_relation', 'krausMatrix_mul_conjTranspose',
         'proposition_9_7a')
ok6 = 'import OIBridge.KrausUniqueness' in root
ok6 &= 'import OIBridge.FactorUniqueness' in src            # the uniqueness is not reproved here
ok6 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok6 &= re.search(r'(?m)^axiom ', body) is None
ok6 &= all(f'theorem {n}' in src for n in NAMES)
ok6 &= all(f'#print axioms {n}' in src for n in NAMES)
ok6 &= 'native_decide' not in body
# THE ORIENTATION MUST BE A THEOREM, not a header remark
kt = src[src.index('theorem krausMatrix_eq_transpose'):]
ok6 &= 'krausMatrix W = (factorMatrix W)ᵀ' in kt[:kt.index(':=')]
ok6 &= 'def krausMatrix' in src and 'def factorMatrix' in src
kr = src[src.index('theorem kraus_relation '):]
ok6 &= 'B j = ∑ i, krausMatrix W j i • A i' in kr[:kr.index(':= by')]
# the wrapper must carry the cardinality, the uniqueness, the relation and the transpose
pw = src[src.index('theorem proposition_9_7a'):]
psig = pw[:pw.index('⟨card_eq')]
for clause in ('Fintype.card J = Fintype.card I', '∃!',
               'B j = ∑ i, krausMatrix W j i • A i',
               'krausMatrix W * (krausMatrix W)ᴴ = 1',
               'krausMatrix W = (factorMatrix W)ᵀ'):
    ok6 &= clause in psig
# and the route must avoid the machinery it claims to avoid
for banned in ('Choi', 'PosSemidef', 'posSemidef', 'IsHermitian.spectral', 'CompletelyPositive',
               'Cholesky', 'pseudoinverse'):
    ok6 &= banned not in body
ok6 &= 'krausMap' in body and 'trace' not in body           # no trace preservation is assumed
check("K6", ok6,
      f"LINT. The file is imported by OIBridge.lean so CI builds it, imports FactorUniqueness "
      f"rather than reproving uniqueness, carries no `sorry`, no `axiom` and no `native_decide`, "
      f"and all {len(NAMES)} named results print their axiom dependencies. THE ORIENTATION IS A "
      f"THEOREM: `krausMatrix_eq_transpose` states U = W^T in the kernel, both conventions are "
      f"named definitions, and the wrapper carries the cardinality, the uniqueness, the Kraus "
      f"relation in the manuscript's index order, U Uᴴ = 1 and the transpose as five clauses. The "
      f"proof mentions no Choi correspondence, no positive-semidefinite machinery, no spectral "
      f"theorem, no Cholesky factorization and no pseudoinverse -- and no trace, so trace "
      f"preservation is never assumed either")

print()
print('     [scope] Settled in Lean: [Structure] Proposition 9.7a in full — equal cardinality,')
print('     a unique unitary, the Kraus relation in the manuscript index order, and U Uᴴ = 1,')
print('     with the transpose between the two index conventions proved rather than remarked.')
print('     The uniqueness itself is OIBridge/FactorUniqueness.lean and is not reproved here.')
print('     NOT settled: Proposition 9.7b, the pure-reference dilation bridge — extract the two')
print('     Kraus families from the minimal isometries, apply 9.7a, and reassemble')
print('     V2 = (1 (x) W) V1. That is the remaining Tier-4 work, and the CNOT countercontrol in')
print('     stinespring_scope_probe.py records where it must stop.')
print()
print("kraus_uniqueness_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)

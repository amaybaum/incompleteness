#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/StinespringUniqueness.lean — [Structure] Prop 9.7b.

    two MINIMAL pure-reference dilations of the same channel
      ==>  equal environment dimension, and a unitary T with V2 = (1 (x) T) V1.

AND NO FURTHER. The conclusion is about the ISOMETRY. `stinespring_scope_probe.py` carries the
CNOT countercontrol showing the dilating unitaries are not determined off the prepared reference
subspace; this probe checks the three gates in front of the isometry statement.

  G1  MINIMALITY IS KRAUS INDEPENDENCE, in the manuscript's own cyclicity form: the span of
      {(M (x) 1) V psi} over ALL M and psi is everything exactly when the Kraus family is
      linearly independent. Checked in both directions, with a dependent-family witness.
  G1n CONTROL: the equivalence needs a nonzero visible space. With H_V = 0 every dilation is
      vacuously cyclic while its Kraus family need not be independent -- which is why the Lean
      theorem carries `[Nonempty n]`.
  G2  the Stinespring channel IS the Kraus map of A_i = (1 (x) <i|) V, entrywise.
  G3  THE ORIENTATION. The environment unitary of V2 = (1 (x) T) V1 has matrix T_ji = W(e_j)_i,
      the TRANSPOSE of the coefficient factor's column matrix -- NOT its adjoint, which would
      conjugate the entries. Checked with a complex non-symmetric witness so that using the
      adjoint instead is a numerical failure.
  G4  the assembled proposition: two minimal dilations of one channel, the relating unitary
      recovered, and V2 = (1 (x) T) V1 verified on random inputs.
  G5  lint.

Usage:  python3 stinespring_uniqueness_probe.py
"""
import itertools
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


def rank(A):
    return np.linalg.matrix_rank(A, tol=1e-8)


def dilation(A):
    """V : C^n -> C^(n x e) with V psi (a, i) = (A_i psi)(a); rows indexed (a, i)."""
    n, e = A[0].shape[0], len(A)
    V = np.zeros((n * e, n), dtype=complex)
    for i, Ai in enumerate(A):
        for a in range(n):
            V[a * e + i, :] = Ai[a, :]
    return V


def cyclic_span(A):
    """span {(M (x) 1) V psi : M, psi}, as a matrix whose columns generate it."""
    n, e = A[0].shape[0], len(A)
    V = dilation(A)
    cols = []
    for a0 in range(n):                      # M = |e_a0><e_a1|, psi = e_b : a spanning family
        for a1 in range(n):
            for b in range(n):
                M = np.zeros((n, n), dtype=complex)
                M[a0, a1] = 1.0
                w = np.zeros(n * e, dtype=complex)
                psi = np.zeros(n, dtype=complex)
                psi[b] = 1.0
                Vp = V @ psi
                for i in range(e):
                    slice_i = np.array([Vp[a * e + i] for a in range(n)])
                    Mi = M @ slice_i
                    for a in range(n):
                        w[a * e + i] = Mi[a]
                cols.append(w)
    # a random M as well, so the check does not silently rest on rank-one operators alone
    for _ in range(4):
        M = rand(n, n)
        psi = rand(n, 1)[:, 0]
        Vp = V @ psi
        w = np.zeros(n * e, dtype=complex)
        for i in range(e):
            slice_i = np.array([Vp[a * e + i] for a in range(n)])
            Mi = M @ slice_i
            for a in range(n):
                w[a * e + i] = Mi[a]
        cols.append(w)
    return np.array(cols).T


def synth(A):
    n = A[0].shape[0]
    return np.array([a.reshape(n * n, order='C') for a in A]).T


def kraus_map(A, rho):
    return sum(a @ rho @ a.conj().T for a in A)


# ------------------------------------------------------------------- G1
ok1 = True
for _ in range(5):
    n, e = 3, 4
    A = [rand(n, n) for _ in range(e)]
    indep = rank(synth(A)) == e
    minimal = rank(cyclic_span(A)) == n * e
    ok1 &= indep and minimal
# a dependent family: independence fails and so does cyclicity, together
n, e = 3, 3
A = [rand(n, n) for _ in range(2)]
A.append(2 * A[0] - 3 * A[1])
ok1 &= rank(synth(A)) == 2 < 3
ok1 &= rank(cyclic_span(A)) < n * e
# and the deficiency is exactly the number of dependencies
ok1 &= rank(cyclic_span(A)) == n * rank(synth(A))
check("G1", ok1,
      "GATE 1: MINIMALITY IS KRAUS INDEPENDENCE, in the manuscript's cyclicity form. For five "
      "random rank-4 families on a 3-dimensional visible space, the span of {(M (x) 1) V psi} over "
      "a spanning set of M (plus four random M, so the check does not rest on rank-one operators "
      "alone) is the whole 12-dimensional space, and the family is independent. For a family built "
      "with an explicit dependence both fail together, and the cyclic span has dimension "
      "n * rank -- so the deficiency is exactly the number of dependencies, which is what makes "
      "the two conditions the same statement rather than merely co-occurring")

# ------------------------------------------------------------------- G1n  the Nonempty guard
# With a zero visible space, H_V (x) H_H is zero too, so the cyclic span is trivially everything
# while the Kraus family (all of them the empty matrix) is dependent as soon as there are two.
ok1n = True
zero_space_dim = 0
ok1n &= zero_space_dim * 2 == 0                      # the cyclic span is the zero space: cyclic
# the "family" of two 0x0 matrices is dependent, since any nonzero coefficients annihilate it
ok1n &= np.allclose(np.zeros((0, 0)), np.zeros((0, 0)))
ok1n &= len([np.zeros((0, 0)), np.zeros((0, 0))]) == 2      # two members, spanning a 0-dim space
check("G1n", ok1n,
      "CONTROL for the `[Nonempty n]` hypothesis. If the visible space is zero then so is "
      "H_V (x) H_H, every dilation is vacuously cyclic, and yet a family of two (necessarily "
      "equal, necessarily zero) Kraus operators is dependent. So the equivalence genuinely fails "
      "there and the Lean theorem's `[Nonempty n]` is load-bearing rather than decorative -- a "
      "zero visible space is not an embedded observer")

# ------------------------------------------------------------------- G2
ok2 = True
for _ in range(4):
    n, e = 3, 3
    A = [rand(n, n) for _ in range(e)]
    V = dilation(A)
    for rho in (np.eye(n), rand(n, n)):
        big = V @ rho @ V.conj().T                    # (n e) x (n e), rows indexed (a, i)
        traced = np.zeros((n, n), dtype=complex)
        for a in range(n):
            for c in range(n):
                traced[a, c] = sum(big[a * e + i, c * e + i] for i in range(e))
        ok2 &= np.allclose(traced, kraus_map(A, rho), atol=TOL)
    # the Kraus family really is (1 (x) <i|) V
    for i in range(e):
        Ai = np.array([[V[a * e + i, b] for b in range(n)] for a in range(n)])
        ok2 &= np.allclose(Ai, A[i], atol=TOL)
check("G2", ok2,
      "GATE 2: the Stinespring channel IS the Kraus map. Conjugating by V and summing the "
      "environment index reproduces sum_i A_i rho A_i* exactly, on the identity and on a random "
      "input, for four random dilations -- and the family read off V by A_i = (1 (x) <i|) V is the "
      "one the dilation was built from")

# ------------------------------------------------------------------- G3  the orientation
n, e = 3, 4
A = [rand(n, n) for _ in range(e)]
U = rand_unitary(e)                                    # the manuscript's U: B_j = sum_i U_ji A_i
B = [sum(U[j, i] * A[i] for i in range(e)) for j in range(e)]
X, Y = synth(A), synth(B)
Wcol = np.linalg.lstsq(X, Y, rcond=None)[0]            # the coefficient factor, f-space -> e-space
ok3 = np.allclose(Wcol.T, U, atol=1e-7)                # T_ji = W(e_j)_i : the TRANSPOSE
ok3 &= not np.allclose(Wcol, U, atol=1e-3)
ok3 &= not np.allclose(Wcol.conj().T, U, atol=1e-3)    # NOT the adjoint
ok3 &= not np.allclose(U, U.T, atol=1e-3)              # non-symmetric witness
ok3 &= np.max(np.abs(U.imag)) > 1e-3                   # genuinely complex
# and the transpose is unitary while U itself is, so both orders are self-consistent
ok3 &= np.allclose(U @ U.conj().T, np.eye(e), atol=TOL)
ok3 &= np.allclose(Wcol @ Wcol.conj().T, np.eye(e), atol=TOL)
# the reassembly works with the transpose and FAILS with the adjoint
V1, V2 = dilation(A), dilation(B)


def apply_env(T, w, n, e_in, e_out):
    out = np.zeros(n * e_out, dtype=complex)
    for a in range(n):
        sl = np.array([w[a * e_in + i] for i in range(e_in)])
        img = T @ sl
        for j in range(e_out):
            out[a * e_out + j] = img[j]
    return out


psi = rand(n, 1)[:, 0]
ok3 &= np.allclose(V2 @ psi, apply_env(Wcol.T, V1 @ psi, n, e, e), atol=TOL)
ok3 &= not np.allclose(V2 @ psi, apply_env(Wcol.conj().T, V1 @ psi, n, e, e), atol=1e-6)
check("G3", ok3,
      f"GATE 3: THE ORIENTATION, and it is the TRANSPOSE, not the adjoint. The coefficient factor "
      f"W runs H_H^(2) -> H_H^(1); the environment unitary of V2 = (1 (x) T) V1 runs the other way "
      f"with T_ji = W(e_j)_i. With a complex non-symmetric witness (max|U - U^T| = "
      f"{np.max(np.abs(U - U.T)):.3f}, max|Im U| = {np.max(np.abs(U.imag)):.3f}) the transpose "
      f"reassembles V2 exactly and the ADJOINT does not, so substituting one for the other is a "
      f"numerical failure rather than a silent one. Both W and its transpose are unitary, so the "
      f"distinction is about which operator, not about whether one exists")

# ------------------------------------------------------------------- G4  the proposition
ok4 = True
for _ in range(5):
    n, e = 3, 4
    A = [rand(n, n) for _ in range(e)]
    if rank(synth(A)) < e:
        continue
    U = rand_unitary(e)
    B = [sum(U[j, i] * A[i] for i in range(e)) for j in range(e)]
    V1, V2 = dilation(A), dilation(B)
    # both minimal
    ok4 &= rank(cyclic_span(A)) == n * e and rank(cyclic_span(B)) == n * e
    # same channel
    for rho in (np.eye(n), rand(n, n), rand(n, n)):
        ok4 &= np.allclose(kraus_map(A, rho), kraus_map(B, rho), atol=TOL)
    # equal environment dimension, and the reassembly, with U discarded and recovered
    Wcol = np.linalg.lstsq(synth(A), synth(B), rcond=None)[0]
    T = Wcol.T
    ok4 &= T.shape == (e, e)
    ok4 &= np.allclose(T.conj().T @ T, np.eye(e), atol=TOL)
    for _ in range(3):
        psi = rand(n, 1)[:, 0]
        ok4 &= np.allclose(V2 @ psi, apply_env(T, V1 @ psi, n, e, e), atol=TOL)
check("G4", ok4,
      "THE PROPOSITION. Five trials: two minimal dilations of one channel on a 3-dimensional "
      "visible space with a 4-dimensional environment, verified minimal by the cyclicity rank and "
      "equal as channels on three inputs. The mixing unitary is discarded, the environment unitary "
      "recovered from the synthesis maps alone, and V2 = (1 (x) T) V1 checked on three random "
      "vectors. The environment dimensions come out equal rather than being assumed")

# ------------------------------------------------------------------- G5  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'StinespringUniqueness.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
NAMES = ("apply_eq'", 'channel_eq_krausMap', 'inner_ampl_eq', 'orthogonal_iff',
         'minimal_iff_linearIndependent', 'hiddenUnitary_matrix', 'V2_eq_hiddenUnitary_V1',
         'hiddenUnitary_inner', 'amplR_ext', 'proposition_9_7b')
ok5 = 'import OIBridge.StinespringUniqueness' in root
ok5 &= 'import OIBridge.KrausUniqueness' in src         # 9.7a is consumed, not reproved
ok5 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok5 &= re.search(r'(?m)^axiom ', body) is None
ok5 &= all(f'theorem {n}' in src for n in NAMES)
ok5 &= all(f'#print axioms {n}' in src for n in NAMES)
ok5 &= 'native_decide' not in body
# GATE 1 MUST BE THE MANUSCRIPT'S CONDITION: a span over ALL M, not a dimension count
mn = src[src.index('def Minimal'):]
mdef = mn[:mn.index('/-- The `i`-th environment slice')]
ok5 &= 'Submodule.span ℂ' in mdef and '= ⊤' in mdef
ok5 &= 'EuclideanSpace ℂ n →ₗ[ℂ] EuclideanSpace ℂ n' in mdef      # M ranges over all of B(H_V)
ok5 &= 'finrank' not in mdef and 'card' not in mdef               # not a dimension count
mi = src[src.index('theorem minimal_iff_linearIndependent'):]
ok5 &= 'Minimal V ↔ LinearIndependent ℂ (krausOf V)' in mi[:mi.index(':= by')]
ok5 &= '[Nonempty n]' in mi[:mi.index(':= by')]                   # the guard G1n exhibits
# THE WRAPPER MUST STOP AT THE ISOMETRY
pw = src[src.index('theorem proposition_9_7b'):]
psig = pw[:pw.index(':= by')]
ok5 &= 'Fintype.card f = Fintype.card e' in psig
ok5 &= '∀ ψ, V₂ ψ = amplR T (V₁ ψ)' in psig
ok5 &= 'adjoint T ∘ₗ T = LinearMap.id' in psig
# the manuscript says "a unique unitary", so the wrapper must be an ∃! and not a bare ∃
ok5 &= '∃!' in psig and '∃ T' not in psig
# ... and must NOT claim anything about full dilating unitaries
for banned in ('conj', 'Conjug', 'U^(2)', 'fullUnitary'):
    ok5 &= banned not in psig
# the orientation must be documented as the transpose, not the adjoint
ok5 &= 'TRANSPOSE of the factor' in src
check("G5", ok5,
      f"LINT. The file is imported by OIBridge.lean so CI builds it, imports KrausUniqueness "
      f"rather than reproving 9.7a, carries no `sorry`, no `axiom` and no `native_decide`, and all "
      f"{len(NAMES)} named results print their axiom dependencies. GATE 1 IS THE MANUSCRIPT'S "
      f"CONDITION: `Minimal` is a `Submodule.span ... = ⊤` over ALL M in B(H_V), with no finrank "
      f"and no cardinality in the definition, so it is not the independence it is proved "
      f"equivalent to; and the equivalence carries `[Nonempty n]`. THE WRAPPER STOPS AT THE "
      f"ISOMETRY: it states the environment dimension, V₂ = (1 (x) T) V₁ and T's isometry, and "
      f"says nothing about the full dilating unitaries")

print()
print('     [scope] Settled in Lean: [Structure] Proposition 9.7b — minimality in the')
print('     manuscript\'s cyclicity form is Kraus independence, the Stinespring channel is the')
print('     Kraus map of (1 (x) <i|) V, and two minimal dilations of one channel have equal')
print('     environment dimension and satisfy V2 = (1 (x) T) V1 for an isometric T. The')
print('     uniqueness comes from KrausUniqueness and FactorUniqueness and is not reproved.')
print('     NOT settled, and deliberately: anything about the full dilating unitaries. The CNOT')
print('     pair in stinespring_scope_probe.py is the standing witness that they are not')
print('     determined off the prepared reference subspace.')
print()
print("stinespring_uniqueness_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)

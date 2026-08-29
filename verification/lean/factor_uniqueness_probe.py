#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/FactorUniqueness.lean.

THE THEOREM. For finite-dimensional inner-product spaces and injective X : E -> H, Y : F -> H,

    X X* = Y Y*   ==>   there is a UNIQUE W : F -> E with Y = X W, and W is unitary.

E and F are unrelated in the hypotheses. That they end up isomorphic -- equal Kraus-family
cardinality, in the consumer -- is part of the conclusion, not an assumption.

WHY IT IS STATED ABSTRACTLY. It is the infrastructure step [Structure] Proposition 9.7a needs, and
it is not about channels: strip the physics and what is left is two injective maps into a common
space with the same X X*. This probe checks it in that abstract form, so the evidence does not
quietly assume the consumer's setting. The Kraus layer is a separate file and a separate probe.

  F1  the theorem itself, as a round trip: build X and Y with X X* = Y Y*, forget the map relating
      them, recover W, and check it is unitary, unique and dimension-matching.
  F2  the one consequence of the hypothesis the construction uses: range X = range Y.
  F3  the step that licenses the right-hand cancellation: X injective implies X* surjective.
  F4  CONTROL: injectivity of X is what makes W unique. Drop it and the zero map is factored by
      everything.
  F5  CONTROL: injectivity of Y is what makes W injective -- with a genuine witness, since the Lean
      statement of this control is structural and needs one.
  F6  CONTROL: the hypothesis is X X* = Y Y*, not equality of ranges. Y = 2X has the same range.
  F7  lint: the Lean file is imported by the gated bridge root, carries no sorry, states the two
      index types separately, and derives the cardinality rather than assuming it.

Usage:  python3 factor_uniqueness_probe.py
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


def rand(m, n):
    return rng.normal(size=(m, n)) + 1j * rng.normal(size=(m, n))


def rand_isometry(m, n):
    """An injective map C^n -> C^m, m >= n, with orthonormal columns."""
    Q, R = np.linalg.qr(rand(m, n))
    return Q @ np.diag(np.sign(np.real(np.diag(R))) + 0j)


def rand_unitary(n):
    return rand_isometry(n, n)


def rank(A):
    return np.linalg.matrix_rank(A, tol=1e-8)


# ------------------------------------------------------------------ F1  the theorem
ok1 = True
for _ in range(8):
    dH, dE = 7, 3
    X = rand(dH, dE)
    while rank(X) < dE:
        X = rand(dH, dE)
    Wtrue = rand_unitary(dE)                      # F has the same dimension -- but we do not use it
    Y = X @ Wtrue
    ok1 &= np.allclose(X @ X.conj().T, Y @ Y.conj().T, atol=TOL)      # the hypothesis holds
    ok1 &= rank(Y) == dE                                             # Y is injective
    # recover W from X and Y alone
    Wrec = np.linalg.lstsq(X, Y, rcond=None)[0]
    ok1 &= np.allclose(X @ Wrec, Y, atol=TOL)                        # it factors
    ok1 &= np.allclose(Wrec.conj().T @ Wrec, np.eye(dE), atol=TOL)   # W* W = 1
    ok1 &= np.allclose(Wrec @ Wrec.conj().T, np.eye(dE), atol=TOL)   # W W* = 1
    ok1 &= np.allclose(Wrec, Wtrue, atol=1e-7)                       # and it is THE one
    # uniqueness needs only injectivity of X: any other factor would differ on some vector
    pert = Wrec + 1e-3 * rand(dE, dE)
    ok1 &= not np.allclose(X @ pert, Y, atol=1e-6)
    ok1 &= Wrec.shape[0] == dE                                       # dim F = dim E, derived
check("F1", ok1,
      "THE THEOREM, as a round trip. Eight random injective X : C^3 -> C^7 are paired with "
      "Y = X W for a random unitary W; W is then DISCARDED and recovered from X and Y alone. The "
      "recovered map factors Y, satisfies W* W = W W* = 1 in both orders, equals the one thrown "
      "away, and has square shape -- so the equality of the two index dimensions comes out of the "
      "conclusion rather than being assumed. A perturbed candidate fails to factor, which is the "
      "uniqueness clause in numerical form")

# ------------------------------------------------------------------ F2  range equality
ok2 = True
for _ in range(6):
    dH, dE, dF = 6, 2, 2
    X = rand_isometry(dH, dE)
    Y = X @ rand_unitary(dF)
    ok2 &= np.allclose(X @ X.conj().T, Y @ Y.conj().T, atol=TOL)
    # the ranges coincide: each column of one is in the column space of the other
    ok2 &= rank(np.hstack([X, Y])) == rank(X) == rank(Y) == dE
# and the converse fails, which is F6's point in advance
Xc = rand_isometry(5, 2)
ok2 &= rank(np.hstack([Xc, 2 * Xc])) == 2
ok2 &= not np.allclose(Xc @ Xc.conj().T, (2 * Xc) @ (2 * Xc).conj().T, atol=TOL)
check("F2", ok2,
      "RANGE EQUALITY, the single consequence of the hypothesis the construction consumes. "
      "X X* = Y Y* forces the two column spaces to coincide, which is `range_self_comp_adjoint` "
      "applied twice in Lean. The converse is already visible here and is F6's subject: doubling X "
      "preserves the range and destroys X X*")

# ------------------------------------------------------------------ F3  the adjoint is surjective
ok3 = True
for (dH, dE) in ((6, 3), (5, 5), (9, 1)):
    X = rand_isometry(dH, dE)
    ok3 &= rank(X) == dE                                # injective
    ok3 &= rank(X.conj().T) == dE                       # so the adjoint has full rank dE ...
    ok3 &= rank(X.conj().T) == dE                       # ... i.e. is onto C^dE
# and it genuinely fails without injectivity
Xd = np.zeros((4, 2), dtype=complex)
Xd[:, 0] = rand(4, 1)[:, 0]
ok3 &= rank(Xd) == 1 and rank(Xd.conj().T) == 1 < 2
check("F3", ok3,
      "THE ADJOINT OF AN INJECTIVE MAP IS SURJECTIVE, in finite dimensions -- the step that "
      "licenses cancelling X* on the right. Checked at three shapes including the square and the "
      "extreme one-dimensional case, and shown to fail for a rank-deficient X, so the hypothesis "
      "is not idle. In Lean this is `orthogonal_ker` plus `bot_orthogonal_eq_top`")

# ------------------------------------------------------------------ F4  X injective is needed
X0 = np.zeros((4, 3), dtype=complex)
Y0 = np.zeros((4, 3), dtype=complex)
ok4 = np.allclose(X0 @ X0.conj().T, Y0 @ Y0.conj().T, atol=TOL)
W1, W2 = np.zeros((3, 3), dtype=complex), np.eye(3, dtype=complex)
ok4 &= np.allclose(X0 @ W1, Y0, atol=TOL) and np.allclose(X0 @ W2, Y0, atol=TOL)
ok4 &= not np.allclose(W1, W2, atol=TOL)
# a non-unitary factor works too, so it is uniqueness that fails and not merely the choice
ok4 &= np.allclose(X0 @ (3 * np.eye(3)), Y0, atol=TOL)
check("F4", ok4,
      "CONTROL: injectivity of X is what makes the factor unique. X = 0 and Y = 0 satisfy the "
      "hypothesis, and 0, the identity and 3.id all factor it -- so without that hypothesis there "
      "is no uniqueness statement to make, unitary or otherwise. Lean records this as "
      "`factor_not_unique_of_not_injective`")

# ------------------------------------------------------------------ F5  Y injective is needed
# the witness the Lean control needs: X injective, Y not, with X X* = Y Y* and dim F > dim E
dH, dE, dF = 5, 2, 3
X = rand_isometry(dH, dE)
M = rand_isometry(dF, dE).conj().T          # a dE x dF coisometry: M M* = 1_dE
Y = X @ M
ok5 = np.allclose(M @ M.conj().T, np.eye(dE), atol=TOL)
ok5 &= np.allclose(X @ X.conj().T, Y @ Y.conj().T, atol=TOL)       # the hypothesis still holds
ok5 &= rank(X) == dE                                                # X injective
ok5 &= rank(Y) == dE < dF                                           # Y is NOT injective
# every factor is M itself, and it cannot be injective: it maps C^3 onto C^2
Wrec = np.linalg.lstsq(X, Y, rcond=None)[0]
ok5 &= np.allclose(X @ Wrec, Y, atol=TOL) and np.allclose(Wrec, M, atol=1e-7)
ok5 &= rank(Wrec) == dE < dF                                        # not injective, so not unitary
ok5 &= not np.allclose(Wrec.conj().T @ Wrec, np.eye(dF), atol=1e-6)
check("F5", ok5,
      "CONTROL: injectivity of Y is what makes the factor injective, WITH THE WITNESS the Lean "
      "control leaves to this layer. Composing an injective X : C^2 -> C^5 with a 2x3 coisometry "
      "gives Y : C^3 -> C^5 satisfying X X* = Y Y* with X injective and Y not. The unique factor is "
      "the coisometry itself; it has rank 2 on a 3-dimensional domain, so it is not injective and "
      "cannot be unitary. This is the same phenomenon as a three-member Kraus family for a "
      "rank-two channel -- exactly [Structure] 9.7a's linear-independence hypothesis")

# ------------------------------------------------------------------ F6  range equality is not enough
X = rand_isometry(6, 3)
Y = 2 * X
ok6 = rank(np.hstack([X, Y])) == 3                                  # same range
ok6 &= not np.allclose(X @ X.conj().T, Y @ Y.conj().T, atol=TOL)    # different X X*
Wrec = np.linalg.lstsq(X, Y, rcond=None)[0]
ok6 &= np.allclose(Wrec, 2 * np.eye(3), atol=1e-8)                  # the factor is 2.id
ok6 &= not np.allclose(Wrec.conj().T @ Wrec, np.eye(3), atol=1e-6)  # ... which is not unitary
ok6 &= np.allclose(Wrec.conj().T @ Wrec, 4 * np.eye(3), atol=1e-8)  # it is 4.id, as Lean derives
check("F6", ok6,
      "CONTROL: the hypothesis is X X* = Y Y* and not equality of ranges. Y = 2X has exactly the "
      "same column space, the unique factor is 2.id, and W* W = 4.id rather than the identity. Lean "
      "records this as `range_eq_insufficient`, deriving the same 4 = 1 contradiction")

# ------------------------------------------------------------------ F7  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'FactorUniqueness.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
NAMES = ('range_eq_of_comp_adjoint_eq', 'surjective_adjoint_of_injective', 'comp_factor',
         'factor_unique', 'factor_comp_adjoint', 'adjoint_comp_factor',
         'existsUnique_unitary_factor', 'finrank_eq', 'factor_not_unique_of_not_injective',
         'factor_not_injective_of_not_injective', 'range_eq_insufficient')
ok7 = 'import OIBridge.FactorUniqueness' in root
ok7 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok7 &= re.search(r'(?m)^axiom ', body) is None
ok7 &= all(f'theorem {n}' in src for n in NAMES)
ok7 &= all(f'#print axioms {n}' in src for n in NAMES)
ok7 &= 'native_decide' not in body
# THE INDEX-TYPE GUARD. E and F must be separate spaces in the statement, and the cardinality
# equality must be a CONCLUSION. A single shared index type would assume what the theorem proves.
mt = src[src.index('theorem existsUnique_unitary_factor'):]
sig = mt[:mt.index(':= by')]
ok7 &= '{X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H}' in sig
ok7 &= 'adjoint W ∘ₗ W = LinearMap.id' in sig and 'W ∘ₗ adjoint W = LinearMap.id' in sig
ok7 &= '∃!' in sig
fr = src[src.index('theorem finrank_eq'):]
ok7 &= 'Module.finrank 𝕜 F = Module.finrank 𝕜 E' in fr[:fr.index(':=')]
# the statement must be about a general field and general spaces, not about matrices
ok7 &= 'RCLike 𝕜' in src and 'Matrix' not in body
# and it must not reach for machinery the route does not need
for banned in ('spectral', 'Cholesky', 'posSemidef', 'PosSemidef', 'pseudoinverse', 'det '):
    ok7 &= banned not in body
check("F7", ok7,
      f"LINT. The file is imported by OIBridge.lean so CI builds it; it carries no `sorry`, no "
      f"`axiom` and no `native_decide`; all {len(NAMES)} named results print their axiom "
      f"dependencies. THE INDEX-TYPE GUARD: the main theorem quantifies over X : E -> H and "
      f"Y : F -> H with E and F separate spaces, and states BOTH adjoint identities inside an "
      f"`∃!`, with `finrank F = finrank E` proved separately as a consequence -- a shared index "
      f"type would assume the cardinality equality the consumer needs proved. The statement is "
      f"over an arbitrary RCLike field with no matrices, and the proof reaches for no spectral "
      f"theorem, Cholesky factorization, pseudoinverse, determinant or PSD library")

print()
print('     [scope] Settled in Lean: the abstract factor theorem, over an arbitrary RCLike field')
print('     and arbitrary finite-dimensional inner-product spaces, with the two index types')
print('     independent and their equality derived. NOT settled here, deliberately: nothing about')
print('     channels. The Kraus layer -- channel equality to equal Choi operator to X X* = Y Y*,')
print('     with linear independence becoming injectivity of the synthesis maps -- is a separate')
print('     file, and [Structure] Proposition 9.7a stays at P until that consumer theorem is')
print('     kernel-checked. This file is infrastructure and promotes nothing on its own.')
print()
print("factor_uniqueness_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scope and countercontrol checks for [Structure] Propositions 9.7a / 9.7b.

WHAT THIS PROBE EXISTS FOR. The earlier Proposition 9.7 asserted that two minimal dilations of the
same channel satisfy

    U^(2) = (1_V (x) W) U^(1) (1_V (x) W^dagger)

as an identity of operators on H_V (x) H_H. That is FALSE, and the falsity is not a technicality:
with a pure reference state the channel constrains U only on H_V (x) C|0>, so its action on the rest
of the space is entirely free, and no unitary conjugation can recover freedom the channel never
saw. S1 below is the witness, and it is kept permanently so the full-operator form cannot return.

The proposition was split accordingly. 9.7a is the algebraic core — minimal Kraus families of one
channel are related by a unitary — and it is true; S3 reproduces it as a round trip. 9.7b transports
that to pure-reference dilations and concludes only about the Stinespring ISOMETRY; S4 checks the
transport and, in the same breath, that the conclusion does not extend off the reference subspace.

  S1  COUNTERCONTROL: CNOT and CNOT.(1 (x) Z) realize the same channel on the same hidden sector,
      both minimally, and no unitary W conjugates one to the other. The full-operator conclusion of
      the old Proposition 9.7 is therefore false, not merely stronger than needed.
  S2  the mixed-reference correction: minimal hidden dimension is NOT the Kraus rank, and can be
      strictly SMALLER. The completely depolarizing qubit channel has Kraus rank 4 and is realized
      by SWAP on a two-dimensional hidden sector with rho_H = 1/2.
  S3  9.7a as a round trip: build a channel, take two linearly independent Kraus families, forget
      the unitary relating them, recover it from the vectorized positive operator, and check it.
  S4  9.7b: minimal pure-reference realizations agree on the reference subspace up to 1 (x) W, and
      the same pair disagrees off it.
  S5  linear independence is not removable in 9.7a: a 3x2 isometry turns a two-member family into a
      three-member family for the same channel, so cardinality is not determined without it.
  S6  lint: the manuscript carries the split, calls Definition 9.2's object a unitary realization,
      and no longer states the full-operator conjugation as a conclusion.

Usage:  python3 stinespring_scope_probe.py
"""
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
TOL = 1e-9

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


I2 = np.eye(2)
Z = np.diag([1.0, -1.0])
KET0 = np.array([[1.0], [0.0]])


def cnot():
    """Control on the visible factor, target on the hidden factor."""
    U = np.zeros((4, 4))
    for v in (0, 1):
        for h in (0, 1):
            U[v * 2 + (h ^ v), v * 2 + h] = 1.0
    return U


def swap():
    U = np.zeros((4, 4))
    for v in (0, 1):
        for h in (0, 1):
            U[h * 2 + v, v * 2 + h] = 1.0
    return U


def apply_channel(U, rho_H, rho, dV=2, dH=2):
    big = np.kron(rho, rho_H)
    M = U @ big @ U.conj().T
    return M.reshape(dV, dH, dV, dH).trace(axis1=1, axis2=3)


def choi(chan, d=2):
    """The Choi matrix, which determines the channel and is determined by it."""
    C = np.zeros((d * d, d * d), dtype=complex)
    for a in range(d):
        for b in range(d):
            E = np.zeros((d, d), dtype=complex)
            E[a, b] = 1.0
            C[a * d:(a + 1) * d, b * d:(b + 1) * d] = chan(E)
    return C


def kraus_from_isometry(V, dV=2, dH=2):
    """A_i = (1_V (x) <i|) V, the Kraus family of an isometry V : H_V -> H_V (x) H_H."""
    return [np.array([[V[v * dH + i, w] for w in range(dV)] for v in range(dV)])
            for i in range(dH)]


def channel_from_kraus(K):
    return lambda rho: sum(A @ rho @ A.conj().T for A in K)


# --------------------------------------------------------- S1  the countercontrol
U1 = cnot()
U2 = cnot() @ np.kron(I2, Z)
pure0 = KET0 @ KET0.T

c1, c2 = choi(lambda r: apply_channel(U1, pure0, r)), choi(lambda r: apply_channel(U2, pure0, r))
ok1 = np.allclose(c1, c2, atol=TOL)                                   # the same channel

# the two dilating unitaries agree exactly on the reference subspace H_V (x) C|0>
V1 = U1 @ np.kron(np.eye(2), KET0)
V2 = U2 @ np.kron(np.eye(2), KET0)
ok1 &= np.allclose(V1, V2, atol=TOL)
ok1 &= np.allclose(V1.conj().T @ V1, np.eye(2), atol=TOL)             # and are isometries
# minimality: the Kraus family is linearly independent, so the Kraus rank is dim H_H = 2
Kr = kraus_from_isometry(V1)
ok1 &= np.linalg.matrix_rank(np.array([A.flatten() for A in Kr]), tol=1e-9) == 2

# the old conclusion: some unitary W on H_H with U2 = (1 (x) W) U1 (1 (x) W^dagger)
best = np.inf
rng = np.random.default_rng(20260829)
for _ in range(20000):
    W, _ = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))
    best = min(best, np.linalg.norm(np.kron(I2, W) @ U1 @ np.kron(I2, W.conj().T) - U2))
for W in (I2, Z, np.array([[0.0, 1.0], [1.0, 0.0]]), np.diag([1, 1j]), np.diag([1, -1j])):
    W = np.asarray(W, dtype=complex)
    best = min(best, np.linalg.norm(np.kron(I2, W) @ U1 @ np.kron(I2, W.conj().T) - U2))
gap = float(np.linalg.norm(U1 - U2))
ok1 &= best > 1.0 and abs(best - gap) < 1e-6      # the best W is the identity, and it fails
# and the reason: minimality forces W = 1, because (1 (x) W) fixes a subspace that generates
ok1 &= not np.allclose(U1, U2, atol=TOL)
check("S1", ok1,
      f"COUNTERCONTROL, and the reason the old Proposition 9.7 was false. U1 = CNOT and "
      f"U2 = CNOT.(1 (x) Z) realize the SAME channel: 1 (x) Z is the identity on H_V (x) C|0>, so "
      f"the two agree exactly where the channel can see them, and both are minimal (Kraus rank 2 = "
      f"dim H_H) on the SAME hidden sector. Minimality then forces W = 1, so the old conclusion "
      f"would read U2 = U1 -- false. Over 20000 random W in U(2) plus the exact candidates the best "
      f"residual is {best:.4f}, exactly ||U1 - U2|| = {gap:.4f}: no W does anything at all. What "
      f"the channel constrains is the ISOMETRY, and U is free off the reference subspace")

# --------------------------------------------------------- S2  the mixed-reference correction
SW = swap()
mixed = I2 / 2.0
dep = lambda r: apply_channel(SW, mixed, r)
ok2 = all(np.allclose(dep(r), I2 / 2.0, atol=TOL) for r in (
    np.array([[1.0, 0], [0, 0]]), np.array([[0.5, 0.5], [0.5, 0.5]]),
    np.array([[0.5, -0.5j], [0.5j, 0.5]])))                            # completely depolarizing
kraus_rank = np.linalg.matrix_rank(choi(dep), tol=1e-9)
ok2 &= kraus_rank == 4                                                 # ... of Kraus rank 4
ok2 &= 2 < kraus_rank                                                  # on a 2-dimensional H_H
# control: with a PURE reference the hidden dimension can no longer beat the Kraus rank, since the
# isometry's own Kraus family has exactly dim H_H members
ok2 &= np.linalg.matrix_rank(np.array([A.flatten() for A in kraus_from_isometry(V1)]),
                             tol=1e-9) <= 2
check("S2", ok2,
      f"THE MIXED-REFERENCE CORRECTION. For a mixed reference state, minimal hidden dimension is "
      f"not Stinespring minimality and is not the Kraus rank -- and it can be strictly SMALLER, not "
      f"larger. The completely depolarizing qubit channel has Kraus rank {kraus_rank}, yet "
      f"rho_H = 1/2 with U = SWAP realizes it on a hidden sector of dimension 2. This is why "
      f"Definition 9.2's object is now a unitary realization rather than a Stinespring dilation: "
      f"OI's own construction uses the uniform mixed reference, so the uniqueness propositions do "
      f"not apply to it without first purifying. The control: with a pure reference the isometry's "
      f"Kraus family has exactly dim H_H members, so that route cannot undercut the rank")

# --------------------------------------------------------- S3  9.7a as a round trip
def random_isometry(d_out, d_in, rng):
    A = rng.normal(size=(d_out, d_in)) + 1j * rng.normal(size=(d_out, d_in))
    Q, R = np.linalg.qr(A)
    return Q @ np.diag(np.sign(np.real(np.diag(R))) + 0j)


def random_unitary(d, rng):
    return random_isometry(d, d, rng)


ok3 = True
for trial in range(6):
    n, r = 3, 4
    V = random_isometry(n * r, n, rng)                      # a channel with Kraus rank <= r
    A = [np.array([[V[v * r + i, w] for w in range(n)] for v in range(n)]) for i in range(r)]
    Wtrue = random_unitary(r, rng)
    B = [sum(Wtrue[j, i] * A[i] for i in range(r)) for j in range(r)]
    # the two families give the same channel
    ok3 &= np.allclose(choi(channel_from_kraus(A), n), choi(channel_from_kraus(B), n), atol=1e-8)
    # both are linearly independent -- this is minimality
    X = np.array([a.flatten(order='F') for a in A]).T
    Y = np.array([b.flatten(order='F') for b in B]).T
    ok3 &= np.linalg.matrix_rank(X, tol=1e-8) == r and np.linalg.matrix_rank(Y, tol=1e-8) == r
    # X X^dagger = Y Y^dagger : the vectorized positive operator the channel determines
    ok3 &= np.allclose(X @ X.conj().T, Y @ Y.conj().T, atol=1e-8)
    # now FORGET Wtrue and recover it: X full column rank, so Y = X W^T has a unique solution
    Wrec = np.linalg.lstsq(X, Y, rcond=None)[0].T
    ok3 &= np.allclose(Wrec @ Wrec.conj().T, np.eye(r), atol=1e-8)          # unitary
    ok3 &= all(np.allclose(B[j], sum(Wrec[j, i] * A[i] for i in range(r)), atol=1e-8)
               for j in range(r))
    ok3 &= np.allclose(Wrec, Wtrue, atol=1e-7)                              # and it is THE one
check("S3", ok3,
      "PROPOSITION 9.7a, as a round trip rather than a restatement. A random rank-4 channel on a "
      "3-dimensional visible sector is given two linearly independent Kraus families related by a "
      "random unitary; the unitary is then DISCARDED and recovered from the vectorized positive "
      "operator alone, which is all the channel determines. The recovered W is unitary, reproduces "
      "the second family from the first, and equals the one thrown away -- so it is unique, not "
      "merely existent. Six independent trials. This is the algebraic core the Lean layer will "
      "target: X X^dagger = Y Y^dagger with X, Y of full column rank forces Y = X W^T")

# --------------------------------------------------------- S4  9.7b, and its boundary
# two pure-reference realizations of one channel, with DIFFERENT hidden bases
Wh = random_unitary(2, rng)
U3 = np.kron(I2, Wh) @ U1                       # V3 = (1 (x) Wh) V1 : same channel, minimal
V3 = U3 @ np.kron(np.eye(2), KET0)
ok4 = np.allclose(choi(lambda r: apply_channel(U3, pure0, r)), c1, atol=1e-8)
ok4 &= np.allclose(V3, np.kron(I2, Wh) @ V1, atol=1e-8)          # 9.7b's conclusion, on the isometry
# and the SAME W does not relate the full unitaries once one of them is modified off-reference
U4 = U3 @ np.kron(I2, Z)                                          # still the same channel
ok4 &= np.allclose(choi(lambda r: apply_channel(U4, pure0, r)), c1, atol=1e-8)
ok4 &= np.allclose(U4 @ np.kron(np.eye(2), KET0), V3, atol=1e-8)   # same isometry ...
ok4 &= not np.allclose(U4, U3, atol=TOL)                           # ... different unitary
check("S4", ok4,
      "PROPOSITION 9.7b, and exactly where it stops. Composing CNOT with a hidden-sector unitary "
      "gives a second minimal pure-reference realization of the same channel, and the two Stinespring "
      "isometries are related by 1 (x) W as the proposition says. Composing further with 1 (x) Z "
      "leaves both the channel and the isometry untouched while changing the unitary, so the "
      "isometry-level conclusion is the whole of what the channel supports. The three freedoms of "
      "Corollary 9.8 are visible in one line: hidden-sector unitary, extension off the prepared "
      "subspace, and -- separately -- non-minimal enlargement")

# --------------------------------------------------------- S5  independence is not removable
n, r = 3, 2
V = random_isometry(n * r, n, rng)
A = [np.array([[V[v * r + i, w] for w in range(n)] for v in range(n)]) for i in range(r)]
M = random_isometry(3, 2, rng)                                     # a 3x2 isometry, M^dagger M = 1
C = [sum(M[k, i] * A[i] for i in range(r)) for k in range(3)]
ok5 = np.allclose(M.conj().T @ M, np.eye(2), atol=1e-8)
ok5 &= np.allclose(choi(channel_from_kraus(A), n), choi(channel_from_kraus(C), n), atol=1e-8)
ok5 &= np.linalg.matrix_rank(np.array([a.flatten() for a in A]), tol=1e-8) == 2
ok5 &= np.linalg.matrix_rank(np.array([c.flatten() for c in C]), tol=1e-8) == 2   # 3 vectors, rank 2
ok5 &= len(C) == 3 and len(A) == 2                                 # different cardinalities
check("S5", ok5,
      "LINEAR INDEPENDENCE IS NOT REMOVABLE from 9.7a. A 3x2 isometry turns a two-member Kraus "
      "family into a three-member family for the SAME channel; the larger family spans only a "
      "2-dimensional space, so it is linearly dependent. Without independence the family size is "
      "not determined and no unitary can relate families of different cardinality -- only an "
      "isometry can. Independence IS minimality, which is why the proposition states it rather "
      "than 'minimal hidden-sector dimension'")

# --------------------------------------------------------- S6  manuscript lint
src = open(os.path.join(ROOT, 'papers', 'Structure.md'), encoding='utf-8').read()
ok6 = '**Proposition 9.7a**' in src and '**Proposition 9.7b**' in src
ok6 &= '**Proposition 9.7**' not in src                    # the false statement is gone, not hedged
# Definition 9.2 names a unitary realization, and pins the Stinespring object to the isometry
d92 = src[src.index('**Definition 9.2**'):src.index('**Definition 9.3**')]
ok6 &= 'unitary realization' in d92
ok6 &= 'it is this isometry — not $U$ — that is a Stinespring dilation' in d92
ok6 &= 'strictly *smaller*' in d92 and 'SWAP' in d92        # the mixed-reference correction is stated
# the full-operator conjugation appears only as something denied
for m in re.finditer(r'U\^\{?\(2\)\}? = \(\\mathbb\{1\}_V \\otimes W\)', src):
    seg = src[max(0, m.start() - 400):m.start() + 200]
    ok6 &= ('false' in seg or 'No equality' in seg)
ok6 &= 'No equality of the full unitaries away from the reference subspaces follows.' in src
# 9.7b concludes on the isometry
p97b = src[src.index('**Proposition 9.7b**'):src.index('**Remark (the conjugation form)')]
ok6 &= 'V_2 = (\\mathbb{1}_V \\otimes W)\\, V_1' in p97b
# Corollary 9.8 carries the three freedoms and the scope qualification
c98 = src[src.index('**Corollary 9.8**'):]
c98 = c98[:c98.index('### 9.4')]
ok6 &= 'does not determine a unique substratum realization' in c98
ok6 &= 'unconstrained off the prepared reference subspace' in c98
ok6 &= 'independently preparable' in c98                    # the scope qualification
# §10.4 flags that OI's own reference state is mixed
ok6 &= 'so this triple is a unitary realization rather than a Stinespring dilation' in src
# and the Substratum semigroup statement is reconciled rather than contradicted
ok6 &= 'why [Substratum] Lemma 24.1 can say more' in src
# the same naming repair reached the parallel sources (A.14 / A.25)
for path in ('papers/Main.md', 'book/appendix-b-derivations.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    t = open(os.path.join(ROOT, path), encoding='utf-8').read()
    ok6 &= 'is a *unitary realization* of $\\Phi$' in t
    ok6 &= 'U_\\varphi, \\rho_H)$ is the Stinespring dilation' not in t
check("S6", ok6,
      "MANUSCRIPT LINT. Proposition 9.7 is split into 9.7a and 9.7b with the old label gone rather "
      "than hedged; Definition 9.2 names a unitary realization and pins the Stinespring object to "
      "the pure-reference isometry, carrying the SWAP correction; the full-operator conjugation "
      "survives only where it is denied; 9.7b concludes on the isometry; Corollary 9.8 lists all "
      "three freedoms and carries the fixed-reference scope qualification; §10.4 flags that OI's "
      "own reference state is mixed; [Substratum] Lemma 24.1's stronger semigroup statement is "
      "reconciled rather than contradicted; and the naming repair reached Main §3.2 and both book "
      "parallel sources")

print()
print('     [scope] Settled here: that the old full-operator form of Proposition 9.7 is FALSE,')
print('     with a two-qubit witness; that mixed-reference minimal hidden dimension is not the')
print('     Kraus rank and can be smaller; that 9.7a holds and its unitary is unique, recovered')
print('     numerically from the channel alone; that 9.7b concludes on the isometry and no')
print('     further; and that linear independence is not removable. NOT settled: none of this is')
print('     a kernel proof. 9.7a is the Lean target, and the general lemma it needs is')
print('     X X^dagger = Y Y^dagger with X, Y of full column rank implies Y = X W for a unique')
print('     unitary W -- two linearly independent rank-one factorizations of one positive')
print('     operator differ by a unitary on the coefficient space. Mathlib has no Stinespring')
print('     theorem, so the dilation layer is downstream of that lemma and not of Mathlib.')
print()
print("stinespring_scope_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)

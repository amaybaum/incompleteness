#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/IdempotentTrace.lean.

This file certifies no manuscript statement. It is INFRASTRUCTURE: the library lemma [SM]
Theorem 7's formalization was blocked on, isolated so that the blocker becomes a resolved
dependency rather than a theorem-specific workaround. The lemma is

    P idempotent, f commuting with P  =>  tr(f restricted to im P) = tr(f . P),

and it mentions no group, no character and no equivariance. The checks here are aimed at the two
hypotheses, because a lemma this short is exactly the kind that gets stated with one of them
quietly missing.

  T1  the identity itself, exactly, over random idempotents and random commuting maps.
  T2  the SHARP hypothesis: commutativity is sufficient but not necessary — only invariance of the
      image is used, and this check is what established it, no countercontrol being available.
  T3  COUNTERCONTROL: drop idempotency and the identity fails.
  T4  the block structure: f preserves im P and ker P, and the two are complementary. These are the
      steps the proof actually goes through, checked independently of the trace.
  T5  the free corollary tr P = dim(im P), and its failure for non-idempotent P.
  T6  lint: the Lean file is imported by the gated bridge root, carries no sorry, states the lemma
      over an arbitrary field with no representation-theoretic hypothesis, and proves the block
      structure without finite-dimensionality.

Usage:  python3 idempotent_trace_probe.py
"""
import os
import random
import re
import sys
from fractions import Fraction as F

CHECKS = []


def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.join(HERE, os.pardir, 'lean-mathlib')
rng = random.Random(70417)


# ----------------------------------------------------------------- exact matrix algebra
def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def rank(A):
    M = [r[:] for r in A]
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = F(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r


def col_space_basis(A):
    """A basis of the column space, as a list of column vectors."""
    n = len(A)
    cols = [[A[i][j] for i in range(n)] for j in range(len(A[0]))]
    basis = []
    for c in cols:
        cand = basis + [c]
        if rank([[v[i] for v in cand] for i in range(n)]) > len(basis):
            basis.append(c)
    return basis


def in_span(basis, v):
    if not basis:
        return all(x == 0 for x in v)
    n = len(v)
    return rank([[u[i] for u in basis] for i in range(n)]) == \
        rank([[u[i] for u in basis + [v]] for i in range(n)])


def apply(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def unimodular(n):
    """A random integer matrix of determinant 1, so its inverse is integral and exact."""
    S = eye(n)
    for _ in range(6):
        i, j = rng.sample(range(n), 2)
        E = eye(n)
        E[i][j] = F(rng.randint(-2, 2))
        S = mul(S, E)
    return S


def inverse(A):
    n = len(A)
    M = [A[i][:] + eye(n)[i][:] for i in range(n)]
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, n) if M[i][c] != 0), None)
        assert piv is not None
        M[r], M[piv] = M[piv], M[r]
        inv = F(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(n):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return [row[n:] for row in M]


def random_idempotent(n, r):
    """S diag(1^r, 0^(n-r)) S^-1, exactly idempotent by construction."""
    S = unimodular(n)
    D = [[F(1) if (i == j and i < r) else F(0) for j in range(n)] for i in range(n)]
    return mul(mul(S, D), inverse(S))


def random_commuting(P, n):
    """P A P + (I-P) B (I-P) commutes with P for any A, B."""
    Q = sub(eye(n), P)
    A = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(n)]
    B = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(n)]
    return add(mul(mul(P, A), P), mul(mul(Q, B), Q))


def restrict_trace(f, P, n):
    """tr of f restricted to im P, computed in a basis of the column space of P."""
    basis = col_space_basis(P)
    r = len(basis)
    if r == 0:
        return F(0)
    # express f(b_j) in the basis: solve [basis] x = f(b_j)
    M = [[basis[j][i] for j in range(r)] for i in range(n)]
    tr = F(0)
    for j in range(r):
        rhs = apply(f, basis[j])
        aug = [M[i][:] + [rhs[i]] for i in range(n)]
        # Gauss-Jordan to read off the j-th coordinate
        rr = 0
        piv_col = {}
        for c in range(r):
            piv = next((i for i in range(rr, n) if aug[i][c] != 0), None)
            if piv is None:
                continue
            aug[rr], aug[piv] = aug[piv], aug[rr]
            inv = F(1) / aug[rr][c]
            aug[rr] = [x * inv for x in aug[rr]]
            for i in range(n):
                if i != rr and aug[i][c] != 0:
                    fct = aug[i][c]
                    aug[i] = [a - fct * b for a, b in zip(aug[i], aug[rr])]
            piv_col[c] = rr
            rr += 1
        assert j in piv_col, "f does not preserve im P"
        tr += aug[piv_col[j]][r]
    return tr


# ----------------------------------------------------------------- T1  the identity
ok1 = True
n1 = 0
for n in (2, 3, 4, 5):
    for r in range(0, n + 1):
        for _ in range(6):
            P = random_idempotent(n, r)
            assert mul(P, P) == P
            f = random_commuting(P, n)
            assert mul(f, P) == mul(P, f)
            ok1 &= restrict_trace(f, P, n) == trace(mul(f, P))
            n1 += 1
check("T1", ok1,
      f"THE IDENTITY, exactly in rational arithmetic on {n1} (idempotent, commuting map) pairs "
      f"across dimensions 2 to 5 and every rank from 0 to the dimension: the trace of f restricted "
      f"to the image of P equals the trace of f composed with P. The restricted trace is computed "
      f"in an independently derived basis of the column space, not from the formula being tested")

# ----------------------------------------------------------------- T2  the sharp hypothesis
# Commutativity turns out to be SUFFICIENT BUT NOT NECESSARY. Searching for a countercontrol found
# none, and the reason is structural: in the decomposition V = im P + ker P, invariance of the image
# alone makes f block TRIANGULAR, and f.P kills the off-diagonal block either way. So this check
# reports the sharp hypothesis rather than a failure, and the Lean file carries the weaker lemma.
ok2 = True
tested2 = 0
for _ in range(6000):
    n = 3
    P = random_idempotent(n, 2)
    f = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(n)]
    if mul(f, P) == mul(P, f):
        continue
    basis = col_space_basis(P)
    if not all(in_span(basis, apply(f, b)) for b in basis):
        continue
    ok2 &= restrict_trace(f, P, n) == trace(mul(f, P))
    tested2 += 1
ok2 &= tested2 >= 10
# and when the image is NOT invariant there is no restriction at all, so the left side is undefined
noninv = 0
for _ in range(3000):
    n = 3
    P = random_idempotent(n, 2)
    f = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(n)]
    basis = col_space_basis(P)
    if basis and not all(in_span(basis, apply(f, b)) for b in basis):
        noninv += 1
ok2 &= noninv > 0
check("T2", ok2,
      f"THE SHARP HYPOTHESIS. No countercontrol for commutativity exists, and this check is what "
      f"established that: on {tested2} maps that preserve the image of P but do NOT commute with "
      f"it, the identity holds every time. Commuting also controls the kernel block, which the "
      f"trace never sees — image-invariance makes f block TRIANGULAR and f.P kills the "
      f"off-diagonal block either way. Image-invariance is nonetheless load-bearing in the only "
      f"sense available: on {noninv} maps that fail it, f has no restriction to the image at all, "
      f"so the left-hand side is undefined rather than wrong. The Lean file records both forms, "
      f"with `trace_restrict_range_of_mapsTo` the weaker one"),

# ----------------------------------------------------------------- T3  countercontrol
ok3 = False
best3 = None
for _ in range(400):
    n = 3
    P = [[F(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
    if mul(P, P) == P:
        continue
    f = eye(n)
    basis = col_space_basis(P)
    if not basis or not all(in_span(basis, apply(f, b)) for b in basis):
        continue
    lhs, rhs = restrict_trace(f, P, n), trace(mul(f, P))
    if lhs != rhs:
        ok3 = True
        best3 = (lhs, rhs, rank(P))
        break
check("T3", ok3,
      f"COUNTERCONTROL for IDEMPOTENCY. Drop `P ∘ₗ P = P` and the identity fails even at f = id: "
      f"the restricted trace reads {best3[0]} — the rank {best3[2]}, since the identity restricted "
      f"to any subspace has trace equal to its dimension — against tr(P) = {best3[1]}. Without "
      f"idempotency the space does not split as im P ⊕ ker P at all, and the block argument has "
      f"nothing to stand on")

# ----------------------------------------------------------------- T4  the block structure
ok4 = True
n4 = 0
for n in (3, 4, 5):
    for r in range(1, n):
        for _ in range(8):
            P = random_idempotent(n, r)
            f = random_commuting(P, n)
            Q = sub(eye(n), P)
            imb = col_space_basis(P)
            kerb = col_space_basis(Q)                    # ker P = im (I - P) for idempotent P
            ok4 &= all(in_span(imb, apply(f, b)) for b in imb)      # f preserves im P
            ok4 &= all(in_span(kerb, apply(f, b)) for b in kerb)    # f preserves ker P
            ok4 &= len(imb) + len(kerb) == n                        # complementary
            ok4 &= all(apply(P, b) == b for b in imb)               # P fixes its image
            ok4 &= all(all(x == 0 for x in apply(P, b)) for b in kerb)
            n4 += 1
check("T4", ok4,
      f"THE BLOCK STRUCTURE, on {n4} systems: f maps the image of P into itself and the kernel into "
      f"itself, the two have complementary dimensions, P fixes its image pointwise and kills the "
      f"kernel. These are `mapsTo_range`, `mapsTo_ker`, `isCompl_range_ker` and "
      f"`apply_eq_self_of_mem_range` — the steps the Lean proof goes through, checked here without "
      f"reference to any trace")

# ----------------------------------------------------------------- T5  the free corollary
ok5 = True
n5 = 0
for n in (2, 3, 4, 5):
    for r in range(0, n + 1):
        for _ in range(5):
            P = random_idempotent(n, r)
            ok5 &= trace(P) == F(rank(P)) and rank(P) == r
            n5 += 1
# and it fails without idempotency
bad5 = None
for _ in range(500):
    P = [[F(rng.randint(-2, 2)) for _ in range(3)] for _ in range(3)]
    if mul(P, P) != P and trace(P) != F(rank(P)):
        bad5 = (trace(P), rank(P))
        break
ok5 &= bad5 is not None
check("T5", ok5,
      f"THE FREE COROLLARY tr P = dim(im P) on {n5} idempotents of every rank, and its failure "
      f"without idempotency: a non-idempotent matrix with trace {bad5[0]} and rank {bad5[1]}. That "
      f"is `trace_eq_finrank_range`, derived in Lean from the main lemma at f = id rather than "
      f"imported, which is a consistency check on the identity's orientation")

# ----------------------------------------------------------------- T6  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'IdempotentTrace.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
NAMES = ('apply_eq_self_of_mem_range', 'mapsTo_range', 'mapsTo_ker', 'isCompl_range_ker',
         'comp_eq_conj_prodMap', 'trace_restrict_range', 'trace_restrict_range_of_mapsTo',
         'trace_eq_finrank_range')
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
ok6 = ('import OIBridge.IdempotentTrace' in root
       and re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
       and re.search(r'(?m)^axiom ', body) is None
       and all(f'theorem {n}' in src for n in NAMES)
       and all(f'#print axioms {n}' in src for n in NAMES))
# it must be representation-free: no group, character or equivariance anywhere in the statements
for word in ('Representation', 'character', 'MonoidHom', 'Equivariant', 'invariants'):
    ok6 &= word not in body
# arbitrary field, not just C
ok6 &= '[Field K]' in src and 'ℂ' not in body
# the block structure must be proved WITHOUT finite-dimensionality: the instance is introduced late
i_var = src.index('variable [FiniteDimensional K V]')
ok6 &= src.index('theorem mapsTo_range') < i_var
ok6 &= src.index('theorem isCompl_range_ker') < i_var
ok6 &= src.index('theorem comp_eq_conj_prodMap') < i_var
ok6 &= src.index('theorem trace_restrict_range') > i_var
check("T6", ok6,
      f"the Lean file is IMPORTED BY OIBridge.lean, so CI builds it; it carries no `sorry` and no "
      f"`axiom`; all {len(NAMES)} named results print their axiom dependencies; nothing in the "
      f"statements mentions a group, a character, a representation or equivariance, so the lemma "
      f"is genuinely library infrastructure rather than a Theorem-7 workaround; it is over an "
      f"arbitrary field rather than ℂ; and the block structure is proved BEFORE the "
      f"finite-dimensionality instance is introduced, which is where it actually belongs")

print()
print('     [scope] Settled: the trace-of-restriction lemma is kernel-proved over an arbitrary')
print('     field — P idempotent and f commuting with P give tr(f|_im P) = tr(f.P) — together')
print('     with the block structure it rests on and the corollary tr P = dim(im P). The sharp')
print('     hypothesis is IMAGE-INVARIANCE, not commutativity: this layer could produce no')
print('     countercontrol for commuting, because there is none, and the Lean file carries the')
print('     weaker form as well. Idempotency IS load-bearing and breaks on an explicit witness.')
print('     NOT settled here: anything about [SM] Theorem 7. This file is the library dependency')
print('     that theorem was blocked on, and supplying it changes Theorem 7 from blocked to')
print('     active. The six-link representation, its decomposition into T1 + E + A1 under the')
print('     24-element ROTATIONAL cubic group O — not the 48-element O_h of Corollary 1a — and')
print('     the H-link transport to the physical carrier are all still to do.')
print()
print("idempotent_trace_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)

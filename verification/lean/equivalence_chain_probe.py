#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/EquivalenceChain.lean — b448's Tier-1 closures.

Three statements from [Main] §2.3 and §3.2 are kernel-proved there; this file is the INDEPENDENT
executable layer that b447 made standard. It re-derives each by computation rather than by proof
and adds the countercontrols that say which hypothesis is load-bearing. PROBED IS NOT FORMALLY
PROVED and the implication runs both ways: a kernel proof of a mis-transcribed statement is still a
kernel proof of the wrong thing, and only an independent computation catches that.

E1 STOCHASTIC INVERSE, exhaustively on a rational grid: no row-stochastic matrix at n = 2 or 3 has
   a stochastic inverse without being a permutation. Every permutation matrix does have one, so the
   statement is not vacuous.
E2 COUNTERCONTROL for E1: "stochastic" on the INVERSE is load-bearing, not decorative. A stochastic
   matrix can be invertible without being a permutation -- its inverse then fails to be stochastic,
   which is exactly what the lemma turns on.
E3 PERMUTATION UNITARITY, exactly in integer arithmetic on a product index set V x H, together
   with the fact that the inverse permutation's matrix IS the conjugate transpose.
E4 DIAGONAL PRESERVATION, exactly in rational arithmetic: Phi_t maps diagonal states to diagonal
   states for random bijections and horizons, with the hidden prior a probability vector.
E5 COUNTERCONTROL for E4: a NON-permutation unitary breaks it. Conjugating a diagonal state by a
   Hadamard produces off-diagonal weight that survives the partial trace, so diagonal preservation
   is a property of the permutation-dilation family and not of unitary dilations in general.
E6 Lint: the Lean file is imported by the gated bridge root, carries no sorry/admit/native_decide,
   states the theorems the coverage ledger attributes to it, and prints their axioms.

Usage:  python3 equivalence_chain_probe.py
"""
import itertools
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
rng = random.Random(448)


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), F(0)) for j in range(n)] for i in range(n)]


def is_identity(M):
    return all(M[i][j] == (1 if i == j else 0) for i in range(len(M)) for j in range(len(M)))


def is_perm(M):
    n = len(M)
    return (all(M[i][j] in (0, 1) for i in range(n) for j in range(n))
            and all(sum(M[i]) == 1 for i in range(n))
            and all(sum(M[i][j] for i in range(n)) == 1 for j in range(n)))


def stochastic_rows(n, grid):
    """Every row of n entries drawn from `grid` that sums to 1."""
    return [r for r in itertools.product(grid, repeat=n) if sum(r) == 1]


# ---------------------------------------------------------------- E1  stochastic inverse
GRID = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]


def inverse(M):
    """Exact rational inverse by Gauss-Jordan, or None if singular. Enumerating A and inverting it
    is exhaustive where enumerating PAIRS (A, B) would be redundant as well as slower: A * B = I
    pins B to A's inverse, so the grid on B never has to be searched at all."""
    n = len(M)
    aug = [list(M[i]) + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next((r for r in range(c, n) if aug[r][c] != 0), None)
        if piv is None:
            return None
        aug[c], aug[piv] = aug[piv], aug[c]
        pv = aug[c][c]
        aug[c] = [x / pv for x in aug[c]]
        for r in range(n):
            if r != c and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[c])]
    return [row[n:] for row in aug]


def is_stochastic(M):
    return all(x >= 0 for r in M for x in r) and all(sum(r, F(0)) == 1 for r in M)


bad = []
tested = 0
for n in (2, 3):
    rows = stochastic_rows(n, GRID)
    for m in itertools.product(rows, repeat=n):
        A = [list(r) for r in m]
        tested += 1
        Ai = inverse(A)
        if Ai is not None and is_stochastic(Ai) and not is_perm(A):
            bad.append((n, A, Ai))
perms_ok = True
for n in (2, 3):
    for sigma in itertools.permutations(range(n)):
        P = [[F(1) if sigma[i] == j else F(0) for j in range(n)] for i in range(n)]
        Q = [[F(1) if sigma[j] == i else F(0) for j in range(n)] for i in range(n)]
        perms_ok &= is_identity(matmul(P, Q)) and is_perm(Q)
check("E1", not bad and perms_ok,
      f"STOCHASTIC INVERSE, exhaustively rather than sampled. Over every row-stochastic matrix "
      f"with entries in {{0, 1/4, 1/2, 3/4, 1}} at n = 2 and n = 3 — {tested} matrices, each "
      f"inverted exactly over the rationals — NONE has a stochastic inverse without being a "
      f"permutation. Inverting A is exhaustive where searching pairs would be redundant: A * B = I "
      f"pins B to A's inverse, so the grid on B never has to be searched. And the statement is not "
      f"vacuous: every permutation matrix has a stochastic inverse, namely its transpose")


# ---------------------------------------------------------------- E2  countercontrol
A = [[F(1, 2), F(1, 2)], [F(0), F(1)]]
Ainv = [[F(2), F(-1)], [F(0), F(1)]]
A_stoch = all(x >= 0 for r in A for x in r) and all(sum(r) == 1 for r in A)
inv_ok = is_identity(matmul(A, Ainv))
inv_stoch = all(x >= 0 for r in Ainv for x in r)
check("E2", A_stoch and inv_ok and not inv_stoch and not is_perm(A),
      "COUNTERCONTROL — `stochastic` ON THE INVERSE IS LOAD-BEARING. [[1/2, 1/2], [0, 1]] is "
      "row-stochastic and invertible and is NOT a permutation; its inverse [[2, -1], [0, 1]] is a "
      "genuine two-sided inverse and is not stochastic. So the lemma is not "
      "`stochastic + invertible => permutation`, and a formalization that dropped the hypothesis "
      "would be proving something false")

# ---------------------------------------------------------------- E3  permutation unitarity
nV, nH = 3, 2
idx = [(v, h) for v in range(nV) for h in range(nH)]
pos = {p: k for k, p in enumerate(idx)}
N = len(idx)
u_ok = True
for _ in range(30):
    perm = idx[:]
    rng.shuffle(perm)
    phi = {p: perm[k] for k, p in enumerate(idx)}
    U = [[1 if phi[idx[i]] == idx[j] else 0 for j in range(N)] for i in range(N)]
    Ud = [[U[j][i] for j in range(N)] for i in range(N)]          # real, so dagger = transpose
    inv = {v: k for k, v in phi.items()}
    Uinv = [[1 if inv[idx[i]] == idx[j] else 0 for j in range(N)] for i in range(N)]
    u_ok &= is_identity(matmul([[F(x) for x in r] for r in U], [[F(x) for x in r] for r in Ud]))
    u_ok &= is_identity(matmul([[F(x) for x in r] for r in Ud], [[F(x) for x in r] for r in U]))
    u_ok &= (Ud == Uinv)
check("E3", u_ok,
      f"PERMUTATION UNITARITY, exact in integer arithmetic on the PRODUCT index set. For 30 random "
      f"bijections of a {nV} x {nH} configuration space, U Uᴴ = UᴴU = I, and the conjugate "
      f"transpose IS the permutation matrix of the inverse bijection — which is the step the "
      f"diagonal-preservation proof reuses rather than recomputes")

# ---------------------------------------------------------------- E4  diagonal preservation
def phi_pow(phi, t):
    out = {p: p for p in idx}
    for _ in range(t):
        out = {p: phi[out[p]] for p in idx}
    return out


d_ok = True
for _ in range(20):
    perm = idx[:]
    rng.shuffle(perm)
    phi = {p: perm[k] for k, p in enumerate(idx)}
    w = [F(rng.randint(1, 5)) for _ in range(nH)]
    tot = sum(w, F(0))
    mu = [x / tot for x in w]                                    # a probability vector
    r = [F(rng.randint(1, 5)) for _ in range(nV)]
    tr = sum(r, F(0))
    rho = [x / tr for x in r]                                    # a diagonal visible state
    for t in range(1, 5):
        pt = phi_pow(phi, t)
        # Phi_t(rho)_ij = sum_h (rho (x) mu)(pt(i,h)) (pt(j,h)), conjugation being a relabelling
        for i in range(nV):
            for j in range(nV):
                if i == j:
                    continue
                s = F(0)
                for h in range(nH):
                    a, b = pt[(i, h)], pt[(j, h)]
                    s += (rho[a[0]] if a[0] == b[0] else F(0)) * (mu[a[1]] if a[1] == b[1] else F(0))
                d_ok &= (s == 0)
check("E4", d_ok,
      f"DIAGONAL PRESERVATION, exact in rational arithmetic. For 20 random bijections of the "
      f"{nV} x {nH} space, horizons t = 1..4, a random diagonal visible state and a random "
      f"probability vector as the hidden prior, every off-diagonal entry of "
      f"Φ_t(ρ) = Tr_H[U^t (ρ ⊗ μ_H) U^{{-t}}] is exactly zero")

# ---------------------------------------------------------------- E5  countercontrol
# One qubit of visible space, one hidden state, and a Hadamard instead of a permutation. Amplitudes
# are kept as exact multiples of 1/2 so no floating point enters.
H2 = [[F(1, 2), F(1, 2)], [F(1, 2), F(-1, 2)]]                   # (1/sqrt2) H, squared entries
rho_diag = [[F(1), F(0)], [F(0), F(0)]]                          # |0><0|
# H rho H^dagger, with the 1/sqrt2 factors combining to 1/2 exactly
conj = [[sum(sum(H2[i][k] * rho_diag[k][l] * H2[j][l] for l in range(2)) for k in range(2))
         for j in range(2)] for i in range(2)]
off = conj[0][1]
check("E5", off != 0,
      f"COUNTERCONTROL — DIAGONAL PRESERVATION IS A PROPERTY OF THE PERMUTATION-DILATION FAMILY "
      f"AND NOT OF UNITARY DILATIONS. Conjugating |0><0| by a Hadamard gives off-diagonal entry "
      f"{off}, exactly nonzero. The manuscript's own scope remark says the same thing from the "
      f"other side: for a general CPTP family the CP-indivisibility reduction FAILS, and it is "
      f"membership in the diagonal-preserving class that licenses the theorem")

# ---------------------------------------------------------------- E6  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'EquivalenceChain.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
code = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
THMS = ('isPermMatrix_of_stochastic_inverse', 'permMatrix_mem_unitaryGroup', 'isDiag_Phi')
ok6 = ('import OIBridge.EquivalenceChain' in root
       and re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', code) is None
       and 'admit' not in code and 'native_decide' not in code
       and all(f'theorem {t}' in src for t in THMS)
       and all(f'#print axioms {t}' in src for t in THMS)
       and 'variable {n : Type*} [Fintype n] [DecidableEq n]' in src)
check("E6", ok6,
      f"the Lean file is IMPORTED BY OIBridge.lean — the bridge library's root, so CI actually "
      f"builds it and the theorems are gated rather than merely present — carries no sorry, admit "
      f"or native_decide, states all {len(THMS)} theorems the coverage ledger attributes to it, "
      f"prints their axiom dependencies at build time, and quantifies over an arbitrary finite "
      f"index type rather than a fixed dimension")

print()
print('     [scope] Settled: three statements of the central equivalence chain are now kernel-')
print('     proved as the manuscript states them. THE STOCHASTIC-INVERSE LEMMA (Main §2.3): a')
print('     finite square stochastic matrix with a stochastic one-sided inverse is a permutation')
print('     matrix. PERMUTATION UNITARITY (Main §3.2): any bijection of C_V x C_H gives a unitary')
print('     on the product. DIAGONAL PRESERVATION (Main §3.2): the permutation-dilation channels')
print('     map computational-diagonal states to computational-diagonal states.')
print('     The hypotheses are load-bearing and the countercontrols say so: a stochastic matrix')
print('     can be invertible without being a permutation, and a NON-permutation unitary destroys')
print('     diagonality outright.')
print('     NOT settled here: the CP-indivisibility theorem that consumes diagonal preservation is')
print('     still level P, and so is the one-step ancilla dilation. The S <=> D <=> Q equivalence')
print('     itself is NOT declared covered merely because several of its legs now are — the final')
print('     theorem has to exist in Lean with the manuscript hypotheses and conclusion before the')
print('     ledger may record it, which is the empty-delta rule applied to the centrepiece.')
print()
print("equivalence_chain_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)

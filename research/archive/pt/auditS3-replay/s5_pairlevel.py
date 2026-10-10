#!/usr/bin/env python3
"""S3 node S3.2(b) -- what pair-level self-duality can and cannot pin down: exact ingredients.

Run: python3 -I -B s5_pairlevel.py

Questions: is every ipW-self-dual, admissible, cnot-invariant pair cone equal to Q3? This script does not settle it.
It checks the exact ingredients of three partial results stated in RESULT.md:
  (a) no ipW-self-dual cone linearly isomorphic to a Lorentz (spin-factor) cone contains SEP;
  (b) an ipW-orthogonal map Psi with SEP <= Psi(Q3) fixes the unit table and sends pure products to rank-one states;
  (c) the seed of an existence argument: C = cone(K_gen u {E0}) is cnot-invariant and pairwise nonnegative.

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. One PASS/FAIL line per check; kinds as in s1-s4. R2. VERDICT only if all pass; else
  'S5-PAIRLEVEL: FAILED -- <ids>' and exit 1. R3. Exact arithmetic; no floating point, randomness or timing.
"""
import sys
from itertools import product

import sympy as sp

Q = sp.Rational
iu = sp.I
R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def note(cid, text):
    print(f"NOTE [written] {cid}  -- {text}", flush=True)


def section(t):
    print()
    print(f"== {t}", flush=True)


def ex(v):
    return sp.expand(v)


def zero(v):
    return ex(v) == 0


def mzero(M):
    return all(ex(v) == 0 for v in M)


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in NEG else 1) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * sp.kronecker_product(S[m], S[n])
    return out / 4


def rho1(x):
    return (S[0] + sum((x[i] * S[i + 1] for i in range(3)), sp.zeros(2, 2))) / 2


E00 = sp.zeros(4, 4)
E00[0, 0] = 1
AX = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
PRODS = [prodState(a, b) for a, b in product(AX, AX)]

# ================================================================================================================
section('S1  averaging and norms of pure products (exact design)')
chk('A1', 'each of the 36 axis products p = prodState a b (a, b unit) has ipW p p = 4',
    all(ipW(p, p) == 4 for p in PRODS), 'enumerate')
chk('A2', 'the average of the 36 axis products is the unit table E00', sum(PRODS, sp.zeros(4, 4)) / 36 == E00,
    'enumerate')
w = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'w{m}{n}', real=True))
chk('A3', 'ipW w w = 4 tr(pauliW(w)^2), symbolic (for w_00 = 1: ipW w w = 4 * purity, <= 4 with equality iff rank one)',
    zero(ipW(w, w) - 4 * (pauliW(w) * pauliW(w)).trace()), 'identity')
chk('A2c', 'countercontrol: the aperture is load-bearing -- every axis product satisfies <E00, p>^2 >= |p|^2/4 (the '
    '60-degree cone about E00 contains SEP) but violates <E00, p>^2 >= |p|^2/2 (the self-dual 45-degree cone)',
    all(ipW(E00, p) ** 2 >= ipW(p, p) / 4 and ipW(E00, p) ** 2 < ipW(p, p) / 2 for p in PRODS), 'countercontrol')
Dp = (PRODS[0] + E00) / 2
chk('A3c', 'countercontrol: the non-isometric map D(w) = (w + w_00 E00)/2 keeps D(p)_00 = 1 but ipW D(p) D(p) = 7/4 < 4 '
    'for an axis product: without orthogonality the purity conclusion of (b) fails',
    Dp[0, 0] == 1 and ipW(Dp, Dp) == Q(7, 4), 'countercontrol')
x = [sp.Symbol(f'x{i}', real=True) for i in range(3)]
chk('A4', 'rho(x)^2 - rho(x) = ((|x|^2 - 1)/4) I, symbolic: rho(x) is a rank-one projector exactly for unit x',
    mzero(rho1(x) * rho1(x) - rho1(x) - (x[0] ** 2 + x[1] ** 2 + x[2] ** 2 - 1) / 4 * sp.eye(2)), 'identity')
note('LOR.W', '(a) Lorentz cones. Let K = Lam(L16) with L16 the standard Lorentz cone of R^16 and Lam linear, and '
     'suppose K = dualW K. Then Lam^T Lam is a symmetric positive definite automorphism of L16, hence a positive '
     'multiple of a Lorentz boost (standard: Aut(L16) = R_+ x O(1,15), and its symmetric positive definite elements '
     'are scaled boosts), so K = O(L16) for an ipW-orthogonal O: K = {v : <u, v> >= |v| / sqrt 2} for a unit axis '
     'u. If K contained SEP it would contain the 36 axis products p, each with |p| = 2 (A1), so <u, p> >= sqrt 2; '
     'averaging (A2) gives <u, E00> >= sqrt 2 > 1 >= <u, E00> (Cauchy-Schwarz): contradiction. So no ipW-self-dual '
     'cone isomorphic to a Lorentz cone contains SEP. [W + X]')
note('ORTH.W', '(b) orthogonal images of Q3. Let Psi be ipW-orthogonal with SEP <= Psi(Q3). For a pure product p, '
     'Psi^-1(p) lies in Q3 with |Psi^-1 p| = 2 (A1); writing t = (Psi^-1 p)_00, A3 gives 4 t^2 >= |Psi^-1 p|^2 = 4, so '
     't >= 1, i.e. <Psi(E00), p> >= 1 for all 36 axis products; averaging (A2) gives <Psi(E00), E00> >= 1 = '
     '|Psi(E00)||E00|, so Psi(E00) = E00, every t = 1, and by A3 every Psi^-1(p) is a rank-one state. So Psi^-1 maps '
     'pure products (A4: rank-one product projectors) to pure states. Whether every such linear bijection is '
     'Ad(U) or Ad(U) composed with a partial transpose (which would leave only Q3 and twin) is a Wigner-type '
     'classification [L, unverified]; it is not checked here. [W + X, with an L step]')

# ================================================================================================================
section('S2  the seed of the (unproved) existence argument for other self-dual cnot-invariant cones')
E0 = sp.zeros(4, 4)
E0[0, 0], E0[1, 3], E0[2, 2] = 1, 1, -1
chk('B1', 'E0 is cnot-invariant and ipW E0 E0 = 3 >= 0', cnot(E0) == E0 and ipW(E0, E0) == 3, 'witness')
psi = sp.Matrix([1, -1, -1, -1]) / 2
G = sp.Matrix(4, 4, lambda m, n: ex((sp.kronecker_product(S[m], S[n]) * psi * psi.T).trace()))
chk('B2', 'E0 is not in Q3: ipW E0 G = -1 with pauliW G = psi psi^T', ipW(E0, G) == -1
    and mzero(pauliW(G) - psi * psi.T), 'witness')
note('BF.W', 'C := cone(K_gen u {E0}) is cnot-invariant and pairwise nonnegative (E0 in dualW K_gen, s2 G1-G3; '
     'K_gen <= dualW K_gen, s2 D.W; B1). A cnot-equivariant form of the Barker-Foran extension theorem would give a '
     'cnot-invariant self-dual cone K with C <= K <= dualW C; such a K contains SEP, lies in maxCone, is closed and '
     'cnot-invariant, and differs from Q3 (E0 in K, B2), so FCC would fail for uniform K (theorem [D] and '
     'classification [W + L]). The equivariant extension is [L, unverified]: the non-equivariant theorem adds one '
     'vector at a time, and the symmetrized step can stall when the added vector and its cnot image have zero '
     'overlap. No exact exotic self-dual cone is exhibited here, and no label rests on this note.')

# ================================================================================================================
print()
failed = [c[0] for c in CHECKS if not c[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'witness', 'enumerate', 'countercontrol')), flush=True)
if failed:
    print(f"S5-PAIRLEVEL: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT S5-PAIRLEVEL-EXACT -- {len(CHECKS)} checks', flush=True)

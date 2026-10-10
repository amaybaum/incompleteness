#!/usr/bin/env python3
"""EQ-D, node N3(b): what composites of face systems buy without a transformation clause.

Setting: a capacity-3 system T with full kinematics on T (x) T (every state, every effect, standard tensor product),
sequential and parallel composition, identity wires and classical feed-forward -- and NO operation acting on T other
than wires, preparations and effects.  Checked exactly:

  (1) gate teleportation: with resource (1 (x) U)|Phi>/sqrt3 on (A,B) and the Bell effects |Phi_ab><Phi_ab| on (I,A),
      the branch Kraus operators I -> B are K_ab = (1/3) U V_ab with V_ab unitary, K_00 = (1/3) U, and
      sum_ab K_ab^dag K_ab = 1.  So every branch is (1/9) conj(unitary), known from the outcome, for every input.
  (2) repeat-until-success: each round succeeds with probability exactly 1/9 whatever the input and the known
      correction; after N rounds the success weight is 1 - (8/9)^N (exact rational), so the deterministic channel
      Phi_N satisfies ||Phi_N - conj(U)||_diamond <= 2 (8/9)^N.
U is taken as the swap P01 and as a non-monomial Gaussian-rational unitary (Cayley transform).  The qutrit Weyl
operators use omega = -1/2 + i sqrt(3)/2 exactly.
Not decided here (named wall): whether some finite protocol of this kind gives conj(U) EXACTLY and deterministically
(generalized port-based teleportation with sender measurements on unselected ports).
"""
import sys
from fractions import Fraction

import sympy as sp

I = sp.I
FAILS = []


def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        FAILS.append(name)


def zero(M):
    return all(sp.simplify(sp.expand(v)) == 0 for v in M)


d = 3
w = sp.Rational(-1, 2) + I * sp.sqrt(3) / 2
check('omega is a primitive cube root of unity (exact)', sp.expand(w**3) == 1 and sp.expand(1 + w + w**2) == 0)
Xs = sp.Matrix(d, d, lambda i, j: 1 if i == (j + 1) % d else 0)
Zs = sp.diag(*[w**j for j in range(d)])


def W(a, b):
    return Xs**a * Zs**b


def ket(n, i):
    v = sp.zeros(n, 1)
    v[i] = 1
    return v


Phi = sum((sp.Matrix(sp.kronecker_product(ket(d, j), ket(d, j))) for j in range(d)), sp.zeros(d * d, 1))


def branch_kraus(U):
    """K_ab : I -> B,  K_ab |x> = (<Phi_ab|_{IA} (x) 1_B) (|x>_I (x) |psi_U>_{AB})."""
    psi = sp.Matrix(sp.kronecker_product(sp.eye(d), U)) * Phi / sp.sqrt(3)
    out = {}
    for a in range(d):
        for b in range(d):
            bell = sp.Matrix(sp.kronecker_product(W(a, b), sp.eye(d))) * Phi / sp.sqrt(3)
            K = sp.zeros(d, d)
            for x in range(d):
                state = sp.Matrix(sp.kronecker_product(ket(d, x), psi))      # order I, A, B
                for bo in range(d):
                    amp = 0
                    for i in range(d):
                        for aa in range(d):
                            amp += sp.conjugate(bell[i * d + aa]) * state[(i * d + aa) * d + bo]
                    K[bo, x] = sp.expand(amp)
            out[(a, b)] = K
    return out


def cayley(S):
    n = S.shape[0]
    return (sp.eye(n) - S) * (sp.eye(n) + S).inv()


P01 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
S = sp.Matrix([[I, 1 + I, 0], [-1 + I, 0, sp.Rational(1, 2)], [0, -sp.Rational(1, 2), 2 * I]])
check('S is skew-Hermitian (so its Cayley transform is unitary)', zero(S.H + S))
Uc = sp.simplify(cayley(S))
check('Cayley unitary Uc: Uc^dag Uc = 1 exactly; Uc is not monomial',
      zero(Uc.H * Uc - sp.eye(d)) and sum(1 for v in Uc.row(0) if sp.simplify(v) != 0) > 1)

for name, U in (('swap P01', P01), ('Cayley Uc', Uc)):
    Ks = branch_kraus(U)
    check(f'(1) [{name}] sum_ab K_ab^dag K_ab = 1 (an instrument on the input)',
          zero(sum((K.H * K for K in Ks.values()), sp.zeros(d, d)) - sp.eye(d)))
    check(f'(1) [{name}] K_00 = U/3 exactly', zero(Ks[(0, 0)] - U / 3))
    ok = True
    for (a, b), K in Ks.items():
        V = 3 * U.H * K                       # K = (1/3) U V
        ok &= zero(V.H * V - sp.eye(d))
    check(f'(1) [{name}] every branch is (1/3) U V_ab with V_ab unitary (branch map = (1/9) conj(U V_ab))', ok)

# (2) repeat-until-success weights, exact
p = Fraction(1, 9)
for N in (1, 2, 5, 10, 40):
    succ = sum(p * (1 - p) ** (r - 1) for r in range(1, N + 1))
    check(f'(2) RUS: success weight after {N} rounds = 1 - (8/9)^{N} exactly', succ == 1 - Fraction(8, 9) ** N)
check('(2) RUS never reaches weight 1 at finite N ((8/9)^N > 0)', all(Fraction(8, 9) ** N > 0 for N in range(1, 200)))
print()
if FAILS:
    print('VERDICT  VOID — failed:', FAILS)
    sys.exit(1)
print('VERDICT  with full kinematics on T(x)T and no operation acting on T, every unitary on T is available as an exact '
      'probabilistic branch (weight 1/9) and deterministically within 2(8/9)^N; exact deterministic availability is not '
      'decided by this computation')

"""Thread SS, probe P3 -- the homogenized split of the 'X-type' NOT on two-level systems over each field.

Read-only research against base 68b6df0651f14b2c8ab082635b8d2051918617a2. Exact arithmetic only.

A two-level system over F (dim_R F = k; k = 0 stands for the classical bit, the diagonal algebra) has the
real space H_2(F) = {[[a, q], [conj q, b]]} of dimension 2 + k, which is the homogenized space HVec d of the
ball of dimension d = 1 + k (spin-factor shape). The NOT exchanging the two levels acts by
(a, b, q) -> (b, a, conj q). DIM-1's parity step (CompositeDimension.lean:682) requires the +1 and -1
eigenspaces of the homogenized NOT to have equal dimension; DIM-1's block step requires the tangent +1
dimension p_tan <= 1. This probe computes the split of this particular NOT for k = 0, 1, 2, 4, 8.
It concerns one NOT per field (the level exchange); DIM-1's IsNot admits every linear involution, and
the d-generic bookkeeping over all involutions is p1 section F.

Run (from scratchpad/ss):  python3 -I p3_field_splits.py
"""
import sympy as sp
from sympy import zeros, eye

CHECKS = []


def check(name, cond):
    cond = bool(cond)
    CHECKS.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


rows = {}
for k, name in [(0, "classical bit"), (1, "R (rebit)"), (2, "C (qubit)"), (4, "H (quaternionic bit)"),
                (8, "O (octonionic bit)")]:
    n = 2 + k                      # coordinates (a, b, q_0..q_{k-1}); q_0 the real part
    M = zeros(n, n)
    M[0, 1], M[1, 0] = 1, 1        # a <-> b
    for j in range(k):
        M[2 + j, 2 + j] = 1 if j == 0 else -1     # conjugation: real part fixed, imaginary parts negated
    plus = len((M - eye(n)).nullspace())
    minus = len((M + eye(n)).nullspace())
    d = 1 + k
    ptan = plus - 1
    rows[k] = (d, plus, minus, ptan)
    print("F=%-22s d=%d homogenized split (+1, -1) = (%d, %d), p_tan = %d, balanced %s, block p_tan<=1 %s"
          % (name, d, plus, minus, ptan, plus == minus, ptan <= 1))
    check("P3 %s: M involutive" % name, M * M == eye(n))
check("P3a the level-exchange NOT is balanced exactly for the classical bit and C",
      [k for k in rows if rows[k][1] == rows[k][2]] == [0, 2])
check("P3b the balanced cases are d = 1 and d = 3, DIM-1's output set",
      sorted(rows[k][0] for k in rows if rows[k][1] == rows[k][2] and rows[k][3] <= 1) == [1, 3])

fails = [nm for nm, c in CHECKS if not c]
print("SUMMARY %d checks, %d failed" % (len(CHECKS), len(fails)))
print("VERDICT " + ("RENDERED: for the level-exchange NOT, DIM-1's parity balance holds exactly over the "
                    "classical bit and C" if not fails else "NOT RENDERED (a control failed)"))

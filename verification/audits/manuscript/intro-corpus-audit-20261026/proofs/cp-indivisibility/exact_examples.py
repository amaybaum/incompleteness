"""Exact checks of the named examples (rational arithmetic throughout).

X1  Main.md:330 remark: Phi_t1 = Ad_H, Phi_t2 = id.
    Ad_H is rational as a superoperator (entries of H E_ab H are +-1/2), so everything is in Q.
X2  Converse failure INSIDE the class: phi(v,h) = (v, h xor v) (CNOT, control V), any
    diagonal prior: T(1) = T(2) = I (P-divisible), Phi_1 = complete dephasing, Phi_2 = id,
    so no linear (a fortiori no CPTP) Lambda with Lambda.Phi_1 = Phi_2.
X3  Intro Appendix B card game: swap with uniform burn card: Phi_1 = tr(.) I/2, Phi_2 = id.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import cp_search as c
from exact_lp import stochastic_divisor

half = F(1, 2)


def compose(A, B):  # superoperators as matrices: (A.B)
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def eye(d):
    return [[F(int(i == j)) for j in range(d)] for i in range(d)]


def choi(S, n):
    """J[(a,c),(b,d)] = <c|Lambda(|a><b|)|d>."""
    d2 = n * n
    J = [[F(0)] * d2 for _ in range(d2)]
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for d in range(n):
                    J[a * n + cc][b * n + d] = S[cc * n + d][a * n + b]
    return J


def is_psd_exact(J):
    """Exact PSD test via LDL^T with rational pivots (symmetric real J)."""
    n = len(J)
    A = [row[:] for row in J]
    for k in range(n):
        if A[k][k] < 0:
            return False
        if A[k][k] == 0:
            if any(A[k][j] != 0 for j in range(k + 1, n)):
                return False
            continue
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= f * A[k][j]
    return True


# ---------------- X1: Hadamard pair
H = [[1, 1], [1, -1]]  # times 1/sqrt2; H E_ab H^T carries the factor 1/2 exactly
n = 2
AdH = [[F(0)] * 4 for _ in range(4)]
for a in range(2):
    for b in range(2):
        for cc in range(2):
            for d in range(2):
                AdH[cc * 2 + d][a * 2 + b] = half * H[cc][a] * H[d][b]
assert compose(AdH, AdH) == eye(4), "Ad_H o Ad_H != id"
J = choi(AdH, 2)
assert is_psd_exact(J), "Ad_H not CP"
# TP: sum_c <c|Lambda(|a><b|)|c> = delta_ab
assert all(sum(AdH[cc * 2 + cc][a * 2 + b] for cc in range(2)) == int(a == b) for a in range(2) for b in range(2))
T1 = c.pops(AdH, 2); T2 = c.pops(eye(4), 2)
assert T1 == [[half, half], [half, half]] and T2 == [[1, 0], [0, 1]]
ok, cert = stochastic_divisor(T1, T2)
assert not ok and c.lift_certificate(T1, T2, cert, 2) is True
dp, cov = c.diag_checks(AdH, 2)
assert not dp, "Ad_H should NOT preserve diagonals"
print("X1  Ad_H.Ad_H = id, Ad_H CPTP (exact Choi PSD, TP): pair CP-divisible with Lambda = Ad_H")
print("    T(t1) = J/2, T(t2) = I: no stochastic divisor (exact Farkas):", [str(v) for v in cert])
print("    Ad_H maps |0><0| to a non-diagonal state: outside the diagonal-preserving class")
print("    whole family {id, Ad_H, id} at t = 0,1,2: CP-divisible for every pair (0,t) trivially,")
print("    (1,2) by Ad_H; populations P-indivisible at (1,2).  Remark verified exactly.")

# ---------------- X2: CNOT dilation, converse failure inside the class
nV, nH = 2, 2
perm = [0] * 4
for v in range(2):
    for h in range(2):
        perm[v * nH + h] = v * nH + (h ^ v)
for mu in [(half, half), (F(1, 3), F(2, 3)), (F(1), F(0))]:
    S1 = c.superop(c.perm_power(perm, 1), nV, nH, mu)
    S2 = c.superop(c.perm_power(perm, 2), nV, nH, mu)
    deph = [[F(0)] * 4 for _ in range(4)]
    deph[0][0] = deph[3][3] = F(1)
    assert S1 == deph and S2 == eye(4)
    assert c.pops(S1, 2) == c.pops(S2, 2) == [[1, 0], [0, 1]]
    assert stochastic_divisor(c.pops(S1, 2), c.pops(S2, 2))[0]
    assert not c.lin_compatible(S1, S2)   # Phi_1(|0><1|) = 0 but Phi_2(|0><1|) != 0
print("X2  CNOT dilation, priors (1/2,1/2),(1/3,2/3),(1,0): Phi_1 = dephasing, Phi_2 = id,")
print("    T(1) = T(2) = I (P-divisible) yet no linear Lambda: CP-indivisible.  Converse fails")
print("    inside the permutation-dilation class.")

# ---------------- X3: card game (swap, uniform burn card)
perm = [0] * 4
for v in range(2):
    for h in range(2):
        perm[v * nH + h] = h * nH + v
mu = (half, half)
S1 = c.superop(c.perm_power(perm, 1), nV, nH, mu)
S2 = c.superop(c.perm_power(perm, 2), nV, nH, mu)
const = [[F(0)] * 4 for _ in range(4)]
for a in range(2):
    const[0][a * 2 + a] = half
    const[3][a * 2 + a] = half
assert S1 == const and S2 == eye(4)
T1, T2 = c.pops(S1, 2), c.pops(S2, 2)
ok, cert = stochastic_divisor(T1, T2)
assert not ok and c.lift_certificate(T1, T2, cert, 2)
assert not c.lin_compatible(S1, S2)
print("X3  card game: Phi_1 = tr(.) I/2, Phi_2 = id; populations P-indivisible (exact Farkas),")
print("    CP-indivisible (exact, both by the theorem's lift and by linear incompatibility).")
print("ALL EXACT CHECKS PASS")

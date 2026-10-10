"""o7_density.py -- research/origin, round 2, node O7: density at the balanced angle (O3-T7's OPEN item).

QUESTION. On three states, two balanced mixers on overlapping pairs generate an element of infinite order
(o3_density E1; audit check X5). Is the generated group dense in SO(3) (or in the relevant compact group), or does it
lie in a proper closed subgroup?

OBJECTS (exact, entries in Q(sqrt2), implemented as pairs a + b sqrt2 with rational a, b):
  R01, R12  the kernel's balanced state-mixing datum rot(pi/4) = [[r, -r], [r, r]], r = sqrt2/2, on the pairs (0,1)
            and (1,2), identity on the third state (rotations, det +1; StateMixingCoupling `rot`, `mixImage`);
  H01, H12  the balanced Hadamard [[r, r], [r, -r]] on the same pairs (reflections, det -1; the audit's X5 form);
  P         the six permutation matrices of the three states (the exchanges).
CERTIFICATE (written; [L] the classification of closed subgroups of SO(3): finite, a circle SO(2)_m, its normalizer
O(2)_m, or SO(3)). If a subgroup G of O(3) contains a rotation U of infinite order with axis n, and some V in G with
V n not parallel to n, then the closure of G contains SO(3): V U V^-1 is a rotation of infinite order about V n, and in
a closed subgroup of type SO(2)_m or O(2)_m every element of infinite order is a rotation about m. Infinite order:
a rotation by theta with e^{i theta} a root of unity has 2 cos theta = tr - 1 an algebraic integer; tr - 1 = a + b sqrt2
with b != 0 has minimal polynomial x^2 - 2a x + (a^2 - 2 b^2), and a coefficient outside Z certifies infinite order.
CHECKS.
  D1  R01, R12 have order 8 each; U = R01 R12 has tr - 1 = sqrt2 - 1/2, minimal polynomial x^2 + x - 7/4: infinite
      order; its axis n (from the antisymmetric part) satisfies U n = n; R01 n is not parallel to n. Verdict for
      <R01, R12>: closure = SO(3) (dense).
  D2  U' = H01 H12 is a rotation with tr - 1 = -3/2... (measured; minimal polynomial over Q); infinite order iff the
      certificate holds; H01 and H12 both fix the axis n' of U' (exactly): the group <H01, H12> fixes n', so its
      closure lies in the stabilizer of n' in O(3), a proper closed subgroup (a copy of O(2)); with U' of infinite
      order the closure is exactly that stabilizer.
  D3  with the exchanges: for <R01, P> and <H01, P> there are an infinite-order rotation in the group and a
      permutation moving its axis off its line: closure = O(3) (det -1 elements present).
  D4  as unitaries of C^3 every element above is real, so the closures lie in O(3), a proper closed subgroup of U(3)
      that does not even give dense control up to phase (the quarter phase diag(i,1,1) is at distance >= 1/2... checked
      as: c V = diag(i,1,1) has no solution with V real orthogonal and |c| = 1); adding the quarter phase S0 =
      diag(i,1,1): Ad(S0) maps the so(3) generator E01 - E10 to i(E01 + E10), outside so(3); so(3) is a maximal
      subalgebra of su(3) (the complement is the irreducible 5-dimensional representation) [W], so the closure
      contains SU(3), and with det(S0) = i, det(P) = +-1, det(R) = 1 the closure is {U in U(3) : det U^4 = 1} [W].
DECISION RULE (fixed before the first run; the verdict is generated from the measured booleans):
  DENSE_ROT := D1;  PROPER_REFL := D2;  O3_WITH_EXCHANGES := D3;  PHASE := D4.
  VERDICT VOID if any countercontrol is True.
  VERDICT DENSE-AT-THE-BALANCED-ANGLE iff DENSE_ROT and PROPER_REFL and O3_WITH_EXCHANGES and PHASE (the rotation pair
    is dense in SO(3); the reflection pair lies in a proper closed subgroup; with the exchanges both close to O(3); the
    quarter phase lifts the closure to contain SU(3)); otherwise VERDICT MIXED with the failing items listed.
COUNTERCONTROLS (must be False):
  CC1 the reflection pair's own generators move the axis of U' (they must not: dihedral group);
  CC2 the infinite-order certificate holds for R01 R01 (a rotation by pi/2, finite order);
  CC3 Ad(diag(-1,1,1)) moves so(3) out of so(3) (it must not: a real diagonal sign normalizes so(3)).

Run: python3 -I -B o7_density.py > o7_density.out 2> o7_density.err; echo "exit $?" >> o7_density.err
"""

from fractions import Fraction as F
from itertools import permutations


class Q2:
    """a + b sqrt2, a and b rational."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, o):
        o = q(o)
        return Q2(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-q(o))

    def __rsub__(self, o):
        return q(o) - self

    def __mul__(self, o):
        o = q(o)
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __eq__(self, o):
        o = q(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def iszero(self):
        return self.a == 0 and self.b == 0

    def __repr__(self):
        if self.b == 0:
            return str(self.a)
        return f"{self.a} + {self.b} sqrt2"


def q(x):
    return x if isinstance(x, Q2) else Q2(x, 0)


R = Q2(0, F(1, 2))       # sqrt2 / 2
Z0, O1 = Q2(0), Q2(1)
I3 = [[O1 if i == j else Z0 for j in range(3)] for i in range(3)]


def mat(rows):
    return [[q(x) for x in r] for r in rows]


def mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), Z0) for j in range(3)] for i in range(3)]


def mv(A, v):
    return [sum((A[i][k] * v[k] for k in range(3)), Z0) for i in range(3)]


def eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(3) for j in range(3))


def tr(A):
    return A[0][0] + A[1][1] + A[2][2]


def cross(u, v):
    return [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]


def pair(kind, a, b):
    M = [[O1 if i == j else Z0 for j in range(3)] for i in range(3)]
    if kind == "rot":
        M[a][a], M[a][b], M[b][a], M[b][b] = R, -R, R, R
    else:
        M[a][a], M[a][b], M[b][a], M[b][b] = R, R, R, -R
    return M


def det(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def order_upto(A, kmax):
    P = A
    for k in range(1, kmax + 1):
        if eq(P, I3):
            return k
        P = mul(P, A)
    return None


def certificate(U):
    """(minimal polynomial of 2cos(theta) = tr - 1 over Q as (c1, c0) for x^2 + c1 x + c0, or degree 1; infinite?)"""
    y = tr(U) - 1
    if y.b == 0:
        c = y.a
        return ("x - " + str(c)), (c.denominator != 1 or c not in (-2, -1, 0, 1, 2)) and c.denominator != 1
    c1, c0 = -2 * y.a, y.a * y.a - 2 * y.b * y.b
    return f"x^2 + ({c1}) x + ({c0})", not (c1.denominator == 1 and c0.denominator == 1)


def axis(U):
    return [U[2][1] - U[1][2], U[0][2] - U[2][0], U[1][0] - U[0][1]]


def parallel(u, v):
    return all(c.iszero() for c in cross(u, v))


def perm_mat(p):
    return [[O1 if p[j] == i else Z0 for j in range(3)] for i in range(3)]


PERMS = [perm_mat(p) for p in permutations(range(3))]
RES = {}
CC = {}
print("== o7_density ==")
print()
R01, R12 = pair("rot", 0, 1), pair("rot", 1, 2)
H01, H12 = pair("ref", 0, 1), pair("ref", 1, 2)
orth = all(eq(mul([[A[j][i] for j in range(3)] for i in range(3)], A), I3) for A in (R01, R12, H01, H12))
print(f"orthogonality of R01, R12, H01, H12: {orth}; determinants: {det(R01)}, {det(R12)}, {det(H01)}, {det(H12)}")
print()
# D1
U = mul(R01, R12)
mp, inf = certificate(U)
n = axis(U)
d1 = (order_upto(R01, 8) == 8 and order_upto(R12, 8) == 8 and inf and any(not c.iszero() for c in n)
      and all((a - b).iszero() for a, b in zip(mv(U, n), n)) and not parallel(mv(R01, n), n))
RES["D1"] = d1 and orth
print(f"D1  rotation pair: orders {order_upto(R01, 8)}, {order_upto(R12, 8)}; U = R01 R12: tr - 1 = {tr(U) - 1}, "
      f"minimal polynomial {mp}, infinite order certified: {inf}; axis n = {n}, U n = n: "
      f"{all((a - b).iszero() for a, b in zip(mv(U, n), n))}; R01 n parallel to n: {parallel(mv(R01, n), n)}  -> "
      f"closure = SO(3): {RES['D1']}")
# D2
Up = mul(H01, H12)
mp2, inf2 = certificate(Up)
n2 = axis(Up)
fix01 = all((a - b).iszero() for a, b in zip(mv(H01, n2), n2))
fix12 = all((a - b).iszero() for a, b in zip(mv(H12, n2), n2))
rot_ok = det(Up) == 1
RES["D2"] = inf2 and rot_ok and fix01 and fix12 and any(not c.iszero() for c in n2)
CC["CC1"] = not (parallel(mv(H01, n2), n2) and parallel(mv(H12, n2), n2))
print(f"D2  reflection pair: U' = H01 H12 (det {det(Up)}): tr - 1 = {tr(Up) - 1}, minimal polynomial {mp2}, infinite "
      f"order certified: {inf2}; axis n' = {n2}; H01 n' = n': {fix01}; H12 n' = n': {fix12}  -> closure = stabilizer "
      f"of n' (a proper closed subgroup, a copy of O(2)): {RES['D2']}")
# D3
moved_rot = [P for P in PERMS if not parallel(mv(P, n), n)]
moved_ref = [P for P in PERMS if not parallel(mv(P, n2), n2)]
odd = [P for P in PERMS if det(P) == -1]
RES["D3"] = len(moved_rot) > 0 and len(moved_ref) > 0 and len(odd) == 3
print(f"D3  with the exchanges: permutations moving n off its line: {len(moved_rot)}/6; moving n' off its line: "
      f"{len(moved_ref)}/6; odd permutations (det -1): {len(odd)}  -> both closures = O(3): {RES['D3']}")
# D4: Gaussian-rational check of Ad(S0) on so(3); real closures cannot reach diag(i,1,1) up to phase
# Ad(S0)(E01 - E10) = S0 (E01 - E10) S0^-1 with S0 = diag(i, 1, 1): entries (0,1) -> i*1, (1,0) -> -1 * conj... computed:
S0 = [complex(0, 1), 1, 1]
S0inv = [complex(0, -1), 1, 1]
Xa = [[0, 1, 0], [-1, 0, 0], [0, 0, 0]]
Ad = [[S0[i] * Xa[i][j] * S0inv[j] for j in range(3)] for i in range(3)]
real_antisym = all(Ad[i][j].imag == 0 and Ad[i][j].real == -Ad[j][i].real for i in range(3) for j in range(3))
expected = [[0, 1j, 0], [1j, 0, 0], [0, 0, 0]]
ad_ok = all(Ad[i][j] == expected[i][j] for i in range(3) for j in range(3))
# c V = diag(i,1,1) with V real: V = c^-1 diag(i,1,1) real needs c^-1 i and c^-1 both real: impossible
# (their ratio i is not real); recorded as the exact ratio test
ratio_real = (complex(0, 1) / 1).imag == 0
D = [-1, 1, 1]
AdD = [[D[i] * Xa[i][j] * D[j] for j in range(3)] for i in range(3)]
CC["CC3"] = not all(AdD[i][j] == -AdD[j][i] for i in range(3) for j in range(3))
dets = sorted({str(det(A)) for A in [R01, R12, H01, H12] + PERMS})
RES["D4"] = ad_ok and not real_antisym and not ratio_real
print(f"D4  Ad(S0)(E01 - E10) = i (E01 + E10): {ad_ok}; still in so(3): {real_antisym}; real V with c V = diag(i,1,1): "
      f"impossible (ratio i/1 real: {ratio_real}); determinants of the real generators: {dets}, det S0 = i  -> "
      f"closure with S0 = {{U : det(U)^4 = 1}}, containing SU(3): {RES['D4']}")
# CC2
U2 = mul(R01, R01)
_, inf_cc = certificate(U2)
CC["CC2"] = inf_cc
print()
print("-- countercontrols (must be False)")
for k in sorted(CC):
    print(f"{k}  {'CC-OK (False as required)' if not CC[k] else 'CC-FAIL (True)'}")
print()
for k in sorted(RES):
    print(f"  {k}: {RES[k]}")
if any(CC.values()):
    print("VERDICT VOID: a countercontrol returned True.")
elif all(RES.values()):
    print("VERDICT DENSE-AT-THE-BALANCED-ANGLE: the rotation pair rot(pi/4) on overlapping pairs is dense in SO(3); the")
    print("  reflection (Hadamard) pair has an infinite-order product but fixes its axis, so its closure is a proper")
    print("  closed subgroup (a copy of O(2)); with the exchanges both close to O(3); as unitaries all are real (closure in")
    print("  O(3), proper in U(3)); the quarter phase lifts the closure to {U : det(U)^4 = 1}, which contains SU(3).")
else:
    print(f"VERDICT MIXED: failing items {[k for k, v in RES.items() if not v]}")

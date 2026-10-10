"""EQ2-C, C3 target 3: the reversible operations.

Question walked here: Theorem BP-S needs SS (the reversible maps act transitively on ORDERED frames). Is SS implied by
weaker, more familiar reversibility premises at capacity two: a CONNECTED group transitive on the pure states,
continuous reversibility, swaps of every frame, together with Spec2 and full effects?

DECISION RULE (fixed before the first run). Verdict "SS-INDEPENDENT" prints only if all checks pass:
  O1 bidisk D x D: SO(2) x SO(2) (connected, abelian) is transitive on the pure states S1 x S1 (exact rational
     witnesses); every frame has a swapping automorphism (exact witnesses for both frame types, including a
     non-antipodal frame); and still SS fails (c3_bp BD.2: frame midpoints c and != c).
  O2 Stiefel orbitope: SO(3) (connected, non-abelian) is transitive on V2(R^3) (exact rational witness); the
     non-antipodal frame (A, B) has a swapping automorphism; SS fails (c3_bp ST.2).
  O3 positive control: on the Bloch ball, SO(3) maps the ordered frame (e3, -e3) to (n, -n) and every frame has a
     swap (a pi-rotation about an axis orthogonal to n) — SS holds.
  O4 the frame swap at capacity two is a NOT candidate: on the ball the pi-rotations about axes orthogonal to z
     swap (z, -z), are involutions and are conjugate by rotations fixing z (type covariance automatic for SO(3),
     EQ-B); countercontrol: two z-flipping orthogonal involutions with different eigen-splits are not conjugate by
     any orthogonal map fixing z (traces differ).
Exact arithmetic only.
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c_common import Checks, dot, vscale, vsub  # noqa: E402

C = Checks("c3_ops")


def rot2(c, s):
    return ((c, -s), (s, c))


def mv(M, v):
    return tuple(sum(M[i][k] * v[k] for k in range(len(v))) for i in range(len(M)))


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0])))
                 for i in range(len(A)))


def T(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))


def eye(n):
    return tuple(tuple(Fr(int(i == j)) for j in range(n)) for i in range(n))


def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return sum(((-1) ** j) * M[0][j] * det(tuple(tuple(M[i][k] for k in range(n) if k != j) for i in range(1, n)))
               for j in range(n))


def householder(w):
    ww = dot(w, w)
    n = len(w)
    return tuple(tuple(Fr(int(i == j)) - 2 * w[i] * w[j] / ww for j in range(n)) for i in range(n))


# ----------------------------------------------------------------------------- O1: the bidisk

print("== O1 bidisk D x D")
units = [(Fr(3, 5), Fr(4, 5)), (Fr(-5, 13), Fr(12, 13)), (Fr(8, 17), Fr(-15, 17)), (Fr(1), Fr(0))]
ok_tr = True
for u in units:
    for v in units:
        Ru = rot2(u[0], u[1])          # maps e1 to u
        Rv = rot2(v[0], v[1])
        ok_tr &= mv(Ru, (Fr(1), Fr(0))) == u and mv(Rv, (Fr(1), Fr(0))) == v and det(Ru) == 1 and det(Rv) == 1 \
            and mm(Ru, T(Ru)) == eye(2)
C.check("O1.1 SO(2) x SO(2) is transitive on S1 x S1: exact rational rotation pairs carry (e1, e1) to (u, v) for 16 "
        "rational unit pairs", ok_tr)
# frame type 1 (antipodal): swap by -1 (central symmetry)
x = ((Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)))
minus = lambda w: tuple(tuple(-c for c in comp) for comp in w)  # noqa: E731
C.check("O1.2 an antipodal frame (x, -x) is swapped by the automorphism w -> -w", minus(minus(x)) == x)
# frame type 2: (x, y) with y1 = -x1, y2 = v' arbitrary unit: swap by (w1, w2) -> (-w1, H w2), H the reflection
# exchanging x2 and v'
v2 = (Fr(-8, 17), Fr(15, 17))
y = (tuple(-c for c in x[0]), v2)
H = householder(vsub(x[1], v2))
swapmap = lambda w: (tuple(-c for c in w[0]), mv(H, w[1]))  # noqa: E731
C.check("O1.3 the non-antipodal frame (x, y), y = (-x1, v'), is swapped by (w1, w2) -> (-w1, H w2) with H the "
        "reflection exchanging x2 and v'; H is orthogonal, so the map is an automorphism of D x D",
        swapmap(x) == y and swapmap(y) == x and mm(H, T(H)) == eye(2))
e_y = lambda w: Fr(1, 2) + Fr(1, 2) * dot(x[0], w[0])  # noqa: E731
C.check("O1.4 (x, y) is a frame: the effect 1/2 + (1/2) x1.w1 is 1 on x and 0 on y; its midpoint is "
        "(0, (x2 + v')/2) != 0, so by the centroid argument (c3_bp BD.2) no automorphism maps it to (x, -x): SS fails "
        "although every frame has a swap and the pure states form one orbit of a connected group",
        e_y(x) == 1 and e_y(y) == 0 and tuple((p + q) / 2 for p, q in zip(x[1], v2)) != (0, 0))

# ----------------------------------------------------------------------------- O2: the Stiefel orbitope

print("== O2 Stiefel orbitope conv V2(R^3)")
n1 = (Fr(2, 3), Fr(1, 3), Fr(2, 3))
n2 = (Fr(-2, 3), Fr(2, 3), Fr(1, 3))            # orthonormal to n1
e1, e2, e3 = (Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0)), (Fr(0), Fr(0), Fr(1))
H1 = householder(vsub(e1, n1))                   # e1 -> n1
H2v = vsub(mv(H1, e2), n2)
H2 = householder(H2v) if dot(H2v, H2v) != 0 else eye(3)
Lrot = mm(H2, H1)                                # e1 -> n1, e2 -> n2 (H2 fixes n1 as n1 is orthogonal to H2v)
if det(Lrot) != 1:                               # make it a rotation: compose with the reflection fixing n1, n2
    Lrot = mm(householder(tuple(a * b - c * d for a, b, c, d in [(n1[1], n2[2], n1[2], n2[1]),
                                                                (n1[2], n2[0], n1[0], n2[2]),
                                                                (n1[0], n2[1], n1[1], n2[0])])), Lrot)
C.check("O2.1 SO(3) is transitive on V2(R^3): an exact rational rotation (det +1) carries the standard 2-frame "
        "(e1, e2) to (n1, n2)", mv(Lrot, e1) == n1 and mv(Lrot, e2) == n2 and det(Lrot) == 1
        and mm(Lrot, T(Lrot)) == eye(3))
A = ((Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(0), Fr(0)))
B = ((Fr(-1), Fr(0)), (Fr(0), Fr(1)), (Fr(0), Fr(0)))
Lref = ((Fr(-1), 0, 0), (0, Fr(1), 0), (0, 0, Fr(1)))
C.check("O2.2 the non-antipodal frame (A, B) of c3_bp ST.1 is swapped by X -> diag(-1,1,1) X, which preserves the "
        "operator norm; its midpoint is not the centroid, so SS fails (c3_bp ST.2)",
        mm(Lref, A) == B and mm(Lref, B) == A)

# ----------------------------------------------------------------------------- O3: the Bloch ball (positive control)

print("== O3 Bloch ball: SS holds")
n = (Fr(2, 3), Fr(1, 3), Fr(2, 3))
R1 = householder(vsub(e3, n))
wp = vsub((Fr(1, 3), Fr(-2, 3), Fr(0)), vscale(dot((Fr(1, 3), Fr(-2, 3), Fr(0)), n), n))
Rot = mm(householder(wp), R1)
C.check("O3.1 a rational rotation maps the ordered frame (e3, -e3) to (n, -n)",
        mv(Rot, e3) == n and det(Rot) == 1)
m = (Fr(1, 3), Fr(-2, 3), Fr(2, 3))             # unit, orthogonal to n
Pi_m = tuple(tuple(2 * m[i] * m[j] - Fr(int(i == j)) for j in range(3)) for i in range(3))
C.check("O3.2 the pi-rotation about m (orthogonal to n) is a rotation swapping n and -n: every frame has a swap",
        mv(Pi_m, n) == vscale(-1, n) and det(Pi_m) == 1 and mm(Pi_m, Pi_m) == eye(3))

# ----------------------------------------------------------------------------- O4: the frame swap as a NOT

print("== O4 the frame swap at capacity two as a NOT; type covariance")
z = e3
Na = tuple(tuple(2 * e1[i] * e1[j] - Fr(int(i == j)) for j in range(3)) for i in range(3))   # pi-rotation about x
a = (Fr(3, 5), Fr(4, 5), Fr(0))
Nb = tuple(tuple(2 * a[i] * a[j] - Fr(int(i == j)) for j in range(3)) for i in range(3))     # pi-rotation about a
g = ((Fr(3, 5), Fr(-4, 5), 0), (Fr(4, 5), Fr(3, 5), 0), (0, 0, Fr(1)))                      # rotation about z, e1 -> a
ginv = T(g)
C.check("O4.1 Na, Nb are z-flipping involutions of the ball (orthogonal, N^2 = 1, N z = -z) and Nb = g Na g^-1 with "
        "g a rotation fixing z (type covariance, EQ-E T2's hypothesis, holds for SO(3)-related NOTs)",
        all(mm(N, N) == eye(3) and mv(N, z) == vscale(-1, z) and mm(N, T(N)) == eye(3) for N in (Na, Nb))
        and mm(mm(g, Na), ginv) == Nb and mv(g, z) == z and det(g) == 1)
# countercontrol: different eigen-splits at d = 5 (NB-1's C2N pair): N_A = diag(1,-1,1,-1,-1), N_B = nC5 =
# diag(1,-1,-1,-1,-1): conjugacy by an orthogonal map preserves the trace
trA = 1 - 1 + 1 - 1 - 1
trB = 1 - 1 - 1 - 1 - 1
C.check(f"O4.2 countercontrol: N_A = diag(1,-1,1,-1,-1) (trace {trA}) and nC5 = diag(1,-1,-1,-1,-1) (trace {trB}) "
        "are not conjugate by any linear map (traces differ): type covariance excludes NB-1's C2N pair",
        trA != trB)

sys.exit(C.finish("SS-INDEPENDENT: SS is not implied by a connected group transitive on pure states with a swap for "
                  "every frame, Spec2, capacity two and full effects (bidisk: abelian; Stiefel: non-abelian); on the "
                  "ball SS holds and its frame swaps are the NOTs, conjugate by rotations fixing z"))

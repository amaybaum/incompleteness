#!/usr/bin/env python3
# nogo_probes.py — certificate for the classical-dimension operational obstruction
# (Main §3.4, b128) and for the COUNTEREXAMPLE that invalidated the earlier
# convex-geometry proof (b125's polytope inference; correction of record, b128).
# Exact arithmetic over Q(√3).
#
# The SIC embedding: tetrahedral unit vectors a_i = (±1,±1,±1)/√3, map
# p_i(r) = (1 + a_i·r)/4. Certified, all exact:
#   (1) affine + injective: r = 3 Σ p_i a_i recovers r on a spanning sample;
#   (2) validity on the ball: p(r) ∈ Δ_3 for representative pure and mixed states —
#       so a 4-ontic-state model CAN carry the qubit state GEOMETRY under restricted
#       preparations (the counterexample to "finite ⇒ polytope state space");
#   (3) curvature witness: image(ẑ) lies strictly outside conv of the four vertex
#       states' images (exact separating functional) — the image is not the polytope
#       on its generators;
#   (4) the obstruction's true mechanism: the sharp effect P0 = |0⟩⟨0| has affine
#       extension ξ(λ_1) = 1/2 + √3/2 > 1 at an ontic vertex — no valid [0,1]
#       response function exists, so the geometric embedding cannot carry the
#       qubit's sharp effects; exact sign test.
#   (5) the elementary factorization half of the Proposition: any N-ontic-state
#       model's prepare-measure behavior matrix factors as B = Ξ M with M column-
#       stochastic (N rows) and Ξ ∈ [0,1] — verified constructively on a finite
#       classical model — so nonnegative rank ≤ N; the unboundedness for qubit
#       behaviors is the imported HKLP theorem, not re-proved here.
import sys, math
from fractions import Fraction as F

fails = 0
def check(name, ok, msg=""):
    global fails
    print(("PASS" if ok else "FAIL"), name, (" " + msg if msg else ""))
    if not ok: fails += 1

class S:  # a + b*sqrt(3), a,b rational
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0): s.a = F(a); s.b = F(b)
    def __add__(s, o): return S(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return S(s.a - o.a, s.b - o.b)
    def __mul__(s, o): return S(s.a * o.a + 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def sign(s):
        if s.a == 0 and s.b == 0: return 0
        if s.a >= 0 and s.b >= 0: return 1
        if s.a <= 0 and s.b <= 0: return -1
        d = s.a * s.a - 3 * s.b * s.b
        if s.a > 0: return 1 if d > 0 else (-1 if d < 0 else 0)
        return -1 if d > 0 else (1 if d < 0 else 0)
    def __float__(s): return float(s.a) + float(s.b) * 3 ** 0.5

ONE, ZERO = S(1), S(0)
IS3 = S(0, F(1, 3))                       # 1/√3
A = [(IS3, IS3, IS3), (IS3, S(0, F(-1,3)), S(0, F(-1,3))),
     (S(0, F(-1,3)), IS3, S(0, F(-1,3))), (S(0, F(-1,3)), S(0, F(-1,3)), IS3)]

def dot(u, v): return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
def pmap(r): return [ (ONE + dot(a, r)) * S(F(1,4)) for a in A ]
def recover(p):
    out = []
    for c in range(3):
        s = ZERO
        for i in range(4): s = s + p[i] * A[i][c]
        out.append(s * S(3))
    return tuple(out)

samples = [tuple(A[0]), tuple(A[1]), (ONE, ZERO, ZERO), (ZERO, ZERO, ONE),
           (S(F(1,2)), ZERO, ZERO), (ZERO, ZERO, ZERO)]
ok1 = all(recover(pmap(r)) == r for r in samples)
check("sic_affine_injective", ok1, "r = 3 Σ p_i a_i on 6 spanning states, exact")

ok2 = True
for r in samples:
    p = pmap(r)
    tot = p[0] + p[1] + p[2] + p[3]
    if tot != ONE: ok2 = False
    for pi in p:
        if pi.sign() < 0 or (pi - ONE).sign() > 0: ok2 = False
check("ball_image_valid", ok2, "images in Δ_3 for pure and mixed states — geometry carried by 4 ontic states")

# (3) separating functional f(p) = (1 + 3 Σ p_i (a_i·ẑ)) / 2 = qubit ⟨P0⟩ pullback
zhat = (ZERO, ZERO, ONE)
def f(p):
    s = ZERO
    for i in range(4): s = s + p[i] * dot(A[i], zhat)
    return (ONE + S(3) * s) * S(F(1,2))
img_z = pmap(zhat)
vals = [f(pmap(a)) for a in [tuple(v) for v in A]]
sep = all(((f(img_z) - v).sign() > 0) for v in vals)
check("image_curved_extreme", sep,
      "f(image ẑ)=1 exceeds f at all four generator images — image is not their hull")

xi_vertex = (ONE + S(3) * dot(A[0], zhat)) * S(F(1,2))   # ξ_{P0}(λ_1) = 1/2 + √3/2
check("sharp_effect_violation", (xi_vertex - ONE).sign() > 0,
      f"ξ_P0(λ_1) = 1/2 + √3/2 ≈ {float(xi_vertex):.3f} > 1 — no valid response function")

# (5) elementary factorization half on a genuine finite classical model:
# 3 ontic states, 4 preparations (columns of M, stochastic), 3 binary effects (Ξ rows)
M = [[F(1,2), F(1,3), F(1), F(0)],
     [F(1,4), F(1,3), F(0), F(1,2)],
     [F(1,4), F(1,3), F(0), F(1,2)]]
Xi = [[F(1), F(0), F(1,2)], [F(0), F(1), F(1,2)], [F(1,2), F(1,2), F(0)]]
B = [[sum(Xi[e][l] * M[l][p] for l in range(3)) for p in range(4)] for e in range(3)]
ok5 = all(F(0) <= B[e][p] <= F(1) for e in range(3) for p in range(4)) and \
      all(sum(M[l][p] for l in range(3)) == F(1) for p in range(4))
check("factorization_half", ok5,
      "B = Ξ M with M column-stochastic, Ξ ∈ [0,1]: nonnegative rank ≤ N by construction")

print("summary: counterexample and mechanism certified exactly over Q(√3); "
      "qubit unboundedness is the imported HKLP theorem")
sys.exit(1 if fails else 0)

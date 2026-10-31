# Random rational pure states and rational measurement bases (Cayley rotations); outcome with
# small or zero exact probability. Report the largest negativity/trace ratio among unclipped
# digitized blocks (exact: ||C_-||_1 = (sqrt(tr^2 - 4 det) - tr)/2 for 2x2 Hermitian C).
from fractions import Fraction as F
import random, sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from neg_parent import rnd
from zero_outcome import block

def rot(t):   # rational rotation from Cayley parameter t
    c = (1 - t * t) / (1 + t * t); s = 2 * t / (1 + t * t); return c, s

random.seed(5)
best = (0, None)
count_dom = 0; total = 0
for _ in range(4000):
    b = random.choice([10, 12, 16])
    c1, s1 = rot(F(random.randint(1, 999), random.randint(1, 999)))
    # measurement basis psi_perp nearly orthogonal (or exactly) to the state
    eps = F(random.choice([0, 0, 1, 3, 7]), 2**(b + random.randint(0, 6)))
    c2, s2 = rot(F(random.randint(1, 999), random.randint(1, 999)))
    rho = [[rnd(c1 * c1, b), rnd(c1 * s1, b)], [rnd(c1 * s1, b), rnd(s1 * s1, b)]]
    # projector onto v = (-s1, c1) rotated slightly towards psi by a rational amount
    vx, vy = -s1 + eps * c1, c1 + eps * s1
    nv = vx * vx + vy * vy
    M = [[vx * vx / nv, vx * vy / nv], [vx * vy / nv, vy * vy / nv]]
    C = block(M, rho, b)
    tr = C[0][0] + C[1][1]; det = C[0][0] * C[1][1] - C[0][1] ** 2
    if tr <= 0: continue
    total += 1
    disc = float(tr * tr - 4 * det)
    neg = max(0.0, (math.sqrt(disc) - float(tr)) / 2)
    r = neg / float(tr)
    if det < -2 * tr * tr: count_dom += 1      # exact test of neg > tr
    if r > best[0]: best = (r, (b, float(tr * 2**b), float(det * 4**b), float(eps)))
print(f"unclipped blocks: {total}; negativity-dominated (exact test ||C_-|| > Tr C): {count_dom}")
print(f"largest ratio ||C_-||_1 / Tr C = {best[0]:.3f} at b, Tr*2^b, det*4^b, eps = {best[1]}")

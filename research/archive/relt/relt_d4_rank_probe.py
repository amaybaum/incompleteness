"""REL-T node N2.4: d = 4 linear-core rank probe (exact rational arithmetic).
For sigma = diag(R, -1) of several types, the rank of a 3x3 block matrix over Lsig (T = z-perp, dim 3) with random
rational coefficients.  Rank 15 at one instance CERTIFIES (exactly) that the tangent-vanishing core admits an
invertible tangent block for that sigma, i.e. the linear core alone does NOT exclude d = 4 there.
Control: at d = 2 the same routine must give a singular block for both sigma (A2); at d = 3 with nflip it must give
full rank 8 (DIM-1 cnot exists)."""
import random, sys
from sympy import Matrix, Rational as R, diag, eye, zeros
from relt_lsig import Lsig_exact, sig_from_R, rot2

rng = random.Random(4)
def rand_block_rank(sigma, tdim):
    B = Lsig_exact(sigma)
    if not B:
        return 0, 0
    n = sigma.shape[0] + 1
    blocks = [[sum((R(rng.randint(-7, 7), rng.randint(1, 5)) * b for b in B), zeros(n, n)) for j in range(tdim)] for k in range(tdim)]
    K = Matrix.vstack(*[Matrix.hstack(*row) for row in blocks])
    return len(B), K.rank()

ok = True
def rep(name, sigma, tdim, expect=None):
    global ok
    dimL, r = rand_block_rank(sigma, tdim)
    full = tdim * (sigma.shape[0] + 1)
    msg = f"{name}: dim Lsig = {dimL}, random block rank {r}/{full}"
    if expect is not None:
        good = (r == full) == expect
        ok = ok and good
        msg = ("PASS " if good else "FAIL ") + msg
    print(msg); sys.stdout.flush()

rep("control d2 diag(1,-1)", sig_from_R(Matrix([[1]])), 1, expect=False)
rep("control d2 -id", sig_from_R(Matrix([[-1]])), 1, expect=False)
rep("control d3 nflip", sig_from_R(diag(1, -1)), 2, expect=True)
rep("control d3 refl3-type sigma=diag(1,1,-1)", sig_from_R(diag(1, 1)), 2, expect=False)
rep("control d3 sigma=-id", sig_from_R(diag(-1, -1)), 2, expect=False)
for name, Rm in [
    ("d4 R=diag(1,-1,-1)  (p_s=1,q_s=2)", diag(1, -1, -1)),
    ("d4 R=diag(1,1,-1)   (p_s=2,q_s=1)", diag(1, 1, -1)),
    ("d4 R=I3             (p_s=3,q_s=0)", eye(3)),
    ("d4 R=-I3            (p_s=0,q_s=3)", -eye(3)),
    ("d4 R=rot(1/2)(+)1", diag(rot2(R(1, 2)), 1)),
    ("d4 R=rot(1/2)(+)-1", diag(rot2(R(1, 2)), -1)),
]:
    rep(name, sig_from_R(Rm), 3)
print("controls ok" if ok else "CONTROL FAILURE")
sys.exit(0 if ok else 1)

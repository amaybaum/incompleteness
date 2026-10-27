# Does the fixed-point kernel produce negativity-dominated branches (||rho_-||_1 > Tr rho > 0)
# that survive clipping?  Real 2x2 fixed-point arithmetic as in opglue_probes.py (round each
# product and each addition; Kraus entries rounded to b bits; Hermiticity by upper triangle).
# State |psi><psi|, psi = (x, y) Pythagorean; measure in the basis {psi, psi_perp}:
# outcome 1 has exact probability 0, so its digitized block is pure rounding noise.
from fractions import Fraction as F
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from neg_parent import rnd

def mm(A, B, b):
    return [[rnd(rnd(A[i][0] * B[0][j], b) + rnd(A[i][1] * B[1][j], b), b) for j in range(2)] for i in range(2)]
def T(A): return [[A[j][i] for j in range(2)] for i in range(2)]
def block(M, rho, b):
    Mh = [[rnd(M[i][j], b) for j in range(2)] for i in range(2)]
    C = mm(mm(Mh, rho, b), T(Mh), b)
    C[1][0] = C[0][1]
    return C

triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37)]
found = []
for (a, c, h) in triples:
    x, y = F(a, h), F(c, h)
    for b in range(8, 25):
        rho = [[rnd(x * x, b), rnd(x * y, b)], [rnd(x * y, b), rnd(y * y, b)]]   # digitized pure state
        M1 = [[y * y, -x * y], [-x * y, x * x]]                                  # projector on psi_perp
        C = block(M1, rho, b)
        tr = C[0][0] + C[1][1]; det = C[0][0] * C[1][1] - C[0][1] ** 2
        # for 2x2 Hermitian with tr > 0: ||C_-||_1 > tr  <=>  det < -2 tr^2
        if tr > 0 and det < -2 * tr * tr:
            found.append((a, c, h, b, tr * 2**b, det * 4**b))
print(f"negativity-dominated unclipped zero-probability blocks found: {len(found)}")
for f in found[:8]:
    print(f"  psi=({f[0]}/{f[2]},{f[1]}/{f[2]}), b={f[3]}: Tr C = {f[4]}*2^-b, det C = {f[5]}*4^-b")

"""Coordinator's independent spot-check of EQ-B (my code; gC5 from my own transcription of RelcSelectC5.lean).

F   The J/K flow at d = 5, rebuilt from EQ-B's stated block formulas (jk.py docstring) with my own operator builder:
      G_t(hom z (x) Y) = hom z (x) Y;  G_t(hom -z (x) Y) = hom -z (x) R_t Y;  G_t(c (x) Y) = c (x) A_t Y + Jc (x) B_t Y,
      R_t = P+ + c P- + s K P-,  A_t = (1+c)/2 I + (1-c)/2 X P+ + (s/2) K P-,
      B_t = (s/2)(P+ - X P+) + (s/2) P- + (1-c)/2 K P-.
    Checks: G_pi == landed gC5 (36x36); G_0 == I; G_t1 G_t2 == G_(t1+t2) at rational (c, s) points; G_t G_-t == I;
    normalization preserved.
W5  The word gC5 (I (x) L) gC5 at EQ-B's rational witness, for the quarter turns of homogeneous planes (2,4) and
    coordinate planes, both orientations: one of them must reproduce EQ-B's exact value
    -13755583160854480616171902/9729699913814233289411449, and gC5 alone must be nonnegative there.
"""
import sys
from sympy import Matrix, Rational as R, eye, zeros
sys.path.insert(0, "/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/bal")
from relt_common import hom, gate_from_fun, apply, prod, pairVal
from bal_gates import landed_gC5, cstruct

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


d, n = 5, 6
X = zeros(n, n); X[0, 1] = 1; X[1, 0] = 1
K = cstruct(n, [(2, 5), (3, 4)])
J = cstruct(n, [(1, 2), (3, 4)])
Pp = zeros(n, n); Pp[0, 0] = 1; Pp[1, 1] = 1
Pm = eye(n) - Pp
z = Matrix([0, 0, 0, 0, 1])
hz, hm = hom(z), hom(-z)


def flow(c, s):
    Rt = Pp + c * Pm + s * K * Pm
    At = (1 + c) / 2 * eye(n) + (1 - c) / 2 * X * Pp + s / 2 * K * Pm
    Bt = s / 2 * (Pp - X * Pp) + s / 2 * Pm + (1 - c) / 2 * K * Pm

    def G_basis(mu, Y):
        if mu == 0:
            return (hz * Y.T + hm * (Rt * Y).T) / 2
        if mu == d:
            return (hz * Y.T - hm * (Rt * Y).T) / 2
        e = zeros(n, 1); e[mu] = 1
        return e * (At * Y).T + (J * e) * (Bt * Y).T

    def fun(w):
        out = zeros(n, n)
        for mu in range(n):
            for nu in range(n):
                if w[mu, nu] != 0:
                    Y = zeros(n, 1); Y[nu] = 1
                    out += w[mu, nu] * G_basis(mu, Y)
        return out
    return gate_from_fun(fun, n)


GC5 = landed_gC5()
Gpi = flow(R(-1), R(0))
check("F G_pi (rebuilt from EQ-B's block formulas) == landed gC5 (my transcription of RelcSelectC5 tables)",
      (Gpi - GC5).is_zero_matrix)
check("F G_0 == identity", (flow(R(1), R(0)) - eye(36)).is_zero_matrix)
c1, s1 = R(3, 5), R(4, 5)
c2, s2 = R(5, 13), R(12, 13)
G1, G2 = flow(c1, s1), flow(c2, s2)
G12 = flow(c1 * c2 - s1 * s2, s1 * c2 + c1 * s2)
check("F group law G_t1 G_t2 == G_(t1+t2) at (3/5, 4/5), (5/13, 12/13)", (G1 * G2 - G12).is_zero_matrix)
check("F inverse G_t G_-t == I", (G1 * flow(c1, -s1) - eye(36)).is_zero_matrix)
check("F normalization: (G_t w)_00 == w_00 for all w (row 0 of the operator is e_00)",
      all(G1[0, j] == (1 if j == 0 else 0) for j in range(36)))

# W5 witness
x = Matrix([R(-504000, 1001741), R(524000, 1001741), R(641000, 1001741), R(253000, 1001741), R(-1741, 1001741)])
y = Matrix([R(-64000, 12477097), R(6292000, 12477097), R(-1692000, 12477097), R(1858000, 12477097),
            R(-10477097, 12477097)])
a = Matrix([R(1004000, 1983973), R(-1046000, 1983973), R(-1252000, 1983973), R(-516000, 1983973),
            R(16027, 1983973)])
b = Matrix([R(5600, 392369), R(-179800, 392369), R(-273400, 392369), R(99200, 392369), R(-192369, 392369)])
check("W5 witness vectors are exact unit vectors", all((v.T * v)[0, 0] == 1 for v in (x, y, a, b)))
target = R(-13755583160854480616171902, 9729699913814233289411449)
e, f = hom(a), hom(b)
P0 = prod(x, y)
base = pairVal(e, f, apply(GC5, P0))
check(f"W5 gC5 alone is nonnegative at the witness ({float(base):.6f})", base >= 0)
found = []
for (i, j) in [(2, 4), (4, 2), (3, 5), (5, 3), (1, 3), (3, 1), (2, 3), (3, 2)]:
    L = eye(n); L[i, i] = 0; L[j, j] = 0; L[j, i] = 1; L[i, j] = -1
    TL = gate_from_fun(lambda w: w * L.T, n)
    v = pairVal(e, f, apply(GC5 * TL * GC5, P0))
    if v == target:
        found.append((i, j))
print("     planes (homogeneous indices, e_i -> e_j) reproducing EQ-B's exact value:", found)
check("W5 EQ-B's exact negative value is reproduced by gC5 (I(x)L) gC5 for a quarter turn of a homogeneous plane",
      len(found) >= 1 and target < 0)

npass = sum(1 for _, c in checks if c)
print(f"review_eqB: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)

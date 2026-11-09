"""ASSESS-868 r2: exact generic checks (WIP / UNVERIFIED).

Generic two-qubit tables and 2x2 / 4x4 matrices only. No OI update rule, encoding, record law or
mechanism is simulated or enumerated. Imports no earlier probe. Run: python3 -I r2_validity_scope.py

Table convention: w[i][j] = <s_i (x) s_j> for i, j in 0..3 with s_0 = I, s_1 = X, s_2 = Y, s_3 = Z.
Pauli product test (a, b) with a = +-e_i, b = +-e_j has value pairVal = ahat^T w bhat >= 0 required
(ahat = (1, a)); herald of wing B by A-effect ahat is h = ahat^T w.

V1  dual cone of the six Pauli sharp effects is the cube {|v_i| <= t} (exact, vertex check);
V2  table w3 (<XX> = <XY> = 1, rest 0) passes all 36 Pauli product tests, its +x herald (1,1,1,0)
    is in the cube cone, outside the octahedron cone and outside the Lorentz cone;
V3  passing every product test is not being a quantum state: T = (I + XX + ZZ)/4 passes every
    full-ball product test (Lemma H (<=): every herald is in Lor) and has eigenvalue -1/4;
    the swap operator is nonnegative on every product of pure states (block-positive) and has
    eigenvalue -1;
V4  law c = (1, 1, 1, 1/2) with zero marginals: p >= 0, no-signalling, max CHSH = 5/2 < 2 sqrt 2;
    PR box S = 4;
V5  real operations keep <Y> = 0 on a real symmetric state; S H |0> has <Y> = 1 (phase needed);
V6  H (x) H is real and non-monomial, and (I + YY)/4, (I - YY)/4 agree on every real product
    test (a non-monomial operation does not give local tomography).
"""
import itertools
import sympy as sp

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
S = [I2, X, Y, Z]
kron = sp.kronecker_product
ok = {}

def pauli_tests_ok(w):
    for i, j in itertools.product(range(1, 4), repeat=2):
        for sa, sb in itertools.product((1, -1), repeat=2):
            a = [0, 0, 0]; a[i - 1] = sa; b = [0, 0, 0]; b[j - 1] = sb
            ah = [1] + a; bh = [1] + b
            v = sum(ah[k] * w[k][l] * bh[l] for k in range(4) for l in range(4))
            if v < 0:
                return False
    # also the 0-index (identity) tests on each wing are covered by marginals here (zero marginals)
    return True

def herald(w, a):
    ah = [1] + list(a)
    return [sum(ah[k] * w[k][l] for k in range(4)) for l in range(4)]

# V1: (t,v) with t +- v_i >= 0 for all i  <=>  max |v_i| <= t; cube vertex (1,1,1,1) passes, (1,1.01..) fails
cube_vertex = [1, 1, 1, 1]
ok['V1'] = all(cube_vertex[0] + s * cube_vertex[i] >= 0 for i in (1, 2, 3) for s in (1, -1)) and \
    not all(1 + s * sp.Rational(101, 100) >= 0 for s in (1, -1))

# V2
w3 = [[0] * 4 for _ in range(4)]; w3[0][0] = 1; w3[1][1] = 1; w3[1][2] = 1
h = herald(w3, (1, 0, 0))
t, v = h[0], h[1:]
ok['V2'] = pauli_tests_ok(w3) and h == [1, 1, 1, 0] and max(abs(x) for x in v) <= t \
    and sum(abs(x) for x in v) > t and sum(x * x for x in v) > t * t

# V3
T = (kron(I2, I2) + kron(X, X) + kron(Z, Z)) / 4
w = [[sp.simplify((T * kron(S[k], S[l])).trace()) for l in range(4)] for k in range(4)]
a1, a2, a3 = sp.symbols('a1 a2 a3', real=True)
hT = herald(w, (a1, a2, a3))
# herald (1, a1, 0, a3): in Lor iff a1^2 + a3^2 <= 1, implied by |a| <= 1
lor_ok = sp.simplify(hT[0] - 1) == 0 and sp.simplify(hT[2]) == 0 and sp.simplify(hT[1] - a1) == 0 and sp.simplify(hT[3] - a3) == 0
evT = T.eigenvals()
SW = sp.Matrix(4, 4, lambda r, c: 1 if (r, c) in {(0, 0), (1, 2), (2, 1), (3, 3)} else 0)
evS = SW.eigenvals()
# block-positivity of swap: <u (x) v| SW |u (x) v> = |<u|v>|^2 >= 0, symbolic in general complex u, v
u = sp.Matrix(sp.symbols('u0 u1')); vv = sp.Matrix(sp.symbols('v0 v1'))
uv = kron(u, vv)
val = sp.expand((uv.H * SW * uv)[0])
inner = sp.expand((u.H * vv)[0] * (vv.H * u)[0])
ok['V3'] = lor_ok and sp.Rational(-1, 4) in evT and sp.simplify(val - inner) == 0 and -1 in evS

# V4
c = {(0, 0): sp.Integer(1), (0, 1): sp.Integer(1), (1, 0): sp.Integer(1), (1, 1): sp.Rational(1, 2)}  # exact (run 1 used Python ints: float division)
probs_ok = all((1 + a * b * c[xy]) / 4 >= 0 for xy in c for a in (1, -1) for b in (1, -1))
# marginals: sum_b p(ab|xy) = 1/2 for every a, x, y  (zero-marginal law, so no-signalling)
ns_ok = all(sum((1 + a * b * c[xy]) / 4 for b in (1, -1)) == sp.Rational(1, 2) for xy in c for a in (1, -1))
chsh = max(abs(s00 * c[(0, 0)] + s01 * c[(0, 1)] + s10 * c[(1, 0)] + s11 * c[(1, 1)])
           for s00, s01, s10, s11 in itertools.product((1, -1), repeat=4)
           if s00 * s01 * s10 * s11 == -1)
pr = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): -1}
ok['V4'] = probs_ok and ns_ok and chsh == sp.Rational(5, 2) and chsh < 2 * sp.sqrt(2) and \
    (pr[(0, 0)] + pr[(0, 1)] + pr[(1, 0)] - pr[(1, 1)]) == 4

# V5
r00, r01, r11 = sp.symbols('r00 r01 r11', real=True)
rho = sp.Matrix([[r00, r01], [r01, r11]])
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2); Sg = sp.diag(1, sp.I)
k0 = sp.Matrix([[1, 0], [0, 0]])
ry = sp.simplify((Sg * H * k0 * H.H * Sg.H * Y).trace())
ok['V5'] = sp.simplify((rho * Y).trace()) == 0 and ry == 1

# V6
HH = kron(H, H)
real_nonmono = all(x.is_real for x in HH) and any(sum(1 for x in HH.row(i) if x != 0) > 1 for i in range(4))
P = (kron(I2, I2) + kron(Y, Y)) / 4; M = (kron(I2, I2) - kron(Y, Y)) / 4
real_effects = [I2, X, Z]  # real symmetric Pauli span (Y is imaginary antisymmetric)
agree = all(sp.simplify((P * kron(A, B)).trace() - (M * kron(A, B)).trace()) == 0
            for A in real_effects for B in real_effects)
ok['V6'] = real_nonmono and agree

for key, val_ in ok.items():
    print(key, 'PASS' if val_ else 'FAIL')
print('ALL PASS' if all(ok.values()) else 'SOME FAIL')
raise SystemExit(0 if all(ok.values()) else 1)

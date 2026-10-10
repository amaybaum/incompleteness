"""o4_dependency.py -- research/origin, node O4: the exact dependency between Origin and the composite-action bridge.

CLAIMS TESTED (exact; rational 3x3 Bloch matrices, Gaussian-rational 2x2 operators):
  D1  ball3Drive's off-frame partner J = cyc3 (cyc3 v = (v2, v0, v1), kernel KInfFoundations `cyc3_apply`) is
      the product R_z(pi/2) R_x(pi/2) of the two flows' quarter turns, so it lies in the group they generate.
  D2  J conjugates the phase flow about the frame axis z into the drive about x: J R_z(t) J^-1 = R_x(t) for
      several Pythagorean angles; so invariance under {R_z(t) for all t, J} is equivalent to invariance under
      {R_z(t), R_x(t) for all t} (stage 6's missing assumption) -- the group identity behind NOTES-O4 (written).
  D3  J is a discrete balanced mixer for the frame z: it maps the pure frame state e_z to the pure balanced state
      e_x; with J^-1 and the frame dephasing the owner's witness (1, 1/2) holds; J has order 3.
  D4  a unitary lift U_J of J (Ad U_J = J on Bloch vectors) is non-monomial, balanced, has the owner's witness
      with U_J^dagger, and U_J^3 is scalar.
  D5  the matrix-level reduction: (1 (x) B)(1 (x) D)(1 (x) B)^dagger = 1 (x) (B D B^dagger) for B = U_J and
      diagonal D, exactly; with B = H the right side is the transition flow (o3_continuous C1a).
DECISION RULE (fixed before the first run): VERDICT O4 is printed iff all checks pass and every countercontrol
returns its expected-false value; otherwise VERDICT VOID. Countercontrols (each must be False):
  CC1  J commutes with R_z(t) (it must not: J is off the flow's axis -- OFF);
  CC2  U_J is monomial in the frame basis;
  CC3  J R_z(t) J^-1 = R_y(t) (the conjugate is specifically the x-rotation; guards against a vacuous identity).

Run: python3 -I -B o4_dependency.py > o4_dependency.out 2> o4_dependency.err; echo "exit $?" >> o4_dependency.err
"""

from fractions import Fraction as Fr

RESULTS = []


def check(cid, ok, msg=""):
    RESULTS.append((cid, bool(ok), "check"))
    print(f"{cid:6s} {'PASS' if ok else 'FAIL'}  {msg}")


def counter(cid, value, msg=""):
    RESULTS.append((cid, not bool(value), "counter"))
    print(f"{cid:6s} {'CC-OK (False as required)' if not value else 'CC-FAIL (True)'}  {msg}")


# ------------------------------------------------------------------ Bloch side (rational 3x3)

def mul3(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def ap3(A, v):
    return tuple(sum(A[i][k] * v[k] for k in range(3)) for i in range(3))


def Rz(c, s):
    return ((Fr(c), Fr(-s), Fr(0)), (Fr(s), Fr(c), Fr(0)), (Fr(0), Fr(0), Fr(1)))


def Rx(c, s):
    return ((Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(c), Fr(-s)), (Fr(0), Fr(s), Fr(c)))


def Ry(c, s):
    return ((Fr(c), Fr(0), Fr(s)), (Fr(0), Fr(1), Fr(0)), (Fr(-s), Fr(0), Fr(c)))


CYC = ((Fr(0), Fr(0), Fr(1)), (Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0)))      # cyc3 v = (v2, v0, v1)
CYCi = tuple(tuple(CYC[j][i] for j in range(3)) for i in range(3))                 # orthogonal: inverse = transpose
I3 = ((Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0)), (Fr(0), Fr(0), Fr(1)))
ANG = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(-7, 25), Fr(24, 25)), (Fr(0), Fr(1)), (Fr(8, 17), Fr(-15, 17))]

print("== o4_dependency ==")
print()
check("D1", mul3(Rz(0, 1), Rx(0, 1)) == CYC and mul3(CYC, CYCi) == I3,
      "cyc3 = R_z(pi/2) R_x(pi/2); cyc3 is orthogonal")
check("D2", all(mul3(mul3(CYC, Rz(c, s)), CYCi) == Rx(c, s) for c, s in ANG),
      f"cyc3 R_z(t) cyc3^-1 = R_x(t) for {len(ANG)} Pythagorean angles")
EZ, EX = (Fr(0), Fr(0), Fr(1)), (Fr(1), Fr(0), Fr(0))
rz_read = lambda v: (1 + v[2]) / 2
Dz = lambda v: (Fr(0), Fr(0), v[2])
mid = ap3(CYC, EZ)
coh = rz_read(ap3(CYCi, mid))
deph = rz_read(ap3(CYCi, Dz(mid)))
order3 = mul3(CYC, mul3(CYC, CYC)) == I3 and mul3(CYC, CYC) != I3
check("D3", mid == EX and rz_read(mid) == Fr(1, 2) and coh == 1 and deph == Fr(1, 2) and order3,
      f"J e_z = {mid} (balanced, pure); sandwich (J, J^-1): ({coh}, {deph}); order 3")

# ------------------------------------------------------------------ operator side (Gaussian rationals)


class G:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        o = gg(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = gg(o)
        return G(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        o = gg(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __neg__(self):
        return G(-self.re, -self.im)

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        o = gg(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def iszero(self):
        return self.re == 0 and self.im == 0

    def __repr__(self):
        if self.im == 0:
            return str(self.re)
        if self.re == 0:
            return f"{self.im}i"
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


def gg(x):
    return x if isinstance(x, G) else G(x, 0)


def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), G()) for j in range(m)] for i in range(n)]


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def eye(n):
    return [[G(1) if i == j else G(0) for j in range(n)] for i in range(n)]


h = Fr(1, 2)
X = [[G(0), G(1)], [G(1), G(0)]]
Y = [[G(0), G(0, -1)], [G(0, 1), G(0)]]
Z = [[G(1), G(0)], [G(0), G(-1)]]
PAULI = [X, Y, Z]


def bloch(rho):  # rho = (1 + x X + y Y + z Z)/2  ->  (x, y, z)
    return (rho[0][1].re * 2, rho[1][0].im * 2, rho[0][0].re - rho[1][1].re)


def ad_bloch(U):
    """the 3x3 Bloch matrix of Ad U: column k is the Bloch vector of U P_k U^dag / 1 (Paulis map to Paulis)."""
    cols = []
    for P in PAULI:
        Q = mm(mm(U, P), dag(U))
        cols.append((Q[0][1].re, Q[1][0].im, Q[0][0].re))
    return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))


U1 = [[G(h, -h), G(-h, -h)], [G(h, -h), G(h, h)]]          # (1 - iX - iY - iZ)/2
U2 = dag(U1)
UJ = None
for cand in (U1, U2):
    if meq(mm(dag(cand), cand), eye(2)) and ad_bloch(cand) == CYC:
        UJ = cand
found = UJ is not None
if found:
    rho0 = [[G(1), G(0)], [G(0), G(0)]]
    r1 = mm(mm(UJ, rho0), dag(UJ))
    back = mm(mm(dag(UJ), r1), UJ)
    r1d = [[r1[0][0], G(0)], [G(0), r1[1][1]]]
    backd = mm(mm(dag(UJ), r1d), UJ)
    U3 = mm(UJ, mm(UJ, UJ))
    scalar3 = U3[0][1].iszero() and U3[1][0].iszero() and U3[0][0] == U3[1][1]
    nonmono = not (UJ[0][1].iszero() or UJ[0][0].iszero())
    check("D4", r1[0][0] == G(h) and r1[1][1] == G(h) and back[0][0] == G(1) and backd[0][0] == G(h)
          and scalar3 and nonmono,
          f"U_J with Ad U_J = cyc3: U_J |0> balanced ({r1[0][0]}, {r1[1][1]}); sandwich (U_J, U_J^dag): "
          f"({back[0][0]}, {backd[0][0]}); U_J^3 = {U3[0][0]} * 1; non-monomial")
else:
    check("D4", False, "no unitary lift of cyc3 found among the two candidates")

p = G(Fr(3, 5), Fr(4, 5))
D = [[p.conj(), G(0)], [G(0), p]]
B = UJ if found else eye(2)
lhs = mm(mm(kron(eye(2), B), kron(eye(2), D)), dag(kron(eye(2), B)))
rhs = kron(eye(2), mm(mm(B, D), dag(B)))
HRAW = [[G(1), G(1)], [G(1), G(-1)]]
HDH = [[x * G(h) for x in row] for row in mm(mm(HRAW, D), HRAW)]
FLOW = [[G(Fr(3, 5)), G(0, Fr(-4, 5))], [G(0, Fr(-4, 5)), G(Fr(3, 5))]]
check("D5", meq(lhs, rhs) and meq(HDH, FLOW),
      "(1 (x) B)(1 (x) D)(1 (x) B)^dag = 1 (x) (B D B^dag) exactly; H D H = the transition flow at cos t = 3/5")

print()
print("-- countercontrols")
counter("CC1", all(mul3(CYC, Rz(c, s)) == mul3(Rz(c, s), CYC) for c, s in ANG), "cyc3 commutes with R_z(t)")
counter("CC2", (UJ is not None) and (UJ[0][1].iszero() or UJ[0][0].iszero()), "U_J is monomial in the frame basis")
counter("CC3", all(mul3(mul3(CYC, Rz(c, s)), CYCi) == Ry(c, s) for c, s in ANG), "cyc3 R_z(t) cyc3^-1 = R_y(t)")

print()
nfail = sum(1 for r in RESULTS if not r[1])
nchk = sum(1 for r in RESULTS if r[2] == "check")
ncc = sum(1 for r in RESULTS if r[2] == "counter")
if nfail == 0:
    print(f"OK -- {nchk}/{nchk} checks, {ncc} countercontrols expected-false")
    print("VERDICT O4: the bridge's off-frame partner J = cyc3 is a discrete balanced mixer for the frame z (the")
    print("  owner's witness holds for it) and conjugates the substratum phase flow into the drive; the missing")
    print("  assumption (b) for {phase flow, drive} is therefore (b) for {phase flow, one discrete balanced mixer};")
    print("  at the matrix level the spectator form of the drive is the spectator form of that one mixer.")
else:
    print(f"VOID -- failing: {[r[0] for r in RESULTS if not r[1]]}")
    print("VERDICT VOID")

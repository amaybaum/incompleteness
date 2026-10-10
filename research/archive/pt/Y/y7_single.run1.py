# y7_single.py -- thread Y (stage 4, Q-EX), record nodes: invariance under ONE extra local rotation (a single
# element, no one-parameter group), with cnot only (level (i)).
#
# Written argument (RESULT Y7): if R in SO(3) acts on the control and the subgroup <R, R'> of SO(3), R' = Rz(pi) R Rz(pi),
# is infinite with R, R' about non-parallel axes, then its closure is SO(3), the closure of <cnot, actC R> contains
# Ad{I(x)P+ + V(x)P- : V in SU(2)}, every pure state is reachable, and K = Q3. Target side: R' = Rx(pi) R Rx(pi).
# Infinite order is certified by an element W = R R' whose cos(angle) = (tr W - 1)/2 is rational and not in
# {0, +-1/2, +-1} (if W^k = 1 then 2cos is a rational algebraic integer, hence an integer).
#
# DECISION RULE (fixed before the first run; rules, not expected numbers):
#  * For each record rotation: PASS iff R is exactly in SO(3) with the stated order, the axes of R and R' are not
#    parallel, cos(angle of R R') is rational and outside {0, +-1/2, +-1}, and a member of the generated group
#    (R or R^2) moves E0 out of K(E0) and some z in Z_F out of K(Z_F), each certified by an exact negative pairing
#    with an exact member of the cone.
#  * Countercontrol (the corpus's J of ball3Drive, cyc3 = rotation by 2pi/3 about (1,1,1)): PASS iff <cyc3, Rz(pi)>
#    enumerated exactly is finite (order printed) and cos(angle of cyc3 cyc3') lies in {0, +-1/2, +-1}: the
#    criterion must not fire.
#  * "VERDICT Y7-SINGLE-EXACT" iff every line passes; otherwise "VERDICT Y7-SINGLE-FAILED" and the failing ids.
import sympy as sp

I = sp.I
S = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]),
     sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
E2 = S[0]


def kron(A, B):
    return sp.Matrix(4, 4, lambda r, c: A[r // 2, c // 2] * B[r % 2, c % 2])


SS = [[kron(S[m], S[n]) for n in range(4)] for m in range(4)]
pauliW = lambda w: sum((w[m][n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4
table = lambda R: [[sp.expand((R * SS[m][n]).trace()) for n in range(4)] for m in range(4)]
ipW = lambda a, b: sp.expand(sum(a[m][n] * b[m][n] for m in range(4) for n in range(4)))
R_ = sp.Rational
fails = []


def report(cid, ok, text):
    print(("PASS " if ok else "FAIL ") + cid + " " + text)
    if not ok:
        fails.append(cid)


def rot_of(q):
    """unnormalized quaternion (a,b,c,d) -> U = (aI - i(bX+cY+dZ))/|q| in SU(2) and its exact rotation R(U)."""
    a, b, c, d = q
    N = a * a + b * b + c * c + d * d
    Uu = a * E2 - I * (b * S[1] + c * S[2] + d * S[3])
    R = sp.Matrix(3, 3, lambda i, j: sp.expand((S[i + 1] * Uu * S[j + 1] * Uu.H).trace() / (2 * N)))
    return Uu, N, R


def order(R, kmax=12):
    P = sp.eye(3)
    for k in range(1, kmax + 1):
        P = P * R
        if P == sp.eye(3):
            return k
    return None


NIVEN = {0, R_(1, 2), -R_(1, 2), 1, -1}
E0 = [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0], [0, 0, 0, 0]]
ZF = [[[R_(1, 4), 0, 0, 0], [0, 0, 0, R_(s1, 4)], [0, 0, R_(s2, 4), 0], [0, -R_(s1 * s2, 4), 0, 0]]
      for s1 in (1, -1) for s2 in (1, -1)]
gE0 = sp.Matrix([1, -1, -1, -1]) / 2
capF = [[vv for (val, mu, vs) in pauliW(z).eigenvects() if val < 0 for vv in vs][0] for z in ZF]


def exits(G):
    tE0 = table(G * pauliW(E0) * G.H)
    okE = ipW(tE0, E0) < 0
    if not okE:
        P = table(G * gE0 * gE0.H * G.H)
        okE = ipW(P, E0) >= 0 and ipW(tE0, P) < 0
    okZ = False
    for z, f in zip(ZF, capF):
        gf = G * f
        P = table(gf * gf.H / sp.expand((f.H * f)[0]))
        if all(ipW(P, zz) >= 0 for zz in ZF) and ipW(table(G * pauliW(z) * G.H), P) < 0:
            okZ = True
    return okE and okZ


RZ, RX = sp.diag(-1, -1, 1), sp.diag(1, -1, -1)
RECORD = {'control, order 3 about (5,1,1)': ((3, 5, 1, 1), 3, 'C'),
          'control, order 4 about (1,2,2)': ((3, 1, 2, 2), 4, 'C'),
          'target, order 3 about (5,1,1)': ((3, 5, 1, 1), 3, 'T')}
for name, (q, k, side) in RECORD.items():
    Uu, N, R = rot_of(q)
    okR = R.T * R == sp.eye(3) and R.det() == 1 and order(R) == k
    F = RZ if side == 'C' else RX
    Rp = F * R * F
    W = R * Rp
    cosW = (W.trace() - 1) / 2
    axis = sp.Matrix(q[1:])
    axisp = F * axis
    nonpar = axis.cross(axisp) != sp.zeros(3, 1)
    okmove = False
    for p in (1, 2):
        Up = (Uu ** p) / sp.sqrt(N) ** p
        G = kron(Up, E2) if side == 'C' else kron(E2, Up)
        okmove = okmove or exits(G)
    ok = okR and nonpar and cosW.is_rational and cosW not in NIVEN and okmove
    report("S-" + name.split(',')[0][0].upper() + str(k), ok,
           "%s: R in SO(3) of order %s; axes of R, R' non-parallel: %s; cos(angle of R R') = %s (not in {0, +-1/2, +-1}); "
           "a member moves E0 and a defect of Z_F out of their cones: %s" % (name, order(R), nonpar, cosW, okmove))
Uc, Nc, Rc = rot_of((1, 1, 1, 1))
grp, frontier = {tuple(sp.eye(3))}, [sp.eye(3)]
while frontier:
    new = []
    for X in frontier:
        for Gen in (Rc, RZ):
            Y = Gen * X
            if tuple(Y) not in grp:
                grp.add(tuple(Y)); new.append(Y)
    frontier = new
Wc = Rc * (RZ * Rc * RZ)
cosc = (Wc.trace() - 1) / 2
report("cc-cyc3", order(Rc) == 3 and len(grp) < 100 and cosc in NIVEN,
       "countercontrol, the corpus's J (cyc3, order %s): <cyc3, Rz(pi)> is finite of order %d, cos(angle of cyc3 cyc3') = %s: "
       "the criterion does not fire (cyc3 is a local Clifford, covered by y5)" % (order(Rc), len(grp), cosc))
if fails:
    print("VERDICT Y7-SINGLE-FAILED " + " ".join(fails))
else:
    print("VERDICT Y7-SINGLE-EXACT")

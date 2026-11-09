#!/usr/bin/env python3
"""r2 labelled exact generic checks for #1216 unit 1, route E_f (finding B2).  Imports nothing
from earlier probes.  Generic matrices only; no OI mechanism is run.

Two identifications of a qubit with laws on the four points (z, x) in F_2^2, both built on the
same vertex set: v(z, x) = ((-1)^z, (-1)^x, (-1)^(z+x)) as (<Z>, <X>, <Y>) components (AP1 sec 4.2).

  R1  (AP1 sec 4.2; MECH-2's R1): a law mu <-> Bloch vector r = sum_l mu_l v_l, i.e.
      rho = sum_l mu_l A_l, A_l = (I + v_l.sigma)/2; coordinates mu_l = tr(rho F_l),
      F_l = (I + v_l.sigma)/4.
  SIC (Main:562): coordinates p_l = (1 + a_l.r)/4 = tr(rho E_l), a_l = v_l/sqrt3,
      E_l = (I + a_l.sigma)/4; reconstruction rho = sum_l p_l D_l, D_l = (I + 3 a_l.sigma)/2.

Frame matrix of a channel C: M[l, k] = tr(F_l C(A_k)) (R1), tr(E_l C(D_k)) (SIC); n-qubit
frames are tensor products.

F1  frame identities; R1 is orthogonal, SIC's reconstruction frame is not; R1's coordinate
    functionals are not PSD, SIC's are.
F2  the 24 single-qubit Clifford unitaries (mod phase): frame matrices coincide in the two frames;
    12 are permutation matrices, the other 12 have minimum entry -1/2.
F3  CNOT (both orientations): minimum frame entry per frame, exact; the two frames' matrices
    differ.  Countercontrol: SWAP (Pauli-weight preserving) has equal matrices in both frames.
F4  states: r = -v_0/sqrt3 (pure) has R1 coordinate (1 - sqrt3)/4 and SIC coordinate 0;
    Phi+ has R1 product-frame minimum -1/8 and SIC product-frame minimum 0.
F5  epsilon-robustness under R1: ||F_0||_op and ||F_l (x) F_m||_op exactly, giving by Hoelder
    ||sigma - rho||_1 >= 2 - sqrt3 for every R1-represented sigma (all coordinates >= 0), for both
    witnesses of F4.
Controls: identity -> identity matrix; a local A4 rotation (x) I -> permutation matrix; a point
mass reconstructs a non-PSD operator in both frames.
Run: python3 -I -B r2_frames.py   (exit 0 iff every check passes)
"""
import itertools
import sys

import sympy as sp

FAILS = []


def check(label, cond):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAILS.append(label)


s3 = sp.sqrt(3)
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
kp = sp.kronecker_product

PTS = [(0, 0), (0, 1), (1, 0), (1, 1)]
VZXY = [((-1) ** z, (-1) ** x, (-1) ** (z + x)) for (z, x) in PTS]  # (<Z>, <X>, <Y>)


def bloch_op(v, s):
    return s * (v[0] * Z + v[1] * X + v[2] * Y)


R1_F = [(I2 + bloch_op(v, 1)) / 4 for v in VZXY]
R1_A = [(I2 + bloch_op(v, 1)) / 2 for v in VZXY]
SIC_E = [(I2 + bloch_op(v, 1 / s3)) / 4 for v in VZXY]
SIC_D = [(I2 + bloch_op(v, 3 / s3)) / 2 for v in VZXY]
FRAMES = {'R1': (R1_F, R1_A), 'SIC': (SIC_E, SIC_D)}


def simp(e):
    return sp.nsimplify(sp.simplify(sp.expand(e)), [s3])


def is_zero(M):
    return all(sp.simplify(sp.expand(x)) == 0 for x in M)


def tensor_frame(frame, n):
    F, A = frame
    Fs, As = [], []
    for idx in itertools.product(range(4), repeat=n):
        f, a = F[idx[0]], A[idx[0]]
        for i in idx[1:]:
            f, a = kp(f, F[i]), kp(a, A[i])
        Fs.append(f)
        As.append(a)
    return Fs, As


def frame_matrix(U, frame, n):
    Fs, As = tensor_frame(frame, n)
    Ud = U.H
    imgs = [U * a * Ud for a in As]
    return sp.Matrix(len(Fs), len(As), lambda l, k: simp((Fs[l] * imgs[k]).trace()))


def is_perm(M):
    n = M.rows
    if any(not (x == 0 or x == 1) for x in M):
        return False
    return all(sum(M.row(i)) == 1 for i in range(n)) and all(sum(M.col(j)) == 1 for j in range(n))


def min_entry(M):
    vals = set(M)
    best = None
    for v in vals:
        if best is None or sp.simplify(v - best) < 0:
            best = v
    return best


# F1 -------------------------------------------------------------------------------------------
for nm, (F, A) in FRAMES.items():
    check(f"F1 {nm}: sum_l F_l = I and tr(F_l A_k) = delta_lk",
          is_zero(sum(F, sp.zeros(2)) - I2)
          and all(simp((F[l] * A[k]).trace()) == (1 if l == k else 0) for l in range(4) for k in range(4)))
check("F1 R1 reconstruction frame is orthogonal: tr(A_k A_l) = 2 delta_kl",
      all(simp((R1_A[k] * R1_A[l]).trace()) == (2 if k == l else 0) for k in range(4) for l in range(4)))
check("F1 SIC reconstruction frame is not orthogonal: tr(D_0 D_1) = -1",
      simp((SIC_D[0] * SIC_D[1]).trace()) == -1)
ev_R1 = [simp(e) for e in R1_F[0].eigenvals()]
ev_SIC = [simp(e) for e in SIC_E[0].eigenvals()]
check("F1 R1 coordinate functional F_0 has eigenvalue (1 - sqrt3)/4 < 0 (not PSD)",
      any(simp(e - (1 - s3) / 4) == 0 for e in ev_R1))
check("F1 SIC coordinate functionals E_l are PSD (eigenvalues 0 and 1/2)",
      all(sorted(simp(e) for e in E.eigenvals()) == [0, sp.Rational(1, 2)] for E in SIC_E))

# F2 -------------------------------------------------------------------------------------------
Hd = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
Sg = sp.Matrix([[1, 0], [0, sp.I]])


def canon(U):
    """Representative of U modulo global phase (first nonzero entry made positive real)."""
    for x in U:
        x = sp.simplify(x)
        if x != 0:
            ph = x / sp.Abs(x)
            return sp.Matrix(U.rows, U.cols, lambda i, j: sp.simplify(sp.expand(U[i, j] / ph)))
    raise ValueError


group = {}
frontier = [canon(I2)]
group[tuple(frontier[0])] = frontier[0]
while frontier:
    nxt = []
    for U in frontier:
        for G in (Hd, Sg):
            W = canon(G * U)
            key = tuple(W)
            if key not in group:
                group[key] = W
                nxt.append(W)
    frontier = nxt
cliff = list(group.values())
check("F2 the single-qubit Clifford group modulo phase has 24 elements", len(cliff) == 24)
same, perms, neg_half = True, 0, 0
for U in cliff:
    Mr = frame_matrix(U, FRAMES['R1'], 1)
    Ms = frame_matrix(U, FRAMES['SIC'], 1)
    if not is_zero(Mr - Ms):
        same = False
    if is_perm(Mr):
        perms += 1
    elif min_entry(Mr) == sp.Rational(-1, 2):
        neg_half += 1
check("F2 every single-qubit Clifford: frame matrix identical in R1 and SIC", same)
check("F2 12 Cliffords give permutation matrices; the other 12 have minimum entry exactly -1/2",
      perms == 12 and neg_half == 12)
check("F2 Hadamard and S are among the 12 with a -1/2 entry",
      min_entry(frame_matrix(Hd, FRAMES['R1'], 1)) == sp.Rational(-1, 2)
      and min_entry(frame_matrix(Sg, FRAMES['R1'], 1)) == sp.Rational(-1, 2))

# F3 -------------------------------------------------------------------------------------------
P0, P1 = sp.diag(1, 0), sp.diag(0, 1)
CX12 = kp(P0, I2) + kp(P1, X)
CX21 = kp(I2, P0) + kp(X, P1)
SWAP = sp.Matrix(4, 4, lambda i, j: 1 if (i, j) in [(0, 0), (1, 2), (2, 1), (3, 3)] else 0)
mins = {}
for cname, C in (('CNOT(1->2)', CX12), ('CNOT(2->1)', CX21)):
    Mr = frame_matrix(C, FRAMES['R1'], 2)
    Ms = frame_matrix(C, FRAMES['SIC'], 2)
    mr, ms = min_entry(Mr), min_entry(Ms)
    mins[cname] = (mr, ms)
    print(f"     {cname}: min entry R1 = {mr} ~ {float(mr):.10f}; SIC = {ms} ~ {float(ms):.10f}")
    check(f"F3 {cname}, R1 frame: minimum entry is exactly -1/4", simp(mr + sp.Rational(1, 4)) == 0)
    check(f"F3 {cname}, SIC frame: minimum entry is exactly 1/4 - sqrt3/3", simp(ms - (sp.Rational(1, 4) - s3 / 3)) == 0)
    check(f"F3 {cname}: R1 and SIC frame matrices differ", not is_zero(Mr - Ms))
check("F3 countercontrol: SWAP has the same frame matrix in both frames (a permutation)",
      is_zero(frame_matrix(SWAP, FRAMES['R1'], 2) - frame_matrix(SWAP, FRAMES['SIC'], 2))
      and is_perm(frame_matrix(SWAP, FRAMES['R1'], 2)))

# F4 -------------------------------------------------------------------------------------------
r = [-sp.Rational(c) / s3 for c in VZXY[0]]  # -v_0/sqrt3 in (<Z>, <X>, <Y>)
rho = (I2 + r[0] * Z + r[1] * X + r[2] * Y) / 2
check("F4 control: rho(-v_0/sqrt3) is a pure state (trace 1, det 0)",
      simp(rho.trace()) == 1 and simp(rho.det()) == 0)
c_r1 = simp((R1_F[0] * rho).trace())
c_sic = simp((SIC_E[0] * rho).trace())
print(f"     R1 coordinate mu_0 = {c_r1}; SIC coordinate p_0 = {c_sic}")
check("F4 that pure state has R1 coordinate (1 - sqrt3)/4 < 0 and SIC coordinate 0",
      simp(c_r1 - (1 - s3) / 4) == 0 and c_sic == 0)
phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
PHI = phi * phi.H
for nm in ('R1', 'SIC'):
    Fs, _ = tensor_frame(FRAMES[nm], 2)
    coords = [simp((f * PHI).trace()) for f in Fs]
    print(f"     Phi+ {nm} product-frame coordinates: min = {min_entry(sp.Matrix(coords))}; sum = {simp(sum(coords))}")
    if nm == 'R1':
        check("F4 Phi+: minimum R1 product-frame coordinate is exactly -1/8",
              min_entry(sp.Matrix(coords)) == sp.Rational(-1, 8) and simp(sum(coords)) == 1)
    else:
        check("F4 Phi+: every SIC product-frame coordinate is >= 0, minimum 0",
              min_entry(sp.Matrix(coords)) == 0 and simp(sum(coords)) == 1)

# F5 -------------------------------------------------------------------------------------------
# epsilon-robustness under R1: a represented state sigma has mu_l(sigma) >= 0, so for a state rho
# with coordinate c < 0 on functional F, Hoelder gives ||sigma - rho||_1 >= -c / ||F||_op.
F0 = R1_F[0]
op1 = max(abs(simp(e)) for e in F0.eigenvals())
F00 = kp(F0, F0)
op2 = max(abs(simp(e)) for e in F00.eigenvals())
bound1 = simp(-((1 - s3) / 4) / op1)
bound2 = simp(sp.Rational(1, 8) / op2)
print(f"     ||F_0||_op = {op1}; ||F_0 (x) F_0||_op = {op2}; trace-norm bounds {bound1}, {bound2}")
check("F5 ||F_0||_op = (1 + sqrt3)/4 and ||F_0 (x) F_0||_op = (2 + sqrt3)/8",
      simp(op1 - (1 + s3) / 4) == 0 and simp(op2 - (2 + s3) / 8) == 0)
# the Phi+ coordinate -1/8 is attained on some F_l (x) F_m; every product functional has the same norm
check("F5 every R1 product functional F_l (x) F_m has operator norm (2 + sqrt3)/8",
      all(simp(max(abs(simp(e)) for e in kp(R1_F[l], R1_F[m]).eigenvals()) - (2 + s3) / 8) == 0
          for l in range(4) for m in range(4)))
check("F5 both bounds equal 2 - sqrt3 > 0: ||sigma - rho||_1 >= 2 - sqrt3 (TD >= (2 - sqrt3)/2) for every"
      " R1-represented sigma, for rho = rho(-v_0/sqrt3) and for rho = Phi+",
      simp(bound1 - (2 - s3)) == 0 and simp(bound2 - (2 - s3)) == 0 and (2 - s3) > 0)

# controls -------------------------------------------------------------------------------------
for nm in ('R1', 'SIC'):
    check(f"control {nm}: identity channel -> 16x16 identity frame matrix",
          is_zero(frame_matrix(sp.eye(4), FRAMES[nm], 2) - sp.eye(16)))
    rot3 = (I2 - sp.I * (X + Y + Z)) / 2  # rotation by 2pi/3 about (1,1,1): an A4 element
    check(f"control {nm}: (A4 3-cycle rotation) (x) I -> permutation frame matrix",
          is_perm(frame_matrix(kp(rot3, I2), FRAMES[nm], 2)))
    A0 = FRAMES[nm][1][0]
    check(f"control {nm}: a point mass reconstructs a non-PSD operator (A_0 (x) A_0 has det < 0 factor)",
          simp(A0.det()) < 0)

print("RESULT " + ("ALL PASS" if not FAILS else f"{len(FAILS)} FAIL"))
sys.exit(1 if FAILS else 0)

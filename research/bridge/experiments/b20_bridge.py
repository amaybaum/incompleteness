#!/usr/bin/env python3
"""b20_bridge.py -- node B20 of research/bridge (round 5): the sufficient bridge in the owner's form. Exact checks of
the facts the design module `lean/BridgeOpDrive.lean` states, and of what K(Z_F) does with the bridge's two operations.
Exact arithmetic only (sympy over Q(i), sqrt(2) symbolic). The dictionary M(w) = (1/4) sum w[m][n] s_m (x) s_n and its
inverse coordOf(H)[m][n] = Re tr((s_m (x) s_n) H) are comparison tools, never premises. Tables act as in
CompositeDimension.lean (:198, :201): actT N w = w Nh^T, actC N w = Nh w, with Nh = 1 (+) N the homogenization.

DECISION RULE (fixed 2026-10-11T07:43:14Z, from `date -u` immediately before writing; before run 1).

K(Z_F) = (Q3 cap Z_F^*) + cone Z_F with the four defects D_s = I - 2 psi_s psi_s^*, psi_s = (1, ab, a, -b)/2 (the
exact data of rounds 1-3, as in b8_composition.py). A matrix y = phi phi^*/|phi|^2 is certified in K(Z_F) when it is
PSD and pairs nonnegatively with every defect (y in Q3 cap Z_F^* subset K); non-membership of X is certified only
through K = K^* [A]: a certified y with tr(y X) < 0.

CHECKS
  P1  zPh = diag(1, 3/5 + 4i/5) equals zPhase(3/5, 4/5) = diag(1, c + is) at (c, s) = (3/5, 4/5); uJ = (I - i(X+Y+Z))/2
      equals the literal cycMat; both unitary; w^4 = (-527 - 336 i)/625 != 1; bloch(zPh) = R_z(th0), bloch(uJ) = cyc.
  P2  On all 16 basis tables E: coordOf(Ad(I (x) zPh) M(E)) = actT R_z(th0) E and coordOf(Ad(I (x) uJ) M(E)) = actT cyc E
      (the two transfer identities `transferMap_zPh`, `transferMap_uJ`); and coordOf . M = id on the 16 tables.
  P3  K(Z_F) is moved by both operations on the target: for L = I (x) zPh and L = I (x) uJ, some defect D_s has
      Ad(L) D_s certified outside K(Z_F) by a certified y with tr(y Ad(L) D_s) < 0 (values printed). Q3 control: the
      same y pairs >= 0 with Ad(L)(psi_t psi_t^*) for every t.
  P4  R_z(th0) has infinite order: 2 cos th0 = 6/5 is rational and not an integer (so not an algebraic integer); and
      actT R_z(th0) and actT cyc do not commute on W 3 (a basis table where the two orders differ).
  P5  The membership step's matrix identity: for random Gaussian-rational U, n = 3 and c = 2 + 3i, the (0, 0) ancilla
      block of c (U (x) 1_n) is c U.

VERDICT B20-EXACT iff P1-P5 all PASS; otherwise VERDICT B20-FAILED followed by the failing ids.

Post-run edit after run 1 (2026-10-11T07:47Z; run 1 kept as b20_bridge.run1.*; rule text unchanged): run 1 failed P3 for
R_z(th0) only because the witness family searched (the images of the defects and their sums with Bell projectors, the
family of b8 X2 for the Cliffords) contains no certified witness for a frame-axis rotation; the family of b8 X3 -- the
Bell projectors rotated by the quarter phase on either token, (I (x) S) psi_t and (S (x) I) psi_t, and their
Hadamard-rotated analogues -- is added to the candidates. Its witness pairs with the image under R_z(c, s) on the target
to -s (B8 X3's flow law), -4/5 at (3/5, 4/5).
"""
import random
import sys

import sympy as sp

I = sp.I
random.seed(2005)
PASS, FAIL = [], []


def check(name, ok, msg):
    (PASS if ok else FAIL).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {msg}")


s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
kron = sp.kronecker_product
I2 = sp.eye(2)


def simp(M):
    return M.applyfunc(lambda z: sp.nsimplify(sp.expand(z)))


def dagger(M):
    return M.conjugate().T


def Mdict(w):
    out = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            if w[mu, nu] != 0:
                out += w[mu, nu] * kron(SIG[mu], SIG[nu])
    return out / 4


def coordOf(H):
    w = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            w[mu, nu] = sp.re(sp.nsimplify(sp.expand((kron(SIG[mu], SIG[nu]) * H).trace())))
    return w


def bloch(U):
    B = sp.zeros(3, 3)
    for j in range(3):
        for k in range(3):
            B[j, k] = sp.nsimplify(sp.expand((SIG[j + 1] * U * SIG[k + 1] * dagger(U)).trace() / 2))
    return B


def hom(N):
    Nh = sp.zeros(4, 4)
    Nh[0, 0] = 1
    Nh[1:, 1:] = N
    return Nh


def actT(N, w):
    return w * hom(N).T


def E(mu, nu):
    w = sp.zeros(4, 4)
    w[mu, nu] = 1
    return w


# ---------------- P1 ----------------
c0, s0_ = sp.Rational(3, 5), sp.Rational(4, 5)
w345 = c0 + I * s0_
zPh = sp.diag(1, w345)
zPhase = sp.diag(1, c0 + s0_ * I)
uJ = simp((I2 - I * (sx + sy + sz)) / 2)
cycMat = sp.Matrix([[(1 - I) / 2, (-1 - I) / 2], [(1 - I) / 2, (1 + I) / 2]])
Rz = sp.Matrix([[c0, -s0_, 0], [s0_, c0, 0], [0, 0, 1]])
CYC = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
w4 = sp.nsimplify(sp.expand(w345 ** 4))
p1 = (simp(zPh - zPhase) == sp.zeros(2, 2) and simp(uJ - cycMat) == sp.zeros(2, 2)
      and simp(dagger(zPh) * zPh) == I2 and simp(dagger(uJ) * uJ) == I2
      and w4 == sp.Rational(-527, 625) - sp.Rational(336, 625) * I and w4 != 1
      and bloch(zPh) == Rz and bloch(uJ) == CYC)
check("P1", p1, f"zPh = zPhase(3/5, 4/5), uJ = cycMat, both unitary; w^4 = {w4}; bloch(zPh) = R_z(th0), bloch(uJ) = cyc")

# ---------------- P2 ----------------
p2 = True
for mu in range(4):
    for nu in range(4):
        w = E(mu, nu)
        if coordOf(Mdict(w)) != w:
            p2 = False
        for U, N in ((zPh, Rz), (uJ, CYC)):
            L = kron(I2, U)
            lhs = coordOf(simp(L * Mdict(w) * dagger(L)))
            if lhs != actT(N, w):
                p2 = False
check("P2", p2, "coordOf . M = id, coordOf(Ad(I(x)zPh) M(E)) = actT R_z(th0) E and coordOf(Ad(I(x)uJ) M(E)) = actT cyc E "
      "on all 16 basis tables")

# ---------------- P3 ----------------
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
PSI = [sp.Matrix([1, a * b, a, -b]) / 2 for (a, b) in SIGNS]
for i in range(4):
    for j in range(4):
        assert sp.nsimplify((dagger(PSI[i]) * PSI[j])[0]) == (1 if i == j else 0)


def ov2(u, v):
    a = sp.expand((dagger(u) * v)[0])
    return sp.nsimplify(sp.expand(a * sp.conjugate(a)))


def norm2(u):
    return sp.nsimplify(sp.expand((dagger(u) * u)[0]))


def certified_member(phi):
    n2 = norm2(phi)
    return all(sp.nsimplify(1 - 2 * ov2(p, phi) / n2) >= 0 for p in PSI)


def pair_with_defect_image(phi, psi_img):
    return sp.nsimplify(1 - 2 * ov2(psi_img, phi) / norm2(phi))


S_GATE = sp.diag(1, I)
H_GATE = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)


def find_witness(imgs):
    cands = list(imgs)
    for s_ in range(4):
        for tt in range(4):
            for c in (1, -1, I, -I):
                cands.append(simp(imgs[s_] + c * PSI[tt]))
    # the witness family of b8 X3: Bell projectors rotated by the quarter phase or the Hadamard-conjugated
    # quarter phase, on either token
    for W in (S_GATE, H_GATE * S_GATE * H_GATE):
        for Wm in (W, dagger(W)):
            for Lw in (kron(I2, Wm), kron(Wm, I2)):
                for tt in range(4):
                    cands.append(simp(Lw * PSI[tt]))
    for phi in cands:
        if norm2(phi) == 0 or not certified_member(phi):
            continue
        for s_ in range(4):
            v = pair_with_defect_image(phi, imgs[s_])
            if v < 0:
                return phi, s_, v
    return None


p3 = True
report = []
for name, U in (("R_z(th0)", zPh), ("J", uJ)):
    L = kron(I2, U)
    imgs = [simp(L * p) for p in PSI]
    wit = find_witness(imgs)
    if wit is None:
        p3 = False
        report.append((name, None))
        continue
    phi, s_, v = wit
    # Q3 control: the same certified y pairs >= 0 with Ad(L)(psi_t psi_t^*) for every t
    ctl = all(sp.nsimplify(ov2(simp(L * p), phi) / norm2(phi)) >= 0 for p in PSI)
    p3 = p3 and ctl
    report.append((name, (s_, v, ctl, list(phi))))
check("P3", p3, "K(Z_F) moved on the target by both operations; certified witnesses and values: "
      + "; ".join(f"{nm}: defect {r[0]}, tr(y Ad D) = {r[1]}, Q3 control {r[2]}" if r else f"{nm}: none"
                  for nm, r in report))

# ---------------- P4 ----------------
tr_half = 2 * c0
not_alg_int = (tr_half.q != 1)
A = hom(Rz).T
B = hom(CYC).T
noncomm = None
for mu in range(4):
    for nu in range(4):
        w = E(mu, nu)
        if (w * A) * B != (w * B) * A:
            noncomm = (mu, nu)
            break
    if noncomm:
        break
p4 = not_alg_int and noncomm is not None
check("P4", p4, f"2 cos th0 = {tr_half} is not an integer (R_z(th0) of infinite order); actT R_z(th0) and actT cyc "
      f"disagree on the basis table E{noncomm}")

# ---------------- P5 ----------------
n = 3
U = sp.Matrix(2, 2, lambda i, j: random.randint(-3, 3) + I * random.randint(-3, 3))
c = 2 + 3 * I
K = c * kron(U, sp.eye(n))
# carrier Fin 2 x Fin n with linear index b*n + k; the (0, 0) ancilla block is K[(s, 0), (t, 0)]
blk = sp.Matrix(2, 2, lambda s, tt: K[s * n + 0, tt * n + 0])
p5 = simp(blk - c * U) == sp.zeros(2, 2)
check("P5", p5, "the (0, 0) ancilla block of c (U (x) 1_3) is c U (random Gaussian-rational U, c = 2 + 3i)")

print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
print("VERDICT B20-EXACT" if not FAIL else "VERDICT B20-FAILED " + " ".join(FAIL))
sys.exit(0)

"""Thread SS, probe P1 -- the uniform single-system countermodel family on eball d.

Read-only research against base 68b6df0651f14b2c8ab082635b8d2051918617a2. Exact arithmetic only
(sympy Rational / symbolic trigonometry); no float is used as evidence.

Question: do the single-system hypotheses of the d = 3 chain (K2Guard.three_of_nativeGateOf_of_two_le
minus its composite hypothesis NativeGateOf) and the rest of the landed single-system vocabulary hold on
eball d for d != 3?  One uniform instance, built only from kernel definitions:

    avail = fullEffects (eball d)          G = fullAut d          r = sharpEff e0
    z = e0                                 N = reflLin e0 (= diag(-1, 1, ..., 1))
    HasTwoSharpTests witness: e = sharpEff e0, f = sharpEff e1, x = e0
    drive (d >= 3): flow = rotation in the plane (0, 1), t0 = pi, J = cyclic permutation of axes 0, 1, 2

Sections
  A  sharp effects are effects on eball d (exact identity), certain/zero values, singleton certain face
  B  IsNot instance: involution, orthogonal (hence preserves eball d), flips z, unit z
  C  boundary transitivity witness (Householder e0 -> rational unit u) and seed transport = sharpEff u
  D  HasTwoSharpTests witness values (d >= 2)
  E  ElementaryDrivability instance for d >= 3; failure of the off-axis clause for every J in O(2) (d = 2)
  F  parity bookkeeping for a NOT on a flow (det +1) against DIM-1's balance and block bound

Run (from scratchpad/ss):  python3 -I p1_countermodel.py
"""
import sympy as sp
from sympy import Rational as R, Matrix, eye, zeros, cos, sin, pi, symbols

CHECKS = []


def check(name, cond):
    cond = bool(cond)
    CHECKS.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


def note(msg):
    print("NOTE " + msg)


def iszero(M):
    return all(sp.simplify(sp.expand_trig(sp.expand(z))) == 0 for z in M)


def e(d, i):
    v = zeros(d, 1)
    v[i] = 1
    return v


def sharp(b, x):
    """sharpEff b x = 1/2 + sum_j b_j/2 * x_j  (EffectSpace.lean:67)."""
    return R(1, 2) + (b.T * x)[0] / 2


def refl(m):
    """reflLin m (EffectSpace.lean:233) as a matrix: I - 2 m m^T / (m^T m)."""
    d = m.shape[0]
    return eye(d) - 2 * (m * m.T) / (m.T * m)[0]


# rational unit vectors used as boundary-transitivity targets
UNIT = {
    1: Matrix([-1]),
    2: Matrix([R(3, 5), R(4, 5)]),
    3: Matrix([R(1, 3), R(2, 3), R(2, 3)]),
    4: Matrix([R(1, 2), R(1, 2), R(1, 2), R(1, 2)]),
    5: Matrix([R(2, 7), R(3, 7), R(6, 7), 0, 0]),
    7: Matrix([R(1, 2), R(1, 2), R(1, 2), 0, 0, 0, R(1, 2)]),
}

t, s = symbols("t s", real=True)
DIMS = [1, 2, 3, 4, 5, 7]

for d in DIMS:
    print("=== d = %d" % d)
    xs = Matrix(symbols("x0:%d" % d, real=True))
    bs = Matrix(symbols("b0:%d" % d, real=True))
    nx2 = (xs.T * xs)[0]
    nb2 = (bs.T * bs)[0]
    # ---- A: sharpEff b is an effect on eball d when |b| = 1:
    #   1 - sharpEff b x = (|b - x|^2 + 1 - |x|^2)/4 ,  sharpEff b x = (|b + x|^2 + 1 - |x|^2)/4
    # both right sides are >= 0 on |x|^2 <= 1.  Identities checked with |b|^2 = 1 substituted.
    lhs1 = 1 - sharp(bs, xs)
    rhs1 = (((bs - xs).T * (bs - xs))[0] + 1 - nx2) / 4
    lhs2 = sharp(bs, xs)
    rhs2 = (((bs + xs).T * (bs + xs))[0] + 1 - nx2) / 4
    check("A1 d=%d upper identity  1 - sharpEff b x = (|b-x|^2 + 1 - |x|^2)/4  (given |b|^2=1)" % d,
          sp.expand(lhs1 - rhs1 + (nb2 - 1) / 4) == 0)
    check("A2 d=%d lower identity  sharpEff b x = (|b+x|^2 + 1 - |x|^2)/4  (given |b|^2=1)" % d,
          sp.expand(lhs2 - rhs2 + (nb2 - 1) / 4) == 0)
    # singleton certain face: sharpEff u x = 1 with |u| = 1, |x| <= 1 forces |x - u|^2 = |x|^2 - 1 <= 0
    check("A3 d=%d certain face identity  |x-u|^2 = |x|^2 - 1 + 4(1 - sharpEff u x)  (given |u|^2=1)" % d,
          sp.expand(((xs - bs).T * (xs - bs))[0] - (nx2 - 1 + 4 * (1 - sharp(bs, xs))) - (nb2 - 1)) == 0)
    z = e(d, 0)
    check("A4 d=%d seed r = sharpEff e0: r(e0) = 1, r(-e0) = 0" % d,
          sharp(z, z) == 1 and sharp(z, -z) == 0)
    # ---- B: IsNot instance N = reflLin e0
    N = refl(z)
    check("B1 d=%d N = reflLin e0 is diag(-1,1,...,1)" % d,
          N == sp.diag(*([-1] + [1] * (d - 1))))
    check("B2 d=%d N involutive" % d, N * N == eye(d))
    check("B3 d=%d N orthogonal (sum of squares preserved, so N maps eball d into itself)" % d,
          N.T * N == eye(d))
    check("B4 d=%d N flips z = e0 and z is a unit vector" % d, N * z == -z and (z.T * z)[0] == 1)
    note("d=%d det N = %s (a reflection: not on any flow)" % (d, N.det()))
    # ---- C: boundary transitivity witness and seed transport
    u = UNIT[d]
    check("C1 d=%d target u is a unit vector" % d, (u.T * u)[0] == 1)
    H = refl(z - u)
    check("C2 d=%d Householder reflLin (e0 - u) is orthogonal and maps e0 to u" % d,
          H.T * H == eye(d) and H * z == u)
    # seed transport r o H^{-1}: x |-> sharpEff e0 (H^{-1} x) = sharpEff (H e0) x since H^{-1} = H^T
    check("C3 d=%d seedTransport (sharpEff e0) H = sharpEff u  (coefficientwise)" % d,
          sp.expand(sharp(z, H.inv() * xs) - sharp(u, xs)) == 0)
    # ---- D: HasTwoSharpTests witness (SharpTests.lean:137 in the K1-SHARP-TESTS worktree)
    if d >= 2:
        f1 = e(d, 1)
        ev, fv = sharp(z, z), sharp(f1, z)
        check("D1 d=%d two sharp tests: at x = e0, e = %s, f = %s, 1 - e = %s; f != e and f != 1 - e"
              % (d, ev, fv, 1 - ev), ev == 1 and fv == R(1, 2) and fv != ev and fv != 1 - ev)
    else:
        note("d=1: HasTwoSharpTests fails (kernel not_hasTwoSharpTests_one, SharpTests.lean:107)")
    # ---- E: drivability
    if d >= 3:
        def Rot(th):
            M = eye(d)
            M[0, 0], M[0, 1], M[1, 0], M[1, 1] = cos(th), -sin(th), sin(th), cos(th)
            return M
        check("E1 d=%d flow law Rot(s) Rot(t) = Rot(s + t) (symbolic)" % d,
              iszero(Rot(s) * Rot(t) - Rot(s + t)))
        check("E2 d=%d flow members orthogonal (symbolic t)" % d, iszero(Rot(t).T * Rot(t) - eye(d)))
        Npi = Rot(pi)
        check("E3 d=%d N := flow(pi) = diag(-1,-1,1,...), involutive, moves e0" % d,
              Npi == sp.diag(*([-1, -1] + [1] * (d - 2))) and Npi * Npi == eye(d) and Npi * z != z)
        J = zeros(d, d)                     # cyc3 on axes 0,1,2: (v0,v1,v2) -> (v2,v0,v1); identity beyond
        J[0, 2], J[1, 0], J[2, 1] = 1, 1, 1
        for k in range(3, d):
            J[k, k] = 1
        e2 = e(d, 2)
        conj = J * Npi * J.inv()
        check("E4 d=%d J orthogonal (body automorphism) and J N J^-1 e2 = -e2 while Rot(s) e2 = e2 for all s"
              % d, J.T * J == eye(d) and conj * e2 == -e2 and iszero(Rot(s) * e2 - e2))
    elif d == 2:
        a = symbols("a", real=True)
        def Rot2(th):
            return Matrix([[cos(th), -sin(th)], [sin(th), cos(th)]])
        F = sp.diag(1, -1)
        okp = iszero(Rot2(a) * Rot2(t) * Rot2(a).inv() - Rot2(t))
        okm = iszero((Rot2(a) * F) * Rot2(t) * (Rot2(a) * F).inv() - Rot2(-t))
        check("E5 d=2 every J in O(2) conjugates the rotation flow into the flow: "
              "R(a) R(t) R(a)^-1 = R(t), (R(a)F) R(t) (R(a)F)^-1 = R(-t)", okp and okm)
        note("d=2: with Aut(eball 2) = O(2) (written: centroid fixed, sum of squares preserved) and every "
             "flow a rotation flow, the off-axis clause J_off_axis fails; eball 2 is not drivable (written).")
    else:
        note("d=1: not drivable (kernel not_drivable_Icc, KInfFoundations.lean:529, for Icc(-1,1) = eball 1 "
             "up to the identification Fin 1 -> R; transport to eball 1 written)")

# ---- F: parity bookkeeping (exact enumeration)
print("=== F")
rows = []
for d in range(1, 16):
    # homogenized split of an involution N with m tangent eigenvalues -1: p_hom = 1 + (d - m), m_hom = m
    bal = [m for m in range(0, d + 1) if 1 + (d - m) == m]          # DIM-1 parity balance
    blk = [m for m in bal if (d - m) <= 1]                           # DIM-1 block bound p_tan <= 1
    flow = [m for m in blk if m % 2 == 0]                            # det N = (-1)^m = +1 (N on a flow)
    rows.append((d, bal, blk, flow))
    print("F d=%2d balanced m=%s  +block m=%s  +det(N)=+1 m=%s" % (d, bal, blk, flow))
check("F1 balance alone: d odd exactly", all((len(r[1]) > 0) == (r[0] % 2 == 1) for r in rows))
check("F2 balance + det(N)=+1 (NOT on a flow): d = 3 mod 4 exactly",
      all((len([m for m in r[1] if m % 2 == 0]) > 0) == (r[0] % 4 == 3) for r in rows))
check("F3 balance + block bound: d in {1, 3}", [r[0] for r in rows if r[2]] == [1, 3])
check("F4 balance + block bound + det(N)=+1: d = 3 only", [r[0] for r in rows if r[3]] == [3])

fails = [n for n, c in CHECKS if not c]
print("SUMMARY %d checks, %d failed" % (len(CHECKS), len(fails)))
print("VERDICT " + ("RENDERED: every listed single-system item holds at each tested d (drivability for d >= 3 "
                    "only); see ledger" if not fails else "NOT RENDERED (a control failed)"))

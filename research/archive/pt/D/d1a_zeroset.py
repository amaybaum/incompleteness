#!/usr/bin/env python3
"""Thread D, certified script d1a -- the zero-set lemma (step 7 of the N-CLASS route, RESULT.md section 1, D1.1).

Setting (DIM-1 conventions, CompositeDimension.lean): HVec 3 = R^4 with index 0 the unit, 1..3 the ball coordinates.
For a 4x4 real matrix A, the bilinear form is beta_A(b, Y) = b^T A Y. For an orthogonal R1 with R1 z3 = -z3 put
  Z1 = {((1, n), (1, -n)) : |n| = 1}             (the pairs with <b, Y> = 0, b and Y on the null cone)
  Z2 = {((1, n), (1, -R1^T n)) : |n| = 1}        (the pairs with <b, homMap(R1) Y> = 0).
S is the matrix of Y -> (Y1, Y0, 0, 0); T is the matrix of Y -> (0, 0, -Y3, Y2).

Written criterion (W0), used by every check below: a polynomial f(n) of degree <= 2 vanishes on the unit sphere iff its
odd part f1 is the zero polynomial and f2(n) + f0 |n|^2 is the zero polynomial (f = f0 + f1 + f2 by degree). Proof:
f(n) - f(-n) = 2 f1(n) vanishes on the sphere and is linear, so f1 = 0; f(n) + f(-n) = 2(f0 + f2(n)) vanishes on the
sphere, and f2(n) + f0 |n|^2 is a homogeneous quadratic vanishing on the sphere, hence everywhere.

DECISION RULES (fixed before the first run; stated as rules, not expected numbers):
  R-Z1  The solution space of "beta_A vanishes on Z1" must coincide with the normal-form space
        NF = {[[a, c^T], [c, a I + K]] : a real, c in R^3, K antisymmetric}: every nullspace basis vector must lie in NF
        and every NF element must satisfy the conditions identically (symbolic a, c, K), with equal dimensions.
  R-Z2  For R1 = nflip (DIM-1's NOT, a rotation by pi): the solution space for Z1 and Z2 together must be exactly
        span{S, T}: S and T satisfy all conditions, and the nullspace dimension equals 2.
  R-Z3  For improper R1 = diag(Rot(cc, ss), -1) with symbolic cc, ss (cc^2 + ss^2 = 1): substituting NF into the Z2
        conditions must yield, as exact polynomial identities, equations forcing c3 = 0 and a = 0, and a linear system
        in the two entries A[1,3], A[2,3] whose determinant is congruent to 2(1 + cc) modulo cc^2 + ss^2 - 1. Then for
        cc != -1 every solution has zero column 3.
  R-Z4  For R1 = -I (the only improper case with cc = -1): every solution must have zero column 0.
  R-S   Sample check: every solution form found in R-Z2 and R-Z4 and the improper rational case must vanish exactly at
        every listed rational point of Z1 and Z2 (Pythagorean quadruples).
  Countercontrols (each must give the opposite verdict to the corresponding favourable check):
  CC1   the span{S, T} forms must NOT all kill Y3 and must NOT all kill Y0 (the improper exclusion does not apply to
        the proper case);
  CC2   dropping Z2 must leave a solution space strictly larger than span{S, T};
  CC3   S must NOT vanish at the pair ((1,1,0,0), (1,1,0,0)), which lies off Z1 and Z2;
  CC4   the criterion W0 must reject f = n1 and accept f = |n|^2 - 1;
  CC5   for the proper rotation by pi about (3/5, 4/5, 0) the forms must NOT all kill Y3.
  A VERDICT line is printed only if every check passes and every countercontrol behaves as stated.
Exact arithmetic only (sympy, rationals). No floating point, no randomness, no timing in stdout.
"""
import sys
import sympy as sp

CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


n = sp.symbols('n1:4', real=True)
NN = n[0] ** 2 + n[1] ** 2 + n[2] ** 2
Asym = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'a{i}{j}', real=True))
AV = list(Asym)


def split_conditions(f):
    """W0: return the polynomial coefficient equations of the odd part and of the homogenized even part."""
    f = sp.expand(f)
    if f == 0:
        return []
    P = sp.Poly(f, *n)
    parts = {0: sp.Integer(0), 1: sp.Integer(0), 2: sp.Integer(0)}
    for mon, cf in zip(P.monoms(), P.coeffs()):
        deg = sum(mon)
        assert deg <= 2
        parts[deg] += cf * sp.prod([n[i] ** mon[i] for i in range(3)])
    eqs = []
    for g in (parts[1], sp.expand(parts[2] + parts[0] * NN)):
        if g != 0:
            eqs += list(sp.Poly(g, *n).coeffs())
    return eqs


def vanishes_on_sphere(f):
    return all(sp.expand(e) == 0 for e in split_conditions(f))


def form_on(A, bvec, Yvec):
    return (sp.Matrix(bvec).T * A * sp.Matrix(Yvec))[0, 0]


def z1_pair():
    return [1] + list(n), [1] + [-v for v in n]


def z2_pair(R1):
    m = -(sp.Matrix(R1).T * sp.Matrix(n))
    return [1] + list(n), [1] + list(m)


def solution_space(R1=None):
    b1, Y1 = z1_pair()
    eqs = split_conditions(form_on(Asym, b1, Y1))
    if R1 is not None:
        b2, Y2 = z2_pair(R1)
        eqs += split_conditions(form_on(Asym, b2, Y2))
    M = sp.Matrix([[sp.diff(e, v) for v in AV] for e in eqs])
    return [sp.Matrix(4, 4, list(v)) for v in M.nullspace()]


Smat = sp.zeros(4, 4); Smat[0, 1] = 1; Smat[1, 0] = 1
Tmat = sp.zeros(4, 4); Tmat[2, 3] = -1; Tmat[3, 2] = 1
NFLIP = sp.diag(1, -1, -1)


def in_span(Ms, basis):
    """Every matrix in Ms is a linear combination of basis (exact)."""
    B = sp.Matrix([list(X) for X in basis]).T
    for X in Ms:
        v = sp.Matrix(list(X))
        if B.rank() != B.row_join(v).rank():
            return False
    return True


# Pythagorean quadruples give rational points of the unit sphere.
QUADS = [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11), (6, 6, 7, 11), (3, 4, 12, 13), (2, 10, 11, 15),
         (1, 12, 12, 17), (8, 9, 12, 17), (6, 13, 18, 23)]
SPHERE_PTS = []
for (p, q, r, d) in QUADS:
    for perm in ((p, q, r), (q, r, p), (r, p, q)):
        for sg in ((1, 1, 1), (1, -1, 1), (-1, 1, -1), (1, 1, -1)):
            SPHERE_PTS.append(tuple(sp.Rational(sg[k] * perm[k], d) for k in range(3)))


def sample_vanish(forms, R1):
    for pt in SPHERE_PTS:
        nv = sp.Matrix(pt)
        b = [1] + list(pt)
        Y1 = [1] + [-v for v in pt]
        Y2 = [1] + list(-(sp.Matrix(R1).T * nv))
        for A in forms:
            if form_on(A, b, Y1) != 0 or form_on(A, b, Y2) != 0:
                return False
    return True


print('== CC4  the criterion W0 on two control polynomials')
chk('CC4a', 'countercontrol: W0 rejects f = n1 (does not vanish on the sphere)', not vanishes_on_sphere(n[0]),
    'countercontrol')
chk('CC4b', 'control: W0 accepts f = |n|^2 - 1', vanishes_on_sphere(NN - 1), 'identity')

print()
print('== R-Z1  forms vanishing on Z1')
asc, c1, c2, c3, kxy, kxz, kyz = sp.symbols('a_ c1 c2 c3 kxy kxz kyz', real=True)
Kmat = sp.Matrix([[0, kxy, kxz], [-kxy, 0, kyz], [-kxz, -kyz, 0]])
NFsym = sp.zeros(4, 4)
NFsym[0, 0] = asc
NFsym[0, 1:4] = sp.Matrix([[c1, c2, c3]])
NFsym[1:4, 0] = sp.Matrix([c1, c2, c3])
NFsym[1:4, 1:4] = asc * sp.eye(3) + Kmat
b1, Y1 = z1_pair()
chk('Z1.a', 'every normal-form matrix [[a, c^T], [c, aI + K]] (symbolic a, c, K) vanishes on Z1 (W0)',
    vanishes_on_sphere(form_on(NFsym, b1, Y1)), 'identity')
sol1 = solution_space(None)
NFbasis = [NFsym.subs({v: (1 if v == w else 0) for v in (asc, c1, c2, c3, kxy, kxz, kyz)})
           for w in (asc, c1, c2, c3, kxy, kxz, kyz)]
chk('Z1.b', f'the Z1 solution space has dimension {len(sol1)} and coincides with the 7-dimensional normal-form space',
    len(sol1) == 7 and in_span(sol1, NFbasis) and in_span(NFbasis, sol1), 'enumerate')

print()
print('== R-Z2  proper case R1 = nflip')
sol_n = solution_space(NFLIP)
b2, Y2 = z2_pair(NFLIP)
chk('Z2.a', 'S and T vanish on Z1 and on Z2(nflip) (W0, symbolic n)',
    all(vanishes_on_sphere(form_on(X, b1, Y1)) and vanishes_on_sphere(form_on(X, b2, Y2)) for X in (Smat, Tmat)),
    'identity')
chk('Z2.b', f'the Z1 + Z2(nflip) solution space has dimension {len(sol_n)} = 2 and equals span{{S, T}}',
    len(sol_n) == 2 and in_span(sol_n, [Smat, Tmat]) and in_span([Smat, Tmat], sol_n), 'enumerate')
chk('Z2.s', 'sample: S and T vanish at 120 rational points of Z1 and Z2(nflip)', sample_vanish([Smat, Tmat], NFLIP),
    'sample')
chk('CC1', 'countercontrol: the span{S,T} forms do not all kill Y3 and do not all kill Y0 (improper exclusion '
    'does not apply)', not all(X[i, 3] == 0 for X in (Smat, Tmat) for i in range(4))
    and not all(X[i, 0] == 0 for X in (Smat, Tmat) for i in range(4)), 'countercontrol')
chk('CC2', f'countercontrol: dropping Z2 leaves a space of dimension {len(sol1)} > 2', len(sol1) > 2, 'countercontrol')
chk('CC3', 'countercontrol: S does not vanish at ((1,1,0,0), (1,1,0,0)) (off Z1, Z2): value '
    f'{form_on(Smat, [1, 1, 0, 0], [1, 1, 0, 0])}', form_on(Smat, [1, 1, 0, 0], [1, 1, 0, 0]) != 0, 'countercontrol')

print()
print('== R-Z3  improper case R1 = diag(Rot(cc, ss), -1), symbolic cc, ss')
cc, ss = sp.symbols('cc ss', real=True)
R1imp = sp.Matrix([[cc, -ss, 0], [ss, cc, 0], [0, 0, -1]])
chk('Z3.0', 'R1 = diag(Rot, -1) is orthogonal modulo cc^2 + ss^2 = 1, has determinant -(cc^2 + ss^2), maps z3 to -z3',
    sp.expand((R1imp.T * R1imp - sp.eye(3)).subs(ss ** 2, 1 - cc ** 2)) == sp.zeros(3, 3)
    and sp.expand(R1imp.det() + cc ** 2 + ss ** 2) == 0 and R1imp * sp.Matrix([0, 0, 1]) == sp.Matrix([0, 0, -1]),
    'identity')
b2i, Y2i = z2_pair(R1imp)
f2 = sp.expand(form_on(NFsym, b2i, Y2i))
P2 = sp.Poly(f2, *n)
odd = sum((cf * sp.prod([n[i] ** m[i] for i in range(3)]) for m, cf in zip(P2.monoms(), P2.coeffs()) if sum(m) == 1),
          sp.Integer(0))
f0 = sum((cf for m, cf in zip(P2.monoms(), P2.coeffs()) if sum(m) == 0), sp.Integer(0))
ev2 = sum((cf * sp.prod([n[i] ** m[i] for i in range(3)]) for m, cf in zip(P2.monoms(), P2.coeffs()) if sum(m) == 2),
          sp.Integer(0))
even_h = sp.expand(ev2 + f0 * NN)
odd_n3 = sp.Poly(odd, *n).coeff_monomial(n[2]) if odd != 0 else 0
even_n3n3 = sp.Poly(even_h, *n).coeff_monomial(n[2] ** 2)
even_n1n3 = sp.Poly(even_h, *n).coeff_monomial(n[0] * n[2])
even_n2n3 = sp.Poly(even_h, *n).coeff_monomial(n[1] * n[2])
print(f'   odd coefficient of n3: {sp.factor(odd_n3)}')
print(f'   even (homogenized) coefficient of n3^2: {sp.factor(even_n3n3)}')
print(f'   even coefficient of n1 n3: {sp.expand(even_n1n3)}')
print(f'   even coefficient of n2 n3: {sp.expand(even_n2n3)}')
chk('Z3.a', 'the odd n3-coefficient of the Z2 condition is a nonzero constant multiple of c3 (forces c3 = 0)',
    sp.expand(odd_n3) != 0 and sp.simplify(odd_n3 / c3).is_constant() and sp.simplify(odd_n3 / c3) != 0, 'identity')
chk('Z3.b', 'the even n3^2-coefficient is a nonzero constant multiple of a (forces a = 0)',
    sp.expand(even_n3n3) != 0 and sp.simplify(even_n3n3 / asc).is_constant() and sp.simplify(even_n3n3 / asc) != 0,
    'identity')
lin = sp.Matrix([[sp.diff(even_n1n3, kxz), sp.diff(even_n1n3, kyz)], [sp.diff(even_n2n3, kxz), sp.diff(even_n2n3, kyz)]])
rest_free = all(sp.expand(e - sp.diff(e, kxz) * kxz - sp.diff(e, kyz) * kyz) == 0 for e in (even_n1n3, even_n2n3))
detlin = sp.expand(lin.det())
print(f'   the (A[1,3], A[2,3]) system matrix: {lin.tolist()}, determinant {detlin}')
chk('Z3.c', 'the n1n3 and n2n3 coefficients involve only A[1,3] = kxz and A[2,3] = kyz, and their system determinant is '
    'congruent to 2(1 + cc) modulo cc^2 + ss^2 - 1',
    rest_free and sp.expand(detlin.subs(ss ** 2, 1 - cc ** 2) - 2 * (1 + cc)) == 0, 'identity')
col3 = [NFsym[i, 3] for i in range(4)]
chk('Z3.d', 'column 3 of the normal form is (c3, kxz, kyz, a): with Z3.a-c every solution has zero column 3 when '
    'cc != -1', col3 == [c3, kxz, kyz, asc], 'identity')
R1rat = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, -1]])
sol_rat = solution_space(R1rat)
sol_d = solution_space(sp.diag(1, 1, -1))
chk('Z3.e', f'instances: R1 = diag(Rot(3/5, 4/5), -1) has solution dimension {len(sol_rat)}; R1 = diag(1, 1, -1) '
    f'has dimension {len(sol_d)}; every solution of both kills Y3',
    all(X[i, 3] == 0 for X in sol_rat + sol_d for i in range(4)), 'enumerate')
chk('Z3.s', 'sample: the diag(1, 1, -1) solutions vanish at 120 rational points of Z1 and Z2',
    sample_vanish(sol_d, sp.diag(1, 1, -1)), 'sample')
w = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5), 0])
Rax = 2 * w * w.T - sp.eye(3)
sol_ax = solution_space(Rax)
chk('CC5', f'countercontrol: proper rotation by pi about (3/5, 4/5, 0): dimension {len(sol_ax)}, and its forms do '
    'NOT all kill Y3', not all(X[i, 3] == 0 for X in sol_ax for i in range(4)), 'countercontrol')

print()
print('== R-Z4  improper case R1 = -I (cc = -1)')
sol_m = solution_space(-sp.eye(3))
chk('Z4.a', f'R1 = -I: solution dimension {len(sol_m)}; every solution has zero column 0 (kills Y0)',
    all(X[i, 0] == 0 for X in sol_m for i in range(4)), 'enumerate')
chk('Z4.s', 'sample: the R1 = -I solutions vanish at 120 rational points of Z1 and Z2', sample_vanish(sol_m, -sp.eye(3)),
    'sample')

print()
fails = [c for c, k, ok in CHECKS if not ok]
print(f'd1a_zeroset: {len(CHECKS)} checks, {len(fails)} failed')
if not fails:
    print('VERDICT ZEROSET-LEMMA-EXACT: proper M1 = nflip gives exactly span{S, T}; every improper M1 gives forms '
          'that kill Y3 (cc != -1) or Y0 (R1 = -I)')
    sys.exit(0)
print('NO VERDICT: failed checks ' + ', '.join(fails))
sys.exit(1)

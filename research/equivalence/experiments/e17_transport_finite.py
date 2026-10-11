"""E17 probe -- the finite-stage case of the transport form of H-DYN (exact: integers and Gaussian rationals).

Written 2026-10-11T04:05Z (date -u read at 04:03:56Z for NOTES-E17 S0), after NOTES-E17 S0 and before the first run.

SETTING.  A stage is the matrix algebra over a finite configuration set C = {0, ..., n-1}; E_cc' is its matrix unit.
A matrix is {0,1} when every entry is 0 or 1.  A star automorphism of M_n is Ad(U): X -> U X U^dagger, U unitary.
Gaussian rationals are pairs (re, im) of Fractions; {0,1} means the entry is exactly (0, 0) or (1, 0).

CHECKS.
  Z1  lemma (a): for n = 1 .. 4, among all 2^(n^2) {0,1} matrices the symmetric idempotent ones (P = P^T, P P = P; for a
      {0,1} matrix self-adjoint means symmetric) are exactly the 2^n diagonal {0,1} matrices.
  Z2  lemma (b) with its row companion: for n = 1 .. 4, the {0,1} matrices V with V^T V idempotent are exactly the
      partial permutation matrices (at most one 1 in each row and in each column), counted 2, 7, 34, 209
      (sum_k C(n,k)^2 k!); and the diagonal of V^T V is the vector of column counts.
  Z3  lemma (c) on instances: for n = 2, 3 and every monomial unitary U = D P (D diagonal with entries in {1, i, -1, -i},
      P the permutation matrix of p, P e_c = e_p(c)), Ad(U) maps every matrix unit to a {0,1} matrix iff D is scalar
      (8 of 32 at n = 2, 24 of 384 at n = 3), and then Ad(U)(E_cc') = E_{p(c) p(c')} for all c, c'.
  Z4  non-monomial unitaries fail at a diagonal unit: the Hadamard matrix (H' = [[1, 1], [1, -1]], H = H'/sqrt 2, so
      Ad(H)(X) = H' X H'^T / 2 exactly) and the rotation R = [[3/5, -4/5], [4/5, 3/5]]; both are unitary (H' H'^T = 2 I,
      R R^T = I) and Ad(U)(E_00) is not {0,1}.
  Z5  positive control at the stage level: for the CNOT update phi(x) = (x0, x0 + x1, x2) (mod 2) on three sites, with
      P_phi the permutation matrix of phi on the top stage (8 configurations), the transport P_phi E P_phi^T of every
      matrix unit E of every non-empty stage (the operator sum_y |c y><c' y|) is a {0,1} matrix; the transport of the
      site-0 unit E^{0}_{0,1} is no matrix unit of any stage (the hypothesis admits interacting dynamics).
COUNTERCONTROLS (each must fail as stated).
  XZ1 "every idempotent {0,1} matrix is diagonal" (self-adjointness dropped from lemma (a)).
  XZ2 "Ad(diag(1, i)) maps every matrix unit of M_2 to a {0,1} matrix" (the phase automorphism).
  XZ3 "a {0,1} matrix whose column sums are at most one has V^T V idempotent".

DECISION RULE (fixed before the first run).  VERDICT E17-TRANSPORT-FINITE-CONSISTENT iff Z1 ... Z5 all pass and XZ1,
XZ2, XZ3 all fail as stated; otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says that the
instances agree with lemmas (a)-(c); the general statements are the design module's (NOTES-E17).
"""
import itertools
from fractions import Fraction as Fr

RESULTS = []
COUNTERS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


def counter(name, claim_holds, detail=''):
    COUNTERS.append((name, not claim_holds))
    print('COUNTER ' + name + (' fails as stated' if not claim_holds else ' HOLDS (unexpected)') +
          ((' -- ' + detail) if detail else ''), flush=True)


# ---------------------------------------------------------------- integer {0,1} matrices
def int_mats(n):
    for bits in itertools.product((0, 1), repeat=n * n):
        yield tuple(tuple(bits[i * n:(i + 1) * n]) for i in range(n))


def imul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return tuple(tuple(sum(A[i][l] * B[l][j] for l in range(k)) for j in range(m)) for i in range(n))


def itr(A):
    return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))


def is_diag(A):
    return all(A[i][j] == 0 for i in range(len(A)) for j in range(len(A)) if i != j)


def is_partial_perm(A):
    n = len(A)
    return (all(sum(A[i]) <= 1 for i in range(n)) and
            all(sum(A[i][j] for i in range(n)) <= 1 for j in range(n)))


def binom(n, k):
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out


def fact(k):
    out = 1
    for i in range(2, k + 1):
        out *= i
    return out


# ---------------------------------------------------------------- Z1
z1_ok, z1_detail = True, []
for n in range(1, 5):
    sym_idem = [P for P in int_mats(n) if P == itr(P) and imul(P, P) == P]
    ok = len(sym_idem) == 2 ** n and all(is_diag(P) for P in sym_idem)
    z1_ok = z1_ok and ok
    z1_detail.append('n=%d: %d symmetric idempotent, all diagonal: %s' % (n, len(sym_idem), all(is_diag(P) for P in sym_idem)))
check('Z1', z1_ok, '; '.join(z1_detail))

# ---------------------------------------------------------------- Z2
z2_ok, z2_detail = True, []
for n in range(1, 5):
    count_idem, count_pp, agree, diag_counts = 0, 0, True, True
    for V in int_mats(n):
        G = imul(itr(V), V)
        idem = imul(G, G) == G
        pp = is_partial_perm(V)
        count_idem += idem
        count_pp += pp
        if idem != pp:
            agree = False
        if any(G[j][j] != sum(V[i][j] for i in range(n)) for j in range(n)):
            diag_counts = False
    formula = sum(binom(n, k) ** 2 * fact(k) for k in range(n + 1))
    ok = agree and diag_counts and count_idem == count_pp == formula
    z2_ok = z2_ok and ok
    z2_detail.append('n=%d: %d with V^T V idempotent, %d partial permutations, formula %d' % (n, count_idem, count_pp, formula))
check('Z2', z2_ok, '; '.join(z2_detail) + '; column counts on the diagonal: checked')

# ---------------------------------------------------------------- Gaussian rationals
ZERO = (Fr(0), Fr(0))
ONE = (Fr(1), Fr(0))
IU = (Fr(0), Fr(1))


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gconj(a):
    return (a[0], -a[1])


def gscale(r, a):
    return (r * a[0], r * a[1])


def gmat_mul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            s = ZERO
            for l in range(k):
                s = gadd(s, gmul(A[i][l], B[l][j]))
            row.append(s)
        out.append(tuple(row))
    return tuple(out)


def dagger(A):
    return tuple(tuple(gconj(A[j][i]) for j in range(len(A))) for i in range(len(A[0])))


def gunit(n, c, cp):
    return tuple(tuple(ONE if (i == c and j == cp) else ZERO for j in range(n)) for i in range(n))


def ad(U, X):
    return gmat_mul(gmat_mul(U, X), dagger(U))


def is01(M):
    return all(x == ZERO or x == ONE for row in M for x in row)


PHASES = [ONE, IU, (Fr(-1), Fr(0)), (Fr(0), Fr(-1))]

# ---------------------------------------------------------------- Z3
z3_ok, z3_detail = True, []
for n in (2, 3):
    total, passing, iff_ok, transport_ok = 0, 0, True, True
    for p in itertools.permutations(range(n)):
        P = tuple(tuple(ONE if i == p[c] else ZERO for c in range(n)) for i in range(n))
        for d in itertools.product(PHASES, repeat=n):
            D = tuple(tuple(d[i] if i == j else ZERO for j in range(n)) for i in range(n))
            U = gmat_mul(D, P)
            total += 1
            ok01 = all(is01(ad(U, gunit(n, c, cp))) for c in range(n) for cp in range(n))
            scalar = all(x == d[0] for x in d)
            if ok01 != scalar:
                iff_ok = False
            if ok01:
                passing += 1
                for c in range(n):
                    for cp in range(n):
                        if ad(U, gunit(n, c, cp)) != gunit(n, p[c], p[cp]):
                            transport_ok = False
    expect = fact(n) * 4
    ok = iff_ok and transport_ok and passing == expect and total == fact(n) * 4 ** n
    z3_ok = z3_ok and ok
    z3_detail.append('n=%d: %d of %d pass, all with scalar D, each the transport along p: %s' % (n, passing, total, transport_ok))
check('Z3', z3_ok, '; '.join(z3_detail))

# ---------------------------------------------------------------- Z4
Hp = ((ONE, ONE), (ONE, (Fr(-1), Fr(0))))
HpHpT = gmat_mul(Hp, dagger(Hp))
h_unitary = HpHpT == (((Fr(2), Fr(0)), ZERO), (ZERO, (Fr(2), Fr(0))))
adH = tuple(tuple(gscale(Fr(1, 2), x) for x in row) for row in ad(Hp, gunit(2, 0, 0)))
R = (((Fr(3, 5), Fr(0)), (Fr(-4, 5), Fr(0))), ((Fr(4, 5), Fr(0)), (Fr(3, 5), Fr(0))))
r_unitary = gmat_mul(R, dagger(R)) == ((ONE, ZERO), (ZERO, ONE))
adR = ad(R, gunit(2, 0, 0))
check('Z4', h_unitary and r_unitary and not is01(adH) and not is01(adR),
      'Ad(H)(E_00) = %s; Ad(R)(E_00) = %s' % ([[str(x[0]) for x in row] for row in adH],
                                              [[str(x[0]) for x in row] for row in adR]))

# ---------------------------------------------------------------- Z5
CONF = list(itertools.product((0, 1), repeat=3))
IDX = {x: k for k, x in enumerate(CONF)}


def phi(x):
    return (x[0], (x[0] + x[1]) % 2, x[2])


Pphi = tuple(tuple(1 if IDX[phi(CONF[c])] == r else 0 for c in range(8)) for r in range(8))


def stage_unit(Lam, c, cp):
    M = [[0] * 8 for _ in range(8)]
    for x in CONF:
        for xp in CONF:
            if all(x[s] == c[k] and xp[s] == cp[k] for k, s in enumerate(Lam)) and \
                    all(x[s] == xp[s] for s in range(3) if s not in Lam):
                M[IDX[x]][IDX[xp]] = 1
    return tuple(tuple(r) for r in M)


regions = [Lam for r in range(1, 4) for Lam in itertools.combinations(range(3), r)]
all_units = {}
for Lam in regions:
    for c in itertools.product((0, 1), repeat=len(Lam)):
        for cp in itertools.product((0, 1), repeat=len(Lam)):
            all_units[(Lam, c, cp)] = stage_unit(Lam, c, cp)
z5_01 = all(all(v in (0, 1) for row in imul(imul(Pphi, E), itr(Pphi)) for v in row) for E in all_units.values())
img = imul(imul(Pphi, all_units[((0,), (0,), (1,))]), itr(Pphi))
not_unit = all(img != E for E in all_units.values())
check('Z5', z5_01 and not_unit and len(all_units) == 3 * 4 + 3 * 16 + 64,
      'CNOT transport of all %d stage units is {0,1}; the image of E^{0}_{0,1} is no stage unit' % len(all_units))

# ---------------------------------------------------------------- countercontrols
M1 = ((1, 1), (0, 0))
claim1 = not (imul(M1, M1) == M1 and not is_diag(M1))
counter('XZ1', claim1, '[[1, 1], [0, 0]] is idempotent and not diagonal')

D2 = ((ONE, ZERO), (ZERO, IU))
img2 = ad(D2, gunit(2, 0, 1))
claim2 = all(is01(ad(D2, gunit(2, c, cp))) for c in range(2) for cp in range(2))
counter('XZ2', claim2, 'Ad(diag(1, i))(E_01) has entry (%s, %s) at (0, 1)' % (img2[0][1][0], img2[0][1][1]))

V3 = ((1, 1), (0, 0))
G3 = imul(itr(V3), V3)
claim3 = not (all(sum(V3[i][j] for i in range(2)) <= 1 for j in range(2)) and imul(G3, G3) != G3)
counter('XZ3', claim3, 'V = [[1, 1], [0, 0]]: column sums 1, 1; V^T V = %s, (V^T V)^2 = %s' % (G3, imul(G3, G3)))

fails = [n for n, ok in RESULTS if not ok]
cfails = [n for n, ok in COUNTERS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(fails)))
if not fails and not cfails:
    print('VERDICT E17-TRANSPORT-FINITE-CONSISTENT')
else:
    print('VERDICT NOT RENDERED -- failing: %s' % ', '.join(fails + cfails))

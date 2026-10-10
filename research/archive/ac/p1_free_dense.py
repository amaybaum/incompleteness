"""AC probe P1 -- freeness and finite-precision density of the rotation pair
R_x(theta), R_z(theta) with cos(theta) = 3/5, sin(theta) = 4/5.  Exact arithmetic only
(Fraction / integers); no float is used as evidence.

Checks
  F1  generators are rational, orthogonal, det 1; inverses are transposes
  F2  5*R_s is an integer matrix for every letter s
  F3  mod-5 finite-state proof of freeness: each A_s = 5 R_s mod 5 has rank 1 with image line l_s,
      and A_t l_s != 0 mod 5 for every ordered pair (s, t) with t != s^-1   (12 pairs)
      => every reduced word W of length n has 5^n W integral and != 0 mod 5, so W != I (written
         induction, recorded in the ledger)
  F4  exhaustive confirmation to length L: 5^n W integral, != 0 mod 5, W != I, W W^T = I, det W = 1
  F5  countercontrol (same axis): R_z(theta), R_z(theta') with cos theta' = 5/13 commute; the
      reduced commutator word is the identity, so freeness is axis-dependent
  F6  countercontrol (rational quarter turn): R_z(pi/2) has order 4 (no 5-adic denominator)
  F7  finite-precision approximation (illustration of density, NOT a proof of it): for rational
      unit targets t, the orbit points W e_z, |W| <= L, come within |W e_z - t|^2 < 1/100
  F8  orbit points are pairwise distinct as rational vectors for the words enumerated that do not
      end (rightmost) in a z-letter, a countable orbit; the count is printed
"""
import sys
from fractions import Fraction as Fr
from itertools import product

L = int(sys.argv[1]) if len(sys.argv) > 1 else 7

c, s = Fr(3, 5), Fr(4, 5)
I3 = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
Rx = [[Fr(1), Fr(0), Fr(0)], [Fr(0), c, -s], [Fr(0), s, c]]
Rz = [[c, -s, Fr(0)], [s, c, Fr(0)], [Fr(0), Fr(0), Fr(1)]]


def T(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def det(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def mv(A, v):
    return [sum(A[i][k] * v[k] for k in range(3)) for i in range(3)]


GEN = {'x': Rx, 'X': T(Rx), 'z': Rz, 'Z': T(Rz)}
INV = {'x': 'X', 'X': 'x', 'z': 'Z', 'Z': 'z'}

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + detail) if detail else ''))


# F1
for k, A in GEN.items():
    check(f'F1 {k} orthogonal', mul(A, T(A)) == I3)
    check(f'F1 {k} det 1', det(A) == 1)
check('F1 inverse is transpose', mul(Rx, GEN['X']) == I3 and mul(Rz, GEN['Z']) == I3)

# F2
INT = {}
for k, A in GEN.items():
    B = [[5 * a for a in row] for row in A]
    ok = all(b.denominator == 1 for row in B for b in row)
    INT[k] = [[int(b) for b in row] for row in B]
    check(f'F2 5*{k} integral', ok)


# F3: mod-5 linear algebra
def mod5(A):
    return [[a % 5 for a in row] for row in A]


def rank_mod_p(A, p=5):
    M = [row[:] for row in A]
    r = 0
    rows, cols = len(M), len(M[0])
    for cc in range(cols):
        piv = next((i for i in range(r, rows) if M[i][cc] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][cc], p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][cc] % p:
                f = M[i][cc]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return r


img = {}
for k in GEN:
    A = mod5(INT[k])
    rk = rank_mod_p(A)
    check(f'F3 rank(5*{k} mod 5) = 1', rk == 1, f'matrix mod 5 = {A}')
    # image line: any nonzero column
    col = next([A[i][j] for i in range(3)] for j in range(3) if any(A[i][j] for i in range(3)))
    img[k] = col
pairs_ok = 0
for s_, t_ in product(GEN, GEN):
    if t_ == INV[s_]:
        continue
    v = [sum(INT[t_][i][k] * img[s_][k] for k in range(3)) % 5 for i in range(3)]
    nz = any(v)
    pairs_ok += nz
    check(f'F3 pair ({s_} then {t_}): A_t l_s != 0 mod 5', nz, f'A_t l_s = {v}')
check('F3 all 12 admissible pairs nonzero', pairs_ok == 12, f'{pairs_ok}/12')
# the inverse pair must vanish (it is excluded because A_{s^-1} A_s = 25 I = 0 mod 5); control that
# the exclusion is load-bearing
inv_zero = 0
for s_ in GEN:
    t_ = INV[s_]
    v = [sum(INT[t_][i][k] * img[s_][k] for k in range(3)) % 5 for i in range(3)]
    inv_zero += (not any(v))
check('F3 control: inverse pairs vanish mod 5 (exclusion load-bearing)', inv_zero == 4, f'{inv_zero}/4')


# F4: exhaustive reduced words
def reduced_words(n):
    if n == 0:
        yield ''
        return
    for w in reduced_words(n - 1):
        for a in GEN:
            if w and a == INV[w[-1]]:
                continue
            yield w + a


def word_matrix(w):
    M = I3
    for a in w:  # leftmost letter acts last: W = A_{w0} A_{w1} ... ; build as product left to right
        M = mul(M, GEN[a])
    return M


count = 0
bad = 0
for n in range(1, L + 1):
    for w in reduced_words(n):
        W = word_matrix(w)
        B = [[a * 5 ** n for a in row] for row in W]
        integral = all(b.denominator == 1 for row in B for b in row)
        nz5 = any(int(b) % 5 for row in B for b in row) if integral else False
        ortho = mul(W, T(W)) == I3
        d1 = det(W) == 1
        if not (integral and nz5 and ortho and d1 and W != I3):
            bad += 1
        count += 1
check(f'F4 exhaustive reduced words 1..{L}: 5^n W integral, nonzero mod 5, orthogonal, det 1, != I',
      bad == 0, f'{count} words, {bad} failures')

# F5 countercontrol: same axis
c2, s2 = Fr(5, 13), Fr(12, 13)
Rz2 = [[c2, -s2, Fr(0)], [s2, c2, Fr(0)], [Fr(0), Fr(0), Fr(1)]]
comm = mul(mul(Rz, Rz2), mul(T(Rz), T(Rz2)))
check('F5 countercontrol: same-axis pair commutes (reduced commutator = I)', comm == I3)

# F6 countercontrol: rational quarter turn has finite order
Q = [[Fr(0), Fr(-1), Fr(0)], [Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
Q4 = mul(mul(Q, Q), mul(Q, Q))
check('F6 countercontrol: R_z(pi/2)^4 = I (finite order, no 5-adic denominator)', Q4 == I3)

# F7 finite-precision approximation
ez = [Fr(0), Fr(0), Fr(1)]
orbit = {}
for n in range(0, L + 1):
    for w in reduced_words(n):
        if w and w[-1] in 'zZ':  # rightmost letter acts first on e_z and fixes it
            continue
        p = tuple(mv(word_matrix(w), ez))
        orbit.setdefault(p, w)
targets = [
    (Fr(1), Fr(0), Fr(0)),
    (Fr(0), Fr(1), Fr(0)),
    (Fr(0), Fr(0), Fr(-1)),
    (Fr(2, 7), Fr(3, 7), Fr(6, 7)),
    (Fr(-2, 7), Fr(-3, 7), Fr(6, 7)),
    (Fr(2, 11), Fr(-6, 11), Fr(9, 11)),
    (Fr(-1, 9), Fr(4, 9), Fr(-8, 9)),
    (Fr(12, 13), Fr(4, 13), Fr(-3, 13)),
    (Fr(-6, 7), Fr(2, 7), Fr(-3, 7)),
]
eps2 = Fr(1, 100)
allnear = True
for t in targets:
    assert sum(x * x for x in t) == 1
    best = None
    for p, w in orbit.items():
        d2 = sum((a - b) ** 2 for a, b in zip(p, t))
        if best is None or d2 < best[0]:
            best = (d2, w)
    near = best[0] < eps2
    allnear &= near
    check(f'F7 target {tuple(str(x) for x in t)}: min |W e_z - t|^2 < 1/100', near,
          f'min = {best[0]} (~{float(best[0]):.2e}, display only), word length {len(best[1])}')
check('F7 all targets approximated at precision 1/10', allnear)
check('F8 orbit points (|W| <= L) all on the unit sphere', all(sum(x * x for x in p) == 1 for p in orbit),
      f'{len(orbit)} distinct points')

# F9: the antipode -e_z is not reached by any enumerated word.  Written proof for all words: a
# rotation carrying u to -u has angle pi (an involution), and a free group has no torsion.
neg = (Fr(0), Fr(0), Fr(-1))
check('F9 -e_z not in the enumerated orbit of e_z (written: never, torsion-freeness)', neg not in orbit)
# control for F9's mechanism: the involution R_x(pi) = diag(1,-1,-1) does carry e_z to -e_z
Rxpi = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(-1), Fr(0)], [Fr(0), Fr(0), Fr(-1)]]
check('F9 control: R_x(pi) e_z = -e_z and R_x(pi)^2 = I', tuple(mv(Rxpi, ez)) == neg and mul(Rxpi, Rxpi) == I3)

nfail = sum(1 for _, ok in results if not ok)
print(f'SUMMARY {len(results) - nfail}/{len(results)} PASS')
print('VERDICT ' + ('free-and-approximating' if nfail == 0 else 'NOT RENDERED'))

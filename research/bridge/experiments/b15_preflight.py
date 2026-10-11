"""b15_preflight.py — research/bridge, round 4, node B15: exact checks for BridgeConverge.lean.

S0 (written 2026-10-11T05:29:31Z, NOTES-B15, before this script's first run). Checks P1-P8 as listed there; exact
arithmetic over the Gaussian rationals (pairs of Fractions); random tables from a fixed seed (replayable).
P1 reads the equivalence thread's module at its authorized commit (cross-branch read logged 2026-10-11T04:04:10Z) and
checks its hash before comparing definitions.
Run from experiments/:  python3 -I -B b15_preflight.py > b15_preflight.out 2> b15_preflight.err
Run 1 (kept as b15_preflight.run1.*) failed P7 on list order only (a harness error); P7 now compares as sets.
"""
import hashlib
import random
import re
import subprocess
from fractions import Fraction as Fr

EQV_COMMIT = 'c10dbaee'
EQV_PATH = 'research/equivalence/lean/EqvK2Schema.lean'
EQV_SHA = '0bc6da00d5b9ba9c4a2f9390db31c15830a19bf1e30fc2ee6889cd9211281221'
BD_PATH = '../lean/BridgeDictionary.lean'

Z = (Fr(0), Fr(0))
ONE = (Fr(1), Fr(0))
I = (Fr(0), Fr(1))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cconj(a):
    return (a[0], -a[1])


def cscale(r, a):
    return (r * a[0], r * a[1])


def cinv(a):
    d = a[0] * a[0] + a[1] * a[1]
    return (a[0] / d, -a[1] / d)


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum_c([cmul(A[i][k], B[k][j]) for k in range(m)]) for j in range(p)] for i in range(n)]


def sum_c(xs):
    s = Z
    for x in xs:
        s = cadd(s, x)
    return s


def dag(A):
    return [[cconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def kron(A, B):
    n, m = len(A), len(B)
    return [[cmul(A[i // m][k // m], B[i % m][k % m]) for k in range(n * m)] for i in range(n * m)]


PAULI = [
    [[ONE, Z], [Z, ONE]],
    [[Z, ONE], [ONE, Z]],
    [[Z, (Fr(0), Fr(-1))], [I, Z]],
    [[ONE, Z], [Z, (Fr(-1), Fr(0))]],
]
T = [[kron(PAULI[m], PAULI[n]) for n in range(4)] for m in range(4)]


def dict_(w):
    D = [[Z] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            c = Fr(w[m][n]) / 4
            for i in range(4):
                for j in range(4):
                    D[i][j] = cadd(D[i][j], cscale(c, T[m][n][i][j]))
    return D


def trace(A):
    return sum_c([A[i][i] for i in range(len(A))])


def coordOf(H):
    return [[trace(mmul(T[m][n], H))[0] for n in range(4)] for m in range(4)]


def actT(N, w):  # N: 3x3 rational matrix acting on the target's vector part
    out = []
    for m in range(4):
        v = w[m]
        out.append([v[0]] + [sum(N[a][b] * v[b + 1] for b in range(3)) for a in range(3)])
    return out


def rotZ(c, s):
    return [[c, -s, Fr(0)], [s, c, Fr(0)], [Fr(0), Fr(0), Fr(1)]]


NFLIP = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(-1), Fr(0)], [Fr(0), Fr(0), Fr(-1)]]


def zPhase(c, s):
    return [[ONE, Z], [Z, (Fr(c), Fr(s))]]


def one2():
    return [[ONE, Z], [Z, ONE]]


def ad(U, H):
    return mmul(mmul(U, H), dag(U))


def rank_gauss(rows):
    rows = [list(r) for r in rows]
    rk, col, ncol = 0, 0, len(rows[0])
    while rk < len(rows) and col < ncol:
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] != Z), None)
        if piv is None:
            col += 1
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        inv = cinv(rows[rk][col])
        rows[rk] = [cmul(x, inv) for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][col] != Z:
                f = rows[i][col]
                rows[i] = [cadd(x, cmul((-f[0], -f[1]), y)) for x, y in zip(rows[i], rows[rk])]
        rk += 1
        col += 1
    return rk


def defs(text, names):
    out = {}
    for nm in names:
        m = re.search(r'noncomputable def ' + nm + r'\b(.*?)(?=\n\n|\n/--|\ntheorem|\nnoncomputable)', text, re.S)
        out[nm] = ' '.join(m.group(1).split()) if m else None
    return out


def main():
    checks = []
    # P1
    eqv = subprocess.run(['git', '-C', '../../..', 'show', EQV_COMMIT + ':' + EQV_PATH],
                         capture_output=True).stdout
    h = hashlib.sha256(eqv).hexdigest()
    print('equivalence module', EQV_COMMIT, EQV_PATH, h)
    with open(BD_PATH, 'rb') as f:
        bd = f.read()
    print('bridge dictionary', BD_PATH, hashlib.sha256(bd).hexdigest())
    names = ['pauli', 'tokMat', 'dict']
    de, db = defs(eqv.decode(), names), defs(bd.decode(), names)
    for nm in names:
        print('  def', nm, '| equivalence:', de[nm])
        print('  def', nm, '| bridge     :', db[nm])
    checks.append(('P0 equivalence module hash = the authorized blob', h == EQV_SHA))
    checks.append(('P1 pauli, tokMat, dict textually identical in the two modules',
                   all(de[n] is not None and de[n] == db[n] for n in names)))
    # P2
    rows = [[T[m][n][i][j] for i in range(4) for j in range(4)] for m in range(4) for n in range(4)]
    rk = rank_gauss(rows)
    print('P2 rank of the sixteen Pauli tensors over Q(i):', rk)
    checks.append(('P2 rank 16: dict is injective', rk == 16))
    # P3 / P4 on random rational tables
    rng = random.Random(20261011)
    tables = [[[Fr(rng.randint(-9, 9), rng.randint(1, 7)) for _ in range(4)] for _ in range(4)] for _ in range(6)]
    one_z = lambda U: kron(one2(), U)
    p3 = all(coordOf(ad(one_z(zPhase(Fr(3, 5), Fr(4, 5))), dict_(w))) == actT(rotZ(Fr(3, 5), Fr(4, 5)), w)
             for w in tables)
    p3q = all(coordOf(ad(one_z(zPhase(Fr(0), Fr(1))), dict_(w))) == actT(rotZ(Fr(0), Fr(1)), w) for w in tables)
    p3c = all(coordOf(dict_(w)) == [[Fr(x) for x in r] for r in w] for w in tables)
    X = PAULI[1]
    p4 = all(coordOf(ad(one_z(X), dict_(w))) == actT(NFLIP, w) for w in tables)
    checks.append(('P3 coordOf(Ad(1 (x) zPhase(3/5,4/5)) dict w) = actT(rotZ(3/5,4/5)) w on 6 tables', p3))
    checks.append(('P3b the same at the quarter turn (0, 1)', p3q))
    checks.append(('P3c coordOf(dict w) = w (the left inverse) on 6 tables', p3c))
    checks.append(('P4 coordOf(Ad(1 (x) X) dict w) = actT nflip w on 6 tables', p4))
    # P5: nflip on the target permutes Z_F
    def zs(s1, s2):
        w = [[Fr(0)] * 4 for _ in range(4)]
        w[0][0], w[1][3], w[2][2], w[3][1] = Fr(1, 4), Fr(s1, 4), Fr(s2, 4), Fr(-s1 * s2, 4)
        return w
    ZF = [zs(a, b) for a in (1, -1) for b in (1, -1)]
    imgs = [actT(NFLIP, z) for z in ZF]
    checks.append(('P5 actT nflip permutes Z_F', sorted(map(str, imgs)) == sorted(map(str, ZF))))
    # P6: e01 moved by the quarter turn on the target
    e01 = [[Fr(1) if (m, n) == (0, 1) else Fr(0) for n in range(4)] for m in range(4)]
    checks.append(('P6 actT(rotZ(0,1)) e01 != e01', actT(rotZ(Fr(0), Fr(1)), e01) != e01))
    # P7: the unitary members of the stated access on one token
    pats = []
    for bits in range(16):
        P = [[(bits >> (2 * i + j)) & 1 for j in range(2)] for i in range(2)]
        if all(sum(P[i]) <= 1 for i in range(2)) and all(P[0][j] + P[1][j] <= 1 for j in range(2)):
            pats.append(P)
    unit = []
    for P in pats:
        PtP = [[sum(P[k][i] * P[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        # (cP)^H (cP) = |c|^2 P^T P is the identity for some c iff P^T P is the identity (then |c| = 1)
        if PtP == [[1, 0], [0, 1]]:
            unit.append(P)
    print('P7 partial permutation patterns:', len(pats), ' unitary up to |c| = 1:', unit)
    checks.append(('P7 unitary scaled partial permutations of one token: exactly c*1 and c*X, |c| = 1',
                   len(pats) == 7 and sorted(unit) == sorted([[[1, 0], [0, 1]], [[0, 1], [1, 0]]])))
    # P8: the quarter access's transferred group on the target
    def m3(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    gens = [NFLIP, rotZ(Fr(0), Fr(1))]
    key = lambda A: tuple(tuple(r) for r in A)
    seen = {key(g): g for g in gens}
    fr = list(gens)
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = m3(A, g)
                if key(B) not in seen:
                    seen[key(B)] = B
                    nx.append(B)
        fr = nx
    order = len(seen)
    has345 = key(rotZ(Fr(3, 5), Fr(4, 5))) in seen
    print('P8 group <actT nflip, actT R_z(pi/2)> on the target: order', order, '; contains R_z(theta0):', has345)
    checks.append(('P8 the quarter access transfers a finite group of order 8 without R_z(theta0)', order == 8 and not has345))
    print('\nCHECKS')
    for nm, ok in checks:
        print(('PASS ' if ok else 'FAIL ') + nm)
    print('VERDICT B15-PREFLIGHT: ' + ('all checks green' if all(ok for _, ok in checks) else 'a check failed'))


main()

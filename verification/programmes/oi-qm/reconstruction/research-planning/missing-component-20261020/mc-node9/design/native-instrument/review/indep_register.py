"""Independent reviewer recomputation (register level). Does not import the author's checker.
Exact rationals throughout."""
from fractions import Fraction as Fr
from itertools import product
from math import log2

AX = {'X': (1, 0, 0), 'Y': (0, 1, 0), 'Z': (0, 0, 1), 'R': (Fr(4, 5), Fr(3, 5), 0)}
NAMES = ['X', 'Y', 'Z', 'R']
STATIONS = [(sg, n) for n in NAMES for sg in (+1, -1)]
def bloch(st): return tuple(st[0] * Fr(x) for x in AX[st[1]])
def ip(u, v): return sum(Fr(x) * Fr(y) for x, y in zip(u, v))
def born(c, w): return (1 + ip(AX[c], w)) / 2

# ---------- 1. brute-force sampler: 16 fair bits per attempt, 4 per component, accept u<10, bit=1 iff u<10p
def attempt_law(w):
    acc = 0; joint = {}
    ks = [born(c, w) * 10 for c in NAMES]
    assert all(k.denominator == 1 for k in ks)
    for us in product(range(16), repeat=4):
        if all(u < 10 for u in us):
            acc += 1
            lam = tuple(int(u < k) for u, k in zip(us, ks))
            joint[lam] = joint.get(lam, 0) + 1
    return Fr(acc, 16 ** 4), {l: Fr(v, acc) for l, v in joint.items()}

acc_by = {}; LAM = {}
for st in STATIONS:
    q, law = attempt_law(bloch(st)); acc_by[st] = q; LAM[st] = law
print('acceptance per attempt by station:', set(acc_by.values()), '(625/4096 =', Fr(625, 4096), ')')
# product structure and Born marginals
ok_prod = True; ok_born = True
for st in STATIONS:
    w = bloch(st)
    for lam in product((0, 1), repeat=4):
        pr = Fr(1)
        for i, c in enumerate(NAMES):
            pr *= born(c, w) if lam[i] else 1 - born(c, w)
        ok_prod &= LAM[st].get(lam, Fr(0)) == pr
    for i, c in enumerate(NAMES):
        ok_born &= sum(v for l, v in LAM[st].items() if l[i] == 1) == born(c, w)
print('hidden register is product with P(l_c=1)=(1+c.w)/2 for all 8 stations:', ok_prod, ok_born)
print('Born table P(+a | w):')
for st in STATIONS:
    print('  %s%s' % ('+' if st[0] > 0 else '-', st[1]), [str(born(a, bloch(st))) for a in NAMES])

# ---------- identities: test via null space computed independently (affine-in-w test)
def solve_affine(vals):
    """Return True iff vals[st] = c0 + c.w for some (c0,c) exactly (least-squares-free exact solve)."""
    # unknowns c0,c1,c2,c3: use stations +X,-X,+Y,+Z to solve, then check all
    pX, mX, pY, pZ = vals[(1, 'X')], vals[(-1, 'X')], vals[(1, 'Y')], vals[(1, 'Z')]
    c0 = (pX + mX) / 2; c1 = (pX - mX) / 2; c2 = pY - c0; c3 = pZ - c0
    return all(vals[st] == c0 + ip((c1, c2, c3), bloch(st)) for st in STATIONS)

def ids_hold(K):
    atoms = set().union(*[set(K[s]) for s in STATIONS])
    return all(solve_affine({s: K[s].get(at, Fr(0)) for s in STATIONS}) for at in atoms)

WA = {(1, 'R'): Fr(13, 16), (-1, 'R'): Fr(3, 16)}
WB = {(1, 'X'): Fr(1, 2), (1, 'Y'): Fr(3, 8), (1, 'Z'): Fr(1, 16), (-1, 'Z'): Fr(1, 16)}
assert sum(WA[s] * Fr(1) * 0 + WA[s] * bloch(s)[0] for s in WA) == sum(WB[s] * bloch(s)[0] for s in WB)
for i in range(3): assert sum(WA[s] * bloch(s)[i] for s in WA) == sum(WB[s] * bloch(s)[i] for s in WB)
def tv(K):
    atoms = set().union(*[set(K[s]) for s in STATIONS])
    return sum(abs(sum(WA[s] * K[s].get(a, 0) for s in WA) - sum(WB[s] * K[s].get(a, 0) for s in WB)) for a in atoms) / 2

Q = Fr(625, 4096)
HER = {1: Q, 2: (1 - Q) * Q, 'f': (1 - Q) ** 2}
def fresh(a):  # r_c ~ Bern((1+a.c)/2), product
    return {r: _prod([born(c, AX[a]) if r[i] else 1 - born(c, AX[a]) for i, c in enumerate(NAMES)])
            for r in product((0, 1), repeat=4)}
def _prod(xs):
    p = Fr(1)
    for x in xs: p *= x
    return p
def rep(lam, r, a):
    la = lam[NAMES.index(a)]; return tuple(la ^ 1 ^ x for x in r)

def single(st, a, mode=''):
    K = {('F',): HER['f']}; ia = NAMES.index(a)
    for j in (1, 2):
        for lam, pl in LAM[st].items():
            for j2 in (1, 2, 'f'):
                base = (j, lam[ia], j2)
                if mode == 'hidden': base += tuple(lam[i] for i in range(4) if i != ia)
                if mode == 'fresh' and j2 != 'f':
                    for r, pr in fresh(a).items():
                        if pr: K[base + r] = K.get(base + r, 0) + HER[j] * pl * HER[j2] * pr
                    continue
                K[base] = K.get(base, 0) + HER[j] * pl * HER[j2]
    return K

def two(st, a, c, nd=False):
    K = {('F',): HER['f']}; ia, ic = NAMES.index(a), NAMES.index(c)
    for j in (1, 2):
        for lam, pl in LAM[st].items():
            k = (j, lam[ia], 'f'); K[k] = K.get(k, 0) + HER[j] * pl * HER['f']
            for j2 in (1, 2):
                for r, pr in fresh(a).items():
                    if not pr: continue
                    l2 = lam if nd else rep(lam, r, a)
                    for j3 in (1, 2, 'f'):
                        k = (j, lam[ia], j2, l2[ic], j3); K[k] = K.get(k, 0) + HER[j] * pl * HER[j2] * pr * HER[j3]
    return K

print('Q1 single-read identities hold (affine test) per setting:', {a: ids_hold({s: single(s, a) for s in STATIONS}) for a in NAMES})
q2 = {(a, c): ids_hold({s: two(s, a, c) for s in STATIONS}) for a in NAMES for c in NAMES}
print('Q2 two-read identities hold for all 16 pairs:', all(q2.values()))
# Born for 2nd read given first outcome
okb2 = True
for st in STATIONS:
    for a in NAMES:
        for c in NAMES:
            K = two(st, a, c)
            for o in (0, 1):
                den = sum(v for k, v in K.items() if len(k) == 5 and k[1] == o)
                if den == 0: continue
                num = sum(v for k, v in K.items() if len(k) == 5 and k[1] == o and k[3] == 1)
                s = 1 if o else -1
                okb2 &= num / den == (1 + s * ip(AX[a], AX[c])) / 2
print('Q3 second-read Born given first outcome exact:', okb2)
# closure
okc = True
for st in STATIONS:
    for a in NAMES:
        ia = NAMES.index(a)
        for o in (0, 1):
            po = sum(v for l, v in LAM[st].items() if l[ia] == o)
            if not po: continue
            out = {}
            for l, v in LAM[st].items():
                if l[ia] != o: continue
                for r, pr in fresh(a).items():
                    l2 = rep(l, r, a); out[l2] = out.get(l2, 0) + v * pr / po
            tgt = LAM[(1 if o else -1, a)]
            okc &= all(out.get(k, 0) == tgt.get(k, 0) for k in set(out) | set(tgt))
print('Q4 closure (outgoing law given outcome = P_{s a}, jointly):', okc)
# C-ND, C-HER-like
ndf = [(a, c) for a in NAMES for c in NAMES if not ids_hold({s: two(s, a, c, True) for s in STATIONS})]
print('C-ND failing pairs:', len(ndf), ndf, 'max TV', max(tv({s: two(s, a, c, True) for s in STATIONS}) for a, c in ndf))
# Q6a
for a in NAMES:
    K = {s: single(s, a, 'hidden') for s in STATIONS}
    print('Q6a', a, 'identities hold:', ids_hold(K), 'TV', tv(K), float(tv(K)), '; =95155025/2^30:', tv(K) == Fr(95155025, 2 ** 30))
# Q6b
for a in NAMES:
    K = {s: single(s, a, 'fresh') for s in STATIONS}
    det = max(fresh(a).values()) < 1
    print('Q6b', a, 'identities hold:', ids_hold(K), '; fresh bits non-degenerate so record determines outgoing (closure fails):', det)
# entropy deficits
h2 = lambda p: 0.0 if p in (0, 1) else -(p * log2(p) + (1 - p) * log2(1 - p))
for a in NAMES:
    d = sum(1 - h2(float(born(c, AX[a]))) for c in NAMES if c != a)
    print('entropy deficit of three fresh bits, setting', a, '%.3f' % d)

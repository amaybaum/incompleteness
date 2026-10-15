#!/usr/bin/env python3
"""bg2_orientation_probe.py -- round BG-2's exact layer (standard library, exact integers).

The premise under test is OIBridge.ScopeTransfer.BGIntegerClassification as the kernel states it.
For ascending six-mark integer rulers F, F' with distinct differences, equal difference sets and no
translation or reflection congruence, its exceptional branch asserts relabelings eS, eT with
    F'(eT (mu a b).2) - F'(eT (mu a b).1) = F(eS b) - F(eS a)        (the SIGNED form)
for every a < b. The REVERSED form has F(eS a) - F(eS b) on the right.

Cells (each prints PASS or FAIL):
  O0  parse r1, r2, mu (HomometricSix.lean) and piccardX, piccardY (PiccardBridge.lean) from the
      kernel sources, with the landed gap identity checked on the parse
  O1  the eight orientation variants of the printed pair (order swapped, either ruler reflected)
      satisfy the premise's hypotheses
  O2  exhaustive eS x eT counts of signed and reversed solutions per variant (complete fingerprints)
  O3  an independent forced-eT algorithm reproduces the O2 counts
  O4  on the frozen box 1 <= p1 <= 7, 1 <= p2 <= 29 of the quoted family, every eligible member
      attains the signed form at (X,Y), (Y,X), (RX,RY) and never at (X,RY), (RX,Y)
  O5  among Golomb rulers of span <= 40: no nontrivial homometric pair at 3, 4, 5 or 7 marks, and
      each nontrivial six-mark ordered pair attains exactly one of the two forms
  K1  the correspondence with mu 0 2 and mu 0 3 exchanged has no solution at (r1, r2)
  K2  the hypothesis checker rejects (r1, 17 - r1 o rev) and (r1, r1 + 3)

The probe is a finite exact check. It does not formalize any classification.
"""
import os
import re
import sys
from collections import Counter
from itertools import combinations, permutations

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.join(HERE, '..', 'lean-mathlib', 'OIBridge')
PAIRS = tuple(combinations(range(6), 2))
PERMS = tuple(permutations(range(6)))
BOX = (7, 29)
SPAN = 40

results = []


def check(name, ok, detail):
    results.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + '  ' + detail)


# ---------------------------------------------------------------- O0 parse
homometric = open(os.path.join(BRIDGE, 'HomometricSix.lean'), encoding='utf-8').read()
bridge = open(os.path.join(BRIDGE, 'PiccardBridge.lean'), encoding='utf-8').read()


def block(text, name, following):
    return text.split('def ' + name + ' :', 1)[1].split('def ' + following + ' :', 1)[0]


def marks(name, following):
    vals = re.findall(r'\|\s*([0-5])\s*=>\s*(-?\d+)', block(homometric, name, following))
    assert [int(i) for i, _ in vals] == list(range(6)), name
    return tuple(int(v) for _, v in vals)


r1, r2 = marks('r1', 'r2'), marks('r2', 'mu')
mu = {(int(a), int(b)): (int(c), int(d)) for a, b, c, d in
      re.findall(r'\|\s*([0-5])\s*,\s*([0-5])\s*=>\s*\(([0-5])\s*,\s*([0-5])\)',
                 block(homometric, 'mu', 'muInv'))}


def family(name):
    body = bridge.split('def ' + name + ' ', 1)[1].split('\n\n', 1)[0]
    items = re.findall(r'\|\s*([0-5])\s*=>\s*([^|\n]+)', body)
    assert [int(i) for i, _ in items] == list(range(6)), name
    coeffs = []
    for _, expr in items:
        expr = expr.strip()
        c = [0, 0]
        for sign, num, var in re.findall(r'([+-]?)\s*(\d*)\s*\*?\s*(p1|p2|0)', expr.replace(' ', '')):
            if var == '0':
                continue
            k = int(num) if num else 1
            c[0 if var == 'p1' else 1] += -k if sign == '-' else k
        coeffs.append(tuple(c))
    return tuple(coeffs)


fx, fy = family('piccardX'), family('piccardY')
landed = all(r2[mu[a, b][1]] - r2[mu[a, b][0]] == r1[b] - r1[a] for a, b in PAIRS)
check('O0', set(mu) == set(PAIRS) and landed and r1 == (0, 1, 4, 10, 12, 17)
      and r2 == (0, 1, 8, 11, 13, 17) and fx == ((0, 0), (1, 0), (-2, 1), (-2, 2), (0, 2), (-1, 3))
      and fy == ((0, 0), (1, 0), (2, 1), (1, 2), (-1, 2), (-1, 3)),
      'r1 %s, r2 %s, mu on 15 pairs with the landed gap identity, piccardX %s, piccardY %s'
      % (r1, r2, fx, fy))


# ---------------------------------------------------------------- the premise's hypotheses
def reflect(x):
    return tuple(x[-1] + x[0] - v for v in reversed(x))


def eligible(x, y):
    """The hypotheses of BGIntegerClassification at six marks, for ascending tuples x, y."""
    gx = [x[b] - x[a] for a, b in PAIRS]
    gy = [y[b] - y[a] for a, b in PAIRS]
    return (all(x[i] < x[i + 1] and y[i] < y[i + 1] for i in range(5))
            and len(set(gx)) == len(set(gy)) == 15 and set(gx) == set(gy)
            and len({y[i] - x[i] for i in range(6)}) > 1
            and len({y[i] + x[5 - i] for i in range(6)}) > 1)


def counts_fingerprint(x, y, corr):
    target = Counter(tuple(y[t[corr[a, b][1]]] - y[t[corr[a, b][0]]] for a, b in PAIRS) for t in PERMS)
    res = [0, 0]
    for s in PERMS:
        v = tuple(x[s[b]] - x[s[a]] for a, b in PAIRS)
        res[0] += target[v]
        res[1] += target[tuple(-z for z in v)]
    return res


def counts_forced(x, y, corr):
    by_gap = {y[j] - y[i]: (i, j) for i in range(6) for j in range(6) if i != j}
    if len(by_gap) != 30:
        return None
    res = [0, 0]
    for s in PERMS:
        for slot, sign in enumerate((1, -1)):
            assign = {}
            ok = True
            for (a, b), (c, d) in corr.items():
                tp = by_gap.get(sign * (x[s[b]] - x[s[a]]))
                if tp is None:
                    ok = False
                    break
                for lab, nat in zip((c, d), tp):
                    if assign.setdefault(lab, nat) != nat:
                        ok = False
                        break
                if not ok:
                    break
            if ok and len(set(assign.values())) == 6:
                res[slot] += 1
    return res


# ---------------------------------------------------------------- O1, O2, O3
variants = []
for swapped in (False, True):
    for rs in (False, True):
        for rt in (False, True):
            x, y = (r2, r1) if swapped else (r1, r2)
            variants.append(((swapped, rs, rt), reflect(x) if rs else x, reflect(y) if rt else y))
check('O1', all(eligible(x, y) for _, x, y in variants),
      'all 8 variants (swapped, source reflected, target reflected) satisfy the hypotheses')
fp = {k: counts_fingerprint(x, y, mu) for k, x, y in variants}
expected = {k: ([0, 3] if k[1] != k[2] else [3, 0]) for k, _, _ in variants}
check('O2', fp == expected,
      'signed/reversed counts per variant: %s'
      % '; '.join('%s%s%s %d/%d' % ('S' if k[0] else '-', 'R' if k[1] else '-', 'R' if k[2] else '-',
                                    v[0], v[1]) for k, v in fp.items()))
fo = {k: counts_forced(x, y, mu) for k, x, y in variants}
check('O3', fo == fp, 'the forced-eT algorithm reproduces every O2 count')

# ---------------------------------------------------------------- O4
members = []
for p1 in range(1, BOX[0] + 1):
    for p2 in range(1, BOX[1] + 1):
        X = tuple(sorted(a * p1 + b * p2 for a, b in fx))
        Y = tuple(sorted(a * p1 + b * p2 for a, b in fy))
        if not eligible(X, Y):
            continue
        members.append((p1, p2, X, Y))


def signed(x, y):
    c = counts_forced(x, y, mu)
    return c is not None and c[0] > 0


o4 = all(signed(X, Y) and signed(Y, X) and signed(reflect(X), reflect(Y))
         and not signed(X, reflect(Y)) and not signed(reflect(X), Y) for _, _, X, Y in members)
check('O4', o4 and len(members) > 0,
      '%d eligible members on the box p1 <= %d, p2 <= %d; signed at (X,Y), (Y,X), (RX,RY) and never at '
      '(X,RY), (RX,Y): %s' % (len(members), BOX[0], BOX[1], o4))


# ---------------------------------------------------------------- O5
def golomb(m, span):
    out = []

    def ext(marks_, used):
        if len(marks_) == m:
            if marks_[-1] <= span:
                out.append(tuple(marks_))
            return
        need = m - len(marks_)
        for v in range(marks_[-1] + 1, span - need + 2):
            ds = [v - w for w in marks_]
            if any(d in used for d in ds):
                continue
            ext(marks_ + [v], used | set(ds))
    ext([0], set())
    return out


o5_ok = True
details = []
six = None
for m in (3, 4, 5, 6, 7):
    rulers = golomb(m, SPAN)
    groups = {}
    for r in rulers:
        groups.setdefault(frozenset(b - a for a, b in combinations(r, 2)), []).append(r)
    pairs = [(a, b) for g in groups.values() for a in g for b in g
             if a != b and b != reflect(a)]
    if m == 6:
        six = pairs
        ns = nr = nn = nb = 0
        for a, b in pairs:
            c = counts_forced(a, b, mu)
            s_, r_ = c[0] > 0, c[1] > 0
            ns += s_ and not r_
            nr += r_ and not s_
            nn += not s_ and not r_
            nb += s_ and r_
        o5_ok &= ns + nr == len(pairs) and len(pairs) > 0
        details.append('m=6: %d rulers, %d ordered pairs: %d signed, %d reversed, %d neither, %d both'
                       % (len(rulers), len(pairs), ns, nr, nn, nb))
    else:
        o5_ok &= not pairs
        details.append('m=%d: %d rulers, %d pairs' % (m, len(rulers), len(pairs)))
check('O5', o5_ok, 'span <= %d; %s' % (SPAN, '; '.join(details)))

# ---------------------------------------------------------------- K1, K2
broken = dict(mu)
broken[0, 2], broken[0, 3] = broken[0, 3], broken[0, 2]
k1 = counts_fingerprint(r1, r2, broken) == [0, 0] and counts_forced(r1, r2, broken) == [0, 0]
check('K1', k1, 'mu 0 2 <-> mu 0 3 exchanged: no signed or reversed solution at (r1, r2), both algorithms')
k2 = not eligible(r1, reflect(r1)) and not eligible(r1, tuple(v + 3 for v in r1))
check('K2', k2, 'the checker rejects (r1, 17 - r1 o rev) and (r1, r1 + 3)')

fails = sum(1 for _, ok in results if not ok)
print('checks: %d, failures: %d' % (len(results), fails))
if fails == 0 and len(results) == 8:
    print('VERDICT PREMISE-ORIENTATION-EXACT')
else:
    print('VERDICT PREMISE-ORIENTATION-NOT-ESTABLISHED')
sys.exit(1 if fails else 0)

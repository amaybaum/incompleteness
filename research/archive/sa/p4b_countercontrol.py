"""P4b -- countercontrol for the label-dual (prefix-closure) premise of AffineRespect, on a carrier whose hidden
bit is passively invisible.  Exact arithmetic only.

Omega = Z2 (visible phase k) x Z2 (hidden h); phi(k,h) = (k+1, h); vis(k,h) = k; action 'g' = controlled flip:
if h = 1 flip k.  Letters: 'o' record vis then phi, 'i' phi, 'g' controlled flip.
Toy-1 of p4_collapse.py was passively separating, which made its obs-only countercontrol vacuous (recorded).
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp

OMEGA = [(k, h) for k in range(2) for h in range(2)]
IDX = {w: n for n, w in enumerate(OMEGA)}
phi = lambda w: ((w[0] + 1) % 2, w[1])
vis = lambda w: w[0]
cflip = lambda w: ((w[0] + w[1]) % 2, w[1])
MU = [F(1, 10), F(2, 10), F(3, 10), F(4, 10)]
STEP = {'o': phi, 'i': phi, 'g': cflip}

def run(sigma, w):
    rec = []
    for a in sigma:
        if a == 'o':
            rec.append(vis(w))
        w = STEP[a](w)
    return tuple(rec), w

def seqs(alph, n):
    out = [()]
    for L in range(1, n + 1):
        out += list(product(alph, repeat=L))
    return out

def preps(alph, n):
    P = {}
    for s in seqs(alph, n):
        b = {}
        for w in OMEGA:
            r, w2 = run(s, w)
            b.setdefault(r, [F(0)] * 4)
            b[r][IDX[w2]] += MU[IDX[w]]
        for r, v in b.items():
            z = sum(v)
            if z > 0:
                P[(s, r)] = tuple(x / z for x in v)
    return P

def effects(alph, n):
    E = [((), ())]
    for s in seqs(alph, n)[1:]:
        for r in product((0, 1), repeat=s.count('o')):
            E.append((s, r))
    return E

resp = lambda e, w: 1 if run(e[0], w)[0] == e[1] else 0

def pushmat(g):
    M = sp.zeros(4, 4)
    for w in OMEGA:
        M[IDX[g(w)], IDX[w]] = 1
    return M

P = preps(('o', 'i', 'g'), 4)
nus = list(set(P.values()))

def test(eff_alph, L, act):
    R = sp.Matrix([[resp(e, w) for w in OMEGA] for e in effects(eff_alph, L)])
    base = sp.Matrix(nus[0])
    diffs = sp.Matrix.hstack(*[sp.Matrix(nu) - base for nu in nus[1:]])
    D = [diffs * c for c in (R * diffs).nullspace()]
    A = pushmat(act)
    bad = [v for v in D if any(x != 0 for x in R * (A * v))]
    return R.rank(), len(D), bad

out = []
rk, nD, bad = test(('o', 'i'), 6, cflip)
out.append(('obs-only effects: AffineRespect(cflip) FAILS (expected)', len(bad) > 0,
            f'rank R_obs {rk}, relations {nD}, violated {len(bad)}; witness relation {list(bad[0]) if bad else None}'))
rk, nD, bad = test(('o', 'i', 'g'), 6, cflip)
out.append(('prefix-closed effects: AffineRespect(cflip) holds', len(bad) == 0, f'rank R {rk}, relations {nD}, violated {len(bad)}'))
rk, nD, bad = test(('o', 'i'), 6, phi)
out.append(('obs-only effects: AffineRespect(idle) holds', len(bad) == 0, f'relations {nD}, violated {len(bad)}'))
# Undoes: cflip is an involution
und = all(P[(x[0] + ('g', 'g'), x[1])] == nu for x, nu in P.items() if len(x[0]) <= 2)
out.append(('Undoes(cflip, cflip): posteriors equal', und, ''))
allok = True
for name, c, d in out:
    allok &= c
    print(('PASS ' if c else 'FAIL ') + name + (' -- ' + d if d else ''))
print('ALL-PASS' if allok else 'SOME-FAIL')

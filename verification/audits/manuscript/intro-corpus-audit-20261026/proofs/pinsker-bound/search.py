"""Exhaustive rational-grid search for violations of  I(X_<k; X_{k+1} | X_k) >= p0 delta^2 / ln 2.

Usage: python3 -I -B search.py <mode> <N>
  full1  : full joint of (X0, X1, X2) on {0,1}^3, all probabilities in (1/N)Z   (k = 1)
  full2  : full joint of (X0, X1, X2, X3) on {0,1}^4                            (k = 2)
  slice1 : one present c, 2 pasts x 2 futures, slack mass on another present   (k = 1)
  slice2 : one present c, 4 pasts x 2 futures, slack                          (k = 2)
  slice1t: one present c, 2 pasts x 3 futures, slack                          (ternary future)
Slice modes are sufficient for a counterexample search: I >= I_c, and the slack
mass on a single cell at another present contributes 0 to I, so every slice
instance is a full joint law.

Every pair of distinct pasts at a common present with positive joint masses is
tested with p0 = min of the two joint masses and delta = their exact TV
(1/2 l1).  Decisions in interval arithmetic against the exact rational bound in nats.
Countercontrol variants (expected to FIRE on fine enough grids) are counted on
the same instances.
"""
import sys, os, itertools, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from cmi_iv import *

mode, N = sys.argv[1], int(sys.argv[2])
if mode == 'full1':
    cells = [((x0,), x1, (x2,)) for x0, x1, x2 in itertools.product((0, 1), repeat=3)]; slack = None
elif mode == 'full2':
    cells = [((x0, x1), x2, (x3,)) for x0, x1, x2, x3 in itertools.product((0, 1), repeat=4)]; slack = None
elif mode == 'slice1':
    cells = [(a, 'c', b) for a in (0, 1) for b in (0, 1)]; slack = ('s', 'other', 0)
elif mode == 'slice2':
    cells = [(a, 'c', b) for a in range(4) for b in (0, 1)]; slack = ('s', 'other', 0)
elif mode == 'slice1t':
    cells = [(a, 'c', b) for a in (0, 1) for b in (0, 1, 2)]; slack = ('s', 'other', 0)
else:
    raise SystemExit('bad mode')

nparts = len(cells) + (1 if slack else 0)
variants = {
    'stated  p0 d^2':           lambda h: h['p0'] * h['delta'] ** 2,
    'harmonic 2w1w2/(w1+w2) d^2': lambda h: 2 * h['w1'] * h['w2'] / (h['w1'] + h['w2']) * h['delta'] ** 2,
    'CC 1.01 p0 d^2':           lambda h: F(101, 100) * h['p0'] * h['delta'] ** 2,
    'CC l1: p0 (2d)^2':         lambda h: h['p0'] * (2 * h['delta']) ** 2,
    'CC conditional p0':        lambda h: h['p0'] / h['pc'] * h['delta'] ** 2,
    'CC average weight':        lambda h: (h['w1'] + h['w2']) / 2 * h['delta'] ** 2,
}
viol = {k: 0 for k in variants}
undec = {k: 0 for k in variants}
first_viol = {}
ninst = npairs = nd1 = 0
bad_vs_H = 0
max_ratio = None
t0 = time.time()
for comp in compositions(N, nparts):
    tab = {}
    for cell, n in zip(cells, comp):
        if n:
            tab[cell] = F(n, N)
    if slack and comp[-1]:
        tab[slack] = F(comp[-1], N)
    hp = hypothesis_pairs(tab)
    hp = [h for h in hp if h['delta'] > 0]
    if not hp:
        continue
    ninst += 1
    I = cmi_nats(tab)
    I2 = cmi_nats_entropy(tab)
    if not (I.a <= I2.b and I2.a <= I.b):
        raise SystemExit(f'CONTROL FAIL: CMI formulas disagree on {tab}')
    HBC = cond_entropy_B_given_C_nats(tab)
    for h in hp:
        npairs += 1
        nd1 += h['delta'] == 1
        for name, f in variants.items():
            r = decide(I, f(h))
            if r == 'VIOLATION':
                viol[name] += 1
                first_viol.setdefault(name, (dict((str(k), str(v)) for k, v in tab.items()), {k: str(v) for k, v in h.items()}))
            elif r == 'undecided':
                undec[name] += 1
        b = ivq(h['p0'] * h['delta'] ** 2)
        if not (b.b <= HBC.a):
            bad_vs_H += 1
        rat = b / I
        if max_ratio is None or rat.b > max_ratio[0]:
            max_ratio = (rat.b, {str(k): str(v) for k, v in tab.items()}, {k: str(v) for k, v in h.items()})
print(f'mode={mode} N={N}: instances with a gap = {ninst}, pairs tested = {npairs}, pairs with delta=1 = {nd1}, time {time.time()-t0:.1f}s')
for name in variants:
    print(f'   {name:<28} violations = {viol[name]:>7}   undecided = {undec[name]}')
print(f'   bound > H(X_k+1|X_k) (not certified <=): {bad_vs_H}')
print(f'   max ratio bound/I (upper end) = {float(max_ratio[0]):.12f}')
print(f'     at {max_ratio[1]}  pair {max_ratio[2]}')
for name, ex in first_viol.items():
    if name.startswith('CC'):
        print(f'   first {name} violation: {ex}')
    else:
        print(f'   *** {name} VIOLATION: {ex}')

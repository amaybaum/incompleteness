"""Reviewer check of cone radii from a reference pair (E = earlier slice, L = later slice).
Forward k steps after L: dependence on L within k, on E within k-1. (Backward is the same with roles swapped.)"""
import random, importlib.util, sys
spec = importlib.util.spec_from_file_location('lm', 'lemmas.py')
src = open('lemmas.py').read().split('rng = random.Random(7)')[0]
ns = {}; exec(src, ns)
evolve, ball = ns['evolve'], ns['ball']
rng = random.Random(3); T, R = 5, 0
cells = ball(R+T)
maxdepE = {}; maxdepL = {}
for trial in range(400):
    E = {c: rng.randrange(8) for c in cells}; L = {c: rng.randrange(8) for c in cells}
    base = evolve(E, L, T, R)
    which = rng.randrange(2); c = rng.choice(cells)
    E2, L2 = dict(E), dict(L)
    (E2 if which == 0 else L2)[c] ^= 1 + rng.randrange(7)
    pert = evolve(E2, L2, T, R)
    d = sum(abs(v) for v in c)
    for k in range(1, T+1):
        if base[k+1][(0,0,0)] != pert[k+1][(0,0,0)]:
            m = maxdepE if which == 0 else maxdepL
            m[k] = max(m.get(k, -1), d)
print('k : max distance of an influencing E-var / L-var (expect k-1 / k)')
for k in range(1, T+1): print(k, maxdepE.get(k), maxdepL.get(k))

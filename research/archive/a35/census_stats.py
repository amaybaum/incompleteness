"""Recompute the 400-sample census statistics with the corrected (symmetric, transpose-paired) profile."""
import numpy as np, itertools, sys
sys.path.insert(0, '.')
from lib35 import *
def prof_sym(H):
    Hn = H / np.abs(H); vals = []
    P2 = np.einsum('ak,bk->abk', Hn, np.conj(Hn))
    for a, b, c, d in itertools.combinations(range(16), 4):
        trip = sorted(round(abs(np.sum(P2[p, q] * P2[r, t])), 6) for (p, q, r, t) in ((a, b, c, d), (a, c, b, d), (a, b, d, c)))
        vals.append(tuple(trip))
    return tuple(sorted(vals))
def prof2(H): return tuple(sorted((prof_sym(H), prof_sym(H.T))))
rng = np.random.default_rng(354)
roots = np.array([1, 1j, -1, -1j])
kron_inv = {}
for nm, X, Y in (('H4⊗H4', U_circle(0, 1), U_circle(0, 1)), ('H4⊗F4', U_circle(0, 1), U_circle(0, 1j)), ('F4⊗H4', U_circle(0, 1j), U_circle(0, 1)), ('F4⊗F4', U_circle(0, 1j), U_circle(0, 1j))):
    H = kron(X, Y); kron_inv[nm] = (prof2(H), haagerup_set(H), defect_numeric(H)[0])
print('Kronecker triples distinct:', len(set(kron_inv.values())))
classes = {}; n_def = 0
for _ in range(400):
    bits = rng.integers(0, 4, size=(3, 3)); D = np.ones((4, 4), dtype=complex); D[1:, 1:] = roots[bits]
    X = U_circle(rng.integers(0, 9), roots[rng.integers(0, 4)] if rng.random() < 0.5 else 1j)
    Ys = [U_circle(rng.integers(0, 9), roots[rng.integers(0, 4)]) for _ in range(4)]
    Hd = dita(X, Ys, D); d = defect_numeric(Hd)[0]
    if d not in {57, 73, 105}: n_def += 1
    classes.setdefault((prof2(Hd), haagerup_set(Hd), d), 0); classes[(prof2(Hd), haagerup_set(Hd), d)] += 1
print('400 samples: distinct (profile pair, Haagerup, defect) triples %d; samples with defect outside {57,73,105}: %d; triples coinciding with a Kronecker triple: %d' % (len(classes), n_def, sum(1 for c in classes if c in kron_inv.values())))
Fi = F4(1j); Dw = np.ones((4, 4), dtype=complex); Dw[1, :] = [1, 1j, 1, -1j]; Hw = dita(Fi, [Fi] * 4, Dw)
print('Hw profile pair != F4⊗F4:', prof2(Hw) != kron_inv['F4⊗F4'][0], '; values Hw', sorted({x for t in prof_sym(Hw) for x in t}), 'F4⊗F4', sorted({x for t in prof_sym(kron(Fi, Fi)) for x in t}))

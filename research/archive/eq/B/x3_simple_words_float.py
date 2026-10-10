"""EXPLORATION ONLY (floating point; certifies nothing).

Search for the simplest word failing posFwd at d = 5: W = G_s (L (x) I) G_t or G_s (I (x) L) G_t with L a
90-degree rotation in one coordinate plane (a signed permutation) and t, s in {pi/2, pi, 3pi/2}.
"""
import numpy as np
import itertools
import importlib.util
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("x1", os.path.join(here, "x1_jk_flow_float.py"))
x1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x1)


def givens90(d, i, j):
    L = np.eye(d)
    L[i, i] = 0; L[j, j] = 0; L[j, i] = 1; L[i, j] = -1
    return L


def hom_map(L):
    d = L.shape[0]
    H = np.eye(d + 1)
    H[1:, 1:] = L
    return H


d = 5
n = d + 1
res = []
for (i, j) in itertools.combinations(range(d), 2):
    L = givens90(d, i, j)
    H = hom_map(L)
    for side in ("control", "target"):
        Loc = np.kron(H, np.eye(n)) if side == "control" else np.kron(np.eye(n), H)
        for t, s in itertools.product((np.pi / 2, np.pi), repeat=2):
            W = x1.gate(d, s) @ Loc @ x1.gate(d, t)
            m, wit = x1.minimise(W, d, iters=800, restarts=8)
            res.append((m, i, j, side, t, s, wit))
            print(f"plane ({i},{j}) {side:7s} t={t:.3f} s={s:.3f}: min {m:+.4f}")
            sys.stdout.flush()
res.sort(key=lambda r: r[0])
m, i, j, side, t, s, (x, y, a, b) = res[0]
print("BEST", m, (i, j), side, t, s)
print("x", x.tolist()); print("y", y.tolist()); print("a", a.tolist()); print("b", b.tolist())

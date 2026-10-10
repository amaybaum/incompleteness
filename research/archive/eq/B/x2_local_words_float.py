"""EXPLORATION ONLY (floating point; certifies nothing).

Does the J/K flow survive the addition of local rotations?  Words W = G_s (L (x) I) G_t and
W = G_s (I (x) L) G_t with L a random rotation of the d-ball (d = 3 control: must stay positive, since all
such words are QT channels; d = 5: Krumm-Mueller predicts a failure).  We minimise the posFwd value
pairVal(e, f, W(hom x (x) hom y)) over unit x, y and extreme effects (1, a), (1, b).
Prints the best witness found for d = 5 to seed the exact certificate (b5).
"""
import numpy as np
import sys
import importlib.util
import os

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("x1", os.path.join(here, "x1_jk_flow_float.py"))
x1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x1)

rng = np.random.default_rng(777)


def rand_rot(d):
    A = rng.normal(size=(d, d))
    Qm, R = np.linalg.qr(A)
    Qm = Qm @ np.diag(np.sign(np.diag(R)))
    if np.linalg.det(Qm) < 0:
        Qm[:, 0] *= -1
    return Qm


def hom_map(L):
    d = L.shape[0]
    H = np.eye(d + 1)
    H[1:, 1:] = L
    return H


def run(d, side, trials=6):
    n = d + 1
    worst = (np.inf, None)
    for tr in range(trials):
        L = rand_rot(d)
        H = hom_map(L)
        Loc = np.kron(H, np.eye(n)) if side == "control" else np.kron(np.eye(n), H)
        t, s = rng.uniform(0.3, 3.0), rng.uniform(0.3, 3.0)
        W = x1.gate(d, s) @ Loc @ x1.gate(d, t)
        m, wit = x1.minimise(W, d, iters=1500, restarts=20)
        if m < worst[0]:
            worst = (m, (L, t, s, wit))
    return worst


if __name__ == "__main__":
    for d in (3, 5):
        for side in ("control", "target"):
            m, data = run(d, side)
            print(f"d={d} local rotation on {side}: min posFwd value over words G_s (L) G_t: {m:+.4e}")
            sys.stdout.flush()
            if d == 5 and m < -1e-3:
                L, t, s, (x, y, a, b) = data
                np.set_printoptions(precision=6, suppress=True)
                print("   witness t, s =", t, s)
                print("   L =", L.tolist())
                print("   x =", x.tolist(), " y =", y.tolist())
                print("   a =", a.tolist(), " b =", b.tolist())

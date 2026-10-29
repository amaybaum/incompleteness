#!/usr/bin/env python3
"""Map (b) at the lyapunov_v3.py size (3D, L=20, q=2^16), exact integers, sampled (not exhaustive).
Per step: is E_q = u.u + v.v - 3^{-1} u.A v (mod 2^16) conserved?  Relative change of the lifted real
energy E_R3 = 3(u.u+v.v) - u.A v on representatives [0,q) (the alpha=1/3 harmonic energy times 3).
Two ensembles: the uniform (infinite-temperature) ensemble lyapunov_v3 uses, and a smooth low-amplitude
state around q/2 (mixing_battery's mode shape) where no wraparound occurs at first.
Control: the same diagnostics on the exact real alpha=1/3 linear map in float64 (E_R3 conserved to rounding)."""
import numpy as np
L, q = 20, 1 << 16
inv3 = pow(3, -1, q)
def nn(x): return sum(np.roll(x, s, a) for a in range(3) for s in (1, -1))
def step_b(cur, prv): return (((nn(cur) + 1) // 3) - prv) % q
def Eq(cur, prv): return int(((prv * prv).sum() + (cur * cur).sum() - inv3 * (prv * nn(cur)).sum()) % q)
def ER3(cur, prv, c=0):
    a = cur.astype(np.float64) - c; b = prv.astype(np.float64) - c
    return 3 * ((a * a).sum() + (b * b).sum()) - (b * nn(a)).sum()
rng = np.random.default_rng(11)
chg = 0; rel = []
for _ in range(200):
    c = rng.integers(0, q, (L, L, L)); p = rng.integers(0, q, (L, L, L))
    c2 = step_b(c, p)
    chg += Eq(c2, c) != Eq(c, p)
    rel.append(abs(ER3(c2, c) - ER3(c, p)) / abs(ER3(c, p)))
print(f"uniform ensemble, 200 states: E_q (mod 2^16, alpha=3^-1) changed in one step for {chg}/200; "
      f"median one-step |dE_R3|/E_R3 = {np.median(rel):.3f}")
x = np.arange(L)
mode = (q // 2 + (q // 8) * np.cos(2 * np.pi * x / L))[:, None, None] * np.ones((1, L, L))
c = np.rint(mode).astype(np.int64) % q; p = c.copy()
E0 = ER3(c, p, q // 2); dev = []; eqc = 0
cf = c.astype(np.float64) - q // 2; pf = cf.copy(); E0f = ER3(cf, pf)
devf = []
for t in range(400):
    e_before = Eq(c, p); c, p = step_b(c, p), c; eqc += Eq(c, p) != e_before
    dev.append(abs(ER3(c, p, q // 2) - E0) / abs(E0))
    cf, pf = nn(cf) / 3.0 - pf, cf; devf.append(abs(ER3(cf, pf) - E0f) / abs(E0f))
print(f"smooth mode (no initial wraparound): E_q changed at {eqc}/400 steps; max relative drift of E_R3 "
      f"(centred) over 400 steps = {max(dev):.2e}; final = {dev[-1]:.2e}")
print(f"control, exact real linear alpha=1/3 map from the same state: max relative drift = {max(devf):.2e}")

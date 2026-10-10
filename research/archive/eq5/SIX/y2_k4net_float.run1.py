"""EQ4-SIX exploration y2 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  The six-token glue network (crossing split): states x on (p, r1, r2), y on (q, u1, u2) glued by
the Bell effect on (p, q); effects e on (s, r1, u1), f on (t, r2, u2) glued by the Bell state on (s, t);
  N = 1/4 sum e[s r1 u1; s' r1' u1'] f[s r2 u2; s' r2' u2'] x[p' r1' r2'; p r1 r2] y[p' u1' u2'; p u1 u2].
With co-self-duality e = T(x~), f = T(y~) for x~, y~ in K3.  Nodes are local-filter images Ad(k) g of K_A generators g
(as GHZ-diagonal operators), so a negative value would be a lead for an obstruction to every K3 containing Lift(K_A).
Controls: PSD nodes give N >= 0; GHZ states against W3 effects give a negative value (the network detects GHZ vs W3).
Also the same-split network N0 for comparison.
"""
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(2026100902)


def idx(x, y, z):
    return 4 * x + 2 * y + z


P = []
for b in range(4):
    b1, b2 = b >> 1, b & 1
    for t in range(2):
        v = np.zeros(8)
        v[idx(0, b1, b2)] = 1
        v[idx(1, 1 - b1, 1 - b2)] = 1 if t == 0 else -1
        P.append(np.outer(v, v) / 2)
I8 = np.eye(8)
NEG = [I8 - 2 * P[j] for j in range(8)] + [I8 - 2 * P[j] + 2 * P[p] for j in range(8) for p in range(8) if p != j]
POS = [P[j] + P[k] for j in range(8) for k in range(j + 1, 8)]
GENS = NEG + POS


def t6(M):
    return M.reshape(2, 2, 2, 2, 2, 2)


def net_cross(x, y, e, f):
    return 0.25 * np.real(np.einsum("abcdef,aghdij,keilbg,kfjlch->", t6(e), t6(f), t6(x), t6(y)))


def net_same(x, y, e, f):
    # effects e on (s, r1, r2), f on (t, u1, u2)
    return 0.25 * np.real(np.einsum("abgdei,achdfj,keilbg,kfjlch->", t6(e), t6(f), t6(x), t6(y)))


def gl2(p):
    return (p[0:4] + 1j * p[4:8]).reshape(2, 2)


def kmat(p):
    return np.kron(np.kron(gl2(p[0:8]), gl2(p[8:16])), gl2(p[16:24]))


def ad(p, g):
    k = kmat(p)
    return k @ g @ k.conj().T


def nodes(p, gs):
    x = ad(p[0:24], gs[0])
    y = ad(p[24:48], gs[1])
    e = ad(p[48:72], gs[2]).T
    f = ad(p[72:96], gs[3]).T
    return x, y, e, f


def val(p, gs, net):
    x, y, e, f = nodes(p, gs)
    nrm = np.linalg.norm(x) * np.linalg.norm(y) * np.linalg.norm(e) * np.linalg.norm(f)
    return net(x, y, e, f) / max(nrm, 1e-300)


# controls
ghz = P[0]
w3 = I8 / 2 - P[0]
psd = [np.outer(v, v.conj()) for v in rng.normal(size=(4, 8)) + 1j * rng.normal(size=(4, 8))]
print("control PSD nodes: cross %.4f same %.4f" % (net_cross(*psd), net_same(*psd)), flush=True)
print("control GHZ states, W3 effects: cross %.4f same %.4f" % (net_cross(ghz, ghz, w3, w3), net_same(ghz, ghz, w3, w3)),
      flush=True)
print("control W3 everywhere: cross %.4f same %.4f" % (net_cross(w3, w3, w3, w3), net_same(w3, w3, w3, w3)), flush=True)
kap = I8 / 2 + P[0] - P[1]
print("kappa everywhere: cross %.4f same %.4f" % (net_cross(kap, kap, kap, kap), net_same(kap, kap, kap, kap)), flush=True)

# unfiltered exhaustive minimum over generator choices for the crossing split (NEG x NEG x NEG x NEG sampled)
best = (np.inf, None)
for trial in range(20000):
    gi = rng.integers(len(GENS), size=4)
    v = net_cross(GENS[gi[0]], GENS[gi[1]], GENS[gi[2]].T, GENS[gi[3]].T)
    if v < best[0]:
        best = (v, tuple(gi))
print("unfiltered random 20000 generator quadruples: min cross value %.4f at %s" % best, flush=True)

for net, nm in ((net_cross, "cross"), (net_same, "same")):
    worst = (np.inf, None)
    for trial in range(400):
        gi = rng.integers(len(NEG), size=4)
        gs = [NEG[i] for i in gi]
        r = minimize(val, rng.normal(size=96), args=(gs, net), method="BFGS", options={"maxiter": 4000, "gtol": 1e-12})
        if r.fun < worst[0]:
            worst = (r.fun, tuple(gi))
    print("%s split: filtered BFGS over 400 random NEG quadruples: worst normalized min %.4e at %s" % (nm, worst[0], worst[1]),
          flush=True)
print("done", file=sys.stderr)

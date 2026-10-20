"""A9: float rank (Gram eigenvalues) of the tight rows at the reference, G-side and G+H-side (H = R^-1, first-order)."""
import json, os, sys
import numpy as np
PRE, WORK, control = sys.argv[1:4]
sys.path.insert(0, PRE)
import controls_gen as cg, controls_verify as cv
body = cv.Body(control); prob = cg.Problem(json.load(open(os.path.join(WORK, 'pool-%s.json' % control))))
nn = prob.n ** 2
if len(sys.argv) > 4:   # widen the pool: 'AB' = pools A and B; 'AB+' = A, B and a third seeded draw C
    from fractions import Fraction as Fr
    import random
    names = ['A', 'B']
    if sys.argv[4] == 'AB+':
        u = cv.units3(); used = set(tuple(x) for k in 'AB' for x in [tuple(s[1:4]) for s in body.pools[k]['states']])
        rest = [x for x in u if tuple(x) not in used]
        cv.POOL_SIZE[control] = int(sys.argv[5]) if len(sys.argv) > 5 else cv.POOL_SIZE[control]
        rng = random.Random(20261020); extra = rng.sample(rest, cv.POOL_SIZE[control])
        b2 = cv.Body.__new__(cv.Body)
    prob.S = np.array([[1.0] + [float(c) for c in s] for k in names for s in body.pools[k]['states']])
    prob.E = np.array([[float(c) for c in e] for k in names for e in body.pools[k]['effects']])
    prob.ns, prob.ne = len(prob.S), len(prob.E)
    print('pools', names, 'states', prob.ns, 'effects', prob.ne)
R = np.array([[float(v) for v in r] for r in body.reference]); Ri = np.linalg.inv(R)
EF = np.einsum('am,bn->abmn', prob.E, prob.E).reshape(prob.ne, prob.ne, nn)
W = np.einsum('xk,yl->xykl', prob.S, prob.S).reshape(prob.ns, prob.ns, nn)
def gram(tq, M):
    Gm = np.zeros((prob.nv, prob.nv))
    for s in range(0, len(tq), 4000):
        q = tq[s:s + 4000]
        ef = EF[q[:, 2], q[:, 3]]; w = W[q[:, 0], q[:, 1]]
        if M is not None:
            ef = ef @ M; w = w @ M.T
        rows = (ef[:, prob.fp] * w[:, prob.fq]) @ prob.Nmat
        Gm += rows.T @ rows
    return Gm
vG = prob.values(R); vH = prob.values(Ri)
tG = np.argwhere(np.abs(vG) < 1e-12); tH = np.argwhere(np.abs(vH) < 1e-12)
gG = gram(tG, None); gH = gram(tH, Ri)
for name, g in (('G-side', gG), ('G+H-side', gG + gH)):
    ev = np.linalg.eigvalsh(g); ev = np.clip(ev, 0, None)
    rk = int((np.sqrt(ev) > 1e-7 * np.sqrt(ev.max())).sum())
    print('%s %s: tight %d/%d; float rank %d of dim F %d; smallest kept sqrt-eig %.2e, largest dropped %.2e'
          % (control, name, len(tG), len(tH), rk, prob.nv, np.sort(np.sqrt(ev))[-rk], np.sort(np.sqrt(ev))[-rk - 1] if rk < prob.nv else 0))

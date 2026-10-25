"""PC zero / PC firing for the embedded class P_emb(m<=2), full-state simulation, exact counts.
Checks only the plan's control facts; it computes no verdict-bearing measurement."""
import importlib.util, sys
from itertools import permutations, product
from collections import Counter
from fractions import Fraction as Fr

spec = importlib.util.spec_from_file_location("c", sys.argv[1])
c = importlib.util.module_from_spec(spec)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(c)


def observers(m):
    M = 2 ** m
    perms = list(permutations(range(M)))
    for r0 in perms:
        for r1 in perms:
            for a in product((0, 1), repeat=M):
                yield r0, r1, a


def joint_P(phi, n, obs, K):
    r0, r1, a = obs
    cnt = Counter()
    for (x, h) in c.states(n):
        v = 0
        s = (x, h)
        for _ in range(K):
            x = s[0]
            v = (r1 if x else r0)[v]
            s = (x ^ a[v], s[1])
            s = phi(s)
        cnt[(v, s[0])] += 1
    return cnt, 2 ** (n + 1)


def joint_Q(obs, K, m):
    r0, r1, a = obs
    dist = Counter({(0, None): 1})  # v, weight over 2^t
    vd = Counter({0: 1})
    # x_0 fair; each step: v <- rho_x(v) with x fair fresh; record x_K fair fresh
    for _ in range(K):
        nd = Counter()
        for v, w in vd.items():
            for x in (0, 1):
                nd[(r1 if x else r0)[v]] += w
        vd = nd
    # v_K has weight over 2^K, x_K fair
    out = Counter()
    for v, w in vd.items():
        for x in (0, 1):
            out[(v, x)] += w
    return out, 2 ** (K + 1)


def tv(Pc, Pd, Qc, Qd):
    keys = set(Pc) | set(Qc)
    return sum(abs(Fr(Pc.get(k, 0), Pd) - Fr(Qc.get(k, 0), Qd)) for k in keys) / 2


for n in (3, 4):
    phi = c.gen("lin", n, c.P[n])
    worst = Fr(0)
    for m in (1, 2):
        for obs in observers(m):
            for K in range(n + 1):
                Pc, Pd = joint_P(phi, n, obs, K)
                Qc, Qd = joint_Q(obs, K, m)
                worst = max(worst, tv(Pc, Pd, Qc, Qd))
    print(f"PC zero, G_lin n={n}, all P_emb(m<=2) incl. active, K<=n: max TV over F = {worst}")

phi = c.gen("dec", 3, c.P[3])
obs = ((0, 1), (1, 0), (0, 0))  # rho0=id, rho1=flip, a=0
Pc, Pd = joint_P(phi, 3, obs, 1)
Qc, Qd = joint_Q(obs, 1, 1)
pP = Fr(sum(w for (v, x), w in Pc.items() if v == x), Pd)
pQ = Fr(sum(w for (v, x), w in Qc.items() if v == x), Qd)
print("PC firing P_emb(1) on G_dec K=1: Pr_P", pP, "Pr_Q", pQ, "adv", abs(pP - pQ))

"""Independent brute force of adv^pred for P^emb(m) observers (no PE-01 code used for the reference)."""
import sys, itertools
from fractions import Fraction
PKG = sys.argv[1]
sys.path.insert(0, PKG)

P = {3: (3, 1, 0), 4: (4, 1, 0), 5: (5, 2, 0)}
def L(h, n, exps):
    bits = [(h >> i) & 1 for i in range(n)]
    fb = 0
    for e in exps:
        if e < n: fb ^= bits[e]
    nb = bits[1:] + [fb]
    return sum(b << i for i, b in enumerate(nb))
def mk(fam, n):
    ex = P[n]
    def sig(x, h):
        if fam == "clk" and x == 1: return L(L(h, n, ex), n, ex)
        return L(h, n, ex)
    def f(h):
        b0, b1, b2 = h & 1, (h >> 1) & 1, (h >> 2) & 1
        return b0 ^ (b1 & b2) if fam == "filt" else b0
    return sig, f

def adv_table(fam, n, m, Kmax):
    """For every observer (r0, r1, a) and chi: Pr[chi(v_K) = x_K] for K = 0..Kmax, as Fractions."""
    sig, f = mk(fam, n)
    V = 1 << m
    perms = list(itertools.permutations(range(V)))
    res = {}
    seeds = [(x, h) for h in range(1 << n) for x in (0, 1)]
    Mtot = len(seeds)
    for r0 in perms:
        for r1 in perms:
            for a in range(1 << V):
                cnt = [[[0, 0] for _ in range(V)] for _ in range(Kmax + 1)]
                for x, h in seeds:
                    v = 0
                    for K in range(Kmax + 1):
                        cnt[K][v][x] += 1
                        v = (r0, r1)[x][v]
                        c = x ^ ((a >> v) & 1)
                        h = sig(c, h)
                        x = c ^ f(h)
                for chi in range(1 << V):
                    res[(r0, r1, a, chi)] = [Fraction(sum(cnt[K][v][(chi >> v) & 1] for v in range(V)), Mtot) - Fraction(1, 2)
                                             for K in range(Kmax + 1)]
    return res

if __name__ == "__main__":
    import numpy as np
    from pe01 import generators as G, observers as O, embedded as E
    for fam, n, m, Kmax in (("clk", 3, 1, 14), ("filt", 4, 1, 20), ("clk", 4, 1, 20), ("lin", 3, 1, 12), ("clk", 3, 2, 10)):
        res = adv_table(fam, n, m, Kmax)
        # K1 prediction max, overall and passive
        best = [max(abs(v[K]) for v in res.values()) for K in range(Kmax + 1)]
        bestp = [max(abs(v[K]) for k, v in res.items() if k[2] == 0) for K in range(Kmax + 1)]
        # window witnesses (|adv| >= 1/8 at K-3..K, same O, chi)
        win = {K: sum(1 for v in res.values() if all(abs(v[t]) >= Fraction(1, 8) for t in range(K - 3, K + 1))) for K in range(3, Kmax + 1)}
        wins = {K: sum(1 for v in res.values() if all(v[t] >= Fraction(1, 8) for t in range(K - 3, K + 1)) or all(v[t] <= -Fraction(1, 8) for t in range(K - 3, K + 1))) for K in range(3, Kmax + 1)}
        # their sweep
        g = G.make(fam, n, G.p_n(n))
        obs = O.all_observers(m)
        sw = E.Sweep(obs, [g], [Kmax], [0], [0], None, "det", {"all": np.ones(obs.n, bool), "passive": obs.passive.copy()},
                     window_cap={0: Kmax}).run()
        theirs = [E.k1_pred_value(sw.k1p[("all", 0)][K][0], g.M) for K in range(Kmax + 1)]
        theirsp = [E.k1_pred_value(sw.k1p[("passive", 0)][K][0], g.M) for K in range(Kmax + 1)]
        twin = {K: sw.win[("all", 0)].get(K, {"count": 0})["count"] for K in range(3, Kmax + 1)}
        print(fam, n, m, "K1pred all equal:", best == theirs, "passive equal:", bestp == theirsp,
              "window counts equal:", win == twin)
        print("  K1 pred:", [str(x) for x in best])
        print("  window |adv| counts:", win)
        print("  window signed-consistent counts:", wins)

"""Independent K0 (worst, average) over tests (rho, a, F) for m = 1 on a family; and the U K1 TV."""
import sys, itertools
from fractions import Fraction
PKG = sys.argv[1]
sys.path.insert(0, PKG)
def prim_polys(n):
    out = []
    for p in range((1 << n) | 1, 1 << (n + 1), 2):
        x, k = 2, 1
        while x != 1 and k <= (1 << n):
            x <<= 1
            if x >> n & 1: x ^= p
            k += 1
        if k == (1 << n) - 1: out.append(p)
    return out
def mk(fam, n, p):
    def L(h):
        fb = bin(h & p & ((1 << n) - 1)).count("1") & 1
        return (h >> 1) | (fb << (n - 1))
    sig = lambda x, h: L(L(h)) if (fam == "clk" and x) else L(h)
    f = (lambda h: (h & 1) ^ ((h >> 1) & (h >> 2) & 1)) if fam == "filt" else (lambda h: h & 1)
    return sig, f
def cells(fam, n, p, r0, r1, a, K):
    sig, f = mk(fam, n, p)
    C = {}
    for h0 in range(1 << n):
        for x0 in (0, 1):
            x, h, v = x0, h0, 0
            for _ in range(K):
                v = (r0, r1)[x][v]
                c = x ^ a[v]
                h = sig(c, h)
                x = c ^ f(h)
            C[(v, x)] = C.get((v, x), 0) + 1
    M = 2 << n
    # Q: v driven by K fair bits; x_K fair
    q = {0: Fraction(1)}
    for _ in range(K):
        nq = {}
        for v, pr in q.items():
            for x in (0, 1):
                w = (r0, r1)[x][v]
                nq[w] = nq.get(w, 0) + pr / 2
        q = nq
    return {(v, x): Fraction(C.get((v, x), 0), M) - q.get(v, 0) / 2 for v in (0, 1) for x in (0, 1)}
if __name__ == "__main__":
    import numpy as np
    from pe01 import generators as G, observers as O, embedded as E
    perms = [(0, 1), (1, 0)]
    for fam, n, Kmax in (("clk", 3, 9), ("filt", 4, 9), ("lin", 4, 9)):
        ps = prim_polys(n)
        gens = [G.make(fam, n, p) for p in ps]
        obs = O.all_observers(1)
        sw = E.Sweep(obs, gens, [Kmax] * len(gens), list(range(len(gens))), [0], Kmax, "det",
                     {"all": np.ones(obs.n, bool)}).run()
        okw = oka = True
        for K in range(Kmax + 1):
            bw, ba = Fraction(-1), Fraction(-1)
            for r0 in perms:
                for r1 in perms:
                    for a in itertools.product((0, 1), repeat=2):
                        D = [cells(fam, n, p, r0, r1, a, K) for p in ps]
                        for Fm in range(16):
                            sel = [(c >> 1, c & 1) for c in range(4) if Fm >> c & 1]
                            vals = [abs(sum(d[c] for c in sel)) for d in D]
                            bw = max(bw, min(vals)); ba = max(ba, sum(vals) / len(vals))
            w, a_ = sw.k0w["all"][K], sw.k0a["all"][K]
            tw, ta = Fraction(w[0], gens[0].M * w[3]), Fraction(a_[0], gens[0].M * a_[3] * len(gens))
            okw &= tw == bw; oka &= ta == ba
            if K in (0, 4, Kmax): print(fam, n, K, "worst", bw, tw, "avg", ba, ta)
        print(fam, n, "K0 worst equal:", okw, "K0 average equal:", oka)

"""Numerical (floating-point) CP-divisibility control for the permutation-dilation family.

For every DISTINCT pair (Phi_s, Phi_t) of superoperators arising at (|V|,|H|) in
{(2,2),(2,3),(3,2)} with the priors of cp_search.py, classify:
  - exact stochastic divisibility of the populations (cp_search / exact_lp);
  - exact linear compatibility (some linear Lambda with Lambda.Phi_s = Phi_t);
  - numerical gap between the PSD Choi cone and the affine set of TP Lambda with
    Lambda.Phi_s = Phi_t (alternating projections; 0 => CP-divisible numerically).
The theorem predicts: P-indivisible  =>  gap > 0 for every pair.
"""
import itertools, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import cp_search as c
from exact_lp import stochastic_divisor

ITERS = int(sys.argv[1]) if len(sys.argv) > 1 else 1500


def adU(U, n):
    U = np.array(U)
    S = np.zeros((n * n, n * n))
    for a in range(n):
        for b in range(n):
            E = np.zeros((n, n)); E[a, b] = 1
            X = U @ E @ U.T
            S[:, a * n + b] = X.reshape(-1)
    return S.tolist()


def controls():
    Hd = [[2 ** -0.5, 2 ** -0.5], [2 ** -0.5, -2 ** -0.5]]
    Id4 = np.eye(4).tolist()
    deph = np.diag([1, 0, 0, 1]).astype(float).tolist()
    transp = np.zeros((4, 4))
    for a in range(2):
        for b in range(2):
            transp[b * 2 + a, a * 2 + b] = 1
    print("controls (gap after %d iterations):" % ITERS)
    print("  +  Ad_H -> id (Hadamard remark, CP-divisible)   %.2e" % c.cp_gap(adU(Hd, 2), Id4, 2, ITERS))
    print("  +  id -> dephasing (CP-divisible)               %.2e" % c.cp_gap(Id4, deph, 2, ITERS))
    print("  -  id -> transpose (positive, not CP)           %.2e" % c.cp_gap(Id4, transp.tolist(), 2, ITERS))
    print("  -  dephasing -> id (no linear Lambda)           %s" % c.cp_gap(deph, Id4, 2, ITERS), flush=True)


def main():
    t0 = time.time()
    controls()
    seen = {}
    for (nV, nH) in [(2, 2), (2, 3), (3, 2)]:
        N = nV * nH
        for perm in itertools.permutations(range(N)):
            perm = list(perm)
            L = c.order(perm)
            for mu in c.priors(nH):
                Ss = {t: c.superop(c.perm_power(perm, t), nV, nH, mu) for t in range(L)}
                for s in range(1, L):
                    for t in range(L):
                        if t == s:
                            continue
                        key = (nV, tuple(map(tuple, Ss[s])), tuple(map(tuple, Ss[t])))
                        if key in seen:
                            continue
                        seen[key] = (nV, nH, tuple(perm), mu, s, t)
    print("distinct (Phi_s, Phi_t) pairs:", len(seen), f"[{time.time()-t0:.0f}s]", flush=True)
    rows = []
    for k, (key, info) in enumerate(seen.items()):
        nV = key[0]
        S1 = [list(r) for r in key[1]]; S2 = [list(r) for r in key[2]]
        T1 = c.pops(S1, nV); T2 = c.pops(S2, nV)
        pdiv = stochastic_divisor(T1, T2)[0]
        lc = c.lin_compatible(S1, S2)
        gap = c.cp_gap(S1, S2, nV, ITERS) if lc else float("inf")
        rows.append((pdiv, lc, gap, info))
        if k % 500 == 0:
            print("  ..", k, f"[{time.time()-t0:.0f}s]", flush=True)
    def cnt(pred):
        return sum(1 for r in rows if pred(r))
    print("\nRESULTS (distinct pairs):")
    print("  P-indivisible:", cnt(lambda r: not r[0]),
          "| of which linearly compatible:", cnt(lambda r: not r[0] and r[1]))
    gi = sorted((r for r in rows if not r[0]), key=lambda r: r[2])
    if gi:
        print("  P-indivisible: min numerical gap = %.3e at %s" % (gi[0][2], gi[0][3]))
        print("  P-indivisible with gap < 1e-3 (would be a counterexample):", cnt(lambda r: not r[0] and r[2] < 1e-3))
    print("  P-divisible:", cnt(lambda r: r[0]),
          "| linearly incompatible (exactly CP-indivisible):", cnt(lambda r: r[0] and not r[1]),
          "| gap<1e-4:", cnt(lambda r: r[0] and r[2] < 1e-4),
          "| gap>1e-3 finite:", cnt(lambda r: r[0] and 1e-3 < r[2] < float('inf')),
          "| ambiguous:", cnt(lambda r: r[0] and 1e-4 <= r[2] <= 1e-3))
    gd = sorted((r for r in rows if r[0] and r[1]), key=lambda r: -r[2])
    for r in gd[:3]:
        print("   P-divisible, lin-compatible, largest gap %.3e  %s" % (r[2], r[3]))
    print(f"done [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main()

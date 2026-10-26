#!/usr/bin/env python3
"""E2: exact re-examination of Main.md:594 ("at (n_V,|C_H|) = (2,3) the minimum equals M_t for only
one of fifteen distinct processes ... residuals up to 0.667 bits", memory_probes.py) and of the
audit's arbitrary-prior recheck (matrix/scripts/b4probe/fixeddim.py, "2 of 16", Nelder-Mead).

Exact criterion used here. In a deterministic realization X3 = f(X2, H2), so
  I(X<2; H2 | X2) - M_2 = I(X<2; H2 | X2, X3)  (chain rule; M_2 := I(X<2; X3 | X2)),
which is zero iff, for every (x2, x3), the conditional law of H2 given (x0, x1, x2, x3) is the
same for every supported (x0, x1). With rational priors this is an exact Fraction test.
For the arbitrary-prior question: states of one path class (x0..x3) have distinct H2 values
(phi^2 is injective and they share x2), so a prior reproducing the law can put any within-class
split on its class; the infimum (attained: compact feasible set) equals M_2 iff some
permutation has every path of the law as a nonempty class and, for each (x2, x3), the H2-value
sets of the supported classes have a common element. Entropy values are printed in floating
point only as diagnostics; no verdict uses them.

Usage: python3 -I E2_memory_exact.py [out.json]   (out.json must not be this script)
"""
import json, os, sys
from fractions import Fraction as F
from itertools import permutations
from math import log2

nV, nH = 2, 3
N = nV * nH

def run(perm, mu):
    """list of (path (x0..x3), h2, weight) for a prior mu on states."""
    out = []
    for s in range(N):
        if mu[s] == 0:
            continue
        p = [s // nH]; t = s
        for k in range(3):
            t = perm[t]; p.append(t // nH)
            if k == 1:
                h2 = t % nH
        out.append((tuple(p), h2, mu[s]))
    return out

def law(rows):
    L = {}
    for p, _, w in rows:
        L[p] = L.get(p, 0) + w
    return L

def conditionals(L):
    """P(x3 | x0, x1, x2) on supported histories."""
    tot = {}
    for p, w in L.items():
        tot[p[:3]] = tot.get(p[:3], 0) + w
    return {p: w / tot[p[:3]] for p, w in L.items()}

def mt_positive(L):
    c = conditionals(L)
    by = {}
    for p in c:
        by.setdefault(p[2], {}).setdefault(p[:2], {})[p[3]] = c[p]
    return any(len({tuple(sorted(d.items())) for d in hs.values()}) > 1 for hs in by.values())

def ci_attains(rows):
    """exact: I(X<2; H2 | X2, X3) == 0."""
    by = {}
    for p, h2, w in rows:
        by.setdefault((p[2], p[3]), {}).setdefault(p[:2], {})
        d = by[(p[2], p[3])][p[:2]]; d[h2] = d.get(h2, 0) + w
    for hs in by.values():
        norm = set()
        for d in hs.values():
            z = sum(d.values()); norm.add(tuple(sorted((h, v / z) for h, v in d.items())))
        if len(norm) > 1:
            return False
    return True

def cmi(rows, a, c, b):
    """float I(A;B|C) in bits; diagnostic only."""
    J = {}
    for p, h2, w in rows:
        k = (a(p, h2), c(p, h2), b(p, h2)); J[k] = J.get(k, 0) + w
    pc, pac, pcb = {}, {}, {}
    for (x, y, z), w in J.items():
        pc[y] = pc.get(y, 0) + w; pac[(x, y)] = pac.get((x, y), 0) + w; pcb[(y, z)] = pcb.get((y, z), 0) + w
    return sum(float(w) * log2(float(w * pc[y] / (pac[(x, y)] * pcb[(y, z)]))) for (x, y, z), w in J.items() if w)

def main():
    uni = [F(1, N)] * N
    perms = list(permutations(range(N)))
    # (1) memory_probes grouping: by the t=2 conditional signature, uniform prior only
    groups = {}
    for perm in perms:
        rows = run(perm, uni)
        L = law(rows)
        groups.setdefault(tuple(sorted(conditionals(L).items())), []).append((perm, rows, L))
    g_pos = [g for g in groups.values() if mt_positive(g[0][2])]
    att_sig = sum(any(ci_attains(r) for _, r, _ in g) for g in g_pos)
    merged = []
    for g in g_pos:
        per = {}
        for _, r, L in g:
            per.setdefault(tuple(sorted(L.items())), set()).add(ci_attains(r))
        if len(per) > 1:
            merged.append([sorted(v) for v in per.values()])
    resid, spread = [], []
    for g in g_pos:
        M = [cmi(r, lambda p, h: p[:2], lambda p, h: p[2], lambda p, h: p[3]) for _, r, _ in g]
        I = [cmi(r, lambda p, h: p[:2], lambda p, h: p[2], lambda p, h: h) for _, r, _ in g]
        resid.append(min(I) - M[0]); spread.append(max(M) - min(M))
    # (2) the B4 grouping: by the full law of (X0..X3) under the uniform prior; attainment over all priors
    targets = {}
    for perm in perms:
        L = law(run(perm, uni))
        targets.setdefault(tuple(sorted(L.items())), L)
    t_pos = [L for L in targets.values() if mt_positive(L)]
    classes = []
    for perm in perms:
        cls = {}
        for s in range(N):
            p, h2, _ = run(perm, [F(int(i == s)) for i in range(N)])[0]
            cls.setdefault(p, set()).add(h2)
        classes.append(cls)
    uni_attain = any_attain = 0
    for L in t_pos:
        ok_any = False
        for cls in classes:
            if any(p not in cls for p in L):
                continue
            by = {}
            for p in L:
                by.setdefault((p[2], p[3]), []).append(cls[p])
            if all(set.intersection(*v) for v in by.values()):
                ok_any = True
                break
        any_attain += ok_any
        uni_attain += any(ci_attains(run(perm, uni)) for perm in perms if law(run(perm, uni)) == L)
    return {"realizations_checked": len(perms),
            "signature_groups_with_Mt_pos": len(g_pos),
            "signature_groups_attained_uniform_prior_exact": att_sig,
            "signature_groups_merging_several_full_laws": merged,
            "max_residual_bits_float": max(resid),
            "max_spread_of_Mt_within_signature_group_float": max(spread),
            "full_laws_with_Mt_pos": len(t_pos),
            "full_laws_attained_uniform_prior_exact": uni_attain,
            "full_laws_attained_some_prior_exact": any_attain}

if __name__ == "__main__":
    out = main()
    js = json.dumps(out, indent=1)
    if len(sys.argv) > 1:
        if os.path.abspath(sys.argv[1]) == os.path.abspath(__file__):
            sys.exit("refusing to overwrite this script")
        open(sys.argv[1], "w").write(js + "\n")
    print(js)

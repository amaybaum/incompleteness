"""P3 -- exact generic check (#1049 re-assessment, WIP / UNVERIFIED, model-written).

Paper claim checked (scope of the sector split in Lemma G1, quarter-phase DESIGN node 1):
  For ANY (possibly non-affine) second-order rule u' = F(u restricted to neighbours) - v, v' = u
  whose update at i reads only graph-neighbours of i (no centre, no same-colour site) on a
  bipartite graph, u_i(t) depends only on initial variables of type t + chi_i, and v_i(t) only
  on type t + chi_i + 1 (dependence = support: changing that variable can change the slot).
Generic random local functions per site, per tick; exhaustive over all initial states.
Countercontrols: a rule that also reads the centre, and one that reads the same-colour site
i+2 (the pattern of SM:112's switched edge), break the split.
Not a computation on an OI mechanism; no premise adopted.
"""
import itertools, random, sys
random.seed(10492)

def run(n, q, T, mode):
    # random local functions: f_{t,i}(a, b) for the two ring-neighbours (and extra arg if needed)
    nargs = 3 if mode in ("centre", "i+2") else 2
    tabs = [[{k: random.randrange(q) for k in itertools.product(range(q), repeat=nargs)}
             for _ in range(n)] for _ in range(T)]
    def evolve(z):
        u, v = list(z[:n]), list(z[n:])
        out = [(tuple(u), tuple(v))]
        for t in range(T):
            nu = []
            for i in range(n):
                args = [u[(i-1) % n], u[(i+1) % n]]
                if mode == "centre": args.append(u[i])
                if mode == "i+2": args.append(u[(i+2) % n])
                nu.append((tabs[t][i][tuple(args)] - v[i]) % q)
            u, v = nu, u
            out.append((tuple(u), tuple(v)))
        return out
    def affine(tab):
        f0 = tab[(0,)*nargs]
        e = [tab[tuple(1 if j == i else 0 for j in range(nargs))] - f0 for i in range(nargs)]
        return all((tab[k] - f0 - sum(k[i]*e[i] for i in range(nargs))) % q == 0 for k in tab)
    evolve.nonaffine = sum(not affine(tb) for row in tabs for tb in row)
    evolve.total = T * n
    return evolve

def dependence(n, q, T, evolve):
    # dep[t][slot] = set of initial variable indices whose change can change that slot
    states = list(itertools.product(range(q), repeat=2*n))
    traj = {z: evolve(z) for z in states}
    dep = [[set() for _ in range(2*n)] for _ in range(T+1)]
    for z in states:
        for k in range(2*n):
            for d in range(1, q):
                z2 = list(z); z2[k] = (z2[k] + d) % q; z2 = tuple(z2)
                for t in range(T+1):
                    for s in range(2*n):
                        a = traj[z][t][0][s] if s < n else traj[z][t][1][s-n]
                        b = traj[z2][t][0][s] if s < n else traj[z2][t][1][s-n]
                        if a != b:
                            dep[t][s].add(k)
    return dep

def split_holds(n, T, dep):
    col = [i % 2 for i in range(n)]                     # n even: proper 2-colouring of C_n
    typ = col + [(c + 1) % 2 for c in col]
    for t in range(T+1):
        for i in range(n):
            if any(typ[k] != (t + col[i]) % 2 for k in dep[t][i]): return False
            if any(typ[k] != (t + col[i] + 1) % 2 for k in dep[t][n+i]): return False
    return True

ok = True
for (n, q, T) in ((6, 2, 5), (4, 3, 4)):
    runs = [run(n, q, T, "nn") for _ in range(5)]
    print(f"  non-affine local tables among NN runs: {sum(r.nonaffine for r in runs)} of {sum(r.total for r in runs)}")
    ok &= sum(r.nonaffine for r in runs) > 0
    res = [split_holds(n, T, dependence(n, q, T, r)) for r in runs]
    cc = [split_holds(n, T, dependence(n, q, T, run(n, q, T, "centre"))) for _ in range(3)]
    c2 = [split_holds(n, T, dependence(n, q, T, run(n, q, T, "i+2"))) for _ in range(3)]
    print(f"n={n} q={q} T={T}: non-affine NN rules keep the sector split: {all(res)}; "
          f"centre-reading breaks it: {not all(cc)}; i+2-reading breaks it: {not all(c2)}")
    ok &= all(res) and (not all(cc)) and (not all(c2))
print("ALL PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)

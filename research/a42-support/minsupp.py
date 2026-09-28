"""Exact minimal support over the gauge class of an integer matrix E:
    min over integer potentials (a, b) of #{(i,j) : E_ij + a_i + b_j != 0}.
Branch and bound over row potentials, organised by the connected components of the zero graph: potentials are pairs
(component, level); two components never share a zero column (their relative offset is generic), so a column scores
the largest multiplicity of -E_ij - a_i within one component. A new row either opens a component, or joins one
component at a level that gives it a zero column with some member, and may in addition merge any further components
at an alignment that gives it a zero column with a member of each. Every realisable zero pattern arises this way, so
the search is exhaustive; the bound is: loss so far (assigned rows minus best multiplicity, summed over columns) must
stay below the incumbent's number of nonzeros."""
import sys, numpy as np, pickle

def min_support(E, start=None):
    E = [list(map(int, r)) for r in E]; n = 16
    best = [start if start is not None else n * n + 1, None]
    def loss(assign):
        tot = 0
        for j in range(n):
            cnt = {}
            for i, (c, a) in assign.items():
                key = (c, -E[i][j] - a); cnt[key] = cnt.get(key, 0) + 1
            tot += len(assign) - (max(cnt.values()) if cnt else 0)
        return tot
    def comps(assign):
        out = {}
        for i, (c, a) in assign.items(): out.setdefault(c, []).append(i)
        return out
    def rec(k, assign, nextc):
        l = loss(assign)
        if l >= best[0]: return
        if k == n:
            best[0] = l; best[1] = dict(assign); return
        i = k
        cs = comps(assign)
        # option: new component
        options = [(None, None)]
        for c, members in cs.items():
            lv = set(assign[i2][1] + E[i2][j] - E[i][j] for i2 in members for j in range(n))
            options += [(c, L) for L in lv]
        for c, L in options:
            if c is None:
                assign[i] = (nextc, 0); rec(k + 1, assign, nextc + 1); del assign[i]; continue
            others = [c2 for c2 in cs if c2 != c]
            # choose merges of the other components (each: not merged, or merged at an alignment)
            def merge(idx, asg):
                if idx == len(others):
                    asg[i] = (c, L); rec(k + 1, asg, nextc); del asg[i]; return
                c2 = others[idx]
                merge(idx + 1, asg)
                shifts = set(L - (asg[i3][1] + E[i3][j] - E[i][j]) for i3 in cs[c2] for j in range(n))
                for sh in shifts:
                    new = dict(asg)
                    for i3 in cs[c2]: new[i3] = (c, asg[i3][1] + sh)
                    merge(idx + 1, new)
            merge(0, dict(assign))
    rec(0, {}, 0)
    return best[0], best[1]

if __name__ == '__main__':
    from lib42 import WIT38, A38, B38, C38
    for nm, E in (('A', A38), ('B', B38), ('C', C38)):
        sE = sum(1 for r in E for x in r if x); r_ = min_support(E, start=sE + 1); print(nm, 'support', sE, 'min over gauge', r_[0] if r_[1] else sE, flush=True)
    s, a = min_support(WIT38, start=49); print('act-38 witness: support 48, min over gauge', s if a else 48, flush=True)
    if a:
        pot = {i: a[i][1] for i in a}; print('  potentials', pot)
    if len(sys.argv) > 1:
        d = pickle.load(open(sys.argv[1], 'rb')); X = np.array([x for R, x in d['nond']])
        E = X[0].reshape(16, 16).tolist(); s, a = min_support(E, start=41)
        print('found leaf: support', sum(1 for r in E for x in r if x), 'min over gauge', s if a else 40, flush=True)

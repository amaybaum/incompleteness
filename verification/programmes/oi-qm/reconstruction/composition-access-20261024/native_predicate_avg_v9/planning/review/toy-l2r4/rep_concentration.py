"""Reviewer probe (non-v8 analogue classes only): representatives per shard when the shard plan
splits the record index range evenly. Record order = l2plan.Space.index_of (singles by site then t;
pairs by (i<j) then t1, t2); a representative is the lexicographically minimal sorted image under
C4v about the z axis (l2analysis.canon). Pure combinatorics; no engine, no context, no closure.
Usage: python3 -I rep_concentration.py RHO NT SHARDS"""
import sys, itertools, json
rho, nt, S = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
assert rho != 4, 'v8 region radius excluded by the reviewer'
reg = sorted(c for c in itertools.product(range(-rho, rho+1), repeat=3) if sum(map(abs, c)) <= rho)
grp = []
for sw in (False, True):
    for sx in (1, -1):
        for sy in (1, -1):
            grp.append(lambda c, sw=sw, sx=sx, sy=sy: ((sx*c[1], sy*c[0], c[2]) if sw else (sx*c[0], sy*c[1], c[2])))
assert all({g(c) for c in reg} == set(reg) for g in grp)
ns = len(reg)
img = [[g(c) for c in reg] for g in grp]
idx = {c: i for i, c in enumerate(reg)}
gi = [[idx[x] for x in row] for row in img]   # site permutation per group element
N = ns*nt + ns*(ns-1)//2*nt*nt
bounds = [s*N//S for s in range(S+1)]
reps = [0]*S
def shard(k):
    lo, hi = 0, S
    while hi - lo > 1:
        mid = (lo+hi)//2
        if bounds[mid] <= k: lo = mid
        else: hi = mid
    return lo
# singles: (x,t) rep iff x minimal site in its orbit (t fixed)
for i in range(ns):
    if min(p[i] for p in gi) == i:
        for t in range(nt):
            reps[shard(i*nt + t)] += 1
# pairs: record {(x,t1),(y,t2)} with i<j; sorted tuple compares sites first (sites distinct)
base = ns*nt
sp = 0
for i in range(ns):
    for j in range(i+1, ns):
        start = base + sp*nt*nt
        # images: (p[i],t1),(p[j],t2) sorted; lexmin over g of sorted pair of (site index, t)
        # site order = reg order = index order, so compare (min site, its t, max site, its t)
        for t1 in range(nt):
            for t2 in range(nt):
                me = (i, t1, j, t2)
                best = me
                for p in gi:
                    a, b = p[i], p[j]
                    cand = (a, t1, b, t2) if a < b else (b, t2, a, t1)
                    if cand < best:
                        best = cand
                        break
                if best == me:
                    reps[shard(start + t1*nt + t2)] += 1
        sp += 1
R = sum(reps)
mean = R/S
print(json.dumps({'rho': rho, 'sites': ns, 'slices': nt, 'records': N, 'shards': S, 'representatives': R,
                  'max_over_mean': round(max(reps)/mean, 3), 'shard0_share': round(reps[0]/R, 4),
                  'top8_share': round(sum(sorted(reps)[-8:])/R, 4) if S >= 8 else None,
                  'per_shard': reps}))

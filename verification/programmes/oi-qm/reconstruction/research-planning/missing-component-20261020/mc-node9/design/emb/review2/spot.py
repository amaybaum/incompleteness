"""Independent spot checks (re-reviewer). Explicit-state forward simulation of
u'_x = sum_{z~x} u_z + v_x, v'_x = u_x over F2, plus symbolic tracking (cells as
bitmasks over initial coordinates) for own-content rank. Imports nothing from the repo."""
from itertools import product
def step(n, adj, u, v):
    nu = [ (sum(u[z] for z in adj[x]) + v[x]) & 1 for x in range(n)]
    return nu, list(u)
def sym_step(n, adj, U, V):  # U[x], V[x] bitmasks over initial coords (u_i -> bit i, v_i -> bit n+i)
    nU = []
    for x in range(n):
        a = V[x]
        for z in adj[x]: a ^= U[z]
        nU.append(a)
    return nU, list(U)
def rank(vs):
    vs = [v for v in vs if v]; r = 0
    while vs:
        p = max(vs); hb = p.bit_length() - 1
        vs = [v ^ p if (v >> hb) & 1 else v for v in vs if v != p]
        vs = [v for v in vs if v]; r += 1
    return r
def analyse(n, edges, clean_sites, unknown_vis, toy, T, read_sites=None, decl=None):
    """clean_sites: dict site->('FULL'|'U'|'V'); unknown_vis: visible but unknown sites.
    Returns per-t (support given read sites, toy prior support, own-content rank)."""
    adj = [[] for _ in range(n)]
    for a, b in edges: adj[a].append(b); adj[b].append(a)
    vis = sorted(set(clean_sites) | set(unknown_vis))
    read = vis if read_sites is None else read_sites
    # unknown coordinates
    unk = []
    for x in range(n):
        for c in (0, 1):
            d = clean_sites.get(x)
            if d == 'FULL' or (d == 'U' and c == 0) or (d == 'V' and c == 1): continue
            unk.append((x, c))
    res = []
    states = []
    for bits in product((0, 1), repeat=len(unk)):
        u = [0] * n; v = [0] * n
        for (x, c), b in zip(unk, bits):
            (u if c == 0 else v)[x] = b
        states.append((u, v))
    U = [1 << x for x in range(n)]; V = [1 << (n + x) for x in range(n)]
    own_mask = (1 << toy) | (1 << (n + toy))
    for t in range(1, T + 1):
        states = [step(n, adj, u, v) for u, v in states]
        U, V = sym_step(n, adj, U, V)
        groups = {}
        toys = set()
        for u, v in states:
            key = tuple((u[x], v[x]) for x in read)
            groups.setdefault(key, set()).add((u[toy], v[toy]))
            toys.add((u[toy], v[toy]))
        sup = max(len(s) for s in groups.values())
        own = rank([U[toy] & own_mask, V[toy] & own_mask])
        res.append((t, sup, len(toys), own))
    return res
def show(name, r):
    print(name)
    print("  t      :", " ".join(f"{t:2d}" for t, *_ in r))
    print("  support:", " ".join(f"{s:2d}" for _, s, _, _ in r))
    print("  prior  :", " ".join(f"{p:2d}" for _, _, p, _ in r))
    print("  own rk :", " ".join(f"{o:2d}" for *_, o in r))
WE2 = [(0, 1), (0, 3), (0, 4), (1, 2)]
show("W-E2 n=5 R={1,2} FULL toy 0, all visible", analyse(5, WE2, {1: 'FULL', 2: 'FULL'}, [], 0, 16))
show("W-E2 pointer site 1 only", analyse(5, WE2, {1: 'FULL', 2: 'FULL'}, [], 0, 16, read_sites=[1]))
show("W-E2 memory site 2 only", analyse(5, WE2, {1: 'FULL', 2: 'FULL'}, [], 0, 16, read_sites=[2]))
show("rank-2 example n=5 R={0,3,4} FULL toy 1", analyse(5, WE2, {0: 'FULL', 3: 'FULL', 4: 'FULL'}, [], 1, 16))
show("mixed n=3 star centre 0 (path 1-0-2), R={0 FULL,1 NONE}, toy 2", analyse(3, [(0, 1), (0, 2)], {0: 'FULL'}, [1], 2, 8))
show("mixed n=3 path 0-1-2, R={0 FULL,1 NONE}, toy 2", analyse(3, [(0, 1), (1, 2)], {0: 'FULL'}, [1], 2, 8))
show("mixed n=3 path 0-1-2 R={0 NONE,1 FULL}, toy 2", analyse(3, [(0, 1), (1, 2)], {1: 'FULL'}, [0], 2, 8))
show("U,U n=3 star centre 0, R={0 U,1 U}, toy 2", analyse(3, [(0, 1), (0, 2)], {0: 'U', 1: 'U'}, [], 2, 8))
show("E1-K2 path 0-1 R={0}", analyse(2, [(0, 1)], {0: 'FULL'}, [], 1, 6))
show("n=4 path 3-0-1-2 R={2,3} toy 0", analyse(4, [(3, 0), (0, 1), (1, 2)], {2: 'FULL', 3: 'FULL'}, [], 0, 8))

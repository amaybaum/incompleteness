"""Mixed declaration at n = 3: one FULL site, one NONE site (visible, uniform at t = 0), toy the
remaining site. Explicit-state forward simulation of u'_x = sum_{z~x} u_z + v_x, v'_x = u_x over F2
on every labelled simple graph on 3 sites and every placement of (toy, FULL, NONE), t = 1..24, a
multiple of every period of the update here (checked). Support: toy states consistent with the
visible cells, the same in every branch (checked); prior: toy states reachable at t. Learning:
support 1, prior 4.
The count uses l1_attack.py [5]'s convention, R = (a, b) with a < b and a FULL. Imports nothing."""
from itertools import product
PAIRS = [(0, 1), (0, 2), (1, 2)]
def run(edges, toy, full, none, T=24):
    adj = {x: [] for x in range(3)}
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    states = []
    for bits in product((0, 1), repeat=4):
        u = [0] * 3; v = [0] * 3
        u[toy], v[toy], u[none], v[none] = bits
        states.append((u, v))
    init = [(list(u), list(v)) for u, v in states]
    out = []
    for t in range(1, T + 1):
        states = [([(sum(u[z] for z in adj[x]) + v[x]) % 2 for x in range(3)], list(u)) for u, v in states]
        br = {}; prior = set()
        for u, v in states:
            br.setdefault(tuple((u[x], v[x]) for x in sorted((full, none))), set()).add((u[toy], v[toy]))
            prior.add((u[toy], v[toy]))
        sizes = {len(s) for s in br.values()}
        assert len(sizes) == 1
        out.append((t, sizes.pop(), len(prior)))
    assert [(list(u), list(v)) for u, v in states] == init, "T is not a multiple of the period"
    return out
def line(r):
    return ("support " + " ".join(str(s) for _, s, _ in r) + " | prior " + " ".join(str(p) for *_, p in r)
            + " | learning t = " + str([t for t, s, p in r if s == 1 and p == 4]))
print("[a] every placement on the two labelled paths 0-1-2 (centre 1) and 1-0-2 (centre 0), t = 1..24")
for edges in ([(0, 1), (1, 2)], [(0, 1), (0, 2)]):
    for toy in range(3):
        for full in range(3):
            if full != toy:
                print(f"  edges {edges} toy {toy} FULL {full} NONE {3 - toy - full}: " + line(run(edges, toy, full, 3 - toy - full)))
print("[b] recount of l1_attack [5] n = 3 'a FULL, b NONE' over all 8 labelled graphs")
tot = learn = 0
for mask in range(8):
    edges = [PAIRS[i] for i in range(3) if mask >> i & 1]
    for a, b in PAIRS:
        toy = 3 - a - b; tot += 1
        r = run(edges, toy, a, b)
        if any(s == 1 and p == 4 for _, s, p in r):
            learn += 1
            print(f"  learns: edges {edges} FULL {a} NONE {b} toy {toy}: " + line(r))
print(f"cases {tot}, learning {learn}")

"""Independent forward-state checks of W-E2, the n = 3 witness, the mixed-declaration witness and
W-E3.  No rank formula: explicit enumeration of initial states, step-by-step simulation from the
defining equations (indep.step_state), grouping by the conditioned visible cells."""
from itertools import product
from indep import adj_from_edges, step_state


def run(n, words, clean, cond_sites_list, toy, T):
    """words: list of edge lists per step (len >= T) or a single edge list for a fixed graph.
    clean: coordinates fixed to 0.  cond_sites_list: dict label -> sites whose both cells are
    conditioned on.  Returns per t: prior support of the toy, and per label the set of posterior
    supports over branches; also K-EXTHIST over the first label."""
    unk = [c for c in range(2 * n) if c not in clean]
    states = []
    for vals in product((0, 1), repeat=len(unk)):
        s = 0
        for v, c in zip(vals, unk):
            s |= v << c
        states.append(s)
    out = []
    cur = list(states)
    hist = [() for _ in states]
    labels = list(cond_sites_list)
    for t in range(1, T + 1):
        ed = words[t - 1] if isinstance(words[0], list) else words
        L = adj_from_edges(n, ed)
        cur = [step_state(n, L, s) for s in cur]
        toyv = [((s >> toy) & 1, (s >> (n + toy)) & 1) for s in cur]
        prior = len(set(toyv))
        row = {"t": t, "prior": prior}
        for lab in labels:
            sites = cond_sites_list[lab]
            g = {}
            for s, tv in zip(cur, toyv):
                key = tuple(((s >> x) & 1, (s >> (n + x)) & 1) for x in sites)
                g.setdefault(key, set()).add(tv)
            row[lab] = sorted({len(v) for v in g.values()})
        sites = cond_sites_list[labels[0]]
        hist = [h + tuple(((s >> x) & 1, (s >> (n + x)) & 1) for x in sites) for h, s in zip(hist, cur)]
        g = {}
        for h, tv in zip(hist, toyv):
            g.setdefault(h, set()).add(tv)
        row["hist"] = sorted({len(v) for v in g.values()})
        out.append(row)
    return out, cur, states


def show(title, rows, labels):
    print(title)
    print("   t      : " + " ".join(f"{r['t']:>3}" for r in rows))
    print("   prior  : " + " ".join(f"{r['prior']:>3}" for r in rows))
    for lab in labels:
        print(f"   {lab:7s}: " + " ".join(f"{'/'.join(map(str, r[lab])):>3}" for r in rows))
    print("   hist   : " + " ".join(f"{'/'.join(map(str, r['hist'])):>3}" for r in rows))


# W-E2
n = 5
E = [(0, 1), (0, 3), (0, 4), (1, 2)]
clean = [1, 2, n + 1, n + 2]
rows, cur, init = run(n, E, clean, {"all-vis": [1, 2], "pointer": [1], "memory": [2]}, 0, 16)
show("W-E2  n=5 edges (0,1),(0,3),(0,4),(1,2)  R={1,2} FULL  toy 0", rows, ["all-vis", "pointer", "memory"])
# period by states
L = adj_from_edges(n, E)
allst = range(1 << (2 * n))
p = 1
while True:
    ok = True
    for s in allst:
        x = s
        for _ in range(p):
            x = step_state(n, L, x)
        if x != s:
            ok = False
            break
    if ok:
        break
    p += 1
print("   period by full state simulation:", p)
# at t = 4: is the toy a function of the bath bright mode only?  is its initial state recovered?
cur4 = list(init)
for _ in range(4):
    cur4 = [step_state(n, L, s) for s in cur4]
f = {}
fi = {}
for s0, s in zip(init, cur4):
    bright = (((s0 >> 3) ^ (s0 >> 4)) & 1, ((s0 >> (n + 3)) ^ (s0 >> (n + 4))) & 1)
    toy = ((s >> 0) & 1, (s >> n) & 1)
    f.setdefault(bright, set()).add(toy)
    vis = tuple((s >> c) & 1 for c in (1, 2, n + 1, n + 2))
    fi.setdefault(vis, set()).add(((s0 >> 0) & 1, (s0 >> n) & 1))
print("   t=4: toy is a function of the bath bright mode (u3+u4, v3+v4):", all(len(v) == 1 for v in f.values()),
      "| toy's initial state determined by visible cells:", all(len(v) == 1 for v in fi.values()))

# n = 3 smallest witness and the mixed-declaration witness
n = 3
E = [(0, 1), (0, 2)]
rows, cur, init = run(n, E, [1, 2, n + 1, n + 2], {"all-vis": [1, 2], "site1": [1]}, 0, 7)
show("n=3 path 1-0-2, R={1,2} FULL, toy 0", rows, ["all-vis", "site1"])
rows, cur, init = run(n, E, [0, n + 0], {"all-vis": [0, 1]}, 2, 7)
show("n=3 star centre 0, R={0 FULL, 1 NONE (visible, uniform)}, toy 2   [one clean pair, two visible sites]", rows, ["all-vis"])
# n = 2 (the only |R|=1 FULL case): never learns
rows, cur, init = run(2, [(0, 1)], [0, 2], {"all-vis": [0]}, 1, 6)
show("n=2 E1-K2 R={0} FULL toy 1", rows, ["all-vis"])

# W-E3
n = 6
word = []
for i, sw in enumerate(("EEEO", "EEE", "EEE")):
    word.append([(0, 1), (0, 5)])
    for lab in sw:
        word.append([(1, 2 + i)] if lab == "E" else [])
clean = [1, 2, 3, 4, n + 1, n + 2, n + 3, n + 4]
rows, cur, init = run(n, word, clean, {"all-vis": [1, 2, 3, 4], "memory": [2, 3, 4]}, 0, 13)
show("W-E3 one reused bath (5), pointer 1, memories 2,3,4, toy 0", rows, ["all-vis", "memory"])
# non-copying and all-idle backgrounds
w2 = []
for i, sw in enumerate(("EEEO", "EEE", "EEE")):
    w2.append([(0, 1), (0, 5)])
    w2 += [[] for _ in sw]
rows, _, _ = run(n, w2, clean, {"all-vis": [1, 2, 3, 4]}, 0, 13)
show("W-E3 non-copying (stores idle)", rows, ["all-vis"])
# fresh bath per read with the same stores
n = 8
word = []
for i, sw in enumerate(("EEEO", "EEE", "EEE")):
    word.append([(0, 1), (0, 5 + i)])
    for lab in sw:
        word.append([(1, 2 + i)] if lab == "E" else [])
clean = [1, 2, 3, 4, n + 1, n + 2, n + 3, n + 4]
rows, _, _ = run(n, word, clean, {"all-vis": [1, 2, 3, 4]}, 0, 13)
show("W-E3 same word, fresh bath per read (5,6,7)", rows, ["all-vis"])

"""C-i widened: the record lifecycle of construction C1 on the lattice (exact; Fractions-free
because every law here is uniform on an affine set -- support sizes are counted by enumeration).

Graphs: memory site w (visible) - pointer site 1 (visible) - toy 0 (hidden) - bath 2 (hidden)
        - reservoir 3 - ... - reservoir L+1 (hidden chain), R = {w, 1}.
        (w = site index L+2; w is optional and only used in stage (c).)
Stages:
 (a) preparation: visible pointer site and memory site clean at (0,0); every hidden coordinate
     under the counting measure (toy uniform as the worst case for the observer).
 (b) coupling: one update step (C1).
 (c) storing: (c1) free retention -- the visible configuration is read (kappa4, no ontic change);
     (c2) a persistent physical record -- the observer's visible operation copies the reading into
     the memory site (X += Q, a CNOT on visible cells, completed to a symplectic map on the visible
     pair: Qb += Xb).  Check: its matrix is the identity on every hidden coordinate, so it has NO
     hidden back-action, for every input.
 (d) reuse / discard: the pointer site can be reset by feedback; the bath and reservoir cannot be
     removed from the toy's neighbourhood (the graph is fixed); every further step is a further read.
     Measured: the support of the TOY's current state given every visible record, step by step.
 (e) later access: whether later steps re-read the bath's hidden record of the first read
     (P at v2, q + Pb at u2) -- measured as the rank of the learnable space of the initial hidden
     variables, step by step.
"""
from itertools import product
from f2 import lattice_update, apply, compose, is_symplectic, identity


def chain(L, with_memory=False):
    """sites: 0 toy, 1 pointer, 2 bath, 3..L+1 reservoir, [L+2 memory]."""
    n = L + 2 + (1 if with_memory else 0)
    edges = [(1, 0), (0, 2)] + [(k, k + 1) for k in range(2, L + 1)]
    if with_memory:
        edges.append((n - 1, 1))
    vis_sites = [1] + ([n - 1] if with_memory else [])
    return n, tuple(edges), vis_sites


def run(L, T, reset=True):
    n, edges, vis_sites = chain(L)
    M = lattice_update(n, edges)
    vmask = sum((1 << x) | (1 << (n + x)) for x in vis_sites)
    hid = [c for c in range(2 * n) if not (vmask >> c) & 1]
    rows = []
    branches = [dict() for _ in range(T)]
    for vals in product((0, 1), repeat=len(hid)):
        s = sum(v << c for v, c in zip(vals, hid))
        recs = []
        for t in range(T):
            s = apply(M, s)
            recs.append(s & vmask)
            if reset:
                s &= ~vmask
            toy = ((s >> 0) & 1, (s >> n) & 1)
            branches[t].setdefault(tuple(recs), set()).add(toy)
    out = []
    for t in range(T):
        sizes = [len(v) for v in branches[t].values()]
        out.append((t + 1, min(sizes), max(sizes), len(branches[t])))
    return out, len(hid)


print("(c2) storing by a visible copy: hidden back-action of the storage operation")
n, edges, vis_sites = chain(1, with_memory=True)       # sites 0 toy,1 ptr,2 bath,3 memory
w = n - 1
G = list(identity(2 * n))
G[w] = (1 << w) | (1 << 1)                  # X(u_w) += Q(u_1)
G[n + 1] = (1 << (n + 1)) | (1 << (n + w))  # Qb(v_1) += Xb(v_w)  (symplectic completion)
G = tuple(G)
hid = [c for c in range(2 * n) if c not in (1, w, n + 1, n + w)]
print("  storage map symplectic:", is_symplectic(G, n))
print("  storage map is the identity on every hidden coordinate (rows and columns):",
      all(G[c] == 1 << c for c in hid) and all(((G[r] >> c) & 1) == (r == c) for r in range(2 * n) for c in hid))
M = lattice_update(n, edges)
ok = True
for vals in product((0, 1), repeat=4):
    s = (vals[0] << 0) | (vals[1] << n) | (vals[2] << 2) | (vals[3] << (n + 2))
    s1 = apply(M, s)
    s2 = apply(G, s1)
    ok &= all(((s1 >> c) & 1) == ((s2 >> c) & 1) for c in hid)
    ok &= ((s2 >> w) & 1) == ((s1 >> 1) & 1)            # memory holds the reading
print("  after the read step, storing leaves every hidden coordinate unchanged and puts the reading in the memory:", ok)

print("(d)/(e) reuse on the fixed graph: support of the TOY's current state given every visible record")
for L in range(1, 6):
    for reset in (True,):
        res, nh = run(L, T=2 * (L + 1) + 3, reset=reset)
        seq = " ".join(f"{mn}" if mn == mx else f"{mn}-{mx}" for (t, mn, mx, nb) in res)
        first = next((t for (t, mn, mx, nb) in res if mx == 1), None)
        print(f"  bath + reservoir of {L} hidden site(s) ({nh} hidden bits incl. toy): toy support after steps 1..{len(res)}: {seq}"
              f"   -> every branch a point mass from step {first}")
res, nh = run(1, 8, reset=False)
print("  (L = 1, no feedback reset of the pointer:", " ".join(str(mn) for (t, mn, mx, nb) in res), ")")

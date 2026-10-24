"""E1/E2 pressure tests on structured graphs (exact, F2): larger memory, longer horizons (one full
period, hence every t), hidden reservoirs, lattice-like graphs, background subtraction and
disturbance accounting, and the K-EXTHIST replay of C-i's lifecycle.

Memory = the visible configuration at time t only, unless a line says K-EXTHIST.  Clean
declaration FULL (both coordinates of every visible site clean at 0) unless stated.
"""
from itertools import combinations
from collections import Counter
from emb_core import lattice_update, vis_coords, clean_coords, mask_of, post_rank, prior_rank, order
from f2 import compose, identity, rank


def powers_of(M, om):
    pw = [identity(len(M))]
    for _ in range(1, om):
        pw.append(compose(M, pw[-1]))
    return pw


def profile(n, edges, R, toy, decl="FULL", hist=True):
    M = lattice_update(n, edges)
    om = order(M)
    pw = powers_of(M, om)
    vc = vis_coords(n, R)
    um = ((1 << (2 * n)) - 1) & ~mask_of(clean_coords(n, R, decl))
    T0 = [1 << toy, 1 << (n + toy)]
    H = [identity(2 * n)[c] for c in vc]
    rows = []
    for t in range(1, om):
        P = pw[t]
        F = [P[c] for c in vc]
        T = [P[toy], P[n + toy]]
        pf, pr = post_rank(F, T, um), prior_rank(T, um)
        pinit = post_rank(F, T0, um)
        if hist:
            H = H + F
            ph = post_rank(H, T, um)
        else:
            ph = None
        rows.append((t, 2 ** pf, pr, 2 ** pinit, None if ph is None else 2 ** ph))
    return om, rows, pw


def summarize(om, rows):
    learn = [t for (t, s, pr, si, sh) in rows if s == 1 and pr == 2]
    anyrec = [t for (t, s, pr, si, sh) in rows if s == 1]
    hist1 = next((t for (t, s, pr, si, sh) in rows if sh == 1), None)
    persist = [t for (t, s, pr, si, sh) in rows if si == 1 and s >= 2]
    return learn, anyrec, hist1, persist


def classify_disturbance(D, F, um):
    if all(d == 0 for d in D):
        return "none"
    if all(d & um == 0 for d in D):
        return "known"
    Fu = [f & um for f in F]
    if rank(Fu + [d & um for d in D]) == rank(Fu):
        return "in memory"
    return "not in memory"


def chainA(m, L):
    """toy 0, pointer 1, bath 2, reservoir 3..L+1, memory chain L+2..L+1+m behind the pointer."""
    n = L + 2 + m
    edges = [(0, 1), (0, 2)] + [(k, k + 1) for k in range(2, L + 1)]
    prev = 1
    for j in range(m):
        x = L + 2 + j
        edges.append((prev, x))
        prev = x
    R = tuple([1] + [L + 2 + j for j in range(m)])
    return n, tuple(edges), R


def lifecycle_replay(L, T, reset):
    """C-i lifecycle.py replay in this engine: K-EXTHIST (every visible configuration retained),
    optional feedback reset of the pointer to 0 after each step (an external operation)."""
    n, edges, R = chainA(0, L)
    M = lattice_update(n, edges)
    vc = vis_coords(n, R)
    um = ((1 << (2 * n)) - 1) & ~mask_of(vc)
    P = identity(2 * n)
    H = []
    out = []
    for t in range(1, T + 1):
        P = compose(M, P)
        H += [P[c] for c in vc]
        out.append(2 ** post_rank(H, [P[0], P[n]], um))
        if reset:
            P = tuple(0 if i in vc else P[i] for i in range(2 * n))
    return out


print("K-EXTHIST control: replay of C-i lifecycle.out (path pointer-toy-bath-reservoir, R = {pointer})")
exp_first = {L: 2 * (L + 1) for L in range(1, 6)}
ok = True
for L in range(1, 6):
    s = lifecycle_replay(L, 2 * (L + 1) + 3, reset=True)
    first = s.index(1) + 1
    ok &= first == exp_first[L] and all(x == 2 for x in s[:first - 1])
    print(f"  L={L} with feedback reset: toy support {' '.join(map(str, s))}  first point mass at {first} (C-i: {exp_first[L]})")
s = lifecycle_replay(1, 8, reset=False)
ok &= s == [2, 2, 2, 1, 1, 1, 1, 1]
print(f"  L=1 no reset: {' '.join(map(str, s))} (C-i: 2 2 2 1 1 1 1 1)")
print("  K-EXTHIST REPLAY:", "PASS" if ok else "FAIL")

print("\nSame graphs, embedded memory only (no external history, no reset): the pointer site is the whole memory")
for L in range(1, 7):
    n, edges, R = chainA(0, L)
    om, rows, _ = profile(n, edges, R, 0)
    learn, anyrec, hist1, persist = summarize(om, rows)
    print(f"  L={L}: period {om}; min toy support over the period {min(r[1] for r in rows)}; learning t: {learn or 'none'};"
          f" K-EXTHIST (no reset) first point mass t={hist1}")

print("\nFamily A (single apparatus): memory chain of m sites behind the pointer, toy, bath, reservoir of L-1 sites")
for m in range(0, 5):
    for L in range(1, 7):
        n, edges, R = chainA(m, L)
        if n > 13:
            continue
        om, rows, pw = profile(n, edges, R, 0)
        learn, anyrec, hist1, persist = summarize(om, rows)
        mins = min(r[1] for r in rows)
        print(f"  m={m} L={L} n={n} period {om}: min support {mins}; learning at {len(learn)} of {om - 1} times"
              f"{' first t=' + str(learn[0]) if learn else ''}; K-EXTHIST first t={hist1};"
              f" times with initial toy fully recorded but current toy support >= 2: {len(persist)}"
              f"{' (first ' + str(persist[0]) + ')' if persist else ''}")

print("\nFamily B (single apparatus, toy with k hidden bath neighbours, memory chain m)")
for k in range(1, 5):
    for m in range(0, 4):
        n = 2 + k + m
        edges = [(0, 1)] + [(0, 2 + j) for j in range(k)]
        prev = 1
        for j in range(m):
            x = 2 + k + j
            edges.append((prev, x))
            prev = x
        R = tuple([1] + [2 + k + j for j in range(m)])
        om, rows, _ = profile(n, tuple(edges), R, 0)
        learn, anyrec, hist1, persist = summarize(om, rows)
        print(f"  k={k} m={m} n={n} period {om}: min support {min(r[1] for r in rows)}; learning times {len(learn)}"
              f"{' first t=' + str(learn[0]) if learn else ''}; K-EXTHIST first t={hist1}")

print("\nWitness W-E2 (from e12_exhaustive): edges (0,1),(0,3),(0,4),(1,2); R = {1, 2}; toy 0; baths 3, 4")
n, edges, R = 5, ((0, 1), (0, 3), (0, 4), (1, 2)), (1, 2)
om, rows, pw = profile(n, edges, R, 0)
print(f"  period {om}")
for (t, s, pr, si, sh) in rows:
    print(f"   t={t}: toy support given final memory {s} (prior {2 ** pr}); initial toy support {si}; K-EXTHIST {sh}")
vc = vis_coords(n, R)
um = ((1 << (2 * n)) - 1) & ~mask_of(vc)
names = ["u0", "u1", "u2", "u3", "u4", "v0", "v1", "v2", "v3", "v4"]


def fmt(r):
    return " + ".join(names[j] for j in range(2 * n) if (r >> j) & 1) or "0"


P = pw[4]
print("  at t=4: memory cells  u1=" + fmt(P[1]) + ";  v1=" + fmt(P[n + 1]) + ";  u2=" + fmt(P[2]) + ";  v2=" + fmt(P[n + 2]))
print("          toy cells     u0=" + fmt(P[0]) + ";  v0=" + fmt(P[n]))
# background subtraction: B0 (no observer: R-H edges cut) and non-copying (memory detached)
for label, ed in (("B0 (all R-H edges cut)", ((1, 2), (0, 3), (0, 4))),
                  ("non-copying (edge pointer-memory removed)", ((0, 1), (0, 3), (0, 4)))):
    M0 = lattice_update(n, ed)
    P0 = identity(2 * n)
    for _ in range(4):
        P0 = compose(M0, P0)
    D = [P[0] ^ P0[0], P[n] ^ P0[n]]
    print(f"  background {label}: toy at t=4 u0={fmt(P0[0])}; v0={fmt(P0[n])};"
          f" difference D = ({fmt(D[0])}, {fmt(D[1])}): {classify_disturbance(D, [P[c] for c in vc], um)}")
    om0, rows0, _ = profile(n, ed, R, 0)
    l0 = [t for (t, s, pr, si, sh) in rows0 if s == 1 and pr == 2]
    print(f"     that background as a protocol: learning times {l0 or 'none'}; min support {min(r[1] for r in rows0)}")


def grid(a, b):
    idx = lambda i, j: i * b + j
    e = []
    for i in range(a):
        for j in range(b):
            if i + 1 < a:
                e.append((idx(i, j), idx(i + 1, j)))
            if j + 1 < b:
                e.append((idx(i, j), idx(i, j + 1)))
    return a * b, tuple(e)


def cube():
    e = []
    for x in range(8):
        for d in (1, 2, 4):
            if not x & d:
                e.append((x, x | d))
    return 8, tuple(e)


print("\nLattice-like graphs: every region R, every toy site, one full period (decl FULL)")
for label, (n, edges) in (("path P7", (7, tuple((i, i + 1) for i in range(6)))),
                          ("cycle C6", (6, tuple((i, (i + 1) % 6) for i in range(6)))),
                          ("cycle C8", (8, tuple((i, (i + 1) % 8) for i in range(8)))),
                          ("grid 2x3", grid(2, 3)), ("grid 2x4", grid(2, 4)), ("grid 3x3", grid(3, 3)),
                          ("cube 2x2x2", cube())):
    M = lattice_update(n, edges)
    om = order(M)
    pw = powers_of(M, om)
    c = Counter()
    for r in range(1, n):
        for R in combinations(range(n), r):
            vc = vis_coords(n, R)
            um = ((1 << (2 * n)) - 1) & ~mask_of(vc)
            for toy in range(n):
                if toy in R:
                    continue
                learn = False
                for t in range(1, om):
                    P = pw[t]
                    F = [P[x] for x in vc]
                    T = [P[toy], P[n + toy]]
                    if prior_rank(T, um) == 2 and post_rank(F, T, um) == 0:
                        learn = True
                        break
                c[(min(r, 3), "cases")] += 1
                c[(min(r, 3), "learn")] += learn
    print(f"  {label}: period {om}; " + "; ".join(
        f"|R|{'=' if k < 3 else '>='}{k}: learning in {c[(k, 'learn')]} of {c[(k, 'cases')]} (R, toy) cases"
        for k in (1, 2, 3) if c[(k, 'cases')]))

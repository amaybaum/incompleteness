"""C-i exhaustive search: can a composition of whole-lattice update steps (Main.md l.290),
interleaved with observer operations on the visible coordinates, realize the target pointer
coupling on designated coordinates?

Target (one toy bit h = (q, p), pointer (Q visible, P hidden), nonzero u = (uq, up) in Z_2^2,
omega(u, h) = uq*p + up*q):
    Q' = Q + omega(u, h),   q' = q + uq*P,   p' = p + up*P,   P' = P.

Word searched:  T = G_k M G_{k-1} M ... G_1 M G_0,  1 <= k <= KMAX, every G_i an observer
operation on the visible coordinates (identity on hidden ones), from one of the classes
    none : G_i = identity (pure waiting),
    cell : permutations of the visible coordinates (cell permutations),
    GL   : every invertible linear map of the visible coordinates (visible dimension <= 4).
Only the four designated output rows are tracked (backwards, as functionals); observer-
operation orbits are canonicalized exactly (GL: column space of the visible block;
cell: sorted column multiset), so each level is complete, not sampled.

Acceptance of a word on a designated assignment, per (toy orientation, u):
    E  : the four designated output rows equal the target rows exactly;
    AV : they equal the target up to terms in non-designated VISIBLE input coordinates
         (realization needs declared clean visible ancillas at 0);
    AH : up to terms that include non-designated HIDDEN input coordinates
         (needs a hidden coordinate supplied in a known state: K-CLN failure mode).
A row touching a designated coordinate other than the target's is a failure.

Partitions:
    strict  : Main.md l.292 -- the visible sector is the set of sites of a region R; both
              coordinates of a site share its visibility.  Q is a coordinate of a visible
              site, P a coordinate of a different, hidden site.
    relaxed : coordinate-level partition (NOT the corpus's region partition): the pointer
              is one site with one visible and one hidden coordinate; other sites may be
              V, H, or split either way.
"""
import sys, time, json
from itertools import combinations, product, permutations
from f2 import (rowmul, lattice_update, gl_elements, perm_elements, popc)

KMAX = 4
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
GL_DMAX = 4

GL_CACHE = {d: gl_elements(d) for d in range(0, GL_DMAX + 1)}
PERM_CACHE = {d: perm_elements(d) for d in range(0, 6)}


def all_graphs(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        yield tuple(p for k, p in enumerate(pairs) if (mask >> k) & 1)


class Config:
    def __init__(self, n, edges, vis_coords, Qc, Pc):
        self.n = n
        self.N = 2 * n
        self.edges = edges
        self.M = lattice_update(n, edges)
        self.vis = sorted(vis_coords)
        self.dv = len(self.vis)
        self.vmask = sum(1 << c for c in self.vis)
        self.hmask = ((1 << self.N) - 1) ^ self.vmask
        self.Qc, self.Pc = Qc, Pc
        self.qa, self.pa = 0, n          # toy site 0: u_0, v_0
        # tracked output rows, in order: Q', u0', v0', P'
        self.out = [Qc, 0, n, Pc]
        self.desig = (1 << Qc) | (1 << 0) | (1 << n) | (1 << Pc)
        self.Qpos = self.vis.index(Qc)

    # split 4 rows into hidden parts and visible column matrix
    def vcols(self, rows):
        cols = []
        for c in self.vis:
            col = 0
            for i, r in enumerate(rows):
                if (r >> c) & 1:
                    col |= 1 << i
            cols.append(col)
        return cols

    def hparts(self, rows):
        return tuple(r & self.hmask for r in rows)

    def from_parts(self, H, cols):
        rows = list(H)
        for j, c in enumerate(self.vis):
            col = cols[j]
            for i in range(4):
                if (col >> i) & 1:
                    rows[i] |= 1 << c
        return tuple(rows)


def span_of(vecs):
    s = {0}
    for v in vecs:
        if v not in s:
            s |= {x ^ v for x in s}
    return frozenset(s)


def targets(cfg):
    """Yield (label, target rows in order Q',u0',v0',P')."""
    n = cfg.n
    for orient in (0, 1):
        q, p = (0, n) if orient == 0 else (n, 0)
        for (uq, up) in ((1, 0), (0, 1), (1, 1)):
            tQ = (1 << cfg.Qc) | (up << q) | (uq << p)
            tq = (1 << q) | (uq << cfg.Pc)
            tp = (1 << p) | (up << cfg.Pc)
            tP = 1 << cfg.Pc
            # rows indexed by output coordinate: Q', u0', v0', P'
            t = {cfg.Qc: tQ, q: tq, p: tp, cfg.Pc: tP}
            yield (f"(q,p)=({'u0,v0' if orient==0 else 'v0,u0'}) u={(uq,up)}",
                   (t[cfg.Qc], t[0], t[n], t[cfg.Pc]))


def classify(cfg, rows, tgt):
    anc = 0
    for r, t in zip(rows, tgt):
        d = r ^ t
        if d & cfg.desig:
            return None
        anc |= d
    if anc == 0:
        return ("E", 0)
    if anc & cfg.hmask:
        return ("AH", anc)
    return ("AV", anc)


RANK = {"E": 0, "AV": 1, "AH": 2}


def best_of(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return a if RANK[a[0]] <= RANK[b[0]] else b


def search_config(cfg, opclass, kmax=KMAX):
    """Return dict k -> best classification found at exactly k update steps (or None)."""
    M = cfg.M
    start = tuple(1 << o for o in cfg.out)
    res = {}
    if opclass == "none":
        level = {start}
        for k in range(1, kmax + 1):
            level = {tuple(rowmul(r, M) for r in e) for e in level}
            best = None
            for e in level:
                for lab, tgt in targets(cfg):
                    c = classify(cfg, e, tgt)
                    if c:
                        best = best_of(best, (c[0], c[1], lab))
            res[k] = best
        return res

    if opclass == "cell":
        perms = list(permutations(range(cfg.dv)))
        def canon(rows):
            cols = cfg.vcols(rows)
            return (cfg.hparts(rows), tuple(sorted(cols)))
        def orbit(key):
            H, cols = key
            seen = set()
            for p in set(permutations(cols)):
                yield cfg.from_parts(H, list(p))
        level = {canon(start)}
        for k in range(1, kmax + 1):
            nxt = set()
            for key in level:
                for e in orbit(key):
                    nxt.add(canon(tuple(rowmul(r, M) for r in e)))
            level = nxt
            best = None
            for key in level:
                for e in orbit(key):
                    for lab, tgt in targets(cfg):
                        c = classify(cfg, e, tgt)
                        if c:
                            best = best_of(best, (c[0], c[1], lab))
            res[k] = best
            res[f"size{k}"] = len(level)
        return res

    if opclass == "GL":
        def canon(rows):
            return (cfg.hparts(rows), span_of(cfg.vcols(rows)))
        orbit_cache = {}
        def orbit_cols(C):
            if C in orbit_cache:
                return orbit_cache[C]
            Cl = sorted(C)
            out = [cols for cols in product(Cl, repeat=cfg.dv) if span_of(cols) == C]
            orbit_cache[C] = out
            return out
        level = {canon(start)}
        for k in range(1, kmax + 1):
            nxt = set()
            for key in level:
                H, C = key
                for cols in orbit_cols(C):
                    e = cfg.from_parts(H, cols)
                    nxt.add(canon(tuple(rowmul(r, M) for r in e)))
            level = nxt
            best = None
            e_Q = 1  # column vector (1,0,0,0): Q' row only
            for (H, C) in level:
                if e_Q not in C:
                    continue
                vis_exact = (C == frozenset({0, 1}))
                for lab, tgt in targets(cfg):
                    anc = 0
                    ok = True
                    for h, t in zip(H, tgt):
                        d = h ^ (t & cfg.hmask)
                        if d & cfg.desig:
                            ok = False
                            break
                        anc |= d
                    if not ok:
                        continue
                    if anc:
                        c = ("AH", anc)
                    elif vis_exact:
                        c = ("E", 0)
                    else:
                        c = ("AV", -1)   # visible ancilla columns: dim C - 1 of them
                    best = best_of(best, (c[0], c[1], lab))
            res[k] = best
            res[f"size{k}"] = len(level)
        return res
    raise ValueError(opclass)


def configs(n, mode):
    """Yield (label, vis_coords, Qc, Pc) for site-class assignments."""
    if mode == "relaxed":
        if n < 2:
            return
        for porient in ("A", "B"):
            Qc, Pc = (1, n + 1) if porient == "A" else (n + 1, 1)
            for classes in product("VHab", repeat=n - 2):
                vis = [Qc]
                for x, cl in zip(range(2, n), classes):
                    if cl == "V":
                        vis += [x, n + x]
                    elif cl == "a":
                        vis += [x]        # u visible, v hidden
                    elif cl == "b":
                        vis += [n + x]    # u hidden, v visible
                yield (f"ptr{porient} others={''.join(classes)}", vis, Qc, Pc)
    else:
        if n < 3:
            return
        for Qc in (1, n + 1):
            for Pc in (2, n + 2):
                for classes in product("VH", repeat=n - 3):
                    vis = [1, n + 1]
                    for x, cl in zip(range(3, n), classes):
                        if cl == "V":
                            vis += [x, n + x]
                    yield (f"Q={'u1' if Qc==1 else 'v1'} P={'u2' if Pc==2 else 'v2'} others={''.join(classes)}",
                           vis, Qc, Pc)


def main():
    t0 = time.time()
    summary = []
    for mode in ("strict", "relaxed"):
        for n in range(2, NMAX + 1):
            for opclass in ("none", "cell", "GL"):
                tally = {}
                hits = []
                ncfg = 0
                for edges in all_graphs(n):
                    for (lab, vis, Qc, Pc) in configs(n, mode):
                        cfg = Config(n, edges, vis, Qc, Pc)
                        if opclass == "GL" and cfg.dv > GL_DMAX:
                            continue
                        if opclass == "cell" and cfg.dv > 5:
                            continue
                        ncfg += 1
                        r = search_config(cfg, opclass)
                        for k in range(1, KMAX + 1):
                            b = r[k]
                            key = (k, b[0] if b else "-")
                            tally[key] = tally.get(key, 0) + 1
                            if b and b[0] in ("E", "AV"):
                                hits.append((k, b[0], edges, lab, b[2]))
                line = f"[{mode}] n={n} ops={opclass}: configs={ncfg}"
                print(line)
                for k in range(1, KMAX + 1):
                    cnt = {c: tally.get((k, c), 0) for c in ("E", "AV", "AH", "-")}
                    print(f"    k={k}: E={cnt['E']} AV={cnt['AV']} AH={cnt['AH']} none={cnt['-']}")
                hits.sort(key=lambda h: (h[0], RANK[h[1]], len(h[2])))
                for h in hits[:6]:
                    print(f"    hit: k={h[0]} {h[1]} edges={h[2]} {h[3]} {h[4]}")
                if len(hits) > 6:
                    print(f"    ... {len(hits)} hits in total")
                sys.stdout.flush()
    print(f"elapsed {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()

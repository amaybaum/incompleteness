"""C-i exhaustive search, record-complete form.

Word: T = G_k M G_{k-1} M ... G_1 M G_0, 1 <= k <= 4, M = Main.md l.290 update on the whole
graph, each G_i an observer operation on the visible coordinates only.

Forward search over equivalence classes.  X_j = M G_{j-1} ... M G_0 is the state map after j
steps.  X and G X (G an observer operation) have identical futures, so a class is
    (hidden rows of X exactly, visible rows of X modulo the left action of the class),
together with L_j = span of the visible rows of X_0..X_j: every linear functional of the input
the observer can compute from the visible configurations read at times 0..j (a readout does
not change the ontic state, so every intermediate configuration is an accessible record).

Observer-operation classes:
    none : no visible operation (pure waiting);
    cell : permutations of the visible coordinates;
    GL   : all invertible linear maps of the visible coordinates (visible dimension <= 4).
(GL contains cell contains none.  Each level is complete: every word of the class is covered.)

At level k, for every target (two toy orientations x three nonzero u):
  designated status  E  : designated output rows equal the target exactly
                     AV : equal up to non-designated visible inputs (clean visible ancillas)
                     AH : need a non-designated hidden input in a known state (K-CLN mode)
  record status      ok   : the learnable functionals of (q, p, P) -- from L_k after
                            eliminating uniform hidden idle inputs and dropping visible
                            (known) inputs -- are exactly span{omega(u, .)}
                     leak : anything more (P, or toy content beyond omega(u, h), or a joint one).
Only E/AV with record ok counts as a realization of R_u by the coupling.
"""
import sys, time
from itertools import combinations, product, permutations
from f2 import rowmul, compose, lattice_update, gl_elements, identity, popc

KMAX = 4


def all_graphs(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        yield tuple(p for k, p in enumerate(pairs) if (mask >> k) & 1)


def basis_key(vecs):
    """Fully reduced echelon basis (canonical) of span(vecs), as a sorted tuple."""
    basis = []
    for v in vecs:
        for b in basis:
            if v & (1 << (b.bit_length() - 1)):
                v ^= b
        if v:
            hb = 1 << (v.bit_length() - 1)
            basis = [b ^ v if b & hb else b for b in basis]
            basis.append(v)
    return tuple(sorted(basis))


def span_list(basis):
    s = [0]
    for b in basis:
        s += [x ^ b for x in s]
    return s


def ordered_bases(basis):
    """All ordered bases of span(basis)."""
    d = len(basis)
    sp = span_list(basis)
    out = []
    def rec(cur, cspan):
        if len(cur) == d:
            out.append(tuple(cur))
            return
        for v in sp:
            if v in cspan:
                continue
            rec(cur + [v], cspan | {x ^ v for x in cspan})
    rec([], {0})
    return out


def eliminate(basis, Zmask):
    """Basis of {f in span(basis) : f & Zmask == 0}."""
    vecs = list(basis)
    z = Zmask
    while z:
        bit = z & -z
        z ^= bit
        piv = next((i for i, v in enumerate(vecs) if v & bit), None)
        if piv is None:
            continue
        pv = vecs.pop(piv)
        vecs = [v ^ pv if v & bit else v for v in vecs]
    return [v for v in vecs if v]


class Cfg:
    def __init__(self, n, edges, vis, Qc, Pc, label):
        self.n, self.N, self.edges, self.label = n, 2 * n, edges, label
        self.M = lattice_update(n, edges)
        self.vis = sorted(vis)
        self.hid = [c for c in range(self.N) if c not in self.vis]
        self.dv = len(self.vis)
        self.vmask = sum(1 << c for c in self.vis)
        self.hmask = ((1 << self.N) - 1) ^ self.vmask
        self.Qc, self.Pc = Qc, Pc
        self.desig = (1 << Qc) | 1 | (1 << n) | (1 << Pc)
        self.Zmask = self.hmask & ~self.desig          # hidden idle (uniform) inputs
        self.qpP = 1 | (1 << n) | (1 << Pc)

    def tgts(self):
        n = self.n
        for orient in (0, 1):
            q, p = (0, n) if orient == 0 else (n, 0)
            for (uq, up) in ((1, 0), (0, 1), (1, 1)):
                t = {self.Qc: (1 << self.Qc) | (up << q) | (uq << p),
                     q: (1 << q) | (uq << self.Pc),
                     p: (1 << p) | (up << self.Pc),
                     self.Pc: 1 << self.Pc}
                wu = (up << q) | (uq << p)
                yield (f"(q,p)=({'u0,v0' if orient == 0 else 'v0,u0'}),u={(uq, up)}", t, wu)


def vkey(cfg, cls, vrows):
    if cls == "GL":
        return basis_key(vrows)
    if cls == "cell":
        return tuple(sorted(vrows))
    return tuple(vrows)


def vchoices(cfg, cls, key):
    if cls == "GL":
        return ordered_bases(key)
    if cls == "cell":
        return list(set(permutations(key)))
    return [key]


def assemble(cfg, H, vrows):
    rows = [0] * cfg.N
    for c, r in zip(cfg.hid, H):
        rows[c] = r
    for c, r in zip(cfg.vis, vrows):
        rows[c] = r
    return tuple(rows)


RANKD = {"E": 0, "AV": 1, "AH": 2}


def final_check(cfg, cls, key, results):
    """Classify one class at the current level for every target; update `results`
    (label -> best (designated, record) pair).  Returns list of (label, d, rec)."""
    H, V, L = key
    Hd = dict(zip(cfg.hid, H))
    if cls == "GL":
        Qcands = [f for f in span_list(V) if f]
    elif cls == "cell":
        Qcands = list(set(V))
    else:
        Qcands = [V[cfg.vis.index(cfg.Qc)]]
    learn = eliminate(L, cfg.Zmask)
    lam = basis_key([f & cfg.qpP for f in learn])
    out = []
    for lab, t, wu in cfg.tgts():
        anc = 0
        ok = True
        for c in (0, cfg.n, cfg.Pc):
            d = Hd[c] ^ t[c]
            if d & cfg.desig:
                ok = False
                break
            anc |= d
        if not ok:
            continue
        best = None
        for f in Qcands:
            d = f ^ t[cfg.Qc]
            if d & cfg.desig:
                continue
            a = anc | d
            cl = "E" if a == 0 else ("AH" if a & cfg.hmask else "AV")
            if best is None or RANKD[cl] < RANKD[best]:
                best = cl
        if best is None:
            continue
        rec = "ok" if lam == basis_key([wu]) else "leak"
        out.append((lab, best, rec))
    return out


def run_cfg(cfg, cls, kmax=KMAX, keep_paths=False):
    X0 = identity(cfg.N)
    H0 = tuple(X0[c] for c in cfg.hid)
    V0 = [X0[c] for c in cfg.vis]
    L0 = basis_key(V0)
    k0 = (H0, vkey(cfg, cls, V0), L0)
    level = {k0}
    parent = {k0: None} if keep_paths else None
    per_k = {}
    for k in range(1, kmax + 1):
        nxt = set()
        for key in level:
            H, Vk, L = key
            for vr in vchoices(cfg, cls, Vk):
                Y = assemble(cfg, H, vr)
                X = compose(cfg.M, Y)
                Hn = tuple(X[c] for c in cfg.hid)
                Vn = [X[c] for c in cfg.vis]
                Ln = basis_key(list(L) + Vn)
                kn = (Hn, vkey(cfg, cls, Vn), Ln)
                if kn not in nxt:
                    nxt.add(kn)
                    if keep_paths and kn not in parent:
                        parent[kn] = (key, vr)
        level = nxt
        hits = []
        for key in level:
            for (lab, d, rec) in final_check(cfg, cls, key, None):
                hits.append((lab, d, rec, key))
        per_k[k] = (len(level), hits)
    return per_k, parent


def configs(n, mode):
    if mode == "relaxed":
        for porient in ("A", "B"):
            Qc, Pc = (1, n + 1) if porient == "A" else (n + 1, 1)
            for classes in product("VHab", repeat=n - 2):
                vis = [Qc]
                for x, cl in zip(range(2, n), classes):
                    if cl == "V":
                        vis += [x, n + x]
                    elif cl == "a":
                        vis += [x]
                    elif cl == "b":
                        vis += [n + x]
                yield (f"ptr{porient}:Q={'u1' if porient=='A' else 'v1'},P={'v1' if porient=='A' else 'u1'};sites2..={''.join(classes)}",
                       vis, Qc, Pc)
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
                    yield (f"Q={'u1' if Qc==1 else 'v1'},P={'u2' if Pc==2 else 'v2'};site1=V,site2=H;sites3..={''.join(classes)}",
                           vis, Qc, Pc)


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    modes = sys.argv[2].split(",") if len(sys.argv) > 2 else ["strict", "relaxed"]
    classes = sys.argv[3].split(",") if len(sys.argv) > 3 else ["none", "cell", "GL"]
    nmin = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    GLMAX = 4
    CELLMAX = 6
    t0 = time.time()
    for mode in modes:
        for n in range(nmin, nmax + 1):
            for cls in classes:
                ncfg = 0
                skipped = 0
                tally = {}
                examples = {}
                maxlev = 0
                for edges in all_graphs(n):
                    for (lab, vis, Qc, Pc) in configs(n, mode):
                        cfg = Cfg(n, edges, vis, Qc, Pc, lab)
                        if (cls == "GL" and cfg.dv > GLMAX) or (cls == "cell" and cfg.dv > CELLMAX):
                            skipped += 1
                            continue
                        ncfg += 1
                        per_k, _ = run_cfg(cfg, cls)
                        for k in range(1, KMAX + 1):
                            sz, hits = per_k[k]
                            maxlev = max(maxlev, sz)
                            best = {}
                            for (tl, d, rec, key) in hits:
                                cat = d + "/" + rec
                                best[cat] = best.get(cat, 0) + 1
                            for cat in best:
                                tally[(k, cat)] = tally.get((k, cat), 0) + 1
                                ex = examples.setdefault((k, cat), [])
                                if len(ex) < 3:
                                    tl = next(h[0] for h in hits if h[1] + "/" + h[2] == cat)
                                    ex.append((edges, lab, tl))
                print(f"[{mode}] n={n} ops={cls}: configurations searched={ncfg} skipped(dim)={skipped} max classes/level={maxlev}")
                for k in range(1, KMAX + 1):
                    cats = sorted(c for (kk, c) in tally if kk == k)
                    s = ", ".join(f"{c}:{tally[(k, c)]}" for c in cats) or "no designated match"
                    print(f"    k={k}: configurations with a designated match by category: {s}")
                for (k, cat), ex in sorted(examples.items()):
                    if cat.split("/")[0] in ("E", "AV"):
                        for e in ex[:2]:
                            print(f"      example k={k} {cat}: edges={e[0]} {e[1]} target {e[2]}")
                sys.stdout.flush()
    print(f"elapsed {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
